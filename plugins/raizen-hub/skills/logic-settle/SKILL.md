---
name: logic-settle
description: Settle the logic layer of an app whose PRD is written — server-state cache, boundary validator, date handling, error reporting, scheduled jobs, change attribution. Audits what the repo runs today, scores the needs from the PRD, interviews only what scores yes with options assembled from the rubric and verified live, records choice and reason in the PRD, installs in one approved block, migrates call sites in one pass where something is replaced, names the one folder every database call lives in, and writes the lint floor that holds the layer there. Use after app-settle and before design-settle on a new repo; also when a repo grows handwritten data-fetching or validation and the user asks what to adopt. Never on your own initiative on a running app.
---

# logic-settle — the layer between the database and the UI

`app-settle` writes the PRD. `design-settle` decides how the app looks. This decides what sits **between the database and the UI**: the libraries — or the deliberate absence of them — for fetching, validating, dating, logging, scheduling, and attributing changes to the user who made them.

**One skill, whether the layer is empty or already running.** There is no mode to pick and no second skill to route to: Step 1 audits what the repo does today, and what it finds decides the rest. An empty audit is a new repo starting from nothing; a full one is an app whose choices were already made, or were never made and got filled in by hand. Everything downstream reads the audit rather than asking which case this is.

On a new repo, run **after `app-settle` and before `design-settle`**. The pages `design-settle` promotes carry loading, empty, and failed states; those states belong to the data layer, so deciding the data layer second means building those pages twice.

## Hard limits

**Never opened on your own initiative on a running app.** The user asking "what should we adopt" is the trigger. A session that finds the logic layer bleeding — handwritten fetching spreading across files, input crossing a trust boundary unvalidated, dates parsed by hand in many places — makes the offer through **AskUserQuestion**, once, and an offer must carry its evidence or it is not made: the measured finding (which files, how many call sites, what it costs today), the concrete consequence of leaving it, and a recommendation. Never a bare "want to run this?". A finding too thin to state in numbers is a report line, not an offer. Declining closes the matter for that session. On a repo with no application code the sequence itself is the trigger and no offer is needed.

**Zero needs scoring yes is a normal ending, and so is keeping everything.** Either way the session closes having installed nothing and reports that plainly. Do not manufacture a need or a change to justify the session — a library nobody needs is maintenance with no payer.

**Only what a scored need asks for is asked, and only what is asked may be installed.** No dependency arrives outside the Step 5 block.

Candidates are **assembled live**: the model's own knowledge proposes, web research verifies each one. `references/logic-rubric.md` holds the categories, the criteria, the admission rule, and the research duty — **it names no candidates**. Do not present an unresearched candidate, and do not offer one the admission rule would refuse.

The output lands in exactly three documents: **PRD Section 1** (choice + one-sentence reason, rejections one line each), the **Stack table of `CLAUDE.md`** (names only, plus the `Data layer` row), and the **`## Logic` part of `AGENTS.md`** at Step 7 — the pointer an agent without the plugin reads. The lint floor of Step 7 is config, not a document. No `ARCHITECTURE.md`, no `DECISIONS.md`, no audit report as a file.

`PRD.md` is an absolute precondition. Do not commit and do not push; staging is fine.

## Step 0 — Preconditions

Check and report one short block:

```
PRD.md         : [present / missing]
Section 1      : [logic decisions recorded / absent — nobody ever decided]
Stack          : [from CLAUDE.md — framework · hosting · database]
Server surface : [yes — which / no — static SPA]
Application code: [present / none yet — the audit will say which]
Branch         : [name · clean or has uncommitted changes]
Flow           : audit → score + data layer folder → interview (only what scores)
                 → PRD + CLAUDE.md → install → one pass, where something is replaced or moved
                 → the floor, always
```

`PRD.md` missing → **STOP**, point to `app-settle`.

Branch `main` → **STOP.** The git guard will refuse it, and that refusal is correct.

