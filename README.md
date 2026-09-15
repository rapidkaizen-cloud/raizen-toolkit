# raizen-toolkit

Private repo. Holds two Claude Code plugins plus a marketplace catalog pointing at both.

| Plugin | Installed | Used |
|---|---|---|
| `raizen-hub` | Globally, once per machine | Once per app — bootstrapping a new one, or writing the PRD an existing one never had |
| `raizen-norms` | Per app repo, via `.claude/settings.json` | Every working session in an app repo |

Split because their context cost differs: bootstrap norms have no business being loaded during daily work.

## Install

### Prerequisites

| Needed | Why | Check |
|---|---|---|
| Claude Code | — | `claude --version` |
| Python 3, reachable as `python3` | All four `raizen-norms` hooks are invoked as `python3`. A machine where only `python` resolves loses every guard **without an error** — they simply never run, and with the account-wide Supabase MCP that includes the project pin | `python3 --version` |
| Node.js | For the `npx skills add` route — the Supabase and taste skills both arrive that way | `node --version` |
| git | A private marketplace is pulled over git | `git --version` |

### Copy-paste into a Claude Code session

**Required.** Run these in order:

```
/plugin marketplace add <source-of-this-repo>
/plugin install raizen-hub@raizen
```

`<source-of-this-repo>` is one of:

| Route | What goes there | When |
|---|---|---|
| **ZIP** | The extracted folder path, e.g. `C:\Users\name\raizen-toolkit` | No git remote yet — the current route |
| **Private GitHub** | `<org>/raizen-toolkit` | Once this repo is pushed |

A ZIP source registers as type `directory`. It works fully, hooks included — the only difference is that `/plugin update` pulls nothing, so updating means replacing the folder's contents and running `/reload-plugins`.

**Recommended.** Nothing here errors without them, so they are separated on purpose — marking as required something that breaks nothing teaches people to ignore the word:

```
npx skills add supabase/agent-skills

/plugin marketplace add DietrichGebert/ponytail
/plugin install ponytail@ponytail
```

Restart the session once you are done installing.

