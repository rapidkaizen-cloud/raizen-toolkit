# PRD STRUCTURE — the frozen `docs/PRD.md`, and what it seeds (N4, D5)

What may be written at all, the header, and each section's shape are `docs-format`'s — its `SKILL.md` and `references/shapes.md`; this file holds what the PRD carries and which living document each section seeds. A legacy root `PRD.md` keeps its own shape (`docs-format`, `references/legacy.md`).

## Sections, in order

Headings verbatim, each section written in the shape of the living document it seeds — its inner headings one level deeper — so seeding copies it unchanged.

| Section | Holds | Seeds |
|---|---|---|
| `## Context`, `## Problem`, `## Success`, `## Non-goals`, `## Roles` | As `product.md`'s sections of the same names | `docs/product.md` |
| `## Rules` | The business rules, grouped, each with its why | `docs/rules.md` |
| `## Glossary` | The terms table | `docs/glossary.md` |
| `## Stack` | Per question answered at N2: the question, the options offered with their one-sentence consequences, the answer, its reason. Then the derived lines and the defaults not asked, one line each | `docs/decisions/` — one record per answered question |
| `## Prohibitions` | The prohibitions the user stated | `docs/product.md` |

**No design system section** (`SKILL.md`, Hard limits).

## Writing and seeding

1. **Write `docs/PRD.md`.** It is frozen from the moment it is written — the summary's approval is its approval.
2. **Seed the living documents from it in the same session** — the Seeds column, each file to `docs-format`'s shapes — then write `docs/README.md`, the index of what now exists, and `README.md` at the root. Nothing else under `docs/`.
3. **Write the Proof profile**: on a web platform, the web default as written in `docs-format`'s shapes; on a Pioneer platform, only lines actually executed are written as fact, the rest `[needs verification]`.
4. **Put rejected stack alternatives in their decision records**, as considered options with their consequences — never among the non-goals, which hold what the app deliberately does not do.

**Document mode** records the stack as found — one line per row of D1's block, each naming its file — and seeds no decision record from it: nobody chose from a list, so there were no options. Its other differences are `document.md`'s D5.
