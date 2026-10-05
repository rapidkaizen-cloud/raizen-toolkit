---
name: simulate
description: Run the interview of any settle skill — app-settle, logic-settle, design-settle, or the chain of them — for real, against an app repo, a described scenario, or a test scenario this skill proposes, without executing anything — every question asked as the live skill would ask it, and after each answer the decision it produces and where the flow goes next, so the user can see whether the flow lands where their answers meant it to. Skips every printed block and every build step; installs nothing, writes nothing, draws nothing. Runs in the raizen-toolkit repo. Use to check a flow's decisions before running it in an app repo, or to test a skill change by answering its interview end to end.
---

# simulate — the interview for real, the work on paper

What the user cannot see by reading a skill is whether their answers land where they meant them to: which decision a tick records, what it switches on, where the flow goes because of it. This skill runs the interview itself — the same questions, in the same order, with options invented for the target the same way — and after every answer states the decision and the direction. Nothing else runs.

## 0 — Where this runs, and what it touches

**In this repo, against the source under `skills/`, never the installed plugin copy.**

The target is one of three: a real app repo added as a working directory — read-only: `ls`, `grep`, `git log`, reading files; `npx impeccable detect <path>` where the skill would run it — a scenario in words, or **a scenario this skill proposes** (below). A scenario missing what the skill's first step reads (document form, `DESIGN.md`, UI present, platform, kind of app, who uses it, what is installed) is completed in **one** AskUserQuestion before the interview starts.

**Nothing is written, installed, drawn, or run.** No file in the target, no report file here, no `npm install`, no dev server, no canvas. The primary working directory is not this repo → **STOP**.

## 1 — The input

1. **Which skill**, or the chain `app-settle → logic-settle → design-settle`, each skill's decisions feeding the next as the live chain would.
2. **The target** — a repo path, a scenario in words, or none: then this skill proposes one.

### Proposed scenarios

No target, or the user asks for one → offer **three or four test scenarios in one AskUserQuestion**, each a real kind of app with a platform, a primary role, a register, and a repo state — and each chosen to trip a **different set of the skill's switches**, named in its description: *template Next.js admin, no PRD, shadcn installed — trips: reading from code, UI exists, Keep candidate, audit, gate* · *fresh repo after app-settle, no UI — the shortest path* · *a written `DESIGN.md`, 40 components, drift only — trips: fix-or-redesign, findings gate* · *public landing page with a brand hex — trips: first-visit register, brand palette as constraint, no data table*. The recommended one is the scenario covering the switches no earlier simulation in this session has exercised. The picked scenario is written out as the facts the skill's first step reads, shown once, and the interview starts from it. At the close, name the switches this run never tripped and the scenario that would.

## 2 — What is read

The skill's `SKILL.md` and **every** reference it names, whole, from this repo, before the first question. The `raizen-norms` skills a step defers to, where the step reads them. From the target, **only what the live skill would read at that step, in that order** — the router at the audit, not at Step 0; a fact read early produces a question the live run could not have asked, and is a defect of the simulation to report.

Where the skill says *verify live* or *research*, the result is not invented: the option carries `would verify live` and the interview goes on.

## 3 — What is skipped, and what replaces it

| The live skill would | This skill does |
|---|---|
| Print a block — preconditions, audit, frame inventory, close | Skip it. State only the switches it sets, in one line: `UI exists: yes → audit runs, Keep candidate offered, gate at Step 6` |
| Stop in chat on a block the user must read — the install block, the gate | Show the block **reduced to its decision lines** — each line's recommendation and alternatives, the gate's diff and removals — and ask the same approval in chat |
| Report cancellable lines — assumptions, ratified values, derived decisions | List the lines, then one multi-select: *which of these do you want to change?* — a cancelled line opens the dialog the skill defines for it |
| Draw frames, build a canvas, promote pages | Describe, do not draw: each candidate's name, the source it takes after, the axis it explores, the proving page and why, the signature — then ask the pick as the live skill asks it |
| Install, run, verify | State `would run:` in one line and move on |
| Ask a question | **Ask it, for real**, through AskUserQuestion, with the options the skill's own rule produces for this target, labels in the user's words, one marked as the skill marks it |

## 4 — After every answer

One block, short, before the next question:

- **Decision recorded** — what the answer becomes: a `DESIGN.md` line, a decision record, an install line, an anchor, a switch, a `[needs verification]`
- **Switched on / off** — every step, dialog, or check this answer turns on or off, with the condition named as the skill names it
- **Next** — where the flow goes, and why
- **Not fired** — conditionals of this step the target did not trip, with the fact that kept each off, in one line

**Options are invented per target under the skill's own rules** — reference products for this app, engine dialogs only where a trigger fired, frame candidates composed from the direction answer, each naming its source. A simulation that reuses an earlier run's options has tested nothing.

## 5 — The close: did the answers land

At the end, one table: **question · your answer · decision recorded · where it lands**. Then the check the whole run exists for:

- **Matches** — the decision says what the answer meant.
- **Mismatch** — the answer meant one thing and the rule recorded another; the rule is quoted and the gap named. *You ticked a direction but did not stress it, and the canvas was not measured against it — that is the rule, not an error.* *You answered "no charts" and an engine line still appeared — that is a finding.*
- **Undecided** — answers the flow never read, and facts the flow needed that no answer or source supplied.

Findings about the skill itself — a step reference that resolves nowhere, a condition with no behavior, a question with no recommendation, two rules that contradict on this target — are listed apart, each quoting the rule. **No patching**: a change here reaches every app repo on the next version bump, and it is the user's call after reading.

Three lines close the output: what a live run would additionally need (installs, credentials, capture tooling, a committed base, a non-`main` branch) · what could not be simulated (pixels, live verification) · that a live run invents different taste options — the shape was tested, not the content.
