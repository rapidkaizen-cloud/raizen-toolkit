# templates/

Copied by `app-settle` bootstrap mode into a new app repo. `{{...}}` placeholders are filled from the interview answers.

**Two files, and deliberately only two** — `CLAUDE.md.tpl` and `.claude/settings.json`. Both are true of every repo under these plugins whatever it runs on, which is the whole test for belonging here.

Nothing for a platform is scaffolded: no hosting config, no CI workflow, no database config. Those were removed rather than left inert. A template for one vendor is a recommendation nobody voted for — the file sits in the repo, the interview reads it as the settled answer, and the choice is made before the question is asked. What each stack needs is named in `stack-questions.md` and written by the session that chose it.

Nothing here is a secret, and nothing here is a placeholder *for* a secret. This repo is private, but what it copies lands in app repos that may not be, so a template that asks for a token is a template that eventually gets committed with one in it.

## Supabase MCP — user scope, not a repo file

Only where the database chosen at Question 6 is Supabase. No `.mcp.json` is scaffolded for it or for anything else: the server is connected once per machine, user scope, and then covers every app repo.

```
claude mcp add -s user --transport http supabase "https://mcp.supabase.com/mcp"
```

The URL must stay bare: Supabase's OAuth rejects any query string (`resource: Resource must be a valid MCP endpoint`), so `?features=` or `?project_ref=` breaks the login itself.

Access is granted by a browser login on first use — once per account, not per project. Which project a session may touch is not decided by the server config: `supabase/config.toml` in the app repo declares that repo's project, and the `guard_project_ref` hook in `raizen-norms` blocks any Supabase MCP call aimed at a different one. That file is **written by `app-settle`, not copied from here** — it is one line, and a one-line template is a vendor choice disguised as a convenience. The pin covers MCP calls only — the `supabase` CLI and raw HTTP are outside it.
