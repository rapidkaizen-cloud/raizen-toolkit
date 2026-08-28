#!/usr/bin/env python3
"""Print the session norms, then the files a session must not start without.

SessionStart hook: stdout is added to the session context.

Everything printed here holds in every app repo, so it lives in the plugin rather
than in an app's CLAUDE.md — changing it then reaches every app through a plugin
update instead of an edit in N repositories. An app's CLAUDE.md keeps only what the
plugin cannot know: its stack, its locale, the rules that belong to that app alone,
and the two gates that must survive the plugin being absent.

`PRD.md` is injected rather than pointed at. A pointer is obeyed by judgement, and
the sessions that skip it are exactly the narrow ones where its prohibitions still
apply.
"""
import json
import sys
from pathlib import Path

NORMS = """\
SESSION NORMS (raizen-norms)

These hold in every app repo. The app's CLAUDE.md holds what is true of that app
alone; where the two disagree about a norm, this one is the newer.

LANGUAGE
The user's language and the repo's language are two different things. `PRD.md` is
injected below in the user's language, and it is the longest thing you will read
this session - do not let it decide the language of what you write.
  The user's language : chat, `PRD.md`, `QUEUE.md`, commit messages, pull
                        requests, and the strings the app puts on screen
  English, always     : comments, identifiers, file names, URL routes, API
                        endpoint paths, and every name in the database - tables,
                        columns, views, enum types, functions, policies, and
                        migration file names
  Decided per case    : enum values. They are stored data rather than a name, so
                        weigh readability against rewriting every existing row,
                        and map them to English keys at the boundary either way.
A route is an identifier the user happens to see - the menu label above it is the
thing written for them. A PRD term that names a thing in the code is translated on
the way in: a PRD that says "view kandidat" becomes `lead_candidates`, never
`lead_kandidat`. Existing code in the other language is a finding to report, not a
licence to match it.

POINTERS - read before touching
  Starting a page, or deciding what to build next : skill `build-flow`
  `PRD.md`                                        : skill `prd-format`
  UI, components, styling tokens                  : skill `ui-build`
  Schema, RLS, migrations                         : skill `db-ops`
  Queries, actions, handlers, keys, env vars      : skill `logic-build`
Skills load by judgement rather than by rule, and a new component triggers no file
read at all. Do not write new UI without reading `ui-build` first, and do not write a
key or an environment variable without reading `logic-build` Section 1 first.

SCOPE
Only what was asked. No refactor, no rename, no "while I'm here" outside scope.
Do not emit documentation that was not explicitly requested. `PRD.md` and `QUEUE.md`
are the only documents maintained in an app repo: `PRD.md` holds intent, `QUEUE.md`
holds what is not built yet.

GIT
Before anything else: `git fetch`, then check the branch position. HEAD on `main` -> stop.
Behind `origin/development` -> stop and say `git pull --ff-only`.

Committing is part of finishing, not a separate request:
  - A scope item that is finished is committed in the same turn, without asking first.
  - Name the paths explicitly. `git add -A` and `git add .` are refused.
  - Paths that changed outside SCOPE are findings reported to the user, never
    committed along.

Do not commit when you stop for one of the three legitimate stops in `build-flow`
Section 6 - the `db-ops` destructive gate, a role test that misses, a business rule
absent from the PRD. Leave the working tree dirty and report the stop instead. So at
the end of a session: a clean tree means finished, a dirty tree means something is
waiting on the user.

`main` never receives a direct commit. A push or a pull request is never started on
your own initiative - the user asks for it.

DECISIONS
An answer carrying two or more decisions, options, or recommendations closes with one
table: question - options - recommendation. An answer that only explains, with nothing
for anyone to choose, does not get one; a table where no decision is due only teaches
the reader to skip past every other table.
The recommendation column is never left out, and it names its trade-off. A
recommendation without a trade-off has not finished being thought through - no solution
is free, and where the price has not been found, say that it has not been found.
This comes before the work, while it can still change the plan. The block below is the
report afterwards, and neither replaces the other.

CLOSING THE SESSION
Report per scope item: what changed, or "UNTOUCHED". A scope item that did not change
is flagged. Then this block, always, even where the answer is "none":
  - Which page is usable now, and at which route
  - Which other pages were touched by spread
  - Which defaults you decided yourself
  - Unfinished steps, written as `QUEUE.md` lines rather than as sentences
  - What the user must do by hand
  - Which branch you are on and what you committed
  - PRD: written this session, and what needs the user's decision
A missing block is ambiguous between "none" and "forgot".
"""

# Sections that used to be rendered into an app's CLAUDE.md and are now owned by this
# plugin. A repo bootstrapped before a move still carries the old copy, and the two
# then contradict each other silently. Detection is by a phrase distinctive to the old
# template — add a line here whenever a section is retired.
STALE = [
    ("then check the branch position", "the git paragraph under 'Before touching anything'"),
    ("Uncommitted :", "the GIT block under 'Closing a session'"),
    ("Pointers — read before touching", "the Pointers table"),
    ("Read `PRD.md` at the start of a session", "the 'read PRD.md' line - the hook injects it now"),
    ("Only what was asked", "the Scope section"),
    ("Report per scope item", "the closing report"),
]

# A PRD past this length means `prd-format` has leaked and the file is accumulating
# status. It is still injected whole — a prohibition cut off at line 400 is worse than
# a long file — but the size is said out loud.
PRD_LINES_WARN = 400


def repo_root() -> Path:
    try:
        payload = json.load(sys.stdin)
    except Exception:
        payload = {}
    return Path(payload.get("cwd") or ".")


def read(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return ""


def inject(path: Path, what: str) -> None:
    text = read(path)
    if not text:
        return
    sys.stdout.write(f"\n--- {path.name} — {what} ---\n\n{text}\n")
    if path.name == "PRD.md":
        lines = text.count("\n") + 1
        if lines > PRD_LINES_WARN:
            sys.stdout.write(
                f"\nWARNING: PRD.md is {lines} lines. Past ~{PRD_LINES_WARN} it is "
                "carrying status rather than intent — read `prd-format` and say so to "
                "the user.\n"
            )


def stale_note(root: Path) -> None:
    text = read(root / "CLAUDE.md")
    if not text:
        return
    found = [label for phrase, label in STALE if phrase in text]
    if not found:
        return
    sys.stdout.write(
        "\nNOTE: CLAUDE.md still carries sections now owned by raizen-norms:\n"
        + "".join(f"  - {label}\n" for label in found)
        + "Tell the user to delete them; the plugin version above is authoritative.\n"
    )


def main() -> None:
    # On Windows stdout defaults to the ANSI codepage, which mangles anything the PRD
    # writes outside it — an em dash, a currency symbol, Indonesian quotation marks.
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

    root = repo_root()
    sys.stdout.write(NORMS)
    inject(root / "PRD.md", "intent and prohibitions")
    inject(root / "QUEUE.md", "what is not built yet")
    stale_note(root)
    sys.exit(0)


if __name__ == "__main__":
    main()
