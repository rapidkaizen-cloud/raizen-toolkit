---
name: app-recover
description: Write PRD.md for an app that already runs and never had one. Reads the stack from the code, interviews the user for the intent no code can hold, records both, and enables the norms plugin. Section 5 is deliberately left unwritten for design-rework. Use on a repo that already has application code and no PRD.md — never on an empty directory.
---

# app-recover — the PRD of an app that already runs

`app-init` starts from an empty directory and decides everything. Here the app already exists: the stack is settled, the pages are built, people are using it. One thing is missing, and it is the one thing code can never supply — **why any of it is the way it is.**

The lockfile always knows *what*. It has never known *why*.

## Hard limits

`PRD.md` is the only document created. Do not write `ARCHITECTURE.md`, `DECISIONS.md`, `SCHEMA.md`, `CHANGELOG.md`, or an audit report as a file. `QUEUE.md` is not born here either — `build-flow` writes it in the first building session.

**Nothing about the app itself changes.** No dependency added, none removed, no file refactored, no stack migrated, no bug fixed on the way past. This skill writes documents and nothing else. A stack that turns out to be a poor fit is a finding reported at the close — see *The stack is not on trial*.

**Section 5 is not written.** Not from the code, not from an interview. It is left absent, and `design-rework` fills it on its ratify path. Copying today's CSS into Section 5 reverses `user → PRD → CSS` and makes every accident an official norm.

Do not commit and do not push. `git add` is fine; the commit waits for the user.

Do not invent. Not settled → `[needs verification]`.

## Step 0 — Declare

Check, then report one short block:

```
Directory  : [path] — [N files]
PRD.md     : [absent / present]
CLAUDE.md  : [absent / present]
Git        : [branch · N commits]  or  [not a repo]
Flow       : read stack → story → reading → 6 themes → summary → PRD + CLAUDE.md
```

`PRD.md` already present → **STOP.** This skill writes a PRD that does not exist; it does not merge into one that does. A PRD that exists but is thin grows under `prd-format`, whose rules already govern that.

No application code → **STOP**, this is `app-init`.

Branch `main` → **STOP.** The git guard will refuse it, and that refusal is correct.

Not a git repo → say so, offer `git init`, and continue either way. A PRD is worth writing for a repo with no history.

## Step 1 — Read the stack, do not ask it

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

Rows that come out `not readable` stay that way. They are asked at Step 3 only where they change what the PRD must say — a hosting platform nobody can name does not.

The **Locale** row matters more than it looks. `app-init` infers it from the user's story; here it can be measured from the strings actually rendered, and measured beats inferred. Confirm it anyway at Step 3: a half-translated UI measures as whichever half is larger.

## Step 2 — The story, then state your reading, then STOP

Do not open with a list of questions. Invite the user to talk freely: what problem this app solves, who uses it, what they did before it existed.

Then state what you took from it in one paragraph and **stop for correction**:

> *"I read this as [problem] experienced by [who], previously handled by [the old way], with this app now covering [which part]."*

**Your reading may draw on the code, and it must say which parts did.** Reading the routes and the schema before asking is exactly what makes this cheaper than `app-init` — the difference here is that a wrong reading can be checked against something real. Separate what you measured from what you inferred, so the user knows what they are correcting.

A reading that misses is not a failure. The correction carries detail no question would have surfaced.

## Step 3 — Six themes, and one rule that outranks the rest

The same six as `app-init`, and you may not continue without them:

- The real problem before this app existed, and why that state was intolerable
- Who uses it, and how they did the work **before** it
- The work each role must be able to finish, plus the limits that bind them
- Business rules **and the reason behind each number**
- Domain terms that are easy to misread
- **Non-goals**: what was deliberately not built, and why that was a decision rather than a gap

**Three are partly readable and three leave no trace at all.** Roles come out of the auth tables and the RLS policies. Rule *values* come out of constraints, RLS predicates, and constants. Terms come out of table and column names. Nothing readable is asked as though unknown — it is **shown and confirmed**, the same economy as Step 1:

