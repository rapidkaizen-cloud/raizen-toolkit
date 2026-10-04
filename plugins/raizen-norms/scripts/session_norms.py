#!/usr/bin/env python3
"""Print the session norms, then the files a session must not start without.

SessionStart hook on Claude Code: stdout is added to the session context. Antigravity
has no such event, so the same script runs as its PreInvocation hook - before every
model call - and hands the same text over once per conversation, as an injected step.

Everything printed here holds in every app repo, so it lives in the plugin rather
than in an app's CLAUDE.md — changing it then reaches every app through a plugin
update instead of an edit in N repositories. An app's CLAUDE.md keeps only what the
plugin cannot know: its stack, its locale, the rules that belong to that app alone,
and the two gates that must survive the plugin being absent.

The documents are injected rather than pointed at. A pointer is obeyed by judgement,
and the sessions that skip it are exactly the narrow ones where its prohibitions still
apply. A repo with a root `PRD.md` is on the legacy form and gets `PRD.md` and
`QUEUE.md`, exactly as before the `docs/` form existed; any other repo gets the `docs/`
form's block, and with `docs/PRD.md` the three living documents `docs-format` names —
never the frozen ones.

The two inventories — components, and the data layer's functions — are printed for
the same reason. `ui-build` orders a listing
of the components folder before any element is written, and a skill is loaded by
judgement — a session that never loads it hunts for `Pagination`, misses `Pager`, and
writes it a second time. It is printed here rather than from a PreToolUse hook on
Write because that hook's additionalContext lands beside the tool result: after the
file is already written.
"""
import contextlib
import io
import json
import os
import re
import sys
from pathlib import Path

import handoff
import host

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
  `PRD.md`                                        : skill `docs-format`
  UI, components, styling tokens                  : skill `ui-build`
  Schema, RLS, migrations                         : skill `db-ops`
  Queries, actions, handlers, keys, env vars      : skill `logic-build`
Skills load by judgement rather than by rule, and a new component triggers no file
read at all - so the components and the data-layer functions this repo already has
are listed at the end of this block, wherever it has any. Do not write new UI without
reading `ui-build` first, do not write a query without reading `logic-build` first,
and do not write a key or an environment variable without its Section 1.

SCOPE
Only what was asked. No refactor, no rename, no "while I'm here" outside scope.
Do not emit documentation that was not explicitly requested. `PRD.md` and `QUEUE.md`
are the only documents maintained in an app repo: `PRD.md` holds intent, `QUEUE.md`
holds what is not built yet.

GIT
Before anything else: `git fetch`, then check the branch position. HEAD on `main` -> stop.
Behind `origin/development` -> stop and ask to run `git pull --ff-only`.

Committing is part of finishing, not a separate request:
  - A scope item that is finished is committed in the same turn, without asking first.
  - Name the paths explicitly. `git add -A` and `git add .` are refused.
  - The message states why, not only what - the diff already shows the what.
  - Paths that changed outside SCOPE are findings reported to the user, never
    committed along.

Do not commit when you stop for one of the three legitimate stops in `build-flow`
Section 6 - the `db-ops` destructive gate, a role test that misses, a business rule
absent from the PRD. Leave the working tree dirty and report the stop instead. So at
the end of a session: a clean tree means finished, a dirty tree means something is
waiting on the user.

`main` never receives a direct commit. A push or a pull request runs only after the
user picks `Run` on an AskUserQuestion naming its exact command - `guard_git` reads
that answer, and one answer covers one run. Under the command, the question lists
every commit it publishes as `- ` bullets, one per commit: short hash and subject.
It offers two options, `Run` and `Cancel`.

ASKING
A decision that is the user's is asked through AskUserQuestion, or answered in chat at
a hard stop; then you run it yourself. Never hand the user a command to type - only
what needs their own hands: a browser login, a dashboard, a key rotation, a payment.

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

