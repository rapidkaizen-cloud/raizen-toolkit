# Stack questions — eight, with dynamic options

Questions travel in batches — up to four per AskUserQuestion call, several calls per turn; a question whose options or recommendation read an earlier answer (the *Fits when* column is the map) goes in a later call than its source. Answers are reconciled after every batch: two that collide go back as one question naming both, never resolved silently. Each: **more than two options** · one marked recommendation · a one-sentence consequence. Answers outside the options are accepted.

**Two questions carry no recommendation, and say so where they are asked** — hosting and which database. Both are vendor picks this toolkit no longer has a stake in, and a recommendation there is a default wearing a question's clothes. Every other question keeps one.

**The stack is not locked.** Options are assembled from the rubric below, filtered by the needs readable from the user's story. Two things are locked. **Options marked Not ready are not offered** — a bootstrap that produces a repo without config and without migrations is a failed bootstrap, and a junior developer will not know what is missing. And **a Pioneer option never hides its cost**: it is offered, but its description opens with what does not exist for it yet, and choosing it routes the bootstrap through the Pioneer path below.

Component library is **not asked here** — it is the library dialog of `design-settle`'s interview, once the app's real needs are readable from the PRD, and `design-settle` also installs it.

---

# Rubric — what may be offered

The **Status** column decides how a row is offered. **Ready** appears as a normal option. **Pioneer** appears as an option whose description opens with its cost — no rubric row to read from, a research-driven bootstrap — governed by the Pioneer path below. **Not ready** is not offered at all.

**Status does not measure templates.** This toolkit scaffolds no hosting, CI, or database config for any stack — only `CLAUDE.md`, `AGENTS.md`, and `.claude/settings.json`, which every repo gets whatever it runs on. What a row's status measures is whether its **guard coverage is stated** and its **migration or deploy path is named**. A row that cannot say what protects a destructive statement is not Ready however many repos already run on it.

## Platform

| Choice | Fits when | Status |
|---|---|---|
| Web app | The work happens at a desk or in a browser, and nothing below pulls harder | **Ready** |
| CLI or service without UI | Nobody looks at a screen — automation, integration, a pipeline | **Ready** |
| Flutter multiplatform | One codebase must serve more than one OS — phone and desktop together — or field use without a browser | **Pioneer** |
| Android native | Phone-only field use, or deep device integration — camera, GPS, offline-first | **Pioneer** |
| Desktop shell — Tauri (recommended), Electron (alternative) | Desktop use with a window, a menu bar, a tray, or local files. The app stays web technology, so the design canvas and its browser proof carry over unchanged; what is new is the Proof profile, distribution in place of hosting, and the desktop design language. Electron over Tauri only where rendering must be identical on every OS — `stack-consequences.md` holds the difference | **Pioneer** |
| Desktop native (WPF, WinUI, SwiftUI) | Local hardware or OS integration a webview cannot reach | **Pioneer** |

Mobile and desktop frameworks are platforms, not framework rows — they are decided at question 2, and the Framework table below applies only when the platform is web.

## Framework and rendering

| Choice | Fits when | Status |
|---|---|---|
| Vite + React, static SPA | App behind a login, SEO is not at stake | **Ready** |
| Next.js | There are public pages that must be indexed, or a server layer is needed | **Ready** — carries its own server layer, so no rewrite rule is needed wherever it is hosted |
| Nuxt | Same, team already writes Vue | **Ready** |
| SvelteKit | Same, the bundle must stay as small as possible | **Ready** |
| Astro | The content is mostly static | **Ready** |

## Hosting

| Choice | Fits when | Status |
|---|---|---|
| Vercel | Nothing pulls elsewhere, and per-scope environment variables are wanted without configuring them | **Ready** — one rewrite rule for a static SPA, written by the session |
| Own server (VPS) | The app must sit beside services already running there, or the server is already paid for | **Ready** — web server config and a deploy path, both written by the session |
| Cloudflare Workers | Cost is the deciding factor, or the team already uses it | **Ready** — needs `wrangler.toml`; see `stack-consequences.md` on build-time `VITE_*` |
| Netlify | Team already uses it | **Ready** — needs `netlify.toml` |

