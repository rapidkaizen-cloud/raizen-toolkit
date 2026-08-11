# Component library rubric

Used in question 12. Score the needs from PRD Sections 1–3, then assemble 3–4 libraries that satisfy **all** of them.

`ui-ux-pro-max` has no data for choosing a library — its `stacks/` folder holds guidance **for** a library already chosen, not a way to choose one. So this rubric lives here and you maintain it.

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

Charts needed → run `--domain chart "<data kind> <stack>"` to learn which chart types and which charting library suit that stack. Its output feeds the options.

## Needs → library map

The **Bundled** column is what arrives with no extra dependency. The **Needs extra** column is what must be installed separately — that is what gets named as the consequence to the user.

### Web

| Library | Bundled | Needs extra |
|---|---|---|
| shadcn/ui | alert · toast (sonner) · skeleton · chart (Recharts) · table · dialog · form | large tables: TanStack Table · full calendar · drag-and-drop |
| Mantine | all of the above · table with sorting and paging · date picker · notifications | heavy charting · drag-and-drop |
| MUI | all of the above · basic Data Grid | paid Data Grid for configurable columns · charting |
| Chakra UI | alert · toast · skeleton · form | tables · charts · calendar · drag-and-drop |
| Own components | nothing | everything |

### Mobile

| Library | Bundled | Needs extra |
|---|---|---|
| React Native Paper | alert · snackbar · basic skeleton · form | charts · tables · calendar |
| Tamagui | shared primitives across web and native · animation | charts · tables · calendar |
| Flutter Material | nearly everything, including basic charts and calendar | large tables |

### Desktop

Follow the stacks available in the `data/stacks/` folder of `ui-ux-pro-max` — WPF, WinUI, Avalonia, Uno, and JavaFX each carry their own guidance there.

## Rules for assembling the options

**Three to four options**, all satisfying every need scored yes. A library that fails on one need does not make the list — unless nothing satisfies all of them, in which case say plainly what will not be met.

**Recommendation:** the one that satisfies everything with the **fewest extra dependencies**. Not the most complete, not the most popular.

**The consequence must name the Needs extra column.** The user is entitled to know what will have to be installed or hand-written before they choose.

**Copy-in versus package.** A packaged library installs faster but bends less when you need something it does not provide. A library that copies code into the repo carries three consequences that must be stated:

- Updates do not arrive on their own — the copied version is the version you maintain.
- Copied components are **existing code** from `ui-build`'s point of view, so a pattern appearing a second time still triggers extraction.
- Raw color or spacing values that came along with the copy are **findings to report**, not a pattern to imitate.

Answers outside the list are always accepted. The user names a library not listed here → use it, and if you do not know what it brings, say so.
