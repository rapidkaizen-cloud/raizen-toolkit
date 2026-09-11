---
name: app-settle
description: Settle the app-level decisions of an app of any kind — the problem domain, the stack, and PRD.md. Three modes, decided by what the directory already holds. Empty — bootstrap mode, interview the domain and the stack, write PRD.md, scaffold the repo, git init. Code but no PRD.md — document mode, write the PRD from the code and an interview, changing nothing about the app. Code and a PRD — rework mode, re-open the app-level decisions with keep always option one and every change carrying its cost and a recommendation. Use to start a new app, to document a running app that has no PRD, or to re-plan one that does. Section 5 is never written here.
---

# app-settle — the app-level decisions, from nothing or from what exists

`logic-settle` decides the layer between the database and the UI. `design-settle` decides how the app looks. This decides everything above both: what the app is for, who uses it, the rules it enforces, the stack it runs on — and `PRD.md`, which is where all of that lives.

**One skill, three modes, and the directory decides which.** There is no mode to pick and no second skill to route to: Step 0 reads what is already there, and what it finds settles the rest.

| What the directory holds | Mode | What the session does |
|---|---|---|
| Nothing | **Bootstrap** | Interview the domain and the stack from zero, write `PRD.md`, scaffold, `git init` |
| Application code, no `PRD.md` | **Document** | The one thing missing is the one thing code can never supply — **why any of it is the way it is.** Write the PRD. Change nothing |
| Application code and `PRD.md` | **Rework** | The user wants the app itself to change. The same interview discipline, with one inversion: every decision starts from what the app already does |

**One session runs one mode.** A repo with no PRD is documented first and reworked in a later session — re-deciding rules that were never written down is exactly how behaviour gets lost.

The user is a junior developer. A reasoned default is more useful than an open choice — open-ended architecture questions force decisions with nothing to base them on. **Only ask what changes the shape of the repo.**

## Hard limits — all three modes

`PRD.md` is the only document created or edited. Do not write `ARCHITECTURE.md`, `DECISIONS.md`, `SCHEMA.md`, `CHANGELOG.md`, or an interview summary or audit report as a file. If another skill in this session produces a document, it is **not committed**.

`QUEUE.md` is the one other file an app repo may carry, and it is not born here — the `build-flow` skill writes it in the first building session, from a queue the user approves.

**Section 5 is never written here.** Bootstrap and document mode leave it absent; rework mode leaves it untouched even when the whole point of the rework is a new look. `design-settle` owns it, on its own audit-then-ratify path. Copying today's CSS into Section 5 reverses `user → PRD → CSS` and makes every accident an official norm.

Do not commit and do not push. `git init` and staging are fine; the commit waits for the user.

Do not invent. Not settled yet → write `[needs verification]` in the PRD.

The domain interview is run by this skill alone, without third-party skills. If another interview skill offers itself during this session (via keyword trigger, for instance), ignore it — its output would collide with `PRD.md`, which is normative and changes only by the user's decision.

**Bootstrap mode only:** do not `npm install` or add dependencies beyond what the templates carry without the user's approval.

**Document and rework modes only — nothing about the app itself changes.** No dependency added, none removed, no file refactored, no migration run, no bug fixed on the way past. Decisions land in `PRD.md`; code catches up in build sessions under `build-flow`, never here.

## Step 0 — Declare

Check the working directory, the files it holds, and the available skills, then report one short block:

```
Directory  : [path] — [empty / N files]
PRD.md     : [absent / present]
CLAUDE.md  : [absent / present]
Git        : [branch · N commits]  or  [not a repo]
Mode       : [bootstrap — empty directory]
             [document  — application code, no PRD.md]
             [rework    — application code and PRD.md]
Flow       : [bootstrap: story → reading → 6 domain themes → 8 stack questions → PRD → scaffold]
             [document:  read stack → story → reading → 6 themes → summary → PRD + CLAUDE.md]
             [rework:    read PRD + stack → drift → story → keep-first decisions → summary → PRD edits]
```

**The directory decides the mode, and nothing else does.** A user asking to "start fresh" in a directory full of code is asking for rework, whatever the words were; a user asking to "fix up" an empty directory is asking for bootstrap. Report the mode with the fact that produced it, and let the user overrule it in one line if the reading is wrong.

