---
name: logic-settle
description: Settle the logic layer of an app whose documents are written — server-state cache, boundary validator, date handling, error reporting, scheduled jobs, change attribution — plus the one folder every database call lives in and the lint floor that holds the layer there. Use after app-settle and before design-settle on a new repo; also when a repo grows handwritten data-fetching or validation and the user asks what to adopt. Never on your own initiative on a running app.
---

# logic-settle — the layer between the database and the UI

`app-settle` writes the documents, `design-settle` decides how the app looks. This skill decides what sits **between the database and the UI**: the libraries — or the deliberate absence of them — for fetching, validating, dating, logging, scheduling, and attributing changes to the user who made them. Documents are named by their `docs/` path; a repo with a root `PRD.md` reads each through `docs-format`'s legacy map.

**One path, no mode to pick.** The Step 1 audit decides the rest: empty, the repo starts from nothing; full, its choices were already made, or never made and filled in by hand. Every later step reads the audit, never asks which case this is.

On a new repo, run **after `app-settle` and before `design-settle`**: the pages `design-settle` promotes carry loading, empty, and failed states, and those belong to the data layer.

## What a run costs — four rules

- **Read a step's file when the flow reaches that step, never earlier.** The table under Step 2 names each one; a file whose condition does not hold is never read, and a need that scored *no* never costs its need file.
- **Run a step's independent reads, searches and commands in one turn** — parallel calls, or one chained command — because every extra model call re-reads the whole session.
- **Hand non-taste work to one subagent on a cheaper model than the session's** (`sonnet` on Claude Code): the Step 1 audit, the live verification of candidates, any other web research. Brief it with the file that rules the job and take back only the compact result that file names — its raw results never enter this session. No subagent → run it here and say so; no model choice → the session's model.
- **Never re-read what the session start printed** — the documents and the two listings; read only the documents it did not print.

## Hard limits

**Never open this skill on your own initiative on a running app.** The user asking what to adopt is the trigger; on a repo with no application code the sequence itself is, and no offer is needed. A session that finds the logic layer bleeding — handwritten fetching spreading across files, input crossing a trust boundary unvalidated, dates parsed by hand in many places — makes the offer through AskUserQuestion, once, carrying its evidence: the measured finding (which files, how many call sites, what it costs today), the concrete consequence of leaving it, and a recommendation — never a bare "want to run this?". A finding too thin to state in numbers is a report line, not an offer. Declining closes the matter for that session.

**Zero needs scoring yes is a normal ending, and so is keeping everything.** Close having installed nothing and report that plainly; manufacture no need and no change to justify the session.

**Ask only what a scored need asks for, and install only what was asked** — no dependency arrives outside the Step 5 block.

**Assemble candidates live, as `references/logic-rubric.md` rules** — it holds the categories, the criteria, the admission rule, and the research duty, and names no candidates. Never present memory as verified, and never offer a candidate the admission rule would refuse.

**Write the output in three places and no fourth:** `docs/decisions/` — one record per decision, its rejected candidates among the considered options; where the folder is new, `docs/README.md` gets its line · the Stack table of `CLAUDE.md` — names only, plus the `Data layer` row · the `## Logic` part of `AGENTS.md`, at Step 7 — the pointer an agent without the plugin reads. The Step 7 lint floor is config, not a document. No `ARCHITECTURE.md`, no `DECISIONS.md`, no audit report as a file.

**The `Data layer` row holds the folder path in backticks, first in its cell**: `session_norms.py` reads the path from exactly there to print the folder's functions at every session start, and a row it cannot parse prints nothing.

**Every question goes through AskUserQuestion, never prose**, in auto mode too — a prose question at the end of a turn is answered by no one. The recommendation is first and marked "(Recommended)", each option's consequence sits in its description, up to four questions travel per call; the tool caps at four options and adds "Other" on its own, which is how an answer outside the options arrives. The Step 5 block is the one chat stop.

**Do not commit and do not push**; staging is fine.

## Step 0 — Preconditions

Fill this block from one turn of parallel reads, and print it:

```
PRD            : [docs/PRD.md / root PRD.md — legacy form / missing]
Decisions      : [logic decisions recorded / none — nobody ever decided]
Stack          : [from CLAUDE.md — framework · hosting · database]
Server surface : [yes — which / no — static SPA]
Application code: [present / none yet — the audit will say which]
Branch         : [name · clean or has uncommitted changes]
Flow           : audit → score + data layer folder → interview (only what scores)
                 → decision records + CLAUDE.md → install → one pass, where something is replaced or moved
                 → the floor, always
```

- **No PRD in either form → STOP**, point to `app-settle`.
- **Branch `main` → STOP**: a session never works on `main`.
- **Server surface decides half the questions**: a static SPA has no boundary handler to validate and no server log to route (`logic-build` Sections 3 and 4). Read it from the Stack table and the Surface in `docs/product.md`, and where application code exists from the **code** as well — in an app that grew the two disagree, and the code is the one that is true.
- **Working tree not clean → say it and carry on.** Name the dirty paths in one line, and say that committing or stashing them first keeps this session's diff separable. Advice, not a gate.
- **No logic decision recorded → not a blocker**: every need starts from *handwritten or nothing* rather than from a recorded choice.

