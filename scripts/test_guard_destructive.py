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


def run(tool_name: str, tool_input: dict, cwd: str | None = None) -> int:
    payload = json.dumps({"tool_name": tool_name, "tool_input": tool_input})
    result = subprocess.run(
        [PYTHON, str(GUARD)], input=payload, capture_output=True, text=True, cwd=cwd
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
    # the PowerShell route carries the same `command` field and the same guard
    assert run("PowerShell", {"command": 'psql -c "TRUNCATE foo;"'}) == 2

    # shell vocabulary is not SQL: `update` without SET, coreutils truncate -> pass
    assert run("Bash", {"command": 'claude plugin update "raizen-hub@raizen"'}) == 0
    assert run("Bash", {"command": "sudo apt update && sudo apt upgrade -y"}) == 0
    assert run("Bash", {"command": "truncate -s 0 logs/app.log"}) == 0
    assert run("PowerShell", {"command": "claude plugin update raizen-norms@raizen"}) == 0
    # but SQL arriving through a shell still blocks
    assert run("Bash", {"command": 'psql -c "UPDATE users SET active = false;"'}) == 2

    # --- shell text is prose as often as SQL: capitals only, unless psql/supabase runs it ---

    # must pass: Tailwind's `truncate` class in a file edit, SQL words in a commit message
    assert run("Bash", {"command": "sed -i 's/flex/truncate text-sm/' src/Row.tsx"}) == 0
    assert run("Bash", {"command": "sed -i 's/flex/truncate block/' src/Row.tsx"}) == 0
    assert run("Bash", {"command": "cat > src/Row.tsx <<'EOF'\n<p className=\"truncate max-w-xs\">x</p>\nEOF"}) == 0
    assert run("PowerShell", {"command": "(Get-Content Row.tsx) -replace 'flex', 'truncate font-medium' | Set-Content Row.tsx"}) == 0
    assert run("Bash", {"command": 'git commit -m "fix: delete from queue when done"'}) == 0
    assert run("Bash", {"command": 'git commit -m "docs: when to drop table rows"'}) == 0
    assert run("Bash", {"command": 'git commit -m "update set of fixtures"'}) == 0
    assert run("Bash", {"command": "truncate logs/app.log -s 0"}) == 0
    # a path merely named after a client does not run it
    assert run("Bash", {"command": "sed -i 's/flex/truncate block/' src/lib/supabase-client.tsx"}) == 0

    # must still block: capitals anywhere in a shell, any case once psql or supabase runs
    assert run("Bash", {"command": "cat > wipe.sql <<'EOF'\nTRUNCATE leads;\nEOF"}) == 2
    assert run("Bash", {"command": 'psql -c "truncate leads;"'}) == 2
    assert run("Bash", {"command": 'psql -c "delete from leads;"'}) == 2
    assert run("Bash", {"command": 'psql -c "update leads set status = 1;"'}) == 2
    assert run("PowerShell", {"command": '& "C:\\Program Files\\PostgreSQL\\16\\bin\\psql.exe" -c "truncate leads;"'}) == 2
    assert run("Bash", {"command": "npx supabase migration new wipe && echo 'truncate leads;' >> supabase/migrations/wipe.sql"}) == 2
    assert run("mcp__supabase__execute_sql", {"query": "truncate leads;"}) == 2

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

    # --- the per-repo off switch: .claude/destructive-gate.off in the project cwd ---

    import tempfile
    with tempfile.TemporaryDirectory() as td:
        # marker present -> everything passes, in that repo only
        (Path(td) / ".claude").mkdir()
        (Path(td) / ".claude" / "destructive-gate.off").write_text("why, in free text\n")
        assert run("mcp__supabase__execute_sql", {"query": "DROP TABLE foo;"}, cwd=td) == 0
    with tempfile.TemporaryDirectory() as td:
        # no marker -> the same payload still blocks (fails closed)
        assert run("mcp__supabase__execute_sql", {"query": "DROP TABLE foo;"}, cwd=td) == 2

    # --- Antigravity: the shapes 1.2.16 sends, the hook started outside the project ---

    def antigravity(name: str, args: dict, workspace: str) -> int:
        payload = json.dumps({"toolCall": {"name": name, "args": args}, "workspacePaths": [workspace]})
        return subprocess.run(
            [PYTHON, str(GUARD)], input=payload, capture_output=True, text=True, cwd=GUARD.parent.parent
        ).returncode

    def mcp(query: str) -> dict:
        return {"ServerName": "supabase", "ToolName": "execute_sql", "Arguments": {"project_id": "x", "query": query}}

    with tempfile.TemporaryDirectory() as td:
        assert antigravity("call_mcp_tool", mcp("SELECT count(*) FROM orders;"), td) == 0
        assert antigravity("call_mcp_tool", mcp(guarded), td) == 0
        assert antigravity("run_command", {"CommandLine": "git commit -m 'delete from the queue'"}, td) == 0
        assert antigravity("view_file", {"AbsolutePath": "DROP TABLE.md"}, td) == 0
        assert antigravity("call_mcp_tool", mcp("DROP TABLE foo;"), td) == 2
        assert antigravity("run_command", {"CommandLine": 'psql -c "drop table foo"'}, td) == 2

        # the off switch is looked for in the workspace, not where the hook starts
        (Path(td) / ".claude").mkdir()
        (Path(td) / ".claude" / "destructive-gate.off").write_text("why, in free text\n")
        assert antigravity("call_mcp_tool", mcp("DROP TABLE foo;"), td) == 0

    print("ok")


if __name__ == "__main__":
    demo()
