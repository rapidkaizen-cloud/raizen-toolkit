---
name: design-init
description: Decide the visual direction and component library of an app whose PRD Section 5 is still unwritten. By default a batched interview over 15 decisions (options assembled live from the ui-ux-pro-max database, domain reading, and a web-research pass) captures the user's preferences, and a temporary in-repo canvas — real component library, canvas-owned theme, the user's feature brief — renders them as every page of the app, expanding thin briefs into a full product with tagged feature proposals and tagged departures; fast mode draws the canvas straight from three dialogs. Ratifies the canvas, writes the rules and the screen-archetype table into PRD Section 5, writes the concrete values into the styling files, generates the dev-only /styleguide route, then promotes every canvas page into the app's real pages on contract fixtures — real data arrives page by page through the build queue. Use before the first UI component of a repo is written, or when PRD Section 5 is still marked as unverified.
---

# design-init — set the visual direction once, in code

Bootstrap produces a `PRD.md` with an empty Section 5. This skill fills it, then **proves it as the real app** — not a picture, not a description.

Run **once per repo**. After the canvas is ratified and its pages promoted, later pages are bound by Section 5 and the component rules in `ui-build`, with no further gate.

The step skeleton below is `design-rework`'s, on purpose — one flow to learn, two skills. The deltas are marked where they are structural: no audit here (nothing exists to audit), no diff gate (no old values to protect), and no isolated branch (a fresh repo has no parallel work to disturb).

## Hard limits

`PRD.md` Section 5 is the only part of the document written. **Do not** create `MASTER.md`, `DESIGN.md`, `design-system/`, or an interview summary as a file. If another skill in this session produces a document, it is not committed and not referenced.

`ui-ux-pro-max` is run **without `--persist`**. That flag writes `design-system/<slug>/MASTER.md` and calls itself the *Global Source of Truth* — two normative documents for the same thing means Section 5 dies slowly.

This is one of only two paths allowed to write Section 5, and only while Section 5 is still empty. Its contents come from the user's answers, not from the agent's taste and not from another skill's output. A Section 5 that is already filled changes only by the user's decision — see `prd-format` in `raizen-norms`.

**The canvas is the final front-end, staged** (`references/canvas.md`). Its files are the future pages, written production-grade — the user approves code, not pictures, and promotion relocates that code instead of imitating it. The one legitimate difference between a canvas file and its live page is the data flowing through it.

Do not commit and do not push. Staging is fine; the commit waits for the user.

Not decided by the user → `[needs verification]`.

## Step 0 — Preconditions

Check and report one short block:

```
PRD.md      : [present / missing]
Section 5   : [empty / already filled / product without UI]
Kind of app : [from Section 1]
Platform    : [from Section 1 Surface — web, or the platform named there]
Primary role: [from Section 2]
Reading     : [one sentence — see Step 1]
Flow        : mode → interview or dialogs → install → canvas rounds →
              ratify + Section 5 → promotion (all pages) → verify → close
```

`PRD.md` missing → **STOP**, point to `app-init`.

Section 5 already filled → **STOP**, ask whether the user really wants to rework the existing visual direction. That work belongs to `design-rework`.

**Section 5 empty but UI components already exist → STOP as well.** This skill decides a direction before any code carries one. An app that already has components needs its existing values measured and put to the user, not overwritten by an interview that has never seen them. That is `design-rework` on its ratify path — the case a repo arrives in through `app-rework`'s document mode.

Product without UI → **STOP**, this skill does not apply.

## Step 1 — The reading, then route the supporting skills

There is no audit — nothing exists to audit; this step is its sibling. **Reading** is your own conclusion before asking anything, one sentence, shaped as: *"I read this as [kind of app] on [platform] for [who uses it], leaning [the feel that fits], because [reason from the PRD]."*

**The platform slot is not decoration.** `app-init` already asked the platform and PRD Section 1 already holds the answer — it is never asked again. It rides in this sentence because the corrected reading becomes the keywords for every query in Step 3, so one word here is what puts the platform into all of them at once. Left out, the queries return the web's answer to every question and no later decision can tell that anything was lost.

