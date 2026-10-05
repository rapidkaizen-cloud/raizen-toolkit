# Run on Antigravity

The repo root is an Antigravity plugin too: install it once per machine, and every folder `agy` opens runs under the norms and the guards.

`plugin.json` and `hooks.json` at the root are its manifest and its hooks, beside Claude Code's `.claude-plugin/` and `hooks/`.

## Install

```
agy plugin install https://github.com/rapidkaizen-cloud/raizen-toolkit
```

The copy lands in `~/.gemini/config/plugins/raizen-norms`.

> [!WARNING]
> - **Install it for the machine, never through a repo's `.agents/plugins.json`.** Registered per folder, the plugin loaded a minute after an interactive conversation began, and that conversation ran unguarded.
> - **Never run `agy plugin import` on this plugin.** It replaces `hooks.json` with Claude Code's, which Antigravity cannot parse, and every guard goes silent.
> - **`python3` must resolve.** There, a hook that cannot start blocks every command.

## Update

```
agy plugin uninstall raizen-norms
agy plugin install https://github.com/rapidkaizen-cloud/raizen-toolkit
```

The install is a copy, and nothing refreshes it.

## Companion skills

- **A companion skill is found only as a folder under `~/.gemini/config/skills/`.** Copy each one there. Under `~/.gemini/antigravity-cli/skills/`, or as a link to a folder elsewhere, it is never listed.
- **`frontend-design` needs no copy on a machine with Claude Code.** The `HOST` block sends the session to Claude Code's own copy, so it is as current as Claude Code keeps it. On a machine without Claude Code, copy its folder like the others.
- **`design-settle` needs there what it needs on Claude Code**: its Required companions, and a browser MCP server for every screenshot and browser check. Absent, it asks.

## Headless runs

A headless run (`agy -p`) cannot be asked for permission, and a skill file sits outside the workspace.

1. **Allow the plugin folder to be read**, in `~/.gemini/antigravity-cli/settings.json`, or the run stops at the first skill it reads:

   ```json
   {"permissions": {"allow": ["read_file(C:/Users/<you>/.gemini/config/plugins/raizen-norms)"]}}
   ```

2. **For a headless `design-settle` run, allow all of these**, or the turn ends with no output at the first one missing:

   | Permission | On |
   |---|---|
   | `read_file` | The plugin, the skills folder, Claude Code's `frontend-design` folder, the repo |
   | `write_file` | The repo |
   | `command(*)` | Every command — `command(git)` does not cover `git status` |
   | `read_url(*)` | Every URL |
   | `mcp(<browser server>/*)` | The browser MCP server |
   | `execute_url(*)` | The browser opening a page |

3. **Refuse what must never run through `deny`**, which does not end the turn.
4. **Continue the conversation with `--conversation <id>`.** A dev server started in a headless turn dies when the turn ends.

## Related

- [Hosts](../concepts/hosts.md) — what differs from Claude Code, and switching hosts mid-work.
- [What is proven](../reference/status.md) — what has run for real on Antigravity.
