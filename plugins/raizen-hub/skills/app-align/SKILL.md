---
name: app-align
description: Bring an app repo that predates these skills, or drifted away from them, back onto the current conventions — dead-platform residue, a CLAUDE.md that duplicates the plugin, identifiers in the UI language, a norm that silently cannot apply here, documents that should not exist or have gone stale, a design system or a logic layer nothing enforces, business rules no test names. Audits the repo against the installed plugin text, ranks every finding by what it costs to leave, stops for the user to pick, then executes one finding per commit. Never changes the stack and never adds a feature. Use when a repo was migrated from another platform, or when the user asks whether an existing app follows the current rules.
---

# app-align — the app catches up with the rules

`app-settle` decides what the app is and writes its documents. `build-flow` builds pages that do not exist yet. This one changes **code that already exists**, and only where it disagrees with the conventions the plugins state today.

It exists because every other skill here reports and refuses to touch. `app-settle` document and rework modes say so outright — *no dependency added, none removed, no file refactored*. `app-eval` says the same pointing the other way — *fixing the app and fixing the toolkit are separate jobs*. This is the second of those two jobs, and it had no home.

Documents are named by their path in the `docs/` form; a repo with a root `PRD.md` reads each through `docs-format`'s legacy map.

**Not the same as rework.** Rework re-opens a decision. This one changes nothing that was decided — it makes the repo match a decision already taken. A finding that can only be settled by re-deciding the stack is not alignment work, and Step 4 stops on it.

## Hard limits

**Never opened on your own initiative.** A session that trips over a finding — a build config still importing the platform the app left, a route named in the UI language — reports it in one line and carries on. The offer to run this skill is made through **AskUserQuestion**, once, and only with its evidence attached: the measured finding, what it costs to leave, a recommendation. A finding too thin to state in files and counts is a report line, not an offer. Declining closes the matter for the session.

**The stack is not on trial.** Swapping a framework, a host, or a database is `app-settle` rework mode in a later session. This skill removes what a departed platform left behind; it does not choose the replacement platform.

**No feature work and no drive-by fixes.** A bug found during the audit is a finding, reported and left. Fixing it inside an alignment commit hides it from the diff that was approved.

**`DESIGN.md` is never written here**, by any path, for the reason `design-settle` owns it. A living document is edited only where a finding is the document itself claiming something the code has never done, and then only the one line. A frozen record is never edited.

**The form is never changed.** A legacy repo is never migrated to `docs/`, and a `docs/` repo never gets a root `PRD.md`.

**No new documents.** No audit report as a file, no migration plan, no checklist committed. The findings live in the session and in the commits. `AGENTS.md` under C2 is the one file this skill may create: it instructs agents and records nothing.

**An empty audit is a normal ending.** Close having changed nothing and say so. Do not manufacture a finding to justify the session.

## Step 0 — Preconditions

Runs **in the app repo**, unlike `app-eval`. Report one block:

```
Repo         : [name · branch · clean or N uncommitted paths]
Documents    : [docs/ form / legacy PRD.md / missing]
CLAUDE.md    : [present — template-derived / present — hand-written / missing]
AGENTS.md    : [present / missing]
Plugin text  : [raizen-norms vX · raizen-hub vY — the installed copies, which are what governs this repo]
Flow         : audit → rank → user picks → execute one finding per commit
```

Branch `main` → **STOP.** The git guard refuses it, and that refusal is correct.

No PRD in either form → **STOP**, point to `app-settle` document mode. Half the audit below reads the documents, and an alignment pass with nothing to align to is a preference pass.

**Working tree dirty → say it and stop.** Not advice here, unlike `logic-settle`: this skill commits per finding, and an approved diff that arrives carrying somebody else's uncommitted work is not the diff that was approved. Name the paths and let the user commit or stash first.

**The installed plugin copy is the standard, not the toolkit repo's `master`.** A rule fixed in the toolkit but not yet released reaches no app. Where the audit needs a rule's exact text, read it from the installed plugin. A rule that looks wrong is a finding for `app-eval`, in the toolkit repo, in another session.

## Step 1 — Audit, before asking anything

Seven categories. Every one runs, every one reports even when clean — a reader cannot tell *audited and clean* from *never audited* without the line.

```
AUDIT
C1 platform residue : [platform that left · what still references it — files, deps, lockfile hosts, agent files, MCP permissions]  or  [none]
C2 agent files      : [CLAUDE.md — N norms duplicated from the plugin · N stale skill or command names · missing Stack rows]
                      [AGENTS.md — missing · parts missing · N paths in its UI or Logic part that do not resolve]  or  [both clean]
C3 language split   : [N identifiers, routes, or database names in the UI language]  or  [clean]
C4 guard coverage   : [per norm that cannot apply here — which one, and why it is silent]  or  [every norm applies]
C5 documents       : [files outside docs-format's list · status columns or ticks in the queue · an empty queue]
                      [docs/ form — frozen records edited or missing their header · living documents missing
                      or unlisted · N tasks with no guide page · N stale paths]  or  [clean]
C6 lint floor       : [UI — absent · N of 4 refusals written]  or  [n/a — no DESIGN.md, `design-settle` writes it]
                      [logic — absent · N of 5 refusals written · Data layer row present / missing · N files calling the database outside the folder]
                      [N inline disables of floor rules · N floor rules lowered to a warning]  or  [clean]
C7 rule coverage    : [N rule topics · N quoted by a test title · runner — <name> / none]  or  [n/a — no rules]
```

