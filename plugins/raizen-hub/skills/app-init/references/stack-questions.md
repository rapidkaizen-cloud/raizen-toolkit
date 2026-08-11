# Stack questions — six, with dynamic options

One question per turn. Each: **more than two options** · one marked recommendation · a one-sentence consequence. Answers outside the options are accepted.

**The stack is not locked.** Options are assembled from the rubric below, filtered by the needs readable from the user's story. Only one thing is locked: **options whose templates do not exist are not offered.** A bootstrap that produces a repo without config and without migrations is a failed bootstrap, and a junior developer will not know what is missing.

Component library is **not asked here** — it is question 0 in `design-init`, once the app's real needs are readable from the PRD, and `design-init` also installs it.

---

# Rubric — what may be offered

The **Status** column decides whether a row appears as an option.

## Framework and rendering

| Choice | Fits when | Status |
|---|---|---|
| Vite + React, static SPA | App behind a login, SEO is not at stake | **Ready** |
| Next.js | There are public pages that must be indexed, or a server layer is needed | **Ready** — Vercel auto-detects it, `vercel.json` is unused |
| Nuxt | Same, team already writes Vue | **Ready** |
| SvelteKit | Same, the bundle must stay as small as possible | **Ready** |
| Astro | The content is mostly static | **Ready** |
| React Native / Flutter | The story mentions field use without a browser | **Not ready** — no templates, and the deploy path is entirely different |

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

---

# The six questions

## 1. Kind of app

Multi-role internal dashboard · single-role internal tool · public site · CLI or service without UI

**Recommendation:** multi-role internal dashboard, if the story mentions more than one kind of user.

**Consequence:** multi-role means RLS and an access matrix from day one — slower in week one, but adding it later means touching every query again.

This answer filters every question after it. No UI → Section 5 is deleted entirely, questions 2 and 3 are skipped, `design-init` does not apply.

## 2. Framework and rendering

**Options from:** the Framework table above, rows marked **Ready** whose *Fits when* is satisfied by the user's story.

**Recommendation:** Vite + React SPA for an app behind a login. There are public pages that must appear in search → Next.js.

**Consequence:** a static SPA has no server layer, so there is nowhere to hide a secret and nothing about rendering to understand first — traded against pages that search engines will not index.

The story says nothing about public pages or SEO → do not recommend Next.js. A server layer nobody needs is still a server layer somebody maintains.

## 3. Frontend hosting

**Options from:** the Hosting table, rows marked **Ready**.

**Recommendation:** Vercel.

**Consequence:** Vercel separates environment variables per scope by default, so per-PR previews point at the staging database with no extra configuration.

The user names Cloudflare or Netlify → accept it, but say plainly that this repo carries no template for it, and name what they will have to set up themselves.

## 4. Database and login needed?

Both · database only · neither

**Recommendation:** both, if there is more than one user or data that survives between sessions.

**Consequence:** a database and auth that arrive together mean no separate auth provider to choose, and access rules live in one place.

Neither → skip questions 5 and 6.

## 5. Which database

**Options from:** the Database table, rows marked **Ready**.

**Recommendation:** Supabase.

**Consequence:** Supabase brings Postgres, auth, and RLS at once — and RLS becomes where access rules live, rather than application code.

The user names a non-SQL store → **say first that the destructive guard does not cover it**, then ask whether to proceed. This is not refusing their choice; it is making sure they know what they lose.

## 6. Database environments

Production only · production + staging · production + staging + local for development

**Recommendation:** production + staging if the data is operational; production only if the app is still an experiment.

**Consequence:** staging means a second database project and a second monthly bill, traded for per-PR previews that never touch real data. Adding local means the Supabase CLI and Docker must run on every machine.

---

# Defaults that are not asked

Show them all at once after the last question. Invite the user to name anything they want changed — do not walk through them one by one.

| Item | Default | Why |
|---|---|---|
| Language | TypeScript | Without types, a wrong data shape only surfaces at runtime |
| Styling | Tailwind | Keeps values in tokens rather than raw numbers in components |
| Migrations | Files in the repo, run by GitHub Actions | Schema gets versioned in git |
| Branches | `main` for production, `development` for work | A session never works on `main` |
| Package manager | npm | No strong reason for anything else at this size |
| Testing | Not installed at bootstrap | Installed once something is stable enough to test, not before |
| UI language | Inferred from the user's story | What the app writes on screen. Shown as a concrete value, together with date format and thousands and decimal separators, so a later session cannot re-derive it wrongly |
| Code language | English, in every app | Comments, identifiers, file names, URL routes, API endpoint paths, and every database name. Never inferred from the UI language — written as its own line so "UI in X" is not read as permission for identifiers in X. Enum values are the one judgement call, decided per enum |
