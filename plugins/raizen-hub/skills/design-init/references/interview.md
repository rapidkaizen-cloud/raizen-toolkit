# Frontend interview — one taste batch, then the stack

**The interview is small on purpose.** Eight taste slots answered in one turn, then the stack questions that gate the install. Everything else is the designer's call, made on the canvas and reported as a cancellable line — never a dialog, never silent. A long interview does not produce a designed app; it produces a questionnaire's average. The design happens on the canvas (`canvas.md`); the batch exists to capture the preferences the user already has, not to manufacture opinions they do not.

## Where options come from

**Every option is invented for this app, from the model's own design knowledge.** Read the corrected Step 1 reading — the kind of app, the platform, who uses it — and write options the way a designer pitches directions for exactly this product. No fixed option list exists anywhere, and **no research pass runs for taste**: the knowledge that names a good direction for a logistics dashboard or a Windows inventory tool is already in the model, and a search adds latency, not taste. The one place research survives is the stack questions below, because an install mis-remembered costs far more than a correction round.

Rules per option:

- **Named in plain words, consequence in parentheses.** The user is a junior developer — the parenthetical is what the choice buys or costs, written fresh for this app. No sample phrasing is written in this file, on purpose: a written example gets copied, and a copied option is a stock option.
- **A well-known product is welcome shorthand** when it genuinely fits this app — never name-dropped for its own sake.
- **Off the web, the target platform's design language is always one of the options**, named as such. On a cross-OS shell (Tauri, Electron, Flutter desktop) the target OS is read from where PRD Section 2's users actually sit, pinned at the Step 1 correction where the PRD does not settle it.
- **A stock option that would fit any app is a failed option.** Every option must be arguable from this PRD or this platform — if the argument cannot be written in one line, replace the option.
- **One option is marked "(Recommended)"** — a real direction with a reason from this app, never "Decide for me".

## The taste batch — one turn, two calls

Eight slots, **two AskUserQuestion calls in the same turn** (the tool caps four questions per call). Single-select per slot. The lead question's text invites everything the options cannot hold: *anything you want that isn't listed — a screen you liked, a hard requirement — type it under Other.* An Other answer may carry an option and its detail together ("Option 1, but with the brand green") — read it as that option with the detail attached.

**Reference is asked first, and the second call is written after the first is answered.** The two calls are sequential tool calls in one turn, so the reference answer is in hand before the second call's options exist — and it is the one answer that should reshape them. A reference named in call one and ignored by call two's options was not an anchor, it was a formality.

**Every slot carries "Decide for me".** Choosing it hands that slot to the canvas's taste license (`canvas.md`): the designer draws their own call, and the user settles it at the judgement — on screen, where a junior developer's judgement is sharpest. "Decide for me" is a real answer, not a failure to answer, and it is never silent: what the designer chose surfaces in the ratification report like every other canvas value. One slot resolves early: **typography** — the install block needs the font's name before the canvas is drawn, so a typography answered "Decide for me" is decided by the designer when the install block is assembled; the block's font line is where the user first sees that call, and refusing the block reopens it as a dialog.

**In `design-rework` overhaul, every slot carries `Keep — <today's value>` first** — from Section 5's current values, or the audit's measured values where Section 5 is empty (the ratify-path overhaul) — an option, never the recommendation: the user chose overhaul, and recommending every current value back re-litigates that choice.

Call one:

| Slot | What it decides | Notes |
|---|---|---|
| **Reference** | The app or site this one should feel like — the anchor everything else is measured against | Its own rules below. Asked first, because a named anchor reshapes every option that follows |
| **Direction** | The overall look — including dark, light, or both | 2–3 invented directions, plus the platform language off-web. Dark mode is part of a direction, not its own question: an option designed dark says so, and its consequence names the cost (every color token carries two values that both must pass contrast) |
| **Palette & accent** | The neutrals and accent, as one designed unit | One fixed option: follow an existing brand color, hex typed via Other |
| **Surface** | Radius and elevation together — the card style | Each option names what it does to depth, read from the direction candidates |

