# engine-rubric — rendering engines beyond the component pack

An **engine** is a library owning a rendering job the component pack (`library-rubric.md`) does not: charts, heavy tables, drag-and-drop, virtualized lists. **Name no candidates in this file** — assemble them live.

## No standing questions — only triggers

Ask engine dialogs only when triggered; an app that trips none never hears about engines.

| Trigger | When the dialog is asked |
|---|---|
| **The user or the documents name the need** — "a trend chart", an import implying a dropzone | Among the stack dialogs — locked, installed at the install gate |
| **The product draft needs it** — the canvas's full-product draft (`canvas.md`, The brief — the expansion duty) implies a job no installed engine covers | Among the stack dialogs — locked, installed at the install gate |
| **It emerges mid-drawing** | Draw the frame with the no-engine rendering, tagged as a proposal; the judgement settles it, and an approved adoption installs the engine and redraws that frame next round |
| **The audit indicts an installed engine** (`design-settle` only) | Among the stack dialogs, priced like the library dialog — *keep* first and recommended unless the indictment stands |

An **installed engine is already decided**; no dialog reopens it without an audit indictment. Swapping or dropping one is always an explicit dialog, never a side effect of approving pixels.

## One dialog per detected category

When a trigger fired before drawing, open one engine dialog per detected category, its trigger in the question (`Chart — the home page draws a revenue trend`), the no-engine option among its options (criterion 3). **Offer detected triggers only, never the full category list.** Choosing no engine keeps the current state, recorded as a decision; a category named through "Other" becomes a named-need trigger with its own dialog.

## The verification duty — candidates assembled live

1. **The model's own knowledge proposes** the engines a working frontend developer would name for this category today.
2. **A verification pass checks every candidate before it is offered**: maintained, broadly adopted, no fresh supply-chain event, bundle weight, **and how it renders — DOM/SVG or canvas**. What it brings and leaves out is the option's one-sentence consequence. One pass covers all candidates.

**Never show an option without verified backing**; every option states what verification found. Zero survive → say so and offer the no-engine rendering; never pad the list.

## Criteria, in order

1. **Styleable by production tokens — hard criterion.** The engine takes colours, type and spacing from the declared token source, verifiably at runtime: on the web, DOM or SVG that CSS variables and classes reach; elsewhere, the Proof profile's **Theme** line. An engine painting an opaque surface (`<canvas>` on the web) escapes the promotion pass's runtime check — offer it only where its capability is the point (very large datasets, maps), as a named exception the user approves knowing that cost.
2. **The component pack goes first.** Where the pack ships the component (table, date picker), it is the default; fire the engine dialog only when the pack's component measurably cannot do the job (nested headers, virtualization, thousands of rows), naming the failing capability. "More powerful" is not a trigger.
3. **No engine is always offered** — styled divs for a decorative-scale chart, consequence named (no axes, interactivity, or legend for free). Choosing it is explicit; hand-rolling *silently* where an installed engine owns the job is a departure to tag (`canvas.md`).
4. **Weight and upkeep** — bundle cost and maintenance status, verified live.

## Categories and trip conditions

Categories say what job fires a dialog — never candidate lists.

**Core categories:** **chart** · **table engine** · **date picker** · **drag-and-drop**. Table-engine and date-picker dialogs fire only past criterion 2.

**Conditional categories** — only when the brief carries the job:

| Category | Trips when |
|---|---|
| Virtualization | Lists or tables in the thousands of rows — usually rides the table decision |
| Rich text editor | The app has notes, comments, or documents |
| File upload / dropzone | The app imports files — the drop area only; parsing the file is `logic-build`'s, ordered at the gate |
| Calendar / scheduler | Schedules, shifts, bookings |
| PDF viewer / generation | Invoices, payslips, printable documents |
| Barcode / QR | Scanning receipts, labels, inventory |
| Editable grid (spreadsheet-edit, not display) | Bulk cell-level editing |
| Diagram / flow | Workflow or pipeline builders |
| Gantt / timeline | Production or project scheduling |
| Code editor | Internal dev tooling |

**Catch-all.** A UI job no category names gets the same treatment: verified candidates, the four criteria, no-engine where honest, one dialog. Absence from this list is never a reason to skip the dialog.