**Directory not empty but the mode read as bootstrap** — files that are neither application code nor a PRD, a stray `README` or a `.git` and nothing else → **STOP**, ask whether to continue here or move. Do not overwrite anything.

Branch `main` → **STOP.** The git guard will refuse it, and that refusal is correct.

Not a git repo, with code already present → say so, offer `git init`, and continue either way. A PRD is worth writing for a repo with no history.

Then run the mode's own steps below. Do not mix them.

---

# Bootstrap mode — a new app from an empty directory

## N1 — Domain

Do not open with a list of questions. Invite the user to talk freely first: what problem they want solved, who uses it, why this app needs to exist now. One open invitation, not an interrogation.

From that story, map to the six points below. These must come out, and you may not continue without them:

- The real problem before this app existed, and why that state was intolerable
- Who uses it, and how they do the work **today** without this app
- The work each role must be able to finish, plus the limits that bind them
- Business rules **and the reason behind each number** — not just the value
- Domain terms that are easy to misread
- **Non-goals**: what is deliberately not built, and why that is a decision rather than a gap

What you do **not** need to dig for: table names, screen names, folder structure. All of that is born from the code later and does not belong in the PRD.

### State your reading, then STOP

Before digging into the six points, state what you took from the story in one paragraph, then **stop and wait for correction**. The shape: *"I read this as [problem] experienced by [who], currently handled by [the old way], with this app replacing [which part]."*

Digging six points on top of a wrong understanding yields six answers that are all correct for the wrong app. One corrected paragraph is cheaper than an interview that has to be redone.

A reading that misses is not a failure — the correction carries detail that no question would have surfaced.

### Digging out the rest

Once the reading is agreed, summarize back to the user what you captured for each point above. For points still empty or ambiguous, ask in one batch, in your own words — independent points travel together in a single message; only a follow-up whose wording depends on an earlier answer waits for it.

**Domain questions carry no options.** Their answers cannot be enumerated, and offering a guess as a choice steers the answer toward it. The "more than two options plus a recommendation" rule applies to technical questions, not to these.

One thing must never be skipped no matter how short the interview runs: **the reason behind every number**. A live check can find the number in a constant or an RLS predicate; it can never recover the reason. "I don't know, it has always been that way" is a valid answer — write it as-is, do not invent one.

Stop when the six points are answered, not when the questions run out.

## N2 — Stack, eight questions

Read `references/stack-questions.md` and `references/stack-consequences.md`, then run them.

Questions travel in batches — up to four per AskUserQuestion call, several calls per turn, sequential only where a question's options or recommendation read an earlier answer (the rubric's *Fits when* column is the map). Answers are reconciled after every batch: two that pull in opposite directions go back as one question naming both and what collides, never resolved silently. Each question carries **more than two options**, one marked recommendation, and a **one-sentence consequence** of that choice. Two options always read like a trap, and options without a recommendation force a decision with nothing to base it on. Answers outside the options are always accepted — if the user names something not on the list, use it and state its consequence if you know it, or say you don't.

**The stack is not locked.** Platform, framework, hosting, and database options are assembled from the rubric in `stack-questions.md`, filtered by the needs readable from the user's story. One hard limit: **options marked Not ready are not offered** — there are no templates for them, and a half-built repo is worse than a shorter list. The user names one anyway → accept it, and say plainly what they will have to set up themselves.

**Options marked Pioneer are offered, with their cost written into the option itself.** A Pioneer answer — chosen from the list or typed in — puts the bootstrap under the Pioneer path in `stack-questions.md`: name what does not exist, research-assembled stack questions, a minimal scaffold, `Platform: <name> (pioneer)` in Section 1, and a Proof profile proven before it is written.

After the eight questions, show the **derived lines** — each with its value and the answer it came from — then the **list of defaults that were not asked** and invite the user to name anything they want changed. Do not walk through them one by one.

Locale — UI language, date format, thousands and decimal separators — is inferred from the user's story and shown in that same block as concrete values. Do not make it a separate question, and do not leave it unwritten: a session opened months later in a different language cannot re-derive it.

