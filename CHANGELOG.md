# Changelog

All notable changes to the `raizen-hub` and `raizen-norms` plugins, newest first. The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/). Versions before these are in `git log`.

## [raizen-norms 0.35.1] - 2026-10-04

### Changed

- Session norms, `HOST - Antigravity`: three lines an Antigravity session got wrong without them — the guards run there as hooks it cannot see, the installed plugins are the folders the skills are read from, and a `claude mcp add` line means the same server in `~/.gemini/config/mcp_config.json`.

## [raizen-norms 0.35.0] - 2026-10-04

### Added

- Antigravity support: `plugin.json` and `hooks.json` at the plugin root, read by `agy`. The same guards run before `run_command` and `call_mcp_tool`, and the norms are injected before the first model call of a conversation, with the app's `CLAUDE.md` and a `HOST` block mapping Claude Code's tool names. Proven on `agy` 1.2.16 — README, Antigravity, holds the registration and what is not yet verified.
- `scripts/host.py`: hands every hook one payload shape on either host.
- Hand-over block at session start: when the working tree is dirty and the other host ran the last session in the repo, the norms end with that session's last request, the user's answers, its todo list and its last messages, read from its transcript on the same machine.

### Changed

- `guard_git`: on Antigravity a held command passes on `Run` answered to `ask_question`, and the held message names the host's own question tool.
- `guard_project_ref`: a crash passes the call on every host.
- Hook payloads are decoded as UTF-8 whatever the console codepage.

## [raizen-hub 0.67.0] - 2026-10-04

### Added

- Antigravity support: `plugin.json` at the plugin root, so `agy` loads the four skills.

### Changed

- `app-settle`, the shape of `AGENTS.md`: Antigravity loads that file and is handed the norms too; the norms' `HOST` block says which holds.

## [raizen-norms 0.34.0] - 2026-10-02

### Changed

- Session norms, `GIT`, and the `guard_git` held message: the commits under a push or pull-request command are `- ` bullets, one per commit, and the question offers exactly two options, `Run` and `Cancel`.

## [raizen-norms 0.33.0] - 2026-10-02

### Changed

- Session norms, `GIT`: the AskUserQuestion that asks for a push or a pull request lists every commit the command publishes under it, one line each: short hash and subject.
- `guard_git`: the held message asks for that list.

## [raizen-hub 0.66.0] - 2026-09-29

### Removed

- The bundled Playwright MCP server pinned to WebKit, with every WebKit capture in `design-settle`: the `Design material` row, the ask when it is absent, and the Judging and verify lines. Screenshots use Chrome DevTools only. The WebKit browser a machine installed for it is no longer used and may be deleted.

## [raizen-norms 0.32.0] - 2026-09-29

### Added

- Session norms, `ASKING`: a decision that is the user's is asked through AskUserQuestion, or in chat at a hard stop, and the session runs it. The user is never handed a command to type, only what needs their own hands: a browser login, a dashboard, a key rotation, a payment.

### Changed

- `guard_git`: a push (`--force-with-lease` included), `gh pr create`, and `gh pr merge` run once the user picks `Run` on an AskUserQuestion that names the exact command; one answer covers one run. The permission prompt is gone, because an SDK host never showed it.
- `guard_git`: a bare force push (`--force`, `-f`, `+branch`) is refused with a pointer to `--force-with-lease`.
- Session norms: a session behind `origin/development` asks to run `git pull --ff-only` instead of telling the user to run it.

### Fixed

- `guard_git`: a command mentioned inside a commit message, a heredoc, or a quoted string is no longer read as a call, so a message naming `git add -A` or `gh pr create` commits.

## [raizen-hub 0.65.0, raizen-norms 0.31.0] - 2026-09-28

### Changed

- `ui-ux-pro-max` is Required, level with `impeccable`: a session without it asks before continuing.
- `ui-build`: where both skills set a UX floor, the stricter one applies; any other contradiction is reported to the user; `DESIGN.md` outranks both.
- `design-settle`: style, colour, and typography search runs once per frame, with that frame's direction as the query.
- `design-settle`: every frame and canvas round meets the UX floor. Step 8 checks Critical and High don'ts per interaction on every promoted page; Step 9 reports any left standing.

### Removed

- `design-settle`: the pure frame, its draw question, and the rule that one frame is drawn without `ui-ux-pro-max`.
