---
name: design-rework
description: Rework the visual direction of an app that already has UI. Audits what the code actually uses, decides repair or overhaul, designs every page on a temporary canvas, rewrites PRD Section 5 from the ratified values, then promotes the canvas into the app in one pass. Use when the user wants to redesign, restyle, or overhaul the look of an existing app — whether Section 5 is already filled, or still empty because the repo arrived through `app-rework`'s document mode.
---

# design-rework — reworking the visual direction of an existing app

The difference from `design-init`: there, Section 5 is empty and no component exists. Here components already exist, and that reverses the order of work — **audit first, interview second.**

## Hard limits

A `PRD.md` is an **absolute precondition**. Missing → STOP.

**Section 5 is never written from existing code.** That direction — `CSS → PRD` instead of `user → PRD → CSS` — turns every accident in the stylesheet into an official norm nobody decided on. The audit produces **findings**; a finding becomes a Section 5 line only once the user ratifies it.

Section 5 is normally already filled when this skill runs. One case where it is legitimately empty: a repo that arrived through `app-rework`'s document mode, which writes the PRD for an app that already has UI and deliberately leaves Section 5 unwritten. Step 0 routes it and Step 2b handles it — under the same direction rule, not as an exemption from it.

Section 5 changes only by **explicit user decision**, line by line. Audit results are findings, not proposed norms.

Two places in the documents may be written, and no third: **PRD Section 5**, and the **Component library row of `CLAUDE.md`** when question 12 is answered with something other than *keep*. Do not create `MASTER.md`, `DESIGN.md`, `design-system/`, or an audit report as a file.

**Keeping everything is a valid ending, not a failure.** Answering *keep* to every question, or reverting after the canvas, closes this skill with the PRD unchanged and the code untouched. Say so plainly and report the audit findings; do not manufacture a change to justify the session.

Do not commit and do not push.

## Step 0 — Preconditions

```
PRD.md        : [present / missing]
Section 5     : [filled / empty / absent]
Branch        : [name · clean or has uncommitted changes]
UI components : [file count]
Path          : [rework / ratify — from the routing below]
Flow          : audit → [repair · overhaul · ratify] → recap → one pass
```

`PRD.md` missing → **STOP.** An app with no PRD has no prior intent to protect and nothing to read the audit against. Point to `app-rework` for a repo that already exists, `app-init` for one that does not.

Two readings decide the path, in this order:

| Section 5 | UI components | Path |
|---|---|---|
| Filled | any | **Rework.** Step 2 asks repair or overhaul |
| Empty or absent | none | **STOP** — nothing built, nothing to audit. This is `design-init` |
| Empty or absent | present | **Ratify.** Step 2 is not asked; go to Step 2b |

That third row is the `app-rework` document-mode case: an app whose visual direction was never decided by anyone, only accumulated. It gets the same audit as any other, and then every entry is put to the user before it becomes a norm.

**Working tree not clean → say it and carry on.** Name the dirty paths in one line, and say that committing or stashing them first is what keeps this session's diff separable — the final pass touches every UI file at once, and uncommitted changes drown among them. Advice, not a gate: the user decides, and a refusal here would block a session over paths the pass may never touch.

What it does change is Step 6. A file that was already dirty cannot be reverted with `git checkout`, because that throws the user's work away along with this skill's — carry the dirty list from here to there.

Branch `main` → STOP. The git guard will refuse it, and that refusal is correct.

## Step 1 — Audit, before asking anything

Read what the code actually uses, not what the PRD says. Report one block:

```
AUDIT
Tokens defined      : [how many colors · text steps · spacing values · radii]
Token health        : [how many never read · duplicate roles · library slots unmapped]
Stray raw values    : [how many hex · font sizes · spacings, across how many files]
Unbacked overrides  : [how many · across how many files]
Icons               : [families, named · how many sizes · how many weights]
Fonts loaded        : [from the styling files, not from the PRD]
Component library   : [name and version, from the dependency file]
Repeated labels     : [longest · median · how many repeat per screen]
Supporting text     : [how many paragraphs · the longest in sentences]
Deviates from S5    : [list, per rule broken]
Components affected : [file count that will be touched if tokens change]
```

