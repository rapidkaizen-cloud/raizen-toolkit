---
name: design-rework
description: Rework the visual direction of an app that already has UI. Audits what the code actually uses, decides repair or overhaul, draws every page as final front-end code on a staged canvas, approves everything at one gate, then relocates the canvas files into the app on an isolated branch — the only difference between canvas and production is the data. Use when the user wants to redesign, restyle, or overhaul the look of an existing app — whether Section 5 is already filled, or still empty because the repo arrived through `app-rework`'s document mode.
---

# design-rework — reworking the visual direction of an existing app

The difference from `design-init`: there, Section 5 is empty and no component exists. Here components already exist, and that reverses the order of work — **audit first, interview second.**

## Hard limits

A `PRD.md` is an **absolute precondition**. Missing → STOP.

**Section 5 is never written from existing code.** That direction — `CSS → PRD` instead of `user → PRD → CSS` — turns every accident in the stylesheet into an official norm nobody decided on. The audit produces **findings**; a finding becomes a Section 5 line only once the user ratifies it.

Section 5 is normally already filled when this skill runs. One case where it is legitimately empty: a repo that arrived through `app-rework`'s document mode, which writes the PRD for an app that already has UI and deliberately leaves Section 5 unwritten. Step 0 routes it and Step 2b handles it — under the same direction rule, not as an exemption from it.

**PRD.md is written exactly once, and only after the Step 6 gate approves it** — as the first act of the pass, on the pass's own branch. Until then nothing touches it, and no draft document stands in for it: the canvas is the draft, its variables and foundations board carry every value the user can inspect. Approval writes Section 5 in full; rejection leaves the PRD exactly as it was. Section 5 changes only by **explicit user decision**, line by line — audit results are findings, not proposed norms.

Two places in the documents may be written, and no third: **PRD Section 5**, and the **Component library row of `CLAUDE.md`** when the library question is answered with something other than *keep*. Do not create `MASTER.md`, `DESIGN.md`, `design-system/`, a staging PRD, or an audit report as a file.

**The canvas is the final front-end, staged** (`canvas.md`). Its files are the future pages, written production-grade — the user approves code, not pictures, and promotion relocates that code instead of imitating it. The one legitimate difference between a canvas file and its live page is the data flowing through it; everything else is a failure to fix or a deviation the user has named.

**Two phases, two safety rules.** The canvas phase only adds files under `src/design-canvas/` — it runs safely beside any other session, and no other session touches that folder. The pass rewrites the app — it runs **isolated on its own branch or worktree**, so parallel feature work continues undisturbed in the main tree and reconciliation happens once, visibly, at a merge the user chooses.

**Keeping everything is a valid ending, not a failure.** Answering *keep* to every question, or reverting after the canvas, closes this skill with the PRD unchanged and the code untouched. Say so plainly and report the audit findings; do not manufacture a change to justify the session.

The pass's commit is **proposed at the close, on the pass's own branch** — made only on the user's word. Never push, never merge, never open a PR.

## Step 0 — Preconditions

```
Skill build   : [raizen-hub x.y.z — read from this plugin's own .claude-plugin/plugin.json]
PRD.md        : [present / missing]
Section 5     : [filled / empty / absent]
Platform      : [from Section 1 Surface — web, or the platform named there; a non-web value routes every browser-named check below to that Surface's Proof profile line]
Branch        : [name · clean or has uncommitted changes]
UI components : [file count]
Leftover      : [none / canvas alive / pass applied — from src/design-canvas/ and git state]
Path          : [rework / ratify / re-entry — from the routing below]
Flow          : audit → [repair · overhaul · ratify] → interview → design plan
                (narrated) → install → direction frames + pick, where the direction
                is still open → canvas rounds → gate → pass (isolated) → verify → close
```

**The block is printed on every invocation** — fresh, re-entry, or ratify — before any work beyond the reads that fill it. A session that starts editing, or even auditing, without having shown this block has routed itself in the dark, and everything it concludes about where the flow stands is a private guess the user never saw.

The `Skill build` line exists so a stale install is visible before the pass, not after: rules fixed in the toolkit reach an app repo only through `/plugin update`, and a session on an old build re-makes exactly the mistakes the fix closed. The user sees the version and decides; the skill does not block on it.

