# Frontend interview — 29 decisions, 13 asked

**The options are not written in this file.** Each question names which query to run against `ui-ux-pro-max` and which column becomes the options, so the choices follow the user's story instead of being one fixed list for every app.

Every numbered entry below is a decision that gets made. Only the entries listed under **Asked** become questions; the rest are **derived** — decided from the basis named in the split below, taking the entry's own Recommendation as the value.

One question per turn. Each still requires: **more than two options** · **one marked recommendation** · **a one-sentence consequence**. Asked through the **AskUserQuestion tool**, never as prose text — recommendation first and marked "(Recommended)"; the tool's automatic "Other" is how answers outside the options arrive. **Everything the user needs to answer lives inside the dialog** — in the question field or the option descriptions. The dialog may render without the prose around it, so a question referring to text "above" can arrive pointing at nothing.

`PRD` = the rule goes into Section 5 · `CSS` = the value goes into the styling files · `PRD+CSS` = the rule in the PRD, the number in CSS.

## Asked or derived

**Asked, in this order:** Q1 · Q2 · Q3–5 as one palette question · Q6 · Q9 · Q12 · Q13 only when the chosen library bundles no icon pack · Q16 · Q17 · Q18 · Q22 · Q23 · Q26 · Q29. Thirteen questions; fourteen when the icon-pack question opens; group F still drops entirely for an app without tables.

**Derived**, each from the basis named here:

