---
name: design-init
description: Decide the visual direction and component library of an app whose PRD Section 5 is still unwritten. One single-turn taste interview — eight slots (reference, direction, palette, surface, density, typography, motion, shell) whose options are invented for this app from the model's own design knowledge, the reference slot naming real products as options, every slot carrying a "Decide for me" option — then the stack questions that gate the install (component library, icon pack, engines by trigger, verified live). A temporary in-repo canvas — real component library, canvas-owned theme, the user's feature brief — renders the answers as every page of the app, expanding thin briefs into a full product with tagged feature proposals and tagged departures. Ratifies the canvas, writes the rules and the screen-archetype table into PRD Section 5, writes the concrete values into the styling files, generates the dev-only /styleguide route, then promotes every canvas page into the app's real pages on contract fixtures — real data arrives page by page through the build queue. Use before the first UI component of a repo is written, or when PRD Section 5 is still marked as unverified.
---

# design-init — set the visual direction once, in code

Bootstrap produces a `PRD.md` with an empty Section 5. This skill fills it, then **proves it as the real app** — not a picture, not a description.

Run **once per repo**. After the canvas is ratified and its pages promoted, later pages are bound by Section 5 and the component rules in `ui-build`, with no further gate.

The step skeleton below is `design-rework`'s, on purpose — one flow to learn, two skills. The deltas are marked where they are structural: no audit here (nothing exists to audit), no diff gate (no old values to protect), and no isolated branch (a fresh repo has no parallel work to disturb).

## Hard limits

`PRD.md` Section 5 is the only part of the document written. **Do not** create `MASTER.md`, `DESIGN.md`, `design-system/`, or an interview summary as a file. If another skill in this session produces a document, it is not committed and not referenced.

This is one of only two paths allowed to write Section 5, and only while Section 5 is still empty. Its contents come from the user's answers, not from the agent's taste and not from another skill's output. A Section 5 that is already filled changes only by the user's decision — see `prd-format` in `raizen-norms`.

**The canvas is the final front-end, staged** (`references/canvas.md`). Its files are the future pages, written production-grade — the user approves code, not pictures, and promotion relocates that code instead of imitating it. The one legitimate difference between a canvas file and its live page is the data flowing through it.

Do not commit and do not push. Staging is fine; the commit waits for the user.

Not decided by the user → `[needs verification]`.

## Step 0 — Preconditions

Check and report one short block:

```
PRD.md      : [present / missing]
Design mat. : [impeccable present/absent · frontend-design present/absent — both Required]
Section 5   : [empty / already filled / product without UI]
Kind of app : [from Section 1]
Platform    : [from Section 1 Surface — web, or the platform named there]
Primary role: [from Section 2]
Reading     : [one sentence — see Step 1]
Flow        : load taste.md + impeccable + frontend-design → reading → taste batch →
              stack questions → design plan (narrated; only its axes
              where direction frames will run) → install → direction frames + pick,
              where the direction is still open → canvas rounds → ratify + Section 5
              → promotion (all pages) → verify → close
```

`PRD.md` missing → **STOP**, point to `app-settle`.

Section 5 already filled → **STOP**, ask whether the user really wants to rework the existing visual direction. That work belongs to `design-rework`.

**Section 5 empty but UI components already exist → STOP as well.** This skill decides a direction before any code carries one. An app that already has components needs its existing values measured and put to the user, not overwritten by an interview that has never seen them. That is `design-rework` on its ratify path — the case a repo arrives in through `app-settle`'s document mode.

Product without UI → **STOP**, this skill does not apply.

## Step 1 — The reading

**Load the three materials first, before the reading sentence is written**: `references/taste.md` beside this skill, and the two Required installs, `impeccable` and `frontend-design`. `taste.md` names which of `impeccable`'s reference files carry the material and `canvas.md` draws the boundary; one absent is reported and does not stop the session. Step 0 has already routed, so nothing is read for a session that stops.

They come first because **the reading sentence is itself the first taste output** — its *leaning* clause is a judgement about how this app should feel, and the paragraph below says every slot's options are invented from the corrected reading. A leaning written before the material is read seeds every option that follows out of the same defaults the material exists to close, and the batch then offers the user a menu of them: a Typography slot offering Inter, a Direction slot offering a cream ground with a serif and a terracotta accent, a reference slot proposing whichever product came to mind first. **A choice never offered is not recovered by any later round** — the judgement can reject what was drawn, but it cannot reach an option that was never written.

