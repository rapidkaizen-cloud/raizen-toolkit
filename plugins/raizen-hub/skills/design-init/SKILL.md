---
name: design-init
description: Decide the visual direction and component library of an app whose PRD Section 5 is still unwritten. By default a batched 10-question interview (options assembled live from the ui-ux-pro-max database, domain reading, and a web-research pass) captures the user's preferences, and a temporary in-repo canvas — real component library, canvas-owned theme, the user's feature brief — renders them as every page of the app, expanding thin briefs into a full product with tagged feature proposals and tagged departures; fast mode draws the canvas straight from three questions. Ratifies value by value, writes the rules and the screen-archetype table into PRD Section 5, writes the concrete values into the styling files, generates the dev-only /styleguide route, then promotes the canvas pages into the app's real pages. Use before the first UI component of a repo is written, or when PRD Section 5 is still marked as unverified.
---

# design-init — set the visual direction once, in code

Bootstrap produces a `PRD.md` with an empty Section 5. This skill fills it, then **proves it on a real page** — not a picture, not a description.

Run **once per repo**. After the canvas is ratified and its pages promoted, later pages are bound by Section 5 and the component rules in `ui-build`, with no further gate.

## Hard limits

`PRD.md` Section 5 is the only part of the document written. **Do not** create `MASTER.md`, `DESIGN.md`, `design-system/`, or an interview summary as a file. If another skill in this session produces a document, it is not committed and not referenced.

`ui-ux-pro-max` is run **without `--persist`**. That flag writes `design-system/<slug>/MASTER.md` and calls itself the *Global Source of Truth* — two normative documents for the same thing means Section 5 dies slowly.

This is one of only two paths allowed to write Section 5, and only while Section 5 is still empty. Its contents come from the user's answers, not from the agent's taste and not from another skill's output. A Section 5 that is already filled changes only by the user's decision — see `prd-format` in `raizen-norms`.

Do not commit and do not push. Staging is fine; the commit waits for the user.

Not decided by the user → `[needs verification]`.

## Step 0 — Preconditions

Check and report one short block:

```
PRD.md      : [present / missing]
Section 5   : [empty / already filled / product without UI]
Kind of app : [from Section 1]
Primary role: [from Section 2]
Reading     : [one sentence — see below]
Flow        : mode → canvas or questions → Section 5 → styling → promotion
```

`PRD.md` missing → **STOP**, point to `app-init`.

Section 5 already filled → **STOP**, ask whether the user really wants to rework the existing visual direction. That work belongs to `design-rework`.

**Section 5 empty but UI components already exist → STOP as well.** This skill decides a direction before any code carries one. An app that already has components needs its existing values measured and put to the user, not overwritten by an interview that has never seen them. That is `design-rework` on its ratify path — the case a repo arrives in through `app-rework`'s document mode.

Product without UI → **STOP**, this skill does not apply.

**Reading** is your own conclusion before asking anything, one sentence, shaped as: *"I read this as [kind of app] for [who uses it], leaning [the feel that fits], because [reason from the PRD]."*

Concluding first beats asking from nothing: the user only corrects what missed, and the correction carries more than an empty question would. A wrong reading is not a failure — it draws out detail that no question would surface.

State the reading, ask for correction, then continue. When the correction is asked through AskUserQuestion, **the full reading sentence goes inside the question field itself** — the dialog may render without the prose around it, so a question that points at text "above" can arrive pointing at nothing. The corrected reading becomes the keywords for every query in Step 2.

**The Step 2 mode question rides in this same AskUserQuestion call** — two questions, one dialog, one turn. Neither reads the other's answer, so nothing is lost by pairing them.

## Step 1 — Route the supporting skills

Read the kind of app from PRD Section 1, then decide once:

| Kind of app | Skills used |
|---|---|
| Internal dashboard · single-role internal tool | `ui-ux-pro-max` only |
| Public site | `ui-ux-pro-max` **and** `design-taste-frontend` |

`design-taste-frontend` states itself that it is not for dashboards, data tables, or multi-step product UI. Using it outside that boundary produces motion dials and icon rules that collide with `ui-ux-pro-max`. Its prohibitions are still used for every kind of app through `references/anti-pattern.md` — that is material, not a live authority.

This table routes the **interview's** live authorities only. The canvas phase additionally reads `high-end-visual-design` and `frontend-design` as material for every kind of app — `canvas.md` states the rule and the same limit: material raises the floor of the free hand, and the user's answer wins every collision.

The two skills disagree about icon pack, motion level, or typeface → **the user's answer wins**, which is exactly why all three are asked.

