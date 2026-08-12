---
name: logic-rework
description: Rework the logic layer of an app that already runs — server-state cache, boundary validator, date handling, error reporting, scheduled jobs, change attribution. Audits what is installed and what is handwritten, scores the needs from the PRD, then puts each one to the user as keep, adopt, or replace, and migrates the call sites in one pass. Use when the user asks what to adopt or wants a logic library changed; never on your own initiative.
---

# logic-rework — the logic layer of an app that already runs

`logic-init` chooses from nothing, before a single page exists. Here the choices were already made — or were never made, and the gaps were filled by hand — and the app is running on the result. That reverses the order of work: **audit first, interview second**, the same shape as `design-rework`.

## Hard limits

**Started by the user, never by you.** An audit finding is a report, not a licence. `logic-build` may raise one surfaced need mid-session; this whole skill opens only when the user asks for it.

`PRD.md` is an **absolute precondition**. Missing → STOP, point to `app-recover`.

**Keeping everything is a valid ending, not a failure.** Every answer *keep* closes this skill with nothing installed, nothing removed, and the PRD unchanged. Report the audit and say so plainly; do not manufacture a change to justify the session.

Two documents may be written, and no third: **PRD Section 1** (choice + one-sentence reason, rejections one line each) and the **Stack table of `CLAUDE.md`** (names only). No `ARCHITECTURE.md`, no `DECISIONS.md`, no audit report as a file.

Options come from `references/logic-rubric.md` in `logic-init`, **verified live at decision time**. Do not present a stale table row as current fact.

Do not commit and do not push. Staging is fine.

## Step 0 — Preconditions

```
PRD.md         : [present / missing]
Section 1      : [logic decisions recorded / absent — this app never ran logic-init]
Stack          : [framework · hosting · database, from CLAUDE.md]
Server surface : [yes — which / no — static SPA]
Branch         : [name · clean or has uncommitted changes]
Flow           : audit → score → interview (only what scores) → PRD + CLAUDE.md → install → one pass
```

`PRD.md` missing → **STOP**, point to `app-recover`.

**Working tree not clean → STOP.** A replacement touches every call site at once; uncommitted changes drown among them and can no longer be separated. A clean tree is also what makes the whole pass revertible.

Branch `main` → **STOP.** The git guard will refuse it, and that refusal is correct.

**Server surface decides half the questions.** A static SPA has no boundary handler to validate and no server log to route. Read it from the **code**, not only from `CLAUDE.md` — in an app that grew, the two disagree, and the code is the one that is true.

Section 1 absent → not a blocker. It means nobody ever decided, which is exactly what this session is for; every need then starts from *handwritten or nothing* rather than from a recorded choice.

## Step 1 — Audit, before asking anything

Read what the repo actually does, not what Section 1 claims. One block:

```
AUDIT
L1 cache       : [library · version]  or  [handwritten — N fetch sites]  or  [no list screens]
L2 validation  : [library · version]  or  [handwritten — N boundary handlers, M unvalidated]  or  [no server surface]
L3 dates       : [library · version]  or  [platform Intl]  or  [raw Date arithmetic — N sites]
L4 errors      : [service]  or  [host log only]  or  [swallowed — N empty catch blocks]
L5 jobs        : [where they run]  or  [none found]
L6 attribution : [trigger on N tables]  or  [application-side]  or  [none]
Health         : [unmaintained · past EOL · known advisory — per library, or "clean"]
Duplicates     : [two libraries covering one need]
Call sites     : [per library, how many files import it]
Deviates from S1: [per line the PRD claims but the code does not do]
```

Three rows carry the weight:

**Call sites** decides the size of any replacement, and the user is entitled to see it before deciding anything. A library imported in four files and one imported in ninety are not the same decision, however identical the rubric row.

**Duplicates** is the finding that pays for this audit. Two date libraries, or a validator sitting beside a hand-rolled checker, means every later session picks one at random. Consolidating is repair — it changes no decision, so it needs approval but no interview.

**Unvalidated boundary handlers are counted and reported always**, including where L2 already names a library. A validator installed but not applied at every boundary is a security finding, not a library finding, and it is the one row here that can be actively unsafe. Report the count even when every other row comes out clean.

A deviation from Section 1 is a **finding**, not a reason to rewrite Section 1. Some of it needs no rework at all — offer that as the cheaper path whenever the audit shows the problem is deviation rather than a wrong choice.

## Step 2 — Score the needs, from the PRD

The same six as `logic-init`, read from `PRD.md` and not asked. **Not mentioned in the PRD means no.**

| # | Need | Read from |
|---|---|---|
| L1 | Screens read lists from the database | Section 2 — a role reads, searches, or filters records |
| L2 | Input crosses a trust boundary | A server surface exists (Step 0) |
| L3 | Rules bound to dates, deadlines, or timezones | Section 3 Timing & Deadlines is non-empty |
| L4 | Errors need a destination beyond the host's default log | A server surface exists, **and** Section 1 says the app is operational rather than an experiment |
| L5 | Work runs on a schedule | Section 3 names a recurring run |
| L6 | A change has to be traceable to the person who made it | Section 2 — a role may change or delete records another role created; **or** Section 3 Approval is non-empty |

One difference from `logic-init`, and it matters: **a need that scores *no* while the audit found something installed for it is still reported**, on its own line. That is either a library nobody needs — maintenance with no payer — or a PRD missing a rule the app has been enforcing all along. Both deserve a sentence; neither is fixed here on your own initiative.

Report the score as one block, one line per need, each naming its source. The user may override any line — a yes they cancel is not asked, a no they raise is.

