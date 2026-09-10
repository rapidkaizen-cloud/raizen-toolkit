---
name: design-settle
description: Settle the visual direction and component library of an app, whether it has UI already or none at all. Audits what the code uses today — empty on a fresh repo — then routes — nothing built goes straight to the interview, a filled Section 5 asks repair or overhaul, and components without a Section 5 go to ratify. One reference question, then 2-4 full-fidelity direction frames the user picks from on screen, then the rest of the taste slots in one turn and the stack questions that gate the install — all options invented for this app. A temporary in-repo canvas renders the answers as every page of the app in production-grade code, judged in the real browser, approved at one gate, then relocated into the app — the only difference between canvas and production is the data. Use before the first UI component of a repo is written, and whenever the user wants to redesign, restyle, or overhaul the look of an app that already has one.
---

# design-settle — the visual direction, from nothing or from what exists

`app-settle` writes the PRD. `logic-settle` decides the layer under the UI. This decides how the app looks, and it is the only path allowed to write **PRD Section 5**.

**One skill, and the audit decides which path it takes.** There is no mode to pick and no second skill to route to: `R1` audits what the code uses today, and on a repo with no UI it comes back empty in one pass — which is the cheapest possible answer to the question "which kind of session is this".

| Section 5 | UI components | Path |
|---|---|---|
| Empty or absent | none | **Fresh.** Nothing to audit; the interview starts from zero and there is no old value to protect |
| Filled | any | **Rework.** `R2` asks repair or overhaul |
| Empty or absent | present | **Ratify.** `R2` is not asked; go to `R2b` |

The third row is the `app-settle` document-mode case: an app whose visual direction was never decided by anyone, only accumulated. It gets the same audit as any other, and then every entry is put to the user before it becomes a norm.

The three paths share one step skeleton, and the deltas are marked where they are structural: **fresh** has no audit findings, no diff gate (no old values to protect), and no isolated branch (a fresh repo has no parallel work to disturb); **rework** and **ratify** carry all three.

## Hard limits

A `PRD.md` is an **absolute precondition**. Missing → STOP, point to `app-settle`, which reads the directory and picks its own mode.

**Section 5 is never written from existing code.** That direction — `CSS → PRD` instead of `user → PRD → CSS` — turns every accident in the stylesheet into an official norm nobody decided on. The audit produces **findings**; a finding becomes a Section 5 line only once the user ratifies it. Section 5 changes only by **explicit user decision**, line by line.

**On the fresh path, Section 5 is written once the canvas is ratified.** On the rework and ratify paths it is written exactly once, and only after the Step 6 gate approves it — as the first act of the pass, on the pass's own branch. Until then nothing touches it, and no draft document stands in for it: the canvas is the draft, its variables and foundations board carry every value the user can inspect. Approval writes Section 5 in full; rejection leaves the PRD exactly as it was.

Two places in the documents may be written, and no third: **PRD Section 5**, and the **Component library row of `CLAUDE.md`** when the library question is answered with something other than *keep*. Do not create `MASTER.md`, `DESIGN.md`, `design-system/`, a staging PRD, or an audit report as a file. If another skill in this session produces a document, it is not committed and not referenced.

**The canvas is the final front-end, staged** (`references/canvas.md`). Its files are the future pages, written production-grade — the user approves code, not pictures, and promotion relocates that code instead of imitating it. The one legitimate difference between a canvas file and its live page is the data flowing through it; everything else is a failure to fix or a deviation the user has named.

**Two phases, two safety rules.** The canvas phase only adds files under `src/design-canvas/` — it runs safely beside any other session, and no other session touches that folder. On the rework and ratify paths the pass rewrites the app, so it runs **isolated on its own branch or worktree**, and parallel feature work continues undisturbed in the main tree. On the fresh path there is nothing to isolate from.

**Keeping everything is a valid ending, not a failure**, on any path that had something to keep. Answering *keep* to every question, or reverting after the canvas, closes this skill with the PRD unchanged and the code untouched. Say so plainly and report the audit findings; do not manufacture a change to justify the session.

Do not commit and do not push. Staging is fine; the commit waits for the user, and on the rework and ratify paths the pass's commit is **proposed at the close, on the pass's own branch**. Never push, never merge, never open a PR.

Not decided by the user → `[needs verification]`.

**Step 0 is the routing table above.** Report it as one line — the two readings and the path they produce — then run that path's own precondition block, `F0` or `R0`. Do not run both.

---

# Fresh path — a repo with no UI yet

## F0 — Preconditions

Check and report one short block:

```
PRD.md      : [present / missing]
Design mat. : [impeccable present/absent · frontend-design present/absent — both Required]
Section 5   : [empty / already filled / product without UI]
Kind of app : [from Section 1 — a label, never a branch]
Register    : [first visit / tenth use / both, per page group — derived from Section 2]
Platform    : [from Section 1 Surface — web, or the platform named there]
Primary role: [from Section 2]
Reading     : [one sentence — see F1]
Flow        : load taste.md + impeccable + frontend-design → reading →
              reference slot, alone → direction frames + pick, unless a reference
              or brand palette pinned the direction → rest of the taste batch →
              stack questions → design plan → install → canvas rounds →
              ratify + Section 5 → promotion (all pages) → verify → close
```

`PRD.md` missing → **STOP**, point to `app-settle`.

Section 5 already filled → **STOP**, ask whether the user really wants to rework the existing visual direction. That work belongs to `design-settle`.

**Section 5 empty but UI components already exist → STOP as well.** This skill decides a direction before any code carries one. An app that already has components needs its existing values measured and put to the user, not overwritten by an interview that has never seen them. That is `design-settle` on its ratify path — the case a repo arrives in through `app-settle`'s document mode.

Product without UI → **STOP**, this skill does not apply.

## F1 — The reading

**Load the three materials first, before the reading sentence is written**: `references/taste.md` beside this skill, and the two Required installs, `impeccable` and `frontend-design`. `taste.md` names which of `impeccable`'s reference files carry the material and `canvas.md` draws the boundary; one absent is **asked** rather than merely reported, under `taste.md`'s rule — continuing without it is an answer the user is allowed to give, and one the session is not allowed to give on their behalf. F0 has already routed, so nothing is read for a session that stops.

They come first because **the reading sentence is itself the first taste output** — its *leaning* clause is a judgement about how this app should feel, and the paragraph below says every slot's options are invented from the corrected reading. A leaning written before the material is read seeds every option that follows out of the same defaults the material exists to close, and the batch then offers the user a menu of them: a Typography slot offering Inter, a Direction slot offering a cream ground with a serif and a terracotta accent, a reference slot proposing whichever product came to mind first. **A choice never offered is not recovered by any later round** — the judgement can reject what was drawn, but it cannot reach an option that was never written.

Both are divergence guidance: they name the defaults that read as generated and the method for choosing a direction, never the direction itself; `canvas.md` holds the rule and where the line falls. No skill that prescribes a fixed look — a fixed palette, a fixed pairing, a card recipe — is read. They stay in hand for the rest of the flow: the design plan at F3, the canvas, the judgement.

There is no audit — nothing exists to audit; this step is its sibling. **Reading** is your own conclusion before asking anything, one sentence, shaped as: *"I read this as [kind of app] on [platform] for [who uses it], leaning [the feel that fits], because [reason from the PRD]."*

**The platform slot is not decoration.** `app-settle` already asked the platform and PRD Section 1 already holds the answer — it is never asked again. It rides in this sentence because the corrected reading is what every slot's options are invented from, so one word here is what puts the platform into all of them at once. Left out, the options arrive in the web's vocabulary and no later decision can tell that anything was lost.

