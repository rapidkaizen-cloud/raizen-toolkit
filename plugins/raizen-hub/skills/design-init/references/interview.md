# Frontend interview — 15 decisions

**The options are not written in this file, and no single source owns them.** They are assembled from three layers, every option labelled with where it came from:

1. **The `ui-ux-pro-max` database** — the floor, always queried. Each decision below names its query and column.
2. **The model's own reading of the domain** — what this kind of app conventionally carries, labelled `assembled`.
3. **Web research — run once, and mandatory.** Before the first question, run a WebSearch pass built from the corrected Step 0 reading: the kind of app, its domain, its closest well-known products. Fold what it returns into the option pool — real reference apps, current library candidates, domain conventions — labelled `research`. One pass feeds the whole interview, never one search per question; a pass that returns nothing useful is said plainly, not padded.

**Answers are the user's preferences, not gates.** They set the canvas's baseline; the canvas may depart from any of them with a drawn, tagged, reasoned departure that the user settles at the judgement — see `canvas.md`. What an answer never loses is its author: every recommendation, assumption, and departure ends as a decision the user makes through AskUserQuestion, never one the agent makes alone.

`PRD` = the rule goes into Section 5 · `CSS` = the value goes into the styling files · `PRD+CSS` = the rule in the PRD, the number in CSS.

## Decisions, dialogs, and facets

**A decision is the unit of the ledger; a dialog is one AskUserQuestion entry.** The two are not the same count. Every decision has one **primary axis**, asked as a dialog. Some decisions also carry **facets** — values that ride along, derived from a named basis, reported and cancellable but not asked. Two decisions (11 and 13) hold two askable axes each, so they are asked as **two dialogs in the same call**.

**An option may bundle several values only when one source row carries them together.** A palette row holds neutral, accent, and destructive as one designed unit (decision 3); the style row's `Design System Variables` column holds radius and shadow together (decision 8). Axes with no shared source are never fused into invented combinations — a bundle nobody designed forces every off-menu preference through Other. They are asked as separate dialogs in the same call, or one becomes a facet.

## The two modes

| Mode | Dialogs |
|---|---|
| **Fast** | Three — decision 7 (library) · its icon facet, only when the library bundles none · decision 10's minimum-width facet, asked directly. The canvas improvises every other value. See `canvas.md` |
| **Full** | Every decision's primary axis: **16 dialogs** (17 when the library bundles no icons), plus the install block presented as a chat stop right after the closing ledger — never as a dialog. Facets stay derived — reported, cancellable, never silently settled |

**Group skips still apply in every mode:** an app with no lists or tables skips decision 11; an app with no text beyond field labels skips decision 15's norms report.

## Batches

**Questions travel in batches, not one per turn.** AskUserQuestion carries up to four questions per call and several calls fit in one turn — so the full interview lands in three turns. **Batch boundaries follow the dependency edges, and the edges live in two places:** each dialog's own *Options-from* line, and the shift table in `adaptation.md`. A dialog whose options or recommendation read an earlier asked answer goes in a later call than its source; dialogs with no edge between them travel together. Between two calls of the same turn the shifts are applied exactly as `adaptation.md` states — batching compresses turns, never the adaptation.

The full-mode shape:

- **Turn 1** — decisions 1 and 2, alone: nearly everything downstream reads them.
- **Turn 2** — call A: decisions 3, 4, 5, 6 · call B: decisions 7, 8, 9, 10. The icon dialog opens after decision 7 only when the chosen library bundles none.
- **Turn 3** — call C: decision 11 (two dialogs), decision 12, decision 13's first dialog · call D: decision 13's second dialog and decision 14. The **install block follows the closing ledger as a chat stop** — its contents known once decisions 6 and 7 are answered; the skill's install step holds the gate rule.

Each dialog still requires: **more than two options** · **one marked recommendation** · **a one-sentence consequence**. Asked through the **AskUserQuestion tool**, never as prose text — recommendation first and marked "(Recommended)"; the tool's automatic "Other" is how answers outside the options arrive. **Everything the user needs to answer lives inside the dialog** — in the question field or the option descriptions. The dialog may render without the prose around it, so a question referring to text "above" can arrive pointing at nothing.