Confirm the score with the **AskUserQuestion tool**, never as prose: the first option accepts the score as read and is the marked recommendation, the second overrides. A prose question at the end of a turn is skipped in auto mode and answered by no one.

All six score *no* and the audit found nothing installed → jump to Step 7 and close.

## Step 3 — Interview, only what scored

Read `references/logic-rubric.md` in `logic-init`. One question per turn, in L-number order. Each carries **more than two options** · **one marked recommendation** · **a one-sentence consequence**, through the AskUserQuestion tool, never prose.

Three rules replace the `logic-init` ones:

**What the repo uses today is always an option, written first** — `Keep — <what is installed>`, or `Keep — handwritten, N sites`. It does not count toward the "more than two options" requirement. A value that is only a recommendation is a suggestion; a value written as an option is a choice.

**Keep is the recommendation, unless the audit produced a concrete finding against it.** Without that clause *keep* always wins and nothing ever improves; without the first clause every session becomes a migration. A concrete finding is one of three, and the list is closed:

| Concrete finding | Not a finding |
|---|---|
| Unmaintained, or a fresh supply-chain event or advisory | The rubric ranks another candidate higher |
| Past end-of-life for security fixes | A newer option exists |
| **It blocks a norm** — something in `raizen-norms` cannot hold while this library stands | You would have picked differently |

A finding exists → the replacement may be recommended, and the finding **is** its one-sentence consequence. State the finding, never a preference.

**Every option quotes its migration size from the audit** — `Replace with X — 31 call sites` beside `Keep — 0`. A decision priced after it is made is not a decision.

Candidates are **verified live** before being presented: still widely adopted, still maintained, no fresh supply-chain event. A check that contradicts the rubric wins over the rubric, and the contradiction is itself a finding worth reporting. Zero verifiable candidates → say so and offer handwritten; never present a stale row as verified.

Answers outside the options are accepted. A library not in the rubric → verify it the same way, use it, and state its consequence — or say you do not know it.

## Step 4 — Record

| Where | What |
|---|---|
| `PRD.md` Section 1 | One line per decision: **choice — one-sentence reason**. Rejected candidates one line each |
| `CLAUDE.md` Stack table | One row per library: name only |

Reasons live in the PRD because that is the one thing a live check can never recover — the lockfile always knows *what*, never *why*. One sentence each; versions stay out of the PRD, or every bump becomes a document edit.

**A *keep* is recorded too**, with its reason, wherever Section 1 carried no line for it before. A later session that finds handwritten fetching must be able to tell a decision from an accident — and after this session it can.

L6 is the exception to the second row: a trigger is not a library, so nothing goes in the Stack table. Write the tracked tables as a **criterion**, never as a list, which goes stale on the next feature.

A library belonging to a family is recorded with its family — `TanStack Query — TanStack ecosystem` — because `design-rework` reads Section 1 when assembling UI options, and an installed family member shifts those recommendations.

## Step 5 — Install, one block

Skip when every answer was *keep*. Otherwise one block, one approval:

```
Will install:
  <library>          [which need, one line why]
Will remove:
  <old library>      [at Step 6, after the call sites move — not now]
Will migrate:
  <need>             [N call sites across M files]
```

Refused → hand over the commands, then wait. Install nothing outside that block; something extra turns out to be needed → ask again, do not slip it in.

A trigger chosen at L6 installs nothing — it is a migration. It goes in the same block, named as a migration rather than a package, and it is applied the way every other schema change in this repo is applied.

## Step 6 — One pass, then verify

**One session, every call site of one decision.** Not staged, and no old library left alive beside the new one.

The order cannot be reversed: move the call sites → confirm the build → **then** remove the old library. A dependency removed first turns every remaining site into a build error and hides which of them was real work.

**A replacement too large to finish in this session is not started.** The size was measured at Step 1; where the call-site count does not fit, the decision still stands and the migration becomes a `QUEUE.md` line under `build-flow` instead. Half a migration leaves two libraries doing one job — the exact `Duplicates` finding this skill exists to remove.

Do not slip in unrelated fixes. A logic migration that also tidies UI produces a diff nobody can read, and one mistake will hide among hundreds of legitimate changes.

Then all of these, before reporting done:

- **The build passes**, and `tsc --noEmit` or the stack's equivalent is clean.
- **Zero imports of the removed library remain** — searched again, not assumed.
- **The unvalidated-boundary count from Step 1 has not grown.** It is allowed to stay; it is never allowed to rise.
- **A trigger chosen at L6 is smoke-checked**, because it never passes through the compiler: as an authenticated user, not `service_role`, write and then delete one throwaway row in a tracked table, and confirm three audit rows exist with the actor filled in. A null actor means the fallback is wired wrong, and that is the entire point of the feature. Then delete the throwaway audit rows — the only moment deleting from that table is correct.

Any of them fails → fix it in the same session. A half-finished logic migration is worse than none: the app still runs, so nobody knows it is broken.

## Step 7 — Close

One block: needs scored and their source lines · what the audit found · decisions taken, including every *keep* · what was installed and removed · call sites moved · migrations deferred to `QUEUE.md` · the verification results · what is still `[needs verification]`.

Nothing changed — every answer was *keep* → say so in one line and list the audit findings that remain. A session that changes nothing has still produced the audit, and that is worth writing down.

**A trigger chosen at L6 creates a responsibility this skill may not write.** Who may read the audit, and whose records they may read, belongs to Section 2 — and Section 1 is the only section this skill writes. Hand the user the line Section 2 now needs, and say plainly that it is theirs to add. A recording nobody is allowed to read costs the same as no recording.

Close by reminding the user that the commit waits for their word, and that a migration of this size deserves a commit of its own, with nothing else riding along inside it.
