# Frontend interview — everything non-visual first, then the look

**The order is fixed:** the non-visual dialogs (the stack, four product calls), then the reference search and `ui-ux-pro-max`'s searches where installed, then the direction question, then the install gate (`SKILL.md` Step 4), then 2–4 direction frames the user picks from on screen. **Install nothing while the interview runs** — every dialog only locks an answer. **Ask nothing about the look after the pick** — the picked frame's values are read at ratification. Everything else is Claude's call, reported as a cancellable line (What the designer settles), never silent.

## Where options come from

**Invent every option and every frame for this app**, from the corrected Step 1 reading — the kind of app, the platform, who uses it. No fixed option list exists anywhere. **`ui-ux-pro-max`'s data is the one outside source** (Part 2): its pure proposal is drawn as generated, and anything else taken from it is argued for this app like an invented option and labelled as its.

- **Name each option in plain words, its consequence in parentheses**, written fresh for this app. This file holds no sample phrasing, because a written example gets copied.
- **Replace any option or frame you cannot argue in one line from this app's documents or platform** — a stock option is a failed option.
- **Mark one real option "(Recommended)"**, first, with its reason from this app. `Decide for me` is never the recommendation.
- **Off the web, one frame is the target platform's design language** (Non-web platforms). On a cross-OS shell (Tauri, Electron, Flutter desktop), read the target OS from where the Roles' users sit; pin it at the Step 1 correction where the documents do not settle it.

**Ask every question through AskUserQuestion** — single-select, except the multi-select direction question. **Batch four dialogs per call, fewest calls possible**; a dialog whose options read an earlier answer rides a later call in the same turn:

| Call | Dialogs |
|---|---|
| 1 | component library · supported widths · theme mode · copy voice |
| 2 | styling (where the library brings none) · icon pack (where it bundles none) · engine overview (where a trigger fired) · the two frame screens |

A third call carries the per-engine dialogs, only where the overview kept a category. Reconcile after every call: two answers that collide go back as one question naming both.

## Part 1 — the non-visual dialogs

### The stack — one dialog per decision, installed later

- **Component library** — per `library-rubric.md`: 3–4 options, *own components* always one. Where UI exists, `Keep — <installed library>` is first and recommended unless the audit indicts the library.
- **Styling** — **ask only where the library brings no styling system** (*own components*, headless). On the web **recommend Tailwind CSS**, plain CSS always an alternative. A library with its own styling (theme object, CSS-in-JS, own CSS layer) decides it without a dialog; one built on Tailwind (shadcn, HeroUI and kin) settles it as Tailwind; report either with the library it came from, cancellable. Off the web there is no Tailwind default: styling follows the platform, and a dialog opens only where the platform leaves a real choice. Where UI exists, the installed styling is `Keep` and first.
- **Icon pack** — ask only when the library bundles none; recommend a pack already installed. Where `ui-ux-pro-max` is installed, the pack its icon search names may be one option, verified like the rest, never with its fallback family. **One icon family per app, no exceptions** — a missing icon is a finding, never a hand-drawn SVG or a second family.
- **Engines** — no standing dialog; only on `engine-rubric.md`'s triggers.

**Verify every stack candidate** per the rubrics — one pass for all, never a candidate offered on memory alone.

**The family rule.** The decision records name logic-layer choices with their families (`TanStack Query — TanStack ecosystem`). A candidate from an already-installed family that passes the rubric rises to the recommendation, and the shift is named ("recommended also because Query is already installed"). It moves the recommendation, never removes an option.

### Four product calls — each with Claude's recommendation

Derive each recommendation from the reading and the Roles — who uses the app, when, where, on what — reason in its description. End each dialog with `Decide for me`: the derived value applies, reported as a cancellable line.

- **Supported widths** — phone, tablet, or desktop only, as the lowest width to hold. A field or phone role pulls it to phone; an all-desk cast keeps desktop. Off the web, use the platform's unit, consistent with the Proof profile's Bounds line. The desktop judged width becomes `DESIGN.md`'s desktop breakpoint; name both widths in the canvas assumptions block and take round-1 screenshots at them. **State the lower bound in `DESIGN.md`, so anything below it is *unsupported rather than broken*.**
- **Theme mode** — light, dark, both, or system (a night shift argues for dark). **The answer binds every frame and the canvas**; only after this dialog's `Decide for me` may one frame be drawn in the other mode (`canvas.md`, Directions first), and picking it settles the mode. With two modes, prove the second on the foundations board and `/design-system`, compute every contrast pair in both, and record the modes in `DESIGN.md`.
- **The two screens the frames are drawn on** — offer 2–4 real pairs, `<proving page> + <second screen>`, from the Roles and `docs/rules.md` or, where UI exists, `handover.md`'s routes. The recommended pair leads with the page carrying the most of this app's own subject — chosen for what the user will see, never for how many controls or fields it holds — plus the screen the direction most likely breaks on. The proving page is held through the flow (`canvas.md`, Directions first).
- **Copy voice** — formal, neutral, or casual, and where the language has several forms of address, which (Indonesian: *Anda* or *kamu*). Where a first-visit page group earns a looser voice than the pages behind login, ask per page group. The answer is the copy voice in `DESIGN.md`'s Overview, read by `ui-build`'s Writing section. Where `ui-ux-pro-max` is installed, read its `brand` voice reference, located through that sub-skill's `SKILL.md`, before writing the options; never run that sub-skill.