**Re-entry is a gate, never an inference.** A leftover from a previous rework — `src/design-canvas/` still present, or a pass already applied on a branch or in the working tree — means this invocation *may* be a continuation, and prior-session summaries or repo state make that likely, not decided. When the `Leftover` line is not `none`, one mandatory AskUserQuestion follows the block, before any other work:

- **Continue** — resume the unfinished flow at the step the state shows: a pass applied but unverified resumes at Step 8; a canvas ratified but not promoted resumes at Step 7; a canvas mid-rounds resumes at Step 5. Announce the resumed step and what remains before touching anything.
- **New rework** — the full flow from Step 1, exactly as a first run: audit, repair-or-overhaul, interview. The leftover canvas is an audit finding; its deletion is proposed at the same chat-stop confirmation Step 8 uses, never assumed.
- **Stop** — report the detected state in one block and close.

A session that skips this dialog and routes itself — because the state "obviously" says where the flow stands — re-makes exactly the mistake this gate exists to close: the user watches edits land without ever having chosen the path.

`PRD.md` missing → **STOP.** An app with no PRD has no prior intent to protect and nothing to read the audit against. Point to `app-rework` for a repo that already exists, `app-init` for one that does not.

Two readings decide the path, in this order:

| Section 5 | UI components | Path |
|---|---|---|
| Filled | any | **Rework.** Step 2 asks repair or overhaul |
| Empty or absent | none | **STOP** — nothing built, nothing to audit. This is `design-init` |
| Empty or absent | present | **Ratify.** Step 2 is not asked; go to Step 2b |

That third row is the `app-rework` document-mode case: an app whose visual direction was never decided by anyone, only accumulated. It gets the same audit as any other, and then every entry is put to the user before it becomes a norm.

**Working tree not clean → say it and carry on.** Name the dirty paths in one line. The pass no longer runs in this tree — it branches from a committed base — so what a dirty tree costs is the base itself: uncommitted work is invisible to the pass's branch, and the promoted app will not carry it until the user commits and the branches meet. Advice, not a gate: the user decides.

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
Fonts loaded        : [from the styling files AND the HTML entry — a family named in CSS
                       but never loaded renders as its fallback, and only this row sees it]
UI stack            : [component library · icon pack · engines — chart, table, date,
                       drag-and-drop — with versions, from the dependency file]