**Four options is the tool's cap per dialog, and the cap is never a reason to thin the pool.** More than four candidates worth showing → split them across two dialogs in the same call ("Reference apps A–D", "Reference apps E–H"), never silently drop the rest. A dialog whose answers combine rather than exclude — reference apps, features to keep, anti-patterns to enforce — is asked with `multiSelect: true`; a value that excludes its alternatives (radius, density, library) stays single-select.

**An Other answer may carry an option and its detail together.** "Option 1, <the name>" selects that option with the detail attached — read it as that option, never as an answer outside the options. An option whose answer needs typed detail says so in its description; the typing path is Other.

## The ledger

Every decision — asked or derived — is visible twice, in the same shape:

1. **Between batches:** a short report of the facets and derived values settled since the last call, one line each with its basis (`contrast → AA (style row Accessibility)`). This is where a facet that feeds a later dialog surfaces before that dialog opens. The decision-10 archetype table is presented here for correction.
2. **At the interview's close:** the full ledger — all 15 decisions, one row each, facets indented under their decision, each line carrying its value and its source (`asked` / the style row / the palette / `PRD` / `built-in`). The same ledger is shown once more at the final ratification, with any canvas departures marked per row.

**The user may cancel any line, asked or derived.** Cancelling a facet opens it as a normal dialog with the options its entry below names. A derived value settled silently — absent from both reports — is a violation, not a shortcut.

## Rules for the whole interview

**The order in this file is the order the decisions are asked**, in every skill that reads it. No dialog is moved, promoted, or asked out of sequence — a skill that reorders them produces two different interviews for the same app.

**Do not ask what is already answered.** An earlier answer or `Decision_Rules` settles a dialog outright → decide it, report it as a derived line, move on. See `adaptation.md`.

**Answers are reconciled after every batch, and once more before the interview closes.** Two answers that overlap or pull in opposite directions — a dense-and-technical decision 1 beside all-airy references in decision 2, a 360px minimum width beside a fixed sidebar — are a conflict the batch let through, and neither side wins silently. Each conflict goes back as **one question**: name both answers and what collides, offer keeping either side (saying what the other becomes) and a named middle path where one exists, with a recommendation. The resolved answer replaces the original before anything downstream reads it. A conflict surfacing later — in a derived line or on the canvas — is asked the same way at that point, never absorbed.

**Context removes a dialog → skip it and say why.** An app without tables skips decision 11 entirely.

**Zero search results, no Python, or the skill is not installed → the database layer drops out, the interview continues.** Say so plainly, then build the options from the other two layers, each still labelled with its source. What stays forbidden is the lie, not the layer — this rule is from `ui-ux-pro-max` itself: *never present a 0-result search as if it returned data.*

Read the `search.py` command shape from the `ui-ux-pro-max` SKILL.md. Do not copy a path from here.

---

## A. Foundation (1–3)

### 1. Visual direction · PRD

**Options from:** `--domain style "<kind of app> <keywords from the user's story>"`. Take rows whose `Best For` includes this kind of app **and** whose `Do Not Use For` does not. The style name plus a summary of `Keywords` becomes the option label.

**Recommendation:** the top row whose `Accessibility` column is at least WCAG AA and whose `Complexity` is lowest.

**Consequence:** take it from that row's `Best For` and `Do Not Use For` — name what becomes easy and what becomes hard.

This answer drives more of the later recommendations than any other. See `adaptation.md`.

### 2. The app that feels right · PRD

**Options from:** the research pass — 4–8 real, named apps or sites fitting this domain and kind of app, each with a one-line reason it fits ("Pipedrive — sales pipeline, medium density, strong mobile"). **`multiSelect: true`** — several references combine into one direction. More than four candidates → two dialogs in the same call, never a thinned list. The user is never asked to recall a name from nothing; the names are proposed, the user recognizes.

**Recommendation:** the one or two whose product shape sits closest to PRD Section 1.

**Consequence:** a named app cuts more errors than five adjectives, and this is the decision that matters most if the canvas later has to be reworked.

