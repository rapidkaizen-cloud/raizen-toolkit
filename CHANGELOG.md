# Changelog

All notable changes to the `raizen-norms` plugin, and to `raizen-hub` until 0.70.0 merged it in, newest first. The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/). Versions before these are in `git log`.

## [raizen-norms 0.77.0] - 2026-10-05

### Added

- `norms-help`: one card holding the version number, the commands of `README.md`'s `Use` section, the pages `docs/README.md` lists, and the newest changelog entry. A question asked with it is answered from the page that covers it, and the file is named. `scripts/norms_help.py` prints each part as its file holds it, so the card cannot disagree with them.
- `docs/guide/help.md`: what the card holds and where each part comes from.

### Removed

- `norms-version`, with its comparison against origin and the update it offered. The version is now its number and one changelog entry. A machine with `autoUpdate` on gets a new version at its next start; `README.md` holds the update under `Update`.

To act on:

- A note or a habit naming `/raizen-norms:norms-version`: the command is `/raizen-norms:norms-help`.

## [raizen-norms 0.76.1] - 2026-10-05

### Fixed

Both found by running 0.76.0 on Antigravity, before any of it was published:

- The document reminder, on Antigravity: a conversation opened within minutes of another one's commit was asked about that commit, and spent thirty steps on it. It is asked only after its own last tool call ran a `git commit`.
- `guard_git`: a command named inside a sentence counted as put to the user, so a closing report saying what it pushed turned the next thing typed into a reply that let one more push through. The command counts only backticked on a line of its own, or alone in a fence; the session norms and the held message say so.

Nothing to act on in an installed app.

## [raizen-norms 0.76.0] - 2026-10-05

### Added

- A document reminder: after a commit that touched no document, in a repo with `docs/PRD.md` or a root `PRD.md`, the session is asked whether a sentence in a document became false, whether a page became usable with no guide page, and whether users will notice. It writes the document into that commit or reports `Docs: none`. `scripts/remind_docs.py` never blocks a commit, and is silent in a repo that keeps no documents. On Claude Code it comes with the result of the `git commit`; on Antigravity, where no hook speaks after a tool, the session-start script hands it over before the next model call, once per commit.

### Changed

- `docs-format` and `build-flow`: `docs/whats-new.md` gets an entry for every commit users will notice, with or without an in-app help page. It was written only where the app had one, which left an app without a help page with no record of change but `git log`.

To act on:

- An app on the `docs/` form with no help page: `docs/whats-new.md` is written from the next commit users notice. Nothing is owed for commits already made.

## [raizen-norms 0.75.0] - 2026-10-05

### Added

- Session start: a repo with no PRD in either form gets `docs/queue.md` printed where it keeps its queue there, as it gets a root `QUEUE.md`.
- `docs/` in the plugin's own repo, written for the people who install it. `docs/guide/gates.md` says what the publishing stop and the destructive gate show, what each waits for, and what its hook checks and does not. The toolkit's own queue moved to `docs/queue.md`.

Nothing to act on in an installed app.

## [raizen-norms 0.74.0] - 2026-10-05

### Changed

- Session norms, `GIT`, and `guard_git`: a push, `gh pr create` and `gh pr merge` are a chat stop, on Claude Code and Antigravity alike. The session ends its turn on a message naming the exact command in backticks, with the commits it publishes under it, and runs the command once when the reply typed in chat is a clear yes, in whatever words. A question, a condition or another instruction is not one.
- `guard_git` enforces the stop, not the yes: the command is held until the session's last message names it and the user has typed a reply to that message, with nothing typed since. One reply covers one run. Reading the reply is the session's.

### Removed

- `guard_git`: `Run` picked on an AskUserQuestion, or on `ask_question`, no longer lets a held command through — a dialog gets clicked before it is read.

To act on:

- Nothing in an installed app's files. At the next held push or pull request, answer in chat where `Run` used to be picked.

