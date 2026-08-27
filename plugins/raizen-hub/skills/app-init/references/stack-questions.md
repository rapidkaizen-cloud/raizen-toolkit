# Stack questions — eight, with dynamic options

Questions travel in batches — up to four per AskUserQuestion call, several calls per turn; a question whose options or recommendation read an earlier answer (the *Fits when* column is the map) goes in a later call than its source. Answers are reconciled after every batch: two that collide go back as one question naming both, never resolved silently. Each: **more than two options** · one marked recommendation · a one-sentence consequence. Answers outside the options are accepted.

**The stack is not locked.** Options are assembled from the rubric below, filtered by the needs readable from the user's story. Two things are locked. **Options marked Not ready are not offered** — a bootstrap that produces a repo without config and without migrations is a failed bootstrap, and a junior developer will not know what is missing. And **a Pioneer option never hides its cost**: it is offered, but its description opens with what does not exist for it yet, and choosing it routes the bootstrap through the Pioneer path below.

Component library is **not asked here** — it is the library question in `design-init`, once the app's real needs are readable from the PRD, and `design-init` also installs it.

---

# Rubric — what may be offered

The **Status** column decides how a row is offered. **Ready** appears as a normal option. **Pioneer** appears as an option whose description opens with its cost — no templates, a research-driven bootstrap — governed by the Pioneer path below. **Not ready** is not offered at all.

## Platform

| Choice | Fits when | Status |
|---|---|---|
| Web app | The work happens at a desk or in a browser, and nothing below pulls harder | **Ready** |
| CLI or service without UI | Nobody looks at a screen — automation, integration, a pipeline | **Ready** |
| Flutter multiplatform | One codebase must serve phone and desktop, or field use without a browser | **Pioneer** |
| Android native | Phone-only field use, or deep device integration — camera, GPS, offline-first | **Pioneer** |
| Desktop native (Tauri, Electron, WPF, …) | Kiosk, heavy offline, local hardware, OS integration | **Pioneer** |

Mobile and desktop frameworks are platforms, not framework rows — they are decided at question 2, and the Framework table below applies only when the platform is web.

## Framework and rendering

| Choice | Fits when | Status |
|---|---|---|
| Vite + React, static SPA | App behind a login, SEO is not at stake | **Ready** |
| Next.js | There are public pages that must be indexed, or a server layer is needed | **Ready** — Vercel auto-detects it, `vercel.json` is unused |
| Nuxt | Same, team already writes Vue | **Ready** |
| SvelteKit | Same, the bundle must stay as small as possible | **Ready** |
| Astro | The content is mostly static | **Ready** |

## Hosting

| Choice | Fits when | Status |
|---|---|---|
| Vercel | Default for everything above | **Ready** |
| Cloudflare Workers | Team already uses it, or cost is the deciding factor | **Not ready** — needs `wrangler.toml`; see `stack-consequences.md` on build-time `VITE_*` |
| Netlify | Team already uses it | **Not ready** — needs `netlify.toml` |

## Database

| Choice | Fits when | Status |
|---|---|---|
| Supabase | Database and login are both needed | **Ready** |
| Another Postgres (Neon, RDS) | The database already exists, or auth lives in another system | **Not ready** — needs a replacement migration workflow; the destructive guard still applies |
| No database | Nothing persists between sessions | **Ready** |
| Non-SQL (Firebase, MongoDB) | The data genuinely is not relational | **Not ready** — and **the destructive guard does not cover it**; see the rule below |

## Adding a new stack to this rubric

**Not ready** becomes **Ready** only once three things exist:

1. Its config template in `templates/`, already tried in one real repo.
2. Its migration or deploy template, if that choice needs one.
3. **A statement of guard coverage.** The `raizen-norms` destructive guard works by matching SQL syntax in the `query`, `command`, `sql`, and `statement` fields. It survives any SQL database. It **does not apply** to non-SQL storage, and a hook that finds nothing does not report — it simply stays quiet. A stack outside the guard's reach must bring a replacement, or make the guard announce its own inapplicability once at session start.

Without item three, do not raise the status. A repo that looks protected while it is not is more dangerous than one that is plainly unprotected.

## The Pioneer path

**Pioneer** exists so that a platform without templates is a visible choice with a stated cost, instead of undefined behavior when the user names one anyway. It governs any Pioneer answer to question 2, and any platform typed in from outside the list. Six rules:

1. **Name what does not exist, first.** Three lines before anything continues: no config template in `templates/`, no deploy or build template, and the guard line below. One confirmation; declining routes back to a Ready platform.
2. **Storage decides the guard line.** The destructive guard matches SQL syntax, so any SQL store — Supabase, SQLite, Room, Drift — stays covered wherever the app runs. A non-SQL store is not covered, and the existing non-SQL rule applies unchanged: say so before question 6 is answered.
3. **The stack questions the tables cannot serve are assembled by live research.** Framework or language where the platform leaves a choice, distribution instead of hosting, project layout — real current options, more than two, one marked recommendation, a one-sentence consequence each. Never from memory alone.
4. **The scaffold is minimal and honest.** The platform's own init command, `.claude/settings.json`, and `CLAUDE.md` — nothing copied from `templates/` that assumes web. What a Ready platform would have received from templates is listed in the close block as work still owed.
5. **`PRD.md` Section 1 records `Platform: <name> (pioneer)`** — the marker later skills read to know this repo runs ahead of the toolkit's templates.
6. **The Proof profile is proven, not asserted.** Its shape lives in `prd-structure.md`. Before a line is written into Section 1, execute it once — run the run command, take one capture. A line that was not executed is written `[needs verification]`, and the skills that read it report instead of claim.

