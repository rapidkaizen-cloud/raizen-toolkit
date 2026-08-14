# The design canvas — taste decided on a free page, not by questions

One temporary TSX route — **every page of the app, redesigned** — where the visual direction and every shell are designed whole, judged in the real browser, then ratified value by value into Section 5. It replaces the **taste** questions of the interview; it never replaces the structural ones.

## When this path runs

- `design-init`, in **Full mode** (the interview runs first, the canvas renders its answers — the default recommendation) and in **Fast mode** (the canvas improvises the values too).
- `design-rework` overhaul, same two routes — full or fast, the user's pick at Step 2.

**Escalation when the canvas misses twice:** on Fast, the full interview opens; on Full, decisions 1–5 are re-asked. The structured questions dig out what the free hand could not.

## The brief — features in, interpretation free

The input to the canvas is the **user's feature list**, plus what the PRD already holds. The user names what the app does; the canvas decides how that looks — composition, richness, hierarchy are the designer's to interpret, and the user judges the result rather than pre-approving a layout.

Two bounds on that freedom, both the user's own condition:

- **Function is faithful.** A feature on the canvas shows what the feature actually does — its real fields, its real states, the figures a business rule demands. Inventing a feature nobody named stays forbidden, exactly as the reference-page rules state.
- **It renders working.** Real fixtures, not lorem; states, not placeholders. The canvas itself is static by design — real behavior arrives when pages are built through `build-flow`, whose Bound list is where *matches the function* is enforced page by page.

**A thin brief is expanded on the canvas itself, never silently and never by a checklist first.** The user naming two features is an opening, not the ceiling. Draw what the brief plausibly implies alongside what it names — candidates from PRD Sections 2–3 and the same product-type database `build-flow` Section 4 draws from — and **mark every improvised feature visibly as a proposal** on the canvas (a small tag on its section). The cut is then **asked, not narrated**: in the same AskUserQuestion call as the judgement verdict, the marked features form a multi-select — every feature an option with a one-line description, keeping all as the recommendation; four options is the tool's cap per question, so more features means more questions in the same call. What is unchecked is removed. Same bias `build-flow` applies per page — propose the full thing, let the user trim — but here the proposal arrives rendered, because a feature is easier to judge on screen than as a line in a list.

A kept proposal the PRD does not yet hold is reported as a PRD line for the user's decision, per `prd-format`: the canvas may show it, only the PRD makes it real.

**In `design-rework` the existing pages are the floor of the brief, never its ceiling.** The brief is still collected from the user; what the app already does joins it as given. Improvised features and reshaped shells are still expected and still tagged — a canvas that redraws today's pages in new tokens is a repaint, and it has failed exactly as the safe-default canvas fails. *Function-faithful* binds what a shown feature does; it never binds a layout to what the layout used to be.

A reference the user points at — a file, a screenshot, an app — is welcome as inspiration for the interpretation. It is **looked at, never parsed or imported**: its values are re-created by the designer where they fit, not transplanted as machinery.

## Asked before drawing

**Fast:** three questions only — Q12 component library · Q13 icon pack (only when the library bundles none) · Q17 lowest supported width. **Full:** the whole interview in `interview.md`, and its answers bind the canvas's values. In `design-rework` every asked entry defaults to *keep*, and an installed library is re-asked only when the audit indicts it.

Install per the skill's own install step **before** the canvas is written. The canvas is built from the real packages, so they must exist.

## The canvas file

**One folder, one file per page.** `src/design-canvas/` beside the styleguide route: one TSX file per page, **named exactly as its real page is or will be named**, plus an index route listing them and one CSS file carrying the canvas variables. Reachable dev-only like `/styleguide`, out of navigation and out of the production build. Never one monolithic file, and never files scattered outside the folder — the folder is the quarantine boundary, and its structure mirrors the app's real pages **so that approval is a promotion, not a rebuild**.

**Every page, drawn.** Derive the archetype table before drawing — group the PRD's pages as Q18 describes; in `design-rework`, from the routes that exist — then draw **every page**, each to its archetype's proposed shell with its own real content. Pages sharing an archetype will read similar; that is the app being consistent, not the canvas being lazy. This is the full redesign, visible up front — the whole app before a single real file moves.

**`/styleguide` is generated before the canvas**, to `design-init` Step 6's spec, rendering the current theme — library defaults on a fresh app. It imports production tokens, so when ratification later writes the new values it follows by itself. Nothing on the canvas depends on it, but the component inventory existing first keeps the canvas honest about what the library actually ships.

**Quarantine, both directions.** Nothing in the app imports the canvas, and the canvas imports only three things: the chosen component library, the chosen icon pack, and its own CSS. Never the production theme, tokens, or components — the canvas is pre-ratification, and its values are its own until the user ratifies them. The app must render identically with the canvas deleted.

**Real components, canvas-owned theme.** The library's components render inside a scoped theme wrapper carrying the canvas's own CSS variables. What the user judges is what the app can actually become — no hand-drawn mockups whose fidelity dies in transplant, and no production theme touched while the canvas iterates.