Both are divergence guidance: they name the defaults that read as generated and the method for choosing a direction, never the direction itself; `canvas.md` holds the rule and where the line falls. No skill that prescribes a fixed look — a fixed palette, a fixed pairing, a card recipe — is read. They stay in hand for the rest of the flow: the design plan at Step 3, the canvas, the judgement.

There is no audit — nothing exists to audit; this step is its sibling. **Reading** is your own conclusion before asking anything, one sentence, shaped as: *"I read this as [kind of app] on [platform] for [who uses it], leaning [the feel that fits], because [reason from the PRD]."*

**The platform slot is not decoration.** `app-settle` already asked the platform and PRD Section 1 already holds the answer — it is never asked again. It rides in this sentence because the corrected reading is what every slot's options are invented from, so one word here is what puts the platform into all of them at once. Left out, the options arrive in the web's vocabulary and no later decision can tell that anything was lost.

Concluding first beats asking from nothing: the user only corrects what missed, and the correction carries more than an empty question would. A wrong reading is not a failure — it draws out detail that no question would surface.

State the reading, ask for correction, then continue. When the correction is asked through AskUserQuestion, **the full reading sentence goes inside the question field itself** — the dialog may render without the prose around it, so a question that points at text "above" can arrive pointing at nothing.

The slots' options and the canvas's values come from the model's own design knowledge of this app and its platform, sharpened by the three materials above, and the user's judgement on screen is what checks the result.

## Step 2 — The taste batch

Read `references/interview.md` and run its taste batch: **eight slots, two AskUserQuestion calls, one turn.** The options are invented for this app from the model's own design knowledge — no fixed list anywhere, and no research pass for taste — each option named in plain words with its consequence in parentheses, one real option marked "(Recommended)". Every slot carries **"Decide for me"**.

**The first slot is the reference** — the app or site this one should feel like — and its options are **real products named by you**, two or three that are arguable for this app, plus `No reference — explore freely` and `Decide for me`. It is asked first because a named anchor reshapes every option that follows, and the second call's options are written after the first is answered. A product the options missed, a screenshot, or a URL arrives through Other, and that is the best outcome rather than a deviation. `interview.md` holds the slot's own rules — what a named reference costs, and the line between setting a direction and reproducing an interface.

The answered slots are the user's preferences and the canvas's baseline; a slot answered "Decide for me" belongs wholly to the canvas's taste license. Either way the canvas may depart from any answered slot with a drawn, tagged, reasoned departure the user settles at the judgement (`canvas.md`), and the archetype table, the `/styleguide` route (Step 6), and real running pages are produced whatever was answered — what an answer changes is only where a value starts.

**Every question goes through the AskUserQuestion tool, never prose text** — the recommendation first and marked "(Recommended)", the consequence in each option's description, everything the user needs inside the dialog itself. This holds in auto mode too: a prose question simply ends the turn unanswered.

**Nothing the user did not choose is silent.** A "Decide for me" slot and every derived value surface as one line each with their basis — in the canvas assumptions block before drawing or the ratification report after approval — and the user may cancel any line; cancelling opens that value as a normal dialog. `interview.md` holds the list of what is derived and the floors that bind it.

**A canvas that misses twice escalates by re-opening this batch:** `taste.md`, `impeccable`, and `frontend-design` are re-read first (`canvas.md`), then every slot is re-asked with sharpened options built from what the two rejections taught — the reference slot with products chosen against what was rejected — and the canvas is regenerated fresh from the new answers, never patched.

## Step 3 — The stack questions, then compile into values

Read `references/library-rubric.md` and `references/engine-rubric.md`, then ask the second batch: the **component library**, its **icon dialog** when the library bundles none, and the **engine dialogs** whose triggers in `engine-rubric.md` have fired — nothing speculative; an app that trips no trigger hears no engine dialog. These are asked rather than improvised because they install code, and their candidates are **verified live** per the rubrics' duty — the one place research survives in this interview. The family rule in `interview.md` shifts recommendations toward already-installed ecosystems.

