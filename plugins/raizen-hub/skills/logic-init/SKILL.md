---
name: logic-init
description: Decide the logic-layer libraries of an app whose PRD is written — server-state cache, boundary validator, date handling, error reporting, scheduled-job placement, change attribution. Scores the needs from the PRD, interviews only the needs that score yes with options assembled from the rubric and verified live, records choice and reason in the PRD, installs in one approved block. Use after app-init and before design-init; also when a repo starts growing handwritten data-fetching or validation and the user asks what to adopt.
---

# logic-init — set the logic layer once, from the PRD

`app-init` writes the PRD. `design-init` decides how the app looks. This decides what sits **between the database and the UI**: the libraries — or the deliberate absence of them — for fetching, validating, dating, logging, scheduling, and attributing changes to the user who made them.

Run **once per repo**, after `app-init`, before `design-init`. The pages `design-init` promotes carry loading, empty, and failed states; those states belong to the data layer, so deciding the data layer second means building those pages twice.

## Hard limits

**Zero needs scoring yes is a normal ending, not a failure.** The session closes having installed nothing and reports that plainly. Do not manufacture a need to justify the session — a library nobody needs is maintenance with no payer.

**Only what a scored need asks for is asked, and only what is asked may be installed.** No dependency arrives outside the Step 4 block.

Options come from `references/logic-rubric.md`, **verified live at decision time** (Step 2). Do not present a stale table row as current fact, and do not invent candidates the rubric's admission rule would refuse.

The interview's output lands in exactly two documents: **PRD Section 1** (choice + one-sentence reason, rejections one line each) and the **Stack table of `CLAUDE.md`** (names). No `ARCHITECTURE.md`, no `DECISIONS.md`, no interview summary as a file.

Do not commit and do not push. Staging is fine; the commit waits for the user.

An existing app that already works is **not** re-run through this on your own initiative. The user asking "what should we adopt" is the trigger; an audit finding is a report, not a license.

## Step 0 — Preconditions

Check and report one short block:

```
PRD.md         : [present / missing]
Stack          : [from CLAUDE.md — framework · hosting · database]
Server surface : [yes — which / no — static SPA]
Flow           : score needs → mode → interview (only what scores) → PRD + CLAUDE.md → install
```

`PRD.md` missing → **STOP**, point to `app-init`.

**Server surface decides half the questions.** A static SPA has no boundary handler to validate and no server log to route — `logic-build` Sections 3 and 4 are different worlds. Read it from the Stack table and Section 1 Surface, and get it right before anything else.

## Step 1 — Score the needs, from the PRD

Six needs. Each is read from the PRD, not asked. **Not mentioned in the PRD means no.**

| # | Need | Read from |
|---|---|---|
| L1 | Screens read lists from the database | Section 2 — a role reads, searches, or filters records |
| L2 | Input crosses a trust boundary | A server surface exists (Step 0) |
| L3 | Rules bound to dates, deadlines, or timezones | Section 3 Timing & Deadlines is non-empty |
| L4 | Errors need a destination beyond the host's default log | A server surface exists, **and** Section 1 says the app is operational rather than an experiment |
| L5 | Work runs on a schedule | Section 3 names a recurring run |
| L6 | A change has to be traceable to the person who made it | Section 2 — a role may change or delete records another role created; **or** Section 3 Approval is non-empty |

Report the score as one block, one line per need: `L1 yes — Section 2, CRM reads the lead list` or `L3 no — Section 3 has no timing rules`. The user may override any line — a yes they cancel is not asked; a no they raise is.

Confirm the score with the **AskUserQuestion tool**, never as a prose question: first option accepts the score as read and is the marked recommendation, second option overrides — the lines to flip arrive through the answer or "Other". A prose question at the end of a turn is skipped in auto mode and answered by no one.

All six no → jump to Step 5 and close.

## Step 2 — Interview, only what scored

### Pick the mode first — one question, before anything else

Right after the score is confirmed, asked with the AskUserQuestion tool like everything else. Offer two, with a recommendation — the same shape as the `design-init` mode question, shrunk to an interview of at most six:

| Mode | What is asked | For whom |
|---|---|---|
| **Fast** | Nothing. Every scored need is decided from the rubric and the PRD reading, then shown once as a list to correct | An app that must ship today, or needs whose platform answer nobody disputes |
| **Full** | Every scored need, one question per turn | **Recommended.** The interview is at most six questions, and each answer is a dependency the repo carries for years |

Exactly one need scored → skip this question and ask that need directly; a mode question would cost as much as the interview it replaces.

**Consequence:** both modes end at the same two documents and the same install block — the only difference is where the correction happens, before the decisions or after them.

Fast mode **must not be silent.** Every decision is reported on one line with its basis:

```
L1 cache → TanStack Query  (rubric: several list screens share server rows)
L3 dates → Intl built-in   (platform ladder: format-only, no date arithmetic)
```

Fast skips the questions, never the verification — a candidate chosen in fast mode is still verified live first, and "none" still wins wherever the platform ladder says it does. The user may cancel any line, and cancelling it opens that question normally.

