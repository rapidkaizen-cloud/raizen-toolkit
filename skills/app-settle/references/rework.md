# Rework mode — re-deciding an app that has its documents

## R1 — Read both, then report the drift

Launch the subagent on `repo-read.md`, mode rework. In the same turn, read the living documents the session start did not print — `docs/rules.md` and `docs/glossary.md`, or the sections of a legacy `PRD.md` it named by line range, Section 5 excepted; a decision record only when R3 opens its decision. Report the STACK and DRIFT blocks the subagent returns.

**Drift is a finding put to the user at R3, never a thing to silently "fix" in either direction** — the document may be stale, or the code may have wandered, and only the user knows which. No drift found → say so in one line and move on.

## R2 — What hurts, then state your reading, then STOP

Run the interview of `SKILL.md`; never open with a decision list. The reading names which documents the rework touches. **A rework that turns out to touch only the design system is not this skill** — close and point to `design-settle` directly.

## R3 — Decisions, keep-first

**Walk only the decisions the story touched, plus those their change forces open — never every document.** "Only ask what changes the shape of the repo" becomes: only ask what the rework changes.

Present every decision the same way:

- **What the app does today**, with where it was read from — a document line, a constraint, `rls/approvals.sql:14`.
- **Option one is always keep**, marked as costing nothing.
- Then the alternatives — more than two options total, each with a one-sentence consequence, one marked recommendation.

A keep answered in one word is a finished decision, not a skipped one: the app already paid for its current choices, so the burden of proof sits on the change.

Three rules ride every decision:

- **Domain questions carry no options** (`SKILL.md`). Show the current value and its recorded reason, then ask openly for the new value and the reason behind it.
- **A changed number without a new reason is not recorded**; "the old reason still holds" is a valid new reason and is written as such.
- **A deleted non-goal is scope opening up.** Ask openly what changed, and record the answer as a decision record — beside the deletion in a legacy repo — so the next session knows why the wall came down.

**The stack is on trial here — the user opened it.** Read `stack-questions.md` and `stack-consequences.md` when a stack decision opens, never before.

- Keep is still option one, but framework, database, and hosting may be re-decided; options marked *Not ready* in the stack rubric are still not offered.
- **A migration option's consequence names the real cost in concrete terms**: which layers get rewritten, what runs in parallel meanwhile, and that the migration itself is separate planned work — decided here, recorded in the documents, executed in its own sessions under `build-flow`. A cost that fits in the word "straightforward" has not been costed.

After the walked decisions, show the block of decisions **kept without being asked**, and invite the user to name any they want opened. Do not walk through them one by one.

## R4 — Summary, then STOP

One message:

- Decisions changed — old → new, each with its reason
- Decisions kept — walked and unasked alike
- Drift resolved — which way each mismatch went
- Execution this creates — schema changes, constraint updates, pages to rebuild — named but not started
- Rows still `[needs verification]`

## R5 — Write

Edit the documents under `docs-format` — **the sections touched, not a rewrite.** The old value of a changed rule does not survive as a ghost paragraph: a living document holds current truth, git holds history.

- **`docs/` form** — rules, roles, context, non-goals, and prohibitions in their living documents, timeless; a changed stack decision is a new record superseding the old; `docs/PRD.md` is never touched. Execution crossing `build-flow`'s big-change threshold gets its change record there, in the build session.
- **Legacy form, in a repo that could not migrate** — `PRD.md`'s sections through the map, decision lines in Section 1.
- **`DESIGN.md`, and a legacy Section 5, are not touched**, whatever the rework was about.
- **`CLAUDE.md` rows whose values the rework changed** — stack lines, locale — are updated to match. Nothing else in it moves.

Commit the edited files, paths named.

## R6 — Close

One block:

```
Changed    : [decision: old → new — one line each]
Kept       : [N decisions — walked and unasked]
Drift      : [resolved which way, or "none found"]
Execution  : [what build sessions must now do — or "none"]
Unverified : [what carries [needs verification]]
DESIGN.md  : untouched — design-settle owns it
```

Then the sessions that execute the decisions, in this order:

```
/logic-settle   — only when a logic-layer choice changed or the rework opened one
/design-settle  — when the look changes: audits the styling, rewrites DESIGN.md,
                  proves it on the design canvas
build sessions  — build-flow queues and executes the rest, page by page;
                  schema and constraint changes go through db-ops on the way
```

`logic-settle` before `design-settle`, because the promoted pages carry loading, empty, and failed states, and those belong to the data layer.

Do not run any of them now.