- **From the style row chosen in Q1:** Q7 contrast (`Accessibility` column) · Q14 radius and Q15 shadow (`Design System Variables`) · Q24 motion (`Effects & Animation`)
- **From another answer:** Q13 icon pack (bundled with the Q12 library — asked instead when it bundles none) · Q20 row separators (the palette's `Border` value) · Q21 row height (from Q16 density)
- **Fixed recommendation as the default:** Q5 status count (four) · Q8 status marker (icon plus color) · Q10 text steps (five) · Q11 line length · Q19 content width · Q25 action feedback · Q27 forms
- **Q28 label length:** in `design-init`, not asked and not derived — nothing exists to measure; report one line deferring it to `design-rework`. In `design-rework` it **is asked**, with options built from the audit numbers.

A derived decision is reported on one line with its basis, exactly like the fast-mode report — never silently. The user may cancel any line, and cancelling it opens that entry as a normal question. In `design-rework`, every entry — asked or derived — defaults to the value Section 5 holds today.

## Rules for the whole interview

**The order in this file is the order the questions are asked**, in every skill that reads it. No question is moved, promoted, or asked out of sequence — a skill that reorders them produces two different interviews for the same app.

**Do not ask what is already answered.** An earlier answer or `Decision_Rules` settles a question outright → decide it, report it as a derived decision, move on. See `adaptation.md`.

**Context removes a question → skip it and say why.** An app without tables skips group F.

**Zero search results, no Python, or the skill is not installed → do not invent.** Say so plainly, then offer two paths: postpone until the skill is usable, or continue with self-assembled options that are **explicitly marked** as not coming from the database. This rule is from `ui-ux-pro-max` itself: *never present a 0-result search as if it returned data.*

Read the `search.py` command shape from the `ui-ux-pro-max` SKILL.md. Do not copy a path from here.

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

**Questions 3–5 are asked as ONE palette question.** A `--domain color` row already carries the neutral, the accent, and the destructive color together, so the options are whole rows — the top 3, each labelled with its neutral temperature and accent, plus one fixed option: follow an existing brand color. Entries 4 and 5 below supply the columns, the recommendation checks, and the consequences that go into that single question; the status **count** in entry 5 stays derived at four.

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

## D. Library & form (12–15)

### 12. Component library · PRD+CSS

**Options from:** `library-rubric.md`. Score the needs from PRD Sections 1–3 (platform · large tables · charts · calendar · drag-and-drop · offline), then assemble 3–4 libraries that satisfy all of them. Charting needs are matched against `--domain chart`.

**Recommendation:** the one that satisfies every need with the fewest extra dependencies.

**Consequence:** name what that library does **not** bring, because that is what gets written by hand later.

This answer decides what is installed, and fills the Component library row in `CLAUDE.md`. It sits here rather than at the front because the only questions depending on it — the icon pack below and group F — come after it.

**In `design-rework` it carries a second consequence:** changing the library rewrites every component whatever the tokens say, and the app's `CLAUDE.md` states the stack was locked at bootstrap. Any answer but *keep* revokes that lock rather than adjusting it.

### 13. Icon pack · PRD+CSS

**Derived when the question 12 library bundles an icon pack; asked when it bundles none** — a headless library leaves no basis to derive from, so the question opens automatically after question 12.

**Options from:** `--domain icons "<kind of app> <visual direction>"`, taking the distinct values of the `Library` column, with the `Style` column (outline or solid) as the qualifier. The icon pack bundled with the component library chosen in question 12, when there is one, is always among the options.

**Recommendation:** the one already installed alongside the chosen component library.

**Consequence:** choosing otherwise means one more dependency, and the library's own components keep their original icons until you replace them one by one.

**One icon family per app**, no exceptions. An icon missing from that family → report it as a finding; do not draw your own SVG and do not mix two families.

### 14. Radius scale · PRD+CSS

**Options from:** the `Design System Variables` column of the chosen style row — its `--border-radius` value becomes one option. Add: sharp (zero) · uniformly soft · tiered with a written rule.

**Recommendation:** the value from `Design System Variables`, since it is already consistent with the style chosen in question 1.

**Consequence:** one value means there is never an argument about which radius a new element takes, and no pill button strays onto a page of sharp corners.

### 15. Elevation and shadow · PRD

**Options from:** the `--shadow` value in the same column. Add: no shadow · floating elements only · soft on cards, stronger on floating elements.

**Recommendation:** follow the chosen style's `--shadow`; if it reads `none`, recommend no shadow.

**Consequence:** cards without shadow force grouping to be built from spacing and rules, which holds up better on a dense screen than a dozen floating boxes all demanding equal attention.

Shadow in use → tint it toward the background hue, never pure black.

---

## E. Space (16–19)

### 16. Density · PRD+CSS

**Options from:** the `--spacing` value in `Design System Variables`, translated into four levels: airy · standard · dense · very dense.

**Recommendation:** dense for an internal dashboard; follow the chosen style's `--spacing` otherwise.

**Consequence:** an app open all day is judged by how much is visible without scrolling — but every element gets smaller, so text contrast cannot be compromised.

→ Fills the `--density` dial.

### 17. Lowest supported screen width · PRD

**Options:** 360px · 768px · 1024px · 1280px

**Recommendation:** 360px if PRD Section 2 names a role working in the field; 1024px if every user sits at a desk.

**Consequence:** stating the lower bound explicitly means anything below it is **unsupported rather than broken** — without that statement, every "it looks wrong on my phone" report becomes work nobody ever decided to take on.

### 18. Page composition · PRD

**Options from:** the `Dashboard Style (if applicable)` column of `--domain product "<kind of app>"`, plus: fixed sidebar · collapsible sidebar · top bar only · sidebar plus top bar.

**Recommendation:** a collapsible left sidebar for a multi-role app.

**Consequence:** a sidebar absorbs a growing menu without being redesigned, and collapses when the user needs full width for a table — two things a top bar cannot do.

→ Also feeds the `--variance` dial.

### 19. Maximum content width · PRD

**Options:** unbounded, always full screen · bounded and centered · bounded for forms and prose, full width for tables

**Recommendation:** bounded for forms and prose, full width for tables.

**Consequence:** a clipped table forces horizontal scrolling that hides columns, while a form as wide as a 27-inch screen puts label and input half a desk apart.

---

## F. Data (20–23)

*Skip this entire group if the app shows no lists or tables.*

### 20. Dense table style · PRD

**Options:** a rule between every row · alternating row tint · no separators, spacing only · rules between groups only

**Recommendation:** a thin rule between every row, using the `Border` value from the chosen palette.

**Consequence:** a thin rule keeps the eye on the same row while scanning to the rightmost column, without the visual weight of alternating tints that make a long table look striped.

### 21. Table row height · PRD+CSS

**Options:** compact (~32px) · medium (~40px) · roomy (~48px) · user-adjustable

**Recommendation:** derive it from the question 16 answer — dense density → compact or medium.

**Consequence:** 40px fits a status badge and an action button inside the row without clipping, while still showing roughly twice the rows of a roomy height.

A row height below the minimum touch target is a collision, not a detail. Say which of the two gives way, and write the exception down where the other rule lives.

### 22. Paging or scrolling · PRD

**Options:** numbered pages · a load-more button · infinite scroll · scrolling with a sticky header row

**Recommendation:** numbered pages.

**Consequence:** paging gives the user a place they can refer to ("it's on page 3") and makes the total count visible — two things infinite scroll loses, and both come up constantly when people ask each other about data over chat.

### 23. Row actions · PRD

**Options:** action icons always visible · a three-dot menu · an icon for the primary action, a menu for the rest · revealed on row hover

**Recommendation:** an icon for the primary action, a menu for the rest.

**Consequence:** the most-used action stays one click away while rare actions stop eating column width — and nothing is hidden behind hover, which does not exist on a touch screen.

---

## G. Interaction (24–27)

### 24. Motion level · PRD

**Options from:** the `Effects & Animation` column of the chosen style row, translated into four levels: near-static · subtle (150–200ms) · moderate · rich.

**Recommendation:** follow that column; for internal apps it usually lands on subtle.

**Consequence:** short transitions explain that something opened or closed without making the user wait, while longer ones read as slow precisely to the people using the same app hundreds of times a day.

→ Fills the `--motion` dial. Any motion honors `prefers-reduced-motion`.

### 25. Reporting the result of an action · PRD

**Options:** a corner toast · inline near the element that changed · inline for failures, toast for successes · toast for everything plus inline for form errors

**Recommendation:** inline for failures, toast for successes.

**Consequence:** a failure that appears next to its cause cannot be missed and does not disappear on its own, while a success is genuinely allowed to pass by without shifting the layout.

### 26. Confirming an irreversible action · PRD

**Options:** a confirmation dialog · a dialog that requires retyping the record's name · run immediately with an undo button for a few seconds · confirmation only for permanent deletion

**Recommendation:** a confirmation dialog for anything irreversible, plus retyping the name for anything deleting many records at once.

**Consequence:** a plain dialog eventually gets clicked through unread, so the second layer is reserved for actions that genuinely have no way back.

### 27. Forms: label position and validation timing · PRD

**Options:** label above + validate on blur · label above + validate on submit · label to the left + validate on blur · label above + validate while typing

**Recommendation:** label above, validate on blur.

**Consequence:** a label above never runs out of room when the wording is long, and validating on blur reports the error before the user reaches the bottom — without scolding someone who has typed two characters.

A placeholder never replaces a label.

---

## H. Copy (28–29)

*Skip this group if the app shows no text beyond field labels.*

**These two have no database source.** A `--domain ux` search for label length or microcopy returns contrast, alt text, font size, and line length — nothing about wording. Do not run it for these two and do not present its rows as if they answered them.

The options come from one of two places instead, depending on which skill is running:

| Skill | Q28 | Q29 |
|---|---|---|
| `design-init` | Not asked — nothing exists yet to measure. Report one line deferring it to `design-rework` | Offer bounded choices and mark every one `built-in; no basis in the data` |
| `design-rework` | Asked, options built around the numbers measured in the audit | Options built around the measured counts |

**The bound is read in the on-screen language.** Take that language from the Locale row of the app's `CLAUDE.md`. A character count borrowed from English-language design guidance is wrong for any other language — "Not contacted" is 13 characters and "Belum dihubungi" is 15, and that difference repeats on nearly every label.

### 28. Repeated label length · PRD

**Options from:** measure every label that repeats once per row — status chips, table column headers, navigation items. Report the longest, the median, and how many times each repeats per screen. Build the options around those numbers: the current maximum as a ceiling, two tighter bounds, and icon-only with the text moved to `aria-label`.

**Recommendation:** the tightest bound that still fits the median, one step tighter if question 16 answered very dense.

**Consequence:** a label repeating twenty-five times down a column sets that column's width, which makes its length a layout decision rather than a wording one.

Buttons are excluded. A button appears once per screen, so cutting its words costs clarity and saves no width.

### 29. Supporting text per section · PRD

**Options from:** count the supporting paragraphs and the sentences in each. Zero paragraphs → skip the question and say why. Otherwise assemble: none at all · at most one sentence · at most two · unbounded — naming the measured maximum alongside them.

**Recommendation:** at most one sentence, and only for a section whose consequence cannot be read from its own contents.

**Consequence:** supporting text is read every time and useful once, so on a screen worked forty times a day it turns into permanent noise.

---

# Mapping to the `ui-ux-pro-max` dials

| Dial | Filled from |
|---|---|
| `--variance` | Q1 (visual direction) and Q18 (page composition) |
| `--motion` | Q24 |
| `--density` | Q16 |

Do not use any skill's built-in baseline. The `design-taste-frontend` baseline (8/6/4) is designed for landing pages and points the wrong way for an internal dashboard.

# What is not asked

Loading, empty state, and error placement are **not questions**. All three are fixed norms in the `ui-build` skill of `raizen-norms`, identical across every internal app.

Wording rules other than questions 28 and 29 are fixed there too — sentence case, active voice, no exclamation marks, and rationale kept off the screen. They do not vary per app, so asking them spends context on an answer that is already known.
