#!/usr/bin/env python3
"""Block destructive SQL sent bare.

What is enforced here is SHAPE, not permission. A hook cannot ask, so it does not
know whether the user agreed. What it checks: whether the destructive operation
arrives wrapped in a DO block with RAISE EXCEPTION as its guard, per statement —
one destructive statement without a guard of its own is still blocked even when
another statement in the same payload is guarded.

A guard can only be written once the Expected number exists, and the Expected
number is only born from a gate the user answered. So enforcing the shape is
enough to enforce that the gate happened.

Exit 0 = pass, exit 2 = block.
"""
import json
import re
import sys

DESTRUCTIVE = [
    (r"\bDROP\s+(TABLE|COLUMN|SCHEMA|TYPE|FUNCTION|POLICY|INDEX|VIEW)\b", "DROP"),
    (r"\bTRUNCATE\b", "TRUNCATE"),
    (r"\bDELETE\s+FROM\b", "DELETE"),
    (r"\bALTER\s+TABLE\b.*\bDROP\s+COLUMN\b", "ALTER ... DROP COLUMN"),
    (r"\bALTER\s+TABLE\b.*\bRENAME\b", "RENAME"),
    (r"\bALTER\s+TYPE\b", "ALTER TYPE"),
]

# "query" = the real field of Supabase MCP execute_sql/apply_migration (not a guess,
# see test_guard_destructive.py); "command" = the Bash field. "sql"/"statement" as a net.
SQL_KEYS = ("query", "sql", "command", "statement")

# The hooks.json matcher is deliberately mcp__.* (not mcp__supabase__.*): the server
# name in the user's MCP config is chosen by whoever connects it, outside this repo's control.
# Widening is safe because SQL_KEYS above comes up empty for non-SQL tools -> main()
# exits 0 on its first line, with no effect on other MCP tools.
DOLLAR_TAG = re.compile(r"\$([A-Za-z_][A-Za-z0-9_]*)?\$")


def read_sql() -> str:
    try:
        payload = json.load(sys.stdin)
    except Exception:
        return ""
    ti = payload.get("tool_input") or {}
    parts = [str(ti[k]) for k in SQL_KEYS if k in ti and ti[k]]
    return "\n".join(parts)


def strip_comments(sql: str) -> str:
    sql = re.sub(r"--[^\n]*", " ", sql)
    sql = re.sub(r"/\*.*?\*/", " ", sql, flags=re.S)
    return sql


def split_statements(sql: str) -> list[str]:
    """Split on ';', aware of dollar-quoting ($$...$$ / $tag$...$tag$).
    A semicolon inside a dollar-quoted block is not a separator, so a whole DO
    block (with its RAISE EXCEPTION) stays one statement. Not aware of ordinary
    string literals ('...') — a semicolon inside one still separates."""
    statements = []
    start = pos = 0
    n = len(sql)
    while pos < n:
        m = DOLLAR_TAG.match(sql, pos)
        if m:
            tag = m.group(0)
            close = sql.find(tag, pos + len(tag))
            pos = close + len(tag) if close != -1 else n
            continue
        if sql[pos] == ";":
            statements.append(sql[start:pos])
            pos += 1
            start = pos
            continue
        pos += 1
    tail = sql[start:pos]
    if tail.strip():
        statements.append(tail)
    return statements


def has_guard(stmt: str) -> bool:
    up = stmt.upper()
    return "RAISE EXCEPTION" in up and re.search(r"\bDO\s+\$", up) is not None


def strip_parens(s: str) -> str:
    """Drop balanced parenthesized content (nested included), so that a WHERE
    belonging to a subquery is not counted as the outer statement's WHERE. A
    mitigation, not a guarantee: not aware of string literals, so parentheses
    inside a string get stripped too."""
    out = []
    depth = 0
    for ch in s:
        if ch == "(":
            depth += 1
        elif ch == ")":
            depth = max(0, depth - 1)
        elif depth == 0:
            out.append(ch)
    return "".join(out)


def bare_update(stmt: str) -> bool:
    """UPDATE without a WHERE, or with a WHERE that is always true."""
    for m in re.finditer(r"\bUPDATE\b(.*?)(;|$)", stmt, flags=re.S | re.I):
        body = strip_parens(m.group(1))
        if not re.search(r"\bWHERE\b", body, flags=re.I):
            return True
        if re.search(r"\bWHERE\s+(true|1\s*=\s*1)\b", body, flags=re.I):
            return True
    return False


def block(op: str) -> None:
    sys.stderr.write(
        "REFUSED: a destructive operation ({op}) was sent without a guard.\n\n"
        "The order is:\n"
        "  1. SELECT COUNT first, and set the Expected number.\n"
        "  2. Show the DESTRUCTIVE block (operation - affected - Expected - reversible), "
        "then STOP and wait for the user's answer in this session.\n"
        "  3. Execute wrapped in a DO block: RAISE EXCEPTION when the row count misses "
        "Expected, followed by a verifying SELECT in the same call.\n\n"
        "The exception aborts the whole transaction, so zero data is lost when the "
        "number does not match.\n".format(op=op)
    )
    sys.exit(2)


def main() -> None:
    sql = strip_comments(read_sql())
    if not sql.strip():
        sys.exit(0)

    for stmt in split_statements(sql):
        if not stmt.strip() or has_guard(stmt):
            continue

        for pattern, label in DESTRUCTIVE:
            if re.search(pattern, stmt, flags=re.I | re.S):
                block(label)

        if bare_update(stmt):
            block("UPDATE without a narrow WHERE")

    sys.exit(0)


if __name__ == "__main__":
    main()
