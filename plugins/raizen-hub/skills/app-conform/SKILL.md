---
name: app-conform
description: Bring an app repo that predates these skills, or drifted away from them, back onto the current conventions — dead-platform residue, a CLAUDE.md that duplicates the plugin, identifiers in the UI language, a norm that silently cannot apply here, documents that should not exist. Audits the repo against the installed plugin text, ranks every finding by what it costs to leave, stops for the user to pick, then executes one finding per commit. Never changes the stack and never adds a feature. Use when a repo was migrated from another platform, or when the user asks whether an existing app follows the current rules.
---

# app-conform — the app catches up with the rules

`app-settle` decides what the app is and writes `PRD.md`. `build-flow` builds pages that do not exist yet. This one changes **code that already exists**, and only where it disagrees with the conventions the plugins state today.

It exists because every other skill here reports and refuses to touch. `app-settle` document and rework modes say so outright — *no dependency added, none removed, no file refactored*. `app-eval` says the same pointing the other way — *fixing the app and fixing the toolkit are separate jobs*. This is the second of those two jobs, and it had no home.

**Not the same as rework.** Rework re-opens a decision. This one changes nothing that was decided — it makes the repo match a decision already taken. A finding that can only be settled by re-deciding the stack is not conform work, and Step 4 stops on it.

## Hard limits

**Never opened on your own initiative.** A session that trips over a finding — a build config still importing the platform the app left, a route named in the UI language — reports it in one line and carries on. The offer to run this skill is made through **AskUserQuestion**, once, and only with its evidence attached: the measured finding, what it costs to leave, a recommendation. A finding too thin to state in files and counts is a report line, not an offer. Declining closes the matter for the session.

**The stack is not on trial.** Swapping a framework, a host, or a database is `app-settle` rework mode in a later session. This skill removes what a departed platform left behind; it does not choose the replacement platform.

**No feature work and no drive-by fixes.** A bug found during the audit is a finding, reported and left. Fixing it inside a conform commit hides it from the diff that was approved.

**`PRD.md` Section 5 is never written here**, by any path, for the reason `design-settle` owns it. Sections 1 and 6 are edited only where a finding is the PRD itself claiming something the code has never done, and then only the one line.

**No new documents.** No audit report as a file, no migration plan, no checklist committed. The findings live in the session and in the commits.

**An empty audit is a normal ending.** Close having changed nothing and say so. Do not manufacture a finding to justify the session.

## Step 0 — Preconditions

Runs **in the app repo**, unlike `app-eval`. Report one block:

```
Repo         : [name · branch · clean or N uncommitted paths]
PRD.md       : [present / missing]
CLAUDE.md    : [present — template-derived / present — hand-written / missing]
Plugin text  : [raizen-norms vX · raizen-hub vY — the installed copies, which are what governs this repo]
Flow         : audit → rank → user picks → execute one finding per commit
```

Branch `main` → **STOP.** The git guard refuses it, and that refusal is correct.

`PRD.md` missing → **STOP**, point to `app-settle` document mode. Half the audit below reads the PRD, and a conform pass with nothing to conform to is a preference pass.

**Working tree dirty → say it and stop.** Not advice here, unlike `logic-settle`: this skill commits per finding, and an approved diff that arrives carrying somebody else's uncommitted work is not the diff that was approved. Name the paths and let the user commit or stash first.

**The installed plugin copy is the standard, not the toolkit repo's `master`.** A rule fixed in the toolkit but not yet released reaches no app. Where the audit needs a rule's exact text, read it from the installed plugin. A rule that looks wrong is a finding for `app-eval`, in the toolkit repo, in another session.

## Step 1 — Audit, before asking anything

Five categories. Every one runs, every one reports even when clean — a reader cannot tell *audited and clean* from *never audited* without the line.

```
AUDIT
C1 platform residue : [platform that left · what still references it — files, deps, lockfile hosts, agent files, MCP permissions]  or  [none]
C2 CLAUDE.md        : [N norms duplicated from the plugin · N stale skill or command names · missing Stack rows]  or  [template-derived, clean]
C3 language split   : [N identifiers, routes, or database names in the UI language]  or  [clean]
C4 guard coverage   : [per norm that cannot apply here — which one, and why it is silent]  or  [every norm applies]
C5 stray documents  : [files outside PRD.md and QUEUE.md · status columns or ticks in QUEUE.md · an empty QUEUE.md]  or  [none]
```

