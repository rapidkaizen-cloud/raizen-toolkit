# templates/

Copied by `app-init` into a new app repo. `{{...}}` placeholders are filled from the interview answers.

Nothing here is a secret, and nothing here is a placeholder *for* a secret. The only value filled in is `{{SUPABASE_PROJECT_REF}}`, an identifier that lands in `supabase/config.toml` — Supabase access is granted by a browser login, and the CI database URLs live in GitHub secrets. This repo is private, but what it copies lands in app repos that may not be, so a template that asks for a token is a template that eventually gets committed with one in it.

## Supabase MCP — user scope, not a repo file

No `.mcp.json` is scaffolded. The Supabase MCP server is connected once per machine, user scope, and then covers every app repo:

```
claude mcp add -s user --transport http supabase "https://mcp.supabase.com/mcp"
```

The URL must stay bare: Supabase's OAuth rejects any query string (`resource: Resource must be a valid MCP endpoint`), so `?features=` or `?project_ref=` breaks the login itself.

Access is granted by a browser login on first use — once per account, not per project. Which project a session may touch is not decided by the server config: `supabase/config.toml` declares the repo's own project, and the `guard_project_ref` hook in `raizen-norms` blocks any Supabase MCP call aimed at a different one. The pin covers MCP calls only — the `supabase` CLI and raw HTTP are outside it.
