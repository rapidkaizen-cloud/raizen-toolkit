# `DESIGN.md` — the design system, in Google's DESIGN.md format

Written by `design-settle` alone, at the root: YAML frontmatter tokens, then markdown sections in a fixed order. **Read the format live before writing** — `npx -p @google/design.md designmd spec --rules`; the dot-free `designmd` alias, because `design.md` as a command name collides with the Markdown file association on Windows. Never write it from memory. Where the live spec differs from this file, the spec decides the format and this file decides what goes where; report the difference. Last verified: format `alpha`, CLI 0.4.0, 2026-09-27.

Headings verbatim; prose in the user's language. **Tokens hold the values, prose holds the rules and the scale**: prose names a role and never restates a token's value.

## Tokens

- **`name`** — the app's name; **`version`** — the spec's current value.
- **`colors`** — each ramp step something reads, named on the stack's convention (Tailwind's `50 … 950`); the semantic alias layer as references to those steps (`surface: "{colors.neutral-50}"`); the chart palette. `primary` names the accent role. A second theme mode repeats the aliases with the mode as suffix (`surface-dark`), pointing into the same ramps.
- **`typography`** — one entry per text step.
- **`rounded`**, **`spacing`** — the ratified scales.
- **`components`** — one entry per component an archetype names, per variant and state (`button-primary`, `button-primary-hover`), in the spec's property set, each value a reference into the groups above. What that set cannot hold goes in the Components section's table.
- **Token names are the production token names** the styling files use (`canvas.md`), so the styling files are a copy of these tokens.
- No other top-level group. Where `impeccable`'s document reference puts a sidecar beside the file, it carries what the frontmatter cannot.

## Sections — the spec's eight, then two of the toolkit's

| Section | Holds |
|---|---|
| `## Overview` | The direction in two or three sentences · the **signature**, the single element the app is remembered by · the **reference** the picked frame was drawn toward, marked *stressed* where the user stressed it · the **copy voice** — formal, neutral, or casual, and the form of address — per page group where it was asked per group · what is deliberately not used |
| `## Colors` | The theme modes · each role's usage rule, per mode · the ramp's step count and the alias list — product code reads an alias, never a step · colour is never the only status marker |
| `## Typography` | How many steps, and what each is for; colour is not a hierarchy tool |
| `## Layout` | The spacing base and permitted values · the **desktop breakpoint** every page is judged at, and the **lowest supported width** — anything below it is unsupported rather than broken · `### Density`, the density profile table, both profiles where a role split produced two |
| `## Elevation & Depth` | How depth is conveyed, and the shadow scale where one exists |
| `## Shapes` | The radius scale and what each step is for |
| `## Components` | The **component-token table**, per component an archetype names — control height per size · input height · field padding · card padding and radius · table row height and vertical padding · header treatment · badge size and radius · modal radius · toast padding · focus ring — then the rules for reusable components, never a list of them. `build-flow` opens every page from this table and never reads the theme |
| `## Do's and Don'ts` | Only prohibitions the user ratified; may be empty — no stock list exists |
| `## Page Composition` | The shell, and the **archetype table**: per archetype its shell layout, components, density profile, empty wording, and the routes it owns — every route in exactly one archetype |
| `## Contrast` | One row per pair `ratify.md`'s Contrast defines, per theme mode: foreground, background, the computed ratio, against 4.5:1 for text and 3:1 for non-text |

The last two are the toolkit's extension sections. The format keeps an unknown section and does not check its order, so they sit after Do's and Don'ts. **Every heading appears once** — a duplicate heading makes the file invalid.

## Proven by its linter

`npx -p @google/design.md designmd lint DESIGN.md` — zero errors; every warning fixed or left standing with one line why. `orphaned-tokens` on a ramp step or an alias is expected: product code reads it, and the linter only sees the components map.

## A legacy repo

Section 5 is the source, holding this content under its own sub-sections (`docs-format`, `references/legacy.md`); the root `DESIGN.md` is generated from it — frontmatter tokens and one body line naming Section 5 as the source. The linter is not run over it.