Concluding first beats asking from nothing: the user only corrects what missed, and the correction carries more than an empty question would. A wrong reading is not a failure — it draws out detail that no question would surface.

State the reading, ask for correction, then continue. When the correction is asked through AskUserQuestion, **the full reading sentence goes inside the question field itself** — the dialog may render without the prose around it, so a question that points at text "above" can arrive pointing at nothing.

The slots' options and the canvas's values come from the model's own design knowledge of this app and its platform, sharpened by the three materials above, and the user's judgement on screen is what checks the result.

## F2 — The taste batch

Read `references/interview.md` and run it in its order: **the reference slot alone, the direction frames it routes to, then six or seven slots across two AskUserQuestion calls in one turn.** The options are invented for this app from the model's own design knowledge — no fixed list anywhere, and no research pass for taste — each option named in plain words with its consequence in parentheses, one real option marked "(Recommended)". Every slot carries **"Decide for me"**.

**The first slot is the reference** — the app or site this one should feel like — and its options are **real products named by you**, two or three that are arguable for this app, plus `No reference — explore freely` and `Decide for me`. It is asked first because a named anchor reshapes every option that follows, and the second call's options are written after the first is answered. A product the options missed, a screenshot, or a URL arrives through Other, and that is the best outcome rather than a deviation. `interview.md` holds the slot's own rules — what a named reference costs, and the line between setting a direction and reproducing an interface.

The answered slots are the user's preferences and the canvas's baseline; a slot answered "Decide for me" belongs wholly to the canvas's taste license. Either way the canvas may depart from any answered slot with a drawn, tagged, reasoned departure the user settles at the judgement (`canvas.md`), and the archetype table, the `/styleguide` route (F6), and real running pages are produced whatever was answered — what an answer changes is only where a value starts.

**Every question goes through the AskUserQuestion tool, never prose text** — the recommendation first and marked "(Recommended)", the consequence in each option's description, everything the user needs inside the dialog itself. This holds in auto mode too: a prose question simply ends the turn unanswered.

**Nothing the user did not choose is silent.** A "Decide for me" slot and every derived value surface as one line each with their basis — in the canvas assumptions block before drawing or the ratification report after approval — and the user may cancel any line; cancelling opens that value as a normal dialog. `interview.md` holds the list of what is derived and the floors that bind it.

**A canvas that misses twice escalates by re-opening this batch:** `taste.md`, `impeccable`, and `frontend-design` are re-read first (`canvas.md`), then the whole interview runs again in its own order — the reference slot first with products chosen against what was rejected, **a fresh set of direction frames** unless that answer pins the direction, then every remaining slot with sharpened options built from what the two rejections taught — and the canvas is regenerated fresh from the new answers, never patched.

## F3 — The stack questions, then compile into values

Read `references/library-rubric.md` and `references/engine-rubric.md`, then ask the second batch: the **component library**, its **icon dialog** when the library bundles none, and the **engine dialogs** whose triggers in `engine-rubric.md` have fired — nothing speculative; an app that trips no trigger hears no engine dialog. These are asked rather than improvised because they install code, and their candidates are **verified live** per the rubrics' duty — the one place research survives in this interview. The family rule in `interview.md` shifts recommendations toward already-installed ecosystems.

**Draft the full product before these dialogs close** — `canvas.md`'s expansion duty, run here rather than at drawing time, because the draft is what trips draft-implied engine triggers: it existing now is what lets every engine ride this batch and the install block close complete the first time.

Answers outside the options are always accepted. The user names something not listed → verify it the same way, use it, state its consequence if you know it, or say you don't.

### Compile into values

Compile the answered slots into the canvas's baseline: concrete hex values, font names, and icon entries. A slot answered "Decide for me" compiles to nothing — the canvas owns it.

The output is the canvas's **baseline, not a gate**. The user corrects values where they are visible: on the canvas, at the judgement. Waiting here for an approval would judge the same values twice.

### Then state the design plan — narrated, not gated

Both materials were loaded at F1 and are already in hand. **Write the plan out in this same turn, before the install block.** This is the step that separates a designed app from a competent average, and it is skipped by exactly the sessions that most needed it.

Five parts, short:

| Part | What is stated |
|---|---|
| Direction | Purpose · the one tone held · what makes this app memorable rather than adequate (`taste.md`) |
| Colour | 4–6 named values with their roles, and where they came from — a brand palette, a reference, or an accent chosen first and the neutrals pulled toward it |
| Type | The pairing and each face's job. Never the four `taste.md` names as failed choices |
| Layout | The shell and the composition in one or two sentences — where the density sits, what breaks the grid |
| Signature | The single element this app is remembered by (`canvas.md`, the taste licence) |

**The frames have already run by the time this step is reached, so the full plan is always written here** — to the candidate the user picked, or to the Direction slot they answered where a reference or brand palette stood the frames down. Nothing announces the plan earlier: the frames carry their own axes, one line of motivation and trade-off each, and that is all a user needs before voting. A plan that named a palette before the candidates were drawn would have decided the vote it was about to hold, which is the rigged set `canvas.md` forbids.

**Then critique it against the brief before drawing, in the same turn.** Work through what a session with a similar brief would produce; any part of the plan that arrives at the same place is a default rather than a decision. **Revise that part and say what changed and why** — one line. A plan reported without that pass has skipped the only step in it that does any work.

**It is a narration, not a gate: state it and keep going in the same turn.** Do not end the turn, do not open an AskUserQuestion, do not wait. What it buys is a decision the user can object to before the canvas exists, and a direction this session cannot quietly drift off later — the judgement still settles every value on screen.

## F4 — Install, before anything is drawn

