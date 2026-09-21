---
name: design-settle
description: Settle the visual direction and component library of an app, with or without existing UI. Two facts switch steps on or off — whether UI components exist (then the code is audited and today's look is one candidate) and whether PRD Section 5 is filled (then fixing only the drift is offered). Flow — the reading; non-visual dialogs that only lock answers; a search for real products and one multi-select direction question; one install gate; 2-4 direction frames drawn with the real packages and picked on screen; an in-repo canvas of every page in production-grade code, judged in the browser, approved at one gate, then promoted into the app. Use before the first UI component of a repo is written, and whenever the user wants to redesign, restyle, or overhaul the look of an app that already has one.
---

# design-settle — the visual direction, from nothing or from what exists

`app-settle` writes the PRD, `logic-settle` the layer under the UI. This skill decides how the app looks, and it is the only skill allowed to write **PRD Section 5**.

**One skill, one path, two facts.** There is no mode. Step 0 reads whether **UI components exist** and whether **Section 5 is filled**; every step says what it does under each.

| UI components | Section 5 | What switches on |
|---|---|---|
| none | empty | The shortest path: reading → interview → frames → canvas → ratify → promote in place → verify |
| present | empty | The audit, the function and frame inventories, `Keep — today's look` as one candidate, the gate before any real page moves, the pass on its own branch, parity checks |
| present | filled | All of the above, plus the fix-or-redesign question before the interview and the Section 5 diff at the gate |
| none | filled | STOP — ask whether the user really means to redesign an app whose UI was removed, and treat the answer as the row above |

Steps are marked *UI exists* or *Section 5 filled*; an unmarked step runs identically for every repo.

## Hard limits

**The confirmed reading is the precondition, not the PRD.** A missing or off-shape `PRD.md` does not stop this skill, but **nothing is asked about the look and nothing is drawn until the user has confirmed the Step 1 reading**.

**Section 5 is never written from existing code.** The audit produces **findings**; a finding becomes a Section 5 line only once the user ratifies it. Section 5 changes only by **explicit user decision**, line by line.

**Section 5 is written once, and never before its stop** — at Step 6 where no UI exists; where UI exists, only after the Step 6 gate approves, as the pass's first act on its own branch. No draft document stands in for it. Rejection leaves the PRD exactly as it was.

Four places may be written, and no fifth: **PRD Section 5**; the **Component library row of `CLAUDE.md`** when the library answer is not *keep*; the **generated `DESIGN.md`** of Step 6 — tokens derived from ratified Section 5, never a decision of its own, never hand-edited; and the **`## UI` part of `AGENTS.md`** — paths and a command, never a value. Do not create `MASTER.md`, `design-system/`, a staging PRD, an audit report as a file, or a `DESIGN.md` written from code. A document another skill produces in this session is not committed and not referenced.

**The canvas is the final front-end, staged** (`references/canvas.md`): production-grade files that promotion relocates, differing from the live page only in data. The canvas phase only adds files under `src/design-canvas/`, and no other session touches that folder; where UI exists the pass runs **isolated on its own branch or worktree**, otherwise in place.

**Keeping everything is a valid ending.** All *keep*, `Keep — today's look`, or a revert closes with the code untouched and the PRD unchanged — except that Keep with an empty Section 5 writes the ratified measured values (Step 6); say so, report the findings, manufacture no change.

**A code-minimizing session mode governs the how, never the what.** Write every file lean, but such a mode never removes, as explicitly requested: the full product draft with its proposals tagged, every state drawn, the fixtures file that closes, the two-layer palette and the component-token table, the `/styleguide` route, the compare page, the signature, and every engine or library approved at the install gate, used where it covers the job.

Do not commit (staging is fine; a branch pass's commit is **proposed at the close, on that branch**). Never push, merge, or open a PR.

**What the session does not know with confidence is researched with WebSearch, never recalled and never written into this toolkit** — platform guidelines, a package's current API or version, a product's current screens, a standard's wording — at the step that needs it, source named. **A search tool the harness defers is loaded before use** — unavailable means the load itself failed, never that the name was absent from the tool list. WebSearch unavailable → say so and mark the finding unverified.

Not decided by the user → `[needs verification]`.

## Step 0 — Preconditions

```
Skill build     : [raizen-hub x.y.z — read from this plugin's own .claude-plugin/plugin.json]
PRD.md          : [present / missing / present, outside prd-structure's shape]
Section 5       : [filled / empty / absent / product without UI]
UI components   : [file count — 0 on a repo with no UI]
Kind of app     : [from Section 1, else read from the code, else asked at Step 1 — a label, never a branch]
Register        : [first visit / tenth use / both, per page group — from Section 2, else from the routes]
Platform        : [from Section 1 Surface, else from the manifest and platform files — web, or the
                   platform found; a non-web value routes every browser-named check below to that
                   Surface's Proof profile line, or to the platform's own tooling where none is written]
Primary role    : [from Section 2, else from the roles the code enforces, else asked at Step 1]
Design material : [impeccable present/absent · frontend-design present/absent — both Required]
Branch          : [name · clean or has uncommitted changes]
Leftover        : [none / canvas alive / pass applied — from src/design-canvas/ and git state]
Switches        : [UI exists: yes/no · Section 5 filled: yes/no]
Reading         : [one sentence — see Step 1]
Flow            : load impeccable + frontend-design → reading (+ audit, in a subagent, where UI exists)
                  → fix or redesign (where Section 5 filled)
                  → non-visual dialogs, answers locked, nothing installed (library · styling ·
                  icons · engines · widths · theme mode · frame screens · copy voice)
                  → reference search (real products, links) → direction question, multi-select
                  → install gate → direction frames composed by Claude, always 2–4, today's
                  look among them where Keep is ticked → pick → refine (only if the pick
                  carries a change)
                  → design plan → canvas rounds → ratify (+ gate where UI exists)
                  → pass (in place, or on its own branch where UI exists) → verify → close
```

**Print the block on every invocation** before any work beyond the reads that fill it. A `Design material` absence is asked right after the block, under Step 1's rule; a stale `Skill build` is shown, not blocked on.

**Re-entry is a gate, never an inference.** When `Leftover` is not `none`, one mandatory AskUserQuestion follows the block, before any other work, however obvious the state looks:

- **Continue** — resume at the step the state shows: pass applied but unverified → Step 8; canvas ratified but not promoted → Step 7; canvas mid-rounds → Step 5; frames drawn but not picked → the pick. Announce the resumed step and what remains before touching anything.
- **Start over** — the full path from Step 1. The leftover canvas is an audit finding; its deletion is proposed at Step 8's chat-stop confirmation, never assumed.
- **Stop** — report the detected state in one block and close.

`PRD.md` missing or off-shape → **not a stop**: say so in the block, read around it as Step 1 describes, and name at the close what `app-settle` still owes. Product without UI → **STOP**, this skill does not apply. Branch `main` → **STOP**. **Working tree not clean, where UI exists → name the dirty paths in one line and carry on**, noting uncommitted work will not reach the pass's branch until committed. Advice, not a gate.

## Step 1 — The reading, and the audit where UI exists

**Load `impeccable` and `frontend-design` before writing the reading** — its *leaning* clause is already a taste judgement. `canvas.md` owns which files carry the material and its boundary. Read no skill that prescribes a fixed look.

**One absent is asked through AskUserQuestion, never merely reported**, naming what is lost — `impeccable`'s ban list, display-face and convergence calibrations, the Operate register, every later detector count; `frontend-design`'s direction method and restraint — with continue-without or stop-to-install (`npx impeccable install`); continuing is recommended where installing is unavailable here. The other material still loads. The answer rides every canvas round and the ratification report as its own line, naming what was missing.

**Sources, in rank: the user, then the code, then the PRD.** An explicit user statement outranks everything. Where the user was silent, read what exists from the code — router for pages, manifest and platform files for the platform, auth and guard code for roles, rendered strings for the locale, dependency file for the stack. Then PRD Sections 1–2 where readable. A gap all three leave is named inside the reading and settled at its correction, never as its own question. **A conflict is a finding named in the reading, never a silent pick**: a user statement against the code is followed and reported; between code and PRD, the code wins on what exists, the PRD on what ought to be, and the loser is reported.

**Reading** is one sentence, your own conclusion before asking anything: *"I read this as [kind of app] on [platform] for [who uses it], leaning [the feel that fits], because [reason from the PRD]."*

**The platform slot is mandatory** — never asked again where Section 1 holds it, otherwise read from the code and confirmed inside the reading, never as its own question.

Ask for correction — **nothing after this runs before it is answered**: no dialog, no search, no frame. Through AskUserQuestion, **put the full reading sentence inside the question field itself**.

### The audit — where UI exists

Run it **before the reading is put for correction**; read what the code uses, not what the PRD says.

**The audit runs in one subagent, this section as its brief; the session that draws never opens the old UI** (`canvas.md`, blindness). It writes two files under `src/design-canvas/.audit/`, deleted with the canvas:

- **`audit.md`** — the block below, the frame inventory, the Section 5 deviations, the screenshot paths. The user reads it now; this session opens it only at Step 6.
- **`handover.md`** — the only thing the drawing session reads, holding in this order and nothing else: the app in three sentences from PRD Sections 1–2 · the roles · the function inventory · the route list, each route with a few words on what it is for and nothing on what it holds · the data vocabulary a fixture must respect, with a handful of real rows from the data layer where it holds any · the UI stack row · the counts that price the pass (components affected, stray values, detector hits) as numbers. **No colour, hex, font name, radius, spacing value, shell description, part or section name per page, Section 5 prose, screenshot, or code excerpt** — nothing on how anything looks or where it sits.

No subagent available → say so, run the walk here, and report the redesign as drawn with the old UI in context.

Report one block:

```
AUDIT
Tokens defined      : [how many colors · text steps · spacing values · radii]
Token health        : [how many never read · duplicate roles · library slots unmapped]
Stray raw values    : [how many hex · font sizes · spacings, across how many files]
Slop detectors      : [how many hits · how many rules, from `npx impeccable detect` on the
                       source tree — the source tier only; the full set needs the running app.
                       `n/a — native surface` where Section 1's Surface is not web technology]
Icons               : [families, named · how many sizes · how many weights]
Fonts loaded        : [from the styling files AND the HTML entry — a family named in CSS
                       but never loaded renders as its fallback, and only this row sees it]
UI stack            : [component library · icon pack · engines — chart, table, date,
                       drag-and-drop — with versions, from the dependency file]
Repeated labels     : [longest · median · how many repeat per screen]
Supporting text     : [how many paragraphs · the longest in sentences]
Frame inventory     : [routes counted from the router · parts and states named per route,
                       or `routes only — the running app could not be walked`]
Deviates from S5    : [list, per rule broken — Section 5 filled only]
Components affected : [file count that will be touched if tokens change]
```

`Components affected` sizes the pass; show it before the user decides anything. **The `UI stack` row is the canvas's import whitelist** (`canvas.md`); a needed job no installed engine covers becomes an engine dialog at Step 3, an installed engine unused is a finding.

**Logic-layer bleeding** (handwritten fetching in UI files, hand-parsed dates, unvalidated inputs) gets the `logic-settle` offer under that skill's rule; continue either way.

**Screenshot one page per archetype at desktop width**, per Section 1's Proof profile, for Step 8's comparison; the drawing session never opens them before the judgement's before/after.

**The function inventory** — every function the app carries, one line each: what can be done, never where or how it looks. It is the canvas's brief-floor (`canvas.md`).

**The frame inventory** — per route, the parts and states that render there, names only; **routes from the router file, never from memory**; states real data cannot produce listed anyway (loading, empty, failed, every role branch). It **never reaches the drawing session**; the Step 6 gate checks the canvas against it.

**App could not be run, or no credentials → say so here and at Step 6**; the inventory is routes only and the gate carries `frame coverage unverified — the running app could not be walked`.

**`Slop detectors`** runs only on a web-technology Surface (`canvas.md`); a native one reports `n/a — native surface` here and at every later detector step. Source-tier only; Step 8 runs the full set. Hits are **findings**, never repairs on the way past. `impeccable` absent → `n/a — not installed`, said aloud.

**Token health** reads the library's slot list from the installed package, never from memory. Read Section 5 first: a legacy stock Section 5 (`prd-structure.md`) reports `n/a — stock` and counts no unmapped slots.

**Where Section 5 is filled, three more things hold.**
- A deviation is a **finding**, not a reason to change Section 5.
- Two Section 5 roles at the same value are a finding against the PRD, merged as repair work.
- **No archetype table is a finding.** Derive one from the routes (`interview.md`, The archetype table) and put it for ratify-or-correct, never adopted silently; ratified, it enters Section 5 at repair scale, and each page far short of its archetype gets one `QUEUE.md` line for `build-flow` Section 4. No `/styleguide` route → the pass generates it (Step 7).

**A page holding too little is not a finding.** Do not fill it; hand it to `build-flow` Section 4 and name it. A redesign still rebuilds its shell to its archetype with the content it has.

## Step 2 — Fix, or redesign — where Section 5 is filled

Section 5 empty → not asked; continue at Step 3.

One question, two options, with a recommendation:

| Choice | What changes | Questions asked | Components touched |
|---|---|---|---|
| **Fix the drift** | Zero new norms — only bringing code back in line with the existing Section 5 | None | Only the deviating ones |
| **Redesign** | **Section 5 is rebuilt from zero** — every line re-decided, archetype shells and visual-direction prose included; today's values survive only as *keep* answers. The app looks redesigned afterwards, not retuned | The full interview, *keep* first on the stack and `Keep — today's look` among the directions; every value names the value it replaces | Every page, replaced by its canvas file |

Offer no third, narrower option: scope is narrowed by *keep* answers, which every decision carries.

**Recommendation:** fix the drift when the audit shows Section 5 is still right and the code strayed.

**Consequence:** quote the affected-component count; state that a redesign includes the component-library dialog; state that a non-*keep* library answer rewrites every component and revokes `CLAUDE.md`'s stack lock; **state that the app looks different afterwards**; name the pages handed to `build-flow`, whose change is capped until their content lands.

Fix the drift → Step 6, whose gate shows the findings. Section 5 is untouched, except merging two roles at one value, approved line by line.

## Step 3 — The interview: everything non-visual, then the look

Read `references/interview.md` and run it in its order: **the non-visual dialogs first — the stack (library · styling · icon pack · triggered engines) and four product calls (supported widths · theme mode · the two screens the frames are drawn on · copy voice) — each only locking its answer; then the reference search; then the direction question, multi-select; then the install gate (Step 4); then the direction frames, picked on screen (Step 5). Nothing is installed while the interview runs, and nothing about the look is asked after the pick.** Every option is invented for this app.

**A tick is inspiration, not an anchor**; nothing stands the frames down (`interview.md`, Part 2).

**Where UI exists, `Keep — today's look` is the first option of the direction question**, never the recommendation. The search runs from `handover.md` alone.

The archetype table, the `/styleguide` route and real running pages are produced whatever was picked.

**Every question goes through AskUserQuestion, never prose**, in auto mode too — recommendation first and marked "(Recommended)", each option's consequence in its description, everything needed inside the dialog, up to four per call. The chat stops this skill names — the install gate, the one-line package approvals (font, linter), the Step 6 gate and its REPAIR list, the Step 8 deletion — are the exceptions: each ends the turn and waits for a reply.

**Nothing the user did not choose is silent**: every value decided beyond the picked frame surfaces as one cancellable line with its basis (`interview.md`, What the designer settles). Where UI exists each line names today's value, and cancelling opens a dialog with `Keep — <today's value>` first.

**A canvas that misses twice re-opens the look, not the interview:** re-read both materials, **re-run the search steered away from what was rejected**, re-ask the direction question, draw **fresh frames**, regenerate the canvas, never patch. The stack and product calls stay closed; a rejection naming a product call re-asks that dialog alone.

### The stack, asked

Read `references/library-rubric.md` and `references/engine-rubric.md`. The stack is settled before the frames — **one dialog per decision, answers locked, installed only at Step 4**:
- **component library** — 3–4 verified options, *own components* always one;
- **styling** — only where the library brings no styling system; Tailwind CSS recommended on the web, plain CSS always an alternative;
- **icon pack** — only when the library bundles none;
- **engines** — only where a trigger in `engine-rubric.md` fired; no trigger, no engine dialog.

Candidates are **verified live** per the rubrics. **Where UI exists every stack dialog carries *keep* first and recommends it**, unless the audit indicts the library or engine itself.

**Draft the full product before the engine dialogs** (`canvas.md`'s expansion duty), so draft-implied triggers fire now. **Answers outside the options are always accepted**, on every dialog. A package named outside them is verified the same way and used; state its consequence if known, or say it is not.

## Step 4 — The install gate, after every answer and before anything is drawn

**The install gate is its own chat stop, after the direction question and before the first frame.** It holds only what the locked answers decided; a reply changing an answer rewrites that line and re-shows the block. **Never put this block inside an AskUserQuestion.** Present it, end the turn, wait for the reply in chat.

```
Will install:
  npm install
  <component library>          [the library answer — nothing where UI exists and it was kept]
  <styling>                    [the styling answer, or what the library brings]
  <what the library omits>     [researched per candidate under library-rubric.md]
  <icon pack>                  [bundled by the library, or the icon answer]
  <engines>                    [chart · table · date · drag-and-drop — only what an
                                engine dialog decided, nothing speculative]
  <linter>                     [only where the repo carries none — Step 6's lint floor is
                                written into it]
```

Wait for approval. Refused → hand over the commands for the user to run, then wait. Nothing to install → say so in one line and continue.

Install nothing outside it; something extra → ask again. The font is the one exception (Step 6). **Where UI exists, the block also says what leaves** — removed in the pass (Step 7), never here.

## Step 5 — The canvas: rounds until final

Run under `canvas.md` entire, in order: the 2–4 direction frames on the two Step 3 screens, drawn with the installed stack, picked on screen, refined once where the pick carries a change (`canvas.md`, Directions first; composition in `interview.md`); the design plan below; then the canvas rounds (`canvas.md`) — two rounds, then Step 3's escalation.

**Where UI exists and Keep was ticked, today's look is one candidate; the canvas is always drawn blind to it** — today's look is the running app at its real routes, captured at both widths in the compare page, never redrawn.

**Picking `Keep — today's look`** ends the drawing: nothing is redrawn, the unchosen frames are deleted, and the flow continues at Step 6 — as fix-the-drift where Section 5 is filled, as the ratification of measured values where it is empty. **A Keep pick carrying a change** (*keep it, but with the brand green*) is not Keep: the refine round redraws the proving page to today's values with the change applied, and the flow is a redesign from there.

### Then state the design plan — narrated, not gated

**Write it in the turn after the pick, before the first full canvas file**, to the picked candidate. Announce nothing of it before the frames.

| Part | What is stated |
|---|---|
| Direction | Purpose · the one tone held · what makes this app memorable rather than adequate (`frontend-design`) · the copy voice answered at Step 3, per page group where it was asked per group (`ui-build`, Writing) |
| Colour | The named values with their roles — as many as the direction needs, no count fixed here — and where they came from — a brand palette, a reference, or an accent chosen first and the neutrals pulled toward it |
| Type | The pairing and each face's job. A face on `impeccable`'s calibration list is named with the reason it was still chosen |
| Layout | The shell and the composition in one or two sentences — where the density sits, what breaks the grid |
| Signature | The single element this app is remembered by (`canvas.md`, the taste licence) |

Where UI exists, the recommended frame names what it departs from, and each value names today's value beside it.

**Then critique it against the brief in the same turn:** any part a session with a similar brief would also arrive at is a default — **revise it and say in one line what changed and why.**

**Narration, not a gate**: do not end the turn, ask, or wait. The PRD is not touched during rounds.

## Step 6 — Ratification: Section 5, the styling files, `/styleguide` — and the gate where UI exists

**The font is installed here** — a face needing a package is one install line approved in chat, named as the only install outside Step 4.

**Generate `DESIGN.md` first, then scan.** Write it at the project root from the ratified values (colours, typography, radius, spacing, Section 5's component tokens) **to the frontmatter schema `impeccable`'s document reference gives, read at write time**, body: `Generated from PRD Section 5 by design-settle — do not edit; Section 5 is the source.` Only this step regenerates it, and it does so whenever Section 5 changes; a hand edit or an `impeccable` refresh from the built world is a finding. Before reporting this step done, run the detector over the styling files and the styleguide route and report the count; a hit on a just-ratified value is named and left standing.

**Approving the canvas is the approval.** Report its values as cancellable derived lines, then write them (`canvas.md`, Ratification). **Where no UI exists there is no second gate** — Section 5 and the styling files are written here. **Where UI exists** the values are the gate's *new* column.

**Where `Keep — today's look` was picked and Section 5 is empty, ratify the measured values** — every value `interview.md` names (the reference, what the frames would have decided, the designer-settles list); the stack and product calls are written as answered. The audit decides how each entry is put:

| What the audit measured | How the entry is put |
|---|---|
| **A coherent value** — a real scale, one family, a consistent radius | **Confirmation.** Show the measured value; first and recommended is an option naming the action plainly — `Keep this value — 8px` — never this file's vocabulary |
| **Nothing coherent** — scattered raw values, no scale, contradictory usage | **A real question**, with real options invented for this app |

**Batch confirmations and questions** through AskUserQuestion. **Write a ratified value exactly as measured**, never tidied. Unanswered → `[needs verification]`, out of the pass. **An answer differing from the measurement is a real change**: diffed at the gate, its pages drawn at Step 5.

### What is written

| Written in | Contents |
|---|---|
| `PRD.md` Section 5 | **Rules and scale** — how many may exist, what is forbidden, written from what the user ratified — never from a stock phrasing |
| Styling files (`tailwind.config`, CSS variables, the component library's theme file) | **Values** — font name, icon pack name, hex, radius number, spacing number |

Section 5 also holds colour and spacing roles, values and usage rules, and **the component-token table** — the **per-component number** for every component an archetype names: control height per size · input height · field padding · card padding and radius · table row height and vertical padding · header treatment · badge size and radius · modal radius · toast padding · focus ring (`build-flow` never reads the theme).

**No `PRD.md` → create it** with Section 5 alone and one header line naming Sections 1–4 `[needs verification]`, owed by `app-settle`. **Off-shape `PRD.md`** → append Section 5 under its own heading, touch nothing else. Follow `prd-structure.md`'s sub-sections. Anti-patterns holds only user-ratified prohibitions, possibly none.

**Page Composition holds the ratified archetype table** — per archetype: shell layout, components, density profile, empty/loading wording, routes. Two density profiles from a role split go under Breakpoints & Density.

**Every Section 5 line traces to an interview answer, a reported derived decision, or a ratified canvas value**; nothing else is written. **A filled Section 5 is rebuilt from zero, never patched**: an old line survives only through *keep* or re-ratification, otherwise it is a removal in the gate's diff.

### Five rules bind the styling files

**The palette is two layers, and the second one is the system.**

- **A ramp per functional hue** (about ten steps) so hover, active, subtle fill, border and text-on-fill each land on **an existing step**. **Derived, never typed**: from the picked accent and its pulled neutral, in OKLCH per `impeccable`. **Follow the stack's convention** (Tailwind's `50 … 950`), never a parallel scale.
- **Three shades per semantic family** — light, base, dark; the dark chosen by measuring it on its light fill to clear 4.5 (`canvas.md`, Ratification).
- **A semantic alias layer, and product code reads only that** — surfaces, text, borders, focus ring by role, each pointing at a step.
- **The chart palette belongs to the token set**, chosen once; `dataviz`, where loaded, assigns series colours from it.

State the step count and the alias list in Section 5's colour table.

**Every semantic slot the component library exposes is mapped**, the neutral `default` included — list the slots first.

**A token nothing reads is not written**, nor a layout constant components duplicate as a utility class.

**Two roles with the same value collapse into one** before Section 5 is written.

**One palette, two consumers.** A utility-CSS theme and a library theme are both written from Section 5's colour table in the same edit.

### The `/styleguide` route

Generated before the canvas (`canvas.md`); verify it here against the done-check. An existing app without one gets it inside the pass (Step 7).

**One route file** (e.g. `src/pages/styleguide.tsx`) at `/styleguide` in dev, out of navigation and the production build. **It imports the production components and tokens** — never copies, a separate HTML file, or a second source of values. Offer deleting it later; never require it.

Sections, in order, rendered from what was decided:

| Section | Contents |
|---|---|
| Foundations | Color roles or scales as Section 5 defines them, with the semantic token list read from the styling files · every text step with a real sample sentence · spacing scale · the density profile table with its numbers, both profiles where a role split produced two · radius, shadow, breakpoints, motion · the contrast section, one row per pair with its computed ratio, in every ratified theme mode. **Rendered by `canvas.md`'s specimen rule** |
| Components | Every component the app uses or an archetype names — variants, sizes, and states per component, including loading, empty, and failed where they apply, with a short real-usage snippet |
| Archetypes | The Section 5 archetype table, one card per archetype: shell sketch, components, routes |

**Done is measured against the table, not the page looking full**: every semantic token appears; a component checklist written first, never recalled — every component an archetype names with its variants and states (inputs: default, focus, disabled, error; buttons: hover, focus, disabled, loading; stepper, dialog, dropzone in a static frame); every archetype card has all three parts. Report **archetype → components it names → where each renders**. The only allowed absence is a component no archetype or flow uses, stated with that reason.

### The lint floor

Write **the four refusals `ui-build` names under its lint floor into the stack's own linter, derived from this app and never pasted from a stock config.**

| Refusal | Derived from |
|---|---|
| Raw element | The shared set the pass promoted, plus what the library ships — only elements this app has a component for |
| Raw value | The utilities and style properties that carry a Section 5 value — colour, radius, font size, the spacing scale |
| Numbered ramp step | The ramp names in the styling files. Not written where a legacy stock Section 5 left no alias layer to read instead |
| Primitive import | The packages the shared set wraps. None → not written |

**Scoped by path**: the components folder is exempt from the first and fourth, the styling files from the second and third, `src/design-canvas/` from all four. JS/TS web: ESLint's `no-restricted-syntax` and `no-restricted-imports`; other stacks: the analyzer's equivalent **verified live at write time**, an inexpressible refusal reported as `not enforceable on <stack>`. No linter → Step 4 installed one; in fix-the-drift, one install line approved in chat.

**Proven on what must pass before what must fail.** Lint the promoted app first; a hit on a freshly written page is a raw value to fix or a pattern too wide (`grid-cols-[1fr_auto]`, a `calc()` is not a raw value). Then plant one violation per refusal in a scratch page, see each refused, delete it.

**Files the pass did not rewrite are baselined, never excused** — in the linter's own suppression baseline, verified live. Never lower a rule to a warning. Report the baseline's size at the close; it only shrinks.

**Write `AGENTS.md`'s `## UI` part in the same act**, to `app-settle` N5's shape: the shared-set file and folder, the library, the styling file, `/styleguide`, the lint command (no file → write it whole). A path that does not resolve is a failed item.

**One floor, one command**: these four join `logic-settle` Step 7's config where it exists, or found it. The detector stays alongside.

### The gate — where UI exists

The **single stop** authorizing the change. **A redesign** — one message, four parts, then a hard stop answered in chat, never an AskUserQuestion:

1. **Section 5 as a diff.** Only what changes, old beside new — removals included:

```
Accent color : blue #2563EB  →  green #059669
Text steps   : five          →  four (merge section title and body)
Radius       : 8px           →  0
Signature    : ledger seam, sole vertical rule  →  removed
```

An old line nothing re-created leaves as `→ removed`, never by omission. Where Section 5 was empty, the *old* column is the **measured** value, marked as such — `Radius : 8px (measured) → 0`.

2. **The file plan.** Each page line reads `replaced by its canvas file` or `retoken only — no canvas frame`, never a third label. **In a redesign `retoken only` is unavailable**: an undrawn component is `deleted` (anything still needing it is drawn), a thin passthrough whose child was redrawn is deleted, its callers reaching the redrawn child directly. An unaccounted file is an inventory failure. **Shared canvas files get their own line under their header's production path.** A page with a canvas file listed `retoken only` is its own question. List chrome, shared components, styling files, linter config, `AGENTS.md`, and `UNTOUCHED` files. Close with the **seam points** from Step 7's order, never a time estimate.

```
PASS — [n] files
LeadTable.tsx    replaced by its canvas file
wizard.tsx       → src/components/import-wizard.tsx · shared by 7 pages · replaced by its canvas file
StatusChip.tsx   retoken only — no canvas frame · 4 status colors updated
index.css        11 tokens replaced · 3 deleted · fonts now load here
App.tsx          replaced by its canvas file (chrome)
UNTOUCHED        PhoneContact.tsx
```

3. **The detector's audit count** and how many hits the canvas removes; the rest listed by rule, returning at Step 8.

4. **What approval orders, contradicts, and removes.** Ratified elements lacking data, one line each — element, page, the work ordered (column · RPC · migration). Then deviations: canvas elements the real flow contradicts and real controls the canvas never drew (`canvas.md`), one decision line each. **Then removals, confirmed item by item** — every function or control leaving, plus every part in `audit.md`'s frame inventory (opened now) that no canvas page carries. *Approve everything* never covers this group.

End the turn and wait for the chat reply; lines may be approved or rejected by name. Rejected values return to Step 5, nothing written; all approved → the pass. Nothing changed → close at Step 9.

**Fix the drift, or `Keep — today's look` with Section 5 filled** — the same gate shows the findings list:

```
REPAIR — [n] findings
1  Usage.tsx:185-188   gradient text           impeccable · craft floor, Refuse
   3 sentences  →  removed
2  StatusChip.tsx:19   label 15 chars          S5 · Repeated label length
   "Belum dihubungi"  →  icon only, text to aria-label
```

STOP for approval per item; a rejected item stays a finding, reported at Step 9.

## Step 7 — The pass: every page, in one session

**Where UI exists, branch first** — own branch or worktree from a committed base (`design/rework-<date>` or the user's naming), an untracked canvas folder brought along. Dropping the branch reverts everything, at the user's word, closing at Step 9.
- **First act: write Section 5** in full, then `CLAUDE.md`'s Component library row if the library changed — the only moment the PRD is written. **The gate block travels with the branch** in the first commit's message body: Section 5 diff, file plan, ordered work, answered deviations.
- **Second act: the freshness check.** Re-walk the function inventory against current code; a flow changed since ratification is a new deviation line put to the user **before** its page moves.

**Where no UI exists, no branch**; the pass runs in place.

**All canvas pages are promoted in one pass**, per `canvas.md`, element for element, in this fixed order:

1. **Foundations.** Theme files take the new values, old tokens **deleted**, plus everything the canvas CSS carries beyond values: **the font loading itself** (a package not installed at Step 6 is one line approved in chat), element rules, shadows, motion durations. Verify in the browser that the computed font-family is the loaded webfont. Step 6's five styling-file rules bind.
2. **Chrome and shared components, from the canvas chrome** — in production before any page importing them counts as moved; production logic (auth, navigation, data) is wired into the canvas markup, never the reverse. **Placement follows `ui-build`'s placement rule.**
3. **Pages — the proving page first**, each canvas file **copied to its real path**, wrapper removed. **With a data layer**, swap the fixture import for it without touching the markup body, and check each page at both widths: holding → report and continue; first collapse → stop, a rework round of that page. **With no backend yet**, pages keep fixtures reshaped to `build-flow`'s contract form (`src/contracts/<page>.ts`, `src/contracts/<page>.fixtures.ts`, per its `references/contract.md`), and **each gets a `QUEUE.md` line** `wire <page> to real data`. Where `logic-settle` chose the data layer, loading, empty and failed states come from its cache, never a handwritten effect.
4. **Components not on the canvas** — **fix-the-drift only**: retoken to zero raw values; a prop or theme value departing from the library default returns to it unless Section 5 requires it. **In a redesign this step is empty**; a file here is a failed inventory to report, never to retoken.
5. **`/styleguide`** — archetype cards on the ratified shells, every new component rendered, Step 6's done-check.
6. **Assets** locked to the old colors — where UI exists: inline SVG, favicon, brand-coloured images.
7. **The old library and engines are removed**, if their decisions changed.
8. **The lint floor, then `AGENTS.md`'s `## UI` part**, per Step 6 — fix-the-drift writes them too.

**The proving page is the bar** for every later page; with data, its fixtures include `bulk` and `messy` cases. `ui-build` binds every promoted page.

Page running → **prove it at two widths with screenshots** (Section 5's desktop breakpoint, the ratified lowest width) per Section 1's Proof profile. No capture tooling → say so, name the run target and both widths; never claim they were judged.

**The UI code is the pass's to rewrite — the behavior is not**: queries and mutations, guards, route paths, and every action's outcome stay unchanged. No unrelated fixes.

**Detector findings are deferred** to Step 8, overriding `impeccable`'s act-on-findings instruction.

**The approved canvas is the specification.** Drawn elements land as drawn; undrawn ones, and prose it left out, do not. A difference the session would prefer is refused, not asked.

**One exception: a ratified element whose data does not exist yet** — no query written; promoted **rendered empty and labelled as waiting**, with one `QUEUE.md` line naming the data. Never dropped or hidden behind a flag.

**The pass also stops** for a drawn element that would make the app claim what it cannot do — a `build-flow` stop.

**Rework rounds.** A page collapsing, or a user-requested rework, gets a rework round. **Two per page at most — a third does not run, and Section 5 reopens** through Step 3's escalation. A changed Section 5 updates the styling values and rebuilds pages from the new tokens, never patched.

**Fix the drift** runs here too, on the same isolated branch: the approved findings, nothing else.

## Step 8 — Verification: evidence, not eyes

Every check leaves something the user can inspect. All of them before reporting done:

- **The build passes.** It does not → stop, fix it, do not report done.
- **The structural diff per canvas file — the primary evidence**, shared files included under their header's production path. Differences are confined to the data seam (fixture import → data layer plus loading and error wiring; with fixtures kept, the removed wrapper and the contract-shaped import) and to lines answered at the gate; anything else is failed. Verdict per file; an unshowable diff is not verified.
- **Computed styles probed in the browser**: fonts are the loaded webfonts; token slots spot-checked against the theme files. (No browser in the Proof profile → its Visual line, naming what could not be verified.)
- **The rendered structure matches, counted.** Canvas and live page in the same dev server; compare each body's element tree (names and classes, **text and numbers discarded**), one line per page: `canvas n · live n · differs n`. Above zero names the elements and is failed. Unshared chrome is excluded and said; an uncountable page is not verified.
- **Zero raw values** across every promoted page and component — search again for hex, font sizes, raw spacing.
- **The lint floor passes, and bites.** Zero hits outside the baseline; each refusal seen refusing its planted violation, reported per refusal, `not enforceable on <stack>` named. Every path in `AGENTS.md`'s `## UI` part resolves.
- **The styleguide passes its done-check** (Step 6), foundations rendered as specimens.
- **Every contrast ratio on the page was computed**, not recalled, in every ratified theme mode; every semantic dark shade clears 4.5 against its own light shade.
- **The fixtures close** on every page still running on them — totals, percentages, bar widths, pagination (`canvas.md`, Coverage).
- **The detector ran against the running app** (the dev server): hit count beside the audit's where UI existed, every hit fixed or left standing with one line why. `impeccable` absent → the check could not run, never reported passed.
- **The signature survived promotion** on the pages that carry it.
- **The proving page holds at both widths**, screenshots taken.
- **Pages running on fixtures are listed by name**, matching the `QUEUE.md` wire lines one for one.
- **Where UI existed — the file plan matched.** Every file listed at the gate changed, and no file outside it did.
- **Where UI existed — the seeded walk.** Seed `[CLAUDE]`-prefixed rows first. Walk the proving page at desktop and the lower bound; compare one page per archetype with its audit screenshot — each reads redesigned unless all behind it was *keep* and the gate said so.
- **Where UI existed — function parity holds.** Every function-inventory line is reachable **at both widths — a control hidden below the breakpoint is a missing function** — unless the user cut it and the gate said so.

Any fails → fix it in the same session.

**The canvas files stay after promotion** (`canvas.md`, Ratification — the canvas lifecycle). **Passing checks earn a proposal to delete — never a deletion.** Where UI existed and real data was wired in-session: report the per-page diff verdict, invite a side-by-side walk at `/design-canvas`, end the turn and ask whether the canvas and seed rows may go — a chat stop, never an AskUserQuestion. Only a granted confirmation deletes page files, entry route, foundations board, canvas CSS and `.audit/` together. A refusal or a named page makes that page a failed item now; the canvas stays. A page left on fixtures keeps its canvas file until it is wired, survives both widths, and the user confirms the side-by-side (carried by `build-flow`). Never delete unasked.

## Step 9 — Close

**Nothing stays a draft.** Every canvas page ends promoted into a real route.

One block: the detector's numbers — Step 8's count, beside the audit's where UI existed — and every hit left standing with its one-line justification · the Section 5 lines that changed, where there was an old one · files changed, with their count, and files `UNTOUCHED` · each page's fate — promoted and wired, or promoted on fixtures with its `QUEUE.md` wire line · items the user rejected, still standing as findings · the canvas outcome and how many rounds it took · the verification results, per-page diff verdicts included · the canvas files still standing and the queue line that will retire each · the `/styleguide` route named as staying dev-only, deletable at the user's word · the lint floor — refusals written, the baseline's size, anything `not enforceable` · what is still `[needs verification]` · **the PRD sections `app-settle` still owes**, where the PRD was missing or off-shape — `build-flow` will not open a page until Sections 2–3 exist.

**A pass this session could not finish is written down, not implied.** Every page not yet promoted and every verification item not yet passing becomes one `QUEUE.md` line; the canvas stays alive until those lines clear.

State that this gate **no longer applies** to later pages — from here on Section 5 and `ui-build`'s component rules bind.

**The commit waits for the user's word** — proposed on the pass's branch with nothing else in it; merging is the user's move.

Nothing changed — every answer *keep*, today's look picked, or the canvas reverted → say so in one line and list the audit findings that remain.
