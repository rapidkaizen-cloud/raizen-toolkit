# Stack questions — N2: nine, with dynamic options

## How they are asked

- **Batch them** — up to four per AskUserQuestion call, several calls per turn; a question whose options or recommendation read an earlier answer (the *Fits when* column is the map) goes in a later call than its source.
- **Reconcile after every batch**: two answers that collide go back as one question naming both and what collides, never resolved silently.
- **Each question carries more than two options, one marked recommendation, and a one-sentence consequence per option** — question 8 has two answers, and so has question 9 where no screen exists. Questions 4 and 6 carry no recommendation, and say so where they are asked — both are vendor picks this toolkit has no stake in.
- **Accept an answer outside the options**: use it, and state its consequence if known or say it is not.
- **The stack is not locked.** Assemble platform, framework, hosting, and database options from the rubric below, filtered by the needs readable from the user's story.
- **Never offer an option marked Not ready** — a bootstrap that leaves a repo without config and without migrations has failed, and a junior developer will not know what is missing. The user names one anyway → accept it, and say plainly what they will have to set up themselves.
- **A Pioneer option never hides its cost**: its description opens with `Pioneer —` and what does not exist for it yet — no rubric row to read from, a research-driven bootstrap.
- **Do not ask the component library** — it is the library dialog of `design-settle`'s interview, asked once the app's real needs are readable from the documents, and `design-settle` also installs it.
- **After the last question, show the derived lines, then the defaults not asked**, in one message, and invite the user to name anything they want changed. Never walk through them one by one.
- **Verify live in one subagent pass** (`SKILL.md`, What a run costs), once the answers they depend on are in: the package manager line and question 8's recommended runner, by `library-rubric.md`'s method — a `design-settle` file, not read for this: maintained, broadly adopted, no fresh supply-chain event. It returns one line per candidate: verdict · last release · sources. Every other candidate is named from model knowledge and marked `unverified` until picked.

---

# Rubric — what may be offered

**The Status column decides how a row is offered**: **Ready** as a normal option · **Pioneer** as an option that opens with its cost · **Not ready** not at all.

**Status measures whether a row's guard coverage is stated and its migration or deploy path is named, never templates** — nothing is scaffolded for any stack beyond `CLAUDE.md`, `AGENTS.md`, and `.claude/settings.json`. A row that cannot say what protects a destructive statement is not Ready however many repos already run on it. A status is raised only through `pioneer.md`'s promotion checklist.

## Platform

| Choice | Fits when | Status |
|---|---|---|
| Web app | The work happens at a desk or in a browser, and nothing below pulls harder | **Ready** |
| CLI or service without UI | Nobody looks at a screen — automation, integration, a pipeline | **Ready** |
| Flutter multiplatform | One codebase must serve more than one OS — phone and desktop together — or field use without a browser | **Pioneer** |
| Android native | Phone-only field use, or deep device integration — camera, GPS, offline-first | **Pioneer** |
| Desktop shell — Tauri (recommended), Electron (alternative) | Desktop use with a window, a menu bar, a tray, or local files. The app stays web technology, so the design canvas and its browser proof carry over unchanged; what is new is the Proof profile, distribution in place of hosting, and the desktop design language. Electron over Tauri only where rendering must be identical on every OS — `stack-consequences.md` holds the difference | **Pioneer** |
| Desktop native (WPF, WinUI, SwiftUI) | Local hardware or OS integration a webview cannot reach | **Pioneer** |

Mobile and desktop frameworks are platforms, not framework rows: they are decided at question 2, and the Framework table applies only when the platform is web.

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

## Database

| Choice | Fits when | Status |
|---|---|---|
| Supabase | Database and login are both needed | **Ready** |
| Another Postgres (Neon, RDS) | The database already exists, or auth lives in another system | **Ready** — its own migration tool is named in the derived block, and auth is answered separately; the destructive guard still applies |
| No database | Nothing persists between sessions | **Ready** |
| Non-SQL (Firebase, MongoDB) | The data genuinely is not relational | **Not ready** — and **the destructive guard does not cover it**; see question 6 |

---

# The nine questions

## 1. Kind of app

**No fixed list.** Read the user's story and offer 3–4 kinds that fit *this* story — named in plain words, one marked recommendation, a one-sentence consequence each, invented for that story the way every taste slot in `design-settle` invents its options. An internal tool, a public product with accounts, a landing page, a game, a kiosk, a portfolio, a docs site are all answers this question can produce; none is assumed before the story is read, the recommendation is never a default kind, and an answer typed under Other is accepted as it is. The chosen kind is a label: it rides `design-settle`'s Step 1 reading sentence and the Problem in `docs/product.md`, and nothing downstream branches on the word itself.

**What downstream reads is four switches, derived from the story and reported as derived lines** — each with its value and where it came from, cancellable like every derived decision:

| Switch | Derived from | Decides |
|---|---|---|
| A screen exists | The story | `design-settle` applies and will write `DESIGN.md`, the Proof profile is written, questions 2–4 are asked. No screen → no design system and no Proof profile, questions 2, 3, and 4 are skipped |
| Who reaches it — named roles · strangers with accounts · anonymous visitors | Roles | Named roles or strangers with accounts → RLS and an access matrix from day one; strangers also make `logic-build`'s trust-boundary validation non-optional. Anonymous visitors only → no RLS, Roles collapse to what a visitor must be able to do |
| Register — judged on the first visit, or on the tenth use | Roles: how often a role comes back | The `frontend-design` branch in `design-settle`'s `frames.md`, whether `impeccable`'s operational register loads, posture allowed or the signature alone. A product with both a public front and a logged-in inside carries both, per page group |
| Data behind the pages | The Data row | Fixture cases and contracts in `build-flow`; without data, a page is proven at the two widths with its real copy |

