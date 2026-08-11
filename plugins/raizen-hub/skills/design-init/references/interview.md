# Frontend interview — a procedure, 27 questions

**The options are not written in this file.** Each question names which query to run against `ui-ux-pro-max` and which column becomes the options, so the choices follow the user's story instead of being one fixed list for every app.

One question per turn. Each still requires: **more than two options** · **one marked recommendation** · **a one-sentence consequence**.

`PRD` = the rule goes into Section 5 · `CSS` = the value goes into the styling files · `PRD+CSS` = the rule in the PRD, the number in CSS.

## Rules for the whole interview

**Do not ask what is already answered.** An earlier answer or `Decision_Rules` settles a question outright → decide it, report it as a derived decision, move on. See `adaptation.md`.

**Context removes a question → skip it and say why.** An app without tables skips group F.

**Zero search results, no Python, or the skill is not installed → do not invent.** Say so plainly, then offer two paths: postpone until the skill is usable, or continue with self-assembled options that are **explicitly marked** as not coming from the database. This rule is from `ui-ux-pro-max` itself: *never present a 0-result search as if it returned data.*

Read the `search.py` command shape from the `ui-ux-pro-max` SKILL.md. Do not copy a path from here.

---

## 0. Component library · PRD+CSS

**Options from:** `library-rubric.md`. Score the needs from PRD Sections 1–3 (platform · large tables · charts · calendar · drag-and-drop · offline), then assemble 3–4 libraries that satisfy all of them. Charting needs are matched against `--domain chart`.

**Recommendation:** the one that satisfies every need with the fewest extra dependencies.

**Consequence:** name what that library does **not** bring, because that is what gets written by hand later.

This answer decides what is installed in Step 5, and fills the Component library row in `CLAUDE.md`.

---

## A. Foundation (1–5)

### 1. Visual direction · PRD

**Options from:** `--domain style "<kind of app> <keywords from the user's story>"`. Take rows whose `Best For` includes this kind of app **and** whose `Do Not Use For` does not. The style name plus a summary of `Keywords` becomes the option label.

**Recommendation:** the top row whose `Accessibility` column is at least WCAG AA and whose `Complexity` is lowest.

**Consequence:** take it from that row's `Best For` and `Do Not Use For` — name what becomes easy and what becomes hard.

This answer drives more of the later recommendations than any other. See `adaptation.md`.

### 2. The app that feels right · PRD

**Options:** name one app or site · none, follow the recommendation · there is one but it is hard to name

**Recommendation:** name one, even if it only half fits.

**Consequence:** one app name cuts more errors than five adjectives, and this is the question that matters most if the reference page later has to be reworked.

"Hard to name" → ask for a screenshot, or ask which app it must **not** resemble. This question has no query; its answer is what improves the queries for the others.

### 3. Neutral family · PRD+CSS

**Options from:** `--domain color "<kind of app>"`. Take the `Background` · `Muted` · `Border` columns from the top 3 rows; the neutral's temperature (cool, warm, pure) is read from its hex values.

**Recommendation:** the top row whose product type is closest to PRD Section 1.

**Consequence:** one neutral family per app — alternating warm and cool between pages makes the app look assembled from two sources.

### 4. Accent color · PRD+CSS

**Options from:** the same query, columns `Accent` · `On Accent` · `Primary`. Add one fixed option: follow an existing brand color.

**Recommendation:** the row whose `Notes` column mentions the contrast was adjusted for WCAG.

**Consequence:** one accent means the primary button is the same color on every screen, so the user learns once where to press.

Avoid a purple-blue gradient as the default — see `anti-pattern.md`.

### 5. Status colors · PRD+CSS

**Options from:** the `Destructive` · `On Destructive` columns of the chosen row, plus how many statuses to carry: four (success, warning, danger, info) · three · two.

**Recommendation:** four statuses.

**Consequence:** giving info its own color stops ordinary messages from being forced into warning yellow, which over time makes people stop reading all yellow.

---

## B. Theme & contrast (6–8)

### 6. Dark mode · PRD

**Options from:** the `Light Mode ✓` and `Dark Mode ✓` columns of the chosen style row. A style that does not fully support one of them → strike that option and say why.

**Recommendation:** light only for the first version, unless the chosen style is designed dark.

**Consequence:** dark mode means every color token carries two values that both have to pass contrast, and adding it later is cheaper than maintaining two values from day one for an app whose shape is not settled.

### 7. Contrast target · PRD