**After one real repo ships on a Pioneer platform, offer the promotion**: its config into `templates/`, through the three-item checklist above — that checklist is unchanged, and it is exactly what turns Pioneer into Ready.

---

# The eight questions

## 1. Kind of app

Multi-role internal dashboard · single-role internal tool · public site · CLI or service without UI

**Recommendation:** multi-role internal dashboard, if the story mentions more than one kind of user.

**Consequence:** multi-role means RLS and an access matrix from day one — slower in week one, but adding it later means touching every query again.

This answer filters every question after it. No UI → Section 5 is deleted entirely, questions 2, 3, and 4 are skipped, `design-init` does not apply.

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

**Options from:** the Hosting table, rows marked **Ready**.

**Recommendation:** Vercel.

**Consequence:** Vercel separates environment variables per scope by default, so per-PR previews point at the staging database with no extra configuration.

The user names Cloudflare or Netlify → accept it, but say plainly that this repo carries no template for it, and name what they will have to set up themselves.

## 5. Database and login needed?

Both · database only · neither

**Recommendation:** both, if there is more than one user or data that survives between sessions.

**Consequence:** a database and auth that arrive together mean no separate auth provider to choose, and access rules live in one place.

Neither → skip questions 6 and 7.

## 6. Which database

**Options from:** the Database table, rows marked **Ready**.

**Recommendation:** Supabase.

**Consequence:** Supabase brings Postgres, auth, and RLS at once — and RLS becomes where access rules live, rather than application code.

The user names a non-SQL store → **say first that the destructive guard does not cover it**, then ask whether to proceed. This is not refusing their choice; it is making sure they know what they lose.

## 7. Database environments

Production only · production + staging · production + staging + local for development

**Recommendation:** production + staging if the data is operational; production only if the app is still an experiment.

**Consequence:** staging means a second database project and a second monthly bill, traded for per-PR previews that never touch real data. Adding local means the Supabase CLI and Docker must run on every machine.

---

# Derived, not asked — reported as a line with its value

These have an answer the moment an earlier question is answered, so asking them again offers a choice that is already made. Each is reported as its own line with the value and the answer it came from, and the user may overrule any of them on the spot. Never folded into the defaults table below: a table read once at bootstrap is exactly where a decision nobody took goes to hide.

| Item | Derived from | Value |
|---|---|---|
| Language | The platform answer | Web, Tauri, or Electron → TypeScript. iOS → Swift. Android → Kotlin. A cross-platform native shell → whatever its own toolchain speaks — Dart for Flutter, TypeScript for React Native, Kotlin for KMP. **Never named as TypeScript before the platform is known**; on a native platform TypeScript is not a default, it is a category error |
| Package manager | The platform answer | Node-based platforms → npm, with pnpm and bun as the named alternatives the user may take on the spot. Android → Gradle. iOS → Swift Package Manager. Flutter → pub. On every native platform the toolchain ships one and there is nothing to choose |
| Migrations | The database answer | Supabase → the Supabase CLI's migration files, run by GitHub Actions. Another database → that engine's own migration tool, named |
| Styling | **Not decided here.** The component library decides it, and that question belongs to `design-init` | Reported there, not here — see `design-init` Step 3 |

**Language carries one real choice, and only on the web.** A small surface — a landing page, a single-form tool — can ship plain JavaScript, and the derived line says so rather than hiding it: report TypeScript with the reason, and take a plain-JavaScript answer without argument where the app's Kind makes it reasonable. What is never reported is a language the platform cannot run.

Styling is named in this block only to say where it is decided. Writing a styling default at bootstrap and letting `design-init` pick a library that contradicts it is how a repo ends up with a decision nobody made: shadcn requires Tailwind, MUI brings its own, and the library answer arrives later.

## 8. Testing at bootstrap

**Question:** install a test runner now, or leave it until something is stable enough to test?

**Options:** assembled under the rubric like every other package question — verified live, never named from memory — with the runner that suits the chosen framework as the recommendation. The two answers differ in what they cost now: a runner installed at bootstrap is configuration to carry through every early change, and one added later is a small setup on a codebase that has stopped moving.

**Recommendation:** leave it until later for a first internal app; install now where the app carries money, permissions, or a rule that is expensive to get wrong.

---

# Defaults that are not asked

Show them all at once after the last question. Invite the user to name anything they want changed — do not walk through them one by one.

| Item | Default | Why |
|---|---|---|
| Branches | `main` for production, `development` for work | A session never works on `main` |
| UI language | Inferred from the user's story | What the app writes on screen. Shown as a concrete value, together with date format and thousands and decimal separators, so a later session cannot re-derive it wrongly |
| Code language | English, in every app | Comments, identifiers, file names, URL routes, API endpoint paths, and every database name. Never inferred from the UI language — written as its own line so "UI in X" is not read as permission for identifiers in X. Enum values are the one judgement call, decided per enum |