The design flow loads two taste materials, and both are Required: `impeccable` (`npx impeccable install`, or the marketplace) and `frontend-design` (Anthropic's, via `/plugin`). Both are divergence guidance — they name templated defaults to avoid without prescribing a style. Skills that prescribe a fixed look (exact fonts, shadows, card recipes) are deliberately not read by any flow: a house style read for every app makes every app look like the house.

`impeccable` carries what `design-settle` and `ui-build` used to state themselves — the ban list, the display faces that mean the model stopped looking, the calibration against the three clusters AI interfaces converge on, the Operate register, and 59 deterministic detector rules. Only `reference/craft-floor.md`, `reference/operate.md`, and `new-work.md`'s two calibrations are read; `shape.md` and the rest of `new-work.md` are a competing pipeline and are not. `canvas.md` draws that boundary.

**Required means the flow is designed around them, not that it stops without them.** Absent, a session **asks** rather than merely reporting: it names what is lost — the ban list, the display-face and convergence calibrations, the Operate register, every detector count — and offers continuing without it against stopping to install. Continuing is a real answer; what is refused is the session spending most of the taste material on the user's behalf while a report line nobody read says it happened. Two notes on the install: its hook fires on every UI edit in every repo and asks to be told what was fixed — `design-settle` Steps 5 and 7 deliberately defer that to Step 8; and its skill description overlaps `design-settle`'s, so invoke the flow as `/design-settle` rather than typing "redesign my app".

### Why each one

**Required** — something breaks or comes out visibly poorer without it:

| Skill | Used for |
|---|---|
| `raizen-hub` | The four skills themselves — `app-settle`, `logic-settle`, `design-settle`, `app-conform` |
| `impeccable` | The craft rules `design-settle` and `ui-build` no longer state, plus the detector `design-settle` reports at Step 1 and Step 8. Loaded before the interview and before any component is written |
| `frontend-design` | Divergence guidance against templated defaults, loaded alongside `impeccable` — never a house style |

**Recommended** — nothing errors without them:

| Skill | Used for |
|---|---|
| `supabase-postgres-best-practices` | Consulted by `db-ops` before a migration is written — index patterns, column types, constraints, RLS policy shape. Disagreement with `db-ops` → `db-ops` wins, and `db-ops` already says to continue when it is absent. It earns its place on RLS, where the wrong shape leaks data rather than merely running slow |
| `ponytail` | Holds back over-engineering. This repo governs other repos, so excess here spreads — but that is a habit it enforces, not something any file calls |


`npx skills add supabase/agent-skills` installs a second skill alongside it, `supabase`, covering Auth, Storage, and `@supabase/ssr`. Nothing in this repo refers to that one; it rides along.

**Do not install the `supabase` plugin** from `claude-plugins-official`. It carries a Supabase MCP server of its own, duplicating whatever already reaches that database — the user-scope server (`claude mcp add -s user`, the one-liner printed by `app-settle` at N6), or a claude.ai connector where one is connected. Two servers means duplicated tools and an ambiguous pick at every call. The skill route above gives the same Postgres guidance without adding a server.

Connectors themselves — database, host, anything the stack uses — are **recommended where they exist and never required**. `app-settle` says so for the database and `build-flow` for the host, each at the point where it matters, derived from the stack the user actually chose. No list of connectors is kept here on purpose: the catalogue changes, this file would not, and a stale promise costs more than none.

The Supabase MCP server is connected **user scope, once per machine** — no `.mcp.json` is scaffolded into app repos, and the account-wide URL means one browser login covers every project. The URL carries **no query parameters at all**: Supabase's OAuth rejects any query string (`resource: Resource must be a valid MCP endpoint`), which is also why the old per-project `?project_ref=` URLs kept failing authentication. That rules out `read_only=true` (which `db-ops` Phase 3 never wanted — it sends guarded destructive statements, and read-only would replace a gated design with a blanket ban) and also rules out a `features` filter, so the full toolset is exposed; the context cost is accepted. Which project an MCP call may touch is pinned by `supabase/config.toml` plus the `guard_project_ref` hook in `raizen-norms`, not by the server config — the pin covers MCP calls only, not the `supabase` CLI or raw HTTP from Bash.

`raizen-norms` is **not installed by hand** — `app-settle` writes it into the app repo's `.claude/settings.json` at bootstrap.

The mechanisms differ deliberately: `raizen-hub` and `ponytail` are Claude Code plugins, while the Supabase and taste skills arrive through the Vercel Agent Skills framework (`npx skills add`) rather than a plugin marketplace. taste-skill is MIT licensed.

`ui-ux-pro-max` is no longer part of any flow here — no skill queries it, installed or not. Where it is installed it stays a standalone tool the user may invoke by name; nothing in this toolkit reads it, and its `--persist` flag must not be used inside an app repo (it writes a rival `MASTER.md` that competes with PRD Section 5).

`caveman` and `i-have-adhd` change how answers read, not what this toolkit does. They are unrelated to it — install them or not.

### Verify

In a fresh session, run `/plugin` and confirm `raizen-hub` is active.

Skills added with `npx skills add` never appear there. Check `~/.claude/skills/` for them, or run `/reload-skills` and look for `supabase-postgres-best-practices` by name.

`design-settle`'s reference question and direction frames run on the model's own design knowledge and need no WebSearch. The stack lines (component library, engines) still verify their candidates live — a session without WebSearch says what could not be verified instead of recalling it from memory as fact.

## Use

From an empty directory, in a Claude Code session:

```
/raizen-hub:app-settle
```

Then in the next sessions, inside the app repo just created:

```
/raizen-hub:logic-settle
/raizen-hub:design-settle
```

For an app that is **already running**, the entry point is `app-settle`, which reads the directory and runs in one of three modes. No `PRD.md` yet → document mode: it writes the PRD the repo never had and changes nothing about the app. `PRD.md` present → rework mode: it re-opens the app-level decisions — business rules, scope, stack — with keep always option one and every change carrying its cost and a recommendation. Then the two narrower rework skills follow:

```
/raizen-hub:app-settle
/raizen-hub:logic-settle
/raizen-hub:design-settle
```

To rework only the look or the logic layer of an app that already has a PRD, the last two are run on their own.

A repo that predates these plugins, or drifted from them, has a fourth entry point:

```
/raizen-hub:app-conform
```

It is the only skill here that changes code already written. Every other one reports and refuses to touch — `app-settle` document mode and `app-eval` both say so outright — which left the second job with no home. It audits the repo against the installed plugin text, ranks findings by what each costs to leave, stops for the user to pick, then executes one finding per commit. It never changes the stack and never adds a feature.

| Skill | Precondition | Produces |
|---|---|---|
| `app-settle` | Any directory — the mode is read from what it holds | Empty → `PRD.md` with an empty Section 5, scaffold, `git init`. Code without a PRD → document mode. Code with a PRD → rework mode |
| `logic-settle` | `PRD.md` present | Audits what the repo runs today — empty on a new repo — then Section 1 records cache, validator, dates, errors, jobs, attribution: keep, adopt, or replace per need, often installing nothing. One skill for both cases; the audit is what tells them apart |
| `design-settle` | Any repo with a UI to settle — a missing or off-shape `PRD.md` is read around, and the user's confirmed reading is the gate | Audits the styling the code uses today — empty on a repo with no UI — then one reference question whose ticks anchor the frames, the stack recommended in one install block, 2–4 full-fidelity direction frames drawn in every session with the real packages that the user picks from on screen, and Section 5 filled or changed line by line, styling tokens written, and every page promoted from the ratified canvas. One path for every repo; two facts read at Step 0 switch its steps |
| `app-conform` | `PRD.md` present, working tree clean | Existing code brought onto the conventions the plugins state today — platform residue, a `CLAUDE.md` duplicating the plugin, identifiers in the UI language, a norm that silently cannot apply, documents that should not exist. One finding per commit; never opened on its own initiative |
| `build-flow` | Section 5 filled | `QUEUE.md` on first run, then usable pages — a UI batch built against contracts first, wired in a backend batch after |

An app with components but no Section 5 — which is exactly what `app-settle`'s document mode hands over — runs the same `design-settle` path with its audit switched on: today's look stands among the direction frames, and picking it puts every measured value to the user for ratification rather than adopting it silently. Two facts read at Step 0 — UI present, Section 5 filled — switch the steps; there is no mode to pick.

`build-flow` is the only one with no command to type — it lives in `raizen-norms` and loads in every working session, which is the point: the build order has to be known before anyone thinks to ask for it.

## Maintaining

Change files in this repo, commit, then on the user's machine run `/plugin update raizen-norms@raizen`. Installed from a ZIP → replace the folder's contents and run `/reload-plugins`; `/plugin update` pulls nothing from a `directory` source.

An app bootstrapped by the current `app-settle` needs no touching. Its `CLAUDE.md` holds only that app's locale, stack, and the two gates that must survive the plugin being absent — norms are never copied there. **Nothing is scaffolded from a template**: every file a new repo gets is written for that repo's own answers, so there is no stock file to go stale between releases.

An app bootstrapped **before** a norm moved into the plugin still carries the old copy, and the two contradict each other without failing. The `SessionStart` hook detects this and names the sections to delete at the start of that repo's next session. Delete them once and the repo is done — sections retired so far:

| Delete from an older app's `CLAUDE.md` |
|---|
| the git paragraph under *Before touching anything* |
| the `GIT` block under *Closing a session* |
| the *Pointers* table |
| the *Scope* section |
| the closing report — *Report per scope item…* and the `PRD` block |
| the line *Read `PRD.md` at the start of a session* — the hook injects the file itself now |

Whenever another section is retired, add its distinctive phrase to `STALE` in `scripts/session_norms.py` and a row here. Nothing else finds the stale copies.

An app bootstrapped **before** the Supabase MCP went account-wide still carries a project-scoped `.mcp.json`. It keeps working, but it shadows the user-scope server — for the same server name, project scope wins over user scope — so that repo keeps its per-project OAuth until the file is gone. Migration is one deletion: remove `.mcp.json`, commit, restart the session; `supabase/config.toml` already holds the ref that `guard_project_ref` pins to. Nothing detects this automatically — `session_norms.py` reads only `CLAUDE.md`.

**`SKILL.md` changes take effect in the running session. Changes to `hooks/`, `.mcp.json`, and `agents/` do not** — they need `/reload-plugins` or a restart. A freshly edited hook is not active until then.

## Not yet verified

- That the hooks actually fire. The tests now invoke `python3` — the same name `hooks.json` uses — so a machine where only `python` resolves fails them instead of passing a test whose subject never runs. What that still does **not** prove is that `${CLAUDE_PLUGIN_ROOT}` expands and that `PreToolUse` matches: only a real session shows those. First session in a fresh app repo, try `git add -A` once and confirm it is refused.
- Whether a private marketplace is readable from a Claude Code cloud session. If not, `raizen-norms` does not load there and the guard hooks are inactive. Until this is verified, cloud sessions are limited to frontend work.
- Supabase MCP payload fields were verified against the official `supabase-community/supabase-mcp` source — `execute_sql`/`apply_migration` do use the `query` field. The tool **prefix** is no longer assumed: the `hooks.json` matcher is `mcp__.*`, and `plugins/raizen-norms/scripts/test_guard_destructive.py` now covers both `mcp__supabase__` (the user-scope server) and `mcp__claude_ai_Supabase__` (a claude.ai connection). Not yet exercised end to end: the hosted account-wide endpoint, its browser authorisation on first use, and whether its tools name the target with `project_id` exactly as `guard_project_ref.py` expects — a real session against a scaffolded app repo shows all three at once.
