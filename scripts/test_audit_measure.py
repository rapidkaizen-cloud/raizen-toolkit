#!/usr/bin/env python3
"""Self-check audit_measure.js: the file is one function, and its colour arithmetic holds.

The function runs in a browser page, where no test of this repo reaches; its `selftest` mode
is the part that needs no page. Skipped, and said so, on a machine with no `node`.
Run directly: python3 test_audit_measure.py
"""
import shutil
import subprocess
from pathlib import Path

SCRIPT = Path(__file__).parent / "audit_measure.js"
RUN = "const t=require('fs').readFileSync(process.argv[1],'utf8');console.log((0,eval)('('+t+')')('selftest'))"


def main() -> None:
    text = SCRIPT.read_text(encoding="utf-8")
    # The brief pastes it as `const M = <this file>`: it must open as a function expression.
    assert text.startswith("function (mode) {"), text[:40]
    if not shutil.which("node"):
        print("audit_measure: skipped - no node on this machine")
        return
    done = subprocess.run(["node", "-e", RUN, str(SCRIPT)], capture_output=True, text=True, encoding="utf-8")
    assert done.returncode == 0 and done.stdout.strip() == "ok", done.stderr or done.stdout
    print("audit_measure: ok")


if __name__ == "__main__":
    main()