**C1 — platform residue.** The app left a platform; the platform did not leave the app. Read the build config, `package.json` and the lockfile's resolved hosts, agent-facing files, and `.claude/settings*.json` permissions. A private registry belonging to a platform nobody uses any more is the row that matters most here: it is invisible until an install fails on a machine that has never run one.

**C2 — `CLAUDE.md`.** Two failures, and they look alike. A norm the plugin now prints, copied into the file, will contradict the plugin the moment the plugin changes — and `session_norms.py` only detects the phrases of the old **English** template, so a hand-written or translated file is invisible to it. Separately, a name that no longer exists — a skill that was merged, a command that was renamed — sends the next session somewhere that is not there.

**C3 — language split.** `raizen-norms` puts identifiers, file names, routes, API paths, and every database name in English, whatever language the UI speaks. Count what deviates and name where. **Do not rename anything at this step** — a database name is a migration and a route is a link somebody may have bookmarked; both belong to Step 4 with their costs stated.

**C4 — guard coverage.** The row that pays for this audit. A norm that cannot apply here is worse than one plainly absent, because the repo reads as protected. Two known shapes: a `supabase/config.toml` whose `project_id` is not a hosted project ref, which makes `guard_project_ref` declare nothing and stay silent; and a `.claude/destructive-gate.off` marker nobody remembers setting. Where a norm is silent, say **which guarantee does not hold**, not merely that a file looks odd.

**C5 — stray documents.** `PRD.md` and `QUEUE.md` are the two documents an app repo carries. Anything else that reads as a norm or a record — `ARCHITECTURE.md`, `DECISIONS.md`, a committed audit report — competes with them, and the loser goes stale silently.

## Step 2 — Rank, with the cost of leaving each one

One table, worst first. The order is by **what breaks without anyone noticing**, never by how easy the fix is.

| Rank | Finding | Costs if left | Costs to fix |
|---|---|---|---|
| 1 | … | … | … |

Three bands, in this order:

1. **A guarantee that does not hold** — C4, and any C1 row that can break an install or a build on a machine that has not run one yet. Silent until it is expensive.
2. **A rule that points somewhere wrong** — C2 stale names, C5 competing documents. Costs the next session, every session.
3. **Drift that is merely untidy** — C3 renames whose blast radius exceeds their benefit, leftover files nobody reads.

**A fix whose cost exceeds what it buys is still listed**, in band 3, with the recommendation *leave it*. A database column renamed for tidiness is a migration, a type regeneration, and every call site — say that plainly rather than dropping the row.

## Step 3 — The user picks, then STOP

Put the ranked table up through **AskUserQuestion**, never as prose at the end of a turn. Options are assembled from the bands: take band 1 only, take bands 1 and 2, take everything, take nothing. The recommendation is **band 1 only** unless the session has room and the bands below carry no migration.

Individual lines are added or dropped through the answer or "Other". Then **STOP** and wait.

Nothing selected is a valid answer and a normal ending. Close with the audit reported and no commits.

## Step 4 — Execute, one finding per commit

**One finding, one commit, named paths.** Not a batch. A finding that turns out wrong is then one `git revert`, and the diff the user approved is the diff in the commit.

Order: as ranked. A later finding that depends on an earlier one says so before the first is started.

Three checks bind every commit:

- **Anything touching build or run config gets one real run before the commit** — the build command, or the dev server reaching one page. A config swap that type-checks and does not boot is the failure mode this catches, and it is the only check this skill requires.
- **Anything touching the database is under `db-ops` unchanged** — the destructive gate, the mandatory order, the role test. A rename is destructive; it does not become safe by being tidy.
- **A finding that turns out to need a decision is dropped, not decided.** The stack, a business rule absent from the PRD, a prohibition nobody stated: stop on that line, leave the working tree as it stands, report it, and carry on with the next finding.

**Scope is the selected lines and nothing else.** A path that changed outside them is reported, never committed along — the `raizen-norms` rule, unchanged.

## Step 5 — Close

```
CONFORM
Fixed        : [one line per finding, with the commit]
Dropped      : [findings that needed a decision — and which decision]
Left         : [band 3 lines the user declined, or that were recommended to leave]
Still silent : [any C4 guarantee that is still not in force, and why]
Verified     : [what was actually run — the build, the page, the role test]
For app-eval : [findings that are defects in the rules rather than in this app — or "none"]
```

The last two rows are the ones that must not be softened. **`Verified` names what was executed**, and a build that was not run is written as not run. **`For app-eval`** is how a rule that produced this drift gets back to the toolkit: it is reported here and fixed there, in the toolkit repo, in another session. Fixing the rule from inside the app repo is the exact thing `app-eval` Step 0 exists to prevent.
