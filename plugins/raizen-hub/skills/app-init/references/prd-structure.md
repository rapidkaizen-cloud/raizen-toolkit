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

A three-row table: **Surface** · **Data** · **Deploy**. Those three rows only. Stack, framework, versions, auth configuration, integration lists **are not written** — all of it is readable from the repo.

Then three blocks:

**The problem being solved** — 2–3 sentences: the real state before this app existed and why it was intolerable. Not a feature description.

**What must be achieved** — 1–2 sentences: the end state that measures success, written as a state.

**Non-goals** — deliberately not built, not a backlog. The most expensive part to lose: no query and no reading of the repo can tell anyone that something is **deliberately** absent. This is also where rejected stack alternatives go, one line each.

`logic-init` later adds its decisions to this section in the same shape: each chosen logic-layer library as one line — **choice, then a one-sentence reason** — and rejected candidates one line each among the rejected alternatives. The name is recoverable from the lockfile; the reason is the part a live check cannot bring back. Versions are never written — they belong to the lockfile, or every bump becomes a document edit.

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

At bootstrap the whole section is written as `[needs verification]`. `design-init` fills it in a separate session, from the user's answers. Do not fill it from your own taste and do not copy it from another skill.

What gets written is only **rules and scale** — how many of a thing may exist, what is forbidden. "One icon family", "at most one accent", "five text steps". The values — font name, icon pack name, radius number — live in the styling files.

Color and spacing are the exception: their roles, values, and usage rules are written here, because contrast is a norm and not an implementation detail.

Sub-sections: Visual Direction (2–3 sentences + what is deliberately not used) · Typography (number of steps + what each is for; color is not a hierarchy tool) · Spacing (base unit + permitted values) · Breakpoints & Density (including the lower bound that is not supported) · Page Composition · Color (role · value · usage rule; minimum contrast 4.5:1 for text, 3:1 for non-text; color is never the only status marker) · Reusable Components (rules, not a list) · Anti-patterns.

## Section 6 — Prohibitions

Things **deliberately** not done or not to be changed, which without this note a later session would "fix" in good faith. That is all it holds — not a list of decisions, not a history.

**Not append-only, and never written by an agent.** Adding and removing both require the user's decision.

Test before proposing, both must pass: *could a later session undo this out of ignorance?* and *is this already normative in Section 1, 3, or 5?*

Shape: a one-sentence principle, plus one sentence of reason. Zero snapshot numbers.

At bootstrap this section is usually near-empty. That is correct — prohibitions are born from mistakes that already happened, and none have happened yet.
