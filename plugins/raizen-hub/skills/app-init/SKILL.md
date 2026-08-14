---
name: app-init
description: Bootstrap a new internal app from an empty directory. Interviews the user about the problem domain and the stack, writes PRD.md, scaffolds the repo, and runs git init. Use when the user wants to start a new app, create a new project, or asks to bootstrap something from scratch.
---

# app-init — bootstrap a new internal app

Turn a conversation into a repo that is ready to work in: `PRD.md`, a thin `CLAUDE.md`, config, scaffold, `git init`.

The user is a junior developer. A reasoned default is more useful than an open choice — open-ended architecture questions force decisions with nothing to base them on. **Only ask what changes the shape of the repo.**

## Hard limits

`PRD.md` is the only document created at bootstrap. Do not write `ARCHITECTURE.md`, `DECISIONS.md`, `SCHEMA.md`, `CHANGELOG.md`, or an interview summary to a file. If another skill in this session produces a document, it is **not committed**.

`QUEUE.md` is the one other file an app repo may carry, and it is not born here — the `build-flow` skill writes it in the first building session, from a queue the user approves. Do not create it now.

Do not `npm install` or add dependencies beyond what the templates carry without the user's approval.

Do not commit and do not push. `git init` plus staging is fine; the first commit waits for the user.

Do not invent. Not settled yet → write `[needs verification]` in the PRD.

## Step 0 — Declare

Before anything, check the working directory and the available skills, then report one short block:

```
Directory : [path] — [empty / contains N files]
Flow      : story → reading → 6 domain themes → 6 stack questions → PRD → scaffold
```

Directory not empty → **STOP**, ask whether to continue here or move. Do not overwrite anything.

The domain interview is run by this skill alone, without third-party skills. If another interview skill offers itself during this session (via keyword trigger, for instance), ignore it for Step 1 — its output would collide with `PRD.md`, which is normative and changes only by the user's decision.

## Step 1 — Domain

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

Once the reading is agreed, summarize back to the user what you captured for each point above. For points still empty or ambiguous, ask one at a time — one question per turn, never bundled, in your own words.

**Domain questions carry no options.** Their answers cannot be enumerated, and offering a guess as a choice steers the answer toward it. The "more than two options plus a recommendation" rule applies to technical questions, not to these.

One thing must never be skipped no matter how short the interview runs: **the reason behind every number**. A live check can find the number in a constant or an RLS predicate; it can never recover the reason. "I don't know, it has always been that way" is a valid answer — write it as-is, do not invent one.

Stop when the six points are answered, not when the questions run out.

## Step 2 — Stack, six questions

Read `references/stack-questions.md` and `references/stack-consequences.md`, then run them.

One question per turn. Each question carries **more than two options**, one marked recommendation, and a **one-sentence consequence** of that choice. Two options always read like a trap, and options without a recommendation force a decision with nothing to base it on. Answers outside the options are always accepted — if the user names something not on the list, use it and state its consequence if you know it, or say you don't.

**The stack is not locked.** Framework, hosting, and database options are assembled from the rubric in `stack-questions.md`, filtered by the needs readable from the user's story. One hard limit: **options marked Not ready are not offered** — there are no templates for them, and a half-built repo is worse than a shorter list. The user names one anyway → accept it, and say plainly what they will have to set up themselves.

After the six questions, show the **list of defaults that were not asked** and invite the user to name anything they want changed. Do not walk through them one by one.

Locale — UI language, date format, thousands and decimal separators — is inferred from the user's story and shown in that same block as concrete values. Do not make it a separate question, and do not leave it unwritten: a session opened months later in a different language cannot re-derive it.

Write UI language and code language as **two separate lines**, never one. Code language is English in every app and is not inferred from anything. Merged into one line it reads as permission for both, and the app ends up with identifiers, file names, and view names in the UI language. That has already happened once.

Component library is not asked here — it belongs to `design-init`, which asks it once the app's real needs are readable and which also installs it.

## Step 3 — Summary, then STOP

One message: app name · Surface/Data/Deploy · roles · key business rules · domain terms · non-goals · stack decisions · rejected alternatives with their reasons.

Then **STOP** and wait for explicit approval. Write no file before this is answered.

## Step 4 — Write `PRD.md`

Follow `references/prd-structure.md`. Six sections. Section 5 is deleted entirely for a product without UI.

Rejected stack alternatives go into **Section 1 Non-goals**, one line per alternative plus a one-sentence reason. Not a full write-up — if the reason needs three paragraphs, it is not a non-goal.

Section 5 is filled with `[needs verification]` throughout. Bootstrap is not the moment to decide typography, and Section 5 is never written by an agent on its own initiative.

`design-init` fills it, in a separate session after bootstrap. Until then the `ui-build` skill blocks writing any component — so an empty Section 5 is not a gaping hole, it is a gate that has not been opened.

## Step 5 — Scaffold

