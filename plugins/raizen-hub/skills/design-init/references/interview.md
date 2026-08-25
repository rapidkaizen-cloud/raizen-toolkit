# Frontend interview — 15 decisions

**The options are not written in this file, and no single source owns them.** They are assembled from three layers, every option labelled with where it came from:

1. **The anchors** — the reference apps the user picks in decision 1 (labelled `reference`) and, off the web, the target platform's design language (labelled `platform`). Once decision 1 is answered, every later pool carries at least one anchored option.
2. **The model's own reading of the domain** — what this kind of app conventionally carries, labelled `assembled`.
3. **Web research — per turn, and mandatory.** Before turn 1, run a WebSearch pass built from the corrected Step 1 reading: the kind of app, its domain, its closest well-known products — this pass is what proposes decision 1's candidate references, and decision 2 reads it too. Before each later turn, run one more pass scoped to that turn's decisions, carrying the chosen references and the answers already given as keywords; a turn whose every dialog carries only fixed options written in this file skips its pass. Fold what each pass returns into that turn's pools, labelled `research`. One pass per turn, never one search per question; a pass that returns nothing useful is said plainly, not padded.

**No option without a stated basis.** Every option assembled for a decision marked *Options from:* states what it stands on — a named real product (`reference`), the platform's design language (`platform`), a research finding with its source (`research`), or a stated domain convention (`assembled`) — and one line on why it fits this app. An option with none of those and no domain reason is the default: it may still be offered, labelled `default`, but it is never the recommendation — written a one-line domain reason, it becomes `assembled`, not `default`. Decisions whose options are structural and written in this file (5, 11, 13, 14) are exempt; their consequence line is the justification. A pool where every option reads `default` is a failed assembly, not a pool — re-run that turn's research pass with sharper keywords before asking, unless the pass already dropped out under the rule below: then the pool stands on the domain reading, labelled honestly.

**Answers are the user's preferences, not gates.** They set the canvas's baseline; the canvas may depart from any of them with a drawn, tagged, reasoned departure that the user settles at the judgement — see `canvas.md`. What an answer never loses is its author: every recommendation, assumption, and departure ends as a decision the user makes through AskUserQuestion, never one the agent makes alone.

`PRD` = the rule goes into Section 5 · `CSS` = the value goes into the styling files · `PRD+CSS` = the rule in the PRD, the number in CSS.

## Decisions, dialogs, and facets

**A decision is the unit of the ledger; a dialog is one AskUserQuestion entry.** The two are not the same count. Every decision has one **primary axis**, asked as a dialog. Some decisions also carry **facets** — values that ride along, derived from a named basis, reported and cancellable but not asked. Two decisions (11 and 13) hold two askable axes each, so they are asked as **two dialogs in the same call**.

**An option may bundle several values only when one anchor carries them together.** A palette is one designed unit — neutral, accent, and destructive read from the same anchor (decision 3); radius and shadow arrive together as one surface treatment read from the chosen direction's anchor (decision 8). Axes with no shared anchor are never fused into invented combinations — a bundle nobody designed forces every off-menu preference through Other. They are asked as separate dialogs in the same call, or one becomes a facet.

## The two modes

| Mode | Dialogs |
|---|---|
| **Fast** | Three — decision 7 (library) · its icon facet, only when the library bundles none · decision 10's minimum-width facet, asked directly. The canvas improvises every other value. See `canvas.md` |
| **Full** | Every decision's primary axis: **16 dialogs** (17 when the library bundles no icons), plus the install block presented as a chat stop right after the closing ledger — never as a dialog. Facets stay derived — reported, cancellable, never silently settled |

**Group skips still apply in every mode:** an app with no lists or tables skips decision 11; an app with no text beyond field labels skips decision 15's norms report.

## Batches

**Questions travel in batches, not one per turn.** AskUserQuestion carries up to four questions per call and several calls fit in one turn — so the full interview lands in three turns. **Batch boundaries follow the dependency edges, and the edges live in two places:** each dialog's own *Options-from* line, and the shift table in `adaptation.md`. A dialog whose options or recommendation read an earlier asked answer goes in a later call than its source; dialogs with no edge between them travel together. Between two calls of the same turn the shifts are applied exactly as `adaptation.md` states — batching compresses turns, never the adaptation.