That last number matters most — it decides the size of the final pass, and the user is entitled to see it before deciding anything.

**While walking the pages, screenshot one page per archetype at desktop width.** Step 9 compares the finished pass against these; without a before, "it looks redesigned" is an assertion nobody can check.

The **Component library** and **Supporting text** rows exist because questions 12 and 29 build their options from measured numbers rather than from a database; **Repeated labels** is measured as findings against the fixed short-label norm (`interview.md` Q28). Measuring them here means the interview never stops to go looking.

**Unbacked overrides** are counted against the `Library defaults` rule in `ui-build`: a component prop, a provider option, or a theme value departing from what the library ships, with no Section 5 line requiring it. They hide from the *stray raw values* row — a `size` or a `variant` is neither a hex nor a spacing — and they are usually the larger of the two numbers. An audit that skips them reports a clean app and sends the user to *repair* with nothing to repair.

**Token health** needs the library's own slot list, read from the installed package rather than remembered. Three numbers: tokens defined but never read, roles sharing one value, and semantic slots the theme file left unmapped. An unmapped slot means the app has been carrying a palette nobody chose, and it surfaces nowhere else in this block.

**An app on a stock Section 5 is the exception**, and Section 5 is read before this row is computed. A repo whose Section 5 adopts the library defaults unmodified has no theme file on purpose: report the row as `n/a — stock` and count no unmapped slots. Every slot there is unmapped by design, and reporting them as findings would push the user to write the very theme file that stock mode exists to refuse. The `Unbacked overrides` row runs the opposite way on the same repo — with no rule in Section 5 for an override to cite, every override counted is unbacked, and that number is the whole reason to audit a stock app.

A deviation from Section 5 is a **finding**, not a reason to change Section 5. Some of it may need fixing without any redesign at all — offer that as the cheaper path when the audit shows the problem is deviation, not direction.

**Section 5 is audited too, not only the code.** Two roles named separately at the same value are one decision written twice, and every later session has to guess which one applies here. That is a finding against the PRD rather than against the code, and merging them is repair work: it changes no visual direction, so it needs no overhaul.

**A page holding too little is not a finding, and not this skill's work.** The audit walks every page, so pages that answer very little are seen here — a screen on correct tokens, correct icons, correct spacing, and still mostly empty. That code breaks no rule. It renders faithfully a content decision nobody ever made, and no styling pass can invent one: what a screen should hold is a product decision belonging to the user.

Do not report it as a deviation, and do not fill it. Hand it to `build-flow` Section 4, which derives candidate content from PRD Sections 2 and 3 and puts it to the user as a proposal — bound items as a statement, optional ones pre-selected to be cut. Name which pages were handed over, and carry on with the audit.

**What is out of scope is the content, not the layout.** In an overhaul the page is not exempt from the pass: its shell and arrangement are rebuilt to its archetype like every other page, using only the content it already has. What stays with `build-flow` is deciding what *else* the page should hold.

**Section 5 without an archetype table is itself a finding** — apps older than the archetype rule have one shell decision and nothing about what pages hold. Derive the table from the routes that exist (grouped as question 18 describes, usually 4–7 archetypes), and present it for ratification the way Step 2b presents measured values: ratify or correct, never adopt silently. A ratified table enters Section 5 at repair scale — it records what the pages already are, no visual direction changes — and every page falling far short of its archetype goes to `build-flow` Section 4 through the hand-over above, one `QUEUE.md` line each. Where the app has no `/styleguide` route, offer generating one as `design-init` Step 6 specifies; the user decides.

## Step 2 — Repair or overhaul

**Ratify path → this step is not asked.** There is no Section 5 to repair against and none to reopen. Go straight to Step 2b.

One question, two options, with a recommendation:

| Choice | What changes | Questions asked | Components touched |
|---|---|---|---|
| **Repair** | Zero new norms — only bringing code back in line with the existing Section 5 | None | Only the deviating ones |
| **Overhaul** | All of Section 5 is reopened, archetype shells included — the app looks redesigned afterwards, not retuned | Full: the keep-first interview (14–15), then the canvas from its answers · Fast: canvas after three keep-first decisions (see `canvas.md`) | Every page, promoted from its canvas file |

There is no third option that narrows the scope, because **every question carries a *keep* option** (see Step 3). Answering *keep* to the parts you do not want touched is what narrowing looks like here — scope is narrowed by answers, not by a mode chosen before the user has seen a single question.

**Recommendation:** repair, when the audit shows Section 5 is actually still right and the code is what strayed. Reworking a norm that was never followed solves nothing — it just produces a second norm that is also not followed.

**Consequence:** quote the affected-component count from the audit, and state that overhaul includes question 12, the component library. Answering that one with anything but *keep* rewrites every component whatever the tokens say, and revokes the stack lock recorded in `CLAUDE.md`.

**State also what overhaul promises: the app looks different afterwards.** Name the pages the audit handed to `build-flow` — their shells will be rebuilt like every other page, but how much they *read* differently is capped until their content proposal lands, and the user hears that before choosing, not after the pass.

Repair → jump to Step 7. Section 5 is not touched, with one exception: two roles the audit found at the same value may be merged, because that removes a duplicate rather than adding a norm. The merge is still an explicit user decision, approved line by line like any other Section 5 change.

## Step 2b — Ratify — ratify path only

Section 5 is empty, so the code has been making these decisions on its own. Walk every entry in `interview.md` once. The audit decides **how** each entry is put to the user, and that is the whole design of this step:

| What Step 1 measured | How the entry is put |
|---|---|
| **A coherent value** — a real scale, one family, a consistent radius | **Confirmation.** Show the measured value; `Ratify — <measured value>` sits first and is the recommendation |
| **Nothing coherent** — scattered raw values, no scale, contradictory usage | **A real question**, asked exactly as `design-init` asks it |

The split is what keeps this honest in both directions. Re-interviewing everything produces answers that contradict the running app, and a PRD that does not describe its own app is worse than no PRD. Ratifying everything writes the stylesheet's accidents into the PRD as norms. Where the code has a real answer the user checks it; where the code has none, nobody may pretend otherwise — offering a "measured value" assembled from noise is inventing a norm and labelling it a finding.

**Batch the confirmations, ask the questions one at a time.** A confirmation carries a measured number and the user is checking it rather than deciding it, so several fit in one call. An entry with no measured basis is an ordinary interview question and keeps the one-per-turn rule from `design-init`.

Every entry goes through the **AskUserQuestion tool** either way, never prose — a prose question at the end of a turn is skipped in auto mode and answered by no one.

**A ratified value is written into Section 5 exactly as measured**, with no tidying on the way in. Rounding a 14px step to 16px because the scale reads nicer is a change of direction disguised as transcription. If it should be 16, that is a question, not a ratification.

An entry the user neither ratifies nor answers → `[needs verification]`. It stays out of the pass and `ui-build` keeps blocking on it. That is the correct outcome: an undecided norm must not become a decided one by default.

### Where the ratify path lands

Decided by the answers, not chosen:

| Outcome | Continue at |
|---|---|
| Every entry ratified as measured | **Step 7, repair.** Section 5 now states what the code already does, so the only work left is the strays the audit found |
| Any entry answered differently from the measurement | **Step 4, overhaul.** Those entries are real changes — they get the old-versus-new diff and the canvas, like any other change of direction |

Nothing else in this skill behaves differently for this path.

## Step 3 — Full or fast, then the canvas — Overhaul only

**Overhaul asks one more question first — full or fast** (`references/canvas.md` of `design-init`). **Full (recommended):** the keep-first interview below runs, and the canvas is then drawn from its answers as the baseline — the canvas may still improvise anywhere, every departure from an answer tagged and confirmed at the judgement. **Fast:** the canvas is drawn straight after the three keep-first decisions, values improvised too. Either way the canvas is built from the installed library and icon pack against the user's feature brief, and its ratified values enter Step 4 as the *new* column of the diff.

