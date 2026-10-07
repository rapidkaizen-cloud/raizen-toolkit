# The audit — a subagent's brief, where UI exists

You audit the UI an app has today, for a session that will redesign it **without ever seeing it**. Read what the code uses, never what `DESIGN.md` says it should. Change nothing in the app and fix nothing on the way past: every hit is a finding. Documents are named by their `docs/` path; a repo with a root `PRD.md` reads each through `docs-format`'s legacy map. Run independent reads and commands in one turn.

## What you write

Three files under `.design-audit/` at the repo root:

- **`audit.md`** — for the user: the block below, the frame inventory, the component measurements, the contrast pairs, the `DESIGN.md` deviations, the screenshot paths.
- **`places.md`** — for a gate that redraws nothing, never read by a session that draws: every hit a repair of the UI could clear, one line per place — file and line · what is there · the block row or `DESIGN.md` rule it falls under.
- **`handover.md`** — the only thing the drawing session reads, holding in this order and nothing else: the app in three sentences from `docs/product.md` · the roles · the function inventory · the route list, each route with a few words on what it is for and nothing on what it holds · the data vocabulary a fixture must respect, with a handful of real rows from the data layer where it holds any · the data-layer files a fixture may take types from, by path, none carrying a look or importing from the components folder · the UI stack row, font packages left out · the counts that price the pass, as numbers.

**`handover.md` carries no colour, hex, font name, radius, spacing value, component measurement, shell description, part or section name per page, `DESIGN.md` prose, screenshot, or code excerpt** — nothing on how anything looks or where it sits.

**`handover.md` carries no person and no secret**: in a real row, replace every name, phone number, e-mail, address, identity or account number and free-text value with an invented one of the same length and format, and list no file that holds real rows — fixtures are copied from what it holds, and committed.

## What you report back

Only this, never the block and never a word on the look: the counts that price the pass (components affected, stray values, detector hits, and the `DESIGN.md` deviations where it is written) · the pages holding too little, by name · any logic-layer bleeding, by file · the `DESIGN.md` indictment count where it is written, and whether it carries an archetype table · whether the installed library, styling, icon pack, or an engine is itself indicted, and by what · whether the running app was walked, and why not where it was not · the path of `audit.md` · the screenshot paths.

## The block `audit.md` opens with

```
AUDIT
Tokens defined      : [how many colors · text steps · spacing values · radii]
Token health        : [how many never read · duplicate roles · library slots unmapped]
Stray raw values    : [how many hex · font sizes · spacings, across how many files]
Slop detectors      : [how many hits · how many rules, from `npx --no-install impeccable detect --json`
                       on the source tree — a clean scan prints `[]`, an absent detector an
                       error, and no output at all is a scan that did not run, written
                       `not run — no output` — the source tier only; the full set needs
                       the running app.
                       `n/a — native surface` where the Surface is not web technology]
Icons               : [families, named · how many sizes · how many weights]
Fonts loaded        : [from the styling files AND the HTML entry, or the root layout where
                       the framework writes none — a family named in CSS but never loaded
                       renders as its fallback, and only this row sees it]
Component values    : [how many items read on the walk · how many `from source` · how many
                       rendered differently from place to place]
Contrast pairs      : [how many read on the walk · how many `from source` · how many under
                       their floor]
UI stack            : [component library · styling · icon pack · engines — chart, table,
                       date, drag-and-drop — with versions, from the dependency file; a
                       copy-in library from its copied folder; an indicted part marked,
                       with its reason]
Repeated labels     : [longest · median · how many repeat per screen]
Supporting text     : [how many paragraphs · the longest in sentences]
Frame inventory     : [routes counted from the router, or from the routes folder of a
                       file-routed app · parts and states named per route, a route the
                       walk could not open by name alone — or, where it opened no route
                       at all, `routes only — the running app could not be walked`]
Deviates            : [list, per DESIGN.md rule broken — DESIGN.md written only]
Components affected : [file count that will be touched if tokens change]
```

Counts are occurrences in source; label lengths are in words, as `ui-build`'s copy caps count them.

## How each part is read

- **The walk** is every route opened in the running app — started by the Proof profile's Run line in `docs/product.md`, or by the repo's own dev command where it has none, and signed in with the account handed to you, which you write into no file. Create no account.
- **`UI stack`** is the canvas's import whitelist. An installed engine nothing uses is a finding.
- **A stack part is indicted** — the library, the styling, the icon pack, an engine — in three cases and no other: a floor (contrast, `impeccable`'s Refuse list, a detector rule) failed inside a package's own stylesheet or anatomy — never inside a copy-in library's files, which are the app's own · two packages in use for one job (two icon families, two chart engines, two styling systems) · an engine that paints where the styling files cannot reach (a `<canvas>` on the web). Every other failure in how the app uses a part is a finding.
- **`Token health`** reads the library's slot list from the installed package — for a copy-in library, from the tokens its copied files read — never from memory. Read `DESIGN.md` first: a legacy Section 5 of the adopted-whole shape (`docs-format`, `references/legacy.md`) reports `n/a — stock` and counts no unmapped slots.
- **`Slop detectors`** runs only on a web-technology Surface, source tier only; a native one reports `n/a — native surface`. `impeccable` absent → `n/a — not installed`.
- **Logic-layer bleeding** — handwritten fetching in UI files, hand-parsed dates, unvalidated inputs.
- **The function inventory** — every function the app carries, one line each: what can be done, never where or how it looks.
- **The frame inventory** — per route, the parts and states that render there, names only; **routes from the router file, or the routes folder of a file-routed app, never from memory**; states real data cannot produce listed anyway (loading, empty, failed, every role branch). It goes in `audit.md` and **never in `handover.md`**.
- **The component measurements** — one line per item of the component-token table, as the `## Components` row of `design-md.md` beside this file lists them, for each whose component the app has: what the walk rendered — on the web the computed style, the focus ring read on a focused control — and the route it was read on. An item rendered differently from place to place lists each value with its files. An item the walk cannot read — the app not run, a dialog never opened, a native Surface — is read from the shared components' source and the library's theme, marked `from source`. They go in `audit.md` and **never in `handover.md`**.
- **The contrast pairs** — one line per distinct pair the walk rendered, in each theme mode the app holds: the foreground colour, the background it sat on, text or non-text, the WCAG ratio calculated from the two computed values, its floor — 4.5:1 for text, 3:1 for non-text — and one route it was read on. A pair the walk cannot read is taken from the styling files and the shared components' source, marked `from source`. They go in `audit.md` and **never in `handover.md`**.
- **Screenshot every route at desktop width**, per the Proof profile — 1440px where it names none — saved under `.design-audit/`.
- **App could not be run, or no credentials → say so in the report**; a route the walk could not open is in the frame inventory by name alone.
- **A page holding too little is not a finding** — name it in the report.

**Where `DESIGN.md` is written:**

- A deviation is a finding, never a reason to change `DESIGN.md` — a component measurement off its value in the component-token table included.
- A departure its Do's and Don'ts ratifies as an exception is no deviation.
- **The indictment** is the count of `DESIGN.md` rules that themselves fail a floor — contrast, `impeccable`'s Refuse list (located through its own `SKILL.md` index), a detector rule.
- Two of its roles at the same value are a finding against it.
- No archetype table is a finding.