The full-mode shape:

- **Turn 1** — decision 1, then decision 2 in a second call of the same turn: 2's pool is anchored to 1's answer, and nearly everything downstream reads both.
- **Turn 2** — call A: decisions 3, 4, 5, 6 · call B: decisions 7, 8, 9, 10. The icon dialog opens after decision 7 only when the chosen library bundles none.
- **Turn 3** — call C: decision 11 (two dialogs) and decision 12 · call D: decision 13 (two dialogs) and decision 14. The **install block follows the closing ledger as a chat stop** — its contents known once decisions 6 and 7 are answered; the skill's install step holds the gate rule.

Each dialog still requires: **more than two options** · **one marked recommendation** · **a one-sentence consequence**. Asked through the **AskUserQuestion tool**, never as prose text — recommendation first and marked "(Recommended)"; the tool's automatic "Other" is how answers outside the options arrive. **Everything the user needs to answer lives inside the dialog** — in the question field or the option descriptions. The dialog may render without the prose around it, so a question referring to text "above" can arrive pointing at nothing.

**Four options is the tool's cap per dialog, and the cap is never a reason to thin the pool.** More than four candidates worth showing → split them across two dialogs in the same call ("Reference apps A–D", "Reference apps E–H"), never silently drop the rest. A dialog whose answers combine rather than exclude — reference apps, features to keep, anti-patterns to enforce — is asked with `multiSelect: true`; a value that excludes its alternatives (radius, density, library) stays single-select.

**An Other answer may carry an option and its detail together.** "Option 1, <the name>" selects that option with the detail attached — read it as that option, never as an answer outside the options. An option whose answer needs typed detail says so in its description; the typing path is Other.

## The ledger

Every decision — asked or derived — is visible twice, in the same shape:

1. **Between batches:** a short report of the facets and derived values settled since the last call, one line each with its basis (`contrast → AA (the ui-build floor)`). This is where a facet that feeds a later dialog surfaces before that dialog opens. The decision-10 archetype table is presented here for correction.
2. **At the interview's close:** the full ledger — all 15 decisions, one row each, facets indented under their decision, each line carrying its value and its source (`asked` / `reference` / `platform` / `research` / `assembled` / `default` / `PRD` / `built-in`) — an asked decision's row is `asked`, whatever label its chosen option carried. The same ledger is shown once more at the final ratification, with any canvas departures marked per row.

**The user may cancel any line, asked or derived.** Cancelling a facet opens it as a normal dialog with the options its entry below names. A derived value settled silently — absent from both reports — is a violation, not a shortcut.

## The default gate

**Run where the answers become concrete values — Full mode's compile step — web only.** Off the web the canvas's side-by-side against a native application is the gate; this one exists because on the web there is no external bar, and the stock look passes every internal check. **A value the user chose through a dialog — asked, Other, or a Keep answer — passes outright**: the gate polices the unchosen, never the user. What it checks is every compiled or derived value whose basis is `assembled` or `default`, against this list — the values an app wears when nobody chose:

- accent `#2563EB` or `#7C3AED` · destructive `#DC2626` — the same color in any notation, not the literal string
- Inter as the sole text family (a monospace for numbers does not count against it)
- `0.5rem` radius everywhere with no shadow anywhere
- a compiled baseline equal to the component library's shipped theme

A listed value with a written domain reason beside it passes. A listed value without one → reopen the decision that produced it, before the canvas renders it — a default nobody chose is cheapest to replace before it is drawn. A reopened decision the user answers with the same value passes: it is chosen now. The list is short on purpose: it names markers of the unchosen, never forbidden values.

## Rules for the whole interview

**The order in this file is the order the decisions are asked**, in every skill that reads it. No dialog is moved, promoted, or asked out of sequence — a skill that reorders them produces two different interviews for the same app.

