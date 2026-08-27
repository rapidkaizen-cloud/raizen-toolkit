---
name: ui-build
description: Rules for building or changing any UI — component reuse, icon sourcing, design tokens, loading and error states, supporting text, accessibility, and the gate that blocks UI work while the design system is still undecided. Use before creating a new component, editing an existing one, or touching styling values.
---

# ui-build — touching the UI

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

## Icons

**One icon family for the whole app** — the pack named in the styling files. No exceptions.

**Never draw an icon.** An icon missing from that pack is a **finding**, reported to the user. It is not permission to write an SVG, to pull one from a second pack, or to use an emoji.

The logo or brand mark is the exception: it belongs to no icon pack and is not an icon.

**Sizes come from Section 5, and there are few of them.** The pack ships one default size; every departure from it is an override under `Library defaults` below and needs the same line behind it. A screen carrying four icon sizes holds three decisions nobody recorded. Two sizes usually cover an app: one inline with text, one for block states like empty and failed.

**`weight`, `fill`, and the pack's other style dials follow the pack default** unless Section 5 names otherwise. Mixed weights inside one app read as inconsistency, not as emphasis.

Where icons are allowed to appear is decided per app in PRD Section 5. This rule governs where they come from.

## Tokens

**Raw color, font size, or spacing values inside a component: forbidden.** Everything goes through tokens.

The split between the PRD and the styling files is permanent:

| Source | Contents |
|---|---|
| PRD Section 5 | **Rules and scale** — one icon family, how many accent hues Section 5 records, how many text steps, one radius scale. Plus the roles, values, and usage rules for color and spacing, and the per-component numbers Section 5 carries as its second value-bearing exception |
| Styling files | **Values** — font name, icon pack name, hex, radius number |

Code that breaks a **rule** in Section 5 (a second icon family, an accent hue beyond the number Section 5 records, a sixth step) → **a finding**. The derivation direction is PRD → CSS, never the reverse. Deviating code is not a new norm.

A need that no token covers → **report it as a finding**. Do not write a raw value and do not add a token yourself: adding or changing a token means changing PRD Section 5, and that requires an explicit user decision.

Findings piling up until it feels like the visual direction is wrong rather than the code → point the user to the `design-rework` skill. It audits what is actually in use, changes Section 5 line by line with the user's approval, then updates every component in one pass. Do not do it yourself in pieces.

## Library defaults

**A library default is the decision until PRD Section 5 says otherwise.**

This covers everything the installed libraries already ship an answer for: component props (`size`, `variant`, `color`, `radius`, `placement`, dismiss behaviour, default open state), provider-level options, and theme values.

The test is one question, and it is deliberately not *"is this reasonable"* — that always answers yes:

> **Can the Section 5 line be satisfied without touching this prop?**
> Yes → use the default. No → the override is the only route, and it is allowed.

Name the line in the same breath as the override. An override whose justification cannot name a line has no justification.

Three levels decide, in this order:

1. **The accessibility rules below.** They outrank a default, because a default can be wrong — a library's medium button is often under the platform's target size, and the target still wins.
2. **A line in PRD Section 5.**
3. **The library default**, which beats a session's taste.

Section 5 states rules, not props, so most overrides are argued from a rule rather than quoted from it. The test still bites, because it asks whether another route exists — not whether the argument sounds good. Density already met by the table's own compact prop means every `size="sm"` scattered across buttons has another route, and loses.

An override already in the repo with nothing behind it is a **finding**, the same standing as a raw hex. Two ways out: revert to the default, or take the decision to the user and write it into Section 5 first. Never a third value picked to split the difference.

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

## Supporting text

Text next to a field, a section, or a state says **what follows for the user**, never **why the rule was designed that way**.

"This store will not be scheduled again" belongs on screen. "Reopening it has to be a deliberate decision by someone" is a rationale, and rationales live in the PRD. A sentence answering *why is the rule like this* was written for whoever reads the document, not for whoever is working this screen for the fortieth time today — and on screen it becomes permanent noise, because it is read every time and useful once.

This does not shorten the empty and failed states above. Those explain a situation the user is in, which is consequence, not rationale.

**A rationale found on screen is a finding, reported to the user** — the same standing as a raw color value, and removed the same way. Without that sentence this rule states a preference nobody is obliged to act on, and the text accumulates one paragraph at a time until a screen is mostly explanation.

How much supporting text a screen may carry, and how long a repeated label may be, are recorded per app in PRD Section 5 — ratified from the canvas's copy decisions in the design interview. This rule governs what may be said, not how much.

## Wording

Fixed norms. Not asked per app, not restated in the PRD, because none of them varies between internal apps.

**Sentence case for every heading, label, and button.** Title Case On Every Header reads as marketing copy and makes ordinary two-word labels look like proper nouns.

**Active voice, naming who did what.** "We could not save your changes", not "the changes were not saved".

**No exclamation marks, and no "Oops".** A failure message states the cause and the next action. Volume is not information.

**No placeholder content in shipped screens** — no lorem ipsum, no `Acme Corp`, no `John Doe`, no invented round figures. A number on screen comes from data, or is clearly marked as an example.

These bind the same way the loading, empty, and failed states above do: written together with the component, not as follow-up work.

## Accessibility

For new code: 4.5:1 contrast for text and 3:1 for non-text, visible focus, keyboard reachability, and every control's role and name reaching the platform's accessibility tree — semantic HTML and ARIA where needed is the web's answer.

Color is never the only status marker.

Spacing and alignment are written direction-neutral — the inline-start / inline-end form rather than left / right, which is what every platform's own layout system already uses. Costs nothing at the moment of writing and cannot be retrofitted cheaply, because it is every edge in the app at once rather than a component.

**Minimum target size follows the surface, read from PRD Section 1.** A web page reaches a touchscreen whatever its users are said to work on, so the web keeps its floor whatever the input: the Section 5 phone profile's touch target, 44×44px where Section 5 is silent, and never below WCAG 2.2's 24×24 CSS px. A mobile app follows its own platform — 44pt on iOS, 48dp on Android, which is above the web figure rather than equal to it. A **desktop application binary**, which only ever runs in the window it ships as, takes its size from the Section 5 density profile instead. Everywhere except that desktop binary, an action revealed only on hover does not exist — provide another route to it; on the desktop binary a hover-revealed row action is the platform's own convention rather than a defect.

Why conditional: written as one number this rule outranks Section 5 by the order above, so it silently overrules a ratified density profile on a surface with no touch screen to protect — while being under Android's minimum on the surface that does have one.

Motion honors `prefers-reduced-motion`.
