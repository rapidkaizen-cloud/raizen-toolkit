---
name: docs-format
description: Rules for the documents an app repo keeps — the closed list under docs/, DESIGN.md and the root README.md; what each holds, who reads and writes it, what triggers a write, which writes stop for the user, which files are frozen, and how a legacy root PRD.md maps onto them. Use before writing, editing, or proposing a change to any of them, and when deciding whether something should be recorded at all.
---

# docs-format — the documents an app repo keeps

Every skill names a document by its path in this form. A repo on the legacy form reads each path through the map at the end.

## Which form

- **A root `PRD.md` → the legacy form.** Keep it. Never migrate it, and never create a `docs/` file beside it.
- **No root `PRD.md` → this form.** `app-settle` writes it, into an empty directory and into an app that never had a PRD.

## The closed list

Write no document outside this list — no `ARCHITECTURE.md`, `DECISIONS.md`, audit report, plan file, or second index. One found is a finding. A document another skill offers to write is not written.

| File | Holds | Read by | Written by, and when | Gate |
|---|---|---|---|---|
| `docs/README.md` | The index: every file below that exists, one line each | Every session — injected at start | `app-settle` seeds it; the commit adding or removing a listed file updates it | None |
| `docs/product.md` | Context — Surface, Data, Deploy, the Proof profile · problem · success · non-goals · roles · prohibitions | Every session — injected at start | `app-settle`; any session, the moment a sentence in it becomes false | Prohibitions and non-goals stop for the user |
| `docs/rules.md` | The business rules, each an explicit sentence with its why | A build session before implementing; `logic-build` Section 10 | `app-settle`; a build session, before the implementation | The user decides the rule |
| `docs/glossary.md` | Domain terms, their precise meaning, what they are misread as | Any session naming a thing | Any session, before the implementation that uses the term | None — append-only |
| `docs/queue.md` | What is not built yet | Every session — injected at start | `build-flow` | `build-flow` Section 3 |
| `docs/decisions/` | One record per decision — stack, library, logic layer, a deliberate "none", a technical choice the user takes | A session about to change a settled choice; `logic-build` Section 6 | `app-settle`, `logic-settle`, `design-settle`; a session changing a library default, or recording a technical choice the user took | The user's answer — then immutable |
| `docs/guide/` | How each role finishes each piece of its work, for the app's users | The app's users; the help page | The build session whose commit changes what a page describes | None — mandatory |
| `docs/whats-new.md` | What users notice, newest first | The app's users, through the help page | The build session whose commit users will notice | Exists only where the app has an in-app help page |
| `docs/changes/` | One record per big change — why, what it touches, the lines it wrote | The sessions executing it | `build-flow`, past its big-change threshold | The user's approval — frozen when done |
| `docs/PRD.md` | The app as first approved | Nobody after seeding — history | `app-settle`, bootstrap and document mode | The user's approval — frozen when written |
| `DESIGN.md` | The design system — tokens, and the rules for applying them | `ui-build` before any UI; every agent through `AGENTS.md` | `design-settle` alone | The section below |
| `README.md` | What the app is and how to run it | Developers | `app-settle`; the commit changing how the app runs | None |

`CLAUDE.md` and `AGENTS.md` instruct agents and record nothing about the app; `app-settle` owns their shape.

## What belongs in any of them

**Write only what a live check cannot recover.** Test every sentence: *deleted, could reading the repo or introspecting the database bring it back?* Yes → do not write it. Tables, columns, routes, components, versions, and whether something is built are read from the code and the live database; a document answering them is a finding.

**Two exceptions.** The Surface row and the Proof profile are written regardless, because every skill that proves a page reads them before it has read enough of the repo to derive them. `docs/guide/` and `docs/whats-new.md` are written for the app's users and describe what they see, which no user recovers by reading code.

Conflict about what exists → the code wins and the document is corrected. Conflict about what ought to be → the document wins and the code is a finding.

Six sentence shapes make a document go stale fast:

| Stale shape | Write instead |
|---|---|
| Enumeration — a list that has to stay complete | The criterion, not the list |
| Status — progress, checkmarks, "not tested yet" | Nothing; zero status fields, no exceptions |
| State description — "the system records X in Y" | The constraint — "no X without Y" |
| Technical identifier — table, column, route, component, file | The concept; the glossary is the bridge. The index, the Proof profile, and `README.md`'s Run section name paths and commands by necessity |
| Snapshot number — "N rows at present" | A number only as the reason behind a rule's value |
| Change history | The state it produced; history is in git and the frozen records |