## Step 2 — The mode, then the canvas or the questions

### Pick the mode first — asked in the Step 0 call, before anything else

Offer three, with a recommendation:

| Mode | What is asked | For whom |
|---|---|---|
| **Stock** | Question 12 only, plus question 13 when the chosen library bundles no icon pack. Nothing else is asked and nothing else is derived — the library's own defaults become the design system | An app whose look nobody has an opinion about, and nobody will |
| **Fast** | Three questions — 12 · 13 when the library bundles none · 17 — then the canvas is designed whole from the feature brief, **every value the designer's own**. See `references/canvas.md` | An app that must ship today, or a user who wants to judge a finished proposal rather than answer questions |
| **Full** | The 10 asked entries in `interview.md`, batched into a few turns — the answers are the user's preferences and the canvas's baseline; the canvas departs wherever the designer judges better, every departure tagged and settled by the user at the judgement. See `references/canvas.md` | **Recommended.** The preferences are captured before anything is drawn, and the canvas shows them as an app instead of as a list |

**Consequence:** all three still end at real pages running on screen, so no mode decides blind — the difference is only where the correction happens, before or after the first screen.

**Fast and Full both end at the canvas; they differ in where the values start.** In Full the interview captures the user's preferences as the baseline and the canvas renders them, departing wherever the designer judges better — each departure tagged and settled by the user at the judgement; in Fast the canvas improvises the values too. Either way the archetype table is still derived and ratified, Section 5 is still written, the styleguide still renders from production tokens, and the pages still end real — `canvas.md` holds the sequence, the quarantine rules, and the promotion with its frozen-reference lifecycle — the canvas empties page by page as real data lands, never before. **A canvas that misses twice escalates:** Fast rises to the full interview; Full re-asks decisions 1–5.

**A mode skips questions, never outputs.** The archetype table (question 18), the `/styleguide` route (Step 6), and real running pages are produced in every mode, fast and stock included — what changes per mode is only where their decisions come from.

### Stock mode

Stock is not fast mode with fewer questions. It is a different decision: **this app has no visual direction of its own, and the library's defaults are adopted whole.**

Say all three of these before the user picks it, because none of them is obvious from the name:

1. **The app will look like the library's demo.** That is the mode working, not a defect.
2. **Density is the library's density.** PRD Section 1 or 4 asking for dense screens while the chosen library ships a spacious one is a real conflict — name it and ask which side gives way. Stock plus a density requirement is the one combination that cannot hold, and it fails silently as a pile of overrides months later.
3. **Changing your mind later is `design-rework`, not an edit.** One override added quietly is how a stock app becomes an app with no design system at all.

Steps 1 and 3 do not run, and neither do the four styling-file rules in Step 4 — there is no theme to write and nothing to translate. Read `references/library-rubric.md` for question 12, skip the rest. Steps 5 through 8 run unchanged: the install block is still approved, and the first page is still built and judged, because it is the only way the user sees what "as it ships" looks like before twenty screens exist.

**The archetype table is the one derivation stock keeps.** The library decides how components look, never which pages hold what — so the question 18 derivation still runs, its table is still ratified, and it joins the stock Section 5 together with the block below. Skipping it would leave `build-flow` Section 4 with no archetype to open any page proposal from.

**Section 5 is still written, and never as `[needs verification]`.** It records the decision that no decision was made:

```
## 5. Design System

Visual direction: the defaults of <library> <version>, adopted unmodified.

- No theme file, no custom token, no palette belonging to this app.
- No component override. There is no rule in this section for one to cite,
  so every override is a finding — see `ui-build`, Library defaults.
- Icons: <the bundled pack, or the pack chosen in question 13>. One family.
- Changing any of this is `design-rework`, not an edit to this section.
```

That shape carries the whole mode. `ui-build` gates on Section 5 being *written*, and lets an override through only when a line here demands it — so a stock Section 5 passes the gate and refuses every override at once, with no new rule anywhere. A stock app left on `[needs verification]` gets the opposite: the gate blocks every page, and the user is stopped by a decision they already made.

Derived decisions are **never silent, in either mode.** Every decision not asked is reported on one line with its basis:

```
Q14 radius   → 8px     (from Design System Variables of style "Minimalism & Swiss")
Q24 motion   → subtle  (from the Effects & Animation column of the same style)
Q25 feedback → inline failures, toast successes (built-in; no basis in the data)
```

A line whose basis is "built-in" is marked as such. The user may cancel any line, and cancelling it opens that question normally.