> *"The code caps approvals at 5,000,000 for the `supervisor` role — `rls/approvals.sql:14`. What is that number for?"*

The problem before the app, how the work was done then, and the non-goals exist nowhere in the repo. Those are asked openly, one at a time, with no options.

**The rule that outranks everything else here: the reason behind every number.** A live check finds every value in the app and will never recover one reason. Where the answer is *"I don't know, it has always been that way"* — write exactly that, and do not improve on it. A recorded ignorance is worth more than a plausible fiction, because the next session knows not to trust it.

**Domain questions carry no options.** Their answers cannot be enumerated, and offering a guess as a choice steers the answer toward it. The "more than two options plus a recommendation" rule belongs to technical questions, not these.

Stop when the six are answered, not when the questions run out.

## Step 4 — Summary, then STOP

One message: app name · Surface/Data/Deploy as read · roles · key business rules **with their reasons** · domain terms · non-goals · every row still `not readable`.

Then **STOP** and wait for explicit approval. Write no file before this is answered.

## Step 5 — Write

Follow `references/prd-structure.md` in `app-init`. The same six sections, with three differences:

| Section | Difference from `app-init` |
|---|---|
| 1 | The stack is recorded **as found**, not as chosen. Each line reads as a measurement. No rejected alternatives — nobody rejected anything, because nobody chose from a list |
| 5 | **Left absent entirely**, with one line saying `design-rework` fills it. Not a template full of `[needs verification]`: an absent section and an unverified one are read differently by `ui-build`, and only one of them is honest here |
| 6 | Prohibitions the user states now. A prohibition inferred from code is not a prohibition, it is a habit |

Then:

- **`CLAUDE.md`** from `${CLAUDE_PLUGIN_ROOT}/templates/CLAUDE.md.tpl`, filled from Step 1. Keep the prose in English exactly as the template writes it — only placeholder values follow the app's locale. A translated file is invisible to the stale-section detector in `session_norms.py`, which matches the template's own English phrasing. Already present → **do not overwrite.** Add only the missing rows and report what was left alone.
- **`.claude/settings.json`** enabling `raizen-norms`. Already present with other plugins → add the key, keep the rest.
- **`supabase/config.toml`** only when the database is Supabase **and** the file is missing. It carries `{{SUPABASE_PROJECT_REF}}` — an identifier, not a secret — which the `guard_project_ref` hook pins every Supabase MCP call to. Present already → leave it alone.

**No scaffold, no `git init` on an existing repo, no `vercel.json`, no CI workflow.** Those belong to `app-init` on an empty directory. Here they either already exist or the user decided against them, and either way it is not this session's business.

`git add` the new files. **Stop before committing.**

## The stack is not on trial

The stack was chosen — or inherited — long before this session, and the app is running on it. **This skill reports; it does not migrate.**

Say it once, in the close block, one line per finding, and only where the finding is concrete:

| A finding | Not a finding |
|---|---|
| The library is unmaintained, or has had a supply-chain event | The rubric would have recommended something else |
| A version is past end-of-life for security fixes | A newer framework exists |
| **A norm can never apply here** — a database with no row-level security makes the `db-ops` role test meaningless | You would have picked differently |

The right-hand column is the whole reason this section exists. `app-init`'s rubric filters options for a **new** repo, where choosing costs nothing; this repo already paid. *Not ready* there means "no template exists", not "wrong".

The third row is the one that must never be softened. It is not a preference — it says plainly that a guarantee this toolkit makes does not hold in this repo, and the user is entitled to know which one and why.

A migration is real work with real risk, and running it **before** the PRD exists means rewriting an app whose rules are still undocumented. That is precisely how behaviour gets lost. PRD first; then a migration has a written test to pass. The user asks for one anyway → that is their call, and it is a separate session with its own plan.

## Step 6 — Close

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
Until Section 5 exists, any session will refuse to write a UI component.
```

`logic-rework` runs first for the same reason `logic-init` does: a reference page carries loading, empty, and failed states, and those belong to the data layer.

Do not run either now. Close by reminding the user that the first commit waits for their word, and that `raizen-norms` becomes active only once the next session starts in this repo.
