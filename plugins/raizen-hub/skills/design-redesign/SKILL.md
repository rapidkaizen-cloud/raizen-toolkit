---
name: design-redesign
description: Rework the visual direction of an app that already has UI. Audits what the code actually uses, decides repair or overhaul, rewrites PRD Section 5, proves it on one reference page, then updates every affected component in one pass. Use when the user wants to redesign, restyle, or overhaul the look of an existing app whose PRD Section 5 is already filled.
---

# design-redesign — reworking the visual direction of an existing app

The difference from `design-init`: there, Section 5 is empty and no component exists. Here both already exist, and that reverses the order of work — **audit first, interview second.**

## Hard limits

A `PRD.md` with a filled Section 5 is an **absolute precondition**. Missing → STOP. Do not write Section 5 from existing code: that reverses the direction `user → PRD → CSS` into `CSS → PRD`, and today's deviations become official norms without anyone ever deciding on them.

Section 5 changes only by **explicit user decision**, line by line. Audit results are findings, not proposed norms.

Two places in the documents may be written, and no third: **PRD Section 5**, and the **Component library row of `CLAUDE.md`** when question 12 is answered with something other than *keep*. Do not create `MASTER.md`, `DESIGN.md`, `design-system/`, or an audit report as a file.

**Keeping everything is a valid ending, not a failure.** Answering *keep* to every question, or reverting after the reference page, closes this skill with the PRD unchanged and the code untouched. Say so plainly and report the audit findings; do not manufacture a change to justify the session.

Do not commit and do not push.

## Step 0 — Preconditions

```
PRD.md        : [present / missing]
Section 5     : [filled / empty / absent]
Branch        : [name · clean or has uncommitted changes]
UI components : [file count]
Flow          : audit → repair or overhaul → [29 questions → Section 5 → reference page] → recap → one pass
```

Section 5 empty → **STOP**, what is needed is `design-init`. `PRD.md` missing entirely → this app did not come from `app-init`; ask for a PRD to be written first, because without Section 5 there is no prior norm to compare against and no direction to protect.

**Working tree not clean → STOP.** The final pass touches every UI file at once; uncommitted changes will drown among them and can no longer be separated. A clean tree is also what makes the reference page revertible with a single `git checkout`.

Branch `main` → STOP. The git guard will refuse it, and that refusal is correct.

## Step 1 — Audit, before asking anything

Read what the code actually uses, not what the PRD says. Report one block:

```
AUDIT
Tokens defined      : [how many colors · text steps · spacing values · radii]
Stray raw values    : [how many hex · font sizes · spacings, across how many files]
Icon families       : [how many, name them]
Fonts loaded        : [from the styling files, not from the PRD]
Component library   : [name and version, from the dependency file]
Repeated labels     : [longest · median · how many repeat per screen]
Supporting text     : [how many paragraphs · the longest in sentences]
Deviates from S5    : [list, per rule broken]
Components affected : [file count that will be touched if tokens change]
```

That last number matters most — it decides the size of the final pass, and the user is entitled to see it before deciding anything.

The **Component library**, **Repeated labels**, and **Supporting text** rows exist because questions 12, 28, and 29 build their options from measured numbers rather than from a database. Measuring them here means the interview never stops to go looking.

A deviation from Section 5 is a **finding**, not a reason to change Section 5. Some of it may need fixing without any redesign at all — offer that as the cheaper path when the audit shows the problem is deviation, not direction.

## Step 2 — Repair or overhaul

One question, two options, with a recommendation:

| Choice | What changes | Questions asked | Components touched |
|---|---|---|---|
| **Repair** | Zero new norms — only bringing code back in line with the existing Section 5 | None | Only the deviating ones |
| **Overhaul** | All of Section 5 is reopened | 29 | One reference page, then the rest |

There is no third option that narrows the scope, because **every question carries a *keep* option** (see Step 3). Answering *keep* to the parts you do not want touched is what narrowing looks like here — scope is narrowed by answers, not by a mode chosen before the user has seen a single question.

**Recommendation:** repair, when the audit shows Section 5 is actually still right and the code is what strayed. Reworking a norm that was never followed solves nothing — it just produces a second norm that is also not followed.

**Consequence:** quote the affected-component count from the audit, and state that overhaul includes question 12, the component library. Answering that one with anything but *keep* rewrites every component whatever the tokens say, and revokes the stack lock recorded in `CLAUDE.md`.

Repair → jump to Step 7. Section 5 is not touched at all.

## Step 3 — Interview, all 29 — Overhaul only

Read `interview.md`, `adaptation.md`, and `anti-pattern.md` in the `references/` folder of `design-init`. The rules are identical: options drawn live from `ui-ux-pro-max`, one question per turn, more than two options, one marked recommendation.

**The order in `interview.md` is followed exactly.** No question is promoted to the front because its consequence is large, and none is deferred because its answer looks settled. A skill that reorders them produces a different interview from `design-init` for the same app, and the two stop being comparable.

Four differences from `design-init`:

**Every question carries a *keep* option, written first.** Labelled `Keep — <the value in Section 5 today>`, and it does not count toward the "more than two options" requirement. A value that is only a recommendation is a suggestion; a value written as an option is a choice. Answering *keep* to all 29 ends the session with the PRD unchanged.

**The old answers are also the starting recommendations.** The current Section 5 was already decided by the user once; treat it as the point of departure, not as a blank page. A recommendation that departs from it must say what changed to justify the departure.

**Question 2 is mandatory** — the app or site that feels right. A redesign always has a reference in the user's head, and drawing it out early cuts rounds at the reference page.

