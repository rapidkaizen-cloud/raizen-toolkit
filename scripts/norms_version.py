#!/usr/bin/env python3
"""Print which raizen-norms this copy is, when it reached this machine, and what changed.

The `norms-version` skill runs this from the plugin folder it was read from, so the
answer is about the copy the session runs: a machine keeps one folder per installed
version, and the newest of them is not always the one a session loaded.

Origin is its changelog alone, read over HTTPS from the public repo - no clone, no
login. Its top heading is the newest version, because CLAUDE.md makes every version bump
write its entry. A machine that cannot reach it still gets its own lines.

Usage: python3 norms_version.py [entries]
"""
import json
import re
import sys
import urllib.request
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MANIFEST = ".claude-plugin/plugin.json"
CHANGELOG = "CHANGELOG.md"
ORIGIN = "https://raw.githubusercontent.com/rapidkaizen-cloud/raizen-toolkit/master/"
HEADING = re.compile(r"^## \[(.+?)\] - (\S+)[ \t]*$", re.M)
# Until 0.70.0 a heading may name `raizen-hub`, alone or beside this plugin.
OWN = re.compile(r"\braizen-norms (\d+(?:\.\d+)*)")


def fetch(name: str) -> str:
    with urllib.request.urlopen(ORIGIN + name, timeout=10) as response:
        return response.read().decode("utf-8", errors="replace")


def entries(changelog: str) -> list:
    """Every entry, newest first as the file is: (raizen-norms version or "", date, text)."""
    marks = list(HEADING.finditer(changelog))
    ends = [mark.start() for mark in marks[1:]] + [len(changelog)]
    found = []
    for mark, end in zip(marks, ends):
        own = OWN.search(mark[1])
        found.append((own[1] if own else "", mark[2], changelog[mark.start():end].strip()))
    return found


def newer(found: list, version: str) -> list:
    """The entries above this version's own. By position, not by number: the old headings
    interleave two plugins' version lines, and no comparison orders those."""
    for i, (own, _, _) in enumerate(found):
        if own == version:
            return found[:i]
    return found


def number(version: str) -> tuple:
    return tuple(int(part) for part in version.split("."))


def report(root: Path, fetch=fetch, count: int = 1) -> str:
    manifest = root / MANIFEST
    version = json.loads(manifest.read_text(encoding="utf-8"))["version"]
    try:
        local = entries((root / CHANGELOG).read_text(encoding="utf-8", errors="replace"))
    except OSError:
        local = []
    released = next((date for own, date, _ in local if own == version), "no entry in this copy's CHANGELOG.md")

    missing = []
    try:
        origin = entries(fetch(CHANGELOG))
        latest = next(own for own, _, _ in origin if own)
        missing = newer(origin, version)
        if not missing:
            state = f"{latest} - this copy is current"
        elif number(version) > number(latest):
            missing = []
            state = f"{latest} - this copy is ahead, not published yet"
        else:
            state = f"{latest} - this copy is behind, {len(missing)} newer"
    except Exception as error:
        state = f"not reachable - {error}"

    since = datetime.fromtimestamp(manifest.stat().st_mtime).strftime("%Y-%m-%d %H:%M")
    out = [
        f"raizen-norms {version}",
        f"  Released        : {released}",
        f"  On this machine : since {since}",
        f"  Read from       : {root}",
        f"  Origin          : {state}",
    ]
    if missing:
        out += ["", "Not on this machine yet:", ""] + [text + "\n" for _, _, text in missing]
    if local:
        out += ["", "In this copy:", ""] + [text + "\n" for _, _, text in local[:count]]
    return "\n".join(out).rstrip() + "\n"


def main() -> None:
    # On Windows stdout defaults to the ANSI codepage, which mangles the changelog's dashes.
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass
    count = int(sys.argv[1]) if len(sys.argv) > 1 else 1
    sys.stdout.write(report(ROOT, count=count))


if __name__ == "__main__":
    main()
