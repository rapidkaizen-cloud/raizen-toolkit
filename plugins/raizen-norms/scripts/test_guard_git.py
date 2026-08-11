#!/usr/bin/env python3
"""Self-check guard_git.py: what is refused, what is asked, what passes.

The three outcomes are distinct and a regression turns one into another silently,
so each is asserted on both the exit code and the presence of the ask payload.
Run directly: python3 test_guard_git.py
"""
import json
import subprocess
from pathlib import Path

GUARD = Path(__file__).parent / "guard_git.py"

# `python3`, not sys.executable: this is the interpreter name hooks.json invokes, so a
# machine where only `python` resolves must fail here rather than pass a test whose
# subject never runs. The failure is the point.
PYTHON = "python3"


def run(command: str) -> tuple:
    payload = json.dumps({"tool_name": "Bash", "tool_input": {"command": command}})
    result = subprocess.run(
        [PYTHON, str(GUARD)], input=payload, capture_output=True, text=True
    )
    decision = ""
    if result.stdout.strip():
        out = json.loads(result.stdout)
        decision = out["hookSpecificOutput"]["permissionDecision"]
    return result.returncode, decision


def demo() -> None:
    # refused outright
    assert run("git add -A") == (2, "")
    assert run("git add .") == (2, "")
    assert run("git push --force origin dev") == (2, "")
    assert run("git push --force-with-lease") == (2, "")

    # a global option between `git` and the subcommand must not shake the guard off
    assert run("git -c core.hooksPath=/dev/null push --force origin dev") == (2, "")
    assert run("git -C . add -A") == (2, "")
    assert run("git --no-pager push origin development") == (0, "ask")

    # force with no flag to grep for: the leading + on the refspec
    assert run("git push origin +main") == (2, "")
    assert run("git push origin +refs/heads/dev:refs/heads/dev") == (2, "")

    # a + inside a branch name is not a force
    assert run("git push origin feature+search") == (0, "ask")

    # handed to the user — a session never publishes on its own
    assert run("git push origin development") == (0, "ask")
    assert run("gh pr create --fill") == (0, "ask")
    assert run("gh pr merge 12 --squash") == (0, "ask")

    # auto-commit must not be slowed down by the guard.
    # Run this from a branch other than main — the commit assertion reads the real
    # HEAD, and on main the guard is supposed to refuse.
    assert run("git commit -m 'add page' -- src/app/orders/page.tsx") == (0, "")
    assert run("git status --porcelain") == (0, "")
    assert run("git fetch") == (0, "")

    # unrelated commands are none of this guard's business
    assert run("npm run dev") == (0, "")
    assert run("gh release list") == (0, "")

    print("ok")


if __name__ == "__main__":
    demo()
