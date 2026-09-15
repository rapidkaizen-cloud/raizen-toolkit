---
name: ui-build
description: Rules for building or changing any UI — component reuse, loading and error states, the interface copy every component ships with, the craft material loaded before any component is written, and the gate that blocks UI work while the design system is still undecided. Use before creating a new component, editing an existing one, touching styling values, or writing any user-facing text.
---

# ui-build — touching the UI

## The material — loaded before the first component

**Two skills carry the craft rules this file no longer states, and both are read before any component is written**: `impeccable` (its `reference/craft-floor.md`, and `reference/operate.md` for an operational app) and `frontend-design`. **Where PRD Section 1's Surface is iOS or Android, `reference/ios.md` or `reference/android.md` is read with them** — both on an adaptive surface — because the platform's navigation, type scale, insets, and touch-target floor live only there. Icons, tokens and raw values, library defaults, and accessibility all live there now.

Both are **Required** installs for a repo under these skills, and the load is not optional for a session that touches UI — a component written before they are read is written out of the defaults they exist to close.

Neither absent stops the work. Say which one is missing and what could not be checked because of it, then carry on: an unenforced rule reported is recoverable, a session that refuses to build is not.

**Material, never an authority.** Where either collides with a ratified PRD Section 5 line, Section 5 wins. Their findings are findings — reported to the user, never fixed in place inside another session's work.

**Read its reference files; never run its commands.** Three of `impeccable`'s commands write documents — `init` and `extract` write `PRODUCT.md`, `document` writes `DESIGN.md` — and `PRD.md` and `QUEUE.md` remain the only documents an app repo maintains. Its menu leads with `init` whenever it finds no `PRODUCT.md`; that offer is answered by pointing at PRD Section 5, not by taking it.

## Gate — the visual direction must already be set

**Before writing any UI component, read PRD Section 5.**

Section 5 still `[needs verification]`, empty, or absent → **STOP.** Do not write a component, do not write a styling value, do not add a token.

**One exemption: the design canvas and the `/styleguide` scaffold.** `src/design-canvas/` and the styleguide route — on a non-web Surface, whatever `canvas.md` defines for that platform — are the instruments that *produce* Section 5 — a design skill building them while Section 5 is still empty is the gate working, not a breach. The exemption is theirs alone: no real page, component, or token is written until Section 5 lands.

**And the canvas folder belongs to the design session that is building it.** A session doing any other work does not edit, move, or delete anything under that canvas folder — a problem found there is a finding reported to the user, never fixed in place. The canvas is a ratified reference; an edit from outside the design flow silently changes what the user approved.

**Point the user at `design-settle`**, whatever state the repo is in. It is one skill with one entry point, and its own audit decides the path: no UI at all → it interviews the direction from nothing, then proves it as every page of the app on a staged canvas; components already there → it measures what those components actually use and puts each value to the user to ratify or overrule. Do not name a path, and do not decide one here — a session that announces which path it will take has pre-empted an audit it has not run.

A repo with components but no Section 5 usually arrived through `app-settle`'s document mode, which writes the PRD for an existing app and deliberately leaves Section 5 unwritten. That is `design-settle`'s normal input, not an error: its audit measures the values and puts each one to the user.

Why stop rather than choose for them: every rule below — tokens, components, contrast — measures the code against Section 5. Without Section 5 there is nothing to measure against, and a session that decides for itself is setting the app's norms through the back door.

Section 5 filled → this gate is done. Later pages need no further visual approval; what binds them is the rules below.

## Components — named in the Plan before execution

Before building any UI element, **check the components already in the repo**. A required step, not a suggestion. Name which existing component covers each element in scope.

**Read the ratified set first, do not search for it.** List the components folder, then read the file holding the app's shared set — one listing, one read, never a grep. A repo whose Section 5 was ratified rather than redrawn has never promoted a canvas, so there may be no single file yet; the listing is still the first move, and the placement rule below is what the first extraction follows. A session hunting for `Pagination` does not find a `Pager`, and writes it a second time under a second name; a year of that leaves three components doing one job and no way to tell which one a page should have used.

The order of sources is fixed:

