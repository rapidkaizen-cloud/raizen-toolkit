#!/usr/bin/env python3
"""Self-check norms_version.py: the copy's own lines, and each thing origin can say about it.

Origin is a function handed in, so no case here needs the network except the last, which
runs the script as the skill does and passes whether or not origin answers.
Run directly: python3 test_norms_version.py
"""
import importlib.util
import json
import subprocess
import tempfile
from pathlib import Path

SCRIPT = Path(__file__).parent / "norms_version.py"

# `python3`, not sys.executable: the name the skill tells a session to run.
PYTHON = "python3"

spec = importlib.util.spec_from_file_location("norms_version", SCRIPT)
norms_version = importlib.util.module_from_spec(spec)
spec.loader.exec_module(norms_version)

OLD = """\
# Changelog

Intro naming the `raizen-norms` plugin.

## [raizen-norms 0.3.0] - 2026-02-01

- third

## [raizen-hub 0.9.0] - 2026-01-20

- hub alone

## [raizen-hub 0.8.0, raizen-norms 0.2.0] - 2026-01-10

- shared heading
"""
NEW = OLD.replace(
    "## [raizen-norms 0.3.0]",
    "## [raizen-norms 0.5.0] - 2026-03-01\n\n- fifth\n\nTo act on:\n\n- rename the thing\n\n"
    "## [raizen-norms 0.4.0] - 2026-02-15\n\n- fourth\n\n## [raizen-norms 0.3.0]",
)


def copy(root: Path, version: str, changelog: str = OLD) -> Path:
    (root / ".claude-plugin").mkdir(exist_ok=True)
    (root / ".claude-plugin" / "plugin.json").write_text(json.dumps({"version": version}), encoding="utf-8")
    (root / "CHANGELOG.md").write_text(changelog, encoding="utf-8")
    return root


def offline(name: str) -> str:
    raise OSError("no route")


def demo() -> None:
    found = norms_version.entries(OLD)
    assert [(own, date) for own, date, _ in found] == [("0.3.0", "2026-02-01"), ("", "2026-01-20"), ("0.2.0", "2026-01-10")]
    assert found[0][2].endswith("- third") and "hub alone" not in found[0][2]

    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)

        # current: its own entry, nothing listed as missing
        out = norms_version.report(copy(root, "0.3.0"), lambda name: OLD)
        assert out.startswith("raizen-norms 0.3.0\n")
        assert "Released        : 2026-02-01" in out
        assert "0.3.0 - this copy is current" in out
        assert "Not on this machine yet" not in out
        assert "- third" in out and "hub alone" not in out

        # behind: every entry above its own, newest first, `To act on` included
        out = norms_version.report(root, lambda name: NEW)
        assert "0.5.0 - this copy is behind, 2 newer" in out
        assert out.index("- fifth") < out.index("- fourth") < out.index("In this copy:")
        assert "- rename the thing" in out

        # behind, from a version under a shared heading: the hub's own entry counts as newer
        out = norms_version.report(copy(root, "0.2.0"), lambda name: NEW)
        assert "0.5.0 - this copy is behind, 4 newer" in out and "Released        : 2026-01-10" in out

        # behind, older than the changelog's first entry: everything in it is newer
        out = norms_version.report(copy(root, "0.1.0"), lambda name: OLD)
        assert "0.3.0 - this copy is behind, 3 newer" in out
        assert "no entry in this copy's CHANGELOG.md" in out

        # ahead: a copy not published yet lacks nothing
        out = norms_version.report(copy(root, "0.6.0"), lambda name: NEW)
        assert "0.5.0 - this copy is ahead" in out and "Not on this machine yet" not in out

        # origin unreachable: the copy's own lines still come, and no version is guessed
        out = norms_version.report(copy(root, "0.3.0"), offline)
        assert "Origin          : not reachable - no route" in out
        assert "Released        : 2026-02-01" in out and "- third" in out

        # more history on request
        out = norms_version.report(root, offline, count=2)
        assert "- third" in out and "hub alone" in out and "shared heading" not in out

        # a copy with no changelog still names its version
        (root / "CHANGELOG.md").unlink()
        assert norms_version.report(root, offline).startswith("raizen-norms 0.3.0\n")

    # as the skill runs it, on this copy: the real changelog must survive the console
    result = subprocess.run([PYTHON, str(SCRIPT)], capture_output=True)
    assert result.returncode == 0, result.stderr
    assert result.stdout.decode("utf-8").startswith("raizen-norms ")

    print("ok")


if __name__ == "__main__":
    demo()