Call two — its options written after call one is answered:

| Slot | What it decides | Notes |
|---|---|---|
| **Density** | How much fits on screen | Phrased in this app's own terms — what the density means on its actual screens, never as abstract levels |
| **Typography** | The text family or pairing | Options name real faces or pairings, invented for this app. A named reference puts the pairing that reads like it among them, named as such |
| **Motion** | How much the interface moves | Options invented for this app — how much motion its work tolerates. Whatever is chosen honors `prefers-reduced-motion` — that part is a rule, not an option |
| **Shell** | The page frame — the navigation model, invented from how this app is used; off-web, the platform's own model is one of the options | The supported widths ride as derived values below, not as questions |

### The reference slot

**The options are real products, proposed by name.** Two or three the model actually knows, each one arguable for *this* app and this platform — never a famous name dropped for its own sake, which `interview.md`'s option rules already forbid. Each option's consequence says what picking it buys in one clause (`the density and the keyboard-first feel of a tracker built for daily use`), not what the product is. One is marked "(Recommended)". No research pass runs here: naming products a working designer would name is model knowledge, and a search adds latency rather than taste.

Four options is the cap, so the slot carries: up to two named products · **`No reference — explore freely`** · **`Decide for me`**. In `design-rework` a reference already recorded in Section 5 takes the first place as `Keep — <it>`, and the named products trim to fit. The user's own answer arrives through Other — a product the options missed, a screenshot, a file, a URL — and that is the best outcome, not a deviation.

**The two non-product answers are different answers, not synonyms.** `No reference` says draw without an anchor; the difference list below never runs. `Decide for me` hands the choice of *whether to work to an anchor* to the designer, who names the anchor they chose — or says they chose none — as a line in the design plan, cancellable like every derived decision.

**What a named reference actually costs and buys** is stated in the question text, because it is the only slot whose answer changes what happens later: the canvas is put beside it and every difference is written out one by one, each settled as a departure with its reason or as a correction round (`canvas.md`, Judging). It also stands the direction frames down — an anchor is a direction, so drawing candidates for one re-opens a question the answer already closed.

**A reference sets direction, never reproduction.** It is measured where reachable and never transplanted (`canvas.md`); imitating a company's distinctive interface is refused however the request is phrased, and an option that would amount to that is not offered.

**Four options is the tool's cap per slot.** Where a slot also carries a platform-language or Keep entry, the invented list trims to fit — the cap trims invented options, never the Keep, platform, or "Decide for me" entries.

**Answers that collide go back as one question.** A dense-and-technical direction beside a spacious density, a brand hex that fails contrast on the chosen direction's ground — name both answers and what collides, offer keeping either side and a named middle path where one exists, with a recommendation. The resolved answer replaces the original before anything downstream reads it.

## The stack questions — asked, because they install code

Taste can be improvised and corrected; an install cannot. These survive as real dialogs, in a second batch after the taste batch:

- **Component library** — candidates scored and assembled under `library-rubric.md`; each option names the icon pack it bundles, or names itself headless.
- **Icon pack** — asked only when the chosen library bundles none; recommendation is the pack already installed alongside the chosen library when there is one. **One icon family per app, no exceptions** — an icon missing from the family is a finding, never a hand-drawn SVG or a second family.
- **Engines** — charts, heavy tables, date pickers, drag-and-drop and the rest: no standing question. Dialogs fire only on `engine-rubric.md`'s triggers, and an app that trips none hears none.

**The verification duty for stack candidates stays** — maintained, adopted, what it bundles versus what it leaves out, per `library-rubric.md` and `engine-rubric.md`. One verification pass covers all candidates together; never one search per option, and never a candidate offered on memory alone.

