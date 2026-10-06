# QUEUE — toolkit work not done yet

- How the lines below were observed, 2026-10-06: headless `claude -p` sessions on Claude Code 2.1.289 in throwaway clones of three apps and in one empty directory — the plugin loaded from this repo by `--plugin-dir`, no MCP server, no web search, no remote but a bare local one, no database, the user's other hooks running — on Sonnet unless a line says Opus. No session ran on the interactive host, and none on Antigravity.

## Decisions owed

- A block a skill orders in the middle of a run, under another plugin's brevity hook: with the `ASKING` line of 0.84.0, two migrate sessions and one document session printed neither Step 0's block nor M1's `MIGRATE` block. A longer wording of the line — `between tool calls too` — changed nothing in the second migrate and was dropped. All three printed their closing block whole, where the session before the line closed in bullets; and a bootstrap and a `logic-settle` session printed Step 0's block, which ended their turn. Owed: whether a block is left to arrive only where a turn ends, or Step 0 ends the turn in every mode.

## Open

- `design-settle`, on a Keep: the component-token table has no measured source, so `build-flow` opens pages from a table marked `[needs verification]`.

## Needs a session this repo cannot run

- `design-settle`, live: never run since the restructure of 0.68.0, and its rules of 0.83.4 with it. It needs a browser and the user's picks on screen.
- A real app, with its database: migrate, align's band 2 and C3, `logic-settle` past its install block, database steps arriving as one command, a `docs/changelog.md` entry from a build session, `build-flow`'s audit by pick and its six-case walk in a subagent.
- The interactive host: every question observed here arrived as chat, never as a dialog; a push there; and `.claude/settings.json`, which a headless session is refused and so never wrote.
- Antigravity: `design-settle`'s `Material loaded:` line is self-reported, and the one run there listed a file its transcript shows it never read.
