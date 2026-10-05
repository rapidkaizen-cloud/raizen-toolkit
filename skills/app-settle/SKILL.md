---
name: app-settle
description: Settle the app-level decisions of an app of any kind — the problem domain, the stack, and the documents that record them — in the mode the directory decides. Empty — bootstrap a new app, interview, documents, scaffold, git init. Code but no PRD — document it, changing nothing about the app. Code and a PRD — rework its decisions, keep first, every change carrying its cost. Use to start a new app, to document a running app that has no PRD, or to re-plan one that does. Never writes DESIGN.md.
---

# app-settle — the app-level decisions, from nothing or from what exists

`logic-settle` decides the layer between the database and the UI, `design-settle` how the app looks. This skill decides what sits above both — what the app is for, who uses it, the rules it enforces, the stack it runs on — and writes the documents holding it: `docs-format`'s closed list, in the `docs/` form, into every repo it starts or documents. Documents are named by their `docs/` path; a repo with a root `PRD.md` reads each through `docs-format`'s legacy map.

**Three modes, and the directory decides which.** Step 0 reads it; there is no mode to pick and no second skill to route to.

| What the directory holds | Mode | What the session does |
|---|---|---|
| Nothing | **Bootstrap** | Interview the domain and the stack from zero, write `docs/PRD.md`, seed the living documents, scaffold, `git init` |
| Application code, neither `PRD.md` nor `docs/PRD.md` | **Document** | Write the documents — what code can never supply is **why any of it is the way it is**. Change nothing |
| Application code and a root `PRD.md` (legacy form) or `docs/PRD.md` | **Rework** | The user wants the app itself to change: the same interview, every decision starting from what the app already does |

**One session runs one mode, never a mix.** A repo with no PRD is documented first and reworked in a later session, because re-deciding rules never written down loses behaviour.

The user is a junior developer: give a reasoned default, and **ask only what changes the shape of the repo**.

## What a run costs — four rules

- **Read a step's file when the flow reaches that step, never earlier.** The table under The steps names each one; a file for another mode, or for a branch not taken, is never read.
- **Run a step's independent reads, searches and commands in one turn** — parallel calls, or one chained command — because every extra model call re-reads the whole session.
- **Hand non-taste work to one subagent on a cheaper model than the session's** (`sonnet` on Claude Code): the repo read of D1 and R1, the live verification of package candidates, the Pioneer research. Brief it with the file that rules the job and take back only the compact result that file names — its raw results never enter this session. No subagent → run it here and say so; no model choice → the session's model. **Verify a recommendation live before its question is asked; offer every other option from model knowledge, marked `unverified`, and verify it only when picked.**
- **Never re-read what the session start printed** — the documents and the two listings.

## Hard limits — all three modes

**Write only `docs-format`'s closed list.** No `ARCHITECTURE.md`, `SCHEMA.md`, `CHANGELOG.md`, interview summary, or audit report as a file. A document another skill produces in this session is **not committed**.

**`docs/queue.md`, `docs/guide/`, `docs/whats-new.md`, and `docs/changes/` are not born here** — `build-flow` writes them in the building sessions.

**`DESIGN.md` is never written here, nor a legacy PRD's Section 5.** Bootstrap and document mode leave it absent; rework mode leaves it untouched even when the whole point of the rework is a new look. `design-settle` owns it, and until it exists `ui-build` blocks every component — a gate not yet opened, never a hole to fill. Copying today's CSS into it reverses `user → DESIGN.md → CSS` and makes every accident a norm.

**Do not commit and do not push.** `git init` and staging are fine; the commit waits for the user.

**Do not invent.** Not settled yet → write `[needs verification]` in the document.

**No secret goes into any file, and no token is asked for**: name the variable, never its value.

**Run the domain interview alone, without third-party skills.** Another interview skill offering itself in this session (a keyword trigger, for instance) is ignored — its output would collide with the documents, which change only by the user's decision.

**N3, D4 and R4 are one message, then a STOP for explicit approval.** No file is written or edited before it is answered.

**Bootstrap mode only — no `npm install` and no dependency added without the user's approval.**

**Document and rework modes only — nothing about the app itself changes.** No dependency added, none removed, no file refactored, no migration run, no bug fixed on the way past. Decisions land in the documents; code catches up in build sessions under `build-flow`, never here.

## Step 0 — Declare

Check the working directory, the files it holds, and the available skills in one turn, then report one short block:

