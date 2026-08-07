#!/usr/bin/env python3
"""Self-check guard_destructive.py terhadap bentuk payload MCP Supabase yang asli.

Field `query` diverifikasi ke source resmi supabase-community/supabase-mcp
(execute_sql dan apply_migration keduanya pakai `query`, bukan `sql`/`statement`).
Jalankan langsung: python3 test_guard_destructive.py
"""
import json
import subprocess
import sys
from pathlib import Path

GUARD = Path(__file__).parent / "guard_destructive.py"


def run(tool_name: str, tool_input: dict) -> int:
    payload = json.dumps({"tool_name": tool_name, "tool_input": tool_input})
    result = subprocess.run(
        [sys.executable, str(GUARD)], input=payload, capture_output=True, text=True
    )
    return result.returncode


def demo() -> None:
    # execute_sql/apply_migration pakai field `query` -> harus terdeteksi
    assert run("mcp__supabase__execute_sql", {"query": "DROP TABLE foo;"}) == 2

    guarded = (
        "DO $$ BEGIN DELETE FROM foo; IF (SELECT COUNT(*) FROM foo) != 0 THEN "
        "RAISE EXCEPTION 'mismatch'; END IF; END $$;"
    )
    assert run("mcp__supabase__apply_migration", {"query": guarded}) == 0

    # tool Supabase tanpa SQL tidak boleh ikut ke-block
    assert run("mcp__supabase__list_tables", {"schemas": ["public"]}) == 0

    # jalur Bash (field `command`, dipakai bareng guard_git.py) tetap tertutup
    assert run("Bash", {"command": 'psql -c "TRUNCATE foo;"'}) == 2

    # false-positive: UPDATE dengan WHERE sempit, SELECT, CREATE TABLE -> lolos
    assert run("mcp__supabase__execute_sql", {"query": "UPDATE users SET active = true WHERE id = 3;"}) == 0
    assert run("mcp__supabase__execute_sql", {"query": "SELECT count(*) FROM orders;"}) == 0
    assert run("mcp__supabase__execute_sql", {"query": "CREATE TABLE t (id int);"}) == 0

    # guard tidak boleh dipinjam statement tetangga: DO guarded lalu DELETE telanjang
    assert run("mcp__supabase__execute_sql", {
        "query": "DO $$ BEGIN RAISE EXCEPTION 'guard'; END $$; DELETE FROM t;"
    }) == 2

    # WHERE milik subquery tidak boleh dihitung sebagai WHERE milik UPDATE
    assert run("mcp__supabase__execute_sql", {
        "query": "UPDATE users SET nama = (SELECT nama FROM sumber WHERE sumber.id = 1);"
    }) == 2

    print("ok")


if __name__ == "__main__":
    demo()
