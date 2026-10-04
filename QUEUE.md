# QUEUE — toolkit work not done yet

- Antigravity, global registration: prove that `~/.gemini/config/plugins.json` loads both plugins before a conversation starts in an interactive `agy` session, then delete its line from README's *Not yet verified*. The user declined that file on their own machine on 2026-10-04 — ask before writing it.
- Antigravity, held push: capture the line `ask_question` records for a picked option and make `approved_antigravity` in `guard_git.py` read it. Prove it against a bare local remote named by absolute path in the prompt, never against a real one.
- Antigravity, `raizen-hub`: run each settle skill there once and record what breaks — the interviews through `ask_question`, the subagents, `design-settle`'s browser steps and its required companions.
- Gemini CLI: not ported. Its hook events are `BeforeTool` and `SessionStart` and its manifest is `gemini-extension.json`; install it and probe the payloads before writing anything.
- Antigravity IDE and 2.0: not run. Plugin-bundled hooks are documented for the CLI only; there the hooks belong in a `hooks.json` of the workspace or the global config.
