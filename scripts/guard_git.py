#!/usr/bin/env python3
"""Guard git operations: block what must never happen, hold publishing for the user's answer.

Reads the hook payload from stdin.
Exit 0 = pass, exit 2 = block (the agent reads stderr).

Refused, and fixed by the agent itself:
  - commit while HEAD is on main, in a repo that has a development branch
  - git add -A / git add .  (a commit holds explicit paths from SCOPE)
  - a bare force push: --force / -f, and the flagless force spelled as a refspec
    (push origin +main). --force-with-lease refuses when the remote moved, so it is
    the only force a session runs.

Held until the user answers:
  - git push, --force-with-lease included
  - gh pr create / gh pr merge

A held command passes once the transcript shows the user picking `Run` on a question
- AskUserQuestion on Claude Code, `ask_question` on Antigravity - that names the exact
command in backticks, and no call of that command has run since - one answer, one run.
The answer is read from the transcript rather than asked for with a permission prompt,
because an SDK host never shows that prompt: "ask" there is a silent refusal that
leaves the user typing the command by hand. Antigravity gets the same reading for a
second reason: its hook `ask` is approved unasked under `--dangerously-skip-permissions`.
"""
import json
import re
import subprocess
import sys

import host

# Global options are allowed to sit between `git` and its subcommand: `git -c k=v push`,
# `git -C dir commit`, `git --no-pager add`. Anchoring on `git push` alone reads only the
# bare spelling, and the long way round walks past every rule below. `-c`/`-C` take a
# separate argument, so they need their own alternative.
GIT = r"\bgit\s+(?:-[cC]\s+\S+\s+|--?[\w-]+(?:=\S+)?\s+)*"

APPROVE = "Run"
SHELLS = ("Bash", "PowerShell")

# A commit message that mentions `gh pr create` is data, not a call. Heredoc bodies and
# quoted strings are blanked before any rule reads the command; the heredoc's opening
# line stays, since commands may follow `<<'EOF'` on it.
# ponytail: `sh -c 'git push'` hides inside quotes too; parse the shell if agents start wrapping git.
HEREDOC = re.compile(r"(<<-?\s*(['\"]?)(\w+)\2[^\n]*\n).*?^\s*\3\s*$", re.S | re.M)
QUOTED = re.compile(r"'[^']*'|\"(?:[^\"\\]|\\.)*\"")


def head_branch() -> str:
    try:
        out = subprocess.run(
            ["git", "rev-parse", "--abbrev-ref", "HEAD"],
            capture_output=True, text=True, timeout=5,
        )
        return out.stdout.strip()
    except Exception:
        return ""


def has_development() -> bool:
    """True when the repo has a `development` branch, local or on origin. A repo with only
    `main` has nowhere else to commit, and refusing there leaves the session no way out."""
    try:
        out = subprocess.run(
            ["git", "for-each-ref", "--count=1", "refs/heads/development", "refs/remotes/origin/development"],
            capture_output=True, text=True, timeout=5,
        )
        return bool(out.stdout.strip())
    except Exception:
        return True  # unreadable: refuse, as before the branch was looked for


def norm(text: str) -> str:
    return " ".join(text.split())


def entries(path: str):
    try:
        with open(path, encoding="utf-8") as f:
            for line in f:
                try:
                    yield json.loads(line)
                except ValueError:
                    continue
    except OSError:
        return


# One `A<n>: <answer>` line per question in the result of Antigravity's `ask_question`.
ANSWER = re.compile(r"^A(\d+):[ \t]*(.*?)[ \t]*$", re.M)


def approved_antigravity(payload: dict, cmd: str) -> bool:
    """`approved`, read from Antigravity's transcript: one step per line, a planner step
    carrying `tool_calls` and the step after it carrying their result."""
    # ponytail: the result is paired to its call by position, which holds while a planner
    # step carries one call; a step asking and pushing at once is held, which is the safe side.
    want = norm(cmd)
    ticked = f"`{want}`"
    granted = running = False
    asked = []
    for step in entries(payload.get("transcript_path") or ""):
        if not isinstance(step, dict):
            continue
        calls = step.get("tool_calls")
        if isinstance(calls, list):
            asked, running = [], False
            for call in calls:
                if not isinstance(call, dict):
                    continue
                args = call.get("args") if isinstance(call.get("args"), dict) else {}
                if call.get("name") == "ask_question":
                    questions = args.get("questions")
                    asked = [
                        str(i + 1)
                        for i, q in enumerate(questions if isinstance(questions, list) else [])
                        if isinstance(q, dict) and ticked in norm(str(q.get("question") or ""))
                    ]
                elif call.get("name") == "run_command" and norm(str(args.get("CommandLine") or "")) == want:
                    running = True
            continue
        if asked:
            answers = dict(ANSWER.findall(str(step.get("content") or "")))
            if any(answers.get(n) == APPROVE for n in asked):
                granted = True
            asked = []
        elif running:
            granted = running = False
    return granted


