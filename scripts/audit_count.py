#!/usr/bin/env python3
"""Count what a UI's source holds outside its tokens, for `design-settle`'s audit.

The audit's first subagent runs this once (`skills/design-settle/references/audit.md`) and
copies what it prints. Counted by hand, two audits of one app read the same rows two ways:
the files a token change touches came out as 793 and as 616. A script counts them one way.

It reads the files git tracks or does not ignore, line by line, and writes nothing but the
`places.md` it is told to write. A styling file - one that defines custom properties, or a
Tailwind config - is where values are defined, so nothing in it is counted.

Usage: python3 audit_count.py <repo root> [--scope PATH ...] [--src PATH ...]
                              [--styles PATH ...] [--out DIR]
"""
import argparse
import json
import re
import subprocess
import sys
from collections import Counter
from pathlib import Path

SOURCE = (".tsx", ".jsx", ".ts", ".js", ".mjs", ".vue", ".svelte", ".astro", ".html", ".blade.php")
CSS = (".css", ".scss", ".less")
# Build output, vendored code and this skill's own folders: never an app's source.
SKIP_DIRS = {"node_modules", "vendor", "dist", "build", "out", "coverage", "storage", "public",
             ".next", ".nuxt", ".svelte-kit", ".git", ".design-audit", "design-canvas"}
MAX_BYTES = 1_500_000
MINIFIED_LINE = 2_000

HEX = re.compile(r"(?<![\w&#/])#(?:[0-9a-fA-F]{8}|[0-9a-fA-F]{6}|[0-9a-fA-F]{3,4})(?![\w-])")
PALETTE = ("slate|gray|zinc|neutral|stone|red|orange|amber|yellow|lime|green|emerald|teal|cyan|sky|"
           "blue|indigo|violet|purple|fuchsia|pink|rose")
KINDS = [
    ("hex", [HEX]),
    ("colour functions", [re.compile(r"\b(?:rgba?|hsla?)\(\s*\d[^)]*\)")]),
    ("font sizes", [re.compile(r"(?<![\w-])text-\[\d[^\]\s]*\]"),
                    re.compile(r"\bfont-size\s*:\s*\d[\w.%]*"),
                    re.compile(r"\bfontSize\s*:\s*['\"]?\d[\w.%]*")]),
    ("spacings", [re.compile(r"(?<![\w-])-?(?:p[xytrblse]?|m[xytrblse]?|gap(?:-[xy])?|space-[xy]|"
                             r"inset(?:-[xy])?|top|right|bottom|left)-\[\d[^\]\s]*\]"),
                  # `margin: 0` is a reset, not a value outside the scale.
                  re.compile(r"\b(?:padding|margin|gap)(?:-[a-z]+|[A-Z][A-Za-z]*)*\s*:\s*['\"]?"
                             r"-?(?:[1-9]|0?\.\d)[\w.%]*")]),
]
RAMP = ("numbered ramp classes", [re.compile(
    r"(?<![\w-])(?:bg|text|border(?:-[trblxyse])?|ring(?:-offset)?|fill|stroke|from|via|to|divide|"
    r"outline|decoration|placeholder|caret|accent|shadow)-(?:" + PALETTE + r")-(?:50|[1-9]00|950)(?![\w-])")])
IMPORT = re.compile(r"(?:\bfrom\s+|\brequire\(\s*|\bimport\s*\(?\s*|@import\s+)['\"]([^'\"./][^'\"]*)['\"]")
ICONS = re.compile(r"lucide|heroicons|react-icons|phosphor|tabler|feather|fontawesome|iconify|ionicons|"
                   r"bootstrap-icons|remixicon|material-icons|@mui/icons|react-icons|/icons?$|-icons?$")
TOKEN_DEF = re.compile(r"^\s*--[\w-]+\s*:", re.M)
FONT_FAMILY = re.compile(r"font-family\s*:\s*([^;{}]+)")
FONT_LINK = re.compile(r"<link[^>]+href=[\"']([^\"']*font[^\"']*)[\"']", re.I)


def listed(root: Path) -> list[str]:
    """Every path git tracks or does not ignore; every file under the root where git has none."""
    try:
        out = subprocess.run(["git", "-C", str(root), "ls-files", "-co", "--exclude-standard", "-z"],
                             capture_output=True, timeout=120)
        if out.returncode == 0 and out.stdout:
            return [p for p in out.stdout.decode("utf-8", "replace").split("\0") if p]
    except (OSError, subprocess.SubprocessError):
        pass
    return [p.relative_to(root).as_posix() for p in root.rglob("*") if p.is_file()]


def under(path: str, roots: list[str]) -> bool:
    return any(path == r or path.startswith(r.rstrip("/") + "/") for r in roots)


def package(spec: str) -> str:
    parts = spec.split("/")
    return "/".join(parts[:2]) if spec.startswith("@") else parts[0]


