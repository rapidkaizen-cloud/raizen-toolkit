# What is proven

What has run for real, on which host, and what has not. A line under "Not yet verified" is behaviour the skills describe that nobody has watched happen.

## Proven on Claude Code

- **`design-settle`'s interview** has been simulated on an existing-UI scenario with a legacy `PRD.md`, in Full, and every decision landed.
- **`app-settle`'s migrate mode** ran twice on copies of two legacy apps, by a session that read only the skill: every sentence of the PRD's six sections arrived word for word, `DESIGN.md` linted clean, one commit each.
- **A session building a new page** ran every step on Opus at 0.87.0, in a copy of a settled app with no sign-in: `build-flow`'s todo list, its proposal with both lists and its audit offer, and all of `ui-build`'s craft material read before the page.
- **`design-settle`'s verification and close** ran on Opus at 0.87.0, on a copy of a finished run with no UI, rewound to before its close commit: the checks in a subagent with a browser, the motion read against `review-animations`, the raw values, the detector's hit, the lint floor and the fixtures' numbers fixed and checked again, `docs/queue.md` written with a line per page still on fixtures, and one commit.

## Proven on Antigravity

On the CLI — `agy` 1.2.16, Windows, headless, installed from this repo's URL with `agy plugin install`:

- The nine skills are listed, `hooks.json` is kept as written, the norms and the `HOST` block are injected, `git add -A` is refused, and a push is held.
- `design-settle` ran end to end at 0.70.0, Fast, on a new app with no UI, one question per headless turn: the Step 0 block, the reference search, `ui-ux-pro-max`'s generator, the install gate, frames and canvas with browser screenshots at both widths, `DESIGN.md`, the decision records, promotion, verification, and a commit with named paths.
- That run read no `impeccable` or `frontend-design` file and ran no detector. A run at 0.72.1 read `impeccable`'s craft floor and operational register and `frontend-design` before the first frame, and ran the detector in every round.

At 0.76.1 on `agy` 1.2.17, headless, installed from a folder, in a throwaway app on the `docs/` form with a bare local remote:

- The session ended its turn on the push command unprompted, a typed yes let it through once, a no with a question published nothing, and a push attempted without the stop was held.
- The document reminder arrived once after the conversation's own commit, and not after another conversation's.

Proven before 0.70.0 only, registered by path: an interactive session, and the hand-over block.

## Not yet verified

- A session building a new page on Sonnet: two sessions at 0.87.0 each dropped at least one of the todo list, the proposal's two lists and the audit offer, and neither read all of the craft material. Two rounds of tighter wording did not change that — build on Opus.
- `design-settle` closing with every check passed: on Opus and on Sonnet the structural diff failed and the session committed with no verdict for it and no queue line. Both reported reduced motion `not verified` — the browser tool cannot emulate it.
- The UI and logic lint floors and the rule tests have never been written in a real app.
- The `docs/` form has never been bootstrapped in a real app.
- `app-settle`'s migrate mode and its align mode have never run in an app. Run migrate on a copy of a legacy app before a real one.
- Whether a cloud session installs this marketplace; until then, cloud sessions do frontend work only.
- The account-wide Supabase MCP endpoint end to end: its first-use login, and `project_id` as `guard_project_ref.py` expects.
- The document reminder after a commit: received on Antigravity only. On Claude Code no session has received it — whether a plugin's `PostToolUse` text reaches the model on an SDK host is unobserved. Both sessions that received it answered `Docs: none`, in an app with no UI; none has answered by writing a document.
- A held push passing on a chat reply: run end to end on Antigravity only. On Claude Code it is replayed against one real transcript, and no session has pushed on a chat reply there.
- `norms-help`: no session has loaded it from an installed copy, on either host.
- On Antigravity: `design-settle` in Full and where UI exists — its audit subagent, its gate; `app-settle` and `logic-settle`; a question asked through `ask_question` in an interactive session; the IDE and Antigravity 2.0. Gemini CLI is not ported.

The full work list, item by item: `docs/queue.md`.
