# The audit — a subagent's brief, where UI exists

You audit the UI an app has today, for a session that will redesign it **without ever seeing it**. Read what the code uses, never what `DESIGN.md` says it should. Change nothing in the app and fix nothing on the way past: every hit is a finding. Documents are named by their `docs/` path; a repo with a root `PRD.md` reads each through `docs-format`'s legacy map. Run independent reads and commands in one turn.

## What you write

Two files under `.design-audit/` at the repo root:

- **`audit.md`** — for the user: the block below, the frame inventory, the component measurements, the `DESIGN.md` deviations, the screenshot paths.
- **`handover.md`** — the only thing the drawing session reads, holding in this order and nothing else: the app in three sentences from `docs/product.md` · the roles · the function inventory · the route list, each route with a few words on what it is for and nothing on what it holds · the data vocabulary a fixture must respect, with a handful of real rows from the data layer where it holds any · the data-layer files a fixture may take types from, by path, none carrying a look or importing from the components folder · the UI stack row, font packages left out · the counts that price the pass, as numbers.

**`handover.md` carries no colour, hex, font name, radius, spacing value, component measurement, shell description, part or section name per page, `DESIGN.md` prose, screenshot, or code excerpt** — nothing on how anything looks or where it sits.

## What you report back

Only this, never the block and never a word on the look: the counts that price the pass (components affected, stray values, detector hits, and the `DESIGN.md` deviations where it is written) · the pages holding too little, by name · any logic-layer bleeding, by file · the `DESIGN.md` indictment count where it is written, and whether it carries an archetype table · whether the installed library, styling, icon pack, or an engine is itself indicted, and by what · the path of `audit.md` · the screenshot paths.

## The block `audit.md` opens with

```
AUDIT
Tokens defined      : [how many colors · text steps · spacing values · radii]
Token health        : [how many never read · duplicate roles · library slots unmapped]
Stray raw values    : [how many hex · font sizes · spacings, across how many files]
Slop detectors      : [how many hits · how many rules, from `npx --no-install impeccable detect`
                       on the source tree, which reports an absent detector as absent — the
                       source tier only; the full set needs the running app.
                       `n/a — native surface` where the Surface is not web technology]
Icons               : [families, named · how many sizes · how many weights]
Fonts loaded        : [from the styling files AND the HTML entry — a family named in CSS
                       but never loaded renders as its fallback, and only this row sees it]
Component values    : [how many items read on the walk · how many `from source` · how many
                       rendered differently from place to place]
UI stack            : [component library · icon pack · engines — chart, table, date,
                       drag-and-drop — with versions, from the dependency file]
Repeated labels     : [longest · median · how many repeat per screen]
Supporting text     : [how many paragraphs · the longest in sentences]
Frame inventory     : [routes counted from the router · parts and states named per route,
                       or `routes only — the running app could not be walked`]
Deviates            : [list, per DESIGN.md rule broken — DESIGN.md written only]
Components affected : [file count that will be touched if tokens change]
```

Counts are occurrences in source; label lengths are in words, as `ui-build`'s copy caps count them.

## How each part is read

- **`UI stack`** is the canvas's import whitelist. An installed engine nothing uses is a finding.
- **`Token health`** reads the library's slot list from the installed package, never from memory. Read `DESIGN.md` first: a legacy Section 5 of the adopted-whole shape (`docs-format`, `references/legacy.md`) reports `n/a — stock` and counts no unmapped slots.
- **`Slop detectors`** runs only on a web-technology Surface, source tier only; a native one reports `n/a — native surface`. `impeccable` absent → `n/a — not installed`.
- **Logic-layer bleeding** — handwritten fetching in UI files, hand-parsed dates, unvalidated inputs.
- **The function inventory** — every function the app carries, one line each: what can be done, never where or how it looks.
- **The frame inventory** — per route, the parts and states that render there, names only; **routes from the router file, never from memory**; states real data cannot produce listed anyway (loading, empty, failed, every role branch). It goes in `audit.md` and **never in `handover.md`**.
- **The component measurements** — one line per item of the component-token table, as the `## Components` row of `design-md.md` beside this file lists them, for each whose component the app has: what the walk rendered — on the web the computed style, the focus ring read on a focused control — and the route it was read on. An item rendered differently from place to place lists each value with its files. An item the walk cannot read — the app not run, a dialog never opened, a native Surface — is read from the shared components' source and the library's theme, marked `from source`. They go in `audit.md` and **never in `handover.md`**.
- **Screenshot every route at desktop width**, per the Proof profile — 1440px where it names none — saved under `.design-audit/`.
- **App could not be run, or no credentials → say so in the report**; the frame inventory is routes only.
- **A page holding too little is not a finding** — name it in the report.

**Where `DESIGN.md` is written:**

- A deviation is a finding, never a reason to change `DESIGN.md` — a component measurement off its value in the component-token table included.
- **The indictment** is the count of `DESIGN.md` rules that themselves fail a floor — contrast, `impeccable`'s Refuse list (located through its own `SKILL.md` index), a detector rule.
- Two of its roles at the same value are a finding against it.
- No archetype table is a finding.