**Server surface decides half the questions.** A static SPA has no boundary handler to validate and no server log to route — `logic-build` Sections 3 and 4 are different worlds. Read it from the Stack table and Section 1 Surface, and where application code exists read it from the **code** as well: in an app that grew, the two disagree, and the code is the one that is true.

**Working tree not clean → say it and carry on.** Name the dirty paths in one line, and say that committing or stashing them first is what keeps this session's diff separable — a replacement touches every call site at once, and uncommitted changes drown among them. Advice, not a gate. Where a dirty path is also a call site the pass will rewrite, name it again at Step 6 rather than only here.

Section 1 absent → not a blocker. It means nobody ever decided, which is exactly what this session is for; every need then starts from *handwritten or nothing* rather than from a recorded choice.

## Step 1 — Audit, before asking anything

**Always run, and it is what decides the shape of everything after it.** Read what the repo actually does, not what Section 1 claims. On a repo with no application code this comes back empty in one pass — that is the cheapest possible answer to the question "which kind of session is this", and it costs less than asking.

```
AUDIT
L1 cache       : [library · version]  or  [handwritten — N fetch sites]  or  [no list screens]
L2 validation  : [library · version]  or  [handwritten — N boundary handlers, M unvalidated]  or  [no server surface]
L3 dates       : [library · version]  or  [platform Intl]  or  [raw Date arithmetic — N sites]
L4 errors      : [service]  or  [host log only]  or  [swallowed — N empty catch blocks]
L5 jobs        : [where they run]  or  [none found]
L6 attribution : [trigger on N tables]  or  [application-side]  or  [none]
Data layer     : [folder · N files call the database · M of them outside it]  or  [no database calls yet]
                 or  [n/a — no database and no remote API]
Health         : [unmaintained · past EOL · known advisory — per library, or "clean"]
Duplicates     : [two libraries covering one need]
Call sites     : [per library, how many files import it]
Deviates from S1: [per line the PRD claims but the code does not do]
```

Every row empty → say so in one line: this repo has no logic layer yet, and every need below starts from nothing. Do not skip the block; a reader cannot tell "audited and empty" from "never audited" without it.

Three rows carry the weight where the audit is not empty:

**Call sites** decides the size of any replacement, and the user is entitled to see it before deciding anything. A library imported in four files and one imported in ninety are not the same decision, however identical the candidates look.

**Duplicates** is the finding that pays for this audit. Two date libraries, or a validator sitting beside a hand-rolled checker, means every later session picks one at random. Consolidating is repair — it changes no decision, so it needs approval but no interview.

**Unvalidated boundary handlers are counted and reported always**, including where L2 already names a library. A validator installed but not applied at every boundary is a security finding, not a library finding, and it is the one row here that can be actively unsafe. Report the count even when every other row comes out clean.

**The `Data layer` row is measured, never asked.** Count the files that import or call the database client and group them by folder: the folder holding most of them, how many sit outside it. It is not one of the six needs — every app with a database has a data layer, chosen or accumulated — and it is what `logic-build` Section 8, the floor at Step 7, and the session-start listing all scope to. A query inline in a page is a query the next session cannot find, so it writes it again; this row is the count of how often that has already happened.

A deviation from Section 1 is a **finding**, not a reason to rewrite Section 1. Some of it needs no rework at all — offer that as the cheaper path whenever the audit shows the problem is deviation rather than a wrong choice.

## Step 2 — Score the needs, from the PRD

Six needs. Each is read from the PRD, not asked. **Not mentioned in the PRD means no.**

| # | Need | Read from |
|---|---|---|
| L1 | Screens read lists from the database | Section 2 — a role reads, searches, or filters records |
| L2 | Input crosses a trust boundary | A server surface exists (Step 0) |
| L3 | Rules bound to dates, deadlines, or timezones | Section 3 Timing & Deadlines is non-empty |
| L4 | Errors need a destination beyond the host's default log | A server surface exists — or the Surface ships as an installed binary, whose failures happen where no host log can see them — **and** Section 1 says the app is operational rather than an experiment |
| L5 | Work runs on a schedule | Section 3 names a recurring run |
| L6 | A change has to be traceable to the person who made it | Section 2 — a role may change or delete records another role created; **or** Section 3 Approval is non-empty |

