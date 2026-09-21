# raizen-toolkit

Private repo (`rapidkaizen-cloud/raizen-toolkit`) holding two Claude Code plugins and the marketplace `raizen`.

| Plugin | Holds | Loaded |
|---|---|---|
| `raizen-hub` | `app-settle`, `logic-settle`, `design-settle`, `app-conform` | When invoked |
| `raizen-norms` | `build-flow`, `prd-format`, `ui-build`, `db-ops`, `logic-build`, guard hooks | Every session in an app repo whose `.claude/settings.json` enables it — `app-settle` writes that line |

## Install

Needs Claude Code, `python3` (every `raizen-norms` hook calls it; with only `python` the guards silently never run), Node.js, and `gh` logged in to an account with **Read** access — another account is added as a collaborator.

```
/plugin marketplace add rapidkaizen-cloud/raizen-toolkit
/plugin install raizen-hub@raizen
/plugin install raizen-norms@raizen
```

- Install at **user scope** only; a project-scope entry updates separately and falls behind.
- In `~/.claude/settings.json`, set `"autoUpdate": false` on `raizen` under `extraKnownMarketplaces` — background auto-update cannot log in to a private repo.
- Restart Claude Code.

Required alongside: `impeccable` (`npx impeccable install`) and `frontend-design` (`/plugin`). A session missing either asks before continuing. Invoke `/design-settle` by name, since `impeccable`'s description overlaps it.

Recommended: `npx skills add supabase/agent-skills` (Postgres guidance for `db-ops`) and `ponytail`. Do not install the `supabase` plugin — it adds a second Supabase MCP server. Connect the Supabase MCP once at user scope, with no query parameters in its URL.

Check: `/plugin` lists both plugins; design-settle's Step 0 prints the running build as `Skill build`.

## Update

Every commit that changes a plugin bumps its version (`.githooks/pre-commit` refuses otherwise — run `git config core.hooksPath .githooks` once per clone). After the push, on every machine:

```
claude plugin marketplace update raizen
claude plugin update raizen-hub@raizen
claude plugin update raizen-norms@raizen
```

Then restart. Nothing reaches a session before this.

## Use

| Situation | Run |
|---|---|
| New app, empty directory | `/raizen-hub:app-settle`, then in the new repo `/raizen-hub:logic-settle` and `/raizen-hub:design-settle` |
| Running app | `/raizen-hub:app-settle` (writes the missing PRD, or reworks it), then the other two |
| Only the look or the logic layer | `design-settle` or `logic-settle` alone |
| Repo that predates or drifted from these rules | `/raizen-hub:app-conform` — the only skill that changes existing code, one finding per commit |

`build-flow` needs no command; it loads in every app session.

## Maintaining app repos

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

- Hooks firing in a real session (`${CLAUDE_PLUGIN_ROOT}` expansion, `PreToolUse` matching): try `git add -A` once in a fresh app repo and confirm the refusal.
- The UI and logic lint floors and the Section 3 rule tests have never been written in a real app.
- Whether a cloud session can read this private marketplace; until then, cloud sessions do frontend work only.
- The account-wide Supabase MCP endpoint end to end: its first-use login, and `project_id` as `guard_project_ref.py` expects.