Write UI language and code language as **two separate lines**, never one. Code language is English in every app and is not inferred from anything. Merged into one line it reads as permission for both, and the app ends up with identifiers, file names, and view names in the UI language. That has already happened once.

Component library is not asked here — it belongs to `design-settle`, which asks it once the app's real needs are readable and which also installs it.

## N3 — Summary, then STOP

One message: app name · Surface/Data/Deploy · roles · key business rules · domain terms · non-goals · stack decisions · rejected alternatives with their reasons.

Then **STOP** and wait for explicit approval. Write no file before this is answered.

## N4 — Write `PRD.md`

Follow `references/prd-structure.md`. Six sections. Section 5 is deleted entirely for a product without UI.

Section 1 carries the **Proof profile** per `prd-structure.md` — on a web platform the web default is written as-is; on a Pioneer platform, only lines that were actually executed are written as fact, the rest `[needs verification]`.

Rejected stack alternatives go into **Section 1 Non-goals**, one line per alternative plus a one-sentence reason. Not a full write-up — if the reason needs three paragraphs, it is not a non-goal.

Section 5 is filled with `[needs verification]` throughout. Bootstrap is not the moment to decide typography, and Section 5 is never written by an agent on its own initiative.

`design-settle` fills it, in a separate session after bootstrap. Until then the `ui-build` skill blocks writing any component — so an empty Section 5 is not a gaping hole, it is a gate that has not been opened.

## N5 — Scaffold

**Nothing is copied — every file here is written for the answers this session got.** This plugin ships no template folder, deliberately: a stock file is a decision taken before its question was asked, and it goes stale without anyone re-reading it. A Pioneer platform therefore receives exactly what a Ready one does, plus its own init command.

| File | Contents |
|---|---|
| `CLAUDE.md` | **Thin**, written to the shape below |
| `.claude/settings.json` | `{"enabledPlugins": {"raizen-norms@raizen": true}}` — that key and nothing else; a repo that already has the file keeps the rest of it |
| Host rewrite rule | Only when the framework is a **static SPA**, and written for the host chosen at Question 4 — `vercel.json` on Vercel, `netlify.toml` on Netlify, a `try_files` line on an own server. Next.js, Nuxt, SvelteKit, and Astro carry their own server layer — do not write one |
| CI workflow | Only when the user asks for migrations through CI at N6. Written for the host and migration tool actually chosen — there is no stock workflow to copy, and one written for the wrong runner is worse than none |
| `supabase/config.toml` | Only when the database is Supabase. **Written here, not copied** — one line, `project_id = "<ref>"`, an identifier and not a secret. This value is what the `guard_project_ref` hook pins every Supabase MCP call to, so a repo that skips it is a repo the guard stays silent in. **Which ref goes in** follows Question 7 — staging exists → the staging project, never production |

### The shape of `CLAUDE.md`

**English prose, whatever the app's UI language** — only the values follow the app's locale. A file written in another language is invisible to the stale-section detector in `session_norms.py`, which matches English phrases from retired sections, so translating it disables the one mechanism that migrates this file later.

Six parts, nothing else. A rule that would hold in another app belongs in the plugin, never here.

| Part | Holds |
|---|---|
| Opening line | That this file holds what is true of this app alone, and that norms are printed by `raizen-norms` every session — a norm living in two places is a norm that will disagree with itself |
| `## Locale` | On screen · in the code · dates · numbers. The first two rows stay separate: a UI language is never a licence for an identifier, a route, or a database name written in it |
| `## Stack` | One row per N2 answer — platform, frontend, hosting, database, auth, component library, environments, migrations — and the line stating this app's stack is locked, re-opened only through `app-settle` rework mode |
| `## Ground truth` | Code and the live database are ground truth for **facts**; `PRD.md` for **intent and prohibitions** |
| `## Gate` | Section 5 empty or `[needs verification]` → `ui-build` refuses to write components, and `design-settle` is what sets it |
| `## Rules for this app only` | Empty at bootstrap. Only rules that would be wrong in another app |

**The last two parts stay in the file on purpose** — they must still bite in a session where the plugin is absent, disabled, or failed to start. Everything else there is a value, not a rule.