**C1 — platform residue.** The app left a platform; the platform did not leave the app. Read the build config, `package.json` and the lockfile's resolved hosts, agent-facing files, and `.claude/settings*.json` permissions. A private registry belonging to a platform nobody uses any more is the row that matters most here: it is invisible until an install fails on a machine that has never run one.

**C2 — the agent files.** `CLAUDE.md` first: two failures, and they look alike. A norm the plugin now prints, copied into the file, will contradict the plugin the moment the plugin changes — and `session_norms.py` only detects the phrases of the old **English** template, so a hand-written or translated file is invisible to it. Separately, a name that no longer exists — a skill that was merged, a command that was renamed — sends the next session somewhere that is not there.

Then `AGENTS.md`, which `app-settle` N5 gives its shape. **Missing, it is not an untidy repo: every agent that is not Claude Code works here with no rules at all** — no norms, no injected documents, no idea a shared set of components exists — and its first UI edit writes a second one. Say that as the cost, and ask which other agents touch this repo, because that answer is what ranks the finding. The fix writes the file to that shape; where `DESIGN.md` exists the `## UI` part is filled from the repo as `design-settle` Step 6 fills it, where the `Data layer` row exists the `## Logic` part as `logic-settle` Step 7 fills it, and every path either names must resolve. **It is never produced by moving `CLAUDE.md`'s content or by linking the two**: they have different readers.

**C3 — language split.** `raizen-norms` puts identifiers, file names, routes, API paths, and every database name in English, whatever language the UI speaks. Count what deviates and name where. **Do not rename anything at this step** — a database name is a migration and a route is a link somebody may have bookmarked; both belong to Step 4 with their costs stated.

**C4 — guard coverage.** The row that pays for this audit. A norm that cannot apply here is worse than one plainly absent, because the repo reads as protected. Two known shapes: a `supabase/config.toml` whose `project_id` is not a hosted project ref, which makes `guard_project_ref` declare nothing and stay silent; and a `.claude/destructive-gate.off` marker nobody remembers setting. Where a norm is silent, say **which guarantee does not hold**, not merely that a file looks odd.

**C5 — the documents.** An app repo carries `docs-format`'s closed list, in the form it is on. Anything else that reads as a norm or a record — `ARCHITECTURE.md`, `DECISIONS.md`, a committed audit report — competes with it, and the loser goes stale silently. `CLAUDE.md` and `AGENTS.md` are not strays, and flagging one is the finding: they instruct agents rather than record the app. **A legacy repo is audited as legacy** — its root `PRD.md` and `QUEUE.md` are its list, its frontmatter-only `DESIGN.md` is not a stray, and an absent `docs/` is never a finding.

**In the `docs/` form, four more checks.** Every frozen record carries its header — `docs/PRD.md` its `Frozen` line, a finished change its `Done` line, a decision record its status — and `git log` shows no edit after it froze beyond a status set to superseded. Every living document exists, and `docs/README.md` lists what exists and nothing else. Every task the Roles name whose page is usable has its guide page. Every path a living document names resolves — the session-start hook prints those that do not. **The fix never rewrites a frozen record**: an edit made after freezing is reverted only on the user's word, and what it meant to say moves to the living document or a superseding record. A missing living document is `app-settle`'s to seed; a missing guide page is a `docs/queue.md` line; a stale path is the one line corrected.

**C6 — the lint floor.** Two halves, one config. The UI half is audited only where `DESIGN.md` exists; without it there is nothing to derive a floor from, and `design-settle` writes both. A `DESIGN.md` with no floor is the same shape as C4: the repo reads as having a design system, and nothing mechanical holds a single file to it — each session, and each agent that never loads `ui-build`, re-decides it by judgement. Count what is there against the four refusals `ui-build` names, then the two ways a floor is hollowed out from inside: inline disables of its rules, and rules lowered to a warning. **The fix is `design-settle` Step 6's lint floor, unchanged** — derived from this app's shared set and styling files, proven on what must pass before what must fail, and **existing hits baselined, not fixed**: repairing them is drift repair, which is `design-settle`'s fix-the-drift path and a diff the user has not approved here. Where the repo has no linter at all, the install is one line inside the finding's cost-to-fix — a dev dependency, not the stack.