An Other answer naming an app not offered is the best possible outcome, not a deviation. A user who recognizes none → ask which app it must **not** resemble, or ask for a screenshot. This decision has no database query; the chosen references improve the queries for every other decision.

### 3. Palette · PRD+CSS

**One dialog, and the bundle is legitimate:** a `--domain color` row carries the neutral, the accent, and the destructive color as one designed unit, so the options are whole rows.

**Options from:** `--domain color "<kind of app>"`. Take the top 3 rows — `Background` · `Muted` · `Border` for the neutral (its temperature — cool, warm, pure — read from the hex values), `Accent` · `On Accent` · `Primary`, and `Destructive` · `On Destructive`. Each option labelled with its neutral temperature and accent. Plus one fixed option: follow an existing brand color, hex typed via Other.

**Recommendation:** the top row whose product type is closest to PRD Section 1; among ties, the row whose `Notes` column mentions the contrast was adjusted for WCAG.

**Consequence:** one neutral family per app — alternating warm and cool between pages makes the app look assembled from two sources.

**Facets — derived with it, never asked:**

- **Hover step:** one step visibly darker than the accent, still passing the contrast target with `On Accent`. Buttons and links read this token for hover and active; a component that darkens the accent inline has made the same decision twice.
- **Status triads:** every status color lands as `subtle` background, `border`, and `text`, with the text step passing the Section 5 contrast target on the subtle background. Badges, chips, and banners read these three tokens; a tint improvised inside a component instead of reading them is a finding. Full 50–900 shade ramps are still not generated — a token nothing reads is not written. Each triad is one ledger line.

Avoid a purple-blue gradient as the default — see `anti-pattern.md`.

---

## B. Theme & contrast (4–5)

### 4. Dark mode · PRD

**Options from:** the `Light Mode ✓` and `Dark Mode ✓` columns of the chosen style row. A style that does not fully support one of them → strike that option and say why.

**Recommendation:** light only for the first version, unless the chosen style is designed dark.

**Consequence:** dark mode means every color token carries two values that both have to pass contrast, and adding it later is cheaper than maintaining two values from day one for an app whose shape is not settled.

**Facet — contrast target:** read from the `Accessibility` column of the chosen style row — AA (4.5:1 text, 3:1 non-text) at minimum, since AA is already the threshold the `ui-build` gate uses; a row reading AAA lands AAA. Cancelling this facet opens it with the options: WCAG AA · WCAG AAA (7:1 text) · AA plus AAA for primary text only — noting that AAA narrows the palette until almost no accent passes.

### 5. Status marker besides color · PRD

**Options:** icon plus color · text label plus color · a distinct badge shape plus color · icon and text together

**Recommendation:** icon plus color.

**Consequence:** an icon is readable by someone who cannot tell red from green, and stays compact inside a narrow table cell — unlike a text label, which forces the column wider.

Color is never the only marker. That is a rule, not a preference.

**Facet — status count:** four (success, warning, danger, info). Giving info its own color stops ordinary messages from being forced into warning yellow, which over time makes people stop reading all yellow. Cancelling opens the choice of four · three · two.

---

## C. Text (6)

### 6. Typography · PRD+CSS

**Options from:** `--domain typography "<visual direction from decision 1> <kind of app>"`. Take `Font Pairing Name` · `Heading Font` · `Body Font` from the top 3–4 rows. Add one option: a single sans family throughout, plus a monospace for numbers.

**Recommendation:** the row whose `Best For` includes this kind of app. For a table-heavy internal app, favor one that carries a monospace.

**Consequence:** monospace figures make currency columns align vertically, so the gap between large and small is visible without reading the digits.

Font names go into the styling files. The CSV's `Tailwind Config` column can be copied directly. Avoid serif as a default — see `anti-pattern.md`.

**Facets — derived with it, never asked:**

- **Five text steps:** page title, section title, body, supporting text, small label. Few choices force hierarchy to be built from size rather than from grays that get harder to read the more you add. Cancelling opens the choice of four · five · six · seven or more.
- **Line length:** bounded for prose (~65 characters), unbounded in table cells. A paragraph as wide as a 27-inch screen makes the eye lose its place on the return sweep, while a table cell needs the full width so its contents are not clipped. Cancelling opens: unbounded · ~65 · ~80 · bounded for prose, unbounded in cells.