**Name the skills that exist today, never from memory of an older flow.** The retired template this replaced still pointed at `/app-init` and `/design-rework` long after both were folded into `app-settle` and `design-settle`: a file nobody re-reads is a file that goes stale in silence, and that is the whole reason this is a shape rather than a template.

**No `.mcp.json` is written — ever.** Database MCP servers are connected **user scope**, once per machine, never per repo; for Supabase the exact `claude mcp add -s user` one-liner is printed at Step 6. A repo-level server config would only duplicate what the machine already has. Project pinning does not come from server config: `supabase/config.toml` declares the repo's project, and the `guard_project_ref` hook in `raizen-norms` blocks any Supabase MCP call aimed at a different one. A database whose official MCP server exists follows the same pattern; a database with no server → say so rather than leaving the gap silent.

Then `git init`, `git branch -M main`, create `development` from `main`, and `git add` the new files. **Stop before committing.**

### Connectors are recommended, never a precondition

Where the database chosen at Question 6 has a Claude connector or an MCP server, say so once, say what it automates, and carry on whatever the answer is. Bootstrap never waits for one — every connector replaces work the user can also do by hand, and an app that cannot be started without one is an app held hostage to somebody's catalogue.

Two rules stop this from rotting:

- **Derive it from the stack, not from this file.** Name what Question 6 actually produced. Supabase appears here because the template covers it, not because it is the answer.
- **Never claim a connector exists.** The catalogue changes and this file does not. Point at the connector settings and let the user see what is really there; a promise that turns out false costs more than saying nothing.

Connectors for **hosting** are not raised here. N6 explains why, and `build-flow` raises them at the one moment they matter.

## N6 — Close

Report one block: the files created, then what the **user must do by hand right now** — create the database project chosen at Question 6, plus its staging counterpart if Question 7 asked for one, and connect it. For Supabase that means putting the **project ref** into `supabase/config.toml`, and — only on a machine not yet set up — connecting the MCP server user-scope, then approving the browser login on first use:

```
claude mcp add -s user --transport http supabase "https://mcp.supabase.com/mcp"
```

The URL must stay **bare** — Supabase's OAuth rejects any query string, so adding `?features=` or `?project_ref=` breaks the login itself.

Both are once per machine and account, never per repo, so a machine already set up needs nothing beyond the ref. For another database, whatever its own equivalent is. Pointed at production because there is no staging → say that plainly, since from then on every guarded destructive statement lands on live data. **No token is written into any file**; asking for one would be wrong. Name the variables, never their values. Without a live database there is no migration and no role test, so not a single page can be built.

Hosting connection, production environment variables, and the CI migration workflow are **not mentioned here**. None of them is needed to build a page locally, and naming them at bootstrap turns infrastructure into homework before anything exists to deploy. Nothing was scaffolded for any of them either — this toolkit writes no hosting or CI file at bootstrap, so there is no inert config sitting in the repo to explain. The `build-flow` skill raises them once the app is ready to ship.

Then offer the next steps, unless the product has no UI:

```
Two sessions remain before pages can be built, in this order:
  /logic-settle — the logic layer: cache, validation, dates, logging,
                 scheduling, audit trail. Scored from the PRD; often
                 installs nothing.
  /design-settle — the visual direction: one reference question, the stack
                 installed, 2–4 direction frames picked on screen, then every
                 page drawn on a canvas, judged, and promoted.
Until design-settle is done, any session will refuse to write UI components.
```

`logic-settle` runs first because the pages `design-settle` promotes carry loading, empty, and failed states — and those belong to the data layer.

Do not run it now. Bootstrap ends with zero dependencies installed, and `design-settle` needs to install several.

Once the visual direction is agreed, building runs under the `build-flow` skill, which writes `QUEUE.md` on its first run. A new app builds its screens first — a UI batch, every page against a hand-written contract with no database behind it — then wires them in a backend batch. `build-flow` owns both, and the size of one session is set there.

Close by reminding the user that the first commit waits for their word, and that `raizen-norms` only becomes active once the next session starts in this repo.

# Document mode — the PRD of an app that never had one

## D1 — Read the stack, do not ask it

Everything in this block is readable, so none of it is a question. Report one block:

```
STACK — read from the repo
Framework     : [name · version — from which file]
Language      : [and whether types are enforced]
Surface       : [platform — web / desktop / mobile, and the files that decided it · then
                server routes or static SPA where it is web]
Database      : [name · how it is reached · migrations present or not]
Hosting       : [from config present, or "not readable"]
Auth          : [library or service / handwritten / none found]
Logic layer   : [the six of logic-settle — cache · validator · dates · errors · jobs · attribution, each named or "none"]
UI components : [file count] · [library · version, or "none"]
Styling       : [tokens defined / raw values only]
Tests         : [runner · how many files, or "none"]
Locale in UI  : [language · date format · separators, from the strings actually rendered]
```

**Every row names where it was read from.** A row nobody can trace back to a file is a guess wearing a fact's clothing.

Rows that come out `not readable` stay that way. They are asked at D3 only where they change what the PRD must say — a hosting platform nobody can name does not.

The **Locale** row matters more than it looks. bootstrap mode infers it from the user's story; here it can be measured from the strings actually rendered, and measured beats inferred. Confirm it anyway at D3: a half-translated UI measures as whichever half is larger.

## D2 — The story, then state your reading, then STOP

Do not open with a list of questions. Invite the user to talk freely: what problem this app solves, who uses it, what they did before it existed.

Then state what you took from it in one paragraph and **stop for correction**:

> *"I read this as [problem] experienced by [who], previously handled by [the old way], with this app now covering [which part]."*

**Your reading may draw on the code, and it must say which parts did.** Reading the routes and the schema before asking is exactly what makes this cheaper than bootstrap mode — the difference here is that a wrong reading can be checked against something real. Separate what you measured from what you inferred, so the user knows what they are correcting.

A reading that misses is not a failure. The correction carries detail no question would have surfaced.

## D3 — Six themes, and one rule that outranks the rest

The same six as bootstrap mode, and you may not continue without them:

- The real problem before this app existed, and why that state was intolerable
- Who uses it, and how they did the work **before** it
- The work each role must be able to finish, plus the limits that bind them
- Business rules **and the reason behind each number**
- Domain terms that are easy to misread
- **Non-goals**: what was deliberately not built, and why that was a decision rather than a gap

**Three are partly readable and three leave no trace at all.** Roles come out of the auth tables and the RLS policies. Rule *values* come out of constraints, RLS predicates, and constants. Terms come out of table and column names. Nothing readable is asked as though unknown — it is **shown and confirmed**, the same economy as D1:

> *"The code caps approvals at 5,000,000 for the `supervisor` role — `rls/approvals.sql:14`. What is that number for?"*

The problem before the app, how the work was done then, and the non-goals exist nowhere in the repo. Those are asked openly, with no options — grouped into one message where they are independent; a follow-up that reads an earlier answer waits for it.

**The rule that outranks everything else here: the reason behind every number.** A live check finds every value in the app and will never recover one reason. Where the answer is *"I don't know, it has always been that way"* — write exactly that, and do not improve on it. A recorded ignorance is worth more than a plausible fiction, because the next session knows not to trust it.

**Domain questions carry no options.** Their answers cannot be enumerated, and offering a guess as a choice steers the answer toward it. The "more than two options plus a recommendation" rule belongs to technical questions, not these.

Stop when the six are answered, not when the questions run out.

## D4 — Summary, then STOP

One message: app name · Surface/Data/Deploy as read · roles · key business rules **with their reasons** · domain terms · non-goals · every row still `not readable`.

Then **STOP** and wait for explicit approval. Write no file before this is answered.

## D5 — Write

Follow `references/prd-structure.md` beside this skill. The same six sections, with three differences:

| Section | Difference from bootstrap mode |
|---|---|
| 1 | The stack is recorded **as found**, not as chosen. Each line reads as a measurement. No rejected alternatives — nobody rejected anything, because nobody chose from a list. The Surface row and Proof profile are still written, measured rather than chosen |
| 5 | **Left absent entirely**, with one line saying `design-settle` fills it. Not a template full of `[needs verification]`: an absent section and an unverified one are read differently by `ui-build`, and only one of them is honest here |
| 6 | Prohibitions the user states now. A prohibition inferred from code is not a prohibition, it is a habit |

Then:

- **`CLAUDE.md`** written to the shape in N5, filled from D1. English prose whatever the app's UI language — a translated file is invisible to the stale-section detector in `session_norms.py`. Already present → **do not overwrite.** Add only the missing rows and report what was left alone.
- **`.claude/settings.json`** enabling `raizen-norms`. Already present with other plugins → add the key, keep the rest.
- **`supabase/config.toml`** only when the database is Supabase **and** the file is missing. One line, `project_id = "<ref>"` — an identifier, not a secret — which the `guard_project_ref` hook pins every Supabase MCP call to. Present already → leave it alone.

**No scaffold, no `git init` on an existing repo, no host config, no CI workflow.** Here they either already exist or the user decided against them, and either way it is not this session's business.

`git add` the new files. **Stop before committing.**

## The stack is not on trial — in this mode

The stack was chosen — or inherited — long before this session, and the app is running on it. **Document mode reports; it does not migrate, and it does not re-litigate.**

Say it once, in the close block, one line per finding, and only where the finding is concrete:

| A finding | Not a finding |
|---|---|
| The library is unmaintained, or has had a supply-chain event | The rubric would have recommended something else |
| A version is past end-of-life for security fixes | A newer framework exists |
| **A norm can never apply here** — a database with no row-level security makes the `db-ops` role test meaningless | You would have picked differently |

The right-hand column is the whole reason this section exists. bootstrap mode's rubric filters options for a **new** repo, where choosing costs nothing; this repo already paid. *Not ready* there means "no template exists", not "wrong".

The third row is the one that must never be softened. It is not a preference — it says plainly that a guarantee this toolkit makes does not hold in this repo, and the user is entitled to know which one and why.

The trial the user actually wants is opened by asking for it: that is rework mode, in a later session, once this PRD exists to judge any change against.

## D6 — Close

One block:

```
Written    : PRD.md · CLAUDE.md [new / N rows added] · .claude/settings.json
Not read   : [rows still unreadable]
Unverified : [what carries [needs verification]]
Findings   : [concrete stack findings only — or "none"]
Section 5  : absent — design-settle fills it
```

Then the next sessions, in this order:

```
/logic-settle   — the logic layer as it stands: what is installed, what is
                  missing, what is the wrong tool. Keeping everything is a
                  valid ending.
/design-settle  — audits the styling, then puts every visual decision to you:
                  ratify what the code already does, or decide otherwise.
/app-settle     — again, once this PRD exists: rework mode re-opens business
                  rules, scope, or stack when the app itself must change.
/app-conform    — only where the Findings row above is not "none": it changes
                  the existing code to match the rules, one commit per finding.
Until Section 5 exists, any session will refuse to write a UI component.
```

`logic-settle` runs first, for the same reason it does on a new repo: the promoted pages carry loading, empty, and failed states, and those belong to the data layer.

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

The reading names which PRD sections the rework touches. A rework that turns out to touch only Section 5 is not this skill — close and point to `design-settle` directly.

## R3 — Decisions, keep-first

Walk **only the decisions the story touched, plus those their change forces open** — never the whole PRD. The bootstrap-mode rule "only ask what changes the shape of the repo" becomes: only ask what the rework changes.

Every decision is presented the same way:

- **What the app does today**, with where it was read from — a PRD line, a constraint, `rls/approvals.sql:14`.
- **Option one is always keep**, and it is marked as costing nothing.
- Then the alternatives — more than two options total, each with a one-sentence consequence, one marked recommendation. Options marked *Not ready* in the stack rubric are still not offered.

The burden of proof sits on the change: the app already paid for its current choices, and a keep answered in one word is a finished decision, not a skipped one.

The rules carried over from bootstrap mode unchanged:

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
Section 5  : untouched — design-settle owns it
```

Then the sessions that execute the decisions, in this order:

```
/logic-settle   — only when a logic-layer choice changed or the rework opened one
/design-settle  — when the look changes: audits the styling, rewrites Section 5,
                  proves it on the design canvas
build sessions  — build-flow queues and executes the rest, page by page;
                  schema and constraint changes go through db-ops on the way
```

`logic-settle` before `design-settle`, for the same reason as always: the promoted pages carry loading, empty, and failed states, and those belong to the data layer.

Do not run any of them now. Close by reminding the user that the commit waits for their word.
