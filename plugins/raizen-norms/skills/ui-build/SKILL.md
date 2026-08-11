---
name: ui-build
description: Rules for building or changing any UI — component reuse, icon sourcing, design tokens, loading and error states, supporting text, accessibility, and the gate that blocks UI work while the design system is still undecided. Use before creating a new component, editing an existing one, or touching styling values.
---

# ui-build — touching the UI

## Gate — the visual direction must already be set

**Before writing any UI component, read PRD Section 5.**

Section 5 still `[needs verification]`, empty, or absent → **STOP.** Do not write a component, do not write a styling value, do not add a token. Point the user to the `design-init` skill, which interviews the visual direction and then proves it on one real page.

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

Components that came from a copy-in library (shadcn and the like) are **existing code** as far as this rule is concerned, not a dependency to be ignored.

## Icons

**One icon family for the whole app** — the pack named in the styling files. No exceptions.

**Never draw an icon.** An icon missing from that pack is a **finding**, reported to the user. It is not permission to write an SVG, to pull one from a second pack, or to use an emoji.

The logo or brand mark is the exception: it belongs to no icon pack and is not an icon.

Where icons are allowed to appear is decided per app in PRD Section 5. This rule governs where they come from.

## Tokens

**Raw color, font size, or spacing values inside a component: forbidden.** Everything goes through tokens.

The split between the PRD and the styling files is permanent:

| Source | Contents |
|---|---|
| PRD Section 5 | **Rules and scale** — one icon family, at most one accent, how many text steps, one radius scale. Plus the roles, values, and usage rules for color and spacing |
| Styling files | **Values** — font name, icon pack name, hex, radius number |

Code that breaks a **rule** in Section 5 (a second icon family, a second accent, a sixth step) → **a finding**. The derivation direction is PRD → CSS, never the reverse. Deviating code is not a new norm.

A need that no token covers → **report it as a finding**. Do not write a raw value and do not add a token yourself: adding or changing a token means changing PRD Section 5, and that requires an explicit user decision.

Findings piling up until it feels like the visual direction is wrong rather than the code → point the user to the `design-redesign` skill. It audits what is actually in use, changes Section 5 line by line with the user's approval, then updates every component in one pass. Do not do it yourself in pieces.

## Loading, empty, and failed

Fixed norms. Not asked per app, not restated in the PRD.

**Loading → a skeleton shaped like the final result.** Not a spinner. A skeleton matching the shape of the content to come keeps the layout from jumping when data arrives, and tells the user what is being waited on.

Spinners are only for things with no shape: a button mid-submit, and work running in the background.

**Empty → explain why it is empty and what comes next.** "No data yet" is not enough. Empty because of a filter is a different thing from empty because nothing has ever existed, and the two need different sentences.

**Failed → put the message next to its cause.** Form errors appear under their field, not stacked at the top of the page. Errors with no field of their own (failed to load, failed to save) appear where the content should have been, together with a way to retry.

A failure message never disappears on its own. Only success notifications may.

Each of these states is written **together with its component**, not as follow-up work. A component that only has a success state is not finished.

## Supporting text

Text next to a field, a section, or a state says **what follows for the user**, never **why the rule was designed that way**.

"This store will not be scheduled again" belongs on screen. "Reopening it has to be a deliberate decision by someone" is a rationale, and rationales live in the PRD. A sentence answering *why is the rule like this* was written for whoever reads the document, not for whoever is working this screen for the fortieth time today — and on screen it becomes permanent noise, because it is read every time and useful once.

This does not shorten the empty and failed states above. Those explain a situation the user is in, which is consequence, not rationale.

## Accessibility

For new code: 4.5:1 contrast for text and 3:1 for non-text, visible focus, semantic HTML, ARIA where needed.

Color is never the only status marker.

Minimum touch target 44×44px. An action that only appears on hover does not exist on a touch screen — provide another route to it.

Motion honors `prefers-reduced-motion`.