**A need that scores *no* while the audit found something installed for it is still reported**, on its own line. That is either a library nobody needs — maintenance with no payer — or a PRD missing a rule the app has been enforcing all along. Both deserve a sentence; neither is fixed here on your own initiative. On an empty audit this case cannot arise.

Report the score as one block, one line per need, each naming its source: `L1 yes — Section 2, CRM reads the lead list` or `L3 no — Section 3 has no timing rules`. The user may override any line — a yes they cancel is not asked; a no they raise is.

Confirm the score with the **AskUserQuestion tool**, never as a prose question: the first option accepts the score as read and is the marked recommendation, the second overrides — the lines to flip arrive through the answer or "Other". A prose question at the end of a turn is skipped in auto mode and answered by no one.

**The score block carries one line that is not a need: the data layer folder.** Derived from the audit, shown with its basis, and overridden through the same dialog as any other line:

| The audit found | The folder |
|---|---|
| One folder holding most of the database calls | That folder, as found. **Never renamed for tidiness** — `src/lib` that works is not improved by becoming `src/data`, and the rename is a diff across every import in the app |
| Calls scattered, no folder holding most | The folder already holding the most, named with its count — the rest are the migration Step 5 prices |
| No database calls yet | The framework's own convention where it names one; else a folder named `data` under the stack's source root, the name the platform architecture guides converge on |

```
Data layer : src/lib — 20 of 20 files already there
```

All six score *no* and the audit found nothing installed → jump to Step 7. The folder and its floor are owed by every app with a database, whatever scored; only an app with no database and no remote API closes at Step 8 from here.

## Step 3 — Interview, only what scored

### Pick the interview mode first — one question, before anything else

Right after the score is confirmed, asked with the AskUserQuestion tool like everything else. Offer two, with a recommendation — one dialog before an interview of at most six:

| Mode | What is asked | For whom |
|---|---|---|
| **Fast** | Nothing. Every scored need is decided from the rubric's criteria, the research, the audit, and the PRD reading, then shown once as a list to correct | An app that must ship today, or needs whose platform answer nobody disputes |
| **Full** | Every scored need, batched — sequential only across a real dependency | **Recommended.** The interview is at most six questions, and each answer is a dependency the repo carries for years |

Exactly one need scored → skip this question and ask that need directly; a mode question would cost as much as the interview it replaces.

**Consequence:** both modes end at the same two documents and the same install block — the only difference is where the correction happens, before the decisions or after them.

Fast mode **must not be silent.** Every decision is reported on one line with its basis:

```
L1 cache → <researched standard>  (criteria: several list screens share server rows; verified live)
L3 dates → Intl built-in          (platform ladder: format-only, no date arithmetic)
```

Fast skips the questions, never the verification — a candidate chosen in fast mode is still verified live first, and "none" or *keep* still wins wherever the ladder and the audit say they do. The user may cancel any line, and cancelling it opens that question normally.

### Running the interview

Read `references/logic-rubric.md`. Questions travel in batches, in L-number order — up to four per AskUserQuestion call, several calls per turn; a need whose options or recommendation read an earlier answer (a family already chosen shifting a later recommendation) waits for that answer, independent needs travel together. Answers are reconciled after every batch: two that collide go back as one question naming both, never resolved silently. Each carries **more than two options** · **one marked recommendation** · **a one-sentence consequence** — the same contract as the `design-settle` interview.

**Every question goes through the AskUserQuestion tool, never prose text.** Options live in the tool call — the recommendation first and marked "(Recommended)", the consequence in each option's description. The tool caps at four options and adds "Other" on its own, which is how answers outside the options arrive. This holds in auto mode too: the interview is a decision only the user can make, and a prose question there simply ends the turn unanswered.

