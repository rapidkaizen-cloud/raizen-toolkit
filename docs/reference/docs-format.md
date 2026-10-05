# docs-format

A session keeps an app repo's documents to a closed list, writes only what reading the code cannot give back, and corrects a document in the same commit that makes it false.

| | |
|---|---|
| Kind | Rule skill — a session loads it by its description; there is no command |
| Loads when | Before writing, editing, or proposing a change to anything under `docs/`, `DESIGN.md`, the root `README.md`, or a legacy root `PRD.md`, and when deciding whether something should be recorded at all |
| Governs | Which documents exist, what each holds, who writes it and when, and how it is worded |
| Reads | `docs/README.md`, `docs/product.md`, `docs/queue.md`; in a legacy repo, the `PRD.md` sections its legacy map names |
| Source | `skills/docs-format/SKILL.md`, with `references/shapes.md` and `references/legacy.md` |

## What a session is held to

**Which form** (Which form, `references/legacy.md`). A repo with no root `PRD.md` uses the `docs/` form, which `app-settle` writes. A repo with a root `PRD.md` stays in the legacy form until `app-settle`'s migrate mode moves it. No other session moves it, and none creates a `docs/` file beside it. In the legacy form each `docs/` path is read from a `PRD.md` section: `product.md` from Sections 1, 2 and 6, `rules.md` from 3, `glossary.md` from 4, the design system from 5, and the queue from `QUEUE.md` at the root. `docs/README.md`, the guide pages, `docs/whats-new.md`, `docs/changes/` and `docs/PRD.md` are never written there.

**A closed list** (The closed list). No other document is written — no `SCHEMA.md`, `DECISIONS.md`, API reference, audit report, plan file or second index. One found is a finding. Every file of the list is written for the developer who continues the app and the agent that builds it, in your language with technical terms left as they are; `docs/guide/` alone is written for the app's users.

| File | Holds | Written by |
|---|---|---|
| `docs/README.md` | The index, one line per file | `app-settle` seeds it; the commit adding or removing a file updates it |
| `docs/product.md` | Context, problem, success, non-goals, roles, prohibitions | `app-settle`; any session when a sentence in it becomes false |
| `docs/rules.md` | Business rules, each with its why | `app-settle`; a build session, before the implementation |
| `docs/glossary.md` | Domain terms and what they are misread as | Any session, before the implementation that uses the term |
| `docs/queue.md` | What is not built yet | `build-flow` |
| `docs/decisions/` | One record per decision you took | `app-settle`, `logic-settle`, `design-settle`, or a build session |
| `docs/architecture.md` | The map: the parts that run, what each talks to, where each kind of code lives, how a user is identified | `app-settle`; any session, in the commit that makes a sentence in it false |
| `docs/runbook.md` | Deploy, roll back, backup and restore, what to check when it is down | `app-settle`; the commit changing how the app is deployed or restored |
| `docs/changelog.md` | What changed in how the app behaves, newest first | The session whose commit changes how the app behaves — mandatory |
| `docs/guide/` | How each role finishes each task, for the app's users — kept only where the Help row of `docs/product.md` is not `none` | The build session whose commit changes what a page describes |
| `docs/changes/` | One record per big change | `build-flow` |
| `docs/PRD.md` | The app as first approved | `app-settle`; frozen when written |
| `DESIGN.md` | The design system | `design-settle` alone |
| `README.md` | What the app is and how to run it | `app-settle`; the commit changing how the app runs |

`CLAUDE.md` and `AGENTS.md` record nothing about the app; `app-settle` owns their shape.

**Only what a live check cannot recover** (What belongs in any of them). Every sentence passes one test: deleted, could reading the repo or introspecting the database bring it back? If yes, it is not written. Three exceptions: the Surface row with the Proof profile; the guide, which describes what users see; and `docs/architecture.md` with `docs/runbook.md`, which say how the parts connect and how the app is operated — never what a table, a column or a route is. Where document and code disagree about what exists, the code wins; about what ought to be, the document wins and the code is a finding.