### Running the interview

Read `references/logic-rubric.md`. One question per turn, in L-number order. Each carries **more than two options** · **one marked recommendation** · **a one-sentence consequence** — the same contract as the `design-init` interview.

**Every question goes through the AskUserQuestion tool, never prose text.** Options live in the tool call — the recommendation first and marked "(Recommended)", the consequence in each option's description. The tool caps at four options and adds "Other" on its own, which is how answers outside the options arrive. This holds in auto mode too: the interview is a decision only the user can make, and a prose question there simply ends the turn unanswered.

Three rules specific to this interview:

**The "none" option is always among the options.** *Handwritten*, *platform built-in*, or *not yet* — whichever the rubric names for that question — is never dropped from the list. It becomes the recommendation whenever the platform already covers the need or the app is too small for the library to pay for itself — and only then does it sit first; when a library is the recommendation, the library sits first and "none" stays in the list below it. The candidates are the fallback; the platform is the default.

**Candidates are verified at decision time.** Before presenting options, run a short web check against the rubric's admission rule — still widely adopted, still maintained, no fresh supply-chain event. The landscape this rubric covers moves faster than any table; a check that contradicts a row wins over the row, and the row is the finding. Zero verifiable candidates → say so and offer handwritten, never present the stale row as if verified.

**The story bends the options.** The rubric's *Fits when* column filters and re-ranks: an Edge runtime reorders L2, a realtime mention extends L1, a two-screen app moves the recommendation to handwritten. Read the story from the PRD, not from the rubric.

Answers outside the options are accepted. The user names a library not in the rubric → verify it the same way, use it, and state its consequence if known — or say you don't know it.

## Step 3 — Record

Two writes, and the split matters:

| Where | What |
|---|---|
| `PRD.md` Section 1 | One line per decision: **choice — one-sentence reason**. Rejected candidates one line each, alongside the rejected stack alternatives already there |
| `CLAUDE.md` Stack table | One row per library: name only |

The reason goes in the PRD because it is the one thing a live check cannot recover — the lockfile always knows *what*, never *why*. Keep the reason to one sentence; versions stay out of the PRD entirely, or every bump becomes a document edit.

Choosing "none" for a scored need is also recorded, with its reason. A later session that finds handwritten fetching must be able to tell a decision from an accident.

**L6 is the exception to the second row.** A trigger is not a library, so nothing goes in the Stack table — the PRD line and the migration are the whole record. Write the tracked tables as a criterion, never as a list: "tracked wherever one role can change another role's records", not the table names, which go stale on the next feature.

A chosen library that belongs to a family is recorded with its family — `TanStack Query — TanStack ecosystem` — because `design-init` reads Section 1 when assembling UI options, and an installed family member shifts those recommendations.

## Step 4 — Install, one block

Skip when every answer was "none". Otherwise:

```
Will install:
  <library>        [which question, one line why]
  ...
```

One approval. Refused → hand over the commands, then wait.

A trigger chosen at L6 installs nothing — it is a migration. It goes in the same approval block, named as a migration rather than a package, and it is applied the way every other schema change in this repo is applied.

A trigger has its own smoke check, because it never passes through the compiler: as an authenticated user, not `service_role`, write and then delete one throwaway row in a tracked table, and confirm three audit rows exist with the actor filled in. A null actor here means the fallback is wired wrong, and that is the whole point of the feature. Then delete the throwaway rows from the audit table too — this is the only moment deleting from it is correct.

After installing, one smoke check: a single throwaway usage that exercises each library, `tsc --noEmit` (or the stack's equivalent) passing, then the throwaway is deleted. A library that does not compile against this repo's TypeScript config is cheaper to discover now than mid-page.

No canvas and no proof page. `design-init` needs them because visual direction can only be judged by looking; a library choice is judged by the build passing and by use, and its first real use arrives with the first page.

When writing against a chosen library later, the installed `docs-lookup` skill (Context7) can pull current documentation — a pointer, not a dependency.

## Step 5 — Close

One block: the needs scored and their source lines · decisions taken, including every "none" · what was installed · what `PRD.md` and `CLAUDE.md` now record · what is still `[needs verification]`.

Nothing scored → one line saying so, and that this is the intended outcome for an app of this shape.

**A trigger chosen at L6 creates a responsibility this skill may not write.** Who may read the audit, and whose records they may read, belongs to Section 2 — and Section 1 is the only section this skill writes. Close by handing the user the line that Section 2 now needs, and say plainly that it is theirs to add. A recording nobody is allowed to read is the same cost as no recording.

Close by reminding the user that the commit waits for their word, then offer `design-init` as the next session — the visual direction is still the open gate.

## Later needs

A need that surfaces after this session — a screen that suddenly wants caching, a handler that appears where none existed — is **raised to the user, never installed silently**. `logic-build` binds every session to that; this skill is the only place the questions are asked, and re-opening one question does not re-open the interview.

Several needs surfacing at once, or a library that turns out to be the wrong tool rather than a missing one, is `logic-rework` — which audits what the repo actually runs before asking anything. It is still the user's to start, never yours.
