---
name: design-redesign
description: Rework the visual direction of an app that already has UI. Audits what the code actually uses, decides preserve or overhaul, rewrites PRD Section 5, then updates every affected component in one pass. Use when the user wants to redesign, restyle, or overhaul the look of an existing app whose PRD Section 5 is already filled.
---

# design-redesign — reworking the visual direction of an existing app

The difference from `design-init`: there, Section 5 is empty and no component exists. Here both already exist, and that reverses the order of work — **audit first, interview second.**

## Hard limits

A `PRD.md` with a filled Section 5 is an **absolute precondition**. Missing → STOP. Do not write Section 5 from existing code: that reverses the direction `user → PRD → CSS` into `CSS → PRD`, and today's deviations become official norms without anyone ever deciding on them.

Section 5 changes only by **explicit user decision**, line by line. Audit results are findings, not proposed norms.

Section 5 is the only part of the document written. Do not create `MASTER.md`, `DESIGN.md`, `design-system/`, or an audit report as a file.

Do not commit and do not push.

## Step 0 — Preconditions

```
PRD.md        : [present / missing]
Section 5     : [filled / empty / absent]
Branch        : [name · clean or has uncommitted changes]
UI components : [file count]
```

Section 5 empty → **STOP**, what is needed is `design-init`. `PRD.md` missing entirely → this app did not come from `app-init`; ask for a PRD to be written first, because without Section 5 there is no prior norm to compare against and no direction to protect.

**Working tree not clean → STOP.** Step 5 touches every UI file at once; uncommitted changes will drown among them and can no longer be separated.

Branch `main` → STOP. The git guard will refuse it, and that refusal is correct.

## Step 1 — Audit, before asking anything

Read what the code actually uses, not what the PRD says. Report one block:

```
AUDIT
Tokens defined     : [how many colors · text steps · spacing values · radii]
Stray raw values   : [how many hex · font sizes · spacings, across how many files]
Icon families      : [how many, name them]
Fonts loaded       : [from the styling files, not from the PRD]
Deviates from S5   : [list, per rule broken]
Components affected: [file count that will be touched if tokens change]
```

That last number matters most — it decides the size of Step 5, and the user is entitled to see it before deciding anything.

A deviation from Section 5 is a **finding**, not a reason to change Section 5. Some of it may need fixing without any redesign at all — offer that as the cheaper path when the audit shows the problem is deviation, not direction.

## Step 2 — Repair, preserve, or overhaul

One question, three options, with a recommendation:

| Choice | What changes | Components touched |
|---|---|---|
| **Repair** | Zero new norms — only bringing code back in line with the existing Section 5 | Only the deviating ones |
| **Preserve** | Part of Section 5: color, or typography, or density — not all of it | Some |
| **Overhaul** | All of Section 5 | Nearly all |

**Recommendation:** repair, when the audit shows Section 5 is actually still right and the code is what strayed. Reworking a norm that was never followed solves nothing — it just produces a second norm that is also not followed.

**Consequence:** quote the affected-component count from the audit for each choice, not an estimate.

Repair → jump to Step 5, Section 5 is not touched at all.

## Step 3 — Interview, only what changes

Read `interview.md`, `adaptation.md`, and `anti-pattern.md` in the `references/` folder of `design-init`. The rules are identical: options drawn live from `ui-ux-pro-max`, one question per turn, more than two options, one marked recommendation.

Three differences:

**Only the sub-sections chosen in Step 2 are asked.** Preserve color only → questions 3, 4, 5, 6, 7 and nothing else. The rest is neither touched nor asked.

**The old answers become the starting recommendations.** The current Section 5 was already decided by the user once; show it as the point of departure, not as a blank page.

**Question 2 is mandatory in every mode** — the app or site that feels right. A redesign always has a reference in the user's head, and drawing it out early cuts rounds in Step 6.

Fast, foundation, and full modes apply exactly as in `design-init`.

## Step 4 — The new Section 5, as a diff

Do not show Section 5 in full. Show **only what changes**, old value beside new:

```
Accent color : blue #2563EB  →  green #059669
Text steps   : five          →  four (merge section title and body)
Radius       : 8px           →  0
```

Then **STOP** and wait for approval **line by line**. The user may approve some and reject the rest; rejected lines revert to their old values and do not travel into Step 5.

Approved lines are written into Section 5. Rejected ones leave no trace in the PRD.

## Step 5 — Rework in one pass

**One session, every component.** Not staged, and no old tokens left alive beside the new ones.

The order cannot be reversed:

1. **Tokens first.** The styling files are updated to the new values. Old tokens are **deleted**, not marked deprecated — a deprecated token that still works will still get used.
2. **Then components**, all of them, until zero raw values remain.
3. **Then assets** locked to the old colors: inline SVG, favicon, images carrying brand color.

The diff will be large. That is the consequence already chosen, and what keeps it reviewable is **reporting per component, not per line**:

```
Button       : bg-blue-600 → bg-emerald-600 · radius 8 → 0
Card         : radius 8 → 0 · shadow removed
StatusBadge  : 4 status colors updated
DataTable    : new border token
```

Components **not** touched are reported as `UNTOUCHED`. One that should have been touched but was not is a finding, not good news.

Do not slip in unrelated fixes. A redesign that also tidies logic produces a diff nobody can read, and one mistake will hide among hundreds of legitimate changes.

## Step 6 — Verification, mandatory

Four, all of them before reporting done:

- **The build passes.** It does not → stop, fix it, do not report done.
- **Zero raw values remain.** Search again for hex, font sizes, and raw spacing across every component. Anything left is unfinished work, not an exception.
- **Contrast still passes** the Section 5 target, for every new color pair.
- **The densest page is opened and looked at**, at desktop and at mobile width. Correct tokens do not guarantee an intact layout.

Any of them fails → fix it in the same session. A half-finished rework is worse than none: the app still runs, so nobody knows it is broken.

## Step 7 — Close

One block: the Section 5 lines that changed · components touched with their count · components `UNTOUCHED` · the four verification results · what is still `[needs verification]`.

Close by reminding the user that the commit waits for their word, and that this diff touches nearly every UI file — so it deserves a commit of its own, with nothing else riding along inside it.