**Six shapes that go stale are not written**: enumerations (the criterion is written instead), status, state descriptions (the constraint instead), technical identifiers (the concept instead, except the index, the Proof profile, the `README.md` Run section, `architecture.md` and `runbook.md`, which name paths and commands by necessity), snapshot numbers, and change history. Environment variables appear by name, never by value.

**Present tense, no dates** (Timeless wording) in `README.md`, `docs/product.md`, `docs/rules.md`, `docs/glossary.md`, `docs/architecture.md`, `docs/runbook.md`, `docs/guide/` and `DESIGN.md`. A sentence that needs a word about change is rewritten as the state it produced.

**The same commit** (Same commit). A commit that makes a living document false carries its correction: a moved part its `architecture.md` sentence, a changed deploy step its `runbook.md` step, a term its glossary row, a changed page its guide page where they are kept, a listed file added or removed its `docs/README.md` line. A commit that changes how the app behaves carries its `docs/changelog.md` entry. A commit that changes no document is reported `Docs: none` with its reason, so no commit goes unreported.

**Frozen records** (Frozen records). `docs/PRD.md` once written, a `docs/changes/` file once done and an accepted decision record are never edited. Superseding a decision sets the old record's status to `superseded by NNNN`.

**Rules before code** (Who may write what). A rule or glossary row is written before the implementation, never after, so a rule is a decision and not a description of code. A rule's why is three sentences at most. Adding a feature, screen, table or column is not a reason to write a document by itself; in doubt, nothing is written.

**One decision record per decision you take**: each stack answer, each `logic-settle` answer, each `design-settle` stack answer, a library default changed on purpose, a technical choice you took. A choice the session made itself gets no record. It is a default, reported at the close.

**`DESIGN.md` is `design-settle`'s alone** (`DESIGN.md` section). The direction runs from you to `DESIGN.md` to the styling files, never the reverse. A session that finds it absent or deviating stops and points you at `design-settle`; deviating code is a finding, never a norm.

## What you will see

- **Documents with fixed headings**, written verbatim from `references/shapes.md`, with the text under them in your language and kebab-case English file names.
- **A Proof profile** under Context in `docs/product.md`, with seven labels: `Run`, `Visual`, `Bounds`, `Cases`, `Roles`, `A11y`, `Theme`. A line not executed is written `[needs verification]`, except the web defaults.
- **`Why:` lines** under each rule. A reason nobody knows is written `Why: unknown — it has always been this way`.
- **Decision records** at `docs/decisions/NNNN-<slug>.md`, with `Context and Problem Statement`, `Considered Options`, `Decision Outcome` and `Consequences`.
- **A proposal** for each prohibition: the sentence, its reason, and when removing, what made it stop applying.
- **A notice** in a legacy repo whose `PRD.md` passes about 400 lines, because past that it carries status, not intent.

## Where it stops

- **Prohibitions.** Adding and removing both wait for you, however obvious.
- **Restructuring.** Adding or removing a section, moving content between documents, or changing a table's shape: the session states what changes and why, then waits.
- **Non-goals.** They change only in an `app-settle` rework; a deleted one turns your reason into a decision record.
- **A rule that surfaces undiscussed** during implementation is a finding and a `build-flow` stop. You decide the rule.
- **`DESIGN.md` absent or deviating.** The session stops and points you at `design-settle`.

## What it does not cover

- **The shape of `DESIGN.md`** belongs to `design-settle`, and of `docs/queue.md` to `build-flow`.
- **The legacy `PRD.md` sections** belong to `app-settle`. In a legacy repo the root `DESIGN.md` is generated and never read as the design system; a hand edit is a finding.
- **Anything a reading of the code or database gives back.** A document answering it is a finding.

## Related

[Documents](../concepts/documents.md) · [build-flow](build-flow.md) · [app-settle](app-settle.md) · [design-settle](design-settle.md) · [logic-settle](logic-settle.md) · [document-reminder](document-reminder.md)