**Options:** WCAG AA (4.5:1 text, 3:1 non-text) · WCAG AAA (7:1 text) · AA plus AAA for primary text only

**Recommendation:** follow the `Accessibility` column of the chosen style; if it reads AAA, offer AAA as the recommendation.

**Consequence:** AA is already the threshold the `ui-build` gate uses, so there is no second rule to remember; AAA narrows the palette until almost no accent passes.

### 8. Status marker besides color · PRD

**Options:** icon plus color · text label plus color · a distinct badge shape plus color · icon and text together

**Recommendation:** icon plus color.

**Consequence:** an icon is readable by someone who cannot tell red from green, and stays compact inside a narrow table cell — unlike a text label, which forces the column wider.

Color is never the only marker. That is a rule, not a preference.

---

## C. Text (9–11)

### 9. Font pairing · PRD+CSS

**Options from:** `--domain typography "<visual direction from Q1> <kind of app>"`. Take `Font Pairing Name` · `Heading Font` · `Body Font` from the top 3–4 rows. Add one option: a single sans family throughout, plus a monospace for numbers.

**Recommendation:** the row whose `Best For` includes this kind of app. For a table-heavy internal app, favor one that carries a monospace.

**Consequence:** monospace figures make currency columns align vertically, so the gap between large and small is visible without reading the digits.

Font names go into the styling files. The CSV's `Tailwind Config` column can be copied directly. Avoid serif as a default — see `anti-pattern.md`.

### 10. Number of text steps · PRD

**Options:** four steps · five · six · seven or more

**Recommendation:** five steps.

**Consequence:** five covers page title, section title, body, supporting text, and small label — and having few choices forces hierarchy to be built from size rather than from grays that get harder to read the more you add.

### 11. Maximum line length · PRD

**Options:** unbounded, follows the container · around 65 characters · around 80 · bounded for prose, unbounded in table cells

**Recommendation:** bounded for prose, unbounded in table cells.

**Consequence:** a paragraph as wide as a 27-inch screen makes the eye lose its place on the return sweep, while a table cell needs the full width so its contents are not clipped.

---

## D. Form (12–14)

### 12. Icon pack · PRD+CSS

**Options from:** `--domain icons "<kind of app> <visual direction>"`, taking the distinct values of the `Library` column, with the `Style` column (outline or solid) as the qualifier. The icon pack bundled with the component library chosen in Q0 is always among the options.

**Recommendation:** the one already installed alongside the chosen component library.

**Consequence:** choosing otherwise means one more dependency, and the library's own components keep their original icons until you replace them one by one.

**One icon family per app**, no exceptions. An icon missing from that family → report it as a finding; do not draw your own SVG and do not mix two families.

### 13. Radius scale · PRD+CSS

**Options from:** the `Design System Variables` column of the chosen style row — its `--border-radius` value becomes one option. Add: sharp (zero) · uniformly soft · tiered with a written rule.

**Recommendation:** the value from `Design System Variables`, since it is already consistent with the style chosen in Q1.

**Consequence:** one value means there is never an argument about which radius a new element takes, and no pill button strays onto a page of sharp corners.

### 14. Elevation and shadow · PRD

**Options from:** the `--shadow` value in the same column. Add: no shadow · floating elements only · soft on cards, stronger on floating elements.

**Recommendation:** follow the chosen style's `--shadow`; if it reads `none`, recommend no shadow.

**Consequence:** cards without shadow force grouping to be built from spacing and rules, which holds up better on a dense screen than a dozen floating boxes all demanding equal attention.

Shadow in use → tint it toward the background hue, never pure black.

---

## E. Space (15–18)

### 15. Density · PRD+CSS

**Options from:** the `--spacing` value in `Design System Variables`, translated into four levels: airy · standard · dense · very dense.

**Recommendation:** dense for an internal dashboard; follow the chosen style's `--spacing` otherwise.

**Consequence:** an app open all day is judged by how much is visible without scrolling — but every element gets smaller, so text contrast cannot be compromised.

→ Fills the `--density` dial.

### 16. Lowest supported screen width · PRD

**Options:** 360px · 768px · 1024px · 1280px

**Recommendation:** 360px if PRD Section 2 names a role working in the field; 1024px if every user sits at a desk.

**Consequence:** stating the lower bound explicitly means anything below it is **unsupported rather than broken** — without that statement, every "it looks wrong on my phone" report becomes work nobody ever decided to take on.

### 17. Page composition · PRD

