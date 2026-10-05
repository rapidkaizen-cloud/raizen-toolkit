# guard-project-ref

Pins every Supabase MCP call to the project the repo itself declares, so a call cannot reach another project in the same account.

| | |
|---|---|
| Kind | Hook — runs by itself; it cannot ask, only pass, refuse, or print |
| Runs on Claude Code | `PreToolUse`, matcher `mcp__.*` |
| Runs on Antigravity | `PreToolUse`, matcher `call_mcp_tool` |
| Script | `scripts/guard_project_ref.py` |
| Self-check | `scripts/test_guard_project_ref.py` |

## What it does

The Supabase MCP server is connected to the whole account, so one login covers every app and any call can name any project through `project_id`. A repo declares its own project in `supabase/config.toml`: a top-level `project_id` whose value is exactly 20 lowercase letters or digits, the shape of a hosted project ref. The hook refuses a Supabase call aimed at a different project.

A call is judged when either holds:

- **The tool name contains `supabase`,** in any case. That covers `mcp__supabase__...` and `mcp__claude_ai_Supabase__...`. On Antigravity the name is built from the server and tool names.
- **The input has a SQL `query` next to a `project_id` or `project_ref`.** The server name is chosen by whoever connects it, so renaming the server does not turn the pin off for SQL calls.

The declaration is read from the project directory: the working directory on Claude Code, the first workspace folder on Antigravity.

## What it refuses or holds

| Case | What happens | What lets it through |
|---|---|---|
| A judged call whose `project_id` or `project_ref` differs from the declared ref | `REFUSED: this Supabase call targets project '<other>', but <path> declares project '<expected>'.` | A call to the declared project |
| A call carrying both keys, one equal to the declaration and one different | Refused: every key present must match | Both keys equal to the declared ref |

A ref padded with spaces is trimmed before the comparison.

The message tells the session to stop and ask you, not to retry with another ref and not to edit `project_id` itself. Re-pointing it re-pins every later call in the repo, which only you may decide.

## What it lets through

A hook that is too strict costs more than no hook, so these pass on purpose:

- **Another server's tools that carry a `project_id`.** No `supabase` in the name and no SQL `query` beside the id.
- **Supabase tools with no project argument,** such as `list_projects` and the docs search.
- **A repo that declares nothing.** No `supabase/config.toml`, a file that cannot be read, a placeholder in double braces that was never filled, or a `project_id` that is not 20 lowercase alphanumerics, such as the directory name the Supabase CLI writes.
- **A `project_id` under a `[section]`,** such as `[remotes.production]`. That is the section's ref, not the repo's. Only the part before the first section header is read.
- **A file that starts with a byte-order mark,** which PowerShell writes by default.
- **Input it cannot read.** Bad stdin, a tool input that is not an object, a config that is not UTF-8.

> [!NOTE]
> The hook fails open. A crash passes the call instead of blocking it. Antigravity blocks a call on any non-zero exit, a crash included, so the script exits 0 on any error.

## What it does not reach

- **The shell route.** The `supabase` CLI and `curl` are not covered; this hook reads MCP calls only.
- **A renamed server's non-SQL tool.** `mcp__db__get_logs` with a `project_id` is not judged, because the shape signal needs a `query` beside the id. The test locks this gap in.

## Related

- [guard-destructive](guard-destructive.md) — the other hook that reads MCP SQL
- [db-ops](db-ops.md) — the rules for touching the database
- [Hosts](../concepts/hosts.md) — what differs between Claude Code and Antigravity