**Candidates are assembled and researched at decision time.** The model's knowledge proposes them; before presenting, web research covers each one against the rubric's admission rule — still widely adopted, still maintained, no fresh supply-chain event — and what it brings versus what it leaves out, which becomes the option's consequence. One pass may cover all candidates; the coverage per option is what is mandatory. Zero candidates surviving → say so and offer handwritten, never present memory alone as if verified.

**The story bends the options.** The rubric's criteria filter and re-rank: an Edge runtime reorders L2, a realtime mention extends L1, a two-screen app moves the recommendation to handwritten. Read the story from the PRD, not from the rubric.

Answers outside the options are accepted. The user names a library the research did not surface → verify it the same way, use it, and state its consequence if known — or say you don't know it.

### Two rules that read the audit, per need

**Where the audit found nothing for this need**, the "none" option is always among the options — *handwritten*, *platform built-in*, or *not yet*, whichever the rubric names — and is never dropped from the list. It becomes the recommendation whenever the platform already covers the need or the app is too small for the library to pay for itself, and only then does it sit first; when a library is the recommendation, the library sits first and "none" stays below it. The candidates are the fallback; the platform is the default.

**Where the audit found something**, that is always an option, **written first** — `Keep — <what is installed>`, or `Keep — handwritten, N sites`. It does not count toward the "more than two options" requirement. A value that is only a recommendation is a suggestion; a value written as an option is a choice. And **keep is the recommendation, unless the audit produced a concrete finding against it** — without that clause *keep* always wins and nothing ever improves; without the first clause every session becomes a migration. A concrete finding is one of three, and the list is closed:

| Concrete finding | Not a finding |
|---|---|
| Unmaintained, or a fresh supply-chain event or advisory | Research ranks another candidate higher |
| Past end-of-life for security fixes | A newer option exists |
| **It blocks a norm** — something in `raizen-norms` cannot hold while this library stands | You would have picked differently |

A finding exists → the replacement may be recommended, and the finding **is** its one-sentence consequence. State the finding, never a preference.

**Every option quotes its migration size from the audit** — `Replace with X — 31 call sites` beside `Keep — 0`. A decision priced after it is made is not a decision.

## Step 4 — Record

Two writes, and the split matters:

| Where | What |
|---|---|
| `PRD.md` Section 1 | One line per decision: **choice — one-sentence reason**. Rejected candidates one line each, alongside the rejected stack alternatives already there |
| `CLAUDE.md` Stack table | One row per library: name only. Plus the **`Data layer` row**: the folder path in backticks, first in its cell — `session_norms.py` reads the path from exactly there to print the folder's functions at every session start, and a row it cannot parse prints nothing |

The reason goes in the PRD because it is the one thing a live check cannot recover — the lockfile always knows *what*, never *why*. Keep the reason to one sentence; versions stay out of the PRD entirely, or every bump becomes a document edit.

**Choosing "none" is recorded, and so is a *keep*** — the latter wherever Section 1 carried no line for it before. A later session that finds handwritten fetching must be able to tell a decision from an accident.

**L6 is the exception to the second row.** A trigger is not a library, so nothing goes in the Stack table — the PRD line and the migration are the whole record. Write the tracked tables as a criterion, never as a list: "tracked wherever one role can change another role's records", not the table names, which go stale on the next feature.

A chosen library that belongs to a family is recorded with its family — `TanStack Query — TanStack ecosystem` — because `design-settle` reads Section 1 when assembling UI options, and an installed family member shifts those recommendations.

## Step 5 — Install, one block

Skip when every answer was "none" or *keep*, the repo already carries a linter, and no database call sits outside the data layer folder. Otherwise one block, one approval — answered in chat at a hard stop, never an AskUserQuestion (a dialog covers the very block the user must read):