**Do not ask what is already answered.** An earlier answer or a shift in `adaptation.md` settles a dialog outright → decide it, report it as a derived line, move on. See `adaptation.md`.

**Answers are reconciled after every batch, and once more before the interview closes.** Two answers that overlap or pull in opposite directions — a dense-and-technical decision 2 beside all-airy references in decision 1, a 360px minimum width beside a fixed sidebar — are a conflict the batch let through, and neither side wins silently. Each conflict goes back as **one question**: name both answers and what collides, offer keeping either side (saying what the other becomes) and a named middle path where one exists, with a recommendation. The resolved answer replaces the original before anything downstream reads it. A conflict surfacing later — in a derived line or on the canvas — is asked the same way at that point, never absorbed.

**Context removes a dialog → skip it and say why.** An app without tables skips decision 11 entirely.

**On a non-web Surface, the vocabulary substitutes before any pool is assembled.** The anchors are product-shaped, and research answers in the web's terms whatever the query carries — so three substitutions, stated once here rather than forked into every decision: the **design language** — the target OS's own enters every pool where a style, palette, or icon family is chosen, as a fixed option labelled `platform`; the **unit** — the platform's own rather than the CSS pixel, so a frame facet reads window minimum size, size classes, or window size classes in dp; the **shell** — that platform's navigation model rather than sidebar-or-top-bar. A substitution with no research or reference behind it is labelled `assembled` and says so. On a cross-OS shell (Tauri, Electron, Flutter desktop) the target OS is read from where PRD Section 2's users actually sit; where the PRD does not settle it, it is pinned at the Step 1 reading correction. Written per decision instead, thirty-two forks would double a file that every web session reads in full.

**A research pass returning nothing useful, or no way to run WebSearch → the research layer drops out for that turn, the interview continues** on the anchors and the domain reading, every option still labelled with its source. What stays forbidden is the lie, not the layer: never present an empty pass as if it returned findings.

**An anchor whose concrete values cannot be read is still an anchor.** Research often cannot confidently yield a reference's actual hex, radius, or shadow. The option is then offered descriptively — the named product and the treatment it wears — and its concrete values are compiled later, labelled `assembled` and said so; every contrast check runs on the concrete candidate actually proposed, whatever its label. A reference is never dropped for being unreadable, and a value is never presented as read from it when it was not.

---

## A. Foundation (1–3)

### 1. The app that feels right · PRD

**Options from:** the turn-1 research pass — 4–8 real, named apps or sites fitting this domain and kind of app, each with a one-line reason it fits ("Pipedrive — sales pipeline, medium density, strong mobile"). **`multiSelect: true`** — several references combine into one direction. More than four candidates → two dialogs in the same call, never a thinned list. The user is never asked to recall a name from nothing; the names are proposed, the user recognizes.

**Recommendation:** the one or two whose product shape sits closest to PRD Section 1.

**Consequence:** a named app cuts more errors than five adjectives, and this is the decision that matters most if the canvas later has to be reworked.

An Other answer naming an app not offered is the best possible outcome, not a deviation. A user who recognizes none → ask which app it must **not** resemble, or ask for a screenshot. **This decision is asked first because it anchors everything:** the chosen references enter every later pool as options and every later research pass as keywords.

### 2. Visual direction · PRD

**Options from:** the chosen references, each read as a direction — one option per distinct direction they carry, its label naming the reference and the treatment ("Linear-like — dark, flat, high type contrast") · off-web, the platform's design language as the fixed `platform` option · the direction the turn-1 research pass surfaced as this domain's convention.

**Recommendation:** the direction the chosen references share, where they share one; otherwise the one that fits how the app is used — all-day internal work reads calm and dense better than expressive.

**Consequence:** name what the direction makes easy and what it makes hard — a dark, dense direction reads fast at a desk and poorly in sunlight; an airy one the reverse.

This answer drives more of the later recommendations than any other. See `adaptation.md`.

### 3. Palette · PRD+CSS

**One dialog, and the bundle is legitimate:** a palette is one designed unit — the neutral, the accent, and the destructive color are read from one anchor, never mixed from three.