1. **A component already in the repo.**
2. **A component from the installed component library.** The library chosen for this app is where UI elements come from, not a place to take inspiration from. An element the library ships is used, not rebuilt — pagination, dialogs, and date fields are shipped far more often than they are missing.

   **List the library's component directory before deciding it lacks something.** One command against `node_modules/<library>/dist/components` or the equivalent for that package. "It probably doesn't have one" without listing is not a reason to build.

3. **A new component** — allowed when the library ships nothing for the case, or ships something that genuinely does not fit. Three conditions:

   - **Say what fails.** Which component was examined, and what it cannot do here. "Not quite the right look" is not it.
   - **Follow the library's idiom.** Same compound shape (`Root` / `Trigger` / `Item`), same prop names (`isDisabled`, `isActive`, `size`), same source of styling. A hand-written component with its own conventions forces every later reader to hold two systems in their head at once. **No library → the first shared component sets the idiom, and every later one follows it** — compound shape, prop names, and styling source are decided once, at the first extraction, and read from that file afterwards.
   - **Say which rule it holds.** A shared component exists for one of two reasons, and its header names which: it freezes a PRD Section 5 line so no call site can break it — a status marker deriving its icon from its tone cannot pair a warning colour with a success icon — or it is the second appearance of a pattern. Neither → it is page code, not a shared component. Leave it in the page.

Creating a new component → say why the existing one is not enough. **Looking slightly different is NOT a reason** — that is what props are for.

A visual pattern appearing a second time → **extract it into a component, do not copy it.** The second appearance is the trigger to extract, not permission to duplicate.

**Where it lands is fixed too.** The components holding Section 5 rules live in **one file**, so a later session reads the whole set in a single pass — that file is what the ratified-set rule above points at. A component carrying a flow of its own — a wizard, the app shell — gets its own file. Split the shared file by group, never one file per component, and only once it has stopped being readable in one pass.

Where the app has a `/styleguide` route, the extracted component is **added to it in the same turn** — that route is the one place all components are seen side by side, and a shared component missing from it is a finding.

Components that came from a copy-in library (shadcn and the like) are **existing code** as far as this rule is concerned, not a dependency to be ignored.

## Loading, empty, and failed

Fixed norms. Not asked per app, not restated in the PRD.

**Loading → a skeleton shaped like the final result.** Not a spinner. A skeleton matching the shape of the content to come keeps the layout from jumping when data arrives, and tells the user what is being waited on.

Spinners are only for things with no shape: a button mid-submit, and work running in the background.

**Empty → explain why it is empty and what comes next.** "No data yet" is not enough. Empty because of a filter is a different thing from empty because nothing has ever existed, and the two need different sentences, and each ends on one action that fills it. A filtered empty state names the query and offers the exit — `No results for "quarterly". Clear filters`. Never park persistent information in an empty state: it disappears the moment content exists. **The fix is deleting it, not relocating it.** Moved to the page header it becomes permanent, and an unasked-for paragraph costs more there than in a state that at least went away. Information worth keeping is an element on the page; a mechanism the user does not act on belongs in `PRD.md`.

**Failed → put the message next to its cause.** Form errors appear under their field, not stacked at the top of the page. Errors with no field of their own (failed to load, failed to save) appear where the content should have been, together with a way to retry.

A failure message never disappears on its own. Only success notifications may.

Each of these states is written **together with its component**, not as follow-up work. A component that only has a success state is not finished.

**Where the app has contract files, these three are proven rather than claimed.** `build-flow` builds each page of a UI batch against six named fixture cases, and three of them are exactly these states — `loading`, `empty`, `failed`. Two more decide whether the rules above hold at scale: `bulk`, several hundred rows, and `messy`, null in every nullable field with the longest string that really occurs. Both must render without the layout breaking before the page is accepted.

Those two are the ones usually skipped and the ones that catch the most. A component that has only ever met three tidy rows has not met the data it will live with. The cases and the rules around them are in `references/contract.md` of `build-flow`.


## Writing

Fixed norms for the tenth-use register — the pages somebody comes back to — not asked per app and not restated in the PRD, because none of them varies between such apps. Copy is written **together with its component**, the same way the three states above are.