**Options from:** the `Dashboard Style (if applicable)` column of `--domain product "<kind of app>"`, plus: fixed sidebar · collapsible sidebar · top bar only · sidebar plus top bar.

**Recommendation:** a collapsible left sidebar for a multi-role app.

**Consequence:** a sidebar absorbs a growing menu without being redesigned, and collapses when the user needs full width for a table — two things a top bar cannot do.

→ Also feeds the `--variance` dial.

### 18. Maximum content width · PRD

**Options:** unbounded, always full screen · bounded and centered · bounded for forms and prose, full width for tables

**Recommendation:** bounded for forms and prose, full width for tables.

**Consequence:** a clipped table forces horizontal scrolling that hides columns, while a form as wide as a 27-inch screen puts label and input half a desk apart.

---

## F. Data (19–22)

*Skip this entire group if the app shows no lists or tables.*

### 19. Dense table style · PRD

**Options:** a rule between every row · alternating row tint · no separators, spacing only · rules between groups only

**Recommendation:** a thin rule between every row, using the `Border` value from the chosen palette.

**Consequence:** a thin rule keeps the eye on the same row while scanning to the rightmost column, without the visual weight of alternating tints that make a long table look striped.

### 20. Table row height · PRD+CSS

**Options:** compact (~32px) · medium (~40px) · roomy (~48px) · user-adjustable

**Recommendation:** derive it from the Q15 answer — dense density → compact or medium.

**Consequence:** 40px fits a status badge and an action button inside the row without clipping, while still showing roughly twice the rows of a roomy height.

### 21. Paging or scrolling · PRD

**Options:** numbered pages · a load-more button · infinite scroll · scrolling with a sticky header row

**Recommendation:** numbered pages.

**Consequence:** paging gives the user a place they can refer to ("it's on page 3") and makes the total count visible — two things infinite scroll loses, and both come up constantly when people ask each other about data over chat.

### 22. Row actions · PRD

**Options:** action icons always visible · a three-dot menu · an icon for the primary action, a menu for the rest · revealed on row hover

**Recommendation:** an icon for the primary action, a menu for the rest.

**Consequence:** the most-used action stays one click away while rare actions stop eating column width — and nothing is hidden behind hover, which does not exist on a touch screen.

---

## G. Interaction (23–26)

### 23. Motion level · PRD

**Options from:** the `Effects & Animation` column of the chosen style row, translated into four levels: near-static · subtle (150–200ms) · moderate · rich.

**Recommendation:** follow that column; for internal apps it usually lands on subtle.

**Consequence:** short transitions explain that something opened or closed without making the user wait, while longer ones read as slow precisely to the people using the same app hundreds of times a day.

→ Fills the `--motion` dial. Any motion honors `prefers-reduced-motion`.

### 24. Reporting the result of an action · PRD

**Options:** a corner toast · inline near the element that changed · inline for failures, toast for successes · toast for everything plus inline for form errors

**Recommendation:** inline for failures, toast for successes.

**Consequence:** a failure that appears next to its cause cannot be missed and does not disappear on its own, while a success is genuinely allowed to pass by without shifting the layout.

### 25. Confirming an irreversible action · PRD

**Options:** a confirmation dialog · a dialog that requires retyping the record's name · run immediately with an undo button for a few seconds · confirmation only for permanent deletion

**Recommendation:** a confirmation dialog for anything irreversible, plus retyping the name for anything deleting many records at once.

**Consequence:** a plain dialog eventually gets clicked through unread, so the second layer is reserved for actions that genuinely have no way back.

### 26. Forms: label position and validation timing · PRD

**Options:** label above + validate on blur · label above + validate on submit · label to the left + validate on blur · label above + validate while typing

**Recommendation:** label above, validate on blur.

**Consequence:** a label above never runs out of room when the wording is long, and validating on blur reports the error before the user reaches the bottom — without scolding someone who has typed two characters.

A placeholder never replaces a label.

---

# Mapping to the `ui-ux-pro-max` dials

| Dial | Filled from |
|---|---|
| `--variance` | Q1 (visual direction) and Q17 (page composition) |
| `--motion` | Q23 |
| `--density` | Q15 |

Do not use any skill's built-in baseline. The `design-taste-frontend` baseline (8/6/4) is designed for landing pages and points the wrong way for an internal dashboard.

# What is not asked

Loading, empty state, and error placement are **not questions**. All three are fixed norms in the `ui-build` skill of `raizen-norms`, identical across every internal app.
