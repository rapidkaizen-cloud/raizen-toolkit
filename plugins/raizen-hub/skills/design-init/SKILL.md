---
name: design-init
description: Decide the visual direction and component library of an app whose PRD Section 5 is still unwritten. Interviews the user through 13 frontend questions covering 29 decisions — the rest derived and reported — with options drawn live from the ui-ux-pro-max database, writes the rules into PRD Section 5, writes the concrete values into the styling files, then builds one real reference page in code. Use before the first UI component of a repo is written, or when PRD Section 5 is still marked as unverified.
---

# design-init — set the visual direction once, in code

Bootstrap produces a `PRD.md` with an empty Section 5. This skill fills it, then **proves it on a real page** — not a picture, not a description.

Run **once per repo**. After the reference page is approved, later pages are bound by Section 5 and the component rules in `ui-build`, with no further gate.

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
Flow        : 13 questions → Section 5 → styling → reference page
```

`PRD.md` missing → **STOP**, point to `app-init`.

Section 5 already filled → **STOP**, ask whether the user really wants to rework the existing visual direction. That work belongs to `design-redesign`.

Product without UI → **STOP**, this skill does not apply.

**Reading** is your own conclusion before asking anything, one sentence, shaped as: *"I read this as [kind of app] for [who uses it], leaning [the feel that fits], because [reason from the PRD]."*

Concluding first beats asking from nothing: the user only corrects what missed, and the correction carries more than an empty question would. A wrong reading is not a failure — it draws out detail that no question would surface.

State the reading, ask for correction, then continue. When the correction is asked through AskUserQuestion, **the full reading sentence goes inside the question field itself** — the dialog may render without the prose around it, so a question that points at text "above" can arrive pointing at nothing. The corrected reading becomes the keywords for every query in Step 2.

## Step 1 — Route the supporting skills

Read the kind of app from PRD Section 1, then decide once:

| Kind of app | Skills used |
|---|---|
| Internal dashboard · single-role internal tool | `ui-ux-pro-max` only |
| Public site | `ui-ux-pro-max` **and** `design-taste-frontend` |

`design-taste-frontend` states itself that it is not for dashboards, data tables, or multi-step product UI. Using it outside that boundary produces motion dials and icon rules that collide with `ui-ux-pro-max`. Its prohibitions are still used for every kind of app through `references/anti-pattern.md` — that is material, not a live authority.

The two skills disagree about icon pack, motion level, or typeface → **the user's answer wins**, which is exactly why all three are asked.

## Step 2 — Interview, 13 questions

### Pick the mode first — one question, before anything else

Offer two, with a recommendation:

| Mode | What is asked | For whom |
|---|---|---|
| **Fast** | Nothing. All 29 decisions are derived from the Step 0 reading, then shown once as a list to correct | An app that must ship today, or a visual direction nobody disputes |
| **Full** | The 13 asked entries in `interview.md` — the icon-pack question joins when the chosen library bundles none, the table group drops when the app has no tables. Every other decision is derived | **Recommended.** Thirteen answers cover everything expensive to get wrong; the rest never needed asking |

**Consequence:** both still end at a working reference page, so fast mode is not deciding blind — the only difference is where the correction happens, before or after the first screen.

Derived decisions are **never silent, in either mode.** Every decision not asked is reported on one line with its basis:

```
Q14 radius   → 8px     (from Design System Variables of style "Minimalism & Swiss")
Q24 motion   → subtle  (from the Effects & Animation column of the same style)
Q25 feedback → inline failures, toast successes (built-in; no basis in the data)
```

A line whose basis is "built-in" is marked as such. The user may cancel any line, and cancelling it opens that question normally.

A second rework in Step 7 → fast rises to full. A session already in full re-asks decisions 1–5, as Step 7 describes. Missing twice means guessing is not the right path for this app.

### Running the interview

Read `references/interview.md`, `references/adaptation.md`, and — for question 12 — `references/library-rubric.md`.

**The order in `interview.md` is the order asked.** No question is promoted to the front because it feels foundational, and none is deferred because its answer looks obvious.

**The options for each question are not written in any file.** `interview.md` names which query to run against `ui-ux-pro-max` and which column becomes the options. Run the query, assemble the options from the result, then ask. This is what makes the choices follow the user's story instead of being one fixed list for every app.

**One question per turn.** Never bundled.

**Every question goes through the AskUserQuestion tool, never prose text.** Options live in the tool call — the recommendation first and marked "(Recommended)", the consequence in each option's description. The tool caps at four options and adds "Other" on its own, which is how answers outside the options arrive. This holds in auto mode too: the interview is a decision only the user can make, and a prose question there simply ends the turn unanswered.

Every question must carry **more than two options**, **one marked recommendation**, and a **one-sentence consequence**. The user is a junior developer — options without a recommendation force a decision with nothing to base it on, and two options always read like a trap.

**Earlier answers shift later recommendations.** `adaptation.md` holds both sources: `Decision_Rules` from `ui-reasoning.csv` as the primary one, and a question-to-question table for what it does not map. Shifting a recommendation is allowed; removing an option is not, unless that option is genuinely impossible.

**Questions whose answer is already settled are not asked.** Decide, report one line as a derived decision, move on. Deciding silently is forbidden — the user must be able to cancel it.

Answers outside the options are always accepted. The user names something not listed → use it, state its consequence if you know it, or say you don't.

A search returning zero results, no Python, or the skill not installed → **do not invent**. Say so plainly, then offer to postpone or to continue with self-assembled options that are explicitly marked as not coming from the database.

## Step 3 — Translate into values

Run `ui-ux-pro-max` to turn the answers into concrete palettes, font pairings, and icon entries. Read the script path and command shape from that skill's own SKILL.md — do not guess, and do not copy a path from here.

The `--variance --motion --density` dials are filled from the answers to questions 1, 18, 24, and 16, never from any skill's built-in baseline.

Zero results → do not invent. Tell the user this recommendation came from general defaults, not from the database.

The output is a **proposal**, not a decision. Show it to the user, invite corrections, then continue.

## Step 4 — Write Section 5 and the styling files

The split is permanent:

| Written in | Contents |
|---|---|
| `PRD.md` Section 5 | **Rules and scale** — how many may exist, what is forbidden. "One icon family", "at most one accent", "four text steps" |
| Styling files (`tailwind.config`, CSS variables) | **Values** — font name, icon pack name, hex, radius number, spacing number |

Color and spacing are the exception: their roles, values, and usage rules are written in Section 5, because contrast is a norm and not an implementation detail.

### Four rules bind the styling files

**Every semantic slot the component library exposes is mapped.** Libraries ship a full set of role colors, including a neutral one — usually named `default` — that every component falls back to when given no color. A slot left unmapped keeps the library's own value, so the app carries two neutral families: the one Section 5 chose, and the one nobody chose. List the library's slots before writing the theme file, then map all of them. This failure is silent: the app looks finished, and the foreign color only surfaces on the components nobody gave a color to.

**A token nothing reads is not written.** A layout constant that the components duplicate as a utility class has two sources for one number, and the token is the one that will drift. Write the token and use it, or use the utility and drop the token.

**Two roles with the same value collapse into one.** A palette naming both `danger` and `destructive` at the same hex has not made two decisions; it has made one and written it twice. Merge before Section 5 is written — afterwards every session has to guess which of the two applies here.

**One palette, two consumers.** An app with both a utility-CSS theme and a component-library theme holds the same hex twice. The Section 5 color table is the source; both files are written in the same edit, never one alone. A color changed in one and not the other splits the app in half — utility classes follow one palette, library components the other, and the seam only shows on the screens nobody has opened yet.

Follow the sub-section structure in `prd-structure.md` under `app-init`. Fill the Anti-patterns sub-section from `references/anti-pattern.md`, taking only what is relevant to this kind of app.

**Every line in Section 5 traces back to one of three sources:** an interview answer, a derived decision already reported to the user, or `references/anti-pattern.md`. A rule belonging to none of them is not written, however sensible it looks — no question asks it, so nobody decided it. A prohibition nobody was asked about still binds every session that follows, and the user only finds out months later, wondering why the app refuses to do something.

Section 5 finished → show it to the user, **STOP**, wait for approval before touching any dependency.

## Step 5 — Ask once to install

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

## Step 6 — Build the reference page

**One page: the most data-dense one belonging to the primary role.** That is where density, tables, and text hierarchy are all tested at once — the three things that decide how an internal app feels. A login page tests nothing.

Realistic dummy data, not lorem and not empty placeholders. Names, dates, and numbers that make sense for the domain in PRD Section 4.

**Improvisation is allowed, and expected.** Add summary cards, charts, badges, filters — anything that makes the page feel alive. Section 5 holds component **rules**, not a component **list**, so adding a component never violates it. A reference page that is nothing but a bare table fails to test density and hierarchy, the two reasons it is built.

Three limits:

- **Data comes from the terms in Section 4.** Do not invent metrics that have no name in this domain.
- **Do not imply features nobody decided on.** A "revenue forecast" chart in an app with no forecasting is a lie that will be invoiced later as a feature.
- **Everything still goes through tokens.** What is forbidden is not a new component, but a new token, a second accent, or a second icon family.
- **`ui-build` binds this page too**, in full — library defaults, and the loading, empty, and failed states written together with their component. A skeleton rather than a spinner, an empty state that says why it is empty. A reference page that skips them is not proving the direction, it is postponing it, and it is the page every later session copies from.

Zero raw hex, font sizes, or spacing in components — this rule applies from the first page, not later.

Data access on this page goes through the layer `logic-init` decided, when that session ran — its loading, empty, and failed states come from the chosen cache, not from a handwritten effect that the first real page would then replace.

Page running → show two widths: desktop and mobile. What is judged at mobile width is how tables and navigation collapse, not a separate page.

Report how to view it (the dev server command and its URL), then **STOP** and wait for the user's judgement.

## Step 7 — Rework rounds

The user may ask for a full rework any number of times. But:

**A second rework of the same page → STOP, reopen Section 5.** Missing once means the layout was off. Missing twice means the visual direction was off, and rewriting the layout a third time will not fix that.

When reopening, fast rises to full; a session already in full re-asks decisions 1–5.

Ask decisions 1–5 again (three questions, after the palette merge), especially question 2 about the app that feels right. The user still struggles to name one → ask them to show an app or a site, because adjectives have demonstrably run out by that point.

Section 5 changed → the styling values are updated with it, and the reference page is rebuilt from the new tokens rather than patched.

## Step 8 — Close

**The reference page does not stay a draft.** Before this step closes it is either routed as a real page of this app, or deleted. A page left in the repo unrouted is dead code that reads as finished work: the next session finds it, copies its patterns, and inherits whatever it got wrong — while the queue still lists that page as unbuilt.

One block: the visual decisions that settled · files changed · the reference page's fate, routed or deleted · what is still `[needs verification]`.

State that this gate **no longer applies** to later pages — from here on what binds is Section 5 and the component rules in `ui-build`.

Close by reminding the user that the commit waits for their word.
