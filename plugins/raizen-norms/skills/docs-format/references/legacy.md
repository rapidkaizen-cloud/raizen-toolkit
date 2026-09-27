# The legacy form — a repo with a root `PRD.md`

Read before editing a legacy `PRD.md`. Every rule of `SKILL.md` binds the section the map sends it to; this file adds only what the legacy form has and the new form does not.

- **`PRD.md` is one copy, at the root.** Nothing under `docs/` is ever created beside it, and nothing migrates it.
- **Keep the shape it has.** Section 1 — a three-row table (Surface · Data · Deploy), the Proof profile under it (`shapes.md`), then problem, success, non-goals. Section 2 — `Role · Must be able to · Must not`. Section 3 — categorized sub-tables with a `Why` column: Timing & Deadlines (`Rule · Value · Why that value`), Matching/Keys (`Source · Key · Fallback`), Approval (`Action · Requires · Notes`), Formulas (`Metric · Formula`), Invariants. Section 4 — `Term · Precise meaning · Commonly misread as`. Section 5 — the design system. Section 6 — prohibitions. Cross-references use the topic name, never a section number.
- **A rule's topic is the first cell of its Section 3 row** — the name a rule test title quotes.
- **Past about 400 lines the PRD carries status, not intent.** The session-start hook says so; tell the user.

## Section 5 — the design system

`design-settle` alone writes it. An off-shape `PRD.md` gets Section 5 under its own heading, and nothing else in the file is touched.

**The root `DESIGN.md` of a legacy repo is generated, never a source.** `design-settle` writes it from ratified Section 5 and the styling files — frontmatter tokens to the schema `impeccable`'s document reference gives, read at write time, with any sidecar that schema puts beside it, and one body line: `Generated from PRD Section 5 and the styling files by design-settle — do not edit; Section 5 is the source.` It is regenerated whenever Section 5 changes and never read as the design system; a hand edit, or an `impeccable` refresh from the built code, is a finding.

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
