#!/usr/bin/env python3
"""Hand every hook one payload shape, whichever host called it.

Claude Code sends `tool_name`, `tool_input`, `cwd` and `transcript_path`, and runs a hook
in the project directory. Antigravity sends `toolCall`, `workspacePaths` and
`transcriptPath`, and runs it in the directory holding `hooks.json`. `read_payload`
returns the Claude Code shape for both and moves into the project directory, so a guard
reads one shape and a relative path means the same thing on either host.

A refusal needs no translation: stderr with exit 2 stops the tool on both hosts. On
Antigravity it also holds under `--dangerously-skip-permissions`, where a hook's `ask`
and `force_ask` are approved without a prompt - which is why no guard answers with one.
"""
import json
import os
import sys

CLAUDE = "claude-code"
ANTIGRAVITY = "antigravity"


def read_payload() -> dict:
    """The hook payload in the Claude Code shape, plus `host`. Empty when unreadable."""
    try:
        # Bytes, not text: stdin decodes as the ANSI codepage on Windows, and a payload
        # that fails to decode would pass every guard as an empty one.
        payload = json.loads(sys.stdin.buffer.read().decode("utf-8-sig", errors="replace"))
    except Exception:
        return {}
    if not isinstance(payload, dict):
        return {}
    if "workspacePaths" not in payload and "toolCall" not in payload:
        payload.setdefault("host", CLAUDE)
        return payload

    call = payload.get("toolCall")
    call = call if isinstance(call, dict) else {}
    args = call.get("args")
    args = args if isinstance(args, dict) else {}
    name = str(call.get("name") or "")
    if name == "run_command":
        tool_name, tool_input = "Bash", {"command": args.get("CommandLine") or ""}
    elif name == "call_mcp_tool":
        tool_name = f"mcp__{args.get('ServerName')}__{args.get('ToolName')}"
        tool_input = args.get("Arguments")
        if isinstance(tool_input, str):
            try:
                tool_input = json.loads(tool_input)
            except ValueError:
                tool_input = {}
        tool_input = tool_input if isinstance(tool_input, dict) else {}
    else:
        tool_name, tool_input = name, args

    roots = payload.get("workspacePaths")
    cwd = str(roots[0]) if isinstance(roots, list) and roots else ""
    if cwd:
        try:
            os.chdir(cwd)
        except OSError:
            cwd = ""
    return {
        **payload,
        "host": ANTIGRAVITY,
        "tool_name": tool_name,
        "tool_input": tool_input,
        "cwd": cwd or os.getcwd(),
        "transcript_path": str(payload.get("transcriptPath") or ""),
    }