**None of these is a default.** What separates them is operational rather than technical: who already pays for what, and what else has to run beside the app.

## Database

| Choice | Fits when | Status |
|---|---|---|
| Supabase | Database and login are both needed | **Ready** |
| Another Postgres (Neon, RDS) | The database already exists, or auth lives in another system | **Ready** — its own migration tool is named in the derived block, and auth is answered separately; the destructive guard still applies |
| No database | Nothing persists between sessions | **Ready** |
| Non-SQL (Firebase, MongoDB) | The data genuinely is not relational | **Not ready** — and **the destructive guard does not cover it**; see the rule below |

## Adding a new stack to this rubric

**Not ready** becomes **Ready** only once two things exist:

1. **A named migration or deploy path**, written out once in a real repo so the session that chooses this row knows what it has to produce. Not a template — this toolkit ships none — a description precise enough to follow.
2. **A statement of guard coverage.** The `raizen-norms` destructive guard works by matching SQL syntax in the `query`, `command`, `sql`, and `statement` fields. It survives any SQL database. It **does not apply** to non-SQL storage, and a hook that finds nothing does not report — it simply stays quiet. A stack outside the guard's reach must bring a replacement, or make the guard announce its own inapplicability once at session start.

Without item two, do not raise the status. A repo that looks protected while it is not is more dangerous than one that is plainly unprotected.

## The Pioneer path

**Pioneer** exists so that a platform without templates is a visible choice with a stated cost, instead of undefined behavior when the user names one anyway. It governs any Pioneer answer to question 2, and any platform typed in from outside the list. Six rules:

1. **Name what does not exist, first.** Three lines before anything continues: no rubric row to read the options from, no repo that has run this platform under these plugins, and the guard line below. One confirmation; declining routes back to a Ready platform. The absence of templates is **not** one of the lines — no platform has any, so naming it here would price a cost every choice carries.
2. **Storage decides the guard line.** The destructive guard matches SQL syntax, so any SQL store — Supabase, SQLite, Room, Drift — stays covered wherever the app runs. A non-SQL store is not covered, and the existing non-SQL rule applies unchanged: say so before question 6 is answered.
3. **The stack questions the tables cannot serve are assembled by live research.** Framework or language where the platform leaves a choice, distribution instead of hosting, project layout — real current options, more than two, one marked recommendation, a one-sentence consequence each. Never from memory alone.
4. **The scaffold is minimal and honest.** The platform's own init command, `.claude/settings.json`, `CLAUDE.md`, and `AGENTS.md` — the same three files a Ready platform receives, since nothing else is scaffolded for anyone. What is still owed is the platform's own config and deploy path, listed in the close block.
5. **`PRD.md` Section 1 records `Platform: <name> (pioneer)`** — the marker later skills read to know this repo runs ahead of the toolkit's templates.
6. **The Proof profile is proven, not asserted.** Its shape lives in `prd-structure.md`. Before a line is written into Section 1, execute it once — run the run command, take one capture. A line that was not executed is written `[needs verification]`, and the skills that read it report instead of claim.

**After one real repo ships on a Pioneer platform, offer the promotion**: a row in the rubric above, through the two-item checklist — the migration or deploy path written out, and the guard line stated. That is what turns Pioneer into Ready. No file is copied anywhere to do it — this plugin ships no templates for any stack.

---

# The eight questions

## 1. Kind of app

**No fixed list.** Read the user's story and offer 3–4 kinds that fit *this* story — named in plain words, one marked recommendation, a one-sentence consequence each — the way every taste slot in `design-settle` invents its options. An internal tool, a public product with accounts, a landing page, a game, a kiosk, a portfolio, a docs site are all answers this question can produce; none is assumed before the story is read, and an answer typed under Other is accepted as it is. The chosen kind is a label: it rides the Step 1 reading sentence and Section 1's problem statement, and nothing downstream branches on the word itself.