---

## D. Library & surface (7–8)

### 7. Component library and icon family · PRD+CSS

**Options from:** `library-rubric.md` — which names no libraries. Score the needs from PRD Sections 1–3 (platform · large tables · charts · calendar · drag-and-drop · offline), then assemble 3–4 candidates from the model's own knowledge and the research pass, each researched per that file's research duty: what it bundles, what it leaves out, maintained and adopted. Charting needs are matched against `--domain chart`. **Each option names the icon pack it bundles**, or names itself headless.

**Recommendation:** the one that satisfies every need with the fewest extra dependencies.

**Consequence:** name what that library does **not** bring, because that is what gets written by hand later.

This answer decides what is installed, and fills the Component library row in `CLAUDE.md`. It sits here rather than at the front because the only things depending on it — the icon facet and decision 11 — come after it.

**In `design-rework` it carries a second consequence:** changing the library rewrites every component whatever the tokens say, and the app's `CLAUDE.md` states the stack was locked at bootstrap. Any answer but *keep* revokes that lock rather than adjusting it.

**Facet — icon pack: derived when the chosen library bundles one; asked when it bundles none** — a headless library leaves no basis to derive from, so a dialog opens automatically after this one. Its options from `--domain icons "<kind of app> <visual direction>"`, taking the distinct values of the `Library` column, with the `Style` column (outline or solid) as the qualifier; recommendation: the pack already installed alongside the chosen library, when there is one. Choosing otherwise means one more dependency, and the library's own components keep their original icons until you replace them one by one.

**One icon family per app**, no exceptions. An icon missing from that family → report it as a finding; do not draw your own SVG and do not mix two families.

### 8. Surface: radius and elevation · PRD+CSS

**One dialog, and the bundle is legitimate:** `--border-radius` and `--shadow` both come from the `Design System Variables` column of the chosen style row — one designed unit.

**Options from:** that column's pair becomes the recommended option. Add assembled pairs: sharp (zero radius) with no shadow, grouping built from spacing and rules alone — only when the decision-1 style's whole identity is flat (Swiss, brutalist), and name that as the reason · a soft radius with shadow on floating elements only (menus, dialogs, popovers) · uniformly soft radius with soft shadow on cards, stronger on floating elements.

**Recommendation:** the style row's own pair; where it carries no shadow value, soft on cards and stronger on floating elements — tinted toward the background hue, never pure black.

**Consequence:** elevation separates a surface from the page without a border doing all the work; an app with no shadow, one radius, and a near-neutral primary reads as a wireframe, and no later token pass can add back a depth decision that was never made.

**Asked, never derived.** This decision separates *designed* from *flat* more than any other single one, and the database's internal-app styles default the shadow to `none` — deriving it is how every app is born flat on a default nobody chose. One radius value means there is never an argument about which radius a new element takes, and no pill button strays onto a page of sharp corners.

---

## E. Space (9–10)

### 9. Density · PRD+CSS

**Options from:** the `--spacing` value in `Design System Variables`, translated into four levels: airy · standard · dense · very dense.

**Recommendation:** dense for an internal dashboard; follow the chosen style's `--spacing` otherwise.

**Consequence:** an app open all day is judged by how much is visible without scrolling — but every element gets smaller, so text contrast cannot be compromised.

→ Fills the `--density` dial.

**Facet — two profiles when the roles split.** PRD Section 2 naming both a desk role and a field or phone role → density is written as **two named profiles with numbers**, not one adjective: control height, table row height, base font size, minimum touch target, and layout columns, per profile. The desk profile follows the level chosen above; the phone profile carries ≥44px touch targets and a single column. Derived from the role split and reported — one role at a desk all day means one profile and this facet stays silent.

### 10. Page frame · PRD

**The dialog asks the shell; the widths ride as facets.**

**Options from:** the `Dashboard Style (if applicable)` column of `--domain product "<kind of app>"`, plus: fixed sidebar · collapsible sidebar · top bar only · sidebar plus top bar.

**Recommendation:** a collapsible left sidebar for a multi-role app.

