# PRD STRUCTURE — shape spec

Used when writing `PRD.md` from scratch. For maintaining an existing PRD, the authority rules live in the `prd-format` skill of `raizen-norms`.

## Single principle

The PRD holds only what a **live check cannot recover**. Test every sentence: *if this sentence were deleted, could reading the repo or introspecting the database bring it back?* Yes → do not write it.

## Six sentence shapes that make a document go stale fast

| Cause | Its opposite |
|---|---|
| Enumeration (a list that has to stay complete) | Write the criterion, not the list |
| Status (progress, checkmarks, "not tested yet") | Zero status fields, no exceptions |
| State description ("the system records X in Y") | Write the constraint ("no X without Y") |
| Technical identifiers (table · column · route · component · file) | Name the concept; Section 4 is the bridge |
| Snapshot numbers ("measured N rows at present") | A number is allowed only when it is the reason behind a rule's value |
| Change history | The PRD holds the present. History lives in git |

Header: `# PRD — [App Name]`, then `**Version:** 1 · [Date]`.

Cross-references between sections use the topic name, not a numeric ID.

## Section 1 — Context

A three-row table: **Surface** · **Data** · **Deploy**. Those three rows only. Stack, framework, versions, auth configuration, integration lists **are not written** — all of it is readable from the repo. **The Surface row names the platform, always** — `Platform: <name>`, with `(pioneer)` appended where the platform runs ahead of the toolkit's templates. Written for every platform including web, because the skills downstream read it to decide what a page is proven on and which vocabulary its options are drawn from. **A Surface row naming no platform means web** — that reading is fixed rather than inferred, so every PRD written before this rule stays correct and no repo becomes ambiguous by being old.

Below the table, when the product has a UI, one block the table cannot carry — the **Proof profile**, seven lines:

```
Run    : <the command that starts the app for a session>
Visual : <how a session captures visual proof — browser screenshot, simulator screenshot, window capture>
Bounds : <the two sizes a screen is judged at — two widths on the web · the smallest supported device and
         the largest device class on a phone · the window minimum and a working size in a desktop binary>
Cases  : <how a session switches the fixture case and the role without a rebuild — two search params on the
         web · launch arguments or a debug-only picker elsewhere>
Roles  : <how a session exercises another role — RLS role test, or the platform's equivalent>
A11y   : <how a control's role and name reach the platform's accessibility tree — semantic HTML and ARIA on
         the web · Semantics, contentDescription, AutomationProperties elsewhere>
Theme  : <where the styling values live, and how a session verifies one actually applied at runtime —
         computed style in the browser · the platform's own inspector elsewhere>
```

**This block is the toolkit's whole answer to "which platform is this".** Every rule that proves something about a screen reads one of these lines instead of naming a browser, a URL, or a CSS pixel — the rule states what must be true, the profile states how this app shows it. A rule naming a browser without naming the line it stands in for is a finding, and so is a profile line left as the web's answer on a platform that has no browser.

It exists because `build-flow` and the design skills must prove pages on every platform, and "screenshot the browser" is only the web's answer. On the web stack every line has a known default — dev server · browser screenshots at the widths Section 5 fixes · two search params · RLS role test · semantic HTML and ARIA · computed style — and the block is still written, so no later session has to assume it. A line that was not executed at bootstrap is written `[needs verification]` — except the web default, which the templates have already proven — and the skills that read it report what they could not capture instead of claiming proof.

Then three blocks:

**The problem being solved** — 2–3 sentences: the real state before this app existed and why it was intolerable. Not a feature description.

**What must be achieved** — 1–2 sentences: the end state that measures success, written as a state.

**Non-goals** — deliberately not built, not a backlog. The most expensive part to lose: no query and no reading of the repo can tell anyone that something is **deliberately** absent. This is also where rejected stack alternatives go, one line each.

`logic-settle` later adds its decisions to this section in the same shape: each chosen logic-layer library as one line — **choice, then a one-sentence reason** — and rejected candidates one line each among the rejected alternatives. The name is recoverable from the lockfile; the reason is the part a live check cannot bring back. Versions are never written — they belong to the lockfile, or every bump becomes a document edit.

## Section 2 — Roles & Responsibilities

Written as **work that must be completable**, not as a list of screens or permissions. Screens change with every feature; responsibility does not.

Table: `Role` · `Must be able to` · `Must not`. A role-by-screen matrix and per-table permissions are not written — that is RLS, read live.

Close with the behavior when a role is empty or unrecognized. Write it explicitly; this is a security decision that is easy to "fix" wrongly.

## Section 3 — Business Rules

The core of the document. In code these rules scatter as constants, conditions, and RLS predicates in different places. A live check can find the numbers, but can never reconstruct the reasons.

