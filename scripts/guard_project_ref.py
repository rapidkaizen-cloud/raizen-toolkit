#!/usr/bin/env python3
"""Pin Supabase MCP calls to the repo's own project.

The Supabase MCP server is connected account-wide (user scope, no project_ref
in the URL), so one browser login covers every app — and every tool call can
name any project in the account via its project_id argument. The repo that the
session runs in declares which project is its own: a top-level `project_id` in
supabase/config.toml whose value has the shape of a hosted project ref
(exactly 20 lowercase alphanumerics). This hook blocks a Supabase call whose
target differs from that declaration.

A call is judged when the tool name contains "supabase" OR when its input has
the Supabase shape — a project target next to a SQL `query`. The second signal
exists because the server name is chosen by whoever connects it, outside this
repo's control (same rationale as guard_destructive.py): renaming the server
must not silently turn the pin off for SQL-carrying calls.

What is NOT blocked, deliberately (a hook that is too strict costs more than
no hook):
- tools of other MCP servers that carry a project_id of their own (Vercel,
  Lovable) — no "supabase" in the name and no SQL query beside the id;
- Supabase tools with no project argument (list_projects, docs search);
- a repo that declares nothing: no supabase/config.toml, an unreadable one, an
  unfilled {{...}} placeholder, or a CLI-written `project_id = "<dir name>"` —
  only a value shaped like a hosted ref counts as a declaration;
- a `project_id` inside a [section] such as [remotes.production] — that is the
  section's ref, not the repo's declaration;
- the Bash route (supabase CLI, curl): this guard covers MCP calls only.

The guard fails OPEN by design: a crash or unreadable input must never turn
into a block-everything hook. Exit 0 = pass, exit 2 = block.
"""
import os
import re
import sys

import host

REF_KEYS = ("project_id", "project_ref")

# A hosted Supabase project ref is exactly 20 lowercase alphanumerics.
# Anything else — notably the directory name `supabase init` writes as
# project_id — declares nothing, so the guard stays silent instead of
# blocking every call in that repo.
REF_SHAPE = re.compile(r"^[a-z0-9]{20}$")

CONFIG_LINE = re.compile(r'^\s*project_id\s*=\s*"([^"]+)"', re.M)


def declared_ref(config_path: str) -> str:
    try:
        # utf-8-sig: swallow a BOM, which PowerShell writes by default.
        with open(config_path, encoding="utf-8-sig") as fh:
            text = fh.read()
    except (OSError, UnicodeError):
        return ""
    # Only the top-level preamble counts — cut at the first [section] header,
    # so [remotes.*] refs are never mistaken for the repo's declaration.
    text = ("\n" + text).split("\n[", 1)[0]
    m = CONFIG_LINE.search(text)
    if not m:
        return ""
    ref = m.group(1).strip()
    return ref if REF_SHAPE.fullmatch(ref) else ""


def main() -> None:
    payload = host.read_payload()

    ti = payload.get("tool_input")
    if not isinstance(ti, dict):
        sys.exit(0)

    tool_name = str(payload.get("tool_name") or "")
    if not tool_name.startswith("mcp__"):
        sys.exit(0)

    named = "supabase" in tool_name.lower()
    shaped = "query" in ti and any(k in ti for k in REF_KEYS)
    if not (named or shaped):
        sys.exit(0)

    # Every present ref key must match — a decoy project_id must not mask a
    # differing project_ref.
    called = [str(ti[k]).strip() for k in REF_KEYS if ti.get(k)]
    called = [c for c in called if c]
    if not called:
        sys.exit(0)

    cwd = str(payload.get("cwd") or os.getcwd())
    config_path = os.path.join(cwd, "supabase", "config.toml")
    expected = declared_ref(config_path)
    if not expected or all(c == expected for c in called):
        sys.exit(0)

    other = next(c for c in called if c != expected)
    sys.stderr.write(
        "REFUSED: this Supabase call targets project '{other}', but {path} "
        "declares project '{expected}'.\n\n"
        "The MCP server is connected account-wide, so a call can reach any "
        "project in the account — this repo only ever operates on its own.\n"
        "Nothing said in this session lifts this, a go-ahead included: STOP "
        "and tell the user. Work on the other project runs from a session in "
        "that project's own repo. Do not retry with a different ref and do "
        "not edit project_id yourself — re-pointing it re-pins every later "
        "call in this repo, which only the user may do, by hand.\n".format(
            other=other, path=config_path, expected=expected
        )
    )
    sys.exit(2)


if __name__ == "__main__":
    try:
        main()
    except Exception:
        # Failing open has to be said out loud here: Antigravity blocks the call on any
        # non-zero exit, a crash included.
        sys.exit(0)