**Options from:** the palettes the chosen references actually wear — neutral temperature (cool, warm, pure — read from their surfaces) plus accent, one option per distinct palette · off-web, the platform language's own palette as the fixed `platform` option · a palette the research pass named for this domain. Each option labelled with its neutral temperature and accent. Plus one fixed option: follow an existing brand color, hex typed via Other.

**Recommendation:** the option closest to the chosen references whose contrast passes the decision 4 target — checked with real hex pairs, never assumed.

**Consequence:** one neutral family per app — alternating warm and cool between pages makes the app look assembled from two sources.

**Facets — derived with it, never asked:**

- **Hover step:** visibly darker than the accent — on the order of 8–12% lightness — still passing the contrast target against the accent's own text color. Buttons and links read this token for hover and active; a component that darkens the accent inline has made the same decision twice.
- **Status triads:** every status color lands as `subtle` background, `border`, and `text`, with the text step passing the Section 5 contrast target on the subtle background. Success, warning, and info hues are read from the chosen reference where readable, otherwise assembled and labelled. Badges, chips, and banners read these three tokens; a tint improvised inside a component instead of reading them is a finding. Full 50–900 shade ramps are still not generated — a token nothing reads is not written. Each triad is one ledger line.

Avoid a purple-blue gradient as the default — see `anti-pattern.md`.

---

## B. Theme & contrast (4–5)

### 4. Dark mode · PRD

**Options from:** the chosen direction's anchor. A reference that ships both modes, or a platform language with a designed dark variant, offers both; an anchor whose dark side would have to be derived → strike that option and say why — a derived dark mode is a second design job, not a toggle.

**Recommendation:** light only for the first version, unless the chosen direction is designed dark.

**Consequence:** dark mode means every color token carries two values that both have to pass contrast, and adding it later is cheaper than maintaining two values from day one for an app whose shape is not settled.

**Facet — contrast target:** WCAG AA (4.5:1 text, 3:1 non-text) at minimum — AA is already the threshold the `ui-build` gate uses; off-web the platform's own accessibility bar applies where it is stricter. Cancelling this facet opens it with the options: WCAG AA · WCAG AAA (7:1 text) · AA plus AAA for primary text only — noting that AAA narrows the palette until almost no accent passes.

### 5. Status marker besides color · PRD

**Options:** icon plus color · text label plus color · a distinct badge shape plus color · icon and text together

**Recommendation:** icon plus color.

**Consequence:** an icon is readable by someone who cannot tell red from green, and stays compact inside a narrow table cell — unlike a text label, which forces the column wider.

Color is never the only marker. That is a rule, not a preference.

**Facet — status count:** four (success, warning, danger, info). Giving info its own color stops ordinary messages from being forced into warning yellow, which over time makes people stop reading all yellow. Cancelling opens the choice of four · three · two.

---

## C. Text (6)

### 6. Typography · PRD+CSS

**Options from:** what the chosen references and direction actually use, where the research pass can name it ("Inter tightened — what Linear ships") · pairings the pass surfaced for this domain · off-web, the platform's system family as the fixed `platform` option. Add one option: a single sans family throughout, plus a monospace for numbers.

**Recommendation:** the pairing that fits this kind of app. For a table-heavy internal app, favor one that carries a monospace.

**Consequence:** monospace figures make currency columns align vertically, so the gap between large and small is visible without reading the digits.

Font names go into the styling files. Avoid serif as a default — see `anti-pattern.md`.

**Facets — derived with it, never asked:**

- **Five text steps:** page title, section title, body, supporting text, small label. Few choices force hierarchy to be built from size rather than from grays that get harder to read the more you add. Cancelling opens the choice of four · five · six · seven or more.
- **Line length:** bounded for prose (~65 characters), unbounded in table cells. A paragraph as wide as a 27-inch screen makes the eye lose its place on the return sweep, while a table cell needs the full width so its contents are not clipped. Cancelling opens: unbounded · ~65 · ~80 · bounded for prose, unbounded in cells.

---

## D. Library & surface (7–8)

### 7. Component library and icon family · PRD+CSS

