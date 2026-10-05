# Maintain app repos

What an app repo started under an older version still carries, and how to clear it.

## Old sections in an app's `CLAUDE.md`

An older app's `CLAUDE.md` may still carry a norm that has since moved into the plugin. The two then contradict each other silently, so the session start names every such section it finds. Delete them:

- the git paragraph under *Before touching anything*
- the `GIT` block under *Closing a session*
- the *Pointers* table
- the *Scope* section
- the closing report (*Report per scope item…* and the `PRD` block)
- *Read `PRD.md` at the start of a session*

Where the two disagree, the plugin's norms are the newer.

## A root `PRD.md`

An app started before the `docs/` form keeps its root `PRD.md` and `QUEUE.md` until `app-settle` runs in it and migrates them, in one commit. Until then every skill reads it through `docs-format`'s legacy map. See [Bring in an existing app](existing-app.md).

## A project-scoped `.mcp.json`

An app with a project-scoped `.mcp.json` shadows the user-scope Supabase server. Delete the file, commit, and restart.

## A plugin entry at project scope

A project-scope entry updates separately from the user-scope one and falls behind, so sessions in that repo can run an older version than the rest of the machine. [norms-help](../reference/norms-help.md) shows which version a session loaded. Install at user scope only.

## Retiring another section

When a section moves from the apps' `CLAUDE.md` into the plugin, add its distinctive phrase to `STALE` in `scripts/session_norms.py`, and a line to the list above.

## Related

- [session-start](../reference/session-start.md) — the notes a session start adds.
- [Update the plugin](update.md)