```
Will install:
  <library>          [which need, one line why]
  <linter>           [only where the repo carries none — Step 7's floor is written into it]
Will remove:
  <old library>      [at Step 6, after the call sites move — not now]
Will migrate:
  <need>             [N call sites across M files]
  data layer         [M files calling the database outside <folder> — moved into it at Step 6]
```

**The data-layer line is a migration like any other: priced in files, and declinable.** Declined, those files are baselined at Step 7 and the floor still refuses every new one — the scatter stops growing without anyone approving a diff they did not want. Approved, each query moves into the folder unchanged in behaviour, its page importing the function instead; too large for this session → a `QUEUE.md` line under Step 6's existing rule, never half a move.

Present the block, end the turn, wait. Refused → hand over the commands, then wait. Install nothing outside that block; something extra turns out to be needed → ask again, do not slip it in.

A trigger chosen at L6 installs nothing — it is a migration. It goes in the same block, named as a migration rather than a package, and it is applied the way every other schema change in this repo is applied.

A trigger has its own smoke check, because it never passes through the compiler: as an authenticated user, not `service_role`, write and then delete one throwaway row in a tracked table, and confirm three audit rows exist with the actor filled in. A null actor here means the fallback is wired wrong, and that is the whole point of the feature. Then delete the throwaway rows from the audit table too — this is the only moment deleting from it is correct.

