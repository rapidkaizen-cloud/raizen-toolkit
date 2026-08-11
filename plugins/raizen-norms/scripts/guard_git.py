#!/usr/bin/env python3
"""Guard git operations: block what must never happen, ask before publishing.

Reads the hook payload from stdin.
Exit 0 = pass, exit 2 = block (the agent reads stderr).
A JSON payload on stdout with permissionDecision "ask" hands the call to the user.

Blocked:
  - commit while HEAD is on main
  - git add -A / git add .  (a commit holds explicit paths from SCOPE)
  - push --force / -f, and the flagless force spelled as a refspec: push origin +main

Asked:
  - git push
  - gh pr create / gh pr merge

A session commits on its own; it never publishes on its own. Asking rather than
refusing is deliberate: a refusal would also hit the push the user just asked for,
and the answer to the prompt is exactly the instruction the norm requires.
"""
import json
import re
import subprocess
import sys

# Global options are allowed to sit between `git` and its subcommand: `git -c k=v push`,
# `git -C dir commit`, `git --no-pager add`. Anchoring on `git push` alone reads only the
# bare spelling, and the long way round walks past every rule below. `-c`/`-C` take a
# separate argument, so they need their own alternative.
GIT = r"\bgit\s+(?:-[cC]\s+\S+\s+|--?[\w-]+(?:=\S+)?\s+)*"


def read_command() -> str:
    try:
        payload = json.load(sys.stdin)
    except Exception:
        return ""
    ti = payload.get("tool_input") or {}
    return ti.get("command") or ""


def head_branch() -> str:
    try:
        out = subprocess.run(
            ["git", "rev-parse", "--abbrev-ref", "HEAD"],
            capture_output=True, text=True, timeout=5,
        )
        return out.stdout.strip()
    except Exception:
        return ""


def block(msg: str) -> None:
    sys.stderr.write(msg + "\n")
    sys.exit(2)


def ask(reason: str) -> None:
    json.dump(
        {
            "hookSpecificOutput": {
                "hookEventName": "PreToolUse",
                "permissionDecision": "ask",
                "permissionDecisionReason": reason,
            }
        },
        sys.stdout,
    )
    sys.exit(0)


def main() -> None:
    cmd = read_command()
    if not re.search(r"\b(git|gh)\b", cmd):
        sys.exit(0)

    if re.search(GIT + r"add\s+(-A\b|--all\b|\.(\s|$))", cmd):
        block(
            "REFUSED: git add -A / git add . is not used in this repo.\n"
            "A commit contains only paths that are in SCOPE, named explicitly.\n"
            "Files changed outside SCOPE are findings reported to the user, "
            "not things to commit along."
        )

    # `\s\+\S` is `push origin +main` — a force with no flag to grep for.
    if re.search(GIT + r"push\b.*(--force\b|--force-with-lease\b|\s-f\b|\s\+\S)", cmd):
        block(
            "REFUSED: a force push is never run from a session. "
            "If a PR flow needs one, the user runs it."
        )

    if re.search(GIT + r"commit\b", cmd):
        branch = head_branch()
        if branch == "main":
            block(
                "REFUSED: HEAD is on main. A session never works on main.\n"
                "Switch to development first, then retry."
            )

    if re.search(r"\bgh\s+pr\s+(create|merge)\b", cmd):
        ask(
            "A pull request is opened or merged only on the user's word. "
            "Approve only if you asked for this."
        )

    if re.search(GIT + r"push\b", cmd):
        ask(
            "A session commits on its own but never publishes on its own. "
            "Approve only if you asked for this push."
        )

    sys.exit(0)


if __name__ == "__main__":
    main()