Concluding first beats asking from nothing: the user only corrects what missed, and the correction carries more than an empty question would. A wrong reading is not a failure — it draws out detail that no question would surface.

State the reading, ask for correction, then continue. When the correction is asked through AskUserQuestion, **the full reading sentence goes inside the question field itself** — the dialog may render without the prose around it, so a question that points at text "above" can arrive pointing at nothing. The corrected reading becomes the keywords for every query in Step 3.

**The Step 2 mode question rides in this same AskUserQuestion call** — two questions, one dialog, one turn. Neither reads the other's answer, so nothing is lost by pairing them.

Then read the kind of app from PRD Section 1, and decide once which skills feed the interview:

| Kind of app | Skills used |
|---|---|
| Internal dashboard · single-role internal tool | `ui-ux-pro-max` only |
| Public site | `ui-ux-pro-max` **and** `design-taste-frontend` |

`design-taste-frontend` states itself that it is not for dashboards, data tables, or multi-step product UI. Using it outside that boundary produces motion dials and icon rules that collide with `ui-ux-pro-max`. Its prohibitions are still used for every kind of app through `references/anti-pattern.md` — that is material, not a live authority.

This table routes the **interview's** live authorities only. The canvas phase additionally reads `high-end-visual-design` and `frontend-design` as material for every kind of app — `canvas.md` states the rule and the same limit: material raises the floor of the free hand, and the user's answer wins every collision.

The two skills disagree about icon pack, motion level, or typeface → **the user's answer wins**, which is exactly why all three are asked.

## Step 2 — The mode

Offer two, with a recommendation — asked in the Step 1 call:

| Mode | What is asked | For whom |
|---|---|---|
| **Fast** | Three dialogs — decision 7 · its icon dialog when the library bundles none · decision 10's minimum-width facet — then the canvas is designed whole from the feature brief, **every value the designer's own**. See `references/canvas.md` | An app that must ship today, or a user who wants to judge a finished proposal rather than answer questions |
| **Full** | Every decision's primary axis in `interview.md` — 15 decisions, 16 dialogs (17 when the library bundles no icons), batched into three turns; facets stay derived, reported, and cancellable. The answers are the user's preferences and the canvas's baseline; the canvas departs wherever the designer judges better, every departure tagged and settled by the user at the judgement. See `references/canvas.md` | **Recommended.** The preferences are captured before anything is drawn, and the canvas shows them as an app instead of as a list |

**Consequence:** both still end at real pages running on screen, so no mode decides blind — the difference is only where the correction happens, before or after the first screen.

**Fast and Full both end at the canvas; they differ in where the values start.** In Full the interview captures the user's preferences as the baseline and the canvas renders them, departing wherever the designer judges better — each departure tagged and settled by the user at the judgement; in Fast the canvas improvises the values too. Either way the archetype table is still derived and ratified, Section 5 is still written, the styleguide still renders from production tokens, and the pages still end real. **A canvas that misses twice escalates:** Fast rises to the full interview; Full re-asks decisions 1–3.

**A mode skips questions, never outputs.** The archetype table (decision 10), the `/styleguide` route (Step 6), and real running pages are produced in both modes — what changes per mode is only where their decisions come from.

Derived decisions are **never silent, in either mode.** Every decision not asked is reported on one line with its basis:

```
D8 radius+shadow → 8px, soft cards (from Design System Variables of style "Minimalism & Swiss")
D12 motion       → subtle (from the Effects & Animation column of the same style)
D13 feedback     → inline failures, toast successes (built-in; no basis in the data)
```

A line whose basis is "built-in" is marked as such. The user may cancel any line, and cancelling it opens that dialog normally. `interview.md`'s ledger rules govern the full report: facets between batches, the 15-row ledger at the interview's close, and the same ledger once more at ratification.

## Step 3 — The interview, then translate into values