```
Directory  : [path] — [empty / N files]
PRD        : [absent / root PRD.md — legacy form / docs/PRD.md]
CLAUDE.md  : [absent / present]
AGENTS.md  : [absent / present]
Git        : [branch · N commits]  or  [not a repo]
Mode       : [bootstrap — empty directory]
             [document  — application code, no PRD]
             [rework    — application code and a PRD, naming its form]
Flow       : [bootstrap: story → reading → 6 domain themes → 8 stack questions → summary
                         → docs/PRD.md → living docs → scaffold]
             [document:  read stack → story → reading → 6 themes → summary → docs/PRD.md
                         → living docs + CLAUDE.md]
             [rework:    read documents + stack → drift → story → keep-first decisions
                         → summary → document edits]
```

- **The directory decides the mode, and nothing else does**: "start fresh" in a directory full of code is rework, "fix up" an empty directory is bootstrap. Report the mode with the fact that produced it; the user may overrule it in one line.
- **Not empty, yet read as bootstrap** — files that are neither application code nor a PRD, a stray `README` or a `.git` and nothing else → **STOP**, ask whether to continue here or move. Overwrite nothing.
- **Branch `main` → STOP**: a session never works on `main`.
- **Not a git repo, with code present** → say so, offer `git init`, and continue either way.
- **`docs/PRD.md` present but a living document it seeds missing** → read `references/prd-structure.md`, seed only the missing ones as N4 does, report them, and close; rework waits for a later session.

Then run the mode's own rows of The steps.

## The interview — N1, D2 and D3, R2 and R3

**Open with one invitation to talk freely, never a list of questions.** Then **state your reading in one paragraph and STOP for correction**, because digging on a wrong reading yields answers that are all correct for the wrong app.

| Mode | Invite the user to say | The reading |
|---|---|---|
| Bootstrap | What problem they want solved, who uses it, why this app needs to exist now | *"I read this as [problem] experienced by [who], currently handled by [the old way], with this app replacing [which part]."* |
| Document | What problem this app solves, who uses it, what they did before it existed | *"I read this as [problem] experienced by [who], previously handled by [the old way], with this app now covering [which part]."* |
| Rework | What feels wrong, what triggered the rework, what must be true when it is over | *"I read this as [what hurts] driving changes to [which decisions], with [what] staying as it is."* |

**Bootstrap and document mode then cover six themes, and do not continue without them** — rework walks decisions instead (`references/rework.md`):

- The real problem before this app existed, and why that state was intolerable
- Who uses it, and how they do the work **today** without this app — in document mode, how they did it **before** it
- The work each role must be able to finish, plus the limits that bind them
- Business rules **and the reason behind each number** — not just the value
- Domain terms that are easy to misread
- **Non-goals**: what is deliberately not built, and why that is a decision rather than a gap

Rules of the digging:

- **Never dig for table names, screen names, or folder structure** — they are born from the code and belong in no document.
- **Once the reading is agreed, summarize back what you captured per theme**, then ask what is still empty or ambiguous in one batch, in your own words; only a follow-up whose wording depends on an earlier answer waits for it.
- **Domain questions carry no options** — their answers cannot be enumerated, and a guess offered as a choice steers the answer. "More than two options plus a recommendation" is the rule for technical questions only.
- **Never skip the reason behind a number.** A live check finds the value in a constant or an RLS predicate and never recovers the reason. *"I don't know, it has always been that way"* is a valid answer — write it as-is, never invent or improve one.
- **Stop when the six are answered, not when the questions run out.**

## The steps — read on arrival

| Step | Read | What it runs |
|---|---|---|
| **Bootstrap** · N1 — Domain | Nothing more | The interview above |
| N2 — Stack, eight questions | `references/stack-questions.md` and `references/stack-consequences.md`, in one turn. `references/pioneer.md` only on a Pioneer answer, or a platform typed from outside the list | The questions in batches, then the derived lines and the defaults not asked |
| N3 — Summary, then STOP | Nothing more | One message: app name · Surface/Data/Deploy · roles · key business rules · domain terms · non-goals · stack decisions · rejected alternatives with their reasons |
| N4 — Write `docs/PRD.md`, then seed the living documents · N5 — Scaffold · N6 — Close | After the approval, in one turn: `references/prd-structure.md` (N4) and `references/scaffold.md` (N5, N6) | The frozen PRD and what it seeds, the repo files, `git init`, the close block |
| **Document** · D1 to D6 | `references/document.md`, in the turn that launches D1's subagent on `references/repo-read.md`. After D4's approval, in one turn: `references/prd-structure.md` and `references/scaffold.md` | The stack read from the repo, the interview above, the summary and its STOP, the documents, the close block |
| **Rework** · R1 to R6 | `references/rework.md`, in the turn that launches R1's subagent on `references/repo-read.md`. `references/stack-questions.md` and `references/stack-consequences.md` only when a stack decision opens | The drift, the interview above, keep-first decisions, the summary and its STOP, the document edits, the close block |
