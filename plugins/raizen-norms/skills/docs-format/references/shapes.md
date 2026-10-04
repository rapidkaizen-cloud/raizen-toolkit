# Shapes — the files of the closed list

Write the headings named here verbatim; skills find content by them. Everything under a heading is in the user's language. File names are English, kebab-case.

## `docs/README.md` — the index

```markdown
# <App name>

<One sentence: what the app is for.>

## Living
- [product.md](product.md) — context, roles, prohibitions
- [rules.md](rules.md) — business rules and why
- [glossary.md](glossary.md) — domain terms
- [decisions/](decisions/) — one record per decision
- [guide/<task>.md](guide/<task>.md) — <the task, in the user's words>
- [whats-new.md](whats-new.md) — what users notice
- [DESIGN.md](../DESIGN.md) — the design system

## History — frozen, never current truth
- [PRD.md](PRD.md) — the app as first approved
- [changes/](changes/) — one record per big change
```

List only files that exist. Guide pages one line each; decisions and changes by their folder. Never the queue: it comes and goes with each batch.

## `docs/product.md`

```markdown
# Product — <App name>

## Context

| | |
|---|---|
| Surface | Platform: <name> — <who uses it, where> |
| Data | <what data the app holds, and where it comes from> |
| Deploy | <where it runs, for whom> |

### Proof profile

Run    : <the command that starts the app for a session>
Visual : <how a session captures visual proof>
Bounds : <the two sizes a screen is judged at>
Cases  : <how a session switches the fixture case and the role without a rebuild>
Roles  : <how a session exercises another role>
A11y   : <how a control's role and name reach the platform's accessibility tree>
Theme  : <where the styling values live, and how a session verifies one applied at runtime>

## Problem
## Success
## Non-goals
## Roles

| Role | Must be able to | Must not |
|---|---|---|

<One sentence: what happens to a user whose role is empty or unrecognised.>

## Prohibitions
```

**Context.** Three rows, no more — stack, framework, versions, and integrations are read from the repo. **The Surface row names the platform, always**: `Platform: <name>`, with `(pioneer)` appended where the platform runs ahead of the toolkit's stack rubric. A Surface row naming no platform means web.

**The Proof profile** is written for every product with a UI, and its seven labels stay verbatim. Every rule that proves something about a screen reads one of its lines instead of naming a browser, a URL, or a CSS pixel; a rule naming a browser without the line it stands in for is a finding, and so is a line left at the web's answer on a platform without a browser. The web defaults: dev server · browser screenshots at the widths `DESIGN.md`'s Layout fixes · two search params · RLS role test · semantic HTML and ARIA · computed style in the browser. Elsewhere: Bounds are the smallest supported device and the largest device class on a phone, the window minimum and a working size on a desktop binary; Cases are launch arguments or a debug-only picker; A11y is Semantics, `contentDescription`, `AutomationProperties`; Theme is the platform's own inspector. **A line not executed is written `[needs verification]`** — except the web defaults — and a skill reading one reports what it could not capture instead of claiming proof. A line names a file only once the file exists; the session-start hook reports a named path that does not.

**Problem** — two or three sentences: the state before the app and why it was intolerable. Not a feature description. **Success** — one or two sentences: the end state that measures success. **Non-goals** — what is deliberately not built, one line each with why it is a decision rather than a gap.

**Roles** — work that must be completable, never screens or permissions, which RLS and the routes hold. The closing sentence is a security decision; write it explicitly.

**Prohibitions** — what a later session would otherwise "fix" in good faith: a one-sentence principle and one sentence of reason each, no snapshot numbers. Near-empty at bootstrap, which is correct.

## `docs/rules.md`

```markdown
# Rules

## <Group>

### <Topic>
<The rule as explicit sentences — the value and what it binds.>
Why: <reason · trade-off · condition for revisiting — three sentences at most>
```

Groups as the app needs — timing and deadlines, matching and keys, approval, formulas, invariants. **No IDs and no numbering: the topic heading is the rule's name**, quoted by its test title (`logic-build` Section 10). A formula is written as a formula. An invariant is a constraint that holds whatever the implementation. A reason nobody knows is written as such — `Why: unknown — it has always been this way` — never invented.

## `docs/glossary.md`

```markdown
# Glossary

| Term | Precise meaning | Commonly misread as |
|---|---|---|
```

## `docs/decisions/NNNN-<slug>.md` — MADR, minimal

`NNNN` is the next free four-digit number.

```markdown
---
status: accepted
date: YYYY-MM-DD
---

# <The decision, as a short statement>

## Context and Problem Statement
<One to three sentences: what had to be decided, and what forced it.>

## Considered Options
- <option> — <its one-sentence consequence>

## Decision Outcome
Chosen option: "<option>", because <the reason — the part no lockfile keeps>.

### Consequences
- Good, because <…>
- Bad, because <…>
```

A superseding record names `supersedes NNNN` in its context, and the old record's status becomes `superseded by NNNN`. A library belonging to a family names it in the outcome — `TanStack Query — TanStack ecosystem` — because `design-settle` reads it. Never a version: the lockfile holds versions.

## `docs/changes/<YYYY-MM-DD>-<slug>.md`

```markdown
# <The change, as a short statement>

Opened: YYYY-MM-DD

## Why
## What changes
<The roles, pages, and data kinds it touches.>
## Documents
<The lines it writes into rules.md, glossary.md and product.md, quoted.>
## Out of scope
## Queue
<The queue lines it produced.>
```

The commit deleting its last queue line adds `Done: YYYY-MM-DD` under `Opened:` — the file's last edit.

## `docs/guide/<task>.md`

One file per piece of work a role must be able to finish (`product.md`'s Roles), named for the task — `approve-a-request.md`.

```markdown
# <The task, in the user's words>

For: <role>

1. <What the user does, naming what they see — labels exactly as the screen writes them.>

## If something goes wrong
<Each failure the user can meet, and what to do about it.>
```

No screenshots; an image goes stale without failing anything.

## `docs/whats-new.md`

```markdown
# What's new

## YYYY-MM-DD
- <What users can do or will notice, in their words.>
```

Newest first. Only what a user notices. An entry is never edited.

## `docs/PRD.md`

Its sections are `app-settle`'s (`prd-structure.md`). It opens:

```markdown
# PRD — <App name>

Frozen YYYY-MM-DD — the app as first approved. History, not current truth: the living documents are listed in docs/README.md.
```

## `README.md` at the root

```markdown
# <App name>

<Two or three sentences, from product.md's Problem and Success.>

## Run
<The Proof profile's Run line, and what it needs first — environment variables by name.>

## Documents
[docs/README.md](docs/README.md)
```
