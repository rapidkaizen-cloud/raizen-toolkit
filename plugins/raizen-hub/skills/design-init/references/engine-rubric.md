# engine-rubric — rendering engines beyond the component pack

An **engine** is a library that owns a rendering job the component pack does not: charts, heavy tables, drag-and-drop, virtualized lists. Decision 7 picks the component pack (`library-rubric.md`); this file governs everything the pack leaves uncovered.

**This file names no candidates.** It holds the trigger model, the criteria, and the category list; the candidates for every category are assembled live, per the research duty below. A pool written here would only go stale and then anchor the dialogs to its staleness.

## No standing questions — only triggers

Engine dialogs have no slot in the interview. They fire only when triggered, and an app that never trips a trigger never hears about engines:

| Trigger | When the dialog is asked |
|---|---|
| **The user or the PRD names the need** — "a trend chart", an import feature implying a dropzone, a schedule board | Through the overview multiselect below, riding the batch that carries decision 7 — stack decisions read side by side; the chosen engine is installed before the canvas is drawn. In Fast there is no interview, so it rides the research pass that runs before drawing |
| **The product draft needs it** — the canvas's full-product draft (`canvas.md`, assumptions block) implies a job no installed engine covers | Alongside the install approval, before drawing |
| **It emerges mid-drawing** | The frame is drawn with the no-engine rendering and tagged as a proposal; the judgement settles it — an approved adoption installs the engine and redraws that frame in the next round |
| **The audit indicts an installed engine** (`design-rework` only) | In the interview, priced like decision 7 — *keep* first, and keep stays the recommendation unless the indictment stands |

An engine **already installed is already decided**: it is part of the declared stack, the canvas draws with it, and no dialog re-opens it without an audit indictment. Swapping or dropping one is always an explicit dialog, never a side effect of approving pixels.

## The overview multiselect — one gate before the dialogs

When at least one trigger has fired before drawing, the detected jobs are put to the user as **one multiSelect AskUserQuestion first**, before any per-engine dialog: every option is a detected category with its trigger named in the description (`Chart — the home page draws a revenue trend`), all pre-selected, keeping all as the recommendation. **The options are the detected triggers only, never the full category list below** — offering categories nothing tripped is a speculative install menu, the exact noise the trigger model exists to prevent. What the user unchecks is settled without a dialog — the current state stays, recorded as a decision line; what the user adds through "Other" becomes a named-need trigger like any other. Only the checked categories open their per-engine dialogs, in the next call — a real dependency, so the two ride sequential calls under `interview.md`'s batching rules. The mid-drawing trigger is unaffected: it still goes through the tag and the judgement.

## The research duty — candidates assembled live

Candidates for a tripped category come from two layers, and both are mandatory:

1. **The model's own knowledge proposes** — the engines a working frontend developer would name for this category today.
2. **The research pass verifies every candidate before it may be offered.** Per candidate: maintained, broadly adopted, no fresh supply-chain event, bundle weight, **and how it renders — DOM/SVG or canvas** — because criterion 1 below turns on it. What a candidate brings and what it leaves out becomes the option's one-sentence consequence. The pass that `interview.md` already mandates covers this; what is mandatory is coverage per option, never one search per option.

**An option without researched backing is not shown**, and every option carries its source label like every interview option. Zero candidates surviving verification → say so plainly and offer the no-engine rendering; never pad the list.

## Criteria, in order

1. **Styleable by production tokens — hard criterion.** The engine renders DOM or SVG that CSS variables and classes reach. An engine that paints to `<canvas>` takes tokens only as JS values, and the computed-style verification of the promotion pass cannot see inside it — offer it only where its capability is the point (very large datasets, maps), as a named exception the user approves knowing that cost.
2. **The component pack goes first.** Where the pack ships the component (its table, its date picker), the pack is the default and the engine dialog fires only when the pack's component measurably cannot do the job — nested headers, virtualization, thousands of rows. Name the failing capability in the dialog; "the engine is more powerful" is not a trigger.
3. **No engine is a real option, always offered.** A simple bar rendered as styled divs is a legitimate answer for decorative-scale charts — with its consequence named (no axes, no interactivity, no legend for free). Choosing it is an explicit decision like any other; hand-rolling *silently* where an installed engine owns the job stays a departure to tag (`canvas.md`).
4. **Weight and upkeep.** Bundle cost and maintenance status, verified live by the research pass — never from memory alone.

## Categories and trip conditions

The categories are trigger knowledge — what kind of job fires a dialog — never candidate lists.

**Core categories** — most internal apps trip at least one: **chart** · **table engine** · **date picker** · **drag-and-drop**. The table-engine and date-picker dialogs fire only past criterion 2 — the pack's own component must have measurably failed a named need first.

**Conditional categories** — the dialog exists only when the brief carries the job:

| Category | Trips when |
|---|---|
| Virtualization | Lists or tables in the thousands of rows — usually rides the table decision |
| Rich text editor | The app has notes, comments, or documents |
| File upload / dropzone | The app imports files |
| Calendar / scheduler | Schedules, shifts, bookings |
| PDF viewer / generation | Invoices, payslips, printable documents |
| Barcode / QR | Scanning receipts, labels, inventory |
| Editable grid (spreadsheet-edit, not display) | Bulk cell-level editing |
| Diagram / flow | Workflow or pipeline builders |
| Gantt / timeline | Production or project scheduling |
| Code editor | Internal dev tooling |

**Catch-all.** A UI job the brief carries that no category above names gets the same treatment: research pass for candidates, the four criteria, no-engine offered where it is honest, one dialog. The category list changes how fast a trigger is recognized, never the rules — a job's absence from it is not a reason to skip the dialog.
