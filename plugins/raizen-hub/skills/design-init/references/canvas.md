# The design canvas — taste decided on a free page, not by questions

One temporary TSX page where the visual direction is designed whole, judged in the real browser, then ratified value by value into Section 5. It replaces the **taste** questions of the interview; it never replaces the structural ones.

## When this path runs

- `design-init`, as **Full mode** — the default recommendation — and whenever the user hands over a finished design-system artifact file.
- `design-rework` overhaul, by default.

The 14-question interview is the fallback, never a parallel path: it opens when the canvas misses twice, or when the user asks to decide by questions.

## Asked first — three questions, nothing else

Q12 component library · Q13 icon pack (only when the library bundles none) · Q17 lowest supported width. In `design-rework` all three default to *keep*, and an installed library is re-asked only when the audit indicts it.

Install per the skill's own install step **before** the canvas is written. The canvas is built from the real packages, so they must exist.

## The canvas file

One route — for example `src/pages/design-canvas.tsx` with its own CSS file — reachable dev-only like `/styleguide`, out of navigation and out of the production build.

**Quarantine, both directions.** Nothing in the app imports the canvas, and the canvas imports only three things: the chosen component library, the chosen icon pack, and its own CSS. Never the production theme, tokens, or components — the canvas is pre-ratification, and its values are its own until the user ratifies them. The app must render identically with the canvas deleted.

**Real components, canvas-owned theme.** The library's components render inside a scoped theme wrapper carrying the canvas's own CSS variables. What the user judges is what the app can actually become — no hand-drawn mockups whose fidelity dies in transplant, and no production theme touched while the canvas iterates.

**The taste license, granted explicitly.** Design the page as a designer with a free hand: the palette family and its steps, tinted surfaces, elevation, type scale, spacing, composition — no database query, no interview default, no obligation to any earlier conservatism. The canvas exists because taste assembled from safe defaults produces a wireframe; a canvas that reaches for the safe default has failed its one job.

**Coverage.** The whole visual language, shown once: every color role in use on real surfaces · text steps on real sentences · one dense table with messy fixtures (long labels, large numbers, missing values) · form controls in their states · status markers · one card or KPI group · the behavior at both widths. Realistic domain data from PRD Section 4 — the same standard the reference page holds.

## Judging

Screenshot at the Section 5 desktop breakpoint (1440px when none exists yet) and at the Q17 lower bound, with the browser tooling available to the session. The user judges. Two rounds on the same canvas; a third round does not run — the canvas has spent its rounds, and the interview fallback opens, because at that point the structured questions dig out what the free hand could not.

## Ratification — approval happens on the canvas, the values follow as a report

**Approving the canvas is the approval.** The values behind it are then read — the canvas's variables and measured values: palette and its steps, type scale, spacing, radius, shadow, density numbers — and reported the way derived decisions are reported: one line each, never silent, cancellable. Cancelling a line reopens that value as a question; the rest proceed. There is no second approval gate over the same pixels the user just judged.

Two cases still stop:

- **Contrast.** Every new pair is checked against the Section 5 target; a failing pair is put to the user, never silently passed and never silently fixed.
- **`design-rework`.** Section 5 there already holds decided values, and it changes only by explicit user decision — so the report is not enough: the values enter Step 4 as the *new* column of the diff, and that line-by-line approval is the one gate. The canvas judgement and the diff never double up; the diff is where the old value is protected.

Ratified values are written into Section 5 and the styling files under `design-init` Step 4's rules, all four. From here the normal flow resumes: `/styleguide` rendered from production tokens, then the reference page.

**The canvas is deleted in the same session**, once `/styleguide` renders the ratified tokens. A canvas left alive is a second source of values — the exact drift the styleguide exists to prevent. An external artifact file stays wherever the user keeps it; it was never in the repo.

## The external artifact variant

The user brings a finished design-system file — typically HTML from a canvas session elsewhere. Same path, two differences: generation is skipped, the file is **parsed** for its palette, scales, and values; and fidelity is lower, because its components are hand-drawn rather than the real library's — say so during ratification. The three questions are still asked, and the parsed values feed the same batched ratification.

## What the canvas never decides

Page content (`build-flow` Section 4) · the archetype table — still derived and ratified as Q18 describes; the canvas may illustrate archetypes, but the table is the decision · loading, empty, and error norms (`ui-build`) · anything the user does not ratify.