**The install block is its own chat gate, right after the stack questions close** — its contents are known once the typography slot and the library and engine dialogs are answered (a typography answered "Decide for me" is decided by the designer here: the block's font line is where the user first sees that call, and refusing the block reopens it as a dialog), and everything is installed before the canvas is drawn (`canvas.md`). Do not ask twice, and **never put this block inside an AskUserQuestion** — a dialog covers the very block the user must read. Present the block, end the turn, and wait for the reply in chat.

One block, one approval:

```
Will install:
  npm install
  <component library>          [from the library answer]
  <what the library omits>     [researched per candidate under library-rubric.md]
  <icon pack>                  [from the library answer — bundled, or its icon dialog]
  <engines>                    [chart · table · date · drag-and-drop — only what an
                                engine-rubric.md trigger decided, nothing speculative]
  <font>                       [self-hosted or a package — say which, and where it loads]
```

Wait for approval. Refused → hand over the commands for the user to run, then wait.

Install nothing outside that block. Something extra turns out to be needed → ask again, do not slip it in.

## F5 — The canvas: rounds until final

Drawn and judged under `canvas.md` entire: the direction frames are already picked, so this step opens on files written production-grade — every state drawn, fixtures in one contract-shaped file that closes arithmetically, imports only from the declared stack — the three-scan self-check before every round (imports · the render · the arithmetic), the signature drawn, tagged, and settled in a question of its own, tagged departures and proposals, the judgement through AskUserQuestion, two rounds then escalation.

The PRD is not touched during rounds. The foundations board is the living draft of every value.

## F6 — Ratification: Section 5, the styling files, and `/styleguide`

**The styling files are scanned once they are written.** The values land from the canvas, so `impeccable`'s `design-system-*` rules have a theme to compare against for the first time here — run the detector over the styling files and the styleguide route before this step is reported done, and report the count. A hit against a value the user just ratified is a finding, not a correction: name it and leave it standing.

**Approving the canvas is the approval — there is no second gate here.** This is the delta from `design-settle`: no old Section 5 exists, so there is no diff to protect and no separate stop. The values behind the approved canvas are read and reported as derived decisions are reported — one line each, cancellable — then written (`canvas.md`, Ratification).

The split is permanent:

| Written in | Contents |
|---|---|
| `PRD.md` Section 5 | **Rules and scale** — how many may exist, what is forbidden, written from what the user ratified — never from a stock phrasing |
| Styling files (`tailwind.config`, CSS variables, the component library's theme file) | **Values** — font name, icon pack name, hex, radius number, spacing number |

Color and spacing are the exception: their roles, values, and usage rules are written in Section 5, because contrast is a norm and not an implementation detail.

**The component-token table is the second exception, and it is written in Section 5.** A scale alone guarantees drift: two sessions given `radius: sm 4 · md 6 · lg 8 · xl 12` will pick differently for a card, and neither is wrong against the scale. So the table states the **per-component number**, one row each, for every component an archetype names: control height per size · input height · field padding · card padding and radius · row height and vertical padding for a table · header treatment · badge size and radius · modal radius · toast padding · focus ring. It lives in Section 5 rather than only in the theme file because `build-flow` Section 4 opens every later page from Section 5 and never reads the theme — a number the queue cannot see is a number the queue will re-decide.

Follow the sub-section structure in `prd-structure.md` under `app-settle`. The Anti-patterns sub-section holds only prohibitions the user ratified — a canvas decision or an interview answer that forbids something — and may be empty; no stock ban list exists to copy from.

**Page Composition holds the ratified archetype table** — one row per archetype: shell layout, components, density profile, empty/loading wording, and the routes it owns. This table is what `build-flow` Section 4 opens every later page proposal from. Where a role split produced two density profiles, their numbers land under Breakpoints & Density.

**Every line in Section 5 traces back to one of three sources:** an interview answer, a derived decision already reported to the user, or a canvas value the user ratified. A rule belonging to none of them is not written, however sensible it looks — no question asks it, so nobody decided it.

### Five rules bind the styling files

**The palette is two layers, and the second one is the system.** A list of hexes is a palette; what makes it a design system is that product code never names one.

- **A ramp per functional hue, deep enough that nothing is improvised.** Hover, active, a subtle fill, a border, and text on that fill must each land on **a step that already exists** — a value invented mid-build is a value no board ever showed and no later page will find again. In practice that is around ten steps. **Where the stack carries a convention, follow it rather than inventing a parallel scale**: Tailwind's `50 … 950` is the one most component libraries already assume, and a second scale beside it means every future session picks between two answers.
- **Three shades per semantic family** — light, base, dark. The dark shade is not decoration: it is what makes text on the light fill clear 4.5, which is why Ratification chooses it by measuring it against its own light shade (`canvas.md`) rather than by stepping once along the ramp.
- **A semantic alias layer, and product code reads only that.** Surfaces, text, and borders are named by their role — the ground, the raised surface, the muted text, the focus ring — each pointing at a step. A component that names a numbered step has hard-coded a decision the alias layer exists to hold, and that is the line that has to move when the direction changes.
- **The chart palette belongs to the token set**, chosen once with the rest, not picked per chart. Where `dataviz` is loaded it decides series colour inside the plot; the token set is where those colours live.

State the step count and the alias list in Section 5's colour table, since colour is already Section 5's exception.

**Every semantic slot the component library exposes is mapped.** Libraries ship a full set of role colors, including a neutral one — usually named `default` — that every component falls back to when given no color. A slot left unmapped keeps the library's own value, so the app carries two neutral families: the one Section 5 chose, and the one nobody chose. List the library's slots before writing the theme file, then map all of them.

**A token nothing reads is not written.** A layout constant that the components duplicate as a utility class has two sources for one number, and the token is the one that will drift.

**Two roles with the same value collapse into one.** A palette naming both `danger` and `destructive` at the same hex has made one decision and written it twice. Merge before Section 5 is written.

**One palette, two consumers.** An app with both a utility-CSS theme and a component-library theme holds the same hex twice. The Section 5 color table is the source; both files are written in the same edit, never one alone.

### The `/styleguide` route

The route already exists — generated before the canvas was drawn (`canvas.md`) — and, importing production tokens, it follows the newly written values by itself; this step verifies it against the done-check below.

**One route file** (for example `src/pages/styleguide.tsx`), reachable at `/styleguide` in dev and kept out of the app's navigation and production build. It renders the whole visual language on one screen so the user corrects it here, while a correction is one token — not twenty screens later.

**It imports the production components and tokens.** Never hand-drawn copies, never a separate HTML file, never a second source of values. Deleting it later is deleting one file — offer that, never require it.

Sections, in order — each rendered from what Steps 2–6 actually decided, not from a fixed template:

| Section | Contents |
|---|---|
| Foundations | Color roles or scales as Section 5 defines them, with the semantic token list read from the styling files · every text step with a real sample sentence · spacing scale · the density profile table with its numbers, both profiles where a role split produced two · radius, shadow, breakpoints, motion · the contrast section, one row per pair with its computed ratio. **Rendered by `canvas.md`'s specimen rule, not as a table of names and values** — each token applied to itself with every other variable held constant, one caption treatment throughout printing the key and its resolved value together. This route outlives the canvas, so it is where that board's method has to survive |
| Components | Every component the app uses or an archetype names — variants, sizes, and states per component, including loading, empty, and failed where they apply, with a short real-usage snippet |
| Archetypes | The Section 5 archetype table, one card per archetype: shell sketch, components, routes |

**Done is measured against the table above, not against the page looking full.** Before reporting this route, check each row: every semantic token appears on the page; the component checklist is written first, not recalled — every component an archetype card names, each with its variants and states (inputs show default, focus, disabled, error; buttons show hover, focus, disabled, loading; mid-flow components — a stepper, a dialog, a dropzone — render in a static frame); every archetype card carries all three parts. When reporting the route, include the mapping **archetype → components it names → where each renders on this page**. The one legitimate absence is a component no archetype and no flow uses — stated, with that reason.

## F7 — Promotion: every page, on contract fixtures

**All canvas pages are promoted in one pass** — each file copied to its real route, the canvas wrapper removed, per `canvas.md`: element for element, chrome components first, the most data-dense page of the primary role leading. The chrome components land under `ui-build`'s placement rule — the set holding Section 5 rules in one file, a component carrying a flow of its own in its own file. This is the same all-at-once promotion `design-settle` runs, with one structural difference: **there is usually no backend yet, so the pages keep their fixtures** — reshaped into `build-flow`'s contract form (`src/contracts/<page>.ts` for the types, `src/contracts/<page>.fixtures.ts` for the cases, per `references/contract.md` of `build-flow`). Real data arrives page by page through the queue; the fixture import is the marker of what is not yet wired.

No isolated branch is needed — a fresh repo has no parallel work to disturb; the pass runs in place.

**Every promoted-but-unwired page gets a `QUEUE.md` line** — `wire <page> to real data` — written by this pass. An app full of fixture-driven pages looks finished while every number on it is fake; the queue lines and the close block are what keep that visible. Where `logic-settle` already chose the data layer, its loading, empty, and failed states come from the chosen cache when wiring happens — never from a handwritten effect.

**The densest page is the bar.** `build-flow` Section 4 judges every later page against it — building it thin lowers the bar for the whole app. Its fixtures must include `bulk` and `messy` cases: a direction that only holds for five tidy rows has not been proven. `ui-build` binds every promoted page in full — tokens only, zero raw values, states drawn.

Page running → **prove it at two widths with screenshots**: the desktop breakpoint from Section 5 and the ratified lowest supported width. Capture follows PRD Section 1's Proof profile — the browser is the web profile's answer; a platform whose profile names an emulator or a window capture proves the same two bounds through it. No capture tooling → say so and report the profile's run target with both widths named — never claim the widths were judged without either.

**Rework rounds.** A page collapsing under its fixtures, or the user asking for a rework, is a rework round of that page. **Two rework rounds of the same page at most — a third does not run, and Section 5 reopens**: the taste batch is re-asked with sharpened options, and the canvas is regenerated fresh from the new answers, never patched. Section 5 changed → the styling values are updated with it, and the pages are rebuilt from the new tokens rather than patched.

## F8 — Verification: evidence, not eyes

Before reporting done:

- **The build passes.**
- **The structural diff per promoted page.** Put each canvas file beside its live page: with fixtures kept, the only legitimate differences are the removed canvas wrapper and the contract-shaped fixture import. Any other difference is a failed promotion to fix now.
- **Fonts load for real.** The computed font-family in the browser resolves to the loaded webfont, not a fallback stack — the canvas CSS carried the loading, and the production entry must carry it now. (The web profile's check — a platform whose Proof profile names no browser verifies the equivalent through its Visual line, and says what could not be verified.)
- **Zero raw values** across every promoted page and component.
- **The styleguide passes its done-check** (the table in F6), its foundations rendered as specimens rather than as a table of names and values.
- **Every contrast ratio on the page was computed**, not recalled, and every semantic dark shade clears 4.5 against its own light shade.
- **The fixtures close** on every page still running on them — totals, percentages, bar widths, pagination — per `canvas.md`'s Coverage.
- **The detector ran against the running app**, not only against `src/` — `impeccable`'s full rule set needs a rendered page. Report the hit count, and triage every hit in the same block: fixed, or left standing as a finding with one line saying why. A hit left standing is not a failure of this step; an unreported one is. `impeccable` absent → say the check could not run, and do not report the step as passed on silence.
- **The signature survived promotion**, on the pages that carry it.
- **The densest page holds at both widths**, screenshots taken.
- **Pages running on fixtures are listed by name.** This list matches the `QUEUE.md` wire lines one for one — a page on neither list does not exist.

Any of them fails → fix it in the same session.

**The canvas files stay after promotion** — frozen references under `canvas.md`'s lifecycle: each dies only when its page is wired with real data, survives both widths, and the user confirms the side-by-side at a chat stop — never through an AskUserQuestion, which would cover the comparison being read. `build-flow` carries that per page through the queue. Never delete unasked.

## F9 — Close

**Nothing stays a draft.** Every canvas page ends promoted into a real route; a page left in the repo unrouted is dead code that reads as finished work.

The close reports the detector's final count beside F8's, and names every hit left standing with the one line that justified it. A design flow that ends without that number has verified its own work by assertion.

One block: the visual decisions that settled · files changed · each page's fate — promoted and wired, or promoted on fixtures with its `QUEUE.md` wire line · the canvas files still standing and the queue line that will retire each · the `/styleguide` route named as staying dev-only, deletable at the user's word · what is still `[needs verification]`.

State that this gate **no longer applies** to later pages — from here on what binds is Section 5 and the component rules in `ui-build`.

Close by reminding the user that the commit waits for their word.

---

# Rework and ratify paths — a repo whose UI already exists

## R0 — Preconditions

```
Skill build   : [raizen-hub x.y.z — read from this plugin's own .claude-plugin/plugin.json]
PRD.md        : [present / missing]
Section 5     : [filled / empty / absent]
Platform      : [from Section 1 Surface — web, or the platform named there; a non-web value routes every browser-named check below to that Surface's Proof profile line]
Register      : [first visit / tenth use / both, per page group — derived from Section 2]
Design material : [impeccable present/absent · frontend-design present/absent — both Required]
Branch        : [name · clean or has uncommitted changes]
UI components : [file count]
Leftover      : [none / canvas alive / pass applied — from src/design-canvas/ and git state]
Path          : [rework / ratify / re-entry — from the routing below]
Flow          : audit → [repair · overhaul · ratify] → reference slot, alone →
                direction frames + pick, unless a reference or brand palette pinned
                the direction → rest of the taste batch → stack questions →
                design plan → install → canvas rounds → gate → pass (isolated)
                → verify → close
```

**The block is printed on every invocation** — fresh, re-entry, or ratify — before any work beyond the reads that fill it. A session that starts editing, or even auditing, without having shown this block has routed itself in the dark, and everything it concludes about where the flow stands is a private guess the user never saw.

The `Design material` line exists for the same reason the `Skill build` line does: both skills are Required installs, they carry the craft rules `taste.md` and `ui-build` no longer state, and a session missing one writes its options out of the very defaults that material exists to close. **An absence is asked, not merely printed** — `taste.md` holds the rule and the question's contents, and this row is the step that fires it. The session still does not block: continuing without the material is one of the two answers, and a redesign that refuses to start until an npm install lands costs more than the gap does. What changed is who spends the material — the user, in a dialog naming what is lost, instead of a row nobody read.

The `Skill build` line exists so a stale install is visible before the pass, not after: rules fixed in the toolkit reach an app repo only through `/plugin update`, and a session on an old build re-makes exactly the mistakes the fix closed. The user sees the version and decides; the skill does not block on it.

**Re-entry is a gate, never an inference.** A leftover from a previous rework — `src/design-canvas/` still present, or a pass already applied on a branch or in the working tree — means this invocation *may* be a continuation, and prior-session summaries or repo state make that likely, not decided. When the `Leftover` line is not `none`, one mandatory AskUserQuestion follows the block, before any other work:

- **Continue** — resume the unfinished flow at the step the state shows: a pass applied but unverified resumes at R8; a canvas ratified but not promoted resumes at R7; a canvas mid-rounds resumes at R5. Announce the resumed step and what remains before touching anything.
- **New rework** — the full flow from R1, exactly as a first run: audit, repair-or-overhaul, interview. The leftover canvas is an audit finding; its deletion is proposed at the same chat-stop confirmation R8 uses, never assumed.
- **Stop** — report the detected state in one block and close.

A session that skips this dialog and routes itself — because the state "obviously" says where the flow stands — re-makes exactly the mistake this gate exists to close: the user watches edits land without ever having chosen the path.

`PRD.md` missing → **STOP.** An app with no PRD has no prior intent to protect and nothing to read the audit against. Point to `app-settle`, which reads the directory and picks its own mode.

Two readings decide the path, in this order:

| Section 5 | UI components | Path |
|---|---|---|
| Filled | any | **Rework.** R2 asks repair or overhaul |
| Empty or absent | none | **STOP** — nothing built, nothing to audit. This is `design-settle` |
| Empty or absent | present | **Ratify.** R2 is not asked; go to R2b |

That third row is the `app-settle` document-mode case: an app whose visual direction was never decided by anyone, only accumulated. It gets the same audit as any other, and then every entry is put to the user before it becomes a norm.

**Working tree not clean → say it and carry on.** Name the dirty paths in one line. The pass no longer runs in this tree — it branches from a committed base — so what a dirty tree costs is the base itself: uncommitted work is invisible to the pass's branch, and the promoted app will not carry it until the user commits and the branches meet. Advice, not a gate: the user decides.

Branch `main` → STOP. The git guard will refuse it, and that refusal is correct.

## R1 — Audit, before asking anything

Read what the code actually uses, not what the PRD says. Report one block:

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
Component library   : [name and version, from the dependency file]
Repeated labels     : [longest · median · how many repeat per screen]
Supporting text     : [how many paragraphs · the longest in sentences]
Frame inventory     : [routes counted from the router · parts and states named per route,
                       or `routes only — the running app could not be walked`]
Deviates from S5    : [list, per rule broken]
Components affected : [file count that will be touched if tokens change]
```

That last number matters most — it decides the size of the final pass, and the user is entitled to see it before deciding anything.

**The `UI stack` row is the canvas's import whitelist** (`canvas.md`, declared stack). A job the brief needs that no installed engine covers becomes an install question at R4; an engine installed but unused is a finding.

**The walk may also expose the logic layer bleeding** — handwritten data-fetching in UI files, hand-parsed dates, unvalidated inputs. That is not this skill's work: make the `logic-settle` offer under that skill's own rule — evidence, cost, and recommendation in one AskUserQuestion — and carry on with the audit either way.

**While walking the pages, screenshot one page per archetype at desktop width** — captured per PRD Section 1's Proof profile: the browser for web, the profile's Visual line elsewhere. R8 compares the finished pass against these; without a before, "it looks redesigned" is an assertion nobody can check. The screenshots are for that comparison and the judgement's before/after — they are not looked at while the canvas is drawn.

**The same walk writes the function inventory** — every function the app carries, one line each, page-agnostic: what can be done, not where it sits or how it looks. In an overhaul this list is the canvas's brief-floor (`canvas.md`), and collecting it here is what lets the drawing phase keep the old pages closed: the audit is the last time they are opened before the pass.

**The same walk writes the frame inventory** — per route, the parts and states that render there, names only: the table, the filter row, the add dialog, the detail panel. **Routes come from the router file itself, never from memory**, so no page can be absent from the list; the walk then says what each one holds. In an overhaul this list is what the canvas must cover — a part missing from it is a part the canvas will not draw and promotion will silently delete, and that loss is invisible to R8, whose diff compares the canvas against its own promoted page rather than against the page it replaced. **States real data cannot produce are listed anyway** — loading, empty, failed, and every role branch — because `ui-build` requires them of every component whether or not the walk could reach them. Names only, never pixels: the screenshots stay closed while the canvas is drawn, and this list is the one thing that crosses into it.

**The app could not be run, or there are no credentials → say so, here and at R6.** The inventory is then routes only, and the gate carries one line — `frame coverage unverified — the running app could not be walked`. A layer skipped in silence reads as a layer that passed.

The **Component library** row exists because the library question builds its options from measured numbers; **Repeated labels** and **Supporting text** are measured so the canvas's copy decisions are judged against real counts rather than guesses (`interview.md`, the designer-settles list). Measuring them here means the interview never stops to go looking.

**The `Slop detectors` row is deterministic and is the only row here that is** — and it runs only where the Surface is web technology, per `canvas.md`'s rule; a native Surface reports `n/a — native surface` here and at every later detector step. Run `impeccable`'s detector over the source tree and report both numbers. It is a **source-tier** scan: the rules that need a rendered page — measure, touch target, occlusion, nested containers — do not fire here, and R8 runs the full set against the running app. Its hits are **findings**, never repairs made on the way past: a finding becomes a Section 5 line only once the user ratifies it, like every other line in this block. `impeccable` absent → report the row as `n/a — not installed` and say so in the same breath.

**Token health** needs the library's own slot list, read from the installed package rather than remembered. Three numbers: tokens defined but never read, roles sharing one value, and semantic slots the theme file left unmapped. An unmapped slot means the app has been carrying a palette nobody chose, and it surfaces nowhere else in this block.

**An app on a stock Section 5 is the exception**, and Section 5 is read before this row is computed. A legacy repo whose Section 5 adopts the library defaults unmodified (a `design-settle` mode since retired — `prd-structure.md` holds the shape) has no theme file on purpose: report the row as `n/a — stock` and count no unmapped slots. Every slot there is unmapped by design, and reporting them as findings would push the user to write the very theme file that Section 5 refuses.

A deviation from Section 5 is a **finding**, not a reason to change Section 5. Some of it may need fixing without any redesign at all — offer that as the cheaper path when the audit shows the problem is deviation, not direction.

**Section 5 is audited too, not only the code.** Two roles named separately at the same value are one decision written twice, and every later session has to guess which one applies here. That is a finding against the PRD rather than against the code, and merging them is repair work: it changes no visual direction, so it needs no overhaul.

**A page holding too little is not a finding, and not this skill's work.** The audit walks every page, so pages that answer very little are seen here — a screen on correct tokens, correct icons, correct spacing, and still mostly empty. That code breaks no rule. It renders faithfully a content decision nobody ever made, and no styling pass can invent one: what a screen should hold is a product decision belonging to the user.

Do not report it as a deviation, and do not fill it. Hand it to `build-flow` Section 4, which derives candidate content from PRD Sections 2 and 3 and puts it to the user as a proposal — bound items as a statement, optional ones pre-selected to be cut. Name which pages were handed over, and carry on with the audit.

**What is out of scope is the content, not the layout.** In an overhaul the page is not exempt from the pass: its shell and arrangement are rebuilt to its archetype like every other page, using only the content it already has. What stays with `build-flow` is deciding what *else* the page should hold.

**Section 5 without an archetype table is itself a finding** — apps older than the archetype rule have one shell decision and nothing about what pages hold. Derive the table from the routes that exist (grouped as `interview.md`'s archetype rule describes, usually 4–7 archetypes), and present it for ratification the way R2b presents measured values: ratify or correct, never adopt silently. A ratified table enters Section 5 at repair scale — it records what the pages already are, no visual direction changes — and every page falling far short of its archetype goes to `build-flow` Section 4 through the hand-over above, one `QUEUE.md` line each. Where the app has no `/styleguide` route, offer generating one as `design-settle` R6 specifies; the user decides.

## R2 — Repair or overhaul

**Ratify path → this step is not asked.** There is no Section 5 to repair against and none to reopen. Go straight to R2b.

One question, two options, with a recommendation:

| Choice | What changes | Questions asked | Components touched |
|---|---|---|---|
| **Repair** | Zero new norms — only bringing code back in line with the existing Section 5 | None | Only the deviating ones |
| **Overhaul** | **Section 5 is rebuilt from zero, as `design-settle` would write it** — every line re-decided, archetype shells and visual-direction prose included; today's values survive only as *keep* answers. The app looks redesigned afterwards, not retuned | The taste batch with a keep option per slot (one turn), the stack questions, then the canvas from its answers (see `canvas.md`) | Every page, replaced by its canvas file |

There is no third option that narrows the scope, because **every question carries a *keep* option** (see R3). Answering *keep* to the parts you do not want touched is what narrowing looks like here — scope is narrowed by answers, not by a mode chosen before the user has seen a single question.

**Recommendation:** repair, when the audit shows Section 5 is actually still right and the code is what strayed. Reworking a norm that was never followed solves nothing — it just produces a second norm that is also not followed.

**Consequence:** quote the affected-component count from the audit, and state that overhaul includes the component-library question. Answering that one with anything but *keep* rewrites every component whatever the tokens say, and revokes the stack lock recorded in `CLAUDE.md`.

**State also what overhaul promises: the app looks different afterwards.** Name the pages the audit handed to `build-flow` — their shells will be rebuilt like every other page, but how much they *read* differently is capped until their content proposal lands, and the user hears that before choosing, not after the pass.

Repair → jump to R6; the gate there shows the findings instead of a canvas. Section 5 is not touched, with one exception: two roles the audit found at the same value may be merged, because that removes a duplicate rather than adding a norm. The merge is still an explicit user decision, approved line by line like any other Section 5 change.

## R2b — Ratify — ratify path only

Section 5 is empty, so the code has been making these decisions on its own. Walk every entry in `interview.md` once — the taste slots, the stack questions, and the derived values its designer-settles list names. The audit decides **how** each entry is put to the user, and that is the whole design of this step:

| What R1 measured | How the entry is put |
|---|---|
| **A coherent value** — a real scale, one family, a consistent radius | **Confirmation.** Show the measured value; first and recommended is an option naming the action plainly — `Keep this value — 8px` — never this file's vocabulary |
| **Nothing coherent** — scattered raw values, no scale, contradictory usage | **A real question**, asked exactly as `design-settle` asks it |

The split is what keeps this honest in both directions. Re-interviewing everything produces answers that contradict the running app, and a PRD that does not describe its own app is worse than no PRD. Ratifying everything writes the stylesheet's accidents into the PRD as norms. Where the code has a real answer the user checks it; where the code has none, nobody may pretend otherwise — offering a "measured value" assembled from noise is inventing a norm and labelling it a finding.

**Batch the confirmations and batch the questions.** A confirmation carries a measured number and the user is checking it rather than deciding it, so several fit in one call. An entry with no measured basis is an ordinary interview question — grouped with its peers in one call (taste entries with the taste batch, stack entries with the stack batch), sequential only across a real dependency.

Every entry goes through the **AskUserQuestion tool** either way, never prose — a prose question at the end of a turn is skipped in auto mode and answered by no one.

**A ratified value is written into Section 5 exactly as measured**, with no tidying on the way in. Rounding a 14px step to 16px because the scale reads nicer is a change of direction disguised as transcription. If it should be 16, that is a question, not a ratification.

An entry the user neither ratifies nor answers → `[needs verification]`. It stays out of the pass and `ui-build` keeps blocking on it. That is the correct outcome: an undecided norm must not become a decided one by default.

### Where the ratify path lands

Decided by the answers, not chosen:

| Outcome | Continue at |
|---|---|
| Every entry ratified as measured | **R6, as repair.** Section 5 now states what the code already does, so the only work left is the strays the audit found |
| Any entry answered differently from the measurement | **R3, overhaul.** Those entries are real changes — they get the old-versus-new diff and the canvas, like any other change of direction |

Nothing else in this skill behaves differently for this path.

## R3 — The interview — Overhaul only

**Load `design-settle`'s `references/taste.md` and the two Required installs, `impeccable` and `frontend-design`, first, before a single option is written** — same reason as there: the batch's options are the first place taste is exercised, and options written out of the defaults are a menu the user can only pick from. On this path the pull toward the defaults is stronger, not weaker: the audit has just filled the session with the app's current values, and every one of them is a default asking to be offered back.

Read `interview.md` in the `references/` folder of `design-settle`. The rules are identical: the reference slot alone in its own turn — its options real products named by you — then the direction frames wherever no reference and no brand palette pinned the direction, then six or seven slots in one turn — options invented for this app from the model's own design knowledge, every slot carrying "Decide for me", one marked recommendation per slot — then the stack questions, their candidates verified per `library-rubric.md` and `engine-rubric.md`. The canvas is drawn from the answers as the baseline and may still improvise anywhere, every departure from an answer tagged and confirmed at the judgement; its ratified values enter R6 as the *new* column of the diff.

**Escalation:** a canvas that misses twice re-opens the taste batch with sharpened options (`canvas.md`).

**Engine dialogs fire on triggers, never on a schedule** (`engine-rubric.md` of `design-settle`): a need the user or the PRD names, a job the product draft implies, or an engine the audit indicts. An installed engine is already decided — it is the declared stack, and no dialog re-opens it without an indictment. Swapping one rewrites every page that uses it, so it is priced and recommended the way the library question is — *keep* first, and keep stays the recommendation unless the indictment stands. A need that only emerges mid-canvas is drawn tagged with the no-engine rendering and settled at the judgement, per the rubric.

Six differences from `design-settle`:

**Every slot and stack dialog carries a *keep* option, written first.** Labelled `Keep — <the value in Section 5 today>`, and it does not replace the invented options the slot must still offer. A value that is only a recommendation is a suggestion; a value written as an option is a choice. Answering *keep* throughout ends the session with the PRD unchanged. A derived value defaults to the value Section 5 holds today, reported on its line — cancelling it opens a dialog with the same keep option first.

**Keep stays an option, but it stops being the recommendation.** The user chose overhaul, and that choice already says the current sum is wrong — recommending every current value back re-litigates it, and an overhaul answered by its recommendations then changes nothing. For the look-bearing slots — direction, palette, surface, density, typography, shell — the recommendation is a real departure, anchored in the reference the user named or the chosen direction, and it names what it departs from. **And the canvas that follows draws blind to the current look** — `canvas.md`'s full-overhaul rule: today's design is not an input, **Section 5's own prose included** — its signature, ornament rules, and shell column bind the canvas no more than the CSS does; only the brief and the answers are inputs. The audit's numbers price the pass and power the before/after, never anchor the new direction. The library question is the one exception: its recommendation stays *keep* unless the audit indicts the library itself, because answering it otherwise rewrites every component for reasons of cost, not of look. Derived decisions derive from the new answers, not from the old Section 5 — `interview.md` states the same split, and an overhaul that reads old values into its derivations has re-imported the design it was told to leave outside.

**The new Section 5 is rebuilt from zero, not patched.** Every line of it traces to the same three sources `design-settle` names: a new answer, a derived decision reported to the user, or a canvas value the user ratified. A line of the old Section 5 that none of the three re-created — a signature paragraph, an ornament rule, a reference-app list — does not carry over by default: it survives only through a *keep* answer or a canvas re-ratification, and otherwise it appears in the R6 diff as a removal. Silent carry-over is the mechanism by which an overhaul stays caged by its predecessor, and one ratified sentence is enough bars.

**The archetype table is reopened with everything else.** Under the new direction, run the archetype derivation again and present each archetype old shell beside new for ratification, the way R6 diffs a token. This is where an overhaul stops being a repaint: the rooms move, not only the walls. A user who ratifies every shell as it was is told plainly that the pages will read similar afterwards.

**A reference is drawn out, not waited for — and here it has its own slot.** A redesign always has a reference in the user's head, so the taste batch's first question asks for it directly, with real products as options rather than an invitation buried in the lead text (`interview.md`, the reference slot). Where Section 5 already records one, it takes the first place as `Keep — <it>`; where it does not, the audit's own reading of what this app was reaching for is what the proposed products are argued from. A named answer becomes the anchor the canvas designs toward and the list the canvas is measured against at the judgement — drawing it out here is what cuts rounds later.

## R4 — Install, before anything is drawn — Overhaul only

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

## R5 — The canvas: rounds until final — Overhaul only

Drawn and judged under `canvas.md` entire: the direction frames are already picked, so this step opens on files written production-grade — every state drawn, fixtures in one contract-shaped file that closes arithmetically, imports only from the declared stack — the three-scan self-check before every round (imports · the render · the arithmetic), the signature drawn, tagged, and settled in a question of its own, tagged departures and proposals, the judgement through AskUserQuestion, two rounds then escalation. The design plan is narrated before drawing here too, under `design-settle` R3 — after the pick where frames ran; `references/taste.md` and `frontend-design` have been in hand since R3's interview. **Frames rarely run on this path**: every slot here carries `Keep — <today's value>` and the look-bearing slots carry a real departure as the recommendation, so a Direction left at "Decide for me" is the exception rather than the norm.

**Detector findings are not an input to a round.** `impeccable`'s hook fires on every canvas file written and asks, in its own words, to be told what was fixed. Do not answer it here. The three self-check scans are the only gate before a round is shown, and the canvas is pre-ratification — a `nested-cards` or `monotonous-spacing` hit may be the very direction the user is about to choose, and acting on it changes what is being judged without the user ever seeing it happen. Carry the hits to R8.

**The PRD is not touched during rounds, and neither is any production file.** The foundations board is the living draft of every value; the user inspects it there, not in a document. The `/styleguide` route keeps rendering the old theme until the pass — the canvas never looks at it.

This phase only adds files under `src/design-canvas/`, so it runs safely beside any other session — days may pass between rounds without holding anything else up.

## R6 — The gate: one approval before anything real changes — both paths

Everything so far has been drawing and answers. This is the **single stop** where the user authorizes the change — Section 5, the file plan, and the known deviations together, because approving pixels is not the same as approving which files move.

**Overhaul** — one message, four parts, then a hard stop answered in chat — never an AskUserQuestion:

1. **Section 5 as a diff.** Only what changes, old value beside new — and removals are changes:

```
Accent color : blue #2563EB  →  green #059669
Text steps   : five          →  four (merge section title and body)
Radius       : 8px           →  0
Signature    : ledger seam, sole vertical rule  →  removed
```

A line of the old Section 5 that no new answer, derivation, or canvas ratification re-created leaves through this diff as `→ removed`, never by omission. Arriving here from R2b, the *old* column is the **measured** value and is marked as such — `Radius : 8px (measured) → 0`; there is no prior Section 5 line to diff against, and writing one as if there were would claim a decision nobody ever made.

2. **The file plan.** Every page line names its source: `replaced by its canvas file`, or `retoken only — no canvas frame` (a stray component the canvas never drew). Two labels per path, never a third. **On the overhaul path `retoken only` is not available at all**: a component the canvas never drew is `deleted`, and whatever still needs it is drawn. An overhaul that repaints a file it never redrew has left the old design standing under new colour, in the one pass that exists to remove it — and a thin passthrough whose child was redrawn is deleted rather than framed, its callers reaching the redrawn child directly. Reaching this plan with a file unaccounted for is R1's inventory failing, never a file that needs no verdict. **Shared canvas files carry their own line under the production path their header names** — a plan that lists only pages leaves the largest promotions unwatched, and a composition promoted as loose parts downgrades every page built on it. The plan closes with its **seam points** — where the pass may stop between sessions, read off R7's fixed order rather than chosen, and never an estimate of time: what the user needs before approving is where the app will sit half-migrated, not how long it takes. A page whose canvas file exists is replaced by it; listing it `retoken only` is proposing to break the ratified canvas, and that line is put to the user as its own question, never slipped through inside the list. Chrome and shared components created or replaced, styling files, and `UNTOUCHED` files are all listed — a file that should have been listed and is not is a finding, not good news.

```
PASS — [n] files
LeadTable.tsx    replaced by its canvas file
wizard.tsx       → src/components/import-wizard.tsx · shared by 7 pages · replaced by its canvas file
StatusChip.tsx   retoken only — no canvas frame · 4 status colors updated
index.css        11 tokens replaced · 3 deleted · fonts now load here
App.tsx          replaced by its canvas file (chrome)
UNTOUCHED        PhoneContact.tsx
```

3. **The detector's R1 count, and what the new direction does to it.** One line: the audit's number, and how many of those hits the canvas removes by construction. The user is about to approve a pass sized in files; this is the one number saying what it buys beyond the look. Hits the canvas does not remove are listed by rule — they survive the pass and return at R8.

4. **What approval orders, then what it contradicts.** Ratified elements whose data does not exist yet come first, one line each — element, page, and the work it orders (column · RPC · migration). **Approving the gate orders that work**, so its cost is read here rather than discovered mid-pass; these are not deviations, because the user has decided to build them. Then the deviations: every canvas element the real flow contradicts, and every real control the canvas never drew (`canvas.md`'s canvas-error rule) — one decision line each, answered here, never absorbed silently. **And what approval removes is its own group, confirmed item by item** — every function or control leaving the app because the canvas does not carry it. A blanket *approve everything* covers the other two groups; not this one. A wrong addition is visible on the screen the moment the page opens, and a wrong removal is visible to nobody.

**The gate is a chat stop, not a dialog.** End the turn on the four-part message and wait for the user's reply in chat. An AskUserQuestion here covers the very summary being approved — the user answers the dialog without having read the diff. Ending the turn is what keeps this safe in auto mode: nothing proceeds without an answer. The ban on prose questions elsewhere in this skill covers questions that let the turn carry on, not a gate that stops it.

The user may approve some lines and reject others, naming them in the reply. Rejected values return to the canvas rounds (R5) and nothing is written anywhere; approved everything → the pass. Nothing changed at all → say so and close at R9.

**Repair** — the same gate shows the findings list instead:

```
REPAIR — [n] findings
1  Usage.tsx:185-188   gradient text           impeccable · craft-floor Refuse
   3 sentences  →  removed
2  StatusChip.tsx:19   label 15 chars          S5 · Repeated label length
   "Belum dihubungi"  →  icon only, text to aria-label
```

STOP and wait for approval per item. A rejected item is not silently dropped — it stays a finding and is reported again at R9.

## R7 — The pass: isolated, one session

**Branch first.** Create the pass's own branch or worktree from a committed base (`design/rework-<date>` or the user's naming). Parallel work continues in the main tree untouched; the canvas folder, if untracked, is brought along into the worktree. Revert of the whole overhaul is now one move — drop the branch — available at the user's word at any point, closing the session at R9.

**First act: write Section 5** — the approved text, in full, rebuilt from zero. Then `CLAUDE.md`'s Component library row if the library answer changed. This is the only moment the PRD is written.

**The gate block travels with the branch.** The pass's first commit carries it in its message body — Section 5 diff, file plan, ordered work, and the deviations the user answered. Chat scrollback does not survive the session, and a later session that cannot read what was approved cannot tell drift from a decision; neither can the user. `git log` is where this repo already keeps that kind of memory.

**Second act: the freshness check.** Time may have passed between ratification and this session, and parallel work may have changed the app. Re-walk the function inventory against the current code; a flow that changed since the canvas was ratified is a new deviation line, put to the user **before** its page moves — the canvas is frozen, so reality has to win by decision, not by silence.

Then one session, every approved file, in an order that cannot be reversed:

1. **Foundations.** The theme files take the new token values — old tokens **deleted**, not deprecated — and everything the canvas CSS carries beyond values lands with them: **the font loading itself** (link or package — then verify in the browser that the computed font-family resolves to the loaded webfont, not a fallback; a token grep cannot see a font that never loads), element-level rules, shadows, motion durations. The five styling-file rules in `design-settle` R6 bind here too: the two-layer palette the canvas ratified, every semantic slot mapped, no unread tokens, duplicate roles collapsed, both theme files in the same edit.
2. **Chrome and shared components, from the canvas chrome.** Each shared component a canvas page imports lives in the production chrome before any page importing it counts as moved — the canvas markup is the component; the production logic (auth, navigation state, data) is wired into it, never the reverse. **Where they land follows `ui-build`'s placement rule**: the components that hold Section 5 rules in one file, a component carrying a flow of its own in its own file. Promotion is the moment that file comes into existence, and every later session is told to read it — scattering the set across fifteen files leaves that instruction pointing at nothing.
3. **Pages — the most data-dense page of the primary role first.** Each canvas file **copied to its real path**, the canvas wrapper removed, the fixture import swapped for the real data layer. The markup body does not change — that is what R8 will diff. Checked at both widths for survival of real data: holding → report and continue; the first collapse → stop, a rework round of that page, two at most, then Section 5 reopens through `canvas.md`'s escalation.
4. **Components not on the canvas** — **repair path only**: retoken until zero raw values remain, and a component prop or theme value departing from what the library ships goes back to the library default in this same pass, unless a Section 5 line requires the departure. **On the overhaul path this step is empty by construction** — R6 gave every such file a `deleted` verdict. A file still standing here is a failed inventory to report, never a file to quietly retoken.
5. **`/styleguide`** — part of the pass: archetype cards updated to the ratified shells, every component the pass created rendering there, held to `design-settle` R6's done-check.
6. **Assets** locked to the old colors: inline SVG, favicon, images carrying brand color.
7. **The old library and engines are removed**, if their decisions changed.

**The UI code is the pass's to rewrite — the behavior is not.** What must come out unchanged is the business behavior — the queries and mutations called, the guard conditions, the route paths, the outcome of every action a user can take. Do not slip in unrelated fixes: a redesign that also tidies logic produces a diff nobody can read, and one mistake will hide among hundreds of legitimate changes.

**Detector findings are deferred here too, and this is where it matters most.** `impeccable`'s `craft-floor.md` tells the model to act on hook findings as it edits; inside this pass that instruction is overridden. The canvas is already approved, so a hit is a difference the session would prefer — refused by the rule below, not weighed. Collect them and report them at R8, where there is already a fix loop and the user can see the whole list at once.

**The approved canvas is the specification, and the pass implements it rather than negotiating with it.** An element the canvas drew lands as drawn; an element it did not draw does not land, and prose the canvas left out is deleted rather than carried over — the user answered that by approving the drawing, so asking again re-opens a settled decision and is how the result drifts. A difference the session would prefer is refused, not raised as a question.

**One exception, and no other: an element the user ratified whose data does not exist yet.** The pass writes no query for it — that stays forbidden. It promotes the element **rendered empty and labelled as waiting**, and writes one `QUEUE.md` line naming the data it needs. Dropping it silently is a failed promotion, and so is hiding it behind a flag: a page that reads finished while an approved element is missing is the one state nobody can see.

**One thing still stops the pass**, and it is the freshness check above plus this: a drawn element that would make the app claim what it cannot do. That is a `build-flow` stop, not a design question.

**Repair** runs here too, on the same isolated branch: fix the approved findings, nothing else.

## R8 — Verification: evidence, not eyes

A claim of parity from the session that produced the code is worth nothing on its own — every check below leaves something the user can inspect. All of them before reporting done:

- **The build passes.** It does not → stop, fix it, do not report done.
- **The structural diff per canvas file — the primary evidence.** Every canvas file, not every promoted page: a page whose body delegates to a shared file diffs empty, and the diff that matters moves to that shared file, under the production path its header names. The differences must be confined to the data seam — the fixture import swapped for the data layer, plus its loading and error wiring — and to lines the user answered at the gate. Any other difference is a failed item to fix now, whichever side reads better. Report the verdict per file; a file whose diff cannot be shown is not verified.
- **Computed styles probed in the browser.** The fonts resolve to the loaded webfonts, not a fallback stack; spot-check token slots on live surfaces against the theme files. (The web profile's check — a platform whose Proof profile names no browser verifies the equivalent through its Visual line, and says what could not be verified.)
- **The rendered structure matches, counted.** Both sides are live in the same dev server — the canvas at its dev route, the page at its real one. Read the element tree of each page body (element names and class lists, **text and numbers discarded** — discarding the text is what takes the data out of the comparison) and report one line per page: `canvas n · live n · differs n`. Anything above zero names the extra or missing elements and is a failed item now. "Richer than the canvas" is drift wearing a compliment, and this count is what sees it — the prose verdict this bullet used to carry did not. Chrome the two sides do not share is excluded and said so; a page whose count cannot be produced is not verified.
- **Zero raw values remain.** Search again for hex, font sizes, and raw spacing across every component.
- **The detector runs against the running app, and its count is reported beside R1's.** `impeccable`'s full rule set needs a rendered page, so this is the pass where it is complete — point it at the dev server, not only at `src/`. Every hit is triaged in the report: fixed, or left standing as a finding with one line saying why. A hit left standing is not a failure of this step; an unreported one is. `impeccable` absent → say the check could not run, and do not report the step as passed on silence.
- **Contrast still passes** the Section 5 target, for every new color pair — the ratio **computed**, never recalled, per `canvas.md`'s Ratification, and every semantic dark shade clearing 4.5 against its own light shade.
- **The fixtures close** on any page still running on them, and the `/styleguide` foundations render as specimens rather than as a table of names and values — `design-settle` R6's done-check, which this pass's styleguide is generated to.
- **The signature survived promotion**, on the pages that carry it. A signature that exists on the canvas and not in the app is a failed item, not a simplification.
- **The file plan matched.** Every file listed at R6 changed, and no file outside that list did.
- **The seeded walk.** Seed `[CLAUDE]`-prefixed rows first — an empty database renders empty states the canvas never drew, and a parity claim over empty tables is void. Then walk the densest page at desktop and at the lower bound, and compare one page per archetype against its R1 screenshot: every archetype reads redesigned, unless everything behind it was answered *keep* and the gate said so.
- **Function parity holds.** Walk the R1 function inventory line by line: every function is still reachable **at both widths — a control hidden below the breakpoint is a missing function at the minimum width, not a responsive choice** — wherever it now lives. A line missing everywhere is a failed item to fix now, unless the user cut it at the judgement and the gate said so.

Any of them fails → fix it in the same session. A half-finished rework is worse than none: the app still runs, so nobody knows it is broken.

**All of them passing earns the right to propose deletion — never to delete.** The canvas is removed only through an explicit confirmation at a chat stop — never an AskUserQuestion, which would cover the verdict being read: report the diff verdict per page, invite the user to walk canvas and app side by side at `/design-canvas`, then end the turn and ask whether the canvas and the seed rows may go. Only a granted confirmation deletes — the page files, the entry route, the foundations board, and the canvas CSS together, per `canvas.md`'s lifecycle. The user refusing, or naming any page, turns each named page into a failed item of the pass to fix now; the canvas stays alive until a later confirmation clears it.

## R9 — Close

The close carries the detector's before and after — R1's count beside R8's — and names every hit left standing with the line that justified it. A rework that reports no number has claimed the app is better without measuring it.

One block: the Section 5 lines that changed · files touched with their count · files `UNTOUCHED` · items the user rejected, still standing as findings · the canvas outcome and how many rework rounds it took · the verification results, the per-page diff verdicts included · what is still `[needs verification]`.

**A pass this session could not finish is written down, not implied.** Every page not yet promoted, and every verification item not yet passing, becomes a `QUEUE.md` line — one each. A truncated pass must read as unfinished in the repo itself; the canvas stays alive as the reference until those lines clear.

**Propose the commit, on the pass's own branch** — a diff of this size deserves a commit of its own, with nothing else riding along inside it. The commit waits for the user's word; merging the branch back is also the user's move, and it is the single point where this work meets whatever parallel sessions built in the meantime. Never push, never open a PR.

Nothing changed — every answer was *keep*, or the canvas was reverted → say that in one line and list the audit findings that remain. A session that changes nothing has still produced the audit, and that is worth writing down.
