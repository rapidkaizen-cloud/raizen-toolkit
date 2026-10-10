# The audit, from the source — the first of two subagents' briefs, where UI exists

You audit the UI an app has today, for a session that will redesign it **without ever seeing it**. Read what the code uses, never what `DESIGN.md` says it should. Change nothing in the app and fix nothing on the way past: every hit is a finding. Documents are named by their `docs/` path; a repo with a root `PRD.md` reads each through `docs-format`'s legacy map. Run independent reads and commands in one turn.

**A second subagent walks the running app after you** (`audit-walk.md`): open no browser and start no server.

## What bounds the work

You are handed a scope — the whole app, or the page groups this run redraws — and the app's page groups with their page counts. Count neither again.

- **Count over the whole app with the script, once**: `python3 <plugin folder>/scripts/audit_count.py <repo root> --scope <the scope's paths> --out <repo root>/.design-audit`, the plugin folder three levels above this file. It writes `places.md` and prints the stray values, the files they sit in, the imports, the icon families and the packages nothing imports: copy its rows into the block as printed, and count nothing it printed a second time. `--src` narrows what it reads, and `--styles` names the styling files where it guessed them wrong.
- **Where it prints `NOT COVERED`, count by commands of your own** that print a count or write the line into the file. Never print a page file to count in it.
- **Read page files in the scope only** — for the function inventory, the frame inventory and the two copy rows. A page outside it is a route name.
- **Pick the routes the walk opens**: one of each kind of page the routes show — a list, a form, a detail, a dashboard, any other — inside the scope, and one of each kind outside it.

## What you write

Three files under `.design-audit/` at the repo root:

- **`audit.md`** — for the user: the block below, the frame inventory, the `DESIGN.md` deviations, and last a section headed `## Routes for the walk` — each route picked, its kind, inside the scope or outside it. The walk adds the component measurements, the contrast pairs and the screenshot paths after it.
- **`places.md`** — for a gate that redraws nothing, never read by a session that draws: every hit a repair of the UI could clear, one line per place — file and line · what is there · the block row or `DESIGN.md` rule it falls under. The script writes it; append in the same shape the places only you found — a `DESIGN.md` deviation, a Refuse-list hit.
- **`handover.md`** — the only thing the drawing session reads, holding in this order and nothing else: the app in three sentences from `docs/product.md` · the roles · the function inventory · the route list of the scope, each route with a few words on what it is for and nothing on what it holds · the page groups outside the scope, by name and page count, because the chrome keeps their entries · the data vocabulary a fixture must respect, with a handful of real rows from the data layer where it holds any · the data-layer files a fixture may take types from, by path, none carrying a look or importing from the components folder · the UI stack row, font packages left out · the counts that price the pass, as numbers.

**`handover.md` carries no colour, hex, font name, radius, spacing value, component measurement, shell description, part or section name per page, `DESIGN.md` prose, screenshot, or code excerpt** — nothing on how anything looks or where it sits.

**`handover.md` carries no person and no secret**: in a real row, replace every name, phone number, e-mail, address, identity or account number and free-text value with an invented one of the same length and format, and list no file that holds real rows — fixtures are copied from what it holds, and committed.

## What you report back

Only this, never the block and never a word on the look: the counts that price the pass (components affected, stray values, detector hits, and the `DESIGN.md` deviations where it is written) · the pages holding too little, by name · any logic-layer bleeding, by file · the `DESIGN.md` indictment count where it is written, and whether it carries an archetype table · whether the installed library, styling, icon pack, or an engine is itself indicted, and by what · the routes picked for the walk · the path of `audit.md`.

## The block `audit.md` opens with

Write the three rows marked `pending — the walk` exactly so: the walk replaces them.

```
AUDIT
Scope               : [the whole app / the page groups handed to you · how many pages of how many]
Walked              : pending — the walk
Tokens defined      : [how many colors · text steps · spacing values · radii]
Token health        : [how many never read · duplicate roles · library slots unmapped]
Stray raw values    : [as the script prints them — hex · colour functions · font sizes · spacings ·
                       numbered ramp classes, each with its files, the scope's beside the
                       whole app's]
Slop detectors      : [how many hits · how many rules, from `npx --no-install impeccable detect --json`
                       on the source tree — a clean scan prints `[]`, an absent detector an
                       error, and no output at all is a scan that did not run, written
                       `not run — no output` — the source tier only; the full set needs
                       the running app.
                       `n/a — native surface` where the Surface is not web technology]
Icons               : [families, named, as the script prints them · how many sizes · how many
                       weights]
Fonts loaded        : [from the styling files AND the HTML entry, or the root layout where
                       the framework writes none — a family named in CSS but never loaded
                       renders as its fallback, and only this row sees it]
Component values    : pending — the walk
Contrast pairs      : pending — the walk
UI stack            : [component library · styling · icon pack · engines — chart, table,
                       date, drag-and-drop — with versions, from the dependency file; a
                       copy-in library from its copied folder; an indicted part marked,
                       with its reason]
Repeated labels     : [longest · median · how many repeat per screen — the scope's pages]
Supporting text     : [how many paragraphs · the longest in sentences — the scope's pages]
Frame inventory     : [routes counted from the router, or from the routes folder of a
                       file-routed app — the scope's, and the whole app's · parts and
                       states named per route of the scope, read from its page file]
Deviates            : [list, per DESIGN.md rule broken — DESIGN.md written only]
Components affected : [as the script prints it — the files holding a value the tokens do not
                       reach]
```

Counts are occurrences in source; label lengths are in words, as `ui-build`'s copy caps count them.

## How each part is read

- **`UI stack`** is the canvas's import whitelist. An installed engine nothing uses is a finding.
- **A stack part is indicted** — the library, the styling, the icon pack, an engine — in three cases and no other: a floor (contrast, `impeccable`'s Refuse list, a detector rule) failed inside a package's own stylesheet or anatomy — never inside a copy-in library's files, which are the app's own · two packages in use for one job (two icon families, two chart engines, two styling systems) · an engine that paints where the styling files cannot reach (a `<canvas>` on the web). Every other failure in how the app uses a part is a finding.
- **`Token health`** reads the library's slot list from the installed package — for a copy-in library, from the tokens its copied files read — never from memory. Read `DESIGN.md` first: a legacy Section 5 of the adopted-whole shape (`docs-format`, `references/legacy.md`) reports `n/a — stock` and counts no unmapped slots.
- **`Slop detectors`** runs only on a web-technology Surface, source tier only; a native one reports `n/a — native surface`. `impeccable` absent → `n/a — not installed`. Run its command once: an error is that answer, and no other copy of the detector is looked for.
- **Logic-layer bleeding** — handwritten fetching in UI files, hand-parsed dates, unvalidated inputs.
- **The function inventory** — every function the pages in scope and the chrome they share carry, one line each: what can be done, never where or how it looks.
- **The frame inventory** — per route of the scope, the parts and states its page file renders, names only; **routes from the router file, or the routes folder of a file-routed app, never from memory**; states real data cannot produce listed anyway (loading, empty, failed, every role branch). It goes in `audit.md` and **never in `handover.md`**.
- **A page holding too little is not a finding** — name it in the report.

**Where `DESIGN.md` is written:**

- A deviation is a finding, never a reason to change `DESIGN.md`.
- A departure its Do's and Don'ts ratifies as an exception is no deviation.
- **The indictment** is the count of `DESIGN.md` rules that themselves fail a floor — contrast, `impeccable`'s Refuse list (located through its own `SKILL.md` index), a detector rule.
- Two of its roles at the same value are a finding against it.
- No archetype table is a finding.
