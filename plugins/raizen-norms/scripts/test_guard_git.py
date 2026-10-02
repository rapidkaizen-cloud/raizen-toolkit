#!/usr/bin/env python3
"""Self-check guard_git.py: what is refused, what is held, what an answer lets through.

The outcomes are distinct and a regression turns one into another silently, so each is
asserted on both the exit code and the word that opens stderr.
Run directly: python3 test_guard_git.py
"""
import json
import subprocess
import tempfile
from pathlib import Path

GUARD = Path(__file__).parent / "guard_git.py"

# `python3`, not sys.executable: this is the interpreter name hooks.json invokes, so a
# machine where only `python` resolves must fail here rather than pass a test whose
# subject never runs. The failure is the point.
PYTHON = "python3"


def run(command: str, transcript: str = "") -> tuple:
    payload = {"tool_name": "Bash", "tool_input": {"command": command}}
    if transcript:
        payload["transcript_path"] = transcript
    result = subprocess.run(
        [PYTHON, str(GUARD)], input=json.dumps(payload), capture_output=True, text=True
    )
    word = result.stderr.split(":", 1)[0] if result.stderr else ""
    return result.returncode, word


def asked(question: str, answer, use_id: str = "ask") -> dict:
    return {
        "type": "user",
        "message": {"role": "user", "content": [{"type": "tool_result", "tool_use_id": use_id, "content": "answered"}]},
        "toolUseResult": {"questions": [{"question": question}], "answers": {question: answer}},
    }


def called(use_id: str, command: str, name: str = "Bash") -> dict:
    return {
        "type": "assistant",
        "message": {"role": "assistant", "content": [{"type": "tool_use", "id": use_id, "name": name, "input": {"command": command}}]},
    }


def ran(use_id: str) -> dict:
    return {"type": "user", "message": {"role": "user", "content": [{"type": "tool_result", "tool_use_id": use_id, "content": "done"}]}}


def demo() -> None:
    refused, held, passed = (2, "REFUSED"), (2, "HELD"), (0, "")

    # refused outright, and fixed by the agent without the user
    assert run("git add -A") == refused
    assert run("git add .") == refused
    assert run("git push --force origin dev") == refused
    assert run("git push -f origin dev") == refused

    # a global option between `git` and the subcommand must not shake the guard off
    assert run("git -c core.hooksPath=/dev/null push --force origin dev") == refused
    assert run("git -C . add -A") == refused
    assert run("git --no-pager push origin development") == held

    # force with no flag to grep for: the leading + on the refspec
    assert run("git push origin +main") == refused
    assert run("git push origin +refs/heads/dev:refs/heads/dev") == refused

    # a + inside a branch name is not a force; the lease is a push like any other
    assert run("git push origin feature+search") == held
    assert run("git push --force-with-lease") == held

    # held without an answer
    assert run("git push origin development") == held
    assert run("gh pr create --fill") == held
    assert run("gh pr merge 12 --squash") == held

    with tempfile.TemporaryDirectory() as tmp:
        def transcript(*lines) -> str:
            path = Path(tmp) / f"t{len(list(Path(tmp).iterdir()))}.jsonl"
            path.write_text("\n".join(json.dumps(x) for x in lines) + "\nnot json\n", encoding="utf-8")
            return str(path)

        push = "git push origin development"
        yes = transcript(asked(f"Run `{push}`?", ["Run"]))

        # the answer lets exactly that command through, whitespace aside
        assert run(push, yes) == passed
        assert run("git  push  origin development", yes) == passed
        assert run("git push origin main", yes) == held

        # the commits listed under the command do not hide it
        listed = f"Run `{push}`?\n- 4cc1af0 feat: push waits for `Run`\n- e2bd00d docs: README"
        assert run(push, transcript(asked(listed, ["Run"]))) == passed

        # the call being checked is already written, not yet answered: not spent
        assert run(push, transcript(asked(f"Run `{push}`?", ["Run"]), called("t1", push))) == passed

        # spent by a run; a new answer grants one more
        spent = [asked(f"Run `{push}`?", ["Run"]), called("t1", push), ran("t1")]
        assert run(push, transcript(*spent)) == held
        assert run(push, transcript(*spent, asked(f"Once more: `{push}`?", ["Run"]))) == passed

        # a run before the answer spends nothing; another command's run spends nothing
        assert run(push, transcript(called("t0", push), ran("t0"), asked(f"`{push}`?", ["Run"]))) == passed
        assert run(push, transcript(asked(f"`{push}`?", ["Run"]), called("t1", "git status"), ran("t1"))) == passed
        assert run(push, transcript(asked(f"`{push}`?", ["Run"]), called("t1", push, "PowerShell"), ran("t1"))) == held

        # anything but the exact label, or a question that does not name the command, is no answer
        assert run(push, transcript(asked(f"Run `{push}`?", ["Cancel"]))) == held
        assert run(push, transcript(asked(f"Run `{push}`?", "Run it"))) == held
        assert run(push, transcript(asked("Push to development?", ["Run"]))) == held
        assert run(push, str(Path(tmp) / "missing.jsonl")) == held

        # the lease and pull requests go through the same answer; a bare force never does
        lease = "git push --force-with-lease=master:90aa7fc origin master"
        assert run(lease, transcript(asked(f"Force push: `{lease}`", "Run"))) == passed
        bare = "git push --force origin master"
        assert run(bare, transcript(asked(f"`{bare}`", ["Run"]))) == refused
        pr = "gh pr create --fill"
        assert run(pr, transcript(asked(f"Open it: `{pr}`", ["Run"]))) == passed

    # a message that mentions a held or refused command is data, not a call
    assert run('git commit -m "docs: gh pr create and git push --force are held"') == passed
    assert run("git commit -F - <<'EOF'\nfeat: never git add -A, gh pr merge waits\nEOF\ngit log -1") == passed
    assert run("git commit -m 'why git push is held' && git status") == passed

    # blanking quotes and heredoc bodies must not hide a real call
    assert run('cd "D:/Codes/my app" && git push origin dev') == held
    assert run("cat <<'EOF' > notes.md && git push origin dev\nbody\nEOF") == held
    assert run("git commit -F - <<'EOF'\nmsg\nEOF\ngit push --force origin dev") == refused

    # auto-commit must not be slowed down by the guard.
    # Run this from a branch other than main — the commit assertion reads the real
    # HEAD, and on main the guard is supposed to refuse.
    assert run("git commit -m 'add page' -- src/app/orders/page.tsx") == passed
    assert run("git add src/app/orders/page.tsx") == passed
    assert run("git status --porcelain") == passed
    assert run("git fetch") == passed

    # unrelated commands are none of this guard's business
    assert run("npm run dev") == passed
    assert run("gh release list") == passed
    assert run("gh pr view 12") == passed

    print("ok")


if __name__ == "__main__":
    demo()
