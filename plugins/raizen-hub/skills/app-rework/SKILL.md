---
name: app-rework
description: Rework an app that already runs. Two modes, decided by whether PRD.md exists. Absent — document mode, write the PRD from the code and an interview, changing nothing about the app, Section 5 left for design-rework. Present — rework mode, re-open the app-level decisions with keep always option one and every change carrying its cost and a recommendation. Use when the user wants to rebuild or re-plan an existing app, change its business rules or stack, or when a running app has no PRD.md. Never on an empty directory.
---

# app-rework — rework an app that already runs

`app-init` starts from an empty directory and decides everything. Here the app already exists: the stack is settled, the pages are built, people are using it. What this session does depends on one fact:

- **No `PRD.md`** → **document mode.** The one thing missing is the one thing code can never supply — **why any of it is the way it is.** The lockfile always knows *what*; it has never known *why*. Write the PRD. Change nothing.
- **`PRD.md` present** → **rework mode.** The user wants the app itself to change. The same interview discipline as `app-init`, with one inversion: every decision starts from what the app already does. Keep is option one and costs nothing; a change carries its cost and a recommendation.

One session runs one mode. A repo with no PRD is documented first and reworked in a later session — re-deciding rules that were never written down is exactly how behaviour gets lost.

## Hard limits — both modes

**Nothing about the app itself changes.** No dependency added, none removed, no file refactored, no migration run, no bug fixed on the way past. Decisions land in `PRD.md`; code catches up in build sessions under `build-flow`, never here.

`PRD.md` is the only document created or edited. Do not write `ARCHITECTURE.md`, `DECISIONS.md`, `SCHEMA.md`, `CHANGELOG.md`, or an audit report as a file. `QUEUE.md` is not born here either — `build-flow` writes it in the first building session.

**Section 5 is never written here.** Document mode leaves it absent; rework mode leaves it untouched even when the whole point of the rework is a new look. `design-rework` owns it, on its own audit-then-ratify path. Copying today's CSS into Section 5 reverses `user → PRD → CSS` and makes every accident an official norm.

Do not commit and do not push. `git add` is fine; the commit waits for the user.

Do not invent. Not settled → `[needs verification]`.

## Step 0 — Declare

Check, then report one short block:

```
Directory  : [path] — [N files]
PRD.md     : [absent → document mode / present → rework mode]
CLAUDE.md  : [absent / present]
Git        : [branch · N commits]  or  [not a repo]
Flow       : [document: read stack → story → reading → 6 themes → summary → PRD + CLAUDE.md]
             [rework:   read PRD + stack → drift → story → keep-first decisions → summary → PRD edits]
```

No application code → **STOP**, this is `app-init`.

Branch `main` → **STOP.** The git guard will refuse it, and that refusal is correct.

Not a git repo → say so, offer `git init`, and continue either way. A PRD is worth writing for a repo with no history.

Then run the mode's own steps below. Do not mix them.

---

# Document mode — the PRD of an app that never had one

## D1 — Read the stack, do not ask it

Everything in this block is readable, so none of it is a question. Report one block:

```
STACK — read from the repo
Framework     : [name · version — from which file]
Language      : [and whether types are enforced]
Surface       : [server routes / static SPA — name the files that decided it]
Database      : [name · how it is reached · migrations present or not]
Hosting       : [from config present, or "not readable"]
Auth          : [library or service / handwritten / none found]
Logic layer   : [the six of logic-init — cache · validator · dates · errors · jobs · attribution, each named or "none"]
UI components : [file count] · [library · version, or "none"]
Styling       : [tokens defined / raw values only]
Tests         : [runner · how many files, or "none"]
Locale in UI  : [language · date format · separators, from the strings actually rendered]
```

**Every row names where it was read from.** A row nobody can trace back to a file is a guess wearing a fact's clothing.

Rows that come out `not readable` stay that way. They are asked at D3 only where they change what the PRD must say — a hosting platform nobody can name does not.

The **Locale** row matters more than it looks. `app-init` infers it from the user's story; here it can be measured from the strings actually rendered, and measured beats inferred. Confirm it anyway at D3: a half-translated UI measures as whichever half is larger.

## D2 — The story, then state your reading, then STOP

Do not open with a list of questions. Invite the user to talk freely: what problem this app solves, who uses it, what they did before it existed.

Then state what you took from it in one paragraph and **stop for correction**:

> *"I read this as [problem] experienced by [who], previously handled by [the old way], with this app now covering [which part]."*

**Your reading may draw on the code, and it must say which parts did.** Reading the routes and the schema before asking is exactly what makes this cheaper than `app-init` — the difference here is that a wrong reading can be checked against something real. Separate what you measured from what you inferred, so the user knows what they are correcting.

A reading that misses is not a failure. The correction carries detail no question would have surfaced.

## D3 — Six themes, and one rule that outranks the rest