**What downstream reads is four switches, derived from the story and reported as derived lines** — each with its value and where it came from, cancellable like every derived decision:

| Switch | Derived from | Decides |
|---|---|---|
| A screen exists | The story | Section 5 exists, `design-settle` applies, questions 2–4 are asked. No screen → Section 5 is deleted entirely, questions 2, 3, and 4 are skipped |
| Who reaches it — named roles · strangers with accounts · anonymous visitors | Section 2 | Named roles or strangers with accounts → RLS and an access matrix from day one; strangers also make `logic-build`'s trust-boundary validation non-optional. Anonymous visitors only → no RLS, Section 2 collapses to what a visitor must be able to do |
| Register — judged on the first visit, or on the tenth use | Section 2: how often a role comes back | The `frontend-design` branch in `canvas.md`, whether `impeccable`'s operational register loads, posture allowed or the signature alone. A product with both a public front and a logged-in inside carries both, per page group |
| Data behind the pages | Section 1's Data row | Fixture cases and contracts in `build-flow`; without data, a page is proven at the two widths with its real copy |

The switches are not written into the PRD as fields — Section 1 keeps its three rows. They are re-derived from Section 2 and the Data row whenever a skill needs them, and `design-settle`'s Step 0 block prints them so a wrong derivation is seen before it costs anything.

**Recommendation:** follows the story, never a default kind.

**Consequence:** stated per option, invented for that story.

## 2. Platform

**Options from:** the Platform table above — every row whose *Fits when* is plausible for the story, ordered best fit first. The Status label travels into the option: a Pioneer option's description opens with `Pioneer —` and its cost, so the price is visible at the moment of choosing, never after.

**Recommendation:** web, unless the story carries a signal from the Platform table — field use without a browser, kiosk, local hardware. The recommendation follows the story, not the table's order.

**Consequence:** web rides templates and guard end to end; a Pioneer platform means a research-driven bootstrap with no templates and a rougher first run — written into the option itself.

A Pioneer answer, or a platform typed from outside the list, puts the rest of the bootstrap under the Pioneer path above: questions 3 and 4 are replaced by research-assembled equivalents, questions 5–7 still run — the database does not care where the app runs, only the guard line does.

## 3. Framework and rendering

**Options from:** the Framework table above, rows marked **Ready** whose *Fits when* is satisfied by the user's story.

**Recommendation:** Vite + React SPA for an app behind a login. There are public pages that must appear in search → Next.js.

**Consequence:** a static SPA has no server layer, so there is nowhere to hide a secret and nothing about rendering to understand first — traded against pages that search engines will not index.

The story says nothing about public pages or SEO → do not recommend Next.js. A server layer nobody needs is still a server layer somebody maintains.

## 4. Frontend hosting

**Options from:** the Hosting table, rows marked **Ready**, plus anything the user already runs.

**No recommendation.** This is the one question where the toolkit has nothing to add: every row costs the same in scaffolding — nothing — and what decides it lives outside the code. Ask what already runs where, and what is already paid for. Presenting a default here would answer a question only the user can.

**Consequence, per option, in one sentence each** — Vercel separates environment variables per scope with no configuration; a VPS puts the app beside whatever else runs there and makes those variables and the TLS certificate the user's to manage; Cloudflare and Netlify each need their own config file, named in the Hosting table.

Whatever is chosen, say plainly what the session will have to write for it, and write it.

## 5. Database and login needed?

Both · database only · neither

**Recommendation:** both, if there is more than one user or data that survives between sessions.

**Consequence:** a database and auth that arrive together mean no separate auth provider to choose, and access rules live in one place.

Neither → skip questions 6 and 7.

## 6. Which database

**Options from:** the Database table, rows marked **Ready**, plus anything the user already runs.

**No recommendation**, for the same reason as question 4: what decides it is what already exists and what is already paid for.

