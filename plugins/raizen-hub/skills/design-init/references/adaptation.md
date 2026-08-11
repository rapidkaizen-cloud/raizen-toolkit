# Adaptation — answers that shift later recommendations

Two sources, used in order.

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
| Q1 = dense and technical | Q13 → sharp or slightly soft · Q14 → no shadow · Q15 → very dense · Q20 → compact · Q23 → near-static |
| Q1 = calm and neutral | Q14 → floating elements only · Q23 → subtle · Q5 → four statuses |
| Q1 = warm and friendly | Q3 → warm neutral · Q13 → uniformly soft · Q23 → subtle or moderate |
| Q1 = bold and high-contrast | Q7 → offer AAA · Q14 → no shadow, separate with rules instead |
| Q6 = dark mode included | Q4 and Q5 → only palettes whose `Dark Mode ✓` is full · Q14 → shadow is less useful on a dark ground, lean toward rules |
| Q7 = AAA | Q4 → strike accents that fail 7:1 · Q3 → higher-contrast neutrals |
| Q15 = very dense | Q10 → four or five steps, no more · Q20 → compact · Q11 → bound prose · Q22 → icon plus menu, not all icons |
| Q16 = 360px | Q17 → collapsible sidebar, not fixed · Q19 → prepare a collapsed form for tables · Q22 → nothing revealed on hover |
| Q17 = top bar only | Q18 → bounded and centered |
| Q0 brings large tables natively | Q19, Q20, Q21 → follow the library's capability, report as derived decisions |
| Q0 = a copy-in library | Q12 → its bundled icons become the recommendation |
| Q2 names one app | Every later query carries that app name as a keyword |

## When a question is skipped rather than shifted

Skip it and report it as a **derived decision** — never silently — when any of these hold:

- The shifts above leave **one** sensible option. Example: Q7 = AAA plus a palette with only one passing accent → Q4 need not be asked.
- An earlier answer already contains the answer. Example: Q0 = a library that ships its own charting system → the chart type is not asked again.
- Context makes it inapplicable. Example: an app with no tables → all of group F.

The report is one line: `Q20 row height → compact (derived from Q15 very dense)`. The user may cancel it at any time.

## The limit

Shifting a recommendation is allowed. **Removing an option is not**, unless that option is genuinely impossible — a palette that fails the requested contrast, or a library that does not support the chosen platform. An option that is merely a poorer fit still gets shown; what changes is the recommendation, not the list.

If no shift applies, use the built-in recommendation in `interview.md` as written. Do not invent relationships between answers that are not listed here.
