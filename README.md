# raizen-toolkit

One plugin, `raizen-norms`, and the marketplace `raizen`, in the public repo `rapidkaizen-cloud/raizen-toolkit`. The repo root is the plugin, for Claude Code and for Antigravity — see [Antigravity](#antigravity).

| Holds | Loaded |
|---|---|
| `app-settle`, `logic-settle`, `design-settle` | When invoked |
| `build-flow`, `docs-format`, `ui-build`, `db-ops`, `logic-build` | By their descriptions |
| `norms-version` | When asked what version runs, whether it is current, or what changed |
| Session norms, guard hooks | Every session where the plugin is enabled — installed at user scope, every folder on that machine; `app-settle` writes the `enabledPlugins` line into each app repo. A repo with no PRD in either form gets the norms in their `NOT SETTLED` form: no document gate, UI only from what the repo already has |

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

Check: `/plugin` lists `raizen-norms`; design-settle's Step 0 prints the running build as `Skill build`; `norms-version` prints it in any session, with whether origin holds a newer one, and offers the update where it is behind.

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

**Proven on the CLI** — `agy` 1.2.16, Windows, headless, installed from this repo's URL with `agy plugin install`: the nine skills are listed, `hooks.json` is kept as written, the norms and the `HOST` block are injected, `git add -A` is refused, and a push is held. The copy lands in `~/.gemini/config/plugins/raizen-norms`. `design-settle` ran there end to end at 0.70.0, Fast, on a new app with no UI, one question per headless turn: the Step 0 block, the reference search, `ui-ux-pro-max`'s generator, the install gate, frames and canvas with browser screenshots at both widths, `DESIGN.md`, the decision records, promotion, verification, and a commit with named paths. That run read no `impeccable` or `frontend-design` file and ran no detector; a run at 0.72.1 read `impeccable`'s craft floor and operational register and `frontend-design` before the first frame, and ran the detector in every round. Proven before 0.70.0 only, registered by path: an interactive session, the hand-over block.

- Install it for the machine as above, never through a repo's `.agents/plugins.json`: registered per folder, the plugin loaded a minute after an interactive conversation began, and that conversation ran unguarded.
- Never run `agy plugin import` on this plugin: it replaces `hooks.json` with Claude Code's, which Antigravity cannot parse, and every guard goes silent.
- `python3` must resolve: there a hook that cannot start blocks every command.
- A headless run (`agy -p`) cannot be asked for permission, and a skill file sits outside the workspace: allow it in `~/.gemini/antigravity-cli/settings.json` with `{"permissions": {"allow": ["read_file(C:/Users/<you>/.gemini/config/plugins/raizen-norms)"]}}`, or the run stops at the first skill it reads.
- `design-settle` needs there what it needs here: its Required companions and a browser MCP server for every screenshot and browser check. Absent, it asks, as on Claude Code.
- A companion skill is found only as a folder under `~/.gemini/config/skills/`: copy each one there. Under `~/.gemini/antigravity-cli/skills/`, or as a link to a folder elsewhere, it is never listed.
- `frontend-design` needs no copy on a machine with Claude Code: the `HOST` block sends the session to Claude Code's own copy, so it is as current as Claude Code keeps it. On a machine without Claude Code, copy its folder like the others.
- A headless `design-settle` run needs these allowed, or the turn ends with no output at the first one missing: `read_file` on the plugin, the skills folder, Claude Code's `frontend-design` folder and the repo, `write_file` on the repo, `command(*)` — `command(git)` does not cover `git status` — `read_url(*)`, `mcp(<browser server>/*)`, and `execute_url(*)` for the browser to open a page. Refuse what must never run through `deny`, which does not end the turn.
- A dev server started in a headless turn dies when the turn ends; continue the conversation with `--conversation <id>`.

What differs from Claude Code:

| | Claude Code | Antigravity |
|---|---|---|
| Norms and documents | `SessionStart` | Injected before the first model call of a conversation, with the app's `CLAUDE.md` and a `HOST` block mapping the tool names |
| Where the norms run | Wherever the plugin is enabled | Every folder `agy` opens |

A held push or pull request runs the same way on both: the session ends its turn on the command and its commits, and runs it once when the reply typed in chat is a yes. The guard holds the command until that reply exists; reading it as a yes is the session's.

**Switching hosts mid-work.** When the working tree is dirty and the other host ran the last session in the repo, the session start prints a hand-over block: that session's last request, the answers the user gave, its todo list, the last it said — read from its transcript, so on the same machine only.

## Use

| Situation | Run |
|---|---|
| New app, empty directory | `/raizen-norms:app-settle`, then in the new repo `/raizen-norms:logic-settle` and `/raizen-norms:design-settle` |
| Running app | `/raizen-norms:app-settle` — it reads the repo and runs the one mode it owes next: documents it, migrates a root `PRD.md` to `docs/`, then audits the code against the rules and fixes what you pick, one finding per commit. Ask it for a change and it reworks the decisions instead. Then the other two |
| Only the look or the logic layer | `design-settle` or `logic-settle` alone |

`design-settle` asks Fast or Full with its first question, on a new app and a redesign alike. Fast answers every design dialog with its recommendation in one block you cancel line by line; the frames, the pick, the gate and every check run as in Full. `/raizen-norms:design-settle fast` skips the question.

`build-flow` needs no command; it loads in every app session.

## Maintaining app repos

An app started before the `docs/` form keeps its root `PRD.md` and `QUEUE.md` until `app-settle` runs in it and migrates them, in one commit; until then every skill reads it through `docs-format`'s legacy map.

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
- `app-settle`'s migrate mode and its align mode have never run in an app. Run migrate on a copy of a legacy app before a real one.
- Whether a cloud session installs this marketplace; until then, cloud sessions do frontend work only.
- The account-wide Supabase MCP endpoint end to end: its first-use login, and `project_id` as `guard_project_ref.py` expects.
- A held push passing on a chat reply (0.74.0): replayed against one real Claude Code transcript, never run in a session on either host, and no session has been seen to read a no, a question or a condition as anything but a yes. On Antigravity the reply is read in the step shape the hand-over block already reads; a push passed there before 0.74.0 only, on `Run` picked in `ask_question`.
- On Antigravity: `design-settle` in Full and where UI exists — its audit subagent, its gate; `app-settle` and `logic-settle`; a question asked through `ask_question` in an interactive session; the IDE and Antigravity 2.0. Gemini CLI is not ported.
