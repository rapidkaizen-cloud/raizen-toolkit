# Component library rubric

Feeds the interview's component-library dialog. Score the needs from PRD Sections 1–3, then assemble 3–4 options that satisfy **all** of them.

**Name no libraries in this file** — assemble candidates live. Once a library is chosen on a non-web platform, research its idioms from the platform's own documentation before building, findings labelled with their source.

## Scoring the needs

Answer six yes or no; not mentioned in the PRD means no.

| Need | How to read it from the PRD |
|---|---|
| Platform | Section 1 Surface — web, mobile, or desktop |
| Large tables | Section 3 mentions lists that could run to thousands of rows, or needs sorting, filtering, or configurable columns |
| Charts | Section 3 carries formulas or metrics that need to be seen as a trend |
| Calendar or scheduling | Section 3 carries time, shift, or deadline rules viewed per date |
| Drag-and-drop | Section 2 mentions work that reorders items or moves them between columns |
| Works offline | Section 2 names a role working without reliable connectivity |

Charts needed → the verification pass also covers which chart types suit this data and stack.

## The verification duty — candidates assembled live

1. **The model's own knowledge proposes** the libraries a working developer would name for this platform today, including those the PRD's stack or Section 1's library-family note leans toward.
2. **A verification pass checks every candidate before it is offered**: maintained, broadly adopted, no fresh supply-chain event, and **what it bundles and leaves out** against the scored needs — table with sorting and paging, charting, date picker, calendar, drag-and-drop, notifications, skeletons, icon pack. One pass covers all candidates; never recall from memory alone.

**Never show an option without verified backing**; every option states what verification found.

## Rules for assembling the options

**Offer three to four options, *own components* always one** — on every platform, whatever the score. Every library beside it satisfies every yes-need; if none does, say plainly what will not be met. Own components' consequence: everything hand-written and hand-maintained, each yes-need named as hand-written work, `ui-build`'s reuse rules binding from the first component.

**Recommendation on the web:** the option satisfying everything with the **fewest extra dependencies** — not the most complete or popular. Own components only where the needs are few enough that hand-writing is honestly cheaper; zero dependencies is not by itself fewest.

**Recommendation on every other platform: the design language outranks the dependency count**, which only separates libraries that carry it. The Platform row is a **pass mark** — whether it runs there, not whether it belongs. Each option says which OS language it carries, or none. Where no candidate carries it (common on macOS and web-hosted ecosystems), say so, fall back to the dependency count, and name what the app will not inherit; never buy a heavier dependency for a language it does not carry.

Every option's consequence names:

- **What the library leaves out** — the researched missing-list.
- **The styling system it brings** — utility CSS, a theme object, CSS-in-JS, or nothing. Nothing (*own components*, headless) → the styling dialog follows, where **Tailwind CSS is the recommendation on the web** and plain CSS always an alternative; off the web styling follows the platform. `app-settle` sets no styling default at bootstrap. Where a library's system differs from one already installed, **the collision is a decision line the user answers here** — keep the installed one and adapt the library, or replace it and say so.
- **How far the look bends** — anatomy the app can reshape (headless, copied into the repo) or bounded by the theme's slots (theme object, fixed variants), verified per candidate. A theme-bounded library gives every direction frame the same control anatomy; say so before the choice.
- **The icon pack it bundles, or that it is headless** — the interview's icon dialog reads this.

**Copy-in versus package.** A package installs faster but bends less. A copy-in library states three consequences:

- Updates do not arrive on their own — the copied version is yours to maintain.
- Copied components are **existing code** to `ui-build`, so a pattern appearing twice still triggers extraction.
- Raw colour or spacing values in the copy are **findings to report**, not a pattern to imitate.

Always accept answers outside the list: verify the named library the same way, use it, and say so if you do not know what it brings.
