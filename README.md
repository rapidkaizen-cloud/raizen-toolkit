# raizen-toolkit

One plugin, `raizen-norms`, and the marketplace `raizen`, in the public repo `rapidkaizen-cloud/raizen-toolkit`. The repo root is the plugin, for Claude Code and for Antigravity — see [Antigravity](#antigravity).

| Holds | Loaded |
|---|---|
| `app-settle`, `logic-settle`, `design-settle`, `app-align` | When invoked |
| `build-flow`, `docs-format`, `ui-build`, `db-ops`, `logic-build` | By their descriptions |
| Session norms, guard hooks | Every session where the plugin is enabled — installed at user scope, every folder on that machine; `app-settle` writes the `enabledPlugins` line into each app repo |

## Install

Needs Claude Code, `python3` (every `raizen-norms` hook calls it; with only `python` the guards silently never run), and Node.js.

```
/plugin marketplace add rapidkaizen-cloud/raizen-toolkit
/plugin install raizen-norms@raizen
```

- Install at **user scope** only; a project-scope entry updates separately and falls behind.
- In `~/.claude/settings.json`, set `"autoUpdate": true` on `raizen` under `extraKnownMarketplaces`, so a new version reaches the machine at its next start.
- Restart Claude Code.

Required alongside: `impeccable` (`npx impeccable install`), `frontend-design` (`/plugin`), and `ui-ux-pro-max` (`/plugin marketplace add nextlevelbuilder/ui-ux-pro-max-skill`, then `/plugin install ui-ux-pro-max@ui-ux-pro-max-skill`) — the UX floor level with `impeccable`, and the style, palette and type results `design-settle` mixes into its frames; `ui-build` forbids `--persist` and every script of its sub-skills. A session missing any asks before continuing. Invoke `/design-settle` by name, since `impeccable`'s description overlaps it.

Optional, never asked for when absent:
- `review-animations`, the motion floor on web Surfaces — installed alone: `npx skills add emilkowalski/skills --skill review-animations -g -a claude-code`.
- `apple-design`, Apple's guideline pages `design-settle` reads for a macOS Surface: `npx skills add dickwu/apple-design-skill --skill apple-design -g -a claude-code --copy`, then add `disable-model-invocation: true` to the frontmatter of `~/.claude/skills/apple-design/SKILL.md` — its description matches any design review, and it must never load as a reviewer. `npx skills update` drops the line; add it again.

Recommended: `npx skills add supabase/agent-skills` (Postgres guidance for `db-ops`) and `ponytail`. Do not install the `supabase` plugin — it adds a second Supabase MCP server. Connect the Supabase MCP once at user scope, with no query parameters in its URL.

Two conventions come with `raizen-norms`, and every app inherits them:
- Sessions sign in and seed test data through an **agent account**: `db-ops` creates it by SQL on Supabase Auth, taking its email and password from the session's own instructions (your `~/.claude/CLAUDE.md`, for example) — the toolkit stores neither.
- Every row a session creates for a test opens with **`[CLAUDE]`**. Only a `DELETE` narrowed to that prefix passes `guard_destructive` unguarded; any other delete goes through the destructive gate.

Check: `/plugin` lists `raizen-norms`; design-settle's Step 0 prints the running build as `Skill build`.

## Update

Every commit that changes the plugin bumps its version (`.githooks/pre-commit` refuses otherwise — run `git config core.hooksPath .githooks` once per clone). After the push, a machine with `autoUpdate` on picks it up at its next start; on any other machine run:

```
claude plugin marketplace update raizen
claude plugin update raizen-norms@raizen
```

Then restart. Nothing reaches a session before this. What each version changes: `CHANGELOG.md`.

## Antigravity

The repo root is an Antigravity plugin too: `plugin.json` and `hooks.json` at the root are its manifest and its hooks, beside Claude Code's `.claude-plugin/` and `hooks/`.

Install once per machine:

```
agy plugin install https://github.com/rapidkaizen-cloud/raizen-toolkit
```

Update: `agy plugin uninstall raizen-norms`, then install again — the install is a copy, and nothing refreshes it.

**Proven on the CLI** — `agy` 1.2.16, Windows, headless, installed from a folder with `agy plugin install`: the nine skills are listed, `hooks.json` is kept as written, the norms and the `HOST` block are injected, `git add -A` is refused, and a push is held. The copy lands in `~/.gemini/config/plugins/raizen-norms`. Proven before 0.70.0 only, registered by path: an interactive session, a held push passing on `Run` and held again once it has run, the hand-over block.

- Install it for the machine as above, never through a repo's `.agents/plugins.json`: registered per folder, the plugin loaded a minute after an interactive conversation began, and that conversation ran unguarded.
- Never run `agy plugin import` on this plugin: it replaces `hooks.json` with Claude Code's, which Antigravity cannot parse, and every guard goes silent.
- `python3` must resolve: there a hook that cannot start blocks every command.
- A headless run (`agy -p`) cannot be asked for permission, and a skill file sits outside the workspace: allow it in `~/.gemini/antigravity-cli/settings.json` with `{"permissions": {"allow": ["read_file(C:/Users/<you>/.gemini/config/plugins/raizen-norms)"]}}`, or the run stops at the first skill it reads.
- `design-settle` needs there what it needs here: its Required companions installed for Antigravity, and a browser MCP server for every screenshot and browser check. Absent, it asks, as on Claude Code.

What differs from Claude Code:

| | Claude Code | Antigravity |
|---|---|---|
| Norms and documents | `SessionStart` | Injected before the first model call of a conversation, with the app's `CLAUDE.md` and a `HOST` block mapping the tool names |
| Where the norms run | Wherever the plugin is enabled | Every folder `agy` opens |
| A held push | `Run` on AskUserQuestion | `Run` on `ask_question` |

**Switching hosts mid-work.** When the working tree is dirty and the other host ran the last session in the repo, the session start prints a hand-over block: that session's last request, the answers the user gave, its todo list, the last it said — read from its transcript, so on the same machine only.

## Use

| Situation | Run |
|---|---|
| New app, empty directory | `/raizen-norms:app-settle`, then in the new repo `/raizen-norms:logic-settle` and `/raizen-norms:design-settle` |
| Running app | `/raizen-norms:app-settle` (writes the missing documents, or reworks them), then the other two |
| Only the look or the logic layer | `design-settle` or `logic-settle` alone |
| Repo that predates or drifted from these rules | `/raizen-norms:app-align` — the only skill that changes existing code, one finding per commit |

`design-settle` asks Fast or Full with its first question, on a new app and a redesign alike. Fast answers every design dialog with its recommendation in one block you cancel line by line; the frames, the pick, the gate and every check run as in Full. `/raizen-norms:design-settle fast` skips the question.

`build-flow` needs no command; it loads in every app session.

## Maintaining app repos

An app started before the `docs/` form keeps its root `PRD.md` and `QUEUE.md`; it is never migrated, and every skill reads it through `docs-format`'s legacy map.

An older app's `CLAUDE.md` may still carry a norm that has since moved into the plugin. The `SessionStart` hook names these sections; delete them:

- the git paragraph under *Before touching anything*
- the `GIT` block under *Closing a session*
- the *Pointers* table
- the *Scope* section
- the closing report (*Report per scope item…* and the `PRD` block)
- *Read `PRD.md` at the start of a session*

Retiring another section → add its phrase to `STALE` in `scripts/session_norms.py` and a line here.

An app with a project-scoped `.mcp.json` shadows the user-scope Supabase server: delete the file, commit, restart.

## Not yet verified

- The UI and logic lint floors and the rule tests have never been written in a real app.
- The `docs/` form has never been bootstrapped in a real app.
- Whether a cloud session installs this marketplace; until then, cloud sessions do frontend work only.
- The account-wide Supabase MCP endpoint end to end: its first-use login, and `project_id` as `guard_project_ref.py` expects.
- On Antigravity: `agy plugin install` from this repo's URL — proven from a folder, and by URL on another plugin. The four settle skills were read by a session there and none has been run — their interviews, their subagents, `design-settle` with its companions and a browser MCP server installed; the IDE and Antigravity 2.0. Gemini CLI is not ported.