**A first-visit page group speaks in its own voice.** A landing page, a marketing site, the public front of a product — the register `app-settle` derives from PRD Section 2 — takes the copy voice Section 5's Visual Direction states for that group: the tone table below yields to it there, and humour, an exclamation, a posture in the copy are the direction's to spend, per page group and never behind the login. Section 5 states no voice for the group → the rules below apply as written. What holds on every register are the structural rules — a verb-first button, a confirmation that repeats its consequence, link text naming its destination, a placeholder that is not a label, an error beside its field written as an instruction, no sentence assembled from fragments, one term per concept — because they are accessibility and localization, not tone.

Clear and brief beats clever; consistent beats varied. The best error message is the interaction redesigned so the error cannot happen.

**Read the copy already on screen before writing more.** The product has one voice and its existing copy establishes it; a local edit does not get to invent a new one. One term per concept — `Archive` in the menu is not `Move to storage` in the toast.

**Voice is fixed, tone moves with the stakes:**

| Context | Tone |
|---|---|
| Success, onboarding, empty states | Warm, may be light |
| Routine actions, settings | Neutral, minimal |
| Errors, destructive confirmations | Calm, plain, zero playfulness |
| Data loss, security | Serious, explicit |

**Address the reader directly.** Instructional copy says "you", never "the user". In an error, drop the actor rather than reaching for "we" — `Unable to load content`, not `We're having trouble loading this content`, which reads as deflection. Possessives sparingly: `Favorites` beats `Your favorites`. Hold one perspective for a whole flow.

**Plain words, and no word that does no work.** No idioms, no colloquialisms, no humour that does not survive translation. Skip unnecessary gender. Match the input device: `tap` on touch, `click` with a pointer, `select` where both are possible.

**Never assemble a sentence from fragments around a variable.** `"You have " + n + " new messages"` breaks the moment word order changes. Use a full templated string with proper pluralization.

**A button label starts with a verb naming the action** — `Send`, `Save draft`, `Delete project`. Never `OK`, `Let's go`, or a bare `Yes` / `No` on a consequential action. **A confirmation button repeats the consequence**, so the dialog is answerable without reading the body: `Delete this project?` offers `Delete project` and `Cancel`.

**One vocabulary for a whole flow.** `Get started` to enter, `Continue` or `Next` — pick one — to advance, `Done` to finish. Alternating synonyms makes the user wonder whether the buttons do different things.

**Link text names its destination.** Screen-reader users navigate by a list of the page's links, so it has to make sense out of context: `Read the billing docs`, never `Click here`. A bare `Learn more` breaks as soon as two appear on one page — suffix each one: `Learn more about exports`.

**Sentence case, one policy per element type.** Sentence case is the default: calmer, no per-word rules to remember, and it localizes cleanly. `Save Changes` beside `Discard changes` reads as sloppiness.

**A toggle is labelled for its ON state.** `Send read receipts` lets the user infer the off state; the negative turns the toggle into a double negative. Link straight to a referenced setting rather than describing the path to it.

**An error is an instruction, and it belongs beside the field that failed.** No blame, no `Oops`, no exclamation marks. Phrase the hint positively, and show it before the mistake rather than after:

| Refused | Written |
|---|---|
| `That password is too short` | `Choose a password with at least 8 characters` |
| `Invalid name` | `Use only letters for your name` |
| `Oops! Something went wrong.` | `Unable to save. Check your connection and try again.` |

The same error firing over and over is a finding about the interaction, not a rewording job.

**A placeholder is an example, not a label.** It shows the expected format — `name@example.com`, `DD/MM/YYYY` — and vanishes on input, so every field keeps a visible label of its own.

**A state already visible is not written out again.** A selected card carrying the selection in its border, a check mark, an `ACTIVE` badge, and a heading repeating that item's name has drawn one fact four times — and each copy makes the reader trust the others less, because a screen that says a thing four ways is a screen where saying it once was not believed. Keep the strongest signal and delete the rest; where the strongest one is not reachable for everyone, the copy that survives is the accessible one, never the decorative one. The same holds for a subtitle repeating a word already in the title above it, and for a count printed beside a list whose length is on screen. **The test is subtraction:** remove the label and ask what became unanswerable. Nothing did → it was never carrying the answer.

These bind new code. Copy already in the repo that breaks one of them is a **finding** reported to the user, the same standing as a raw hex value — never rewritten in place inside another session's work. **Source is enough to check every rule here**; none of them needs a rendered page.

Adapted from the `better-writing` skill of [jakubkrehel/skills](https://github.com/jakubkrehel/skills) (MIT).