**Consequence:** a sidebar absorbs a growing menu without being redesigned, and collapses when the user needs full width for a table — two things a top bar cannot do.

→ Also feeds the `--variance` dial.

**Facets — derived with it, never asked:**

- **Lowest supported width:** 360px when PRD Section 2 names a role working in the field; 1024px when every user sits at a desk. Stating the lower bound explicitly means anything below it is **unsupported rather than broken** — without that statement, every "it looks wrong on my phone" report becomes work nobody ever decided to take on. Cancelling opens: 360px · 768px · 1024px · 1280px. **Fast mode asks this facet directly.**
- **Maximum content width:** bounded for forms and prose, full width for tables. A clipped table forces horizontal scrolling that hides columns, while a form as wide as a 27-inch screen puts label and input half a desk apart. Cancelling opens: unbounded · bounded and centered · bounded for forms and prose, full width for tables.

**The archetype table, derived after the shell is chosen.** Group every page of PRD Sections 2 and 3 into **screen archetypes** — usually 4–7 (auth, dashboard, data table, form, wizard, detail/approval are the recurring ones). Per archetype one row: shell layout in one sentence, the components it is built from, its density profile, its empty/loading wording, and the routes it owns. Every route lands in exactly one archetype. Derived and shown once as a table for the user to correct — in the between-batch report, exactly like a fast-mode report — never asked page by page. A page fitting no archetype is put to the user as its own question; it is never silently given a bespoke layout, because the table is what stops a later session from assembling that page from nothing. The ratified table is written into Section 5 under Page Composition, and `build-flow` Section 4 opens every later page proposal by naming its archetype.

---

## F. Data (11)

*Skip this entire decision if the app shows no lists or tables.*

### 11. Tables · PRD+CSS

**Two dialogs in the same call — paging and row actions have no shared source and do not bundle.**

**Dialog one — paging or scrolling:**

**Options:** numbered pages · a load-more button · infinite scroll · scrolling with a sticky header row

**Recommendation:** numbered pages.

**Consequence:** paging gives the user a place they can refer to ("it's on page 3") and makes the total count visible — two things infinite scroll loses, and both come up constantly when people ask each other about data over chat.

**Dialog two — row actions:**

**Options:** action icons always visible · a three-dot menu · an icon for the primary action, a menu for the rest · revealed on row hover

**Recommendation:** an icon for the primary action, a menu for the rest.

**Consequence:** the most-used action stays one click away while rare actions stop eating column width — and nothing is hidden behind hover, which does not exist on a touch screen.

**Facets — derived, never asked:**

- **Row separators:** a thin rule between every row, using the `Border` value from the chosen palette. A thin rule keeps the eye on the same row while scanning to the rightmost column, without the visual weight of alternating tints that make a long table look striped. Cancelling opens: rule every row · alternating tint · spacing only · rules between groups.
- **Row height:** derived from the decision-9 density — dense → compact-to-medium (~32–40px). 40px fits a status badge and an action button inside the row without clipping, while still showing roughly twice the rows of a roomy height. Cancelling opens: compact (~32px) · medium (~40px) · roomy (~48px) · user-adjustable. A row height below the minimum touch target is a collision, not a detail — say which of the two gives way, and write the exception down where the other rule lives.

---

## G. Interaction (12–14)

### 12. Motion level · PRD

**Options from:** the `Effects & Animation` column of the chosen style row, translated into four levels: near-static · subtle (150–200ms) · moderate · rich.

**Recommendation:** follow that column; for internal apps it usually lands on subtle.

**Consequence:** short transitions explain that something opened or closed without making the user wait, while longer ones read as slow precisely to the people using the same app hundreds of times a day.

→ Fills the `--motion` dial. Any motion honors `prefers-reduced-motion`.

### 13. Feedback and confirmation · PRD

**Two dialogs in the same call — reporting results and guarding destruction have no shared source and do not bundle.**

**Dialog one — reporting the result of an action:**

**Options:** a corner toast · inline near the element that changed · inline for failures, toast for successes · toast for everything plus inline for form errors

**Recommendation:** inline for failures, toast for successes.

