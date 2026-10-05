---
name: app-align
description: Bring an app repo that predates these skills, or drifted from them, back onto the current conventions — platform residue, agent files, identifiers in the UI language, norms that silently cannot apply, stray or stale documents, a lint floor nothing enforces, rules no test names. Audits, ranks each finding by what it costs to leave, the user picks, one finding per commit. Never changes the stack or adds a feature. Use when a repo was migrated from another platform, or when the user asks whether an existing app follows the current rules.
---

# app-align — the app catches up with the rules

This skill changes **code that already exists**, and only where it disagrees with the conventions the installed plugin states. Documents are named by their `docs/` path; a repo with a root `PRD.md` reads each through `docs-format`'s legacy map.

## What a run costs — four rules

- **Only the audit subagent reads `references/audit.md`**, the one reference file — read it here only when no subagent can run.
- **Run independent reads, searches and commands in one turn** — parallel calls, or one chained command — because every extra model call re-reads the whole session.
- **Run the audit in one subagent on a cheaper model than the session's** (`sonnet` on Claude Code), briefed as Step 1 says, so what it reads never enters this session. No model choice → the session's model.
- **Never re-read what the session start printed** — the documents and the two listings.

## Hard limits

**Never opened on your own initiative.** A session that trips over a finding reports it in one line and carries on. Offer this skill through **AskUserQuestion**, once, with its evidence attached — the measured finding, what it costs to leave, a recommendation; a finding too thin to state in files and counts is a report line, not an offer. Declining closes the matter for the session.

**The stack is not on trial, and no decision is re-opened.** Remove what a departed platform left behind; never choose its replacement. Swapping a framework, a host, or a database is `app-settle` rework mode in a later session, and a finding only a new decision can settle is dropped at Step 4.

**No feature work and no drive-by fixes.** A bug found during the audit is a finding, reported and left: fixed inside an alignment commit, it hides from the diff that was approved.

**`DESIGN.md` is never written here**, by any path — `design-settle` owns it. Edit a living document only where the finding is the document claiming something the code has never done, and then only that line. Never edit a frozen record.

**The form is never changed.** A legacy repo is never migrated to `docs/`; a `docs/` repo never gets a root `PRD.md`.

**No new documents** — no audit report as a file, no migration plan, no committed checklist: the findings live in the session and the commits. `AGENTS.md` under C2 is the one file this skill may create, because it instructs agents and records nothing.

**An empty audit is a normal ending.** Close having changed nothing and say so; manufacture no finding.

## Step 0 — Preconditions

Run **in the app repo**, unlike `app-eval`. Print one block, filled from one turn of reads:

```
Repo         : [name · branch · clean or N uncommitted paths]
Documents    : [docs/ form / legacy PRD.md / missing]
CLAUDE.md    : [present — template-derived / present — hand-written / missing]
AGENTS.md    : [present / missing]
Plugin text  : [raizen-norms vX — the installed copy, which is what governs this repo]
Flow         : audit → rank → user picks → execute one finding per commit
```

- Branch `main` → **STOP**: the git guard refuses it, correctly.
- No PRD in either form → **STOP** and point to `app-settle` document mode; there is nothing to align to.
- **Working tree dirty → name the paths and STOP** until the user commits or stashes — a stop, not advice as in `logic-settle`, because this skill commits per finding and an approved diff must not carry somebody else's uncommitted work.
- **The installed plugin copy is the standard, not the toolkit repo's `master`** — an unreleased fix reaches no app. Read a rule's exact text from the installed plugin. A rule that looks wrong is a finding for `app-eval`, in the toolkit repo, in another session.

## Step 1 — Audit, before asking anything

**Run the audit in one subagent whose whole brief is `references/audit.md`**: hand it that path, the repo root, the installed plugin path, and every `NOTE` line the session start printed, and never read that file here. No subagent → say so and run the audit here from that file.

**It returns only the `AUDIT` block — seven rows, C1 to C7, a clean one included — with what each row counts listed under it.** Print it as returned.

Each row's cost if left, and the fix this skill allows:

- **C1 platform residue** — what still references the platform the app left.
- **C2 agent files** — a norm copied into `CLAUDE.md` contradicts the plugin once the plugin changes; a stale skill or command name sends the next session somewhere that is not there. **With no `AGENTS.md`, every agent that is not Claude Code works here with no rules at all** — no norms, no injected documents, no idea a shared set of components exists — and its first UI edit writes a second one: say that as the cost, and ask which other agents touch this repo, because the answer ranks the finding. Write the file to the shape `app-settle`'s `references/scaffold.md` gives (N5) — the `## UI` part, where `DESIGN.md` exists, as `design-settle`'s `pass.md` fills it under The lint floor; the `## Logic` part, where the `Data layer` row exists, as `logic-settle` Step 7 (`references/floor.md`) fills it; every path either names must resolve. **Never produce it by moving `CLAUDE.md`'s content or by linking the two**: they have different readers.
- **C3 language split** — rename only at Step 4, with the cost stated: a database name is a migration, a type regeneration, and every call site; a route is a link somebody may have bookmarked.
- **C4 guard coverage** — a norm that silently cannot apply here: the repo reads as protected and is not.
- **C5 documents** — a stray competes with `docs-format`'s closed list, and the loser goes stale silently. **Never rewrite a frozen record**: revert an edit made after freezing only on the user's word, and move what it meant to say to the living document or a superseding record. A missing living document is `app-settle`'s to seed; a missing guide page is a `docs/queue.md` line; a stale path is the one line corrected.
- **C6 lint floor** — two halves in one config behind one lint command, each proven as Step 4 orders.
  - **UI half, only where `DESIGN.md` exists** — without it there is nothing to derive a floor from, and `design-settle` writes both. With no floor, each session, and each agent that never loads `ui-build`, re-decides the design system by judgement. **The fix is `design-settle`'s lint floor, unchanged** (its `pass.md`, The lint floor), derived from this app's shared set and styling files, **existing hits baselined, not fixed**: repairing them is `design-settle`'s fix-the-drift path, a diff the user has not approved here. No linter in the repo → its install is one line inside the finding's cost-to-fix: a dev dependency, not the stack.
  - **Logic half, owed by every app with a database or a remote API** — with no `Data layer` row in `CLAUDE.md`, the first refusal has no path to scope to and the session-start listing prints nothing. **The fix is `logic-settle` Step 7's floor (`references/floor.md`), unchanged**: the folder named as that skill's Step 2 derives it, as found and never renamed; the five refusals derived from this app; everything already standing baselined. **Never move old call sites into the folder**: that is a migration priced in files, and `logic-settle` is where the user approves one.
- **C7 rule coverage** — an uncovered topic is a rule the next session, or another agent, can change while every page still renders. **Never write the test here**: a rule test attacks an enforcement point and a failing one is a bug, both build work. Write one `docs/queue.md` line per uncovered topic, `Prove: <topic>`, in `build-flow`'s shape, creating the file with its header where a finished app no longer has one. No runner → never ask here whether to install one: the build session that reaches the first line asks, under `logic-build`.

## Step 2 — Rank, with the cost of leaving each one

One table, worst first, ordered by **what breaks without anyone noticing**, never by how easy the fix is.

| Rank | Finding | Costs if left | Costs to fix |
|---|---|---|---|
| 1 | … | … | … |

Three bands, in this order:

1. **A guarantee that does not hold** — C4, a C6 floor that is absent or hollowed out, a C7 topic carrying money or permissions with no test, a missing `AGENTS.md` where the user named another agent working here, and any C1 row that can break an install or a build on a machine that has not run one yet. Silent until it is expensive.
2. **A rule that points somewhere wrong** — C2 stale names and an `AGENTS.md` path that does not resolve, a missing `AGENTS.md` where no other agent is in use yet, the remaining C7 topics, C5 documents — competing, stale, or edited after freezing. Costs the next session, every session.
3. **Drift that is merely untidy** — C3 renames whose blast radius exceeds their benefit, leftover files nobody reads.

**A fix whose cost exceeds what it buys is still listed**, in band 3, with the recommendation *leave it* — a column renamed for tidiness states its C3 cost rather than dropping the row.

## Step 3 — The user picks, then STOP

Put the ranked table up through **AskUserQuestion**, never as prose at the end of a turn. Assemble the options from the bands: band 1 only · bands 1 and 2 · everything · nothing. Recommend **band 1 only** unless the session has room and the bands below carry no migration. Individual lines are added or dropped through the answer or "Other". Then **STOP** and wait.

Nothing selected is a valid answer and a normal ending: close with the audit reported and no commits.

## Step 4 — Execute, one finding per commit

**One finding, one commit, named paths — never a batch**: a finding that turns out wrong is then one `git revert`, and the approved diff is the diff in the commit. Work in ranked order; a later finding that depends on an earlier one says so before the first is started.

Four checks bind every commit:

- **Anything touching build or run config gets one real run before the commit** — the build command, or the dev server reaching one page — because a config swap can type-check and not boot. It is the only check this skill requires.
- **A lint floor is proven before its commit, in the order `design-settle`'s `pass.md` gives under The lint floor** — the lint command over the whole app first, where every hit is either baselined or a pattern too wide to keep, then one planted violation per refusal seen refused, the scratch file deleted. A floor committed unrun is a C4 finding this skill wrote itself.
- **Anything touching the database is under `db-ops` unchanged** — the destructive gate, the mandatory order, the role test. A rename is destructive, however tidy.
- **A finding that turns out to need a decision is dropped, not decided** — the stack, a business rule absent from `docs/rules.md`, a prohibition nobody stated: stop on that line, leave the working tree as it stands, report it, and carry on with the next finding.

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

Never soften the last two rows. **`Verified` names what was executed**: a build that was not run is written as not run. **`For app-eval`** reports a rule that produced this drift; never fix it from inside the app repo — it is fixed in the toolkit repo, in another session (`app-eval` Step 0).
