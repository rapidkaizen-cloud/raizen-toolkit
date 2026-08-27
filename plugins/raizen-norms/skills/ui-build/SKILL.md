---
name: ui-build
description: Rules for building or changing any UI — component reuse, loading and error states, the craft material loaded before any component is written, and the gate that blocks UI work while the design system is still undecided. Use before creating a new component, editing an existing one, or touching styling values.
---

# ui-build — touching the UI

## The material — loaded before the first component

**Two skills carry the craft rules this file no longer states, and both are read before any component is written**: `impeccable` (its `reference/craft-floor.md` and, for an operational app, `reference/operate.md`) and `frontend-design`. Icons, tokens and raw values, library defaults, supporting text, wording, and accessibility all live there now.

Both are **Required** installs for a repo under these skills, and the load is not optional for a session that touches UI — a component written before they are read is written out of the defaults they exist to close.

Neither absent stops the work. Say which one is missing and what could not be checked because of it, then carry on: an unenforced rule reported is recoverable, a session that refuses to build is not.

**Material, never an authority.** Where either collides with a ratified PRD Section 5 line, Section 5 wins. Their findings are findings — reported to the user, never fixed in place inside another session's work.

**Read its reference files; never run its commands.** Three of `impeccable`'s commands write documents — `init` and `extract` write `PRODUCT.md`, `document` writes `DESIGN.md` — and `PRD.md` and `QUEUE.md` remain the only documents an app repo maintains. Its menu leads with `init` whenever it finds no `PRODUCT.md`; that offer is answered by pointing at PRD Section 5, not by taking it.

## Gate — the visual direction must already be set

**Before writing any UI component, read PRD Section 5.**

Section 5 still `[needs verification]`, empty, or absent → **STOP.** Do not write a component, do not write a styling value, do not add a token.

**One exemption: the design canvas and the `/styleguide` scaffold.** `src/design-canvas/` and the styleguide route — on a non-web Surface, whatever `canvas.md` defines for that platform — are the instruments that *produce* Section 5 — a design skill building them while Section 5 is still empty is the gate working, not a breach. The exemption is theirs alone: no real page, component, or token is written until Section 5 lands.

**And the canvas folder belongs to the design session that is building it.** A session doing any other work does not edit, move, or delete anything under that canvas folder — a problem found there is a finding reported to the user, never fixed in place. The canvas is a ratified reference; an edit from outside the design flow silently changes what the user approved.

Which skill to point at is decided by **whether this repo already has UI components**, not by the state of Section 5 alone:

| UI components in the repo | Point the user to |
|---|---|
| None | `design-init` — it interviews the visual direction from nothing, then proves it as every page of the app on a staged canvas |
| Some already exist | `design-rework` — it measures what those components actually use and puts each value to the user to ratify or overrule |

Getting that wrong sends the user in a circle: `design-init` refuses a repo that already has components, so naming it there produces a second STOP and no way forward. A repo in that state usually arrived through `app-rework`'s document mode, which writes the PRD for an existing app and deliberately leaves Section 5 unwritten.

Why stop rather than choose for them: every rule below — tokens, components, contrast — measures the code against Section 5. Without Section 5 there is nothing to measure against, and a session that decides for itself is setting the app's norms through the back door.

Section 5 filled → this gate is done. Later pages need no further visual approval; what binds them is the rules below.

## Components — named in the Plan before execution

Before building any UI element, **check the components already in the repo**. A required step, not a suggestion. Name which existing component covers each element in scope.

The order of sources is fixed:

1. **A component already in the repo.**
2. **A component from the installed component library.** The library chosen for this app is where UI elements come from, not a place to take inspiration from. An element the library ships is used, not rebuilt — pagination, dialogs, and date fields are shipped far more often than they are missing.

   **List the library's component directory before deciding it lacks something.** One command against `node_modules/<library>/dist/components` or the equivalent for that package. "It probably doesn't have one" without listing is not a reason to build.

3. **A new component** — allowed when the library ships nothing for the case, or ships something that genuinely does not fit. Two conditions:

   - **Say what fails.** Which component was examined, and what it cannot do here. "Not quite the right look" is not it.
   - **Follow the library's idiom.** Same compound shape (`Root` / `Trigger` / `Item`), same prop names (`isDisabled`, `isActive`, `size`), same source of styling. A hand-written component with its own conventions forces every later reader to hold two systems in their head at once.

Creating a new component → say why the existing one is not enough. **Looking slightly different is NOT a reason** — that is what props are for.

A visual pattern appearing a second time → **extract it into a component, do not copy it.** The second appearance is the trigger to extract, not permission to duplicate.

Where the app has a `/styleguide` route, the extracted component is **added to it in the same turn** — that route is the one place all components are seen side by side, and a shared component missing from it is a finding.

Components that came from a copy-in library (shadcn and the like) are **existing code** as far as this rule is concerned, not a dependency to be ignored.

## Loading, empty, and failed

Fixed norms. Not asked per app, not restated in the PRD.

**Loading → a skeleton shaped like the final result.** Not a spinner. A skeleton matching the shape of the content to come keeps the layout from jumping when data arrives, and tells the user what is being waited on.

Spinners are only for things with no shape: a button mid-submit, and work running in the background.

**Empty → explain why it is empty and what comes next.** "No data yet" is not enough. Empty because of a filter is a different thing from empty because nothing has ever existed, and the two need different sentences.

**Failed → put the message next to its cause.** Form errors appear under their field, not stacked at the top of the page. Errors with no field of their own (failed to load, failed to save) appear where the content should have been, together with a way to retry.

A failure message never disappears on its own. Only success notifications may.

Each of these states is written **together with its component**, not as follow-up work. A component that only has a success state is not finished.

**Where the app has contract files, these three are proven rather than claimed.** `build-flow` builds each page of a UI batch against six named fixture cases, and three of them are exactly these states — `loading`, `empty`, `failed`. Two more decide whether the rules above hold at scale: `bulk`, several hundred rows, and `messy`, null in every nullable field with the longest string that really occurs. Both must render without the layout breaking before the page is accepted.

Those two are the ones usually skipped and the ones that catch the most. A component that has only ever met three tidy rows has not met the data it will live with. The cases and the rules around them are in `references/contract.md` of `build-flow`.