The logic half is owed by every app with a database or a remote API, `DESIGN.md` or none. Count what is there against the five refusals `logic-build` Section 9 names, and read the `Data layer` row of `CLAUDE.md`: missing, the first refusal has no path to scope to and the session-start listing prints nothing. **The fix is `logic-settle` Step 7's floor, unchanged** — the folder named as that skill's Step 2 derives it, as found and never renamed; the five refusals derived from this app; the same two-step proof; and everything already standing baselined. **Moving old call sites into the folder is not alignment work**: it is a migration priced in files, and `logic-settle` is where the user approves one. Both halves land in one config behind one lint command.

**C7 — rule coverage.** `logic-build` Section 10 has every implemented rule leave a test whose title quotes its topic as `docs/rules.md` writes it, so coverage is a search: list the topics, search the test files for each. A topic no title carries is a rule the app enforces on nobody's word but the session's that wrote it — and the next session, or another agent, can change it while every page still renders. Report the count and name the uncovered topics. **The fix is never a test written here**: a rule test attacks an enforcement point, a failing one is a bug, and both are build work. It is one `docs/queue.md` line per uncovered topic, `Prove: <topic>`, in `build-flow`'s shape — the file created with its header where a finished app no longer has one. No runner in the repo → say so in the row; whether to install one is asked by the build session that reaches the first line, under `logic-build`.

## Step 2 — Rank, with the cost of leaving each one

One table, worst first. The order is by **what breaks without anyone noticing**, never by how easy the fix is.

| Rank | Finding | Costs if left | Costs to fix |
|---|---|---|---|
| 1 | … | … | … |

Three bands, in this order:

1. **A guarantee that does not hold** — C4, a C6 floor that is absent or hollowed out, a C7 topic carrying money or permissions with no test, a missing `AGENTS.md` where the user named another agent working here, and any C1 row that can break an install or a build on a machine that has not run one yet. Silent until it is expensive.
2. **A rule that points somewhere wrong** — C2 stale names and an `AGENTS.md` path that does not resolve, a missing `AGENTS.md` where no other agent is in use yet, the remaining C7 topics, C5 documents — competing, stale, or edited after freezing. Costs the next session, every session.
3. **Drift that is merely untidy** — C3 renames whose blast radius exceeds their benefit, leftover files nobody reads.

**A fix whose cost exceeds what it buys is still listed**, in band 3, with the recommendation *leave it*. A database column renamed for tidiness is a migration, a type regeneration, and every call site — say that plainly rather than dropping the row.

## Step 3 — The user picks, then STOP

Put the ranked table up through **AskUserQuestion**, never as prose at the end of a turn. Options are assembled from the bands: take band 1 only, take bands 1 and 2, take everything, take nothing. The recommendation is **band 1 only** unless the session has room and the bands below carry no migration.

Individual lines are added or dropped through the answer or "Other". Then **STOP** and wait.

Nothing selected is a valid answer and a normal ending. Close with the audit reported and no commits.

## Step 4 — Execute, one finding per commit

**One finding, one commit, named paths.** Not a batch. A finding that turns out wrong is then one `git revert`, and the diff the user approved is the diff in the commit.

Order: as ranked. A later finding that depends on an earlier one says so before the first is started.

Four checks bind every commit:

- **Anything touching build or run config gets one real run before the commit** — the build command, or the dev server reaching one page. A config swap that type-checks and does not boot is the failure mode this catches, and it is the only check this skill requires.
- **A lint floor is proven before its commit, in the order `design-settle`'s `pass.md` gives under The lint floor** — the lint command over the whole app first, where every hit is either baselined or a pattern too wide to keep, then one planted violation per refusal seen refused, the scratch file deleted. A floor committed unrun is a C4 finding this skill wrote itself.
- **Anything touching the database is under `db-ops` unchanged** — the destructive gate, the mandatory order, the role test. A rename is destructive; it does not become safe by being tidy.
- **A finding that turns out to need a decision is dropped, not decided.** The stack, a business rule absent from `docs/rules.md`, a prohibition nobody stated: stop on that line, leave the working tree as it stands, report it, and carry on with the next finding.

**Scope is the selected lines and nothing else.** A path that changed outside them is reported, never committed along — the `raizen-norms` rule, unchanged.

## Step 5 — Close

```
ALIGN
Fixed        : [one line per finding, with the commit]
Dropped      : [findings that needed a decision — and which decision]
Left         : [band 3 lines the user declined, or that were recommended to leave]
Still silent : [any C4 guarantee that is still not in force, and why]
Verified     : [what was actually run — the build, the page, the role test]
For app-eval : [findings that are defects in the rules rather than in this app — or "none"]
```

The last two rows are the ones that must not be softened. **`Verified` names what was executed**, and a build that was not run is written as not run. **`For app-eval`** is how a rule that produced this drift gets back to the toolkit: it is reported here and fixed there, in the toolkit repo, in another session. Fixing the rule from inside the app repo is the exact thing `app-eval` Step 0 exists to prevent.