## [raizen-norms 0.73.0] - 2026-10-05

### Added

- `norms-version`: reports the version of the copy the session runs, the date it was released and the time it reached the machine, whether origin holds a newer one, and its changelog entry — with every entry the machine lacks when it is behind. `scripts/norms_version.py` does the reading: origin is its changelog, fetched over HTTPS from the public repo, and a machine that cannot reach it still gets its own lines. Behind, on Claude Code, it asks whether to update now and runs the `README.md` commands on `Update`; on Antigravity it reports only.

Nothing to act on in an installed app.

## [raizen-norms 0.72.2] - 2026-10-05

### Changed

`app-settle`'s migrate mode, corrected from two runs on copies of legacy apps:

- A block of `CLAUDE.md` telling a session how to write, keep, or format the PRD is deleted and named in the close block. Left standing, it ordered the next session to write a root `PRD.md` back.
- A Section 3 list item keeps its whole text under its topic. Its topic is the opening words a rule test already quotes, else its bold lead-in, else its opening words up to the first punctuation mark. A paragraph is never a topic.
- Everything inside the six sections moves: a part its shape has no heading for stays under its own label, and only text outside the sections is left in `docs/PRD.md` alone.
- `DESIGN.md` gets no `## Contrast`, its sections follow the format's order, and the five token groups it marks `omitted` are named.
- The rule-test check, the session-start check, the frozen line and the files that name the old form are each stated one way.

Also:

- Session start, the stale-path note: a backticked token with no letter in it — a document number, a fraction — is no longer read as a path.

To act on:

- An app repo migrated under 0.72.0 or 0.72.1: read its `CLAUDE.md` for a block that still tells sessions to maintain `PRD.md`, and delete it.

## [raizen-norms 0.72.1] - 2026-10-05

### Changed

- `design-settle`, the frames: the session prints `Material loaded:` with the path of every file it read before the first frame, and names the detector command and its hit count in each round's report — `detector not run` and why where it did not. A full run on Antigravity drew frames and a canvas having read no `impeccable` or `frontend-design` file and run no detector, and nothing in its output showed it.
- The Antigravity `HOST` block says what loading a skill means there: read its `SKILL.md`, then the files it names.
- The Antigravity `HOST` block sends a session to Claude Code's own copy of `frontend-design` where one exists: no installer puts that skill on Antigravity, and a linked folder is not listed there. The copy follows Claude Code's updates; a machine without Claude Code copies the folder.

Nothing to act on in an installed app. On Antigravity, uninstall and install again to get it; a headless run there also allows `read_file` on Claude Code's `frontend-design` folder.

## [raizen-norms 0.72.0] - 2026-10-05

### Added

- `app-settle`, migrate mode: a repo with a root `PRD.md` is moved to the `docs/` form in one commit — `PRD.md` to a frozen `docs/PRD.md`, `QUEUE.md` to `docs/queue.md`, its sections copied word for word into `docs/product.md`, `docs/rules.md`, `docs/glossary.md` and `docs/decisions/`, a ratified Section 5 converted into `DESIGN.md` with no value changed. It runs before align or rework, and a repo that cannot move mechanically stays legacy for that run.
- `app-settle`, align mode: the audit, the ranked table and the one-finding-per-commit fixes that were `app-align`.

### Changed

- `app-settle` has five modes — bootstrap, document, migrate, align, rework — and Step 0 decides which from the directory and the code. With documents in place it audits for align unless the user asks for a change, which is rework. Each mode is decision work or mechanical work, never both.
- `app-settle` commits what a mode wrote, by the norms' `GIT` block. Bootstrap makes the first commit on `main`, then creates `development` and switches to it.
- `app-settle` Step 0: on `main` with no `development` branch it offers to create one; migrate and align stop on a dirty working tree.
- `docs-format`: a root `PRD.md` is the legacy form until `app-settle` migrates it, and `DESIGN.md` has one writer besides `design-settle` — that conversion.
- Align corrects a document only where it states what exists and the code shows otherwise; a mismatch about what ought to be is left for rework.