Component library   : [name and version, from the dependency file]
Repeated labels     : [longest · median · how many repeat per screen]
Supporting text     : [how many paragraphs · the longest in sentences]
Deviates from S5    : [list, per rule broken]
Components affected : [file count that will be touched if tokens change]
```

That last number matters most — it decides the size of the final pass, and the user is entitled to see it before deciding anything.

**The `UI stack` row is the canvas's import whitelist** (`canvas.md`, declared stack). A job the brief needs that no installed engine covers becomes an install question at Step 4; an engine installed but unused is a finding.

**The walk may also expose the logic layer bleeding** — handwritten data-fetching in UI files, hand-parsed dates, unvalidated inputs. That is not this skill's work: make the `logic-rework` offer under that skill's own rule — evidence, cost, and recommendation in one AskUserQuestion — and carry on with the audit either way.

**While walking the pages, screenshot one page per archetype at desktop width** — captured per PRD Section 1's Proof profile: the browser for web, the profile's Visual line elsewhere. Step 8 compares the finished pass against these; without a before, "it looks redesigned" is an assertion nobody can check. The screenshots are for that comparison and the judgement's before/after — they are not looked at while the canvas is drawn.

**The same walk writes the function inventory** — every function the app carries, one line each, page-agnostic: what can be done, not where it sits or how it looks. In an overhaul this list is the canvas's brief-floor (`canvas.md`), and collecting it here is what lets the drawing phase keep the old pages closed: the audit is the last time they are opened before the pass.

The **Component library** row exists because the library question builds its options from measured numbers; **Repeated labels** and **Supporting text** are measured so the canvas's copy decisions are judged against real counts rather than guesses (`interview.md`, the designer-settles list). Measuring them here means the interview never stops to go looking.

**Unbacked overrides** are counted against the `Library defaults` rule in `ui-build`: a component prop, a provider option, or a theme value departing from what the library ships, with no Section 5 line requiring it. They hide from the *stray raw values* row — a `size` or a `variant` is neither a hex nor a spacing — and they are usually the larger of the two numbers. An audit that skips them reports a clean app and sends the user to *repair* with nothing to repair.

**Token health** needs the library's own slot list, read from the installed package rather than remembered. Three numbers: tokens defined but never read, roles sharing one value, and semantic slots the theme file left unmapped. An unmapped slot means the app has been carrying a palette nobody chose, and it surfaces nowhere else in this block.

**An app on a stock Section 5 is the exception**, and Section 5 is read before this row is computed. A legacy repo whose Section 5 adopts the library defaults unmodified (a `design-init` mode since retired — `prd-structure.md` holds the shape) has no theme file on purpose: report the row as `n/a — stock` and count no unmapped slots. Every slot there is unmapped by design, and reporting them as findings would push the user to write the very theme file that Section 5 refuses. The `Unbacked overrides` row runs the opposite way on the same repo — with no rule in Section 5 for an override to cite, every override counted is unbacked, and that number is the whole reason to audit such an app.

A deviation from Section 5 is a **finding**, not a reason to change Section 5. Some of it may need fixing without any redesign at all — offer that as the cheaper path when the audit shows the problem is deviation, not direction.

**Section 5 is audited too, not only the code.** Two roles named separately at the same value are one decision written twice, and every later session has to guess which one applies here. That is a finding against the PRD rather than against the code, and merging them is repair work: it changes no visual direction, so it needs no overhaul.

**A page holding too little is not a finding, and not this skill's work.** The audit walks every page, so pages that answer very little are seen here — a screen on correct tokens, correct icons, correct spacing, and still mostly empty. That code breaks no rule. It renders faithfully a content decision nobody ever made, and no styling pass can invent one: what a screen should hold is a product decision belonging to the user.

Do not report it as a deviation, and do not fill it. Hand it to `build-flow` Section 4, which derives candidate content from PRD Sections 2 and 3 and puts it to the user as a proposal — bound items as a statement, optional ones pre-selected to be cut. Name which pages were handed over, and carry on with the audit.

**What is out of scope is the content, not the layout.** In an overhaul the page is not exempt from the pass: its shell and arrangement are rebuilt to its archetype like every other page, using only the content it already has. What stays with `build-flow` is deciding what *else* the page should hold.

**Section 5 without an archetype table is itself a finding** — apps older than the archetype rule have one shell decision and nothing about what pages hold. Derive the table from the routes that exist (grouped as `interview.md`'s archetype rule describes, usually 4–7 archetypes), and present it for ratification the way Step 2b presents measured values: ratify or correct, never adopt silently. A ratified table enters Section 5 at repair scale — it records what the pages already are, no visual direction changes — and every page falling far short of its archetype goes to `build-flow` Section 4 through the hand-over above, one `QUEUE.md` line each. Where the app has no `/styleguide` route, offer generating one as `design-init` Step 6 specifies; the user decides.

## Step 2 — Repair or overhaul

**Ratify path → this step is not asked.** There is no Section 5 to repair against and none to reopen. Go straight to Step 2b.

One question, two options, with a recommendation:

| Choice | What changes | Questions asked | Components touched |
|---|---|---|---|
| **Repair** | Zero new norms — only bringing code back in line with the existing Section 5 | None | Only the deviating ones |
| **Overhaul** | **Section 5 is rebuilt from zero, as `design-init` would write it** — every line re-decided, archetype shells and visual-direction prose included; today's values survive only as *keep* answers. The app looks redesigned afterwards, not retuned | The taste batch with a keep option per slot (one turn), the stack questions, then the canvas from its answers (see `canvas.md`) | Every page, replaced by its canvas file |

There is no third option that narrows the scope, because **every question carries a *keep* option** (see Step 3). Answering *keep* to the parts you do not want touched is what narrowing looks like here — scope is narrowed by answers, not by a mode chosen before the user has seen a single question.

**Recommendation:** repair, when the audit shows Section 5 is actually still right and the code is what strayed. Reworking a norm that was never followed solves nothing — it just produces a second norm that is also not followed.

**Consequence:** quote the affected-component count from the audit, and state that overhaul includes the component-library question. Answering that one with anything but *keep* rewrites every component whatever the tokens say, and revokes the stack lock recorded in `CLAUDE.md`.

**State also what overhaul promises: the app looks different afterwards.** Name the pages the audit handed to `build-flow` — their shells will be rebuilt like every other page, but how much they *read* differently is capped until their content proposal lands, and the user hears that before choosing, not after the pass.

Repair → jump to Step 6; the gate there shows the findings instead of a canvas. Section 5 is not touched, with one exception: two roles the audit found at the same value may be merged, because that removes a duplicate rather than adding a norm. The merge is still an explicit user decision, approved line by line like any other Section 5 change.

## Step 2b — Ratify — ratify path only

Section 5 is empty, so the code has been making these decisions on its own. Walk every entry in `interview.md` once — the taste slots, the stack questions, and the derived values its designer-settles list names. The audit decides **how** each entry is put to the user, and that is the whole design of this step:

| What Step 1 measured | How the entry is put |
|---|---|
| **A coherent value** — a real scale, one family, a consistent radius | **Confirmation.** Show the measured value; first and recommended is an option naming the action plainly — `Keep this value — 8px` — never this file's vocabulary |
| **Nothing coherent** — scattered raw values, no scale, contradictory usage | **A real question**, asked exactly as `design-init` asks it |

The split is what keeps this honest in both directions. Re-interviewing everything produces answers that contradict the running app, and a PRD that does not describe its own app is worse than no PRD. Ratifying everything writes the stylesheet's accidents into the PRD as norms. Where the code has a real answer the user checks it; where the code has none, nobody may pretend otherwise — offering a "measured value" assembled from noise is inventing a norm and labelling it a finding.

**Batch the confirmations and batch the questions.** A confirmation carries a measured number and the user is checking it rather than deciding it, so several fit in one call. An entry with no measured basis is an ordinary interview question — grouped with its peers in one call (taste entries with the taste batch, stack entries with the stack batch), sequential only across a real dependency.

Every entry goes through the **AskUserQuestion tool** either way, never prose — a prose question at the end of a turn is skipped in auto mode and answered by no one.

**A ratified value is written into Section 5 exactly as measured**, with no tidying on the way in. Rounding a 14px step to 16px because the scale reads nicer is a change of direction disguised as transcription. If it should be 16, that is a question, not a ratification.

An entry the user neither ratifies nor answers → `[needs verification]`. It stays out of the pass and `ui-build` keeps blocking on it. That is the correct outcome: an undecided norm must not become a decided one by default.

### Where the ratify path lands

Decided by the answers, not chosen:

| Outcome | Continue at |
|---|---|
| Every entry ratified as measured | **Step 6, as repair.** Section 5 now states what the code already does, so the only work left is the strays the audit found |
| Any entry answered differently from the measurement | **Step 3, overhaul.** Those entries are real changes — they get the old-versus-new diff and the canvas, like any other change of direction |

Nothing else in this skill behaves differently for this path.

## Step 3 — The interview — Overhaul only

**Load `design-init`'s `references/taste.md` and `frontend-design` first, before a single option is written** — same reason as there: the batch's options are the first place taste is exercised, and options written out of the defaults are a menu the user can only pick from. On this path the pull toward the defaults is stronger, not weaker: the audit has just filled the session with the app's current values, and every one of them is a default asking to be offered back.

Read `interview.md` in the `references/` folder of `design-init`. The rules are identical: the taste batch's eight slots in one turn — reference first, its options real products named by you — options invented for this app from the model's own design knowledge, every slot carrying "Decide for me", one marked recommendation per slot — then the stack questions, their candidates verified per `library-rubric.md` and `engine-rubric.md`. The canvas is drawn from the answers as the baseline and may still improvise anywhere, every departure from an answer tagged and confirmed at the judgement; its ratified values enter Step 6 as the *new* column of the diff.

**Escalation:** a canvas that misses twice re-opens the taste batch with sharpened options (`canvas.md`).

**Engine dialogs fire on triggers, never on a schedule** (`engine-rubric.md` of `design-init`): a need the user or the PRD names, a job the product draft implies, or an engine the audit indicts. An installed engine is already decided — it is the declared stack, and no dialog re-opens it without an indictment. Swapping one rewrites every page that uses it, so it is priced and recommended the way the library question is — *keep* first, and keep stays the recommendation unless the indictment stands. A need that only emerges mid-canvas is drawn tagged with the no-engine rendering and settled at the judgement, per the rubric.

Six differences from `design-init`:

**Every slot and stack dialog carries a *keep* option, written first.** Labelled `Keep — <the value in Section 5 today>`, and it does not replace the invented options the slot must still offer. A value that is only a recommendation is a suggestion; a value written as an option is a choice. Answering *keep* throughout ends the session with the PRD unchanged. A derived value defaults to the value Section 5 holds today, reported on its line — cancelling it opens a dialog with the same keep option first.

**Keep stays an option, but it stops being the recommendation.** The user chose overhaul, and that choice already says the current sum is wrong — recommending every current value back re-litigates it, and an overhaul answered by its recommendations then changes nothing. For the look-bearing slots — direction, palette, surface, density, typography, shell — the recommendation is a real departure, anchored in the reference the user named or the chosen direction, and it names what it departs from. **And the canvas that follows draws blind to the current look** — `canvas.md`'s full-overhaul rule: today's design is not an input, **Section 5's own prose included** — its signature, ornament rules, and shell column bind the canvas no more than the CSS does; only the brief and the answers are inputs. The audit's numbers price the pass and power the before/after, never anchor the new direction. The library question is the one exception: its recommendation stays *keep* unless the audit indicts the library itself, because answering it otherwise rewrites every component for reasons of cost, not of look. Derived decisions derive from the new answers, not from the old Section 5 — `interview.md` states the same split, and an overhaul that reads old values into its derivations has re-imported the design it was told to leave outside.

**The new Section 5 is rebuilt from zero, not patched.** Every line of it traces to the same three sources `design-init` names: a new answer, a derived decision reported to the user, or a canvas value the user ratified. A line of the old Section 5 that none of the three re-created — a signature paragraph, an ornament rule, a reference-app list — does not carry over by default: it survives only through a *keep* answer or a canvas re-ratification, and otherwise it appears in the Step 6 diff as a removal. Silent carry-over is the mechanism by which an overhaul stays caged by its predecessor, and one ratified sentence is enough bars.

**The archetype table is reopened with everything else.** Under the new direction, run the archetype derivation again and present each archetype old shell beside new for ratification, the way Step 6 diffs a token. This is where an overhaul stops being a repaint: the rooms move, not only the walls. A user who ratifies every shell as it was is told plainly that the pages will read similar afterwards.

**A reference is drawn out, not waited for — and here it has its own slot.** A redesign always has a reference in the user's head, so the taste batch's first question asks for it directly, with real products as options rather than an invitation buried in the lead text (`interview.md`, the reference slot). Where Section 5 already records one, it takes the first place as `Keep — <it>`; where it does not, the audit's own reading of what this app was reaching for is what the proposed products are argued from. A named answer becomes the anchor the canvas designs toward and the list the canvas is measured against at the judgement — drawing it out here is what cuts rounds later.

## Step 4 — Install, before anything is drawn — Overhaul only

The canvas is built from real packages, so everything it will draw with exists **before** the first file is written (`canvas.md`). One block, one approval — answered in chat at a hard stop, never an AskUserQuestion (a dialog covers the block being read):

```
Will install:
  <component library>   [the library answer — only if it changed]
  <icon pack>           [its icon dialog — only if it changed]
  <engines>             [chart · table · date · drag-and-drop — newly chosen, or
                         needed by the brief and missing from the UI stack row]
  <fonts>               [only if the type answer changed them — say how they load]