**The family rule.** PRD Section 1 records the logic-layer choices with their families (`TanStack Query — TanStack ecosystem`). Whenever a candidate list includes a member of an already-installed family, that member rises to the recommendation, provided it passes the rubric's own checks — and the shift is named when recommending ("recommended also because Query is already installed"). A shift moves the recommendation, never removes an option.

## What the designer settles — reported, cancellable, never silent

Everything a long-form interview would have asked is the designer's call on the canvas, surfaced through the two reports that already exist: the assumptions block before drawing and the ratification value report after approval (`canvas.md`). One line each, and the user may cancel any line — cancelling opens that value as a normal dialog with real options. What this list saves in questions it must not lose in visibility.

What it covers, with the floors that are rules rather than preferences:

- **Contrast** — WCAG AA (4.5:1 text, 3:1 non-text) is the floor `ui-build` already gates on; off-web the platform's own accessibility bar applies where it is stricter.
- **Status colors and markers** — how many statuses, their hues and tints. **Color is never the only marker**: an icon, label, or shape rides with it, readable by someone who cannot tell red from green.
- **Text scale, spacing scale, hover steps** — the designer's own, read off the canvas at ratification.
- **Supported and judged widths** — the lowest supported width derives from PRD Section 2's roles: a field or phone role pulls it down to phone width, an all-desk cast keeps it at desktop; the desktop judged width becomes the Section 5 desktop breakpoint. Off the web, both are read from and kept consistent with the Proof profile's Bounds line. Both widths are named in the canvas assumptions block — the round-1 screenshots are taken at them — and the lower bound is stated explicitly in Section 5, so anything below it is *unsupported rather than broken*; without that sentence, every "looks wrong on my phone" report becomes work nobody decided to take on.
- **Tables, feedback placement, confirmation guards, form layout and validation timing** — the designer follows this app's platform conventions and the chosen direction, not a fixed web idiom: a desktop application follows its OS's own idioms; the web follows the chosen references. Two guards stand whatever is drawn: an irreversible action gets a confirmation, and permanent mass-deletion gets a stronger one; **a placeholder never replaces a label**.
- **Copy on controls and labels** — wording, label length, and supporting text are the designer's, judged on the canvas in the app's on-screen language (the Locale row of `CLAUDE.md`); in `design-rework` the audit's measured label and supporting-text counts are the evidence they are judged against. What stays fixed is accessibility, not taste: an icon-only control carries its verb in `aria-label` and a tooltip, and a destructive confirmation and a page's primary action are never icon-only.

## The archetype table

Derived once the shell slot is answered, never asked page by page. Group every page of PRD Sections 2 and 3 into **screen archetypes** — usually 4–7 (auth, dashboard, data table, form, wizard, detail/approval recur). Per archetype one row: shell layout in one sentence, the components it is built from, its density, its empty/loading wording, and the routes it owns. Every route lands in exactly one archetype; a page fitting none is put to the user as its own question, never silently given a bespoke layout. The table is shown once for correction — as a report, not a dialog per row. The ratified table is written into Section 5 under Page Composition, and `build-flow` Section 4 opens every later page proposal by naming its archetype.

## Non-web platforms

The slots are product-shaped, so off the web the vocabulary substitutes before any option is written: the **design language** — the target OS's own enters the direction, surface, and typography slots as a fixed option; the **unit** — the platform's own rather than the CSS pixel, so widths read as window minimum size or size classes in dp; the **shell** — the platform's navigation model rather than sidebar-or-top-bar. The canvas's native side-by-side proof (`canvas.md`) is what holds the result to the platform — the interview only has to keep the vocabulary from silently defaulting to the web's.

---

# What is not asked

Loading, empty state, and error placement are **not decisions here**. All three are fixed norms in the `ui-build` skill of `raizen-norms`, identical across every internal app.

Wording rules are fixed there too — sentence case, active voice, no exclamation marks, rationale kept off the screen. They do not vary per app, so asking them spends context on an answer that is already known.