The same six as `app-init`, and you may not continue without them:

- The real problem before this app existed, and why that state was intolerable
- Who uses it, and how they did the work **before** it
- The work each role must be able to finish, plus the limits that bind them
- Business rules **and the reason behind each number**
- Domain terms that are easy to misread
- **Non-goals**: what was deliberately not built, and why that was a decision rather than a gap

**Three are partly readable and three leave no trace at all.** Roles come out of the auth tables and the RLS policies. Rule *values* come out of constraints, RLS predicates, and constants. Terms come out of table and column names. Nothing readable is asked as though unknown — it is **shown and confirmed**, the same economy as D1:

> *"The code caps approvals at 5,000,000 for the `supervisor` role — `rls/approvals.sql:14`. What is that number for?"*

The problem before the app, how the work was done then, and the non-goals exist nowhere in the repo. Those are asked openly, one at a time, with no options.

**The rule that outranks everything else here: the reason behind every number.** A live check finds every value in the app and will never recover one reason. Where the answer is *"I don't know, it has always been that way"* — write exactly that, and do not improve on it. A recorded ignorance is worth more than a plausible fiction, because the next session knows not to trust it.

**Domain questions carry no options.** Their answers cannot be enumerated, and offering a guess as a choice steers the answer toward it. The "more than two options plus a recommendation" rule belongs to technical questions, not these.

Stop when the six are answered, not when the questions run out.

## D4 — Summary, then STOP

One message: app name · Surface/Data/Deploy as read · roles · key business rules **with their reasons** · domain terms · non-goals · every row still `not readable`.

Then **STOP** and wait for explicit approval. Write no file before this is answered.

## D5 — Write

Follow `references/prd-structure.md` in `app-init`. The same six sections, with three differences:

| Section | Difference from `app-init` |
|---|---|
| 1 | The stack is recorded **as found**, not as chosen. Each line reads as a measurement. No rejected alternatives — nobody rejected anything, because nobody chose from a list |
| 5 | **Left absent entirely**, with one line saying `design-rework` fills it. Not a template full of `[needs verification]`: an absent section and an unverified one are read differently by `ui-build`, and only one of them is honest here |
| 6 | Prohibitions the user states now. A prohibition inferred from code is not a prohibition, it is a habit |

Then:

- **`CLAUDE.md`** from `${CLAUDE_PLUGIN_ROOT}/templates/CLAUDE.md.tpl`, filled from D1. Keep the prose in English exactly as the template writes it — only placeholder values follow the app's locale. A translated file is invisible to the stale-section detector in `session_norms.py`, which matches the template's own English phrasing. Already present → **do not overwrite.** Add only the missing rows and report what was left alone.
- **`.claude/settings.json`** enabling `raizen-norms`. Already present with other plugins → add the key, keep the rest.
- **`supabase/config.toml`** only when the database is Supabase **and** the file is missing. It carries `{{SUPABASE_PROJECT_REF}}` — an identifier, not a secret — which the `guard_project_ref` hook pins every Supabase MCP call to. Present already → leave it alone.

**No scaffold, no `git init` on an existing repo, no `vercel.json`, no CI workflow.** Those belong to `app-init` on an empty directory. Here they either already exist or the user decided against them, and either way it is not this session's business.

`git add` the new files. **Stop before committing.**

## The stack is not on trial — in this mode

The stack was chosen — or inherited — long before this session, and the app is running on it. **Document mode reports; it does not migrate, and it does not re-litigate.**

Say it once, in the close block, one line per finding, and only where the finding is concrete:

| A finding | Not a finding |
|---|---|
| The library is unmaintained, or has had a supply-chain event | The rubric would have recommended something else |
| A version is past end-of-life for security fixes | A newer framework exists |
| **A norm can never apply here** — a database with no row-level security makes the `db-ops` role test meaningless | You would have picked differently |

The right-hand column is the whole reason this section exists. `app-init`'s rubric filters options for a **new** repo, where choosing costs nothing; this repo already paid. *Not ready* there means "no template exists", not "wrong".

The third row is the one that must never be softened. It is not a preference — it says plainly that a guarantee this toolkit makes does not hold in this repo, and the user is entitled to know which one and why.

The trial the user actually wants is opened by asking for it: that is rework mode, in a later session, once this PRD exists to judge any change against.

## D6 — Close

One block:

```
Written    : PRD.md · CLAUDE.md [new / N rows added] · .claude/settings.json
Not read   : [rows still unreadable]
Unverified : [what carries [needs verification]]
Findings   : [concrete stack findings only — or "none"]
Section 5  : absent — design-rework fills it
```

Then the next sessions, in this order:

```
/logic-rework   — the logic layer as it stands: what is installed, what is
                  missing, what is the wrong tool. Keeping everything is a
                  valid ending.
/design-rework  — audits the styling, then puts every visual decision to you:
                  ratify what the code already does, or decide otherwise.
/app-rework     — again, once this PRD exists: rework mode re-opens business
                  rules, scope, or stack when the app itself must change.
Until Section 5 exists, any session will refuse to write a UI component.
```