Will remove:
  <old library · old engines>   [at the end of the pass, not now — the pass needs both]
```

Nothing to install → say so in one line and continue; a complete stack never stops this step. Refused → hand over the commands for the user to run, then wait. Install nothing outside that block — something extra turns out to be needed → ask again, do not slip it in.

## Step 5 — The canvas: rounds until final — Overhaul only

Drawn and judged under `canvas.md` entire: the direction frames first where the direction is still open, then files written production-grade — every state drawn, fixtures in one contract-shaped file that closes arithmetically, imports only from the declared stack — the three-scan self-check before every round (imports · the render · the arithmetic), the signature drawn and tagged, tagged departures and proposals, the judgement through AskUserQuestion, two rounds then escalation. The design plan is narrated before drawing here too, under `design-init` Step 3 — after the pick where frames ran; `references/taste.md` and `frontend-design` have been in hand since Step 3's interview. **Frames rarely run on this path**: every slot here carries `Keep — <today's value>` and the look-bearing slots carry a real departure as the recommendation, so a Direction left at "Decide for me" is the exception rather than the norm.

**The PRD is not touched during rounds, and neither is any production file.** The foundations board is the living draft of every value; the user inspects it there, not in a document. The `/styleguide` route keeps rendering the old theme until the pass — the canvas never looks at it.

