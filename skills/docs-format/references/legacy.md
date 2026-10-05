# The legacy form — a repo with a root `PRD.md`

Every rule of `SKILL.md` binds the section the map sends it to; this file adds only what the legacy form has and the `docs/` form does not.

## The legacy map

| A skill names | A repo with a root `PRD.md` reads |
|---|---|
| `docs/product.md` — Context, Surface, Proof profile, problem, success, non-goals | `PRD.md` Section 1 |
| `docs/product.md` — Roles | Section 2 |
| `docs/rules.md` | Section 3 |
| `docs/glossary.md` | Section 4 |
| `DESIGN.md` | Section 5. The root `DESIGN.md` there is generated from it and is never read as the design system |
| `docs/product.md` — Prohibitions | Section 6 |
| `docs/decisions/` | Section 1 — one line per `app-settle` or `logic-settle` choice, or technical choice the user took, with its reason, rejected alternatives among the non-goals. `design-settle` records none there; its library is `CLAUDE.md`'s row |
| `docs/queue.md` | `QUEUE.md` at the root |
| `docs/README.md`, `docs/guide/`, `docs/whats-new.md`, `docs/changes/`, `docs/PRD.md` | Nothing — never written in a legacy repo |

## `PRD.md`

- **Keep the shape it has.** Section 1 — a three-row table (Surface · Data · Deploy), the Proof profile under it (`shapes.md`), then problem, success, non-goals. Section 2 — `Role · Must be able to · Must not`. Section 3 — categorized sub-tables with a `Why` column: Timing & Deadlines (`Rule · Value · Why that value`), Matching/Keys (`Source · Key · Fallback`), Approval (`Action · Requires · Notes`), Formulas (`Metric · Formula`), Invariants. Section 4 — `Term · Precise meaning · Commonly misread as`. Section 5 — the design system. Section 6 — prohibitions. Cross-references use the topic name, never a section number.
- **A rule's topic is the first cell of its Section 3 row** — the name a rule test title quotes.
- **Past about 400 lines the PRD carries status, not intent.** The session-start hook says so; tell the user.
- **The session-start hook prints Sections 1, 2 and 6 only**, where all six are in shape. Read Section 3, 4 or 5 from the file, at the line range the hook names, before writing or changing anything it governs.

## Section 5 — the design system

`design-settle` alone writes it. An off-shape `PRD.md` gets Section 5 under its own heading, and nothing else in the file is touched.

**The root `DESIGN.md` of a legacy repo is generated, never a source.** `design-settle` writes it from ratified Section 5 and the styling files — frontmatter tokens to the schema `impeccable`'s document reference gives, read at write time, with any sidecar that schema puts beside it, and one body line: `Generated from PRD Section 5 and the styling files by design-settle — do not edit; Section 5 is the source.` It is regenerated whenever Section 5 changes; a hand edit, or an `impeccable` refresh from the built code, is a finding.

**Section 5 holds rules and scale; the styling files hold the values** — except colour and spacing, whose values contrast needs, and the component-token table.

**Where a skill names a `DESIGN.md` section, a legacy Section 5 reads its sub-section:**

| `DESIGN.md` | Section 5 |
|---|---|
| Overview | Visual Direction — the direction, the signature, the reference, the copy voice, what is deliberately not used |
| Colors | Color — theme modes, and per mode role · value · usage rule; ramp step count and alias list |
| Typography | Typography — number of steps, what each is for |
| Layout | Spacing, and Breakpoints & Density — base unit, permitted values, the desktop breakpoint, the unsupported lower bound, density profiles |
| Elevation & Depth, Shapes | None — shadows and radius live in the styling files and the component tokens |
| Components | Component Tokens and Reusable Components |
| Do's and Don'ts | Anti-patterns — only prohibitions the user ratified |
| Page Composition | Page Composition — the shell and the archetype table |
| Contrast | The contrast minimums in Color |

**A Section 5 of the adopted-whole shape** — a library and version adopted unmodified, an icon family, and three prohibitions: no theme file, no custom token, no override — is still normative where it exists, though none is written this way any more. It is never `[needs verification]`: the decision was made. It refuses overrides more completely than a filled Section 5, because it states no rule an override could cite. The spacing scale in use is the library's.

**An empty Section 5 has two readings.** Every line `[needs verification]` → bootstrap wrote it, and no UI was built. The section absent → the app has UI nobody decided on. `design-settle`'s audit handles both; no other skill fills either.