The **Why** column is at most three sentences, in order: reason · trade-off · the condition for revisiting, if any. Anything that does not fit in three sentences is not a reason, it is a post-mortem.

Categorized sub-tables, drop the irrelevant ones: Timing & Deadlines (`Rule · Value · Why that value`) · Matching/Keys (`Source · Key · Fallback`) · Approval (`Action · Requires · Notes`) · Formulas (`Metric · Formula`) · Invariants (constraints that must hold true regardless of implementation).

## Section 4 — Domain Glossary

Introspection gives structure; it never gives meaning.

**Append-only.** An old term never changes meaning — if the meaning changes, it is a new term.

Table: `Term` · `Precise meaning` · `Commonly misread as`.

## Section 5 — Design System *(delete entirely for a product without UI)*

**Normative, not descriptive.** Sections 1–4 describe the system that exists; this one prescribes. A repo that deviates is a finding, not a new norm. The derivation direction is permanently **PRD → CSS**.

What this section looks like when the PRD is first written, and which skill fills it later, depends on which skill wrote the PRD:

| Written by | Section 5 at the end of that session | Filled later by |
|---|---|---|
| bootstrap mode | Present, every line `[needs verification]` | `design-init`, from the user's answers, before any component exists |
| document mode | **Absent entirely**, with one line naming the skill that fills it | `design-rework`, on its ratify path |

The difference is not cosmetic. `[needs verification]` says *a decision is pending in a repo where nothing has been built yet*; an absent section says *this app has UI that nobody ever decided on*. `ui-build` routes on exactly that distinction, and a documented repo handed `[needs verification]` would be sent to `design-init`, which refuses a repo that already has components.

Either way: do not fill it from your own taste, and do not copy it from another skill.

What gets written is only **rules and scale** — how many of a thing may exist, what is forbidden — phrased from what the user actually ratified, never from a stock phrasing. The values — font name, icon pack name, radius number — live in the styling files.

Two exceptions carry values, and both for the same reason — a later session reads this section and never opens the theme file. **Color and spacing**, because contrast is a norm rather than an implementation detail. **Component tokens**, because `build-flow` Section 4 opens every later page from here: a scale alone guarantees drift, since two sessions given `radius: sm 4 · md 6 · lg 8 · xl 12` will pick differently for a card and neither is wrong against the scale.

Sub-sections: Visual Direction (2–3 sentences + the **signature**, the single element this app is remembered by + the **reference** it was designed toward, where one was named + what is deliberately not used) · Typography (number of steps + what each is for; color is not a hierarchy tool) · Spacing (base unit + permitted values) · Breakpoints & Density (including the lower bound that is not supported) · Page Composition (the shell, plus the screen archetype table: per archetype one row naming its shell layout, components, density profile, empty/loading wording, and the routes it owns — every route lands in exactly one archetype) · Color (role · value · usage rule; the ramp's step count and the **semantic alias list**, since product code reads a role and never a numbered step; minimum contrast 4.5:1 for text, 3:1 for non-text; color is never the only status marker) · Component Tokens (one row per component an archetype names, carrying its own numbers — control height per size, input height, field padding, card padding and radius, table row height, badge size and radius, modal radius, focus ring) · Reusable Components (rules, not a list — the numbers live in the row above) · Anti-patterns (only prohibitions the user ratified; may be empty — no stock list exists to copy from).

### A legacy shape: an app that adopted its library whole

An older Section 5 may hold only the decision itself: a library and version adopted unmodified, an icon family, and three prohibitions — no theme file, no custom token, no override. That shape came from a `design-init` mode since retired; no new Section 5 is written this way, but the shape stays normative where it already exists, and the sub-sections above have nothing to hold there — the spacing scale in use is the library's.

Two things hold for it. It is **never `[needs verification]`**: the decision was made, and marking it pending stops `ui-build` on a question the user already answered. And it is **not a weaker Section 5** — stating no rule that an override could cite, it refuses overrides more completely than a filled one does. Reworking such an app is `design-rework`, which reads this shape on its audit.

Everything else on this page still binds, including that changing it later is the user's decision and never an agent's.

## Section 6 — Prohibitions

Things **deliberately** not done or not to be changed, which without this note a later session would "fix" in good faith. That is all it holds — not a list of decisions, not a history.

**Not append-only, and never written by an agent.** Adding and removing both require the user's decision.

Test before proposing, both must pass: *could a later session undo this out of ignorance?* and *is this already normative in Section 1, 3, or 5?*

Shape: a one-sentence principle, plus one sentence of reason. Zero snapshot numbers.

At bootstrap this section is usually near-empty. That is correct — prohibitions are born from mistakes that already happened, and none have happened yet.