**Consequence, per option, in one sentence each** — Supabase brings Postgres, auth, and RLS together, so access rules live in the database rather than in application code; another Postgres means auth is a separate choice and the migration tool is that engine's own; no database means nothing survives between sessions.

The user names a non-SQL store → **say first that the destructive guard does not cover it**, then ask whether to proceed. This is not refusing their choice; it is making sure they know what they lose.

## 7. Database environments

Production only · production + staging · production + staging + local for development

**Recommendation:** production + staging if the data is operational; production only if the app is still an experiment.

**Consequence:** staging means a second database project and a second monthly bill, traded for per-PR previews that never touch real data. Adding local means that engine's own local stack on every machine — for Supabase, its CLI and Docker.

---

# Derived, not asked — reported as a line with its value

These have an answer the moment an earlier question is answered, so asking them again offers a choice that is already made. Each is reported as its own line with the value and the answer it came from, and the user may overrule any of them on the spot. Never folded into the defaults table below: a table read once at bootstrap is exactly where a decision nobody took goes to hide.

| Item | Derived from | Value |
|---|---|---|
| Language | The platform answer | **The chosen platform's own toolchain language — read from its row in the Platform rubric above, never from a list kept here.** A second list in this block is a list that drifts from the rubric the moment a platform is added to it. On a native platform TypeScript is not a weak default, it is a category error |
| Package manager | The platform answer | **Whatever that platform's toolchain ships.** Where it ships exactly one, there is nothing to choose and the line says so. Where the ecosystem has real competitors — Node is the case that matters — name them under `library-rubric.md`'s method, verified live rather than recalled, because that field changes faster than this file does |
| Migrations | The database answer | Supabase → the Supabase CLI's migration files. Another database → that engine's own migration tool, named. **How they run is not derived** — by hand from a machine, or through CI the user sets up; nothing here scaffolds a runner, so a repo with no CI is the normal state, not a gap |
| Styling | **Not decided here.** The component library decides it, and that question belongs to `design-settle` | Reported there, not here — see `design-settle` Step 3 |

Both rows are **rules, not tables**, and deliberately so: the Platform rubric above is the single list, it carries a documented path for adding a stack, and anything restated here would go stale without anyone noticing. Where a platform's row does not make its toolchain obvious, that is a gap in the rubric to report — not a reason to invent the mapping in this block.

**Language carries one real choice, and only on the web.** A small surface — a landing page, a single-form tool — can ship plain JavaScript, and the derived line says so rather than hiding it: report TypeScript with the reason, and take a plain-JavaScript answer without argument where the app's Kind makes it reasonable. What is never reported is a language the platform cannot run.

Styling is named in this block only to say where it is decided. Writing a styling default at bootstrap and letting `design-settle` pick a library that contradicts it is how a repo ends up with a decision nobody made: shadcn requires Tailwind, MUI brings its own, and the library answer arrives later.

## 8. Testing at bootstrap

**Question:** install a test runner now, or leave it until something is stable enough to test?

**Options:** assembled under the rubric like every other package question — verified live, never named from memory — with the runner that suits the chosen framework as the recommendation. The two answers differ in what they cost now: a runner installed at bootstrap is configuration to carry through every early change, and one added later is a small setup on a codebase that has stopped moving.

**Recommendation:** leave it until later for a first app; install now where the app carries money, permissions, or a rule that is expensive to get wrong.

---

# Defaults that are not asked

Show them all at once after the last question. Invite the user to name anything they want changed — do not walk through them one by one.

| Item | Default | Why |
|---|---|---|
| Branches | `main` for production, `development` for work | A session never works on `main` |
| UI language | Inferred from the user's story | What the app writes on screen. Shown as a concrete value, together with date format and thousands and decimal separators, so a later session cannot re-derive it wrongly |
| Code language | English, in every app | Comments, identifiers, file names, URL routes, API endpoint paths, and every database name. Never inferred from the UI language — written as its own line so "UI in X" is not read as permission for identifiers in X. Enum values are the one judgement call, decided per enum |