### Removed

- The skill `app-align`. `/raizen-norms:app-align` no longer exists; run `/raizen-norms:app-settle`.

To act on:

- An app repo whose `CLAUDE.md` or `AGENTS.md` names `app-align`: the next align run counts it under C2 and corrects it.
- An app repo with a root `PRD.md`: the next `app-settle` run there migrates it. Migrate has not run in a real app — try it on a copy first.

## [raizen-norms 0.71.0] - 2026-10-05

### Changed

- Session norms: a repo with neither a root `PRD.md` nor `docs/PRD.md` gets a shorter block. `POINTERS` and `CLOSING THE SESSION` are cut, and a `NOT SETTLED` section stands in their place: `build-flow` and `docs-format` do not apply there, `ui-build`, `db-ops` and `logic-build` hold except where a rule reads `docs/` or `DESIGN.md`, and in an app repo the session says once that `app-settle` has not run.
- `ui-build`: the `DESIGN.md` gate does not bind a repo marked `NOT SETTLED`. UI there is built only from the components and tokens the repo already has, with no new styling value.
- `guard_git`: a commit on `main` is refused only where the repo has a `development` branch, local or on `origin`. The `GIT` block of the norms says the same.
- `app-settle`, `logic-settle`, `app-align`: the stop on branch `main` gives the rule as its reason, no longer the guard.

To act on:

- An app repo with a PRD in either form: nothing — its session start and its gates are unchanged.
- An app repo with only `main`: sessions now commit there. Create `development` to get the refusal back.

## [raizen-norms 0.70.0] - 2026-10-05

### Changed

- One plugin instead of two: `raizen-hub` is merged into `raizen-norms`, which holds all nine skills, the session norms and the guards. The version continues above both — 0.70.0 follows `raizen-hub` 0.69.0 and `raizen-norms` 0.37.1.
- The plugin is the repo root: `skills/`, `scripts/`, `hooks/` and both manifests moved up from `plugins/raizen-norms/`, so Antigravity installs it from the repo URL with `agy plugin install`.
- The four settle skills are invoked as `/raizen-norms:app-settle`, `/raizen-norms:logic-settle`, `/raizen-norms:design-settle` and `/raizen-norms:app-align`.
- `design-settle` Step 0 and `app-align` print one plugin version.

### Removed

- The plugin `raizen-hub`. The marketplace's `renames` map sends the name to `raizen-norms`, so Claude Code moves an enabled `raizen-hub@raizen` onto it.
- The `plugins/` folder.

To act on:

- An app repo: nothing — its `enabledPlugins` line names `raizen-norms@raizen` already.
- A Claude Code machine: after the update, `/plugin` lists `raizen-norms` and no `raizen-hub`. Where `raizen-hub` is still listed, uninstall it — its copy of the four skills is stale. A machine that enabled only `raizen-hub` now runs the norms and the guards in every folder.
- An Antigravity machine: a `~/.gemini/config/plugins.json` entry naming `…/raizen/plugins` resolves to nothing once that clone updates, and every session there runs without norms or guards. Remove the entry and install as the README's Antigravity section says.

## [raizen-norms 0.37.1] - 2026-10-04

### Changed

- `build-flow`: commit timing follows the session norms' `GIT` block everywhere. Section 9 no longer says the commit is never made mid-session, and the audit is no longer offered before anything is committed — a finished page is committed when it is finished, and an audit fix is its own commit.
- `build-flow` Section 9: no longer says bootstrap wrote no host config and no CI workflow; `app-settle` N5 writes a rewrite rule for a static SPA, and a CI workflow when the user asks for one.
- `ui-build`: the `bulk` fixture case is 500+ rows, the number `build-flow`'s `references/contract.md` gives.

Nothing to act on in an installed app.

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