# The block above is the legacy form's, printed byte for byte where a root `PRD.md`
# exists. The `docs/` form differs only where the block names a document.
DOCS_FORM = [
    (
        "`PRD.md` is\ninjected below in the user's language, and it is the longest thing you will read\n"
        "this session - do not let it decide the language of what you write.\n",
        "The `docs/`\nfiles are injected below in the user's language - do not let them decide the\n"
        "language of what you write.\n",
    ),
    (
        "  The user's language : chat, `PRD.md`, `QUEUE.md`, commit messages, pull\n"
        "                        requests, and the strings the app puts on screen\n",
        "  The user's language : chat, `docs/`, the prose of `DESIGN.md` and `README.md`,\n"
        "                        commit messages, pull requests, and the strings the\n"
        "                        app puts on screen\n",
    ),
    ("A PRD term that names", "A term that names"),
    ("a PRD that says", "a glossary that says"),
    (
        "  `PRD.md`                                        : skill `docs-format`\n",
        "  `docs/`, `DESIGN.md`, `README.md`               : skill `docs-format`\n",
    ),
    (
        "Do not emit documentation that was not explicitly requested. `PRD.md` and `QUEUE.md`\n"
        "are the only documents maintained in an app repo: `PRD.md` holds intent, `QUEUE.md`\n"
        "holds what is not built yet.\n",
        "Write no document outside the closed list in `docs-format`, and keep every listed\n"
        "one true in the commit that changes what it says. `docs/queue.md` holds what is\n"
        "not built yet.\n",
    ),
    (
        "absent from the PRD. Leave the working tree dirty and report the stop instead. So at\n"
        "the end of a session: a clean tree means finished, a dirty tree means something is\n"
        "waiting on the user.\n",
        "absent from `docs/rules.md`. Leave the working tree dirty and report the stop\n"
        "instead. So at the end of a session: a clean tree means finished, a dirty tree\n"
        "means something is waiting on the user.\n",
    ),
    ("written as `QUEUE.md` lines", "written as `docs/queue.md` lines"),
    (
        "  - PRD: written this session, and what needs the user's decision\n",
        "  - Docs: which files of `docs-format`'s list this session changed, and what\n"
        "    needs the user's decision\n",
    ),
]

# The living documents a `docs/` repo gets at every session start. The frozen ones —
# `docs/PRD.md`, `docs/changes/`, the decision records — are history and never printed.
LIVING = [
    ("docs/README.md", "the index"),
    ("docs/product.md", "context, roles, prohibitions"),
    ("docs/queue.md", "what is not built yet"),
]
# Living documents whose named paths are checked. Frozen records may name paths that are
# gone on purpose, `whats-new.md` is dated history, and the queue names files not built yet.
PATH_CHECKED = ["README.md", "product.md", "rules.md", "glossary.md"]
LINK = re.compile(r"\]\(([^)\s]+)\)")
TICKED = re.compile(r"`([^`\s]+)`")
FILE_EXT = re.compile(r"\.(md|mdx|[cm]?[jt]sx?|json|toml|ya?ml|s?css|sql|py|dart|kt|swift|vue|svelte|astro|html|sh)$")
STALE_MAX = 20


def docs_norms() -> str:
    text = NORMS
    for old, new in DOCS_FORM:
        text = text.replace(old, new)
    return text


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

# A PRD past this length means `docs-format` has leaked and the file is accumulating
# status. It is still injected whole — a prohibition cut off at line 400 is worse than
# a long file — but the size is said out loud.
PRD_LINES_WARN = 400


# The norms and the skills are written in Claude Code's vocabulary. A session on another
# host gets this block after them, and it is the only place the two are mapped.
HOST_ANTIGRAVITY = """\

HOST - Antigravity
The norms above and every skill name Claude Code's tools. Use this host's own:
  AskUserQuestion            : `ask_question`
  the Bash, PowerShell tools : `run_command`
  a subagent, the Agent tool : `invoke_subagent`
  an `mcp__server__tool`     : `call_mcp_tool` with that server and tool
Write the todo list `build-flow` requires in chat, since this host has no tool for one.
`CLAUDE.md` is printed below, because this host does not load it.
This host loads `AGENTS.md`, which was written for a session without these norms -
where the two disagree, these norms hold.
"""