**Draft the full product before these dialogs close** — `canvas.md`'s expansion duty, run here rather than at drawing time, because the draft is what trips draft-implied engine triggers: it existing now is what lets every engine ride this batch and the install block close complete the first time.

Answers outside the options are always accepted. The user names something not listed → verify it the same way, use it, state its consequence if you know it, or say you don't.

### Compile into values

Compile the answered slots into the canvas's baseline: concrete hex values, font names, and icon entries. A slot answered "Decide for me" compiles to nothing — the canvas owns it.

The output is the canvas's **baseline, not a gate**. The user corrects values where they are visible: on the canvas, at the judgement. Waiting here for an approval would judge the same values twice.

### Then state the design plan — narrated, not gated

Both materials were loaded at Step 1 and are already in hand. **Write the plan out in this same turn, before the install block.** This is the step that separates a designed app from a competent average, and it is skipped by exactly the sessions that most needed it.

Five parts, short:

| Part | What is stated |
|---|---|
| Direction | Purpose · the one tone held · what makes this app memorable rather than adequate (`taste.md`) |
| Colour | 4–6 named values with their roles, and where they came from — a brand palette, a reference, or an accent chosen first and the neutrals pulled toward it |
| Type | The pairing and each face's job. Never the four `taste.md` names as failed choices |
| Layout | The shell and the composition in one or two sentences — where the density sits, what breaks the grid |
| Signature | The single element this app is remembered by (`canvas.md`, the taste licence) |

**Where the direction frames will run (`canvas.md`), this step states only their axes — and the plan itself waits for the pick.** One line per candidate axis, no palette values, no type pairing, no signature. A plan that names a palette before the candidates are drawn has already decided the vote it is about to hold, and candidates drawn around a published direction are the rigged set `canvas.md` forbids. The five-part plan is then written in the turn after the user picks, to the candidate they picked, and critiqued as below. Everywhere else — a Direction slot the user answered, a reference named, a brand palette to follow — the frames do not run and the full plan is written here.

**Then critique it against the brief before drawing, in the same turn.** Work through what a session with a similar brief would produce; any part of the plan that arrives at the same place is a default rather than a decision. **Revise that part and say what changed and why** — one line. A plan reported without that pass has skipped the only step in it that does any work.

**It is a narration, not a gate: state it and keep going in the same turn.** Do not end the turn, do not open an AskUserQuestion, do not wait. What it buys is a decision the user can object to before the canvas exists, and a direction this session cannot quietly drift off later — the judgement still settles every value on screen.

## Step 4 — Install, before anything is drawn

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

## Step 5 — The canvas: rounds until final

Drawn and judged under `canvas.md` entire: the direction frames first where the direction is still open, then files written production-grade — every state drawn, fixtures in one contract-shaped file that closes arithmetically, imports only from the declared stack — the three-scan self-check before every round (imports · the render · the arithmetic), the signature drawn and tagged, tagged departures and proposals, the judgement through AskUserQuestion, two rounds then escalation.

The PRD is not touched during rounds. The foundations board is the living draft of every value.

## Step 6 — Ratification: Section 5, the styling files, and `/styleguide`

**The styling files are scanned once they are written.** The values land from the canvas, so `impeccable`'s `design-system-*` rules have a theme to compare against for the first time here — run the detector over the styling files and the styleguide route before this step is reported done, and report the count. A hit against a value the user just ratified is a finding, not a correction: name it and leave it standing.

**Approving the canvas is the approval — there is no second gate here.** This is the delta from `design-rework`: no old Section 5 exists, so there is no diff to protect and no separate stop. The values behind the approved canvas are read and reported as derived decisions are reported — one line each, cancellable — then written (`canvas.md`, Ratification).

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

## Step 7 — Promotion: every page, on contract fixtures

**All canvas pages are promoted in one pass** — each file copied to its real route, the canvas wrapper removed, per `canvas.md`: element for element, chrome components first, the most data-dense page of the primary role leading. This is the same all-at-once promotion `design-rework` runs, with one structural difference: **there is usually no backend yet, so the pages keep their fixtures** — reshaped into `build-flow`'s contract form (`src/contracts/<page>.ts` for the types, `src/contracts/<page>.fixtures.ts` for the cases, per `references/contract.md` of `build-flow`). Real data arrives page by page through the queue; the fixture import is the marker of what is not yet wired.