This phase only adds files under `src/design-canvas/`, so it runs safely beside any other session — days may pass between rounds without holding anything else up.

## Step 6 — The gate: one approval before anything real changes — both paths

Everything so far has been drawing and answers. This is the **single stop** where the user authorizes the change — Section 5, the file plan, and the known deviations together, because approving pixels is not the same as approving which files move.

**Overhaul** — one message, three parts, then a hard stop answered in chat — never an AskUserQuestion:

1. **Section 5 as a diff.** Only what changes, old value beside new — and removals are changes:

```
Accent color : blue #2563EB  →  green #059669
Text steps   : five          →  four (merge section title and body)
Radius       : 8px           →  0
Signature    : ledger seam, sole vertical rule  →  removed
```

A line of the old Section 5 that no new answer, derivation, or canvas ratification re-created leaves through this diff as `→ removed`, never by omission. Arriving here from Step 2b, the *old* column is the **measured** value and is marked as such — `Radius : 8px (measured) → 0`; there is no prior Section 5 line to diff against, and writing one as if there were would claim a decision nobody ever made.

2. **The file plan.** Every page line names its source: `replaced by its canvas file`, or `retoken only — no canvas frame` (a stray component the canvas never drew). There is no third label. **Shared canvas files carry their own line under the production path their header names** — a plan that lists only pages leaves the largest promotions unwatched, and a composition promoted as loose parts downgrades every page built on it. The plan closes with its **seam points** — where the pass may stop between sessions, read off Step 7's fixed order rather than chosen, and never an estimate of time: what the user needs before approving is where the app will sit half-migrated, not how long it takes. A page whose canvas file exists is replaced by it; listing it `retoken only` is proposing to break the ratified canvas, and that line is put to the user as its own question, never slipped through inside the list. Chrome and shared components created or replaced, styling files, and `UNTOUCHED` files are all listed — a file that should have been listed and is not is a finding, not good news.