def approved(payload: dict, cmd: str) -> bool:
    """True when the last `Run` answer naming `cmd` has not been spent by a run of it.

    A call of the command counts as spent once its tool_result is in the transcript, so
    the call being checked right now - written, not yet answered - never spends it.
    """
    if payload.get("host") == host.ANTIGRAVITY:
        return approved_antigravity(payload, cmd)
    want = norm(cmd)
    ticked = f"`{want}`"
    granted = False
    pending = set()
    for entry in entries(payload.get("transcript_path") or ""):
        if not isinstance(entry, dict):
            continue
        content = (entry.get("message") or {}).get("content")
        for block in content if isinstance(content, list) else []:
            if not isinstance(block, dict):
                continue
            if (
                block.get("type") == "tool_use"
                and block.get("name") in SHELLS
                and norm(str((block.get("input") or {}).get("command") or "")) == want
            ):
                pending.add(block.get("id"))
            elif block.get("type") == "tool_result" and block.get("tool_use_id") in pending:
                granted = False
        result = entry.get("toolUseResult")
        if isinstance(result, dict) and isinstance(result.get("answers"), dict):
            for question, answer in result["answers"].items():
                picked = answer if isinstance(answer, list) else [answer]
                # ponytail: the whole question is searched, commit list included, so a listed
                # subject quoting another held command in backticks approves that one too;
                # match the first line only if that ever happens.
                if ticked in norm(str(question)) and APPROVE in picked:
                    granted = True
                    pending.clear()
    return granted


def block(msg: str) -> None:
    sys.stderr.write(msg + "\n")
    sys.exit(2)


def hold(payload: dict, cmd: str, what: str) -> None:
    if approved(payload, cmd):
        sys.exit(0)
    ask = host.ASK_TOOL.get(payload.get("host"), host.ASK_TOOL[host.CLAUDE])
    block(
        f"HELD: {what} runs only on the user's answer. Ask with {ask}: name this "
        f"exact command in backticks in the question, list under it every commit it publishes "
        f"as `- ` bullets, short hash and subject, and offer two options labelled exactly "
        f"`{APPROVE}` and `Cancel`. On `{APPROVE}`, retry the same command unchanged - one answer covers "
        "one run. Never hand the command to the user to type.\n"
        f"Command: {norm(cmd)}"
    )


def main() -> None:
    payload = host.read_payload()
    cmd = (payload.get("tool_input") or {}).get("command") or ""
    code = QUOTED.sub("''", HEREDOC.sub(r"\1", cmd))
    if not re.search(r"\b(git|gh)\b", code):
        sys.exit(0)

    if re.search(GIT + r"add\s+(-A\b|--all\b|\.(\s|$))", code):
        block(
            "REFUSED: git add -A / git add . is not used in this repo.\n"
            "A commit contains only paths that are in SCOPE, named explicitly.\n"
            "Files changed outside SCOPE are findings reported to the user, "
            "not things to commit along."
        )

    # `\s\+\S` is `push origin +main` — a force with no flag to grep for.
    if re.search(GIT + r"push\b.*(--force(?![-\w])|\s-f\b|\s\+\S)", code):
        block(
            "REFUSED: a bare force push. Use --force-with-lease instead - it refuses when "
            "the remote moved since your last fetch - and ask for it as for any push."
        )

    if re.search(GIT + r"commit\b", code):
        branch = head_branch()
        if branch == "main" and has_development():
            block(
                "REFUSED: HEAD is on main. A session never works on main.\n"
                "Switch to development first, then retry."
            )

    if re.search(r"\bgh\s+pr\s+(create|merge)\b", code):
        hold(payload, cmd, "opening or merging a pull request")

    if re.search(GIT + r"push\b", code):
        hold(payload, cmd, "a push")

    sys.exit(0)


if __name__ == "__main__":
    main()