**Questions 28 and 29 build their options from the audit**, not from the database — the numbers measured in Step 1. `interview.md` group H holds the rule.

Fast, foundation, and full modes apply exactly as in `design-init`.

## Step 4 — The new Section 5, as a diff — Overhaul only

Do not show Section 5 in full. Show **only what changes**, old value beside new:

```
Accent color : blue #2563EB  →  green #059669
Text steps   : five          →  four (merge section title and body)
Radius       : 8px           →  0
```

Then **STOP** and wait for approval **line by line**. The user may approve some and reject the rest; rejected lines revert to their old values and do not travel into the pass.

Approved lines are written into Section 5. Rejected ones leave no trace in the PRD.

Nothing changed at all → say so and close at Step 10. That is an outcome, not a failure.

## Step 5 — Install — Overhaul only, and only if question 12 changed

Question 12 answered *keep* → skip this step entirely.

Otherwise, one block, one approval:

```
Will install:
  <new component library>      [from question 12]
  <what the library omits>     [the "Needs extra" column in library-rubric.md]
  <icon pack>                  [from question 13, if it changed]
Will remove:
  <old component library>      [at Step 8, not now — the reference page needs both]
```

Wait for approval. Refused → hand over the commands for the user to run, then wait.

Install nothing outside that block. Something extra turns out to be needed → ask again, do not slip it in.

## Step 6 — Reference page — Overhaul only

**One page, before all the others.** The most data-dense page belonging to the primary role, rebuilt from the new tokens. Not a picture, not a description, and not a new page — the real one, running.

This step exists because an overhaul is otherwise decided from a diff of text lines and then executed across every file at once. A layout that reads correctly as a rule can still collapse as a screen, and the only cheap moment to discover that is before the other files move.

The page is built **in place**. The working tree was clean at Step 0, so `git checkout -- <file>` is the entire revert mechanism; do not create a branch for it.

Show it at desktop width and at the lower bound from question 17, then **STOP** and wait for judgement. Three endings:

| Judgement | What happens |
|---|---|
| **Approve** | Step 7 continues with the remaining files |
| **Rework** | The same page is rebuilt from the new tokens rather than patched. Two rounds at most |
| **Revert** | The file is checked out, Section 5 goes back to its old values, nothing else was touched. The session closes at Step 10 |

A second rework → **STOP, reopen Section 5** and raise the interview mode one level, exactly as `design-init` does. Missing once means the layout was off; missing twice means the visual direction was off, and rebuilding the same page a third time will not fix that.

## Step 7 — Recap before the pass — both paths

Everything approved so far has been a **rule**. This step is the first time the user sees the **files**. Do not skip it because the decisions already feel settled: an approved Section 5 line and the twelve files it moves are not the same information, and only one of the two is reviewable.

Repair:

```
REPAIR — [n] findings
1  Usage.tsx:185-188   rationale on screen     ui-build · Supporting text
   3 sentences  →  removed
2  StatusChip.tsx:19   label 15 chars          S5 · Repeated label length
   "Belum dihubungi"  →  icon only, text to aria-label
```

Overhaul:

```
PASS — [n] files
LeadTable.tsx    radius 8 → 0 · row height 44 → 40 · 2 raw values removed
StatusChip.tsx   4 status colors updated · label to aria-label
index.css        11 tokens replaced · 3 deleted
App.tsx          fixed sidebar → collapsible
UNTOUCHED        Login.tsx, PhoneContact.tsx
```

Then **STOP** and wait for approval **per item**. A rejected item is not silently dropped — it stays a finding and is reported again at Step 10.

A file that should have been listed and is not is a finding, not good news. Report `UNTOUCHED` explicitly rather than letting silence stand for it.

## Step 8 — Rework in one pass

**One session, every approved file.** Not staged, and no old tokens left alive beside the new ones.

The order cannot be reversed:

1. **Tokens first.** The styling files are updated to the new values. Old tokens are **deleted**, not marked deprecated — a deprecated token that still works will still get used.
2. **Then components**, all of them, until zero raw values remain.
3. **Then assets** locked to the old colors: inline SVG, favicon, images carrying brand color.
4. **Then the old library is removed**, if question 12 changed it.

Report per file, matching the Step 7 recap line for line, so the two can be read against each other.

Do not slip in unrelated fixes. A redesign that also tidies logic produces a diff nobody can read, and one mistake will hide among hundreds of legitimate changes.

## Step 9 — Verification, mandatory

Five, all of them before reporting done:

- **The build passes.** It does not → stop, fix it, do not report done.
- **Zero raw values remain.** Search again for hex, font sizes, and raw spacing across every component. Anything left is unfinished work, not an exception.
- **Contrast still passes** the Section 5 target, for every new color pair.
- **The recap matched.** Every file listed at Step 7 changed, and no file outside that list did.
- **The densest page is opened and looked at**, at desktop and at the lower bound. Correct tokens do not guarantee an intact layout.

Any of them fails → fix it in the same session. A half-finished rework is worse than none: the app still runs, so nobody knows it is broken.

## Step 10 — Close

One block: the Section 5 lines that changed · files touched with their count · files `UNTOUCHED` · items the user rejected, still standing as findings · the reference page outcome and how many rework rounds it took · the five verification results · what is still `[needs verification]`.

Nothing changed — every answer was *keep*, or the reference page was reverted → say that in one line and list the audit findings that remain. A session that changes nothing has still produced the audit, and that is worth writing down.

Close by reminding the user that the commit waits for their word, and that a diff of this size deserves a commit of its own, with nothing else riding along inside it.