## Step 1 — Audit, before asking anything

**Always run it, in one subagent whose whole brief is `references/audit.md`** — hand it that path and the repo root, and never read the file here. It reads what the repo does, never what the decision records claim, and returns the filled `AUDIT` block. No subagent → run the audit here from that file and say so.

- **Print the block on every repo, as returned.** Every row empty → say in one line that this repo has no logic layer yet and every need below starts from nothing; never skip the block, or "audited and empty" reads as "never audited".
- **`Call sites` sizes any replacement** — show it before the user decides anything.
- **`Duplicates` — two libraries covering one need — is consolidated as repair**: it changes no decision, so it needs approval but no interview.
- **Report the unvalidated-boundary count always**, even where L2 names a library and every other row is clean: it is the one row that can be actively unsafe.
- **A deviation from a decision record is a finding, never a reason to supersede the record.** Where the audit shows deviation rather than a wrong choice, offer bringing the code back in line as the cheaper path — some of it needs no rework at all.

## Step 2 — Score the needs, from the documents

**Read each of the six needs from the documents, never ask it. Not mentioned in them means no.**

| # | Need | Read from |
|---|---|---|
| L1 | Screens read lists from the database | Roles — a role reads, searches, or filters records |
| L2 | Input crosses a trust boundary | A server surface exists (Step 0) |
| L3 | Rules bound to dates, deadlines, or timezones | `docs/rules.md` holds timing or deadline rules |
| L4 | Errors need a destination beyond the host's default log | A server surface exists — or the Surface ships as an installed binary, whose failures happen where no host log can see them — **and** `docs/product.md` says the app is operational rather than an experiment |
| L5 | Work runs on a schedule | A rule names a recurring run |
| L6 | A change has to be traceable to the person who made it | Roles — a role may change or delete records another role created; **or** `docs/rules.md` holds approval rules |

- **Report the score as one block, one line per need, each naming its source**: `L1 yes — Roles, CRM reads the lead list` or `L3 no — no timing rules`.
- **A need that scores *no* while the audit found something installed for it gets its own line** — a library nobody needs, or `docs/rules.md` missing a rule the app has been enforcing all along. Report it; fix neither on your own initiative.
- **The block carries one line that is not a need: the data layer folder**, measured by the audit, never asked, and shown with its basis. `logic-build` Section 8, the Step 7 floor, and the session-start listing all scope to it.

| The audit found | The folder |
|---|---|
| One folder holding most of the database calls | That folder, as found. **Never renamed for tidiness** — `src/lib` that works is not improved by becoming `src/data`, and the rename is a diff across every import in the app |
| Calls scattered, no folder holding most | The folder already holding the most, named with its count — the rest are the migration Step 5 prices |
| No database calls yet | The framework's own convention where it names one; else a folder named `data` under the stack's source root, the name the platform architecture guides converge on |

A page or component folder is never the data layer, however many calls it holds — its calls are the migration.

```
Data layer : src/lib — 20 of 20 files already there
```

- **Confirm the block through AskUserQuestion**: the first option accepts the score as read and is the marked recommendation, the second overrides — the lines to flip arrive through the answer or "Other". A yes the user cancels is not asked; a no they raise is; the folder line is overridden through the same dialog.
- **All six score *no* and the audit found nothing installed → jump to Step 7.** The folder and its floor are owed by every app with a database, whatever scored; only an app with no database and no remote API closes at Step 8 from here.

## Steps 3 to 8 — read on arrival

| Step | Read | Runs when |
|---|---|---|
| 3 — Interview · 4 — Record | `references/interview.md` and `references/logic-rubric.md`, plus under `references/` the need file of each need asked: L1 `need-cache.md` · L2 `need-validation.md` · L3 `need-dates.md` · L4 `need-errors.md` · L5 `need-jobs.md` · L6 `need-attribution.md` | A need is asked — only what scored |
| 5 — Install | `references/install.md` | Skipped when every answer was "none" or *keep*, the repo already carries a linter, and no database call sits outside the data layer folder |
| 6 — One pass | `references/pass.md` | Only where something is replaced or moved. Nothing removed and nothing migrated — every need answered "none", *keep*, or a first install onto bare ground, and the data-layer line declined or empty — → skip to Step 7 |
| 7 — The floor · 8 — Close | `references/floor.md` | Step 7 for every app with a database or a remote API; Step 8 always |

## Later needs

A need that surfaces after this session — a screen that suddenly wants caching, a handler appearing where none existed — is **raised to the user, never installed silently** (`logic-build` Section 6). This skill is the only place its question is asked, and re-opening one question does not re-open the interview. Several at once, or a library that is the wrong tool rather than a missing one, re-opens this skill in full, from the Step 1 audit — still the user's to start, never yours.