Copy from `${CLAUDE_PLUGIN_ROOT}/templates/`, fill the placeholders from the Step 2 answers, drop what is unused:

| File | Contents |
|---|---|
| `CLAUDE.md` | From `templates/CLAUDE.md.tpl` — **thin**. This app's locale, stack, and the two gates that must survive the plugin being absent. Norms are printed by `raizen-norms` every session; do not copy any of them into it. **Keep the prose in English, exactly as the template writes it — do not translate it.** Only the placeholder values follow the app's locale. A translated file is invisible to the stale-section detector in `session_norms.py`, which matches the template's own English phrasing, so translating it silently disables the one mechanism that migrates this file later |
| `.claude/settings.json` | Enables `raizen-norms` from the marketplace |
| `vercel.json` | Only when hosting is Vercel **and** the framework is a static SPA. Next.js, Nuxt, SvelteKit, and Astro are auto-detected — do not create it |
| `.github/workflows/` | Only when migrations run through CI |
| `supabase/config.toml` | Only when the database is Supabase. Carries the one placeholder, `{{SUPABASE_PROJECT_REF}}` — an identifier, not a secret. This value is what the `guard_project_ref` hook pins every Supabase MCP call to. **Which ref goes in** follows Question 6 — staging exists → the staging project, never production |

**No `.mcp.json` is written — ever.** Database MCP servers are connected **user scope**, once per machine, never per repo; for Supabase the exact `claude mcp add -s user` one-liner is printed at Step 6. A repo-level server config would only duplicate what the machine already has. Project pinning does not come from server config: `supabase/config.toml` declares the repo's project, and the `guard_project_ref` hook in `raizen-norms` blocks any Supabase MCP call aimed at a different one. A database whose official MCP server exists follows the same pattern; a database with no server → say so rather than leaving the gap silent.

Then `git init`, `git branch -M main`, create `development` from `main`, and `git add` the new files. **Stop before committing.**

### Connectors are recommended, never a precondition

Where the database chosen at Question 5 has a Claude connector or an MCP server, say so once, say what it automates, and carry on whatever the answer is. Bootstrap never waits for one — every connector replaces work the user can also do by hand, and an app that cannot be started without one is an app held hostage to somebody's catalogue.

Two rules stop this from rotting:

- **Derive it from the stack, not from this file.** Name what Question 5 actually produced. Supabase appears here because the template covers it, not because it is the answer.
- **Never claim a connector exists.** The catalogue changes and this file does not. Point at the connector settings and let the user see what is really there; a promise that turns out false costs more than saying nothing.

Connectors for **hosting** are not raised here. Step 6 explains why, and `build-flow` raises them at the one moment they matter.

## Step 6 — Close

Report one block: the files created, then what the **user must do by hand right now** — create the database project chosen at Question 5, plus its staging counterpart if Question 6 asked for one, and connect it. For Supabase that means putting the **project ref** into `supabase/config.toml`, and — only on a machine not yet set up — connecting the MCP server user-scope, then approving the browser login on first use:

```
claude mcp add -s user --transport http supabase "https://mcp.supabase.com/mcp"
```

The URL must stay **bare** — Supabase's OAuth rejects any query string, so adding `?features=` or `?project_ref=` breaks the login itself.

Both are once per machine and account, never per repo, so a machine already set up needs nothing beyond the ref. For another database, whatever its own equivalent is. Pointed at production because there is no staging → say that plainly, since from then on every guarded destructive statement lands on live data. **No token is written into any file**; asking for one would be wrong. Name the variables, never their values. Without a live database there is no migration and no role test, so not a single page can be built.

Hosting connection, production environment variables, and the CI migration workflow are **not mentioned here**. None of them is needed to build a page locally, and naming them at bootstrap turns infrastructure into homework before anything exists to deploy. `vercel.json` and `.github/workflows/` are still written — inert files cost nothing — they are simply not wired up yet. The `build-flow` skill raises them once the app is ready to ship.

Then offer the next steps, unless the product has no UI:

```
Two sessions remain before pages can be built, in this order:
  /logic-init  — the logic layer: cache, validation, dates, logging,
                 scheduling, audit trail. Scored from the PRD; often
                 installs nothing.
  /design-init — the visual direction: a judged canvas page, then one real
                 page to judge.
Until design-init is done, any session will refuse to write UI components.
```

`logic-init` runs first because the pages `design-init` promotes carry loading, empty, and failed states — and those belong to the data layer.

Do not run it now. Bootstrap ends with zero dependencies installed, and `design-init` needs to install several.

Once the visual direction is agreed, building runs under the `build-flow` skill, which writes `QUEUE.md` on its first run. A new app builds its screens first — a UI batch, every page against a hand-written contract with no database behind it — then wires them in a backend batch. `build-flow` owns both, and the size of one session is set there.

Close by reminding the user that the first commit waits for their word, and that `raizen-norms` only becomes active once the next session starts in this repo.
