#!/usr/bin/env python3
"""Self-check handoff.py: when the hand-over block is printed, and what it carries.

The quiet cases come first. The block is paid for in context, so a clean tree, a repo
the other host never worked in, and a host whose own session is the newer one must each
print nothing. Run directly: python3 test_handoff.py
"""
import json
import os
import re
import subprocess
import tempfile
from pathlib import Path

import handoff
import host


def write(path: Path, *lines) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(json.dumps(x) for x in lines) + "\nnot json\n", encoding="utf-8")
    return path


def age(path: Path, seconds: int) -> None:
    stamp = path.stat().st_mtime - seconds
    os.utime(path, (stamp, stamp))


def demo() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        home = Path(tmp) / "home"
        root = Path(tmp) / "my app"
        root.mkdir(parents=True)
        subprocess.run(["git", "init", "-q", str(root)], check=True)
        slug = re.sub(r"[^A-Za-z0-9]", "-", str(root))

        # quiet: the other host never worked in this repo
        (root / "page.tsx").write_text("half a page\n", encoding="utf-8")
        assert handoff.note(root, host.ANTIGRAVITY, home=home) == ""

        claude = write(
            home / ".claude" / "projects" / slug / "s1.jsonl",
            {"type": "user", "message": {"role": "user", "content": "build the approval inbox"}},
            {"type": "assistant", "message": {"role": "assistant", "content": [
                {"type": "tool_use", "id": "t1", "name": "TodoWrite", "input": {"todos": [
                    {"content": "contract", "status": "completed"},
                    {"content": "fixtures, six cases", "status": "in_progress"},
                ]}},
                {"type": "text", "text": "Contract written, starting the fixtures."},
            ]}},
            {"type": "user", "toolUseResult": {"answers": {"Which columns does the inbox drop?": ["keep all"]}}},
            {"type": "assistant", "isSidechain": True, "message": {"role": "assistant", "content": [
                {"type": "text", "text": "a subagent's own chatter"},
            ]}},
        )

        # quiet: a clean tree needs no hand-over
        (root / "page.tsx").unlink()
        assert handoff.note(root, host.ANTIGRAVITY, home=home) == ""

        # dirty tree, last session on the other host: the block, with what no file holds
        (root / "page.tsx").write_text("half a page\n", encoding="utf-8")
        out = handoff.note(root, host.ANTIGRAVITY, home=home)
        assert "ran on Claude Code" in out
        assert "build the approval inbox" in out
        assert "Which columns does the inbox drop? -> keep all" in out
        assert "[in_progress] fixtures, six cases" in out
        assert "starting the fixtures" in out and "subagent" not in out

        # another repo's sessions are not this repo's
        assert handoff.note(Path(tmp), host.ANTIGRAVITY, home=home) == ""

        # the same switch the other way: Antigravity's last conversation for this workspace
        cli = home / ".gemini" / "antigravity-cli"
        (cli / "cache").mkdir(parents=True)
        (cli / "cache" / "last_conversations.json").write_text(json.dumps({str(root): "c1"}), encoding="utf-8")
        write(
            cli / "brain" / "c1" / ".system_generated" / "logs" / "transcript_full.jsonl",
            {"type": "USER_INPUT", "source": "USER_EXPLICIT", "content": "<USER_REQUEST>\nwire the inbox\n</USER_REQUEST>"},
            {"type": "USER_INPUT", "source": "SYSTEM_SDK", "content": "<USER_REQUEST>\nSESSION NORMS\n</USER_REQUEST>"},
            {"type": "PLANNER_RESPONSE", "tool_calls": [{"name": "ask_question", "args": {"questions": [
                {"question": "Approve limit per role?", "options": ["Yes", "No"]},
            ]}}]},
            {"type": "GENERIC", "content": "Created At: now\nA1: Yes"},
            {"type": "PLANNER_RESPONSE", "content": "Migration written, role test next."},
        )
        out = handoff.note(root, host.CLAUDE, home=home)
        assert "ran on Antigravity" in out
        assert "wire the inbox" in out and "SESSION NORMS" not in out
        assert "Approve limit per role? -> Yes" in out and "role test next" in out

        # quiet: this host's own previous session is the newer one
        age(claude, 3600)
        assert handoff.note(root, host.ANTIGRAVITY, home=home) == ""
        # ... but the session now starting does not count as one
        assert "ran on Antigravity" in handoff.note(root, host.CLAUDE, current=str(claude), home=home)

    print("ok")


if __name__ == "__main__":
    demo()
