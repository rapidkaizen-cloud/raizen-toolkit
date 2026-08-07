#!/usr/bin/env python3
"""Blokir SQL destruktif yang dikirim telanjang.

Yang ditegakkan di sini adalah BENTUK, bukan izin. Hook tidak bisa bertanya,
jadi ia tidak tahu user sudah setuju atau belum. Yang ia periksa: apakah operasi
destruktif datang terbungkus DO block dengan RAISE EXCEPTION sebagai guard,
per statement — satu statement destruktif tanpa guard sendiri tetap diblokir
meski ada statement lain di payload yang sama yang guarded.

Guard hanya bisa ditulis kalau angka Harapan sudah ada, dan angka Harapan hanya
lahir dari gate yang dijawab user. Jadi menegakkan bentuk cukup untuk menegakkan
bahwa gate-nya terjadi.

Exit 0 = lolos, exit 2 = blokir.
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

# "query" = field asli execute_sql/apply_migration Supabase MCP (bukan tebakan,
# lihat test_guard_destructive.py); "command" = field Bash. "sql"/"statement" jaga-jaga.
SQL_KEYS = ("query", "sql", "command", "statement")

# Matcher di hooks.json sengaja mcp__.* (bukan mcp__supabase__.*): nama key
# server di .mcp.json repo app bisa diubah manual, di luar kendali repo ini.
# Aman dilebarkan karena SQL_KEYS di atas kosong untuk tool non-SQL -> main()
# exit 0 di baris pertama, tanpa efek untuk tool MCP lain.
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
    """Pisahkan per ';', sadar dollar-quoting ($$...$$ / $tag$...$tag$).
    Titik koma di dalam blok dollar-quoted bukan pemisah, jadi DO block utuh
    (RAISE EXCEPTION di dalamnya) tetap satu statement. Tidak sadar string
    literal biasa ('...') — titik koma di dalamnya tetap jadi pemisah."""
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
    """Buang isi kurung berimbang (termasuk nested), supaya WHERE milik
    subquery tidak terhitung sebagai WHERE milik statement luar. Mitigasi,
    bukan jaminan: tidak sadar string literal, jadi kurung di dalam string
    ikut disaring juga."""
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
    """UPDATE tanpa WHERE, atau WHERE yang selalu benar."""
    for m in re.finditer(r"\bUPDATE\b(.*?)(;|$)", stmt, flags=re.S | re.I):
        body = strip_parens(m.group(1))
        if not re.search(r"\bWHERE\b", body, flags=re.I):
            return True
        if re.search(r"\bWHERE\s+(true|1\s*=\s*1)\b", body, flags=re.I):
            return True
    return False


def block(op: str) -> None:
    sys.stderr.write(
        "DITOLAK: operasi destruktif ({op}) dikirim tanpa guard.\n\n"
        "Urutannya:\n"
        "  1. SELECT COUNT lebih dulu, tetapkan angka Harapan.\n"
        "  2. Tampilkan blok DESTRUKTIF (operasi - terdampak - Harapan - reversible), "
        "lalu BERHENTI dan tunggu jawaban user di sesi ini.\n"
        "  3. Eksekusi terbungkus DO block: RAISE EXCEPTION bila jumlah baris meleset "
        "dari Harapan, disusul SELECT verifikasi dalam panggilan yang sama.\n\n"
        "Exception membatalkan seluruh transaction, jadi nol data hilang saat angkanya "
        "tidak cocok.\n".format(op=op)
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
            block("UPDATE tanpa WHERE sempit")

    sys.exit(0)


if __name__ == "__main__":
    main()
