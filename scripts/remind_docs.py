#!/usr/bin/env python3
"""After a commit that touched no document, ask the session whether one became false.

PostToolUse hook on the shell tools, on Claude Code. On Antigravity a hook that runs
after a tool cannot hand the model text, so `session_norms.py` asks through `unasked`
before the next model call instead. It never blocks. Most commits owe no document, and a
hook cannot tell which do - so it asks, at the one moment the same-commit rule can still
be met by an amend, and takes "none" for an answer.

Silent unless all hold: the project keeps documents (`docs/PRD.md`, or a root `PRD.md`),
HEAD is a commit just made, and nothing it changed is a document. On Claude Code the
command must have run a `git commit`; on Antigravity the commit must not have been asked
about already.
"""
import json
import re
import subprocess
import sys
import time
from pathlib import Path

import guard_git
import host

# Documents kept at the root, in either form; everything under `docs/` is one too.
DOCUMENTS = ("PRD.md", "QUEUE.md", "DESIGN.md", "README.md")

# PostToolUse fires when the command exits 0, and `git commit ...; git status` exits 0
# with nothing committed. HEAD is taken as this command's commit only while it is fresh.
# ponytail: a clock, not the command's output; read `tool_response` if a stale HEAD is
# ever asked about.
FRESH_SECONDS = 300

# Opens the reminder, the commit's short hash after it: what `unasked` looks for.
MARK = "DOCS CHECK - commit "

DOCS_FORM = (
    "  - Did a sentence in `docs/product.md`, `docs/rules.md`, `docs/glossary.md` or "
    "`README.md` become false?\n"
    "  - Did a page become usable to its role with no `docs/guide/` page for its task, or "
    "with its `docs/queue.md` line still standing?\n"
    "  - Will users notice it? Then it owes a `docs/whats-new.md` entry.\n"
)
LEGACY_FORM = (
    "  - Did a sentence in `PRD.md` become false?\n"
    "  - Did it finish a `QUEUE.md` line that is still standing?\n"
)


def git(*args: str) -> str:
    try:
        out = subprocess.run(["git", *args], capture_output=True, text=True, timeout=10)
    except Exception:
        return ""
    return out.stdout.strip() if out.returncode == 0 else ""


def reminder() -> str:
    """The text for HEAD, or an empty string when HEAD owes no question."""
    # The project directory, as `session_norms` reads the form from it - and no git call
    # at all in a folder that keeps no documents, which on Antigravity is every model call.
    if Path("docs", "PRD.md").is_file():
        questions = DOCS_FORM
    elif Path("PRD.md").is_file():
        questions = LEGACY_FORM
    else:
        return ""  # never settled: no document here to keep true
    stamp = git("log", "-1", "--format=%ct")
    if not stamp.isdigit() or time.time() - int(stamp) > FRESH_SECONDS:
        return ""
    # A merge lists nothing here, and owes nothing its parents did not.
    files = [f for f in git("show", "--name-only", "--format=", "HEAD").splitlines() if f]
    if not files or any(f.startswith("docs/") or f in DOCUMENTS for f in files):
        return ""
    return (
        f"{MARK}{git('rev-parse', '--short', 'HEAD')} changed {len(files)} "
        "file(s) and no document.\n"
        "A commit that makes a document false carries its correction (`docs-format`, Same "
        "commit). Answer for this commit before the next step:\n"
        + questions
        + "Any yes -> write it and amend it into this commit while it is unpushed. All no -> "
        "carry on, and report `Docs: none` for this commit at the close. Write nothing a "
        "live check of the code can recover."
    )


def unasked(transcript: str) -> str:
    """`reminder`, for a host that can only speak before a model call: empty once the
    transcript shows this commit was asked about."""
    text = reminder()
    if not text:
        return ""
    mark = text.split(" changed ", 1)[0]
    try:
        with open(transcript, encoding="utf-8", errors="replace") as f:
            asked = any(mark in line for line in f)
    except OSError:
        return ""  # nothing remembers what was asked: silence, not a question before every call
    return "" if asked else text


def main() -> None:
    tool_input = host.read_payload().get("tool_input")
    cmd = str(tool_input.get("command") or "") if isinstance(tool_input, dict) else ""
    code = guard_git.QUOTED.sub("''", guard_git.HEREDOC.sub(r"\1", cmd))
    if not re.search(guard_git.GIT + r"commit\b", code):
        sys.exit(0)
    text = reminder()
    if text:
        # Plain stdout from this event goes to a debug log; only this shape reaches the model.
        json.dump({"hookSpecificOutput": {"hookEventName": "PostToolUse", "additionalContext": text}}, sys.stdout)
    sys.exit(0)


if __name__ == "__main__":
    main()