## Part 2 — the reference search, then the direction question

### The reference search

**Run it once with WebSearch, between the non-visual dialogs and the direction question.** Find **real products** in this app's domain and platform — product sites, app-store pages, docs showing the product's own screens, galleries of shipped screens. **Concept shots (Dribbble, Behance and kin) are not references.** The platform scopes the search: a Windows tool is not answered with web SaaS.

Show **in chat, before the dialog**: 3–6 products, each **name · link · one line on what this app could take from it**, grouped into **2–4 directions**, each named on an axis sayable in a sentence. Print only links the search returned, and **say in one line how many products the search returned** — a set of fewer than three, or one without links, is the unavailable path below and is named as such, never passed off as the search's result. Where UI exists, the search runs in the drawing session, briefed only by `handover.md` — search the app's job, never its current look.

**WebSearch unavailable → say so in one line**, name products from model knowledge without links, mark the set unverified, and still ask the direction question.

### `ui-ux-pro-max` — only where it is installed

**Run its design-system generator once, after the search**, with a query built from the corrected reading — kind of app, domain, who uses it — **and its style, colour, and typography searches with the same query** — its fonts search where a face needs replacing, its motion presets where a frame animates, for their timing only and never their library, its landing search only for a first-visit page group. Read its `SKILL.md` for the commands only, and **never pass `--persist`**. Show the generator's result in chat under the search's list as **one line — style · palette · type pairing — labelled as the generator's, never as a real product**.

**Ask whether to draw it as its own single-select question, in the direction question's call.** Recommend drawing it only where the app has a first-visit page group, because its page patterns are landing patterns; elsewhere recommend not drawing it, with that reason.

**Drawn, the pure proposal is one frame of the 2–4**: its style, palette and type pairing on the two frame screens, its page pattern only on a first-visit page group. **It is drawn exactly as generated, floor failures included**: compute each pair it fails and list them under the frame at the pick; a status colour its palette lacks is derived and tagged. Picked, each failing value is replaced at the refactor as a floor-forced line (What the designer settles). Where the set already holds four frames without it, one question asks which frame gives way.

**Claude's own frames may mix in its search results** — a style, a palette, a pairing — beside ingredients from the reference search or the subject's world. **Adjust each to this app**: move a stock value off its default, fix a pair that fails the floor, replace a face that lacks the app's script. The frame's motivation line names each ingredient's source and its adjustment.

**At least one frame takes nothing from it**, because it returns the same results for the same reading, and a set drawn from it alone converges across apps of one kind.

**After a rejected set, and at the escalation, the pure proposal is neither offered nor drawn again** — the generator returns the same proposal for the same reading. Its searches re-run only with the steered query.

Not installed → no line, no question, no ingredient.

### The direction question

One AskUserQuestion, **multi-select**:

- Where UI exists, **`Keep — today's look`** first, its consequence in its text: ticked, the running app stands among the frames at its real routes, never redrawn. Never the recommendation.
- The **search's directions**, as many as fit — three, or two beside Keep — one "(Recommended)" with its reason.
- **`Decide for me`** last: Claude composes the set.

The question text says, in the user's own words: *tick what appeals — it is inspiration, not a template; I draw 2–4 directions and you pick on screen. If you want one of them followed closely, say so in your own words under Other or in chat — it then gets a frame of its own drawn closely to it, and the finished design is checked against it point by point. A product the list missed, a screenshot, a URL: under Other — for a picture, answer "screenshot" and paste it in chat.* Read a screenshot or reachable page and take its numbers before the first frame (`canvas.md`, Measured, never transplanted).

**A tick is inspiration, never an anchor.** A reference becomes the **stressed reference** only when the user stresses it in their own words — follow it closely, strictly, or as the main reference. Never infer it from a tick, a recommendation, or a product named under Other without that emphasis. A stressed reference gets its own frame drawn closely to it and is measured against at the judgement (`canvas.md`, Judging); an unstressed tick costs nothing there.

### The frames the answers produce — composed by Claude