The switches are not written into any document as fields — Context keeps its four rows. They are re-derived from Roles and the Data row whenever a skill needs them, and `design-settle`'s Step 0 block prints them so a wrong derivation is seen before it costs anything.

## 2. Platform

**Options from:** the Platform table — every row whose *Fits when* is plausible for the story, ordered best fit first, its Status label travelling into the option so the price is visible at the moment of choosing.

**Recommendation:** web, unless the story carries a signal from the Platform table — field use without a browser, kiosk, local hardware. It follows the story, not the table's order.

**Consequence:** web rides the rubric and the guard end to end; a Pioneer platform means a research-driven bootstrap and a rougher first run — written into the option itself.

A Pioneer answer, or a platform typed from outside the list → read `pioneer.md` now; it rules the rest of the bootstrap.

## 3. Framework and rendering

**Options from:** the Framework table, rows marked **Ready** whose *Fits when* is satisfied by the user's story.

**Recommendation:** Vite + React SPA for an app behind a login. There are public pages that must appear in search → Next.js. The story says nothing about public pages or SEO → do not recommend Next.js, because a server layer nobody needs is still a server layer somebody maintains.

**Consequence:** a static SPA has no server layer, so there is nowhere to hide a secret and nothing about rendering to understand first — traded against pages that search engines will not index.

## 4. Frontend hosting

**Options from:** the Hosting table, rows marked **Ready**, plus anything the user already runs.

**No recommendation, and no default.** Every row costs the same in scaffolding — nothing — and what decides it is operational: ask what already runs where, what is already paid for, and what else has to run beside the app.

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

## 8. Testing at bootstrap

**Question:** install a test runner now, or leave it until something is stable enough to test?

**Options:** assembled like every other package question — the runner that suits the chosen framework as the recommendation, verified live and never named from memory (How they are asked). The two answers differ in what they cost now: a runner installed at bootstrap is configuration to carry through every early change, and one added later is a small setup on a codebase that has stopped moving.

**Recommendation:** leave it until later for a first app; install now where the app carries money, permissions, or a rule that is expensive to get wrong.

## 9. Help for the app's users

**Question:** do the people who use the app get written help, and where do they read it? The repo's own documents are written either way, for the developer and the agent.

**Options:** `None` — nothing is written for users · `Guide pages` — one page per task under `docs/guide/`, written by the session that makes the task's page usable, read as files · `In-app help` — the same pages, and a page inside the app that renders them: one queue line, its route in English and its label in the UI language. No screen → `In-app help` is not offered.

**Recommendation:** `None` for a tool its own builders use; `In-app help` where a role is trained on the app, or the app changes hands.

The answer is Context's Help row, its first words verbatim — `none`, `guide pages`, `in-app` — and a decision record like every other.

---

# Derived, not asked — reported as a line with its value

Each has its answer the moment an earlier question is answered. Report each as its own line, with the value and the answer it came from; the user may overrule any of them on the spot. Never fold them into the defaults table below, where a decision nobody took goes to hide.

| Item | Derived from | Value |
|---|---|---|
| Language | The platform answer | **The chosen platform's own toolchain language — read from its row in the Platform rubric, never from a list kept here**, and never a language the platform cannot run: on a native platform TypeScript is a category error. **The one real choice is on the web**: report TypeScript with the reason, and take a plain-JavaScript answer without argument where the app's Kind makes it reasonable — a landing page, a single-form tool |
| Package manager | The platform answer | **Whatever that platform's toolchain ships.** Where it ships exactly one, the line says there is nothing to choose. Where the ecosystem has real competitors — Node is the case that matters — name them, verified live rather than recalled (How they are asked) |
| Migrations | The database answer | Supabase → the Supabase CLI's migration files. Another database → that engine's own migration tool, named. **How they run is not derived** — by hand from a machine, or through CI the user sets up; nothing here scaffolds a runner, so a repo with no CI is the normal state, not a gap |
| Styling | **Not decided here** | The component library decides it — see `design-settle` Step 3 — and this line only says where. Never write a styling default at bootstrap: shadcn requires Tailwind, MUI brings its own, and the library answer arrives later |

Language and Package manager are **rules, not tables**: the Platform rubric is the single list, and a second list here would drift from it. Where a platform's row does not make its toolchain obvious, report that gap in the rubric — never invent the mapping here.

---

# Defaults that are not asked

| Item | Default | Why |
|---|---|---|
| Branches | `main` for production, `development` for work | A session never works on `main` |
| UI language | Inferred from the user's story | What the app writes on screen. Shown as a concrete value, together with date format and thousands and decimal separators — never a separate question and never left unwritten, because a session opened months later in a different language cannot re-derive it |
| Code language | English, in every app | Comments, identifiers, file names, URL routes, API endpoint paths, and every database name. Never inferred from anything, and **written as its own line, never merged with UI language** — merged, "UI in X" reads as permission for identifiers, file names, and view names in X. Enum values are the one judgement call, decided per enum |
