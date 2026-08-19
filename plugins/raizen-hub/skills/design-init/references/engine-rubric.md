# engine-rubric — rendering engines beyond the component pack

An **engine** is a library that owns a rendering job the component pack does not: charts, heavy tables, drag-and-drop, virtualized lists. Decision 7 picks the component pack (`library-rubric.md`); this file governs everything the pack leaves uncovered.

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

When at least one trigger has fired before drawing, the detected jobs are put to the user as **one multiSelect AskUserQuestion first**, before any per-engine dialog: every option is a detected category with its trigger named in the description (`Chart — the home page draws a revenue trend`), all pre-selected, keeping all as the recommendation. **The options are the detected triggers only, never the full catalog below** — offering categories nothing tripped is a speculative install menu, the exact noise the trigger model exists to prevent. What the user unchecks is settled without a dialog — the current state stays, recorded as a decision line; what the user adds through "Other" becomes a named-need trigger like any other. Only the checked categories open their per-engine dialogs, in the next call — a real dependency, so the two ride sequential calls under `interview.md`'s batching rules. The mid-drawing trigger is unaffected: it still goes through the tag and the judgement.

## Criteria, in order

1. **Styleable by production tokens — hard criterion.** The engine renders DOM or SVG that CSS variables and classes reach. An engine that paints to `<canvas>` (ECharts, Chart.js) takes tokens only as JS values, and the computed-style verification of the promotion pass cannot see inside it — offer it only where its capability is the point (very large datasets, maps), as a named exception the user approves knowing that cost.
2. **The component pack goes first.** Where the pack ships the component (HeroUI Table, HeroUI DatePicker), the pack is the default and the engine dialog fires only when the pack's component measurably cannot do the job — nested headers, virtualization, thousands of rows. Name the failing capability in the dialog; "the engine is more powerful" is not a trigger.
3. **No engine is a real option, always offered.** A simple bar rendered as styled divs is a legitimate answer for decorative-scale charts — with its consequence named (no axes, no interactivity, no legend for free). Choosing it is an explicit decision like any other; hand-rolling *silently* where an installed engine owns the job stays a departure to tag (`canvas.md`).
4. **Weight and upkeep.** Bundle cost and maintenance status, verified live by the research pass — never from memory.

## Candidate pools

Starting pools, not verdicts — the research pass verifies status and versions live before any dialog is shown, and options carry their source labels like every interview option.

**Core categories** — most internal apps trip at least one:

| Category | Pool | Notes |
|---|---|---|
| Chart | Recharts · visx · ECharts · no engine | Recharts: SVG, ecosystem default, token-friendly. visx: primitives, small, high build cost. ECharts: canvas-rendered — hard-criterion exception only |
| Table engine | component pack's table · TanStack Table · no engine | TanStack: headless, all features free, UI fully owned by the tokens — the fidelity pick when the pack's table hits its ceiling |
| Date picker | component pack's picker · React Aria composition | Usually owned by the pack; dialog fires only when the pack ships none or it fails a named need |
| Drag-and-drop | dnd-kit · pragmatic-drag-and-drop | dnd-kit: community standard, small, accessible. Pragmatic: Jira/Trello scale |

**Conditional categories** — the dialog exists only when the brief carries the job:

| Category | Pool | Trips when |
|---|---|---|
| Virtualization | TanStack Virtual · react-window | Lists or tables in the thousands of rows — usually rides the table decision |
| Rich text editor | Tiptap · Lexical · Plate | The app has notes, comments, or documents |
| File upload / dropzone | react-dropzone · hand-rolled on the pack's primitives | The app imports files |
| Calendar / scheduler | FullCalendar · react-big-calendar | Schedules, shifts, bookings |

**Second-tier categories** — less frequent, one-line head starts; same trigger rules:

| Category | Pool | Trips when |
|---|---|---|
| PDF viewer / generation | react-pdf · pdf.js | Invoices, payslips, printable documents |
| Barcode / QR | zxing · html5-qrcode | Scanning receipts, labels, inventory |
| Editable grid (spreadsheet-edit, not display) | Glide Data Grid · Handsontable | Bulk cell-level editing |
| Diagram / flow | React Flow (xyflow) | Workflow or pipeline builders |
| Gantt / timeline | vis-timeline | Production or project scheduling |
| Code editor | CodeMirror · Monaco | Internal dev tooling |

**Catch-all.** A UI job the brief carries that no pool above covers — maps, a command palette, anything newer than this file — gets the same treatment assembled live: research pass for candidates, the four criteria above, no-engine offered where it is honest, one dialog. The pools are a head start, never a closed list — a category's absence here changes the amount of research, never the rules.
