#!/usr/bin/env python3
"""Self-check guard_project_ref.py — the pass cases first.

Per this repo's rule for hooks: test what must PASS before what must be
refused. A guard that blocks other servers' project ids, a CLI-standard
config.toml, or a repo that has declared nothing is worse than no guard.

Refs in these tests are 20 lowercase alphanumerics — the real shape of a
hosted Supabase project ref, which the guard requires before it enforces.
The `project_id` argument name matches the hosted Supabase MCP tools in
account mode. Run directly: python3 test_guard_project_ref.py
"""
import json
import subprocess
import tempfile
from pathlib import Path

GUARD = Path(__file__).parent / "guard_project_ref.py"

# `python3`, not sys.executable: the interpreter name hooks.json invokes — a
# machine where only `python` resolves must fail here, not pass vacuously.
PYTHON = "python3"

OURS = "aaaaaaaaaaaaaaaa1111"    # the repo's declared project
OTHER = "bbbbbbbbbbbbbbbb2222"   # some other project in the same account


def run(tool_name: str, tool_input, cwd: str) -> int:
    payload = json.dumps({"tool_name": tool_name, "tool_input": tool_input, "cwd": cwd})
    result = subprocess.run(
        [PYTHON, str(GUARD)], input=payload, capture_output=True, text=True
    )
    return result.returncode


def repo_with(config_text: str, raw: bytes = None) -> str:
    root = tempfile.mkdtemp(prefix="guard_ref_")
    sub = Path(root) / "supabase"
    sub.mkdir()
    if raw is not None:
        (sub / "config.toml").write_bytes(raw)
    else:
        (sub / "config.toml").write_text(config_text, encoding="utf-8")
    return root


def demo() -> None:
    repo = repo_with('project_id = "%s"\n' % OURS)
    bare = tempfile.mkdtemp(prefix="guard_ref_bare_")

    # PASS: the declared project itself, through both tool prefixes
    assert run("mcp__supabase__execute_sql", {"project_id": OURS, "query": "SELECT 1;"}, repo) == 0
    assert run("mcp__claude_ai_Supabase__execute_sql", {"project_id": OURS, "query": "SELECT 1;"}, repo) == 0

    # PASS: a padded but identical ref is still the declared project
    assert run("mcp__supabase__execute_sql", {"project_id": OURS + " ", "query": "SELECT 1;"}, repo) == 0

    # PASS: Supabase tools with no project argument (account-level reads)
    assert run("mcp__supabase__list_projects", {}, repo) == 0
    assert run("mcp__supabase__search_docs", {"graphql_query": "{}"}, repo) == 0

    # PASS: another server's project_id is not a Supabase ref — no "supabase"
    # in the name, no SQL query beside the id
    assert run("mcp__claude_ai_Vercel__get_project", {"project_id": OTHER}, repo) == 0

    # PASS: repo declares nothing — no config.toml, or a placeholder unfilled
    assert run("mcp__supabase__execute_sql", {"project_id": OTHER, "query": "SELECT 1;"}, bare) == 0
    placeholder = repo_with('project_id = "{{SUPABASE_PROJECT_REF}}"\n')
    assert run("mcp__supabase__execute_sql", {"project_id": OTHER, "query": "SELECT 1;"}, placeholder) == 0

    # PASS: a CLI-standard config (`supabase init` writes the directory name)
    # is not a declaration — it must never block the repo's real calls
    cli_repo = repo_with('project_id = "my-app"\n\n[api]\nport = 54321\n')
    assert run("mcp__supabase__execute_sql", {"project_id": OURS, "query": "SELECT 1;"}, cli_repo) == 0

    # PASS: a ref inside a [section] is not the repo's declaration
    remotes = repo_with('project_id = "my-app"\n\n[remotes.production]\nproject_id = "%s"\n' % OTHER)
    assert run("mcp__supabase__execute_sql", {"project_id": OURS, "query": "SELECT 1;"}, remotes) == 0

    # PASS: a BOM (PowerShell default) must not hide the top-level declaration
    bom = repo_with("", raw=b'\xef\xbb\xbfproject_id = "%s"\n' % OURS.encode())
    assert run("mcp__supabase__execute_sql", {"project_id": OURS, "query": "SELECT 1;"}, bom) == 0

    # PASS: malformed input must never block — bad stdin, non-dict tool_input,
    # a config that is not UTF-8
    result = subprocess.run([PYTHON, str(GUARD)], input="not json", capture_output=True, text=True)
    assert result.returncode == 0
    assert run("mcp__supabase__execute_sql", ["not", "a", "dict"], repo) == 0
    latin1 = repo_with("", raw=b'# caf\xe9\nproject_id = "x"\n')
    assert run("mcp__supabase__execute_sql", {"project_id": OTHER, "query": "SELECT 1;"}, latin1) == 0

    # PASS (documented gap, locked in): a renamed server's non-SQL tool is not
    # judged — the shape signal needs a query beside the project id
    assert run("mcp__db__get_logs", {"project_id": OTHER, "service": "api"}, repo) == 0

    # BLOCK: a call aimed at a different project than the repo declares
    assert run("mcp__supabase__execute_sql", {"project_id": OTHER, "query": "SELECT 1;"}, repo) == 2
    assert run("mcp__claude_ai_Supabase__apply_migration", {"project_id": OTHER, "query": "CREATE TABLE t (id int);"}, repo) == 2
    assert run("mcp__claude_ai_Supabase__execute_sql", {"project_ref": OTHER, "query": "SELECT 1;"}, repo) == 2

    # BLOCK: renaming the server key must not turn the pin off for SQL calls
    assert run("mcp__db__execute_sql", {"project_id": OTHER, "query": "SELECT 1;"}, repo) == 2

    # BLOCK: a decoy project_id equal to the declaration must not mask a
    # differing project_ref
    assert run("mcp__supabase__execute_sql", {"project_id": OURS, "project_ref": OTHER, "query": "SELECT 1;"}, repo) == 2

    # BLOCK: the BOM repo still enforces its declaration
    assert run("mcp__supabase__execute_sql", {"project_id": OTHER, "query": "SELECT 1;"}, bom) == 2

    print("ok")


if __name__ == "__main__":
    demo()