**Escalation:** a canvas that misses twice on Fast rises to this interview; on Full, decisions 1–5 are re-asked.

Read `interview.md`, `adaptation.md`, and `anti-pattern.md` in the `references/` folder of `design-init`. The rules are identical: options drawn live from `ui-ux-pro-max`, one question per turn, more than two options, one marked recommendation.

**The order in `interview.md` is followed exactly.** No question is promoted to the front because its consequence is large, and none is deferred because its answer looks settled. A skill that reorders them produces a different interview from `design-init` for the same app, and the two stop being comparable.

Five differences from `design-init`:

**Every question carries a *keep* option, written first.** Labelled `Keep — <the value in Section 5 today>`, and it does not count toward the "more than two options" requirement. A value that is only a recommendation is a suggestion; a value written as an option is a choice. Answering *keep* throughout ends the session with the PRD unchanged.

**Keep stays an option, but it stops being the recommendation.** The user chose overhaul, and that choice already says the current sum is wrong — recommending every current value back re-litigates it, and an overhaul answered by its recommendations then changes nothing. For the look-bearing entries — palette, type, radius, density, shell — the recommendation is a real departure, anchored in the question 2 answer, and it names what it departs from. Question 12 is the one exception: its recommendation stays *keep* unless the audit indicts the library itself, because answering it otherwise rewrites every component for reasons of cost, not of look. Derived decisions derive from the new answers, not from the old Section 5.

**The archetype table is reopened with everything else.** Under the new direction, run the question 18 derivation again and present each archetype old shell beside new for ratification, the way Step 4 diffs a token. This is where an overhaul stops being a repaint: the rooms move, not only the walls. A user who ratifies every shell as it was is told plainly that the pages will read similar afterwards.

**Question 2 is mandatory** — the app or site that feels right. A redesign always has a reference in the user's head, and drawing it out early cuts rounds at the canvas.

**Question 29 builds its options from the audit**, not from the database — the numbers measured in Step 1. `interview.md` group H holds the rule; Q28 is a fixed norm there and is not asked.

Fast and full modes apply exactly as in `design-init`.

## Step 4 — The new Section 5, as a diff — Overhaul only

Do not show Section 5 in full. Show **only what changes**, old value beside new:

```
Accent color : blue #2563EB  →  green #059669
Text steps   : five          →  four (merge section title and body)
Radius       : 8px           →  0
```

Arriving here from Step 2b, the *old* column is the **measured** value and is marked as such — `Radius : 8px (measured) → 0`. There is no prior Section 5 line to diff against, and writing one as if there were would claim a decision nobody ever made.

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
  <old component library>      [at Step 8, not now — the pass needs both]
