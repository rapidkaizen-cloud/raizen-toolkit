# Adaptation — answers that shift later recommendations

Three sources, used in order.

## 1. `Decision_Rules` from `ui-reasoning.csv`

The row matching the product type in PRD Section 1 carries a `Decision_Rules` column holding conditional JSON, shaped like:

```
{"if_ux_focused": "prioritize-minimalism", "if_data_heavy": "add-glassmorphism"}
```

Read its conditions, match them against what is already known from the PRD and from earlier answers, then apply them to the queries of questions not yet run. The same row also carries `Anti_Patterns` and `Severity` — the ones marked HIGH go into the Anti-patterns sub-section of Section 5.

This is the primary source. The table below only patches what it does not map.

## 2. Question-to-question table

`Decision_Rules` is keyed per product type and does not map question to question. The table below does.

Apply these as **recommendation shifts**, not as answers. The user still chooses.

| Answer | Shifts |
|---|---|
| Q1 = dense and technical | Q14 → sharp or slightly soft · Q15 → floating elements only · Q16 → very dense · Q21 → compact · Q24 → near-static · Q28 → the tightest measured bound |
| Q1 = calm and neutral | Q15 → soft on cards, stronger on floating elements · Q24 → subtle · Q5 → four statuses |
| Q1 = warm and friendly | Q3 → warm neutral · Q14 → uniformly soft · Q24 → subtle or moderate |
| Q1 = bold and high-contrast | Q7 → offer AAA · Q15 → no shadow, separate with rules instead |
| Q6 = dark mode included | Q4 and Q5 → only palettes whose `Dark Mode ✓` is full · Q15 → shadow is less useful on a dark ground, lean toward rules |
| Q7 = AAA | Q4 → strike accents that fail 7:1 · Q3 → higher-contrast neutrals |
| Q12 brings large tables natively | Q20, Q21, Q22 → follow the library's capability, report as derived decisions |
| Q12 = a copy-in library | Q13 → its bundled icons become the recommendation |
| Q16 = very dense | Q10 → four or five steps, no more · Q21 → compact · Q11 → bound prose · Q23 → icon plus menu, not all icons · Q29 → at most one sentence |
| Q17 = 360px | Q18 → collapsible sidebar, not fixed · Q20 → prepare a collapsed form for tables · Q23 → nothing revealed on hover |
| Q18 = top bar only | Q19 → bounded and centered |
| Q2 selects reference apps | Every later query carries those app names as keywords |

## 3. What `logic-init` already installed

PRD Section 1 records the logic-layer choices, each with its family when it has one — `TanStack Query — TanStack ecosystem`. One shift follows, and it is a rule, not a list: **whenever a question's candidates include a member of an already-installed family, that member rises to the recommendation**, provided it passes the question's own checks. With Query in, that surfaces as TanStack Table behind Q12 and group F — but any family member behind any question qualifies the same way. A family member no question asks for is never offered on family grounds alone; a need outside the interview goes through `logic-init`'s "Later needs" rule instead. The same limit as everything here: the shift moves the recommendation, never removes an option, and the shift is named when recommending (`recommended also because Query is already installed`).

## When a question is skipped rather than shifted

Skip it and report it as a **derived decision** — never silently — when any of these hold:

- The shifts above leave **one** sensible option. Example: Q7 = AAA plus a palette with only one passing accent → Q4 need not be asked.
- An earlier answer already contains the answer. Example: Q12 = a library that ships its own charting system → the chart type is not asked again.
- Context makes it inapplicable. Example: an app with no tables → all of group F.

The report is one line: `Q21 row height → compact (derived from Q16 very dense)`. The user may cancel it at any time.

## The limit

Shifting a recommendation is allowed. **Removing an option is not**, unless that option is genuinely impossible — a palette that fails the requested contrast, or a library that does not support the chosen platform. An option that is merely a poorer fit still gets shown; what changes is the recommendation, not the list.

If no shift applies, use the built-in recommendation in `interview.md` as written. Do not invent relationships between answers that are not listed here.