After installing, one smoke check: a single throwaway usage that exercises each library, `tsc --noEmit` (or the stack's equivalent) passing, then the throwaway is deleted. A library that does not compile against this repo's config is cheaper to discover now than mid-page.

No canvas. `design-settle` needs one because visual direction can only be judged by looking; a library choice is judged by the build passing and by use, and its first real use arrives with the first page.

When writing against a chosen library later, the installed `docs-lookup` skill (Context7) can pull current documentation — a pointer, not a dependency.

## Step 6 — One pass, then verify

**Runs only where something is replaced or moved.** Nothing removed and nothing migrated — every need answered "none", *keep*, or a first install onto bare ground, and the data-layer line declined or empty — → skip to Step 7. There are no call sites to move.

**One session, every call site of one decision.** Not staged, and no old library left alive beside the new one.

The order cannot be reversed: move the call sites → confirm the build → **then** remove the old library. A dependency removed first turns every remaining site into a build error and hides which of them was real work.

**A replacement too large to finish in this session is not started.** The size was measured at Step 1; where the call-site count does not fit, the decision still stands and the migration becomes a `QUEUE.md` line under `build-flow` instead. Half a migration leaves two libraries doing one job — the exact `Duplicates` finding this skill exists to remove.

Do not slip in unrelated fixes. A logic migration that also tidies UI produces a diff nobody can read, and one mistake will hide among hundreds of legitimate changes.

Then all of these, before reporting done:

- **The build passes**, and `tsc --noEmit` or the stack's equivalent is clean.
- **Zero imports of the removed library remain** — searched again, not assumed.
- **Where the data layer moved: no database call remains outside the folder**, searched again, and every moved query returns what it returned before — the diff of a move shows an import changing and a body relocating, nothing else.
- **The unvalidated-boundary count from Step 1 has not grown.** It is allowed to stay; it is never allowed to rise.
- **A trigger chosen at L6 is smoke-checked** per Step 5's procedure.

Any of them fails → fix it in the same session. A half-finished logic migration is worse than none: the app still runs, so nobody knows it is broken.

## Step 7 — The floor: what the repo refuses from now on

**Runs for every app with a database or a remote API, whatever scored** — including the session that installed nothing and the one that kept everything. Where the jump from Step 2 skipped Step 4, the `Data layer` row of `CLAUDE.md` is written here first. An app with neither skips this step and says so.

Section 1 and `logic-build` are obeyed by judgement, and an agent that is not Claude Code reads neither. What keeps a later session — any agent's — from re-deciding this layer is the repo refusing it: **the five refusals `logic-build` Section 9 names, written into the stack's own linter, derived from this app and never pasted from a stock config.**

| Refusal | Derived from |
|---|---|
| Database client outside the data layer | The folder on the `Data layer` row, and the client package the audit found |
| A secret on its way to the client | The stack's public prefix — `VITE_`, `NEXT_PUBLIC_`, `PUBLIC_`, or its equivalent — and every path a browser can reach; on a static SPA that is all of the source |
| A second library for a settled need | Step 4's decisions: for each need answered with a library or a recorded "none", the alternatives the research surfaced. A need never scored restricts nothing |
| A cast that erases a database type | The data layer folder and its call sites. Not written on an untyped stack |
| A swallowed error | Nothing to derive — it holds in every app. The L4 count from Step 1 is its baseline |

**Scoped by path, and proven on what must pass before what must fail.** The data layer folder is exempt from the first refusal; test files from the fourth and the fifth. On a JS or TS stack ESLint's `no-restricted-imports`, `no-restricted-syntax`, and `no-empty` express all five; another stack uses its own analyzer's equivalent, **verified live at write time, never recalled**, and a refusal it cannot express is reported as `not enforceable on <stack>` — never dropped in silence. Run the lint command over the whole app first: every hit is a real finding or a pattern too wide. Only then plant one violation of each refusal in a scratch file, see each one refused, and delete the file — a config whose glob matches nothing passes every run and guards nothing.

**What already stands is baselined, never excused and never repaired here.** Database calls the user declined to move, old casts, old empty catches: they go into the linter's own suppression baseline — verified live that it has one — so the floor refuses every new violation from its first commit. Never by lowering a rule to a warning: no agent reads a warning. Repairing them is a diff nobody approved in this session. The baseline's size is reported at the close, and it only ever shrinks.

**One floor, one command.** Where `design-settle` has already written the UI floor, these five join the same config and the same lint command; where it has not, this step founds the config and `design-settle` joins it later. Two configs is two commands, and the second one is the one no session runs.

**`AGENTS.md` gets its `## Logic` part in the same act** — to the shape `app-settle` N5 gives that file: the data layer folder and that no database call is written outside it · that access rules live in the database and are never re-implemented in application code · the settled libraries by pointer to `CLAUDE.md`'s Stack table, never repeated · the lint command and the test command · that a failing rule test is never fixed by editing the test. Where the repo has no `AGENTS.md`, the whole file is written to that shape.

## Step 8 — Close

One block: the needs scored and their source lines · what the audit found · decisions taken, including every "none" and every *keep* · the data layer folder and its basis · what was installed and removed · call sites moved · migrations deferred to `QUEUE.md` · the floor — refusals written, the baseline's size, anything `not enforceable` · the verification results · what is still `[needs verification]`.

Nothing scored, or nothing changed → say so in one line, list the audit findings that remain, and say that this is the intended outcome for an app of this shape. A session that changes nothing has still produced the audit, and that is worth writing down.

**A trigger chosen at L6 creates a responsibility this skill may not write.** Who may read the audit, and whose records they may read, belongs to Section 2 — and Section 1 is the only section this skill writes. Close by handing the user the line that Section 2 now needs, and say plainly that it is theirs to add. A recording nobody is allowed to read is the same cost as no recording.

Close by reminding the user that the commit waits for their word — and where a migration ran, that a migration of this size deserves a commit of its own, with nothing else riding along inside it. On a new repo, offer `design-settle` as the next session: the visual direction is still the open gate.

## Later needs

A need that surfaces after this session — a screen that suddenly wants caching, a handler that appears where none existed — is **raised to the user, never installed silently**. `logic-build` binds every session to that; this skill is the only place the questions are asked, and re-opening one question does not re-open the interview.

Several needs surfacing at once, or a library that turns out to be the wrong tool rather than a missing one, re-opens this skill in full — the audit at Step 1 is what makes that safe. It is still the user's to start, never yours.