Read `references/interview.md`, `references/adaptation.md`, and — for decision 7 — `references/library-rubric.md`. Engine dialogs — charts, heavy tables, drag-and-drop, and the rest of what the component pack does not own — have no slot of their own: they fire only on the triggers in `references/engine-rubric.md`, and an app that trips none hears none.

**The order in `interview.md` is the order asked.** No question is promoted to the front because it feels foundational, and none is deferred because its answer looks obvious.

**The options for each question are not written in any file, and the database is not their only source.** `interview.md` names three layers — the `ui-ux-pro-max` query, the model's own domain reading, and a mandatory one-off WebSearch research pass run before the first question — every option labelled with its source. Run the layers, assemble the pool, then ask. This is what makes the choices follow the user's story instead of being one fixed list for every app.

**Questions travel in batches** — up to four per AskUserQuestion call, several calls per turn, sequential only across a real dependency. `interview.md` holds the batching rules, the four-option cap, and which questions are `multiSelect`.

**Every question goes through the AskUserQuestion tool, never prose text.** Options live in the tool call — the recommendation first and marked "(Recommended)", the consequence in each option's description. The tool caps at four options and adds "Other" on its own, which is how answers outside the options arrive. This holds in auto mode too: the interview is a decision only the user can make, and a prose question there simply ends the turn unanswered.

Every question must carry **more than two options**, **one marked recommendation**, and a **one-sentence consequence**. The user is a junior developer — options without a recommendation force a decision with nothing to base it on, and two options always read like a trap.

**Earlier answers shift later recommendations.** `adaptation.md` holds both sources: `Decision_Rules` from `ui-reasoning.csv` as the primary one, and a question-to-question table for what it does not map. Shifting a recommendation is allowed; removing an option is not, unless that option is genuinely impossible.

**Questions whose answer is already settled are not asked.** Decide, report one line as a derived decision, move on. Deciding silently is forbidden — the user must be able to cancel it.

Answers outside the options are always accepted. The user names something not listed → use it, state its consequence if you know it, or say you don't.

A search returning zero results, no Python, or the skill not installed → **the database layer drops out, the interview continues** on the other two layers, every option still labelled with its source. Never present a 0-result search as if it returned data.

### Translate into values

**Fast: this does not run** — the values come from the canvas, not from the database. In Full, run `ui-ux-pro-max` to turn the answers into concrete palettes, font pairings, and icon entries — the canvas's baseline. Read the script path and command shape from that skill's own SKILL.md — do not guess, and do not copy a path from here.

The `--variance --motion --density` dials are filled from the answers to decisions 1, 10, 12, and 9, never from any skill's built-in baseline.

Zero results → do not invent. Tell the user this recommendation came from general defaults, not from the database.

The output is the canvas's **baseline, not a gate** — do not stop to show it as its own proposal. The user corrects values where they are visible: on the canvas, at the judgement. Stopping here would judge the same values twice.

## Step 4 — Install, before anything is drawn

**Canvas path: the install block is its own chat gate, right after the interview closes** — in Full it follows the closing ledger, in Fast it follows the three dialogs; its contents are known once decisions 6 and 7 are answered, and everything is installed before the canvas is drawn (`canvas.md`). Do not ask twice, and **never put this block inside an AskUserQuestion** — a dialog covers the very block the user must read. Present the block, end the turn, and wait for the reply in chat.

One block, one approval:

```
Will install:
  npm install
  <component library>          [from decision 7]
  <what the library omits>     [researched per candidate under library-rubric.md]
  <icon pack>                  [from decision 7 — bundled, or its icon dialog]
  <engines>                    [chart · table · date · drag-and-drop — only what an
                                engine-rubric.md trigger decided, nothing speculative]
  <font>                       [self-hosted or a package — say which, and where it loads]
```

Wait for approval. Refused → hand over the commands for the user to run, then wait.

Install nothing outside that block. Something extra turns out to be needed → ask again, do not slip it in.

## Step 5 — The canvas: rounds until final

