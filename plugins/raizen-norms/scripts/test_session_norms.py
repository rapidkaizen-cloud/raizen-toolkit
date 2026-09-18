#!/usr/bin/env python3
"""Self-check session_norms.py: the two listings, and that they stay quiet.

Components are found by folder name; the data layer is read from the `Data layer` row
of the app's CLAUDE.md. The quiet cases come first on purpose. Both listings are paid
for in every session of every app repo, so a repo with nothing to list must add
nothing — a listing that appears where it should not costs more than one that is missing.
Run directly: python3 test_session_norms.py
"""
import json
import subprocess
import tempfile
from pathlib import Path

SCRIPT = Path(__file__).parent / "session_norms.py"
MARK = "Components already in this repo"
DATA_MARK = "Data layer of this repo"

# `python3`, not sys.executable: this is the interpreter name hooks.json invokes, so a
# machine where only `python` resolves must fail here rather than pass a test whose
# subject never runs. The failure is the point.
PYTHON = "python3"


def run(root: Path) -> str:
    result = subprocess.run(
        [PYTHON, str(SCRIPT)],
        input=json.dumps({"cwd": str(root)}),
        capture_output=True,
        text=True,
        encoding="utf-8",
    )
    assert result.returncode == 0, result.stderr
    return result.stdout


def write(root: Path, rel: str, text: str = "") -> None:
    path = root / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def demo() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)

        # quiet: an empty repo gets the norms and nothing else
        out = run(root)
        assert "SESSION NORMS" in out
        assert MARK not in out

        # quiet: a repo with code but no components folder
        write(root, "src/lib/date.ts", "export const Format = 1\n")
        write(root, "PRD.md", "# PRD - Demo\n")
        out = run(root)
        assert "# PRD - Demo" in out
        assert MARK not in out

        # quiet: components that live only where nobody should be sent looking
        write(root, "node_modules/lib/components/Thing.tsx", "export function Thing() {}\n")
        write(root, "src/design-canvas/components/Draft.tsx", "export function Draft() {}\n")
        write(root, ".next/components/Built.tsx", "export function Built() {}\n")
        assert MARK not in run(root)

        # listed: the one shared file, by its exported names — capitalised only, so a
        # variants helper or a hook does not read as a component
        write(
            root,
            "src/components/ui.tsx",
            "export function Button() {}\n"
            "export const Pager = () => null\n"
            "export const buttonVariants = {}\n"
            "export const PAGE_SIZES = [10, 50]\n"
            "export function usePager() {}\n",
        )
        # listed: the copy-in library shape, names exported in one trailing brace
        write(
            root,
            "src/components/ui/dialog.tsx",
            "function Dialog() {}\nfunction DialogTrigger() {}\n"
            "export { Dialog, DialogTrigger as Trigger, dialogVariants }\n",
        )
        # listed: a feature-local folder, which is where duplicates hide
        write(root, "src/features/leads/components/LeadCard.tsx", "export default function LeadCard() {}\n")
        # listed by file name: a single-file component format
        write(root, "src/components/StatusChip.vue", "<template/>\n")
        # not listed: tests and stories sitting beside the components
        write(root, "src/components/ui.test.tsx", "export function Fake() {}\n")
        write(root, "src/components/ui.stories.tsx", "export function Story() {}\n")

        out = run(root)
        assert MARK in out
        assert "src/components/ui.tsx: Button, Pager" in out
        assert "buttonVariants" not in out and "usePager" not in out and "PAGE_SIZES" not in out
        assert "src/components/ui/dialog.tsx: Dialog, Trigger" in out
        assert "src/features/leads/components/LeadCard.tsx: LeadCard" in out
        assert "src/components/StatusChip.vue: StatusChip" in out
        assert "Fake" not in out and "Story" not in out
        assert "Thing" not in out and "Draft" not in out and "Built" not in out
        # the inventory comes last, after the documents it must not push out of view
        assert out.index("# PRD - Demo") < out.index(MARK)

    # native surfaces: the platform axis has broken quietly three times already
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        write(root, "lib/widgets/pager.dart", "class Pager extends StatelessWidget {}\nclass _State {}\n")
        write(
            root,
            "app/src/main/java/ui/components/Chips.kt",
            "@Composable\nfun StatusChip() {}\n\n@Composable\nprivate fun Dot() {}\n\nfun helper() {}\n",
        )
        write(root, "App/Components/Badge.swift", "struct Badge: View {}\nstruct Model: Codable {}\n")
        out = run(root)
        assert "lib/widgets/pager.dart: Pager" in out
        assert "Chips.kt: StatusChip, Dot" in out and "helper" not in out
        assert "Badge.swift: Badge" in out and "Model" not in out

    # capped: a large app gets the shallowest files and a count, never the whole tree
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        for i in range(90):
            write(root, f"src/components/deep/nested/C{i:02}.tsx", f"export function C{i:02}() {{}}\n")
        write(root, "src/components/Shell.tsx", "export function Shell() {}\n")
        out = run(root)
        assert "src/components/Shell.tsx: Shell" in out
        assert "31 more" in out
        assert "C89" not in out

    # the data layer: read from the row `logic-settle` writes, never guessed from a name —
    # `lib`, `services`, `data`, and `api` all occur, and `lib` holds far more than queries
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        stack = "## Stack\n\n| Aspect | Choice |\n|---|---|\n| Database | Supabase |\n"

        # quiet: code that calls the database, but no app file declaring where it lives
        write(root, "src/lib/leads.ts", "export async function getLeads() {}\n")
        assert DATA_MARK not in run(root)

        # quiet: a Stack table with no Data layer row — nobody settled it yet
        write(root, "CLAUDE.md", stack)
        assert DATA_MARK not in run(root)

        # said out loud: a row pointing at a folder that is not there is a stale pointer,
        # and the lint floor's globs are wrong in the same way
        write(root, "CLAUDE.md", stack + "| Data layer | `src/data` — every database call |\n")
        out = run(root)
        assert DATA_MARK not in out
        assert "Data layer row" in out and "src/data" in out

        # listed: functions by name; types, constants, and tests are not functions to call
        write(root, "CLAUDE.md", stack + "| Data layer | `src/lib` — every database call |\n")
        write(
            root,
            "src/lib/leads.ts",
            "export type Lead = {}\nexport interface Row {}\n"
            "export const PAGE_SIZE = 50\n"
            "export async function getLeads() {}\n"
            "export const approveLead = async () => {}\n"
            "function internal() {}\nexport { internal as archiveLead }\n",
        )
        write(root, "src/lib/leads.test.ts", "export function fake() {}\n")
        write(root, "src/lib/many.ts", "".join(f"export function fn{i:02}() {{}}\n" for i in range(20)))
        out = run(root)
        assert DATA_MARK in out and "src/lib" in out
        assert "src/lib/leads.ts: getLeads, approveLead, archiveLead" in out
        assert " Lead," not in out and " Row" not in out and "PAGE_SIZE" not in out
        assert "fake" not in out
        assert "fn11, +8" in out and "fn12" not in out

        # a path that climbs out of the repo is not followed
        write(root, "CLAUDE.md", stack + "| Data layer | `../outside` |\n")
        assert DATA_MARK not in run(root)

    print("ok")


if __name__ == "__main__":
    demo()
