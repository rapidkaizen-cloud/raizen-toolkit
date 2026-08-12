#!/usr/bin/env python3
"""Self-check guard_destructive.py against the real Supabase MCP payload shape.

The `query` field was verified against the official supabase-community/supabase-mcp
source (execute_sql and apply_migration both use `query`, not `sql`/`statement`).
Run directly: python3 test_guard_destructive.py
"""
import json
import subprocess
from pathlib import Path

GUARD = Path(__file__).parent / "guard_destructive.py"

# `python3`, not sys.executable: this is the interpreter name hooks.json invokes, so a
# machine where only `python` resolves must fail here rather than pass a test whose
# subject never runs. The failure is the point.
PYTHON = "python3"


def run(tool_name: str, tool_input: dict) -> int:
    payload = json.dumps({"tool_name": tool_name, "tool_input": tool_input})
    result = subprocess.run(
        [PYTHON, str(GUARD)], input=payload, capture_output=True, text=True
    )
    return result.returncode


def demo() -> None:
    # execute_sql/apply_migration use the `query` field -> must be detected
    assert run("mcp__supabase__execute_sql", {"query": "DROP TABLE foo;"}) == 2

    guarded = (
        "DO $$ BEGIN DELETE FROM foo; IF (SELECT COUNT(*) FROM foo) != 0 THEN "
        "RAISE EXCEPTION 'mismatch'; END IF; END $$;"
    )
    assert run("mcp__supabase__apply_migration", {"query": guarded}) == 0

    # a Supabase tool carrying no SQL must not get blocked
    assert run("mcp__supabase__list_tables", {"schemas": ["public"]}) == 0

    # the same SQL arriving through the claude.ai-connected Supabase MCP, whose tools are
    # prefixed mcp__claude_ai_Supabase__ instead. This is what the mcp__.* matcher in
    # hooks.json buys: the prefix is set by whoever connects the server, not by this repo.
    assert run("mcp__claude_ai_Supabase__execute_sql", {"query": "DROP TABLE foo;"}) == 2
    assert run("mcp__claude_ai_Supabase__execute_sql", {"query": "SELECT count(*) FROM orders;"}) == 0

    # the Bash route (field `command`, shared with guard_git.py) stays closed
    assert run("Bash", {"command": 'psql -c "TRUNCATE foo;"'}) == 2

    # false positives: UPDATE with a narrow WHERE, SELECT, CREATE TABLE -> pass
    assert run("mcp__supabase__execute_sql", {"query": "UPDATE users SET active = true WHERE id = 3;"}) == 0
    assert run("mcp__supabase__execute_sql", {"query": "SELECT count(*) FROM orders;"}) == 0
    assert run("mcp__supabase__execute_sql", {"query": "CREATE TABLE t (id int);"}) == 0

    # a guard must not be borrowed by a neighbour: guarded DO, then a bare DELETE
    assert run("mcp__supabase__execute_sql", {
        "query": "DO $$ BEGIN RAISE EXCEPTION 'guard'; END $$; DELETE FROM t;"
    }) == 2

    # a subquery's WHERE must not count as the UPDATE's own WHERE
    assert run("mcp__supabase__execute_sql", {
        "query": "UPDATE users SET name = (SELECT name FROM source WHERE source.id = 1);"
    }) == 2

    # --- the [CLAUDE] carve-out: cleaning up one's own test rows needs no gate ---

    # must pass: prefix LIKE, and an exact match on a full [CLAUDE] title
    assert run("mcp__supabase__execute_sql", {
        "query": "DELETE FROM notes WHERE title LIKE '[CLAUDE]%';"
    }) == 0
    assert run("mcp__supabase__execute_sql", {
        "query": "DELETE FROM notes WHERE title = '[CLAUDE] smoke test';"
    }) == 0
    # the same cleanup arriving through Bash
    assert run("Bash", {
        "command": "psql -c \"DELETE FROM notes WHERE title LIKE '[CLAUDE]%';\""
    }) == 0
    # narrowed further by AND — still inside the prefix
    assert run("mcp__supabase__execute_sql", {
        "query": "DELETE FROM notes WHERE title LIKE '[CLAUDE]%' AND created_at < now();"
    }) == 0

    # must still block: contains, not opens-with -> reaches real rows mentioning the marker
    assert run("mcp__supabase__execute_sql", {
        "query": "DELETE FROM notes WHERE title LIKE '%[CLAUDE]%';"
    }) == 2
    # NOT inverts the target into everything the agent does not own
    assert run("mcp__supabase__execute_sql", {
        "query": "DELETE FROM notes WHERE title NOT LIKE '[CLAUDE]%';"
    }) == 2
    # OR widens back out past the prefix
    assert run("mcp__supabase__execute_sql", {
        "query": "DELETE FROM notes WHERE title LIKE '[CLAUDE]%' OR id = 1;"
    }) == 2
    # the prefix lives in a subquery: says nothing about the row being deleted
    assert run("mcp__supabase__execute_sql", {
        "query": "DELETE FROM notes WHERE id IN (SELECT id FROM src WHERE title LIKE '[CLAUDE]%');"
    }) == 2
    # no WHERE at all, whatever the table is called
    assert run("mcp__supabase__execute_sql", {"query": "DELETE FROM notes;"}) == 2
    # the carve-out is DELETE-only: it must not leak to DROP
    assert run("mcp__supabase__execute_sql", {
        "query": "DROP TABLE \"[CLAUDE] tmp\";"
    }) == 2
    # an exempt DELETE does not shelter a DROP sharing the payload
    assert run("mcp__supabase__execute_sql", {
        "query": "DELETE FROM notes WHERE title LIKE '[CLAUDE]%'; DROP TABLE orders;"
    }) == 2

    print("ok")


if __name__ == "__main__":
    demo()