```
PASS — [n] files
LeadTable.tsx    replaced by its canvas file
wizard.tsx       → src/components/import-wizard.tsx · shared by 7 pages · replaced by its canvas file
StatusChip.tsx   retoken only — no canvas frame · 4 status colors updated
index.css        11 tokens replaced · 3 deleted · fonts now load here
App.tsx          replaced by its canvas file (chrome)
UNTOUCHED        PhoneContact.tsx
```

3. **What approval orders, then what it contradicts.** Ratified elements whose data does not exist yet come first, one line each — element, page, and the work it orders (column · RPC · migration). **Approving the gate orders that work**, so its cost is read here rather than discovered mid-pass; these are not deviations, because the user has decided to build them. Then the deviations: every canvas element the real flow contradicts, and every real control the canvas never drew (`canvas.md`'s canvas-error rule) — one decision line each, answered here, never absorbed silently. **And what approval removes is its own group, confirmed item by item** — every function or control leaving the app because the canvas does not carry it. A blanket *approve everything* covers the other two groups; not this one. A wrong addition is visible on the screen the moment the page opens, and a wrong removal is visible to nobody.

**The gate is a chat stop, not a dialog.** End the turn on the three-part message and wait for the user's reply in chat. An AskUserQuestion here covers the very summary being approved — the user answers the dialog without having read the diff. Ending the turn is what keeps this safe in auto mode: nothing proceeds without an answer. The ban on prose questions elsewhere in this skill covers questions that let the turn carry on, not a gate that stops it.

The user may approve some lines and reject others, naming them in the reply. Rejected values return to the canvas rounds (Step 5) and nothing is written anywhere; approved everything → the pass. Nothing changed at all → say so and close at Step 9.

**Repair** — the same gate shows the findings list instead:

```
REPAIR — [n] findings
1  Usage.tsx:185-188   rationale on screen     ui-build · Supporting text
   3 sentences  →  removed
2  StatusChip.tsx:19   label 15 chars          S5 · Repeated label length
   "Belum dihubungi"  →  icon only, text to aria-label
```

STOP and wait for approval per item. A rejected item is not silently dropped — it stays a finding and is reported again at Step 9.

## Step 7 — The pass: isolated, one session

**Branch first.** Create the pass's own branch or worktree from a committed base (`design/rework-<date>` or the user's naming). Parallel work continues in the main tree untouched; the canvas folder, if untracked, is brought along into the worktree. Revert of the whole overhaul is now one move — drop the branch — available at the user's word at any point, closing the session at Step 9.

