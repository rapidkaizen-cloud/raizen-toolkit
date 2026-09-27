# PRD STRUCTURE — the frozen `docs/PRD.md`

Used when bootstrap or document mode writes `docs/PRD.md`. What may be written at all, the header, and each section's shape are `docs-format`'s — its `SKILL.md` and `references/shapes.md`; this file holds what the PRD carries and which living document each section seeds. A legacy root `PRD.md` keeps its own shape (`docs-format`, `references/legacy.md`).

## Sections, in order

Headings verbatim, each section written in the shape of the living document it seeds — its inner headings one level deeper — so seeding copies it unchanged.

| Section | Holds | Seeds |
|---|---|---|
| `## Context`, `## Problem`, `## Success`, `## Non-goals`, `## Roles` | As `product.md`'s sections of the same names | `docs/product.md` |
| `## Rules` | The business rules, grouped, each with its why | `docs/rules.md` |
| `## Glossary` | The terms table | `docs/glossary.md` |
| `## Stack` | Per question answered at N2: the question, the options offered with their one-sentence consequences, the answer, its reason. Then the derived lines and the defaults not asked, one line each | `docs/decisions/` — one record per answered question |
| `## Prohibitions` | The prohibitions the user stated | `docs/product.md` |

**No design system section.** `DESIGN.md` is `design-settle`'s, written in its own session.

**Document mode** records the stack as found — one line per row of D1's block, each naming its file — and seeds no decision record from it: nobody chose from a list, so there were no options.