Environment variables by name, never by value.

## Timeless wording

**The living documents state what is true, in the present tense** — `README.md`, `product.md`, `rules.md`, `glossary.md`, `guide/`, `DESIGN.md`. No "now", "new", "currently", "no longer", "previously", "was changed", no dates: a sentence needing one describes a change, so write the state it produced. History is in git and in the frozen records.

## Same commit

**A commit that makes a living document false carries its correction** — the page whose behaviour changed carries its guide page, a new term its glossary row, a file the index lists, added or removed, its `docs/README.md` line. A correction left for later is never made.

## Frozen records

**`docs/PRD.md` once written, a `docs/changes/` file once done, and an accepted decision record are never edited.** The one exception: superseding a decision sets the old record's status to `superseded by NNNN`. They are history — never read as current truth, never injected. One turns out wrong → correct the living document, or supersede the decision.

## Who may write what

**The trigger is narrow.** A living document changes when a sentence in it becomes false, or when a rule, a term, or a prohibition must be remembered by later sessions. A new feature, screen, table, or column is not a trigger by itself. In doubt → do not write.

**Written freely**: a sentence that became false, corrected · Context and Roles in `product.md`, each on its own trigger · a glossary row · a guide page · a `whats-new.md` entry · a `docs/README.md` line.

**Rules and glossary rows are written before the implementation, never after** — a rule written by the session that just built it describes its code, and looks decided when nobody decided it. Test: *a business decision, or a mechanism I just built?* The latter → do not write it; a rule that surfaces mid-implementation undiscussed is a finding and a `build-flow` stop. The why is at most three sentences — a business or empirical reason, never how it works: reason · trade-off · the condition for revisiting. A glossary term never changes meaning; a changed meaning is a new term.

**Prohibitions — propose, then STOP.** Adding and removing both wait for the user, however obvious, even for a mistake made in this session. Present the sentence, its reason, and — when removing — what made it stop applying. A lifted prohibition is deleted. Propose only what a later session could undo out of ignorance and what `product.md`, `rules.md`, the decision records, or `DESIGN.md` do not already hold.

**Non-goals change only in `app-settle` rework.** A deleted non-goal is scope opening; the user's reason becomes a decision record.

**One decision record per decision the user takes**: each stack answer at bootstrap, each `logic-settle` answer and each `design-settle` stack answer — every deliberate "none" and every *keep* that had no record included — a library default changed on purpose (`logic-build` Section 6), and a technical choice the user takes in a build session whose reason the code cannot show. A business decision goes to `docs/rules.md` and a "never do this" to Prohibitions instead; a choice you made yourself gets no record — it is a default, reported at the close. A changed decision is a new record superseding the old.

**Restructuring stops first.** Adding or removing a section of a living document, moving content between documents, changing a table's shape: state what changes and why, then wait. Structure changed without deliberation leaves a thin document, and thin looks recorded.

## `DESIGN.md` — `design-settle` alone

The derivation runs **user → `DESIGN.md` → styling files**, never the reverse. `design-settle` writes it from the user's answers, or from measured values the user ratified one by one; no other session edits it. A session finding it absent or deviating stops and points the user at `design-settle`. Deviating code is a finding, never a new norm, however much of it exists. Its shape is `design-settle`'s.

## Shapes

Read `references/shapes.md` before writing a new file of the list, or a new section in one. `DESIGN.md`'s shape is `design-settle`'s; `docs/queue.md`'s is `build-flow`'s.

## The legacy map

| A skill names | A repo with a root `PRD.md` reads |
|---|---|
| `docs/product.md` — Context, Surface, Proof profile, problem, success, non-goals | `PRD.md` Section 1 |
| `docs/product.md` — Roles | Section 2 |
| `docs/rules.md` | Section 3 |
| `docs/glossary.md` | Section 4 |
| `DESIGN.md` | Section 5. The root `DESIGN.md` there is generated from it and is never read as the design system |
| `docs/product.md` — Prohibitions | Section 6 |
| `docs/decisions/` | Section 1 — one line per `app-settle` or `logic-settle` choice, or technical choice the user took, with its reason, rejected alternatives among the non-goals. `design-settle` records none there; its library is `CLAUDE.md`'s row |
| `docs/queue.md` | `QUEUE.md` at the root |
| `docs/README.md`, `docs/guide/`, `docs/whats-new.md`, `docs/changes/`, `docs/PRD.md` | Nothing — never written in a legacy repo |

Every rule above binds the mapped section. Read `references/legacy.md` before editing a legacy `PRD.md`.