```

Wait for approval. Refused → hand over the commands for the user to run, then wait.

Install nothing outside that block. Something extra turns out to be needed → ask again, do not slip it in.

## Step 6 — Styleguide first, then the proof lives in the pass — Overhaul only

**The styleguide route comes first, here too.** Write the new tokens to the styling files, then bring `/styleguide` to `design-init` Step 6's spec under the new direction — the route imports production tokens, so most of it follows the theme files by itself; what is updated by hand is the archetype cards to the ratified shells and any component the new direction adds. The user corrects the visual language here, while a correction is one token rather than a rebuilt page. No `/styleguide` route yet → generate it now, same spec.

**There is no reference page — the canvas is the reference, and the pass promotes it** (`canvas.md`): every page was already designed and judged there, in a file named as its real page. The pass walks every page, the most data-dense page of the primary role **first** — each canvas file moved to its real path, the canvas wrapper removed, the real data wired in place of fixtures — and checked at both widths for **survival of real data**. **Holding → report and continue.** The first **collapse → stop**: a rework round of that page, two at most, then Section 5 reopens through the interview fallback — missing twice means the direction was off, and a third rebuild will not fix that.

The page is rebuilt **in place**; do not create a branch for it. How it is reverted depends on what Step 0 read of this particular file:

- **It was clean** → `git checkout -- <file>` is the entire mechanism.
- **It already carried uncommitted changes** → that checkout would delete the user's work together with this skill's, and nothing brings it back. Undo the edits by hand instead, and say which file that applied to.

**Revert of the whole overhaul stays available at the user's word**, at any point: the styling files, `/styleguide`, and the pages already moved go back to their Step 0 state — each by whichever of the two routes above applies — Section 5 goes back to its old values, and the session closes at Step 10.

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

**Pages handed to `build-flow` at Step 1 appear here for their shell only.** The overhaul rebuilds their arrangement like any page's, but adds no content — deciding what belongs on a screen stays with the user. Their content proposal is still named separately, as work waiting on the user; in a repair they do not appear at all.

## Step 8 — Rework in one pass

**One session, every approved file.** Not staged, and no old tokens left alive beside the new ones.

The order cannot be reversed:

1. **Tokens first.** The styling files are updated to the new values. Old tokens are **deleted**, not marked deprecated — a deprecated token that still works will still get used.
2. **Then shells — the most data-dense page of the primary role first**, each page promoted from its canvas file as Step 6 states, carrying the content the page already had — never inventing what it lacks; that stays with `build-flow`. A pass that re-tokens twenty pages inside their old layouts has repainted the app, not redesigned it.
3. **Then components**, all of them, until zero raw values remain and every surviving override can name the Section 5 line behind it. An override with no line goes back to the library default in this same pass; it is not carried forward as a finding to fix later.
4. **Then assets** locked to the old colors: inline SVG, favicon, images carrying brand color.
5. **Then the old library is removed**, if question 12 changed it.

The four styling-file rules in `design-init` Step 4 bind here too: every semantic slot the component library exposes is mapped, a token nothing reads is not written, two roles with the same value collapse into one, and both theme files are written in the same edit. A rework that leaves a slot unmapped hands the app back carrying a neutral palette nobody chose.

**The `/styleguide` route is part of the pass.** When the pass ends it matches the app it describes: archetype cards show the ratified shells and every component the pass created or reshaped renders there — held to `design-init` Step 6's done-check.

Report per file, matching the Step 7 recap line for line, so the two can be read against each other.

Do not slip in unrelated fixes. A redesign that also tidies logic produces a diff nobody can read, and one mistake will hide among hundreds of legitimate changes.

## Step 9 — Verification, mandatory

Seven, all of them before reporting done:

- **The build passes.** It does not → stop, fix it, do not report done.
- **Zero raw values remain.** Search again for hex, font sizes, and raw spacing across every component. Anything left is unfinished work, not an exception.
- **Every surviving override names its line.** Search again for props, provider options, and theme values departing from the library default, and check each against Section 5. The count here must match what the Step 7 recap promised.
- **Contrast still passes** the Section 5 target, for every new color pair.
- **The recap matched.** Every file listed at Step 7 changed, and no file outside that list did.
- **The densest page is opened and looked at**, at desktop and at the lower bound. Correct tokens do not guarantee an intact layout.
- **Every archetype reads redesigned** — overhaul only. Compare one page per archetype against its Step 1 screenshot, side by side. A page that reads unchanged is a failed item of the pass to fix now — unless every entry behind it was answered *keep*, and the recap already said so.

Any of them fails → fix it in the same session. A half-finished rework is worse than none: the app still runs, so nobody knows it is broken.

## Step 10 — Close

One block: the Section 5 lines that changed · files touched with their count · files `UNTOUCHED` · items the user rejected, still standing as findings · the canvas outcome and how many rework rounds it took · the seven verification results · what is still `[needs verification]`.

Nothing changed — every answer was *keep*, or the canvas was reverted → say that in one line and list the audit findings that remain. A session that changes nothing has still produced the audit, and that is worth writing down.

Close by reminding the user that the commit waits for their word, and that a diff of this size deserves a commit of its own, with nothing else riding along inside it.