**Compose 2–4 frames**, the count set by how much the answers leave open and stated in one line. Drawing, judging and promotion are `canvas.md`'s.

- **Every ticked direction is in the set**; a stressed reference has its own frame.
- **`ui-ux-pro-max`'s pure proposal, where the user said draw it**, holds one frame, its source named as the generator, never as a product.
- **The rest are Claude's own**, each from a source of a different kind than the ticks and each other — **a product from the search, or a thing from the subject's world** (an object, a place, a medium its users picture), since a set drawn from software alone inherits the nearest software's look.
- **Off the web, the platform's design language holds one frame** before Claude fills any.
- **Keep, where ticked, is a frame**, never redrawn.
- **Only `Decide for me` ticked** → the whole set is Claude's, across the search's directions and the subject's world, beside the generator's pure frame where the user said draw it.
- **The set is never one frame.**

**Every frame names its source in its motivation line.** The picked frame's source is what `DESIGN.md`'s Overview records as the reference.

**Nothing stands the frames down** — not a stressed reference, not a brand palette (a constraint every frame is drawn under), not Keep.

**A reference sets direction, never reproduction** (`canvas.md`). Refuse imitating a company's distinctive interface however phrased, and never offer an option amounting to it.

**A correction that collides with the pick goes back as one question** (a brand hex under Other failing contrast on the picked frame's ground): name both sides, offer keeping either and a named middle path where one exists, with a recommendation. The resolved answer replaces the original before anything downstream reads it.

## Part 3 — the install gate, then the frames

Draw the frames only after the install gate. A change the user wants rides the pick under Other (*the second one, but with the brand green*), read as that frame with the correction attached.

**`Decide for me` is a real answer and never silent**: name what Claude chose in each frame's motivation line and in the ratification report.

## What the designer settles

Everything beyond the dialogs is Claude's call on the canvas, one line each in the design plan, the assumptions block, or the ratification value report (`canvas.md`). Any line may be cancelled, opening that value as a normal dialog — where UI exists, with `Keep today's value` first; picked, that one value is read from the styling files (`canvas.md`, blindness), and every other old value appears only at the gate (`SKILL.md` Step 6). **A value a floor forced is the exception**: one line naming the floor and the value it replaced, never cancellable.

- **The picked frame's values** — palette and accent, surface, density, typography, motion, shell — read at ratification, never re-asked. **Motion honours `prefers-reduced-motion` whatever was drawn.**
- **Contrast** — WCAG AA floor (4.5:1 text, 3:1 non-text), from `impeccable`'s Verify list; off the web the platform's bar where stricter.
- **Status colours and markers.** **Colour is never the only marker** — an icon, label, or shape rides with it.
- **Text scale, spacing scale, hover steps** — read at ratification.
- **Tables, feedback placement, confirmation guards, form layout, validation timing** — the platform's conventions (a desktop app follows its OS), on the web the chosen direction. Always: an irreversible action gets a confirmation, permanent mass-deletion a stronger one, and **a placeholder never replaces a label**.
- **Copy on controls and labels** — in the answered voice, judged on the canvas in the app's on-screen language (`CLAUDE.md` Locale row); where UI exists, against the audit's measured label and supporting-text counts. An icon-only control carries its verb in `aria-label` and a tooltip; a destructive confirmation and a page's primary action are never icon-only.

## The archetype table

**Group first, fill after the pick**, never page by page. Before the frame screens are asked — at Step 1 where UI exists, from the routes — group every page the Roles and `docs/rules.md` imply into **screen archetypes**, usually 4–7 (auth, dashboard, data table, form, wizard, detail/approval; on a landing page the unit is the section — hero, benefits, pricing, social proof, CTA/footer), and show the grouping once as a report for correction, not a dialog per row. Every route lands in exactly one archetype; a page fitting none goes to the user as its own question, never a silent bespoke layout. Once the frame is picked, fill each row: shell layout in a sentence, components, density, empty wording — the shells settled at the judgement (`canvas.md`). Write the ratified table into `DESIGN.md`'s Page Composition; `build-flow` Section 4 names the archetype in every later page proposal.

## Non-web platforms

Substitute the vocabulary before any option is written: **design language** — one frame in the target OS's own, named as such; **unit** — the platform's own (window minimum size, size classes in dp), not the CSS pixel; **shell** — one frame carries the platform's navigation model, not sidebar-or-top-bar; **search** — applications on that OS, not web products.

---

# What is not asked

Loading, empty state, and error placement, and the structural writing rules (button and link text, capitalization, toggle labels, error phrasing, the tone table), are fixed in `raizen-norms`' `ui-build`; only the voice varies per app. **Copy length is capped by `ui-build`'s copy caps**, on tenth-use pages; first-visit page groups are exempt. `build-flow` prints each page's longest and median.