def number(n: int) -> str:
    return f"{n:,}"


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("root")
    ap.add_argument("--scope", nargs="*", default=[], help="paths the run redraws, relative to the root")
    ap.add_argument("--src", nargs="*", default=[], help="count only under these paths")
    ap.add_argument("--styles", nargs="*", default=[], help="styling files, where this script guessed wrong")
    ap.add_argument("--out", help="folder to write places.md into")
    args = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    root = Path(args.root).resolve()
    norm = lambda paths: [Path(p).as_posix().strip("/") for p in paths]
    scope, src, styles_given = norm(args.scope), norm(args.src), norm(args.styles)

    deps, data = {}, {}
    manifest = root / "package.json"
    if manifest.is_file():
        try:
            data = json.loads(manifest.read_text(encoding="utf-8", errors="replace"))
            deps = {**data.get("devDependencies", {}), **data.get("dependencies", {})}
        except ValueError:
            pass
    tailwind = "tailwindcss" in deps or any(root.glob("tailwind.config.*"))
    kinds = KINDS + ([RAMP] if tailwind else [])

    paths = [p for p in listed(root)
             if p.lower().endswith(SOURCE + CSS) and not p.lower().endswith((".min.js", ".min.css", ".d.ts"))
             and not SKIP_DIRS.intersection(p.split("/")[:-1]) and (not src or under(p, src))]
    by_ext, skipped, styling = Counter(), 0, []
    hits = {k: Counter() for k, _ in kinds}            # kind -> file -> occurrences
    places, imports, fonts, links = [], Counter(), Counter(), set()
    for rel in sorted(paths):
        file = root / rel
        try:
            if file.stat().st_size > MAX_BYTES:
                skipped += 1
                continue
            text = file.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
        lines = text.split("\n")
        if any(len(line) > MINIFIED_LINE for line in lines[:5]):
            skipped += 1
            continue
        by_ext[rel[rel.rindex("."):]] += 1
        for name in {package(s) for s in IMPORT.findall(text)}:
            imports[name] += 1
        css = rel.lower().endswith(CSS)
        is_styling = (under(rel, styles_given) if styles_given
                      else Path(rel).name.startswith("tailwind.config.") or (css and len(TOKEN_DEF.findall(text)) >= 3))
        if css:
            fonts.update(" ".join(f.split()) for f in FONT_FAMILY.findall(text))
        links.update(FONT_LINK.findall(text))
        if is_styling:
            styling.append(rel)
            continue
        for no, line in enumerate(lines, 1):
            for kind, patterns in kinds:
                found = [m.group(0) for p in patterns for m in p.finditer(line)
                         # In a stylesheet `#abc {` is a selector: a colour follows a colon.
                         if not (css and p is HEX and ":" not in line[:m.start()])]
                if found:
                    hits[kind][rel] += len(found)
                    places.append(f"{rel}:{no} · {' '.join(found)[:120]} · Stray raw values — {kind}")

    affected = {f for c in hits.values() for f in c}
    def row(pick) -> str:
        return " · ".join(f"{k} {number(sum(n for f, n in hits[k].items() if pick(f)))} in "
                          f"{number(sum(1 for f in hits[k] if pick(f)))} files" for k, _ in kinds)

    print(f"AUDIT COUNT — {root}")
    print("Files read          : " + number(sum(by_ext.values())) + " source files ("
          + " · ".join(f"{e} {number(n)}" for e, n in by_ext.most_common()) + f") · {skipped} skipped as minified or too large")
    print("Styling files       : " + (" · ".join(styling) or "none found") + " — values defined there are not counted")
    print("Stray raw values    : whole app — " + row(lambda f: True))
    if scope:
        print("                      scope     — " + row(lambda f: under(f, scope)))
    if not tailwind:
        print("                      numbered ramp classes not counted — no Tailwind in this repo")
    print(f"Components affected : {number(len(affected))} files hold at least one of the values above"
          + (f" · scope {number(sum(1 for f in affected if under(f, scope)))}" if scope else ""))
    if args.out:
        out = Path(args.out)
        out.mkdir(parents=True, exist_ok=True)
        head = ("# places.md\n\nOne line per place: file and line · what is there · the audit row it falls under. "
                "Written by `audit_count.py` over the whole app.\n\n")
        (out / "places.md").write_text(head + "\n".join(places) + "\n", encoding="utf-8", newline="\n")
        print(f"places.md           : {number(len(places))} lines written to {(out / 'places.md').as_posix()}")
    if deps:
        used = sorted(((n, d) for d, n in imports.items() if d in deps), reverse=True)
        print("Imports             : " + " · ".join(f"{d} {n}" for n, d in used[:25])
              + (f" · and {len(used) - 25} more" if len(used) > 25 else "") + "  (package, files importing it)")
        icons = [f"{d} {n}" for n, d in used if ICONS.search(d)]
        print("Icon families       : " + (" · ".join(icons) or "none imported"))
        config = " ".join(p.read_text(encoding="utf-8", errors="replace") for p in root.iterdir()
                          if p.is_file() and ".config." in p.name)
        scripts = json.dumps(data.get("scripts", {}))
        never = sorted(d for d in deps if d not in imports and d not in config and d.split("/")[-1] not in scripts
                       and not d.startswith("@types/"))
        print("Never imported      : " + (" · ".join(never) or "none")
              + "  (in package.json; no source file, root config file or script names them)")
    if fonts:
        print("Font families named : " + " | ".join(f for f, _ in fonts.most_common(6)))
    if links:
        print("Fonts loaded by link: " + " ".join(sorted(links)))
    if not paths:
        print("NOT COVERED — no web source file found; count this stack by your own commands")
    return 0


if __name__ == "__main__":
    sys.exit(main())
