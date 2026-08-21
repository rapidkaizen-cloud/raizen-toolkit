# Component library rubric

Used in decision 7. Score the needs from PRD Sections 1–3, then assemble 3–4 libraries that satisfy **all** of them.

`ui-ux-pro-max` has no data for choosing a library — its `stacks/` folder holds guidance **for** a library already chosen, not a way to choose one. **And this file names no libraries either**: it holds the scoring, the assembly rules, and the research duty; the candidates are assembled live. A needs-to-library map written here goes stale the moment the ecosystem moves, and then anchors every interview to a list nobody re-checked.

## Scoring the needs

Read the PRD and answer these six yes or no. Not mentioned in the PRD means no.

| Need | How to read it from the PRD |
|---|---|
| Platform | Section 1 Surface — web, mobile, or desktop |
| Large tables | Section 3 mentions lists that could run to thousands of rows, or needs sorting, filtering, or configurable columns |
| Charts | Section 3 carries formulas or metrics that need to be seen as a trend |
| Calendar or scheduling | Section 3 carries time, shift, or deadline rules viewed per date |
| Drag-and-drop | Section 2 mentions work that reorders items or moves them between columns |
| Works offline | Section 2 names a role working without reliable connectivity |

Charts needed → run `--domain chart "<data kind> <stack>"` to learn which chart types suit that stack. Its output feeds the options.

## The research duty — candidates assembled live

Candidates come from two layers, and both are mandatory:

1. **The model's own knowledge proposes** — the component libraries a working developer would name for this platform today, including the ones the PRD's stack or Section 1's library-family note already leans toward.
2. **The research pass verifies every candidate before it may be offered.** Per candidate: maintained, broadly adopted, no fresh supply-chain event — and, against the scored needs, **what it bundles and what it leaves out**: table with sorting and paging, charting, date picker, calendar, drag-and-drop, notifications, skeletons, and the icon pack it ships or does not ship. That bundled-versus-missing pair is the option's consequence, and it is researched per candidate, never recalled from memory alone. The pass `interview.md` already mandates covers this; what is mandatory is coverage per option, never one search per option.

**An option without researched backing is not shown.** Every option carries its source label like every interview option.

For desktop stacks, the `data/stacks/` folder of `ui-ux-pro-max` carries per-stack guidance — read it alongside the research, not instead of it.

## Rules for assembling the options

**Three to four options**, all satisfying every need scored yes. A library that fails on one need does not make the list — unless nothing satisfies all of them, in which case say plainly what will not be met. "Own components" — no library at all — is offered when the needs are few enough that it is honest, with its consequence stated: everything is hand-written and hand-maintained.

**Recommendation:** the one that satisfies everything with the **fewest extra dependencies**. Not the most complete, not the most popular.

**The consequence must name what the library leaves out.** The user is entitled to know what will have to be installed or hand-written before they choose — that is the researched missing-list, stated per option.

**Each option names the icon pack it bundles, or names itself headless** — `interview.md` decision 7's icon facet reads this.

**Copy-in versus package.** A packaged library installs faster but bends less when you need something it does not provide. A library that copies code into the repo carries three consequences that must be stated:

- Updates do not arrive on their own — the copied version is the version you maintain.
- Copied components are **existing code** from `ui-build`'s point of view, so a pattern appearing a second time still triggers extraction.
- Raw color or spacing values that came along with the copy are **findings to report**, not a pattern to imitate.

Answers outside the list are always accepted. The user names a library the research did not surface → verify it the same way, use it, and if you do not know what it brings, say so.
