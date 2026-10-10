#!/usr/bin/env python3
"""Self-check audit_count.py: what it counts, what it leaves alone, and what it writes.

The first cases are the ones that must not be counted - a token file, a selector that looks
like a colour, a reset, a class that reads a token - because a count that is too high prices
a pass that is not owed.
Run directly: python3 test_audit_count.py
"""
import subprocess
import tempfile
from pathlib import Path

SCRIPT = Path(__file__).parent / "audit_count.py"
# `python3`, not sys.executable: the name the brief tells a subagent to run.
PYTHON = "python3"

FILES = {
    "package.json": '{"dependencies": {"lucide-react": "1", "left-pad": "1", "tailwindcss": "3"}}',
    # A styling file: every value in it is a definition. `--bg` is read by its own rule, `--fg` by
    # card.css, `--primary` by a class, `--radius` only inside another token; nothing reads the last two.
    "src/app.css": (":root {\n  --bg: #ffffff;\n  --fg: #111111;\n  --radius: 8px;\n  --primary: #2563eb;\n"
                    "  --card: #ffffff;\n  --radius-lg: calc(var(--radius) + 2px);\n}\n"
                    "body { background: var(--bg); font-size: 14px; }\n"),
    # Not a styling file: `#add` is a selector, the colour after the colon is a stray.
    "src/card.css": "#add { color: #ff0000; margin: 0; padding: 12px; border-color: var(--fg); }\n",
    "src/pages/Sales/Index.tsx": (
        'import { Plus } from "lucide-react";\n'
        'export const A = () => <div className="bg-primary text-foreground p-4 text-sm">\n'      # reads tokens
        '  <b className="text-[13px] p-[7px] bg-blue-500 hover:text-gray-600/50">x</b>\n'        # four strays
        '  <i style={{ color: "#0af", fontSize: 12, marginTop: 6 }} />\n'                        # three strays
        '  <Plus className="h-4 w-4" strokeWidth={1.5} /><Plus size={20} />\n'                   # two icons
        '  <button title="Save invoice">Save invoice</button>{t("Delete this sales invoice now")}\n'
        '  {t("sales.empty_title")}\n'                                                           # a key, no label
        "</div>;\n"),
    "src/pages/Other/Index.tsx": 'export const B = () => <a href="#section" className="m-0">ok</a>;\n',
    "dist/bundle.js": 'const c = "#123456";\n',
}


def run(root: Path, *extra: str) -> str:
    done = subprocess.run([PYTHON, str(SCRIPT), str(root), *extra], capture_output=True, text=True, encoding="utf-8")
    assert done.returncode == 0, done.stderr
    return done.stdout


def main() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        for rel, text in FILES.items():
            (root / rel).parent.mkdir(parents=True, exist_ok=True)
            (root / rel).write_text(text, encoding="utf-8")
        out = run(root, "--scope", "src/pages/Sales", "--out", str(root / ".design-audit"))
        whole = next(line for line in out.splitlines() if "whole app" in line)
        scope = next(line for line in out.splitlines() if "scope     " in line)

        # Must not be counted: the token file, the selector, the reset, the token classes, the build folder.
        assert "src/app.css" in next(line for line in out.splitlines() if line.startswith("Styling files"))
        places = (root / ".design-audit" / "places.md").read_text(encoding="utf-8")
        for absent in ("app.css", "#add", "margin: 0", "bg-primary", "p-4", "Other/Index.tsx", "bundle.js"):
            assert absent not in places, absent

        # Must be counted, each once.
        assert "hex 2 in 2 files" in whole, whole                       # card.css, Index.tsx
        assert "font sizes 2 in 1 files" in whole, whole                # text-[13px], fontSize: 12
        assert "spacings 3 in 2 files" in whole, whole                  # padding: 12px, p-[7px], marginTop: 6
        assert "numbered ramp classes 2 in 1 files" in whole, whole     # bg-blue-500, text-gray-600/50
        assert "hex 1 in 1 files" in scope and "spacings 2 in 1 files" in scope, scope
        assert "Components affected : 2 files" in out and "scope 1" in out, out
        assert "src/pages/Sales/Index.tsx:3 · text-[13px] · Stray raw values — font sizes" in places, places

        assert "Icon families       : lucide-react 1" in out, out
        never = next(line for line in out.splitlines() if line.startswith("Never imported"))
        assert "left-pad" in never and "lucide-react" not in never, never

        # A token is never read only where no var(), no class and no other token reaches it.
        health = next(line for line in out.splitlines() if line.startswith("Token health"))
        assert "6 tokens defined · never read 2 (card · radius-lg)" in health, health
        assert "maps it 1 (radius)" in health and "`:root` 1 groups holding 2 of 4 colours" in health, health
        sizes = next(line for line in out.splitlines() if line.startswith("Icon sizes"))
        assert "2 icon elements in 1 files · 2 sizes — 4 ×1 · 20px ×1 · weights set — 1.5 ×1" in sizes, sizes
        labels = next(line for line in out.splitlines() if line.startswith("Repeated labels"))
        assert "4 strings in 1 files of the scope · longest 5 words" in labels and "median 2 ·" in labels, labels
        assert "Sales/Index.tsx 1 labels in 2 places · 1 translation keys left out" in labels, labels

        # No Tailwind, no ramp row and no class read; a stack with no web source says so.
        (root / "package.json").write_text('{"dependencies": {}}', encoding="utf-8")
        bare = run(root)
        assert "never read 3 (card · primary · radius-lg)" in bare and "a read is a var() only" in bare, bare
        assert "numbered ramp classes not counted" in bare
        with tempfile.TemporaryDirectory() as empty:
            assert "NOT COVERED" in run(Path(empty))
    print("audit_count: ok")


if __name__ == "__main__":
    main()