**The taste license, granted explicitly.** Design the page as a designer with a free hand — no database query, no obligation to any earlier conservatism. In **Fast** the license covers everything: palette family and its steps, tinted surfaces, elevation, type scale, spacing, composition. In **Full** the interview's answers are the **baseline, not a cage**: the license still covers everything, but where the canvas departs from an answer, the departure is **drawn, tagged, and asked** — one line per departure in the judgement call, shaped `answered X → drawn Y, because Z`. An unapproved departure reverts to the answered value; an approved one enters ratification like any other canvas value. The answer wins by default — the departure carries the burden of proof. The canvas exists because taste assembled from safe defaults produces a wireframe; a canvas that reaches for the safe default has failed its one job. The entries of `anti-pattern.md` still bind, **with their qualifiers** — a purple-blue gradient *as the default*, a *pure black* shadow — guardrails against clichés, never a taste to follow.

**The canvas opens with its own foundations board** — palette roles and steps with their values, text scale on real sentences, spacing, radius, shadow, status triads — rendered from the canvas's own variables, above the pages that use them. Design system and prototype on one board: the user judges a token and the pages wearing it in the same scroll, and this board is a live preview of what `/styleguide` will hold permanently once the values are ratified.

**The canvas's variables carry the production token names.** The vars are the canvas's own, but named exactly as the theme files will name them — ratification is then a copy, not a translation, and nothing gets renamed on the way into production.

**Coverage.** The whole visual language, shown once across the pages: every color role in use on real surfaces · text steps on real sentences · one dense table with messy fixtures (long labels, large numbers, missing values) · form controls in their states · status markers · one card or KPI group · the behavior at both widths. Realistic domain data from PRD Section 4 — the same standard `build-flow` holds every page to.

## Judging

Screenshot at the Section 5 desktop breakpoint (1440px when none exists yet) and at the Q17 lower bound, with the browser tooling available to the session. The user judges. Two rounds on the same canvas; a third round does not run — the canvas has spent its rounds, and the escalation above opens.

**Escalation decides values, not pixels.** Its answers become the brief's constraints, and the canvas is **regenerated fresh from them** — never patched over the failed one — then judged again under the same two-round rule.

**Every decision in this path goes through the AskUserQuestion tool**, under the rules `interview.md` states — a prose question at the end of a turn is answered by no one. The judgement is one call: a single-select verdict (approve · rework this round · escalate to the questions), the marked-feature multi-select above, the answer-departure lines (Full mode), and one shell question per archetype whose canvas screen departs from what exists today. Four questions per call is the tool's cap — more archetypes means a second call in the same turn. Contrast failures, cancelled value lines, and reopened questions are asked the same way.

## Ratification — approval happens on the canvas, the values follow as a report

**Approving the canvas is the approval.** The values behind it are then read — the canvas's variables and measured values: palette and its steps, type scale, spacing, radius, shadow, density numbers — and reported the way derived decisions are reported: one line each, never silent, cancellable. Cancelling a line reopens that value as a question; the rest proceed. There is no second approval gate over the same pixels the user just judged.

Two cases still stop:

- **Contrast.** Every new pair is checked against the Section 5 target; a failing pair is put to the user, never silently passed and never silently fixed.
- **`design-rework`.** Section 5 there already holds decided values, and it changes only by explicit user decision — so the report is not enough: the values enter Step 4 as the *new* column of the diff, and that line-by-line approval is the one gate. The canvas judgement and the diff never double up; the diff is where the old value is protected.

Ratified values are written into Section 5 and the styling files under `design-init` Step 4's rules, all four. The styleguide already exists and follows the new tokens by itself — verify it against `design-init` Step 6's done-check, then the pass runs.

**No reference page exists — the canvas is the reference, and approval promotes it.** The canvas pages are structured like the real ones, so the pass **moves each file to its real path** — the most data-dense page of the primary role first — removes the canvas theme wrapper (the token names are already production's), and replaces the fixtures with the real data layer as `build-flow` and `logic-init` prescribe. In `design-init` there is usually no backend yet: promotion keeps the contract fixtures in `build-flow`'s shape, and real wiring arrives page by page through the queue; in `design-rework` the existing data layer is wired in the pass itself. What is checked per page, at both widths, is **survival of real data**: a layout that collapses under real rows, a token that did not land, a section that vanished — that is divergence, and the first one stops the pass as a rework round of that page, two at most before Section 5 reopens. Real rows differing from fixtures is not divergence. `/styleguide` embeds no page — the app itself is the composition, one route away. The densest page simply remains the bar `build-flow` judges later pages against.

**The promotion empties the canvas folder, and its remnants are deleted in the same session** — the index route, and the canvas CSS once its values live in the theme files. A canvas file left alive is a second source of values — the exact drift the styleguide exists to prevent.

## What the canvas never decides

Page content (`build-flow` Section 4) · the archetype table — the canvas proposes every shell on screen, but the table becomes real only through the user's answers in the judgement call · loading, empty, and error norms (`ui-build`) · anything the user does not ratify.