**First act: write Section 5** — the approved text, in full, rebuilt from zero. Then `CLAUDE.md`'s Component library row if the library answer changed. This is the only moment the PRD is written.

**The gate block travels with the branch.** The pass's first commit carries it in its message body — Section 5 diff, file plan, ordered work, and the deviations the user answered. Chat scrollback does not survive the session, and a later session that cannot read what was approved cannot tell drift from a decision; neither can the user. `git log` is where this repo already keeps that kind of memory.

**Second act: the freshness check.** Time may have passed between ratification and this session, and parallel work may have changed the app. Re-walk the function inventory against the current code; a flow that changed since the canvas was ratified is a new deviation line, put to the user **before** its page moves — the canvas is frozen, so reality has to win by decision, not by silence.

Then one session, every approved file, in an order that cannot be reversed:

1. **Foundations.** The theme files take the new token values — old tokens **deleted**, not deprecated — and everything the canvas CSS carries beyond values lands with them: **the font loading itself** (link or package — then verify in the browser that the computed font-family resolves to the loaded webfont, not a fallback; a token grep cannot see a font that never loads), element-level rules, shadows, motion durations. The five styling-file rules in `design-init` Step 6 bind here too: the two-layer palette the canvas ratified, every semantic slot mapped, no unread tokens, duplicate roles collapsed, both theme files in the same edit.
2. **Chrome and shared components, from the canvas chrome.** Each shared component a canvas page imports lives in the production chrome before any page importing it counts as moved — the canvas markup is the component; the production logic (auth, navigation state, data) is wired into it, never the reverse.
3. **Pages — the most data-dense page of the primary role first.** Each canvas file **copied to its real path**, the canvas wrapper removed, the fixture import swapped for the real data layer. The markup body does not change — that is what Step 8 will diff. Checked at both widths for survival of real data: holding → report and continue; the first collapse → stop, a rework round of that page, two at most, then Section 5 reopens through `canvas.md`'s escalation.
4. **Components not on the canvas** — retoken only, until zero raw values remain and every surviving override names its Section 5 line. An override with no line goes back to the library default in this same pass.
5. **`/styleguide`** — part of the pass: archetype cards updated to the ratified shells, every component the pass created rendering there, held to `design-init` Step 6's done-check.
6. **Assets** locked to the old colors: inline SVG, favicon, images carrying brand color.
7. **The old library and engines are removed**, if their decisions changed.

**The UI code is the pass's to rewrite — the behavior is not.** What must come out unchanged is the business behavior — the queries and mutations called, the guard conditions, the route paths, the outcome of every action a user can take. Do not slip in unrelated fixes: a redesign that also tidies logic produces a diff nobody can read, and one mistake will hide among hundreds of legitimate changes.

**The approved canvas is the specification, and the pass implements it rather than negotiating with it.** An element the canvas drew lands as drawn; an element it did not draw does not land, and prose the canvas left out is deleted rather than carried over — the user answered that by approving the drawing, so asking again re-opens a settled decision and is how the result drifts. A difference the session would prefer is refused, not raised as a question.

**One exception, and no other: an element the user ratified whose data does not exist yet.** The pass writes no query for it — that stays forbidden. It promotes the element **rendered empty and labelled as waiting**, and writes one `QUEUE.md` line naming the data it needs. Dropping it silently is a failed promotion, and so is hiding it behind a flag: a page that reads finished while an approved element is missing is the one state nobody can see.

**One thing still stops the pass**, and it is the freshness check above plus this: a drawn element that would make the app claim what it cannot do. That is a `build-flow` stop, not a design question.

**Repair** runs here too, on the same isolated branch: fix the approved findings, nothing else.

## Step 8 — Verification: evidence, not eyes

A claim of parity from the session that produced the code is worth nothing on its own — every check below leaves something the user can inspect. All of them before reporting done:

- **The build passes.** It does not → stop, fix it, do not report done.
- **The structural diff per canvas file — the primary evidence.** Every canvas file, not every promoted page: a page whose body delegates to a shared file diffs empty, and the diff that matters moves to that shared file, under the production path its header names. The differences must be confined to the data seam — the fixture import swapped for the data layer, plus its loading and error wiring — and to lines the user answered at the gate. Any other difference is a failed item to fix now, whichever side reads better. Report the verdict per file; a file whose diff cannot be shown is not verified.
- **Computed styles probed in the browser.** The fonts resolve to the loaded webfonts, not a fallback stack; spot-check token slots on live surfaces against the theme files. (The web profile's check — a platform whose Proof profile names no browser verifies the equivalent through its Visual line, and says what could not be verified.)
- **The rendered structure matches, counted.** Both sides are live in the same dev server — the canvas at its dev route, the page at its real one. Read the element tree of each page body (element names and class lists, **text and numbers discarded** — discarding the text is what takes the data out of the comparison) and report one line per page: `canvas n · live n · differs n`. Anything above zero names the extra or missing elements and is a failed item now. "Richer than the canvas" is drift wearing a compliment, and this count is what sees it — the prose verdict this bullet used to carry did not. Chrome the two sides do not share is excluded and said so; a page whose count cannot be produced is not verified.
- **Zero raw values remain.** Search again for hex, font sizes, and raw spacing across every component.
- **Every surviving override names its line.** Search again for props, provider options, and theme values departing from the library default, and check each against Section 5. The count must match what the Step 6 file plan promised.
- **Contrast still passes** the Section 5 target, for every new color pair — the ratio **computed**, never recalled, per `canvas.md`'s Ratification, and every semantic dark shade clearing 4.5 against its own light shade.
- **The fixtures close** on any page still running on them, and the `/styleguide` foundations render as specimens rather than as a table of names and values — `design-init` Step 6's done-check, which this pass's styleguide is generated to.
- **The signature survived promotion**, on the pages that carry it. A signature that exists on the canvas and not in the app is a failed item, not a simplification.
- **The file plan matched.** Every file listed at Step 6 changed, and no file outside that list did.
- **The seeded walk.** Seed `[CLAUDE]`-prefixed rows first — an empty database renders empty states the canvas never drew, and a parity claim over empty tables is void. Then walk the densest page at desktop and at the lower bound, and compare one page per archetype against its Step 1 screenshot: every archetype reads redesigned, unless everything behind it was answered *keep* and the gate said so.
- **Function parity holds.** Walk the Step 1 function inventory line by line: every function is still reachable **at both widths — a control hidden below the breakpoint is a missing function at the minimum width, not a responsive choice** — wherever it now lives. A line missing everywhere is a failed item to fix now, unless the user cut it at the judgement and the gate said so.

Any of them fails → fix it in the same session. A half-finished rework is worse than none: the app still runs, so nobody knows it is broken.

**All of them passing earns the right to propose deletion — never to delete.** The canvas is removed only through an explicit confirmation at a chat stop — never an AskUserQuestion, which would cover the verdict being read: report the diff verdict per page, invite the user to walk canvas and app side by side at `/design-canvas`, then end the turn and ask whether the canvas and the seed rows may go. Only a granted confirmation deletes — the page files, the entry route, the foundations board, and the canvas CSS together, per `canvas.md`'s lifecycle. The user refusing, or naming any page, turns each named page into a failed item of the pass to fix now; the canvas stays alive until a later confirmation clears it.

## Step 9 — Close

One block: the Section 5 lines that changed · files touched with their count · files `UNTOUCHED` · items the user rejected, still standing as findings · the canvas outcome and how many rework rounds it took · the verification results, the per-page diff verdicts included · what is still `[needs verification]`.

**A pass this session could not finish is written down, not implied.** Every page not yet promoted, and every verification item not yet passing, becomes a `QUEUE.md` line — one each. A truncated pass must read as unfinished in the repo itself; the canvas stays alive as the reference until those lines clear.

**Propose the commit, on the pass's own branch** — a diff of this size deserves a commit of its own, with nothing else riding along inside it. The commit waits for the user's word; merging the branch back is also the user's move, and it is the single point where this work meets whatever parallel sessions built in the meantime. Never push, never open a PR.

Nothing changed — every answer was *keep*, or the canvas was reverted → say that in one line and list the audit findings that remain. A session that changes nothing has still produced the audit, and that is worth writing down.
