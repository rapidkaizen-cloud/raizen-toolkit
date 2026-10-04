# QUEUE — toolkit work not done yet

- Token-cost cuts (`raizen-hub` 0.68.0 and 0.69.0, `raizen-norms` 0.36.0 to 0.37.0) are committed and not pushed. Run `simulate` on `design-settle` in a fresh session and check that every decision of the flow lands where it did before; push only after it passes. No run of the restructured skills against an app exists yet.
- `app-settle` N6: the sentence that no hosting or CI file is written at bootstrap was removed, because the N5 table writes a host rewrite rule and a CI workflow. Confirm the table is the intent, or delete its two `Bootstrap` rows.
- `build-flow` Section 9 states the commit once and never mid-session; the session norms' `GIT` block commits a finished scope item in the same turn. Decide which holds.
- `bulk` is "several hundred rows" in `ui-build` and "500+ rows" in `build-flow`'s `references/contract.md`. Keep one number.
- `logic-settle`: the jump to Step 7 when nothing scored skips Step 5's install block, though Step 7 may need a linter installed.
- `app-align`: the hard limit names `AGENTS.md` as the only file it may create, and C7 creates `docs/queue.md`.
- `db-ops`: `references/agent-account.md` says it is also read when a session must sign in without an account; `SKILL.md` points to it only from the role test.