No isolated branch is needed — a fresh repo has no parallel work to disturb; the pass runs in place.

**Every promoted-but-unwired page gets a `QUEUE.md` line** — `wire <page> to real data` — written by this pass. An app full of fixture-driven pages looks finished while every number on it is fake; the queue lines and the close block are what keep that visible. Where `logic-settle` already chose the data layer, its loading, empty, and failed states come from the chosen cache when wiring happens — never from a handwritten effect.

**The densest page is the bar.** `build-flow` Section 4 judges every later page against it — building it thin lowers the bar for the whole app. Its fixtures must include `bulk` and `messy` cases: a direction that only holds for five tidy rows has not been proven. `ui-build` binds every promoted page in full — tokens only, zero raw values, states drawn.

Page running → **prove it at two widths with screenshots**: the desktop breakpoint from Section 5 and the ratified lowest supported width. Capture follows PRD Section 1's Proof profile — the browser is the web profile's answer; a platform whose profile names an emulator or a window capture proves the same two bounds through it. No capture tooling → say so and report the profile's run target with both widths named — never claim the widths were judged without either.

**Rework rounds.** A page collapsing under its fixtures, or the user asking for a rework, is a rework round of that page. **Two rework rounds of the same page at most — a third does not run, and Section 5 reopens**: the taste batch is re-asked with sharpened options, and the canvas is regenerated fresh from the new answers, never patched. Section 5 changed → the styling values are updated with it, and the pages are rebuilt from the new tokens rather than patched.

## Step 8 — Verification: evidence, not eyes

Before reporting done:

- **The build passes.**
- **The structural diff per promoted page.** Put each canvas file beside its live page: with fixtures kept, the only legitimate differences are the removed canvas wrapper and the contract-shaped fixture import. Any other difference is a failed promotion to fix now.
- **Fonts load for real.** The computed font-family in the browser resolves to the loaded webfont, not a fallback stack — the canvas CSS carried the loading, and the production entry must carry it now.
- **Zero raw values** across every promoted page and component.
- **The styleguide passes its done-check** (the table in Step 6), its foundations rendered as specimens rather than as a table of names and values.
- **Every contrast ratio on the page was computed**, not recalled, and every semantic dark shade clears 4.5 against its own light shade.
- **The fixtures close** on every page still running on them — totals, percentages, bar widths, pagination — per `canvas.md`'s Coverage.
- **The detector ran against the running app**, not only against `src/` — `impeccable`'s full rule set needs a rendered page. Report the hit count, and triage every hit in the same block: fixed, or left standing as a finding with one line saying why. A hit left standing is not a failure of this step; an unreported one is. `impeccable` absent → say the check could not run, and do not report the step as passed on silence.
- **The signature survived promotion**, on the pages that carry it.
- **The densest page holds at both widths**, screenshots taken.
- **Pages running on fixtures are listed by name.** This list matches the `QUEUE.md` wire lines one for one — a page on neither list does not exist.

Any of them fails → fix it in the same session.

**The canvas files stay after promotion** — frozen references under `canvas.md`'s lifecycle: each dies only when its page is wired with real data, survives both widths, and the user confirms the side-by-side at a chat stop — never through an AskUserQuestion, which would cover the comparison being read. `build-flow` carries that per page through the queue. Never delete unasked.

## Step 9 — Close

**Nothing stays a draft.** Every canvas page ends promoted into a real route; a page left in the repo unrouted is dead code that reads as finished work.

The close reports the detector's final count beside Step 8's, and names every hit left standing with the one line that justified it. A design flow that ends without that number has verified its own work by assertion.

One block: the visual decisions that settled · files changed · each page's fate — promoted and wired, or promoted on fixtures with its `QUEUE.md` wire line · the canvas files still standing and the queue line that will retire each · the `/styleguide` route named as staying dev-only, deletable at the user's word · what is still `[needs verification]`.

State that this gate **no longer applies** to later pages — from here on what binds is Section 5 and the component rules in `ui-build`.

Close by reminding the user that the commit waits for their word.