A second rework in Step 7 → Fast rises to the full interview; Full re-asks decisions 1–5, as Step 7 describes. Missing twice means guessing is not the right path for this app.

### Running the interview

Read `references/interview.md`, `references/adaptation.md`, and — for question 12 — `references/library-rubric.md`.

**The order in `interview.md` is the order asked.** No question is promoted to the front because it feels foundational, and none is deferred because its answer looks obvious.

**The options for each question are not written in any file, and the database is not their only source.** `interview.md` names three layers — the `ui-ux-pro-max` query, the model's own domain reading, and a mandatory one-off WebSearch research pass run before the first question — every option labelled with its source. Run the layers, assemble the pool, then ask. This is what makes the choices follow the user's story instead of being one fixed list for every app.

**Questions travel in batches** — up to four per AskUserQuestion call, several calls per turn, sequential only across a real dependency. `interview.md` holds the batching rules, the four-option cap, and which questions are `multiSelect`.

**Every question goes through the AskUserQuestion tool, never prose text.** Options live in the tool call — the recommendation first and marked "(Recommended)", the consequence in each option's description. The tool caps at four options and adds "Other" on its own, which is how answers outside the options arrive. This holds in auto mode too: the interview is a decision only the user can make, and a prose question there simply ends the turn unanswered.

Every question must carry **more than two options**, **one marked recommendation**, and a **one-sentence consequence**. The user is a junior developer — options without a recommendation force a decision with nothing to base it on, and two options always read like a trap.

**Earlier answers shift later recommendations.** `adaptation.md` holds both sources: `Decision_Rules` from `ui-reasoning.csv` as the primary one, and a question-to-question table for what it does not map. Shifting a recommendation is allowed; removing an option is not, unless that option is genuinely impossible.

**Questions whose answer is already settled are not asked.** Decide, report one line as a derived decision, move on. Deciding silently is forbidden — the user must be able to cancel it.

Answers outside the options are always accepted. The user names something not listed → use it, state its consequence if you know it, or say you don't.

A search returning zero results, no Python, or the skill not installed → **the database layer drops out, the interview continues** on the other two layers, every option still labelled with its source. Never present a 0-result search as if it returned data.

## Step 3 — Translate into values

**Fast: this step does not run** — the values come from the canvas, not from the database. In Full the translation feeds the canvas's baseline; stock skips this step entirely.

Run `ui-ux-pro-max` to turn the answers into concrete palettes, font pairings, and icon entries. Read the script path and command shape from that skill's own SKILL.md — do not guess, and do not copy a path from here.

The `--variance --motion --density` dials are filled from the answers to questions 1, 18, 24, and 16, never from any skill's built-in baseline.

Zero results → do not invent. Tell the user this recommendation came from general defaults, not from the database.

The output is the canvas's **baseline, not a gate** — do not stop to show it as its own proposal. The user corrects values where they are visible: on the canvas, at the judgement. Stopping here would judge the same values twice.

## Step 4 — Write Section 5 and the styling files

The split is permanent:

| Written in | Contents |
|---|---|
| `PRD.md` Section 5 | **Rules and scale** — how many may exist, what is forbidden. "One icon family", "at most one accent", "four text steps" |
| Styling files (`tailwind.config`, CSS variables, the component library's theme file) | **Values** — font name, icon pack name, hex, radius number, spacing number |

Color and spacing are the exception: their roles, values, and usage rules are written in Section 5, because contrast is a norm and not an implementation detail.

Follow the sub-section structure in `prd-structure.md` under `app-init`. Fill the Anti-patterns sub-section from `references/anti-pattern.md`, taking only what is relevant to this kind of app.

**Page Composition holds the ratified archetype table from question 18** — one row per archetype: shell layout, components, density profile, empty/loading wording, and the routes it owns. This table is what `build-flow` Section 4 opens every later page proposal from, so a Section 5 written without it leaves every future page assembling its layout from nothing. Where question 16 produced two density profiles, their numbers land under Breakpoints & Density.

**Every line in Section 5 traces back to one of four sources:** an interview answer, a derived decision already reported to the user, a canvas value the user ratified (the canvas path), or `references/anti-pattern.md`. A rule belonging to none of them is not written, however sensible it looks — no question asks it, so nobody decided it. A prohibition nobody was asked about still binds every session that follows, and the user only finds out months later, wondering why the app refuses to do something.

### Four rules bind the styling files

**Every semantic slot the component library exposes is mapped.** Libraries ship a full set of role colors, including a neutral one — usually named `default` — that every component falls back to when given no color. A slot left unmapped keeps the library's own value, so the app carries two neutral families: the one Section 5 chose, and the one nobody chose. List the library's slots before writing the theme file, then map all of them. This failure is silent: the app looks finished, and the foreign color only surfaces on the components nobody gave a color to.

**A token nothing reads is not written.** A layout constant that the components duplicate as a utility class has two sources for one number, and the token is the one that will drift. Write the token and use it, or use the utility and drop the token.

**Two roles with the same value collapse into one.** A palette naming both `danger` and `destructive` at the same hex has not made two decisions; it has made one and written it twice. Merge before Section 5 is written — afterwards every session has to guess which of the two applies here.

**One palette, two consumers.** An app with both a utility-CSS theme and a component-library theme holds the same hex twice. The Section 5 color table is the source; both files are written in the same edit, never one alone. A color changed in one and not the other splits the app in half — utility classes follow one palette, library components the other, and the seam only shows on the screens nobody has opened yet.

Section 5 finished → **on the canvas path it is a report, not a gate**: the values were ratified on the canvas, and a second approval over the same pixels is the double gate `canvas.md` forbids. Only stock still stops here — its Section 5 was never judged anywhere, so show it and wait before touching any dependency.

## Step 5 — Ask once to install

**Canvas path: the install block is approved inside the interview itself** — in Fast at the three questions, in Full as the **last question of the final batch**, its contents known once Q12, Q13, and the font are answered — and installed before the canvas is drawn (`canvas.md`). Do not ask twice. Only stock reaches this step as a standalone ask, after its Section 5 stop above.

One block, one approval:

```
Will install:
  npm install
  <component library>          [from question 12]
  <what the library omits>     [the "Needs extra" column in library-rubric.md]
  <icon pack>                  [from question 13]
  <font>                       [self-hosted or a package — say which]
```

Wait for approval. Refused → hand over the commands for the user to run, then wait.

Install nothing outside that block. Something extra turns out to be needed → ask again, do not slip it in.

## Step 6 — Generate `/styleguide`, then the first pages

### The styleguide route comes first

**One route file** (for example `src/pages/styleguide.tsx`), reachable at `/styleguide` in dev and kept out of the app's navigation and production build. It renders the whole visual language on one screen so the user corrects it here, while a correction is one token — not twenty screens later.

**It imports the production components and tokens.** Never hand-drawn copies, never a separate HTML file, never a second source of values. That is the whole defence against drift: a page that renders the real `Button` with the real theme cannot disagree with the app. Deleting it later is deleting one file — offer that, never require it.

Sections, in order — each rendered from what Steps 2–4 actually decided, not from a fixed template:

| Section | Contents |
|---|---|
| Foundations | Color roles or scales as Section 5 defines them, with the semantic token list read from the styling files · every text step with a real sample sentence · spacing scale · the density profile table with its numbers, both profiles where question 16 produced two · radius, shadow, breakpoints, motion |
| Components | Every component the app uses or an archetype names — variants, sizes, and states per component, including loading, empty, and failed where they apply, with a short real-usage snippet |
| Archetypes | The Section 5 archetype table, one card per archetype: shell sketch, components, routes |

Realistic sample data, the same standard the first page holds below. `ui-build` binds this route like any page.

**Done is measured against the table above, not against the page looking full.** The observed failure is always the same sampler: one input rendered in one state, archetype cards reduced to a route plus a sentence, the Reference section silently absent — and it reads as finished. Before reporting this route, check each row:

- **Foundations** — every semantic token the styling files define appears on the page, and the density profile table shows its numbers rather than a summary sentence.
- **Components** — the checklist is written first, not recalled: every component an archetype card names, plus every form control the app's flows use. Each entry renders with its variants and states — inputs show default, focus, disabled, and error; buttons show hover, focus, disabled, and loading. A component that lives mid-flow — a stepper, a tab set, a dialog, an upload dropzone — renders here in a static frame; "needs a flow to show" is not a reason to skip it.
- **Archetypes** — every card carries all three parts: shell sketch, component list, routes. A route with one describing sentence is not a card.

When reporting the route, include the mapping **archetype → components it names → where each renders on this page**. A named component with no render is work to finish in this session, not a gap to note. The one legitimate absence is a component no archetype and no flow uses — stated, with that reason.

### The first page

**On the canvas path this page arrives by promotion** — see `canvas.md`; the standards below bind it either way. On the question paths it is built here, as the proof of the direction.

**One page: the most data-dense one belonging to the primary role.** That is where density, tables, and text hierarchy are all tested at once — the three things that decide how an internal app feels. A login page tests nothing.

Realistic dummy data, not lorem and not empty placeholders. Names, dates, and numbers that make sense for the domain in PRD Section 4.

**That data is written as this page's contract and fixtures**, in the shape `build-flow` uses — `src/contracts/<page>.ts` for the types, `src/contracts/<page>.fixtures.ts` for the cases, per `references/contract.md` of `build-flow`. This is the first page of the app either way, so the pattern it sets is the one every later page copies; leaving its data inline means page two starts by inventing a convention that already exists. Judging the direction needs `bulk` and `messy` in particular — a direction that only holds for five tidy rows has not been proven.

**Improvisation is allowed, and expected.** Add summary cards, charts, badges, filters — anything that makes the page feel alive. Section 5 holds component **rules**, not a component **list**, so adding a component never violates it. A first page that is nothing but a bare table fails to test density and hierarchy, the two reasons it matters.

That richness outlives this session: `build-flow` Section 4 judges every later page against this one. A page far emptier than this one goes back to its content proposal rather than becoming the app's new normal. Building this page thin therefore costs more than one page — it lowers the bar for all of them.

Four limits:

- **Data comes from the terms in Section 4.** Do not invent metrics that have no name in this domain.
- **Do not imply features nobody decided on — untagged.** An improvised feature carries its proposal tag until the user keeps it at the judgement; a "revenue forecast" chart with no tag and no decision is a lie that will be invoiced later as a feature.
- **Everything still goes through tokens.** What is forbidden is not a new component, but a new token, a second accent, or a second icon family.
- **`ui-build` binds this page too**, in full — library defaults, and the loading, empty, and failed states written together with their component. A skeleton rather than a spinner, an empty state that says why it is empty. A page that skips them is not proving the direction, it is postponing it, and it is the page every later session copies from.

Zero raw hex, font sizes, or spacing in components — this rule applies from the first page, not later.

Data access on this page goes through the layer `logic-init` decided, when that session ran — its loading, empty, and failed states come from the chosen cache, not from a handwritten effect that the first real page would then replace.

**The page proves one archetype in full — name which.** Every later page of that archetype copies this one, so an archetype proven here is an archetype nobody re-derives.

Page running → **prove it at two widths with screenshots**: the desktop breakpoint from Section 5 and the lower bound from question 17. Take them with the browser tooling available to the session; no browser tooling → say so and report the dev-server URL with both widths named for the user to check — never claim the widths were judged without either. What is judged at the lower bound is how tables and navigation collapse, not a separate page.

**On the canvas modes this page arrives by promotion** — its canvas file moved to the real path, real data wired — and the judgement is survival of real data: holding → report and continue; collapsing → a rework round of this page. **On stock** there is no canvas — report how to view it (the dev server command and its URL), then **STOP** and wait for the user's judgement.

## Step 7 — Rework rounds

The user may ask for a full rework any number of times. But:

**A second rework of the same page → STOP, reopen Section 5.** Missing once means the layout was off. Missing twice means the visual direction was off, and rewriting the layout a third time will not fix that.

When reopening: Fast rises to the full interview; Full re-asks decisions 1–5 — and either way the canvas is regenerated fresh from the answers, as `canvas.md` describes, never patched.

Ask decisions 1–5 again (three questions, after the palette merge), especially question 2 about the app that feels right. The user still struggles to name one → ask them to show an app or a site, because adjectives have demonstrably run out by that point.

Section 5 changed → the styling values are updated with it, and the pages are rebuilt from the new tokens rather than patched.

## Step 8 — Close

**Nothing stays a draft.** Before this step closes, canvas pages end promoted into real routes, and a question-path first page is either routed as a real page or deleted. A page left in the repo unrouted is dead code that reads as finished work: the next session finds it, copies its patterns, and inherits whatever it got wrong — while the queue still lists that page as unbuilt.

**Frozen canvas references are not drafts.** After promotion the canvas folder keeps the ratified originals under `canvas.md`'s lifecycle — comparison references until each page is wired with real data, deleted page by page by the session that wires it. The close block lists every canvas file still standing and the queue line that will retire it.

One block: the visual decisions that settled · files changed · each page's fate — promoted, routed, or deleted · the `/styleguide` route named as staying dev-only, deletable at the user's word · what is still `[needs verification]`.

State that this gate **no longer applies** to later pages — from here on what binds is Section 5 and the component rules in `ui-build`.

Close by reminding the user that the commit waits for their word.