MARK = NORMS.splitlines()[0]


def printed(transcript: str) -> bool:
    """True when this conversation was already handed the norms."""
    try:
        with open(transcript, encoding="utf-8", errors="replace") as f:
            return any(MARK in line for line in f)
    except OSError:
        return False


def read(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return ""


def inject(root: Path, rel: str, what: str) -> None:
    text = read(root / rel)
    if not text:
        return
    sys.stdout.write(f"\n--- {rel} — {what} ---\n\n{text}\n")
    if rel == "PRD.md":
        lines = text.count("\n") + 1
        if lines > PRD_LINES_WARN:
            sys.stdout.write(
                f"\nWARNING: PRD.md is {lines} lines. Past ~{PRD_LINES_WARN} it is "
                "carrying status rather than intent — read `docs-format` and say so to "
                "the user.\n"
            )


# Where components live, by the folder name every stack in the rubric converges on.
# ponytail: a name heuristic, not a declared path. A repo keeping its shared set under
# another name is listed as nothing; read the path from the app's own files when one does.
UI_DIRS = {"components", "widgets"}
PRUNE = {"node_modules", "dist", "build", "out", "target", "vendor", "coverage", "design-canvas"}
SKIP_FILES = (".test.", ".spec.", ".stories.")
INVENTORY_MAX = 60  # files listed; the rest are counted, so the cost per session is bounded
INVENTORY_DEPTH = 5  # how deep a components folder is looked for, not how deep one is read

# Capitalised names only: a variants helper or a hook is not a component, and listing
# it buries the ones that are.
JS_DECLARED = re.compile(r"export\s+(?:default\s+)?(?:async\s+)?(?:function|const|class)\s+([A-Z]\w*)")
JS_BRACED = re.compile(r"export\s*\{([^}]*)\}")
NAMES = {
    ".tsx": None,
    ".jsx": None,
    ".vue": "stem",
    ".svelte": "stem",
    ".astro": "stem",
    ".dart": re.compile(r"class\s+([A-Z]\w*)\s+extends\s+\w*Widget\b"),
    ".kt": re.compile(r"@Composable(?:\s+@?\w+(?:\([^)]*\))?)*?\s+fun\s+([A-Z]\w*)"),
    ".swift": re.compile(r"struct\s+([A-Z]\w*)\s*:[^{]*\bView\b"),
}


def component_names(path: Path) -> list:
    rule = NAMES[path.suffix]
    if rule == "stem":
        return [path.stem]
    text = read(path)
    if rule is not None:
        return rule.findall(text)
    names = JS_DECLARED.findall(text)
    for group in JS_BRACED.findall(text):
        for item in group.split(","):
            # `Dialog as Trigger` exports Trigger; `type Props` exports no component
            name = item.split(" as ")[-1].strip()
            if name[:1].isupper() and " " not in name:
                names.append(name)
    # `IMPORT_STEPS` is capitalised and is a constant
    return [n for n in dict.fromkeys(names) if not n.isupper()]


def component_files(root: Path) -> list:
    found = []
    for cur, dirs, files in os.walk(root):
        rel = Path(cur).relative_to(root)
        inside = any(part.lower() in UI_DIRS for part in rel.parts)
        dirs[:] = [
            d for d in dirs
            if not d.startswith(".") and d not in PRUNE
            and (inside or d.lower() in UI_DIRS or len(rel.parts) < INVENTORY_DEPTH)
        ]
        if inside:
            found += [
                rel / f for f in files
                if Path(f).suffix in NAMES and not any(s in f for s in SKIP_FILES)
            ]
    return sorted(found, key=lambda p: (len(p.parts), p.as_posix()))


def inventory(root: Path) -> None:
    try:
        files = component_files(root)
    except OSError:
        return
    if not files:
        return
    sys.stdout.write(
        "\n--- Components already in this repo - reuse before writing a new one ---\n\n"
        "A listing, not the rule: `ui-build` is still read before any UI is written, and\n"
        "the file holding the shared set is still read whole.\n\n"
    )
    for rel in files[:INVENTORY_MAX]:
        names = component_names(root / rel)
        sys.stdout.write(rel.as_posix() + (": " + ", ".join(names) if names else "") + "\n")
    if len(files) > INVENTORY_MAX:
        sys.stdout.write(f"... {len(files) - INVENTORY_MAX} more files - list the folder.\n")


# The data layer is read from the row `logic-settle` writes into the app's Stack table,
# never guessed from a folder name: `lib`, `services`, `data`, and `api` all occur, and a
# wrong guess lists utilities as if they were queries. No row → nothing is printed.
DATA_ROW = re.compile(r"^\|\s*Data layer\s*\|\s*([^|]+)\|", re.I | re.M)
DATA_SUFFIXES = {".ts", ".tsx", ".js", ".jsx", ".mjs"}
DATA_MAX_FILES = 40
DATA_MAX_NAMES = 12
FN_DECLARED = re.compile(r"export\s+(?:async\s+)?(?:function\s+|const\s+)([A-Za-z_]\w*)")


def function_names(path: Path) -> list:
    # ponytail: JS and TS only. Another language lists its files by name; add its
    # declaration pattern here when an app on that stack has a data layer to list.
    if path.suffix not in DATA_SUFFIXES:
        return []
    text = read(path)
    names = FN_DECLARED.findall(text)
    for group in JS_BRACED.findall(text):
        for item in group.split(","):
            name = item.split(" as ")[-1].strip()
            if name and " " not in name:
                names.append(name)
    return [n for n in dict.fromkeys(names) if not n.isupper()]


def data_layer(root: Path) -> None:
    row = DATA_ROW.search(read(root / "CLAUDE.md"))
    if not row:
        return
    cell = row.group(1).strip()
    ticked = re.search(r"`([^`]+)`", cell)
    rel = (ticked.group(1) if ticked else cell.split()[0]).strip("/\\")
    folder = (root / rel).resolve()
    if root.resolve() not in folder.parents:
        return
    if not folder.is_dir():
        sys.stdout.write(
            f"\nNOTE: the Data layer row of CLAUDE.md names `{rel}`, and no such folder "
            "exists. The lint floor scoped to it guards nothing. Tell the user.\n"
        )
        return
    files = sorted(
        (
            p.relative_to(root) for p in folder.rglob("*")
            if p.is_file() and not p.name.endswith(".d.ts")
            and not any(s in p.name for s in SKIP_FILES)
            and not any(part in PRUNE or part.startswith(".") for part in p.relative_to(root).parts)
        ),
        key=lambda p: (len(p.parts), p.as_posix()),
    )
    if not files:
        return
    sys.stdout.write(
        f"\n--- Data layer of this repo ({rel}) - call what exists before writing a query ---\n\n"
        "A listing, not the rule: `logic-build` is still read before a query, an action,\n"
        "or a handler is written, and no database call is written outside this folder.\n\n"
    )
    for path in files[:DATA_MAX_FILES]:
        names = function_names(root / path)
        shown = names[:DATA_MAX_NAMES]
        if len(names) > DATA_MAX_NAMES:
            shown.append(f"+{len(names) - DATA_MAX_NAMES}")
        sys.stdout.write(path.as_posix() + (": " + ", ".join(shown) if shown else "") + "\n")
    if len(files) > DATA_MAX_FILES:
        sys.stdout.write(f"... {len(files) - DATA_MAX_FILES} more files - list the folder.\n")


def named_paths(doc: Path, root: Path) -> list:
    """Paths a living document names that do not exist: link targets resolved from the
    document's folder, backticked paths from the repo root."""
    # ponytail: a shape heuristic — a backticked token with a slash or a known file
    # extension. A backticked `and/or` reads as a path; widen the skip list when one shows up.
    text = read(doc)
    missing = []
    for target in LINK.findall(text):
        target = target.split("#")[0]
        if not target or "://" in target or target.startswith(("mailto:", "/")):
            continue
        if not (doc.parent / target).exists():
            missing.append(target)
    for token in TICKED.findall(text):
        if token.startswith(("/", "~", "$", "-", "http", "@")) or any(c in token for c in "<>*{}()=:"):
            continue
        first = token.split("/")[0]
        if "/" not in token and not FILE_EXT.search(token):
            continue
        if "." in first.lstrip(".") and "/" in token:
            continue  # a host name, not a folder
        if not (root / token).exists():
            missing.append(token)
    return list(dict.fromkeys(missing))


def stale_paths(root: Path) -> None:
    docs = root / "docs"
    files = [docs / name for name in PATH_CHECKED] + sorted((docs / "guide").glob("**/*.md"))
    found = []
    for doc in files:
        if doc.is_file():
            found += [f"{doc.relative_to(root).as_posix()}: `{p}`" for p in named_paths(doc, root)]
    if not found:
        return
    sys.stdout.write(
        "\nNOTE: these living documents name paths that do not exist:\n"
        + "".join(f"  - {line}\n" for line in found[:STALE_MAX])
        + (f"  ... {len(found) - STALE_MAX} more\n" if len(found) > STALE_MAX else "")
        + "A commit that moved them should have corrected the document (`docs-format`,\n"
        "same commit). Tell the user, and correct them in this session's scope.\n"
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


def emit(root: Path, payload: dict) -> None:
    on_antigravity = payload.get("host") == host.ANTIGRAVITY
    tail = HOST_ANTIGRAVITY if on_antigravity else ""
    if (root / "PRD.md").is_file():
        sys.stdout.write(NORMS + tail)
        inject(root, "PRD.md", "intent and prohibitions")
        inject(root, "QUEUE.md", "what is not built yet")
    elif (root / "docs" / "PRD.md").is_file():
        sys.stdout.write(docs_norms() + tail)
        for rel, what in LIVING:
            inject(root, rel, what)
        for rel in ("docs/README.md", "docs/product.md"):
            if not (root / rel).is_file():
                sys.stdout.write(
                    f"\nNOTE: {rel} is missing. `app-settle` seeds it from docs/PRD.md - tell the user.\n"
                )
        stale_paths(root)
    else:
        # No PRD in either form: an empty directory, an app not documented yet, or a repo
        # that is not an app. The docs block is the form app-settle will write; a root
        # QUEUE.md is still the only queue such a repo has.
        sys.stdout.write(docs_norms() + tail)
        inject(root, "QUEUE.md", "what is not built yet")
    if on_antigravity:
        inject(root, "CLAUDE.md", "what is true of this app alone")
    stale_note(root)
    inventory(root)
    data_layer(root)
    sys.stdout.write(handoff.note(root, payload.get("host") or host.CLAUDE, payload.get("transcript_path") or ""))


def main() -> None:
    # On Windows stdout defaults to the ANSI codepage, which mangles anything the PRD
    # writes outside it — an em dash, a currency symbol, Indonesian quotation marks.
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

    payload = host.read_payload()
    root = Path(payload.get("cwd") or ".")
    if payload.get("host") != host.ANTIGRAVITY:
        emit(root, payload)
        sys.exit(0)

    # PreInvocation fires before every model call. The norms go in before the first call
    # of a conversation that has not been handed them: the first call of a turn is the
    # only one that checks, and the transcript is what remembers across turns.
    if payload.get("invocationNum") or printed(payload.get("transcript_path") or ""):
        sys.exit(0)
    text = io.StringIO()
    with contextlib.redirect_stdout(text):
        emit(root, payload)
    # A user-role step stays in the conversation; an `ephemeralMessage` is gone after one call.
    json.dump({"injectSteps": [{"userMessage": text.getvalue()}]}, sys.stdout)
    sys.exit(0)


if __name__ == "__main__":
    main()
