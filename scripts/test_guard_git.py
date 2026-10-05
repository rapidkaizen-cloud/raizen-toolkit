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


def run_antigravity(command: str, transcript: str = "", workspace: str = "") -> tuple:
    """The payload Antigravity 1.2.16 sends before `run_command`, with the hook started
    where Antigravity starts it: the folder holding hooks.json, not the project."""
    payload = {
        "toolCall": {"name": "run_command", "args": {"CommandLine": command, "Cwd": workspace}},
        "workspacePaths": [workspace or str(Path.cwd())],
        "transcriptPath": transcript,
    }
    result = subprocess.run(
        [PYTHON, str(GUARD)], input=json.dumps(payload), capture_output=True, text=True, cwd=GUARD.parent.parent
    )
    word = result.stderr.split(":", 1)[0] if result.stderr else ""
    return result.returncode, word, result.stderr


def planned(name: str, args: dict) -> dict:
    return {"type": "PLANNER_RESPONSE", "tool_calls": [{"name": name, "args": args}]}


def question(*texts) -> dict:
    return planned("ask_question", {"questions": [{"question": t, "options": ["Run", "Cancel"]} for t in texts]})


def result(content: str = "The command exited with code 0.") -> dict:
    return {"type": "GENERIC", "content": f"Created At: 2026-10-04T20:42:25+07:00\n{content}"}


def antigravity() -> None:
    def outcome(command: str, transcript: str = "", workspace: str = "") -> tuple:
        return run_antigravity(command, transcript, workspace)[:2]

    refused, held, passed = (2, "REFUSED"), (2, "HELD"), (0, "")

    # passes first: what a session does all day must not be slowed down
    assert outcome("git status --porcelain") == passed
    assert outcome("git add src/app/orders/page.tsx") == passed
    assert outcome("git commit -m 'add page' -- src/app/orders/page.tsx") == passed
    assert outcome("npm run dev") == passed

    assert outcome("git add -A") == refused
    assert outcome("git push --force origin dev") == refused

    push = "git push origin development"
    code, word, message = run_antigravity(push)
    assert (code, word) == held
    # the held message names this host's question tool, not Claude Code's
    assert "ask_question" in message and "AskUserQuestion" not in message

    with tempfile.TemporaryDirectory() as tmp:
        def transcript(*steps) -> str:
            path = Path(tmp) / f"t{len(list(Path(tmp).iterdir()))}.jsonl"
            path.write_text("\n".join(json.dumps(x) for x in steps) + "\nnot json\n", encoding="utf-8")
            return str(path)

        ask = question(f"Run `{push}`?\n- 4cc1af0 feat: push waits for `Run`")
        yes = [ask, result("A1: Run")]

        assert outcome(push, transcript(*yes)) == passed
        assert outcome("git push origin main", transcript(*yes)) == held

        # the call being checked is already written, not yet answered: not spent
        mine = planned("run_command", {"CommandLine": push})
        assert outcome(push, transcript(*yes, mine)) == passed

        # spent by a run; a new answer grants one more
        assert outcome(push, transcript(*yes, mine, result())) == held
        assert outcome(push, transcript(*yes, mine, result(), *yes)) == passed

        # a held attempt before the answer spends nothing
        assert outcome(push, transcript(mine, result("HELD: a push"), *yes, mine)) == passed

        # the second of two questions answers for itself
        two = question("Deploy too?", f"Run `{push}`?")
        assert outcome(push, transcript(two, result("A1: Cancel\nA2: Run"))) == passed
        assert outcome(push, transcript(two, result("A1: Run\nA2: Cancel"))) == held

        # no answer, another answer, or a question that does not name the command
        assert outcome(push, transcript(ask, result("A1: User Skipped"))) == held
        assert outcome(push, transcript(ask, result("A1: Cancel"))) == held
        assert outcome(push, transcript(ask, result("A1: Run it"))) == held
        assert outcome(push, transcript(question("Push to development?"), result("A1: Run"))) == held
        assert outcome(push, transcript(ask)) == held

        # the branch is read in the workspace, not in the folder the hook starts in
        repo = Path(tmp) / "repo"
        repo.mkdir()
        subprocess.run(["git", "init", "-q", "-b", "main", str(repo)], check=True)
        subprocess.run(
            ["git", "-C", str(repo), "-c", "user.name=t", "-c", "user.email=t@t.dev",
             "commit", "-q", "--allow-empty", "-m", "init"],
            check=True,
        )
        assert outcome("git commit -m 'add page' -- a.txt", workspace=str(repo)) == refused

    print("ok antigravity")


if __name__ == "__main__":
    demo()
    antigravity()