**Options from:** `library-rubric.md` — which names no libraries. Score the needs from PRD Sections 1–3 (platform · large tables · charts · calendar · drag-and-drop · offline), then assemble 3–4 candidates from the model's own knowledge and the research pass, each researched per that file's research duty: what it bundles, what it leaves out, maintained and adopted. Charting needs are researched per candidate under the same duty. **Each option names the icon pack it bundles**, or names itself headless.

**Recommendation:** the one that satisfies every need with the fewest extra dependencies.

**Consequence:** name what that library does **not** bring, because that is what gets written by hand later.

This answer decides what is installed, and fills the Component library row in `CLAUDE.md`. It sits here rather than at the front because the only things depending on it — the icon facet and decision 11 — come after it.

**In `design-rework` it carries a second consequence:** changing the library rewrites every component whatever the tokens say, and the app's `CLAUDE.md` states the stack was locked at bootstrap. Any answer but *keep* revokes that lock rather than adjusting it.

**Facet — icon pack: derived when the chosen library bundles one; asked when it bundles none** — a headless library leaves no basis to derive from, so a dialog opens automatically after this one. Its options from the research pass and the chosen references — the icon families this platform and direction actually use, outline or solid named as the qualifier; recommendation: the pack already installed alongside the chosen library, when there is one. Choosing otherwise means one more dependency, and the library's own components keep their original icons until you replace them one by one.

**One icon family per app**, no exceptions. An icon missing from that family → report it as a finding; do not draw your own SVG and do not mix two families.

### 8. Surface: radius and elevation · PRD+CSS

**One dialog, and the bundle is legitimate:** radius and shadow arrive together as one surface treatment, read from the chosen direction's anchor — a reference app or platform language carries them as one designed decision.

**Options from:** the anchor's own pair — measured from the chosen references or the platform language — becomes the recommended option. Add assembled pairs: sharp (zero radius) with no shadow, grouping built from spacing and rules alone — only when the decision-2 direction's whole identity is flat (Swiss, brutalist), and name that as the reason · a soft radius with shadow on floating elements only (menus, dialogs, popovers) · uniformly soft radius with soft shadow on cards, stronger on floating elements.

**Recommendation:** the anchor's own pair; where the anchor carries no shadow, soft on cards and stronger on floating elements — tinted toward the background hue, never pure black.

**Consequence:** elevation separates a surface from the page without a border doing all the work; an app with no shadow, one radius, and a near-neutral primary reads as a wireframe, and no later token pass can add back a depth decision that was never made.

**Asked, never derived.** This decision separates *designed* from *flat* more than any other single one, and internal apps drift shadowless by default — deriving it is how every app is born flat on a default nobody chose. One radius value means there is never an argument about which radius a new element takes, and no pill button strays onto a page of sharp corners.

---

## E. Space (9–10)

### 9. Density · PRD+CSS

**Options from:** four levels — airy · standard · dense · very dense — the recommended one read from how the chosen references sit; a reference open all day is nearly always dense.

**Recommendation:** dense for an internal dashboard; the chosen references' own density otherwise.

**Consequence:** an app open all day is judged by how much is visible without scrolling — but every element gets smaller, so text contrast cannot be compromised.

**Facet — two profiles when the roles split.** PRD Section 2 naming both a desk role and a field or phone role → density is written as **two named profiles with numbers**, not one adjective: control height, table row height, base font size, minimum touch target, and layout columns, per profile. The desk profile follows the level chosen above; the phone profile carries ≥44px touch targets and a single column. Derived from the role split and reported — one role at a desk all day means one profile and this facet stays silent.

### 10. Page frame · PRD

**The dialog asks the shell; the widths ride as facets.**

**Options from:** fixed sidebar · collapsible sidebar · top bar only · sidebar plus top bar — the shell the chosen references wear named as such in its option.

**Recommendation:** a collapsible left sidebar for a multi-role app.

**Consequence:** a sidebar absorbs a growing menu without being redesigned, and collapses when the user needs full width for a table — two things a top bar cannot do.

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

