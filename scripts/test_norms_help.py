#!/usr/bin/env python3
"""Self-check norms_help.py: the card holds the version, the commands, the pages and one entry.

The last case runs the script on this repo as the skill does. It fails when `README.md`
loses its `Use` heading or stops naming the skill there, because the card would then go
out with no commands and nothing else would say so.
Run directly: python3 test_norms_help.py
"""
import importlib.util
import json
import subprocess
import tempfile
from pathlib import Path

SCRIPT = Path(__file__).parent / "norms_help.py"

# `python3`, not sys.executable: the name the skill tells a session to run.
PYTHON = "python3"

spec = importlib.util.spec_from_file_location("norms_help", SCRIPT)
norms_help = importlib.util.module_from_spec(spec)
spec.loader.exec_module(norms_help)

README = """\
# the plugin

## Install

install text

## Use

| Situation | Run |
|---|---|
| New app | `/x:settle` |

## Update

update text
"""
PAGES = """\
# docs

| File | Holds |
|---|---|
| [guide/gates.md](guide/gates.md) | The stops |
"""
CHANGELOG = """\
# Changelog

Intro.

## [raizen-norms 0.3.0] - 2026-02-01

- third

To act on:

- rename the thing

## [raizen-norms 0.2.0] - 2026-01-10

- second
"""


def demo() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        (root / ".claude-plugin").mkdir()
        (root / ".claude-plugin" / "plugin.json").write_text(json.dumps({"version": "0.3.0"}), encoding="utf-8")

        # a copy holding nothing but its manifest still names its version, and adds no empty block
        assert norms_help.card(root) == "raizen-norms 0.3.0\n"

        (root / "docs").mkdir()
        (root / "README.md").write_text(README, encoding="utf-8")
        (root / "docs" / "README.md").write_text(PAGES, encoding="utf-8")
        (root / "CHANGELOG.md").write_text(CHANGELOG, encoding="utf-8")
        out = norms_help.card(root)

        assert out.startswith("raizen-norms 0.3.0\n")
        # the commands: the `Use` section alone
        assert "`/x:settle`" in out and "install text" not in out and "update text" not in out
        # the pages: the index without its title
        assert "guide/gates.md" in out and "# docs" not in out
        # the version's change: the top entry whole, and no older one
        assert "## [raizen-norms 0.3.0] - 2026-02-01" in out and "- rename the thing" in out
        assert "0.2.0" not in out and "- second" not in out
        assert out.index("COMMANDS") < out.index("PAGES") < out.index("LAST CHANGE")

    # as the skill runs it, on this repo: the real files must fill every block
    result = subprocess.run([PYTHON, str(SCRIPT)], capture_output=True)
    assert result.returncode == 0, result.stderr
    out = result.stdout.decode("utf-8")
    assert out.startswith("raizen-norms ")
    assert "COMMANDS" in out and "PAGES" in out and "LAST CHANGE" in out
    assert "/raizen-norms:norms-help" in out and "guide/help.md" in out
    assert out.count("\n## [") == 1

    print("ok")


if __name__ == "__main__":
    demo()