Drawn and judged under `canvas.md` entire: files written production-grade — every state drawn, fixtures in one contract-shaped file, imports only from the declared stack — the import self-check before every round, tagged departures and proposals, the judgement through AskUserQuestion, two rounds then escalation.

The PRD is not touched during rounds. The foundations board is the living draft of every value.

## Step 6 — Ratification: Section 5, the styling files, and `/styleguide`

**Approving the canvas is the approval — there is no second gate here.** This is the delta from `design-rework`: no old Section 5 exists, so there is no diff to protect and no separate stop. The values behind the approved canvas are read and reported as derived decisions are reported — one line each, cancellable — then written (`canvas.md`, Ratification).

The split is permanent:

| Written in | Contents |
|---|---|
| `PRD.md` Section 5 | **Rules and scale** — how many may exist, what is forbidden. "One icon family", "at most one accent", "four text steps" |
| Styling files (`tailwind.config`, CSS variables, the component library's theme file) | **Values** — font name, icon pack name, hex, radius number, spacing number |

Color and spacing are the exception: their roles, values, and usage rules are written in Section 5, because contrast is a norm and not an implementation detail.

Follow the sub-section structure in `prd-structure.md` under `app-init`. Fill the Anti-patterns sub-section from `references/anti-pattern.md`, taking only what is relevant to this kind of app.

**Page Composition holds the ratified archetype table from decision 10** — one row per archetype: shell layout, components, density profile, empty/loading wording, and the routes it owns. This table is what `build-flow` Section 4 opens every later page proposal from. Where decision 9 produced two density profiles, their numbers land under Breakpoints & Density.

**Every line in Section 5 traces back to one of four sources:** an interview answer, a derived decision already reported to the user, a canvas value the user ratified, or `references/anti-pattern.md`. A rule belonging to none of them is not written, however sensible it looks — no question asks it, so nobody decided it.

### Four rules bind the styling files

**Every semantic slot the component library exposes is mapped.** Libraries ship a full set of role colors, including a neutral one — usually named `default` — that every component falls back to when given no color. A slot left unmapped keeps the library's own value, so the app carries two neutral families: the one Section 5 chose, and the one nobody chose. List the library's slots before writing the theme file, then map all of them.

**A token nothing reads is not written.** A layout constant that the components duplicate as a utility class has two sources for one number, and the token is the one that will drift.

**Two roles with the same value collapse into one.** A palette naming both `danger` and `destructive` at the same hex has made one decision and written it twice. Merge before Section 5 is written.

**One palette, two consumers.** An app with both a utility-CSS theme and a component-library theme holds the same hex twice. The Section 5 color table is the source; both files are written in the same edit, never one alone.

### The `/styleguide` route

**One route file** (for example `src/pages/styleguide.tsx`), reachable at `/styleguide` in dev and kept out of the app's navigation and production build. It renders the whole visual language on one screen so the user corrects it here, while a correction is one token — not twenty screens later.

**It imports the production components and tokens.** Never hand-drawn copies, never a separate HTML file, never a second source of values. Deleting it later is deleting one file — offer that, never require it.

Sections, in order — each rendered from what Steps 2–6 actually decided, not from a fixed template:

| Section | Contents |
|---|---|
| Foundations | Color roles or scales as Section 5 defines them, with the semantic token list read from the styling files · every text step with a real sample sentence · spacing scale · the density profile table with its numbers, both profiles where decision 9 produced two · radius, shadow, breakpoints, motion |
| Components | Every component the app uses or an archetype names — variants, sizes, and states per component, including loading, empty, and failed where they apply, with a short real-usage snippet |
| Archetypes | The Section 5 archetype table, one card per archetype: shell sketch, components, routes |

**Done is measured against the table above, not against the page looking full.** Before reporting this route, check each row: every semantic token appears on the page; the component checklist is written first, not recalled — every component an archetype card names, each with its variants and states (inputs show default, focus, disabled, error; buttons show hover, focus, disabled, loading; mid-flow components — a stepper, a dialog, a dropzone — render in a static frame); every archetype card carries all three parts. When reporting the route, include the mapping **archetype → components it names → where each renders on this page**. The one legitimate absence is a component no archetype and no flow uses — stated, with that reason.

## Step 7 — Promotion: every page, on contract fixtures

**All canvas pages are promoted in one pass** — each file copied to its real route, the canvas wrapper removed, per `canvas.md`: element for element, chrome components first, the most data-dense page of the primary role leading. This is the same all-at-once promotion `design-rework` runs, with one structural difference: **there is usually no backend yet, so the pages keep their fixtures** — reshaped into `build-flow`'s contract form (`src/contracts/<page>.ts` for the types, `src/contracts/<page>.fixtures.ts` for the cases, per `references/contract.md` of `build-flow`). Real data arrives page by page through the queue; the fixture import is the marker of what is not yet wired.

No isolated branch is needed — a fresh repo has no parallel work to disturb; the pass runs in place.

**Every promoted-but-unwired page gets a `QUEUE.md` line** — `wire <page> to real data` — written by this pass. An app full of fixture-driven pages looks finished while every number on it is fake; the queue lines and the close block are what keep that visible. Where `logic-init` already chose the data layer, its loading, empty, and failed states come from the chosen cache when wiring happens — never from a handwritten effect.

**The densest page is the bar.** `build-flow` Section 4 judges every later page against it — building it thin lowers the bar for the whole app. Its fixtures must include `bulk` and `messy` cases: a direction that only holds for five tidy rows has not been proven. `ui-build` binds every promoted page in full — tokens only, zero raw values, states drawn.

Page running → **prove it at two widths with screenshots**: the desktop breakpoint from Section 5 and the lower bound from decision 10's minimum width. Capture follows PRD Section 1's Proof profile — the browser is the web profile's answer; a platform whose profile names an emulator or a window capture proves the same two bounds through it. No capture tooling → say so and report the profile's run target with both widths named — never claim the widths were judged without either.

**Rework rounds.** A page collapsing under its fixtures, or the user asking for a rework, is a rework round of that page. **A second rework of the same page → STOP, reopen Section 5**: Fast rises to the full interview, Full re-asks decisions 1–3, and the canvas is regenerated fresh from the answers, never patched. Section 5 changed → the styling values are updated with it, and the pages are rebuilt from the new tokens rather than patched.

## Step 8 — Verification: evidence, not eyes

Before reporting done:

- **The build passes.**
- **The structural diff per promoted page.** Put each canvas file beside its live page: with fixtures kept, the only legitimate differences are the removed canvas wrapper and the contract-shaped fixture import. Any other difference is a failed promotion to fix now.
- **Fonts load for real.** The computed font-family in the browser resolves to the loaded webfont, not a fallback stack — the canvas CSS carried the loading, and the production entry must carry it now.
- **Zero raw values** across every promoted page and component.
- **The styleguide passes its done-check** (the table in Step 6).
- **The densest page holds at both widths**, screenshots taken.
- **Pages running on fixtures are listed by name.** This list matches the `QUEUE.md` wire lines one for one — a page on neither list does not exist.

Any of them fails → fix it in the same session.

**The canvas files stay after promotion** — frozen references under `canvas.md`'s lifecycle: each dies only when its page is wired with real data, survives both widths, and the user confirms the side-by-side at a chat stop — never through an AskUserQuestion, which would cover the comparison being read. `build-flow` carries that per page through the queue. Never delete unasked.

## Step 9 — Close

**Nothing stays a draft.** Every canvas page ends promoted into a real route; a page left in the repo unrouted is dead code that reads as finished work.

One block: the visual decisions that settled · files changed · each page's fate — promoted and wired, or promoted on fixtures with its `QUEUE.md` wire line · the canvas files still standing and the queue line that will retire each · the `/styleguide` route named as staying dev-only, deletable at the user's word · what is still `[needs verification]`.

State that this gate **no longer applies** to later pages — from here on what binds is Section 5 and the component rules in `ui-build`.

Close by reminding the user that the commit waits for their word.