**Consequence:** the most-used action stays one click away while rare actions stop eating column width — and nothing is hidden behind hover, which does not exist on a touch screen. A desktop application binary is the exception `ui-build` names: there hover-revealed row actions are the platform's own convention.

**Facets — derived, never asked:**

- **Row separators:** a thin rule between every row, using the `Border` value from the chosen palette. A thin rule keeps the eye on the same row while scanning to the rightmost column, without the visual weight of alternating tints that make a long table look striped. Cancelling opens: rule every row · alternating tint · spacing only · rules between groups.
- **Row height:** derived from the decision-9 density — airy → roomy (~48px) · standard → medium (~40px) · dense → compact-to-medium (~32–40px) · very dense → compact (~32px). 40px fits a status badge and an action button inside the row without clipping, while still showing roughly twice the rows of a roomy height. Cancelling opens: compact (~32px) · medium (~40px) · roomy (~48px) · user-adjustable. A row height below the minimum touch target is a collision, not a detail — say which of the two gives way, and write the exception down where the other rule lives.

---

## G. Interaction (12–14)

### 12. Motion level · PRD

**Options from:** four levels — near-static · subtle (150–200ms) · moderate · rich — the recommended one read from the chosen direction's anchor.

**Recommendation:** what the anchor carries; for internal apps it usually lands on subtle.

**Consequence:** short transitions explain that something opened or closed without making the user wait, while longer ones read as slow precisely to the people using the same app hundreds of times a day.

Any motion honors `prefers-reduced-motion`.

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

**Nothing here is asked — the whole decision is fixed norms**, written into Section 5 as derived lines, each cancellable from the ledger like any other. They have no research source to consult, and none is run for them.

**Every bound is read in the on-screen language.** Take that language from the Locale row of the app's `CLAUDE.md`. A character count borrowed from English-language design guidance is wrong for any other language — "Not contacted" is 13 characters and "Belum dihubungi" is 15, and that difference repeats on nearly every label.

**Norm — repeated labels: short by default, the tightest wording that still names the thing exactly.** Precision first, then brevity: cut articles and qualifiers, never the distinguishing word. A repeated label — status chip, column header, navigation item — that needs a sentence moves the sentence to `aria-label` or a tooltip and keeps the exact short form on screen. Why fixed: a label repeating twenty-five times down a column sets that column's width — and the untended default drifts long, because descriptive reads as safe.

**Norm — navigation and button labels: two words as the target, a third only when it removes ambiguity.** "Ekspor" alone is ambiguous where "Ekspor ke Excel" is not — the third word that disambiguates stays; a word that decorates goes. A button appears once per screen, so cutting its words saves no width — the target serves precision, not space: a button carries the verb that names its action exactly, and nothing decorative. "Simpan", "Jalankan pencocokan" — never "Klik di sini untuk menyimpan". Short follows from the right verb by itself.

**Norm — icon plus verb is the default for every action button** — the icon makes the action scannable across the system, the verb kills the ambiguity, and the icon comes from the app's one family. **Icon-only is the exception, at named places**: row actions in tables (decision 11) and toolbar conventions (search, edit, delete) — always with the verb in `aria-label` and a tooltip. **Never icon-only**: a destructive action's confirming button, and a page's primary action.

**Norm — supporting text: at most one short sentence per section, and only for a section whose consequence cannot be read from its own contents.** Supporting text is read every time and useful once, so on a screen worked forty times a day it turns into permanent noise. Cancelling this line opens: none at all · at most one sentence · at most two · unbounded.

**In `design-rework`** the audit measures the longest and median repeated label and counts the supporting paragraphs and their sentences — reported as findings and measured confirmations against these norms, never re-derived. A cancelled norm there builds its options around the measured counts.

---

# What is not asked

Loading, empty state, and error placement are **not decisions here**. All three are fixed norms in the `ui-build` skill of `raizen-norms`, identical across every internal app.

Wording rules beyond decision 15 are fixed there too — sentence case, active voice, no exclamation marks, and rationale kept off the screen. They do not vary per app, so asking them spends context on an answer that is already known.
