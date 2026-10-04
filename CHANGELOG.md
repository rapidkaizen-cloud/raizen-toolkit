# Changelog

All notable changes to the `raizen-hub` and `raizen-norms` plugins, newest first. The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/). Versions before these are in `git log`.

## [raizen-hub 0.69.0] - 2026-10-04

### Changed

- `app-settle`, `logic-settle` and `app-align` are read one step at a time, as `design-settle` is since 0.68.0: `SKILL.md` keeps the cost rules, the hard limits and the first steps, and names per later step the file to read on arrival. Step and question numbers and the finding codes C1 to C7 are unchanged. Every `description` is shorter.
- `app-settle`: `SKILL.md` is a quarter of its size. Document mode is `references/document.md`, rework `references/rework.md`, N5 and N6 `references/scaffold.md`, the Pioneer path `references/pioneer.md`. The repo read of D1 and R1 runs in a subagent briefed with `references/repo-read.md`.
- `logic-settle`: Steps 3 to 8 are `references/interview.md`, `install.md`, `pass.md` and `floor.md`; each need of the rubric is its own `references/need-*.md`, read only when that need is asked. The audit runs in a subagent briefed with `references/audit.md`.
- `app-align`: the audit runs in a subagent briefed with `references/audit.md`.
- All three: a subagent doing an audit or a live verification runs on a cheaper model than the session's. Only a question's recommendation is verified before it is asked; another option is marked `unverified` and verified when picked.

### Removed

- `app-settle`, N6: the sentence that the toolkit writes no hosting or CI file at bootstrap, which the N5 table contradicted. The table stands; the session still never raises hosting, production env or CI.

Nothing to act on in an installed app.

## [raizen-norms 0.37.0] - 2026-10-04

### Changed

- All five skills are shorter to load, with the same rules: each states a rule once, drops the sentences that argued for it, and opens with the cost rules — independent reads and commands in one turn, nothing the session start printed re-read. Section numbers and names are unchanged. Every `description` is shorter.
- `build-flow`: `SKILL.md` is half its size. Section 3 — the three routes of a new queue, the change record, the UI and backend split — and the two queue file templates are `references/new-queue.md`, read when `docs/queue.md` is absent or just emptied or the user asks for something outside it. The rule test before wiring, the wiring rules and canvas-file retirement are `references/backend.md`, read by a backend batch or an app that never split. The audit pass is `references/audit.md`, read when the user accepts it. The wiring rules were in two places and are now in one, which a backend batch reads.
- `ui-build`: the craft material is one table naming what to read before which edit. The voice of a first-visit page group is `references/first-visit.md`.
- `logic-build`: the rule-test table per enforcement point and the no-test-runner procedure are `references/rule-test.md`; Section 10 keeps the rules.
- `docs-format`: the legacy map is in `references/legacy.md`, read at once in a repo with a root `PRD.md`.

Nothing to act on in an installed app.

## [raizen-hub 0.68.0] - 2026-10-04

### Changed

- `design-settle` is read one step at a time. `SKILL.md` keeps the switches, the hard limits, Fast or Full and Steps 0 to 2; each later step is a file read when the flow reaches it — `references/interview.md` (Steps 3 and 4), `frames.md` and `canvas.md` (Step 5), `ratify.md` and, where UI exists, `gate.md` (Step 6), `pass.md` (Step 7), `verify.md` (Steps 8 and 9). The audit is `references/audit.md`, read only by the subagent that runs it. Step numbers are unchanged.
- `design-settle`, cost rules: a step's independent reads, searches and commands run in one turn; the audit, the stack verification, the reference search, the platform research and Step 8's mechanical checks run in a subagent on a cheaper model than the session's; what the session start printed is not re-read.
- `design-settle`: `impeccable`, `frontend-design` and `review-animations` are loaded after the install gate, before the first frame, instead of before the reading.
- `design-settle`, the stack where UI exists: a library, styling, icon pack or engine the audit does not indict is one cancellable `Keep` line, not a dialog. On every repo only a dialog's recommendation is verified before it is asked; another option is marked `unverified` and verified when picked.
- `design-settle`: the `/design-system` route is written once, in the pass, instead of before the frames; the lint floor's rules moved with it to `pass.md`.
- `design-settle`: every frame's `ui-ux-pro-max` searches run in one command; its commands are taken by searching its `SKILL.md`, not by reading it whole.

Nothing to act on in an installed app.

## [raizen-norms 0.36.1] - 2026-10-04

### Changed

- `build-flow`: the pointer to `design-settle`'s product draft names its new file.

## [raizen-norms 0.36.0] - 2026-10-04

### Changed

- Session start, legacy `PRD.md` repos: the hook prints Sections 1, 2 and 6 only — context, roles, prohibitions, what `docs/product.md` holds in the other form. Sections 3, 4 and 5 are named with their line range and read from the file when a skill sends a session there. A `PRD.md` whose six numbered sections cannot be located is still printed whole. Nothing to act on in an installed app.

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
