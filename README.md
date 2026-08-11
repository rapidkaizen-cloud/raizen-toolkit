# raizen-toolkit

Private repo. Holds two Claude Code plugins plus a marketplace catalog pointing at both.

| Plugin | Installed | Used |
|---|---|---|
| `raizen-hub` | Globally, once per machine | Once per new app — bootstrap |
| `raizen-norms` | Per app repo, via `.claude/settings.json` | Every working session in an app repo |

Split because their context cost differs: bootstrap norms have no business being loaded during daily work.

## Install

### Prerequisites

| Needed | Why | Check |
|---|---|---|
| Claude Code | — | `claude --version` |
| Python 3, reachable as `python3` | `ui-ux-pro-max` runs `search.py`, and all three `raizen-norms` hooks are invoked as `python3`. A machine where only `python` resolves loses every guard **without an error** — they simply never run | `python3 --version` |
| Node.js | For the `npx skills add` route — the Supabase and taste skills both arrive that way | `node --version` |
| git | A private marketplace is pulled over git | `git --version` |

### Copy-paste into a Claude Code session

**Required.** Run these in order:

```
/plugin marketplace add nextlevelbuilder/ui-ux-pro-max-skill
/plugin install ui-ux-pro-max@ui-ux-pro-max-skill

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

**Only if you build public sites** — `design-init` references it in one branch only, and its prohibitions are already copied into `anti-pattern.md`, so internal apps do not need it:

```
npx skills add https://github.com/Leonxlnx/taste-skill --skill "design-taste-frontend"
```

Restart the session once you are done installing.

### Why each one

**Required** — something breaks or comes out visibly poorer without it:

| Skill | Used for |
|---|---|
| `ui-ux-pro-max` | The source of every option and recommendation across the 27 visual questions. Without it `design-init` can only offer self-assembled options, which it must mark as not coming from the database |
| `raizen-hub` | `app-init`, `design-init`, and `design-redesign` themselves |

**Recommended** — nothing errors without them:

| Skill | Used for |
|---|---|
| `supabase-postgres-best-practices` | Consulted by `db-ops` before a migration is written — index patterns, column types, constraints, RLS policy shape. Disagreement with `db-ops` → `db-ops` wins, and `db-ops` already says to continue when it is absent. It earns its place on RLS, where the wrong shape leaks data rather than merely running slow |
| `ponytail` | Holds back over-engineering. This repo governs other repos, so excess here spreads — but that is a habit it enforces, not something any file calls |
| `design-taste-frontend` | Public sites only, as above |

`npx skills add supabase/agent-skills` installs a second skill alongside it, `supabase`, covering Auth, Storage, and `@supabase/ssr`. Nothing in this repo refers to that one; it rides along.

**Do not install the `supabase` plugin** from `claude-plugins-official`. It carries a Supabase MCP server of its own, duplicating whatever already reaches that database — an app repo's own `.mcp.json`, or a claude.ai connector where one is connected. Two servers means duplicated tools and an ambiguous pick at every call. The skill route above gives the same Postgres guidance without adding a server.

Connectors themselves — database, host, anything the stack uses — are **recommended where they exist and never required**. `app-init` says so for the database and `build-flow` for the host, each at the point where it matters, derived from the stack the user actually chose. No list of connectors is kept here on purpose: the catalogue changes, this file would not, and a stale promise costs more than none.

`templates/.mcp.json` deliberately does **not** set `read_only=true`. `db-ops` Phase 3 sends guarded destructive statements through that server, so read-only would replace a gated design with a blanket ban. It does restrict `features` to the tool groups `db-ops` and `build-flow` actually use.

`raizen-norms` is **not installed by hand** — `app-init` writes it into the app repo's `.claude/settings.json` at bootstrap.

The mechanisms differ deliberately: `ui-ux-pro-max`, `raizen-hub`, and `ponytail` are Claude Code plugins, while the Supabase and taste skills arrive through the Vercel Agent Skills framework (`npx skills add`) rather than a plugin marketplace. taste-skill is MIT licensed.

`caveman` and `i-have-adhd` change how answers read, not what this toolkit does. They are unrelated to it — install them or not.

### Verify

In a fresh session, run `/plugin` and confirm `ui-ux-pro-max` and `raizen-hub` are active.

Skills added with `npx skills add` never appear there. Check `~/.claude/skills/` for them, or run `/reload-skills` and look for `supabase-postgres-best-practices` by name.

The only absence that actually costs output quality is **`ui-ux-pro-max`**: `design-init` still runs, but its options become agent-assembled ones that must be marked *not from the database*, and Section 5 comes out far poorer.

`design-init` fails to run its search → check Python first.

## Use

From an empty directory, in a Claude Code session:

```
/raizen-hub:app-init
```

Then in the next session, inside the app repo just created:

```
/raizen-hub:design-init
```

To rework the look of an app already running:

```
/raizen-hub:design-redesign
```

| Skill | Precondition | Produces |
|---|---|---|
| `app-init` | Empty directory | `PRD.md` with an empty Section 5, scaffold, `git init` |
| `design-init` | Section 5 empty | Section 5 filled, styling tokens, one working reference page |
| `design-redesign` | Section 5 filled | Section 5 changed line by line, plus every component updated in one pass |
| `build-flow` | Section 5 filled | `QUEUE.md` on first run, then one usable page per session |

`build-flow` is the only one with no command to type — it lives in `raizen-norms` and loads in every working session, which is the point: the build order has to be known before anyone thinks to ask for it.

## Maintaining

Change files in this repo, commit, then on the user's machine run `/plugin update raizen-norms@raizen`. Installed from a ZIP → replace the folder's contents and run `/reload-plugins`; `/plugin update` pulls nothing from a `directory` source.

An app bootstrapped from the current template needs no touching. Its `CLAUDE.md` holds only that app's locale, stack, and the two gates that must survive the plugin being absent — norms are never copied there.

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

**`SKILL.md` changes take effect in the running session. Changes to `hooks/`, `.mcp.json`, and `agents/` do not** — they need `/reload-plugins` or a restart. A freshly edited hook is not active until then.

## Not yet verified

- That the hooks actually fire. The tests now invoke `python3` — the same name `hooks.json` uses — so a machine where only `python` resolves fails them instead of passing a test whose subject never runs. What that still does **not** prove is that `${CLAUDE_PLUGIN_ROOT}` expands and that `PreToolUse` matches: only a real session shows those. First session in a fresh app repo, try `git add -A` once and confirm it is refused.
- Whether a private marketplace is readable from a Claude Code cloud session. If not, `raizen-norms` does not load there and the guard hooks are inactive. Until this is verified, cloud sessions are limited to frontend work.
- Supabase MCP payload fields were verified against the official `supabase-community/supabase-mcp` source — `execute_sql`/`apply_migration` do use the `query` field. The tool **prefix** is no longer assumed: the `hooks.json` matcher is `mcp__.*`, and `plugins/raizen-norms/scripts/test_guard_destructive.py` now covers both `mcp__supabase__` (an app repo's own server, keyed in `templates/.mcp.json`) and `mcp__claude_ai_Supabase__` (a claude.ai connection). Not yet exercised end to end: the hosted endpoint `templates/.mcp.json` now points at, and its browser authorisation on first use.