**Consequence:** a failure that appears next to its cause cannot be missed and does not disappear on its own, while a success is genuinely allowed to pass by without shifting the layout.

**Dialog two — confirming an irreversible action:**

**Options:** a confirmation dialog · a dialog that requires retyping the record's name · run immediately with an undo button for a few seconds · confirmation only for permanent deletion

**Recommendation:** a confirmation dialog for anything irreversible, plus retyping the name for anything deleting many records at once.

**Consequence:** a plain dialog eventually gets clicked through unread, so the second layer is reserved for actions that genuinely have no way back.

### 14. Forms: label position and validation timing · PRD

**Options:** label above + validate on blur · label above + validate on submit · label to the left + validate on blur · label above + validate while typing

**Recommendation:** label above, validate on blur.

**Consequence:** a label above never runs out of room when the wording is long, and validating on blur reports the error before the user reaches the bottom — without scolding someone who has typed two characters.

A placeholder never replaces a label.

---

## H. Copy (15)

*Skip this decision's report if the app shows no text beyond field labels.*

### 15. Copy norms · PRD

**Nothing here is asked — the whole decision is fixed norms**, written into Section 5 as derived lines, each cancellable from the ledger like any other. These norms have no database source: a `--domain ux` search for label length or microcopy returns contrast, alt text, font size, and line length — nothing about wording. Do not run it here and do not present its rows as if they answered this.

**Every bound is read in the on-screen language.** Take that language from the Locale row of the app's `CLAUDE.md`. A character count borrowed from English-language design guidance is wrong for any other language — "Not contacted" is 13 characters and "Belum dihubungi" is 15, and that difference repeats on nearly every label.

**Norm — repeated labels: short by default, the tightest wording that still names the thing exactly.** Precision first, then brevity: cut articles and qualifiers, never the distinguishing word. A repeated label — status chip, column header, navigation item — that needs a sentence moves the sentence to `aria-label` or a tooltip and keeps the exact short form on screen. Why fixed: a label repeating twenty-five times down a column sets that column's width — and the untended default drifts long, because descriptive reads as safe.

**Norm — navigation and button labels: two words as the target, a third only when it removes ambiguity.** "Ekspor" alone is ambiguous where "Ekspor ke Excel" is not — the third word that disambiguates stays; a word that decorates goes. A button appears once per screen, so cutting its words saves no width — the target serves precision, not space: a button carries the verb that names its action exactly, and nothing decorative. "Simpan", "Jalankan pencocokan" — never "Klik di sini untuk menyimpan". Short follows from the right verb by itself.

**Norm — icon plus verb is the default for every action button** — the icon makes the action scannable across the system, the verb kills the ambiguity, and the icon comes from the app's one family. **Icon-only is the exception, at named places**: row actions in tables (decision 11) and toolbar conventions (search, edit, delete) — always with the verb in `aria-label` and a tooltip. **Never icon-only**: a destructive action's confirming button, and a page's primary action.

**Norm — supporting text: at most one short sentence per section, and only for a section whose consequence cannot be read from its own contents.** Supporting text is read every time and useful once, so on a screen worked forty times a day it turns into permanent noise. Cancelling this line opens: none at all · at most one sentence · at most two · unbounded.

**In `design-rework`** the audit measures the longest and median repeated label and counts the supporting paragraphs and their sentences — reported as findings and measured confirmations against these norms, never re-derived from a database. A cancelled norm there builds its options around the measured counts.

---

# Mapping to the `ui-ux-pro-max` dials

| Dial | Filled from |
|---|---|
| `--variance` | Decision 1 (visual direction) and decision 10 (page frame) |
| `--motion` | Decision 12 |
| `--density` | Decision 9 |

Do not use any skill's built-in baseline. The `design-taste-frontend` baseline (8/6/4) is designed for landing pages and points the wrong way for an internal dashboard.

# What is not asked

Loading, empty state, and error placement are **not decisions here**. All three are fixed norms in the `ui-build` skill of `raizen-norms`, identical across every internal app.

Wording rules beyond decision 15 are fixed there too — sentence case, active voice, no exclamation marks, and rationale kept off the screen. They do not vary per app, so asking them spends context on an answer that is already known.
