# Adaptation — answers that shift later recommendations

Three sources, used in order.

## 1. `Decision_Rules` from `ui-reasoning.csv`

The row matching the product type in PRD Section 1 carries a `Decision_Rules` column holding conditional JSON, shaped like:

```
{"if_ux_focused": "prioritize-minimalism", "if_data_heavy": "add-glassmorphism"}
```

Read its conditions, match them against what is already known from the PRD and from earlier answers, then apply them to the queries of decisions not yet run. The same row also carries `Anti_Patterns` and `Severity` — the ones marked HIGH go into the Anti-patterns sub-section of Section 5.

This is the primary source. The table below only patches what it does not map.

## 2. Decision-to-decision table

`Decision_Rules` is keyed per product type and does not map decision to decision. The table below does. Decision numbers are `interview.md`'s; a shift may land on a decision's dialog or on one of its facets — the facet is named where it matters.

Apply these as **recommendation shifts**, not as answers. The user still chooses. A shift landing a size below the target size for this surface is a collision, not a shift — resolved the way `interview.md`'s row-height rule states, and reported as a derived line.

| Answer | Shifts |
|---|---|
| D1 = dense and technical | D8 → sharp or slightly soft radius, shadow on floating elements only · D9 → very dense · D11 row height → compact · D12 → near-static · D15 labels → the tightest measured bound |
| D1 = calm and neutral | D8 → soft on cards, stronger on floating elements · D12 → subtle · D5 count → four statuses |
| D1 = warm and friendly | D3 → warm neutral · D8 → uniformly soft radius · D12 → subtle or moderate |
| D1 = bold and high-contrast | D4 contrast → offer AAA · D8 → no shadow, separate with rules instead |
| D4 = dark mode included | D3 → only palettes whose `Dark Mode ✓` is full (at reconciliation or a reopened palette) · D8 → shadow is less useful on a dark ground, lean toward rules |
| D4 contrast = AAA | D3 → strike accents that fail 7:1, favor higher-contrast neutrals |
| D7 brings large tables natively | D11 → follow the library's capability, report as derived lines |
| D7 = a copy-in library | its icon facet → the bundled icons become the recommendation |
| D9 = very dense | D6 steps facet → four or five, no more · D6 line facet → bound prose · D11 row height → compact · D11 row actions → icon plus menu, not all icons · D15 supporting text → at most one sentence |
| D10 lower bound = 360px, or the narrow bound the Proof profile names (known from the PRD before the shell dialog) | D10 shell → one that hands the width back on demand, a collapsible rather than fixed sidebar on the web · D11 → prepare a collapsed form for tables, and nothing revealed on hover |
| D10 shell = top bar only | D10 content-width facet → bounded and centered |
| D2 selects reference apps | Every later query carries those app names as keywords |
| D2 references are all non-native for this platform | D7 → the recommendation follows the references' design language rather than the OS's, and the option states which OS language it drops · the canvas platform comparison names those references as its bar instead of an OS application |

## 3. What `logic-init` already installed

PRD Section 1 records the logic-layer choices, each with its family when it has one — `TanStack Query — TanStack ecosystem`. One shift follows, and it is a rule, not a list: **whenever a decision's candidates include a member of an already-installed family, that member rises to the recommendation**, provided it passes the decision's own checks. With Query in, that surfaces as TanStack Table behind decision 7 and decision 11 — but any family member behind any decision qualifies the same way. A family member no decision asks for is never offered on family grounds alone; a need outside the interview goes through `logic-init`'s "Later needs" rule instead. The same limit as everything here: the shift moves the recommendation, never removes an option, and the shift is named when recommending (`recommended also because Query is already installed`).

## When a dialog is skipped rather than shifted

Skip it and report it as a **derived line** — never silently — when any of these hold:

- The shifts above leave **one** sensible option. Example: contrast at AAA plus only one palette row whose accent passes 7:1 → the palette dialog need not be asked.
- An earlier answer already contains the answer. Example: D7 = a library that ships its own charting system → the chart type is not asked again.
- Context makes it inapplicable. Example: an app with no tables → all of decision 11.

The report is one line: `D11 row height → compact (derived from D9 very dense)`. The user may cancel it at any time.

## The limit

Shifting a recommendation is allowed. **Removing an option is not**, unless that option is genuinely impossible — a palette that fails the requested contrast, or a library that does not support the chosen platform. An option that is merely a poorer fit still gets shown; what changes is the recommendation, not the list.

If no shift applies, use the built-in recommendation in `interview.md` as written. Do not invent relationships between answers that are not listed here.