`logic-rework` runs first for the same reason `logic-init` does: the promoted pages carry loading, empty, and failed states, and those belong to the data layer.

Do not run any of them now. Close by reminding the user that the first commit waits for their word, and that `raizen-norms` becomes active only once the next session starts in this repo.

---

# Rework mode — re-deciding an app that has a PRD

## R1 — Read both, then report the drift

Read `PRD.md` for the intent, and the repo for the reality — the same STACK block as D1, every row naming where it was read from. Then put the two side by side and report the drift, one line per mismatch:

```
DRIFT — PRD says · code does
[Section N claim]  : [what the code actually does — file:line]
[not in PRD]       : [something load-bearing the code does that no section covers]
```

Drift is a finding put to the user at R3, never a thing to silently "fix" in either direction — the PRD may be stale, or the code may have wandered, and only the user knows which.

No drift found → say so in one line and move on.

## R2 — What hurts, then state your reading, then STOP

Do not open with a decision list. Invite the user to talk freely: what feels wrong, what triggered the rework, what must be true when it is over.

Then state what you took from it in one paragraph and **stop for correction**:

> *"I read this as [what hurts] driving changes to [which decisions], with [what] staying as it is."*

The reading names which PRD sections the rework touches. A rework that turns out to touch only Section 5 is not this skill — close and point to `design-rework` directly.

## R3 — Decisions, keep-first

Walk **only the decisions the story touched, plus those their change forces open** — never the whole PRD. The `app-init` rule "only ask what changes the shape of the repo" becomes: only ask what the rework changes.

Every decision is presented the same way:

- **What the app does today**, with where it was read from — a PRD line, a constraint, `rls/approvals.sql:14`.
- **Option one is always keep**, and it is marked as costing nothing.
- Then the alternatives — more than two options total, each with a one-sentence consequence, one marked recommendation. Options marked *Not ready* in the `app-init` rubric are still not offered.

The burden of proof sits on the change: the app already paid for its current choices, and a keep answered in one word is a finished decision, not a skipped one.

The rules carried over from `app-init` unchanged:

- **Domain questions carry no options.** A business rule's new value and the reason behind it cannot be enumerated. Show the current value and its recorded reason, then ask openly.
- **The reason behind every number.** A changed number without a new reason is not recorded; "the old reason still holds" is a valid new reason and is written as such.
- **A deleted non-goal is scope opening up.** Ask openly what changed, and record the answer next to the deletion — the next session must know why the wall came down.

**The stack is on trial here — the user opened it.** Keep is still option one, but framework, database, and hosting may be re-decided. The consequence line of a migration option must name the real cost in concrete terms: which layers get rewritten, what runs in parallel meanwhile, and that the migration itself is separate planned work — decided here, recorded in the PRD, executed in its own sessions under `build-flow`. A migration whose cost fits in the word "straightforward" has not been costed.

After the walked decisions, show the block of decisions **kept without being asked**, and invite the user to name any they want opened. Do not walk through them one by one.

## R4 — Summary, then STOP

One message:

- Decisions changed — old → new, each with its reason
- Decisions kept — walked and unasked alike
- Drift resolved — which way each mismatch went
- Execution this creates — schema changes, constraint updates, pages to rebuild — named but not started
- Rows still `[needs verification]`

Then **STOP** and wait for explicit approval. Edit no file before this is answered.

## R5 — Write

Edit `PRD.md` under `prd-format`'s rules — **edits to the sections touched, not a rewrite.** The old value of a changed rule does not survive as a ghost paragraph: the PRD holds current truth, git holds history. Section 5 is not touched, whatever the rework was about.

`CLAUDE.md` rows whose values the rework changed — stack lines, locale — are updated to match. Nothing else in it moves.

`git add` the edited files. **Stop before committing.**

## R6 — Close

One block:

```
Changed    : [decision: old → new — one line each]
Kept       : [N decisions — walked and unasked]
Drift      : [resolved which way, or "none found"]
Execution  : [what build sessions must now do — or "none"]
Unverified : [what carries [needs verification]]
Section 5  : untouched — design-rework owns it
```

Then the sessions that execute the decisions, in this order:

```
/logic-rework   — only when a logic-layer choice changed or the rework opened one
/design-rework  — when the look changes: audits the styling, rewrites Section 5,
                  proves it on the design canvas
build sessions  — build-flow queues and executes the rest, page by page;
                  schema and constraint changes go through db-ops on the way
```

`logic-rework` before `design-rework`, for the same reason as always: the promoted pages carry loading, empty, and failed states, and those belong to the data layer.

Do not run any of them now. Close by reminding the user that the commit waits for their word.
