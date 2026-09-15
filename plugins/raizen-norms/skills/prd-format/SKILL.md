---
name: prd-format
description: Rules for reading and writing PRD.md — what belongs in it, which sections may be written freely, and which ones stop and wait for the user. Use before editing PRD.md, before proposing any change to it, and when deciding whether something should be recorded there at all.
---

# prd-format — maintaining PRD.md

`PRD.md` sits at the repo root, one copy.

## When to read it

When you need to know **intent**: a business rule, a prohibition, the meaning of a domain term, a design system norm.

Not when you need a **fact**. Tables, columns, routes, components, stack, and whether something is built yet are read from the code and the live database — **never from the PRD**. A PRD that answers those questions is a broken PRD; report it as a finding.

Conflict about what exists → the code wins, the PRD is corrected. Conflict about what ought to be → the PRD wins, the code is a finding.

## The single principle, before writing anything

The PRD holds only what a **live check cannot recover**. Test every sentence: *if this sentence were deleted, could reading the repo or introspecting the database bring it back?* Yes → do not write it.

**One named exception: Section 1's Surface row carries the platform, and the Proof profile under it carries how a session runs this app and captures visual proof.** Both are recoverable from the repo in principle and are written regardless, because every skill that proves a page reads them *before* it has read enough of the repo to derive them — and a session that derives the platform wrongly proves nothing while believing it did. Nothing else about the stack joins them.

**The trigger is narrow.** This document is touched only when a sentence inside it **becomes false**, or a new prohibition needs to be remembered by later sessions. **A new feature, a new screen, a new table, a new column are not triggers.** In doubt → do not write.

The PRD is not a changelog. History lives in git. Snapshot numbers are not written — they go wrong within days and nothing triggers their correction.

## What may be written freely

Correcting a sentence that **became factually false** — the most common trigger and the most often right. Plus Section 1 Context and Section 2 Roles, each on its own trigger.

## Sections 3 and 4 — allowed, with one condition

**Written BEFORE implementation, not after.**

The danger is not who types it, but the **direction**. A session that has just implemented something and then writes Business Rules tends to write a summary of the code it just produced — and that flips PRD → code into code → PRD. A rule born that way looks decided when nobody ever decided it.

Test before writing: *is this sentence a business decision, or a description of a mechanism I just built?* The latter → do not write it.

The **Why** column is at most three sentences, holding a business or empirical reason — not how it works.

A rule that appears mid-implementation without ever being discussed → **report it as a finding**, do not write it.

Section 4 is **append-only**. An old term never changes meaning; if the meaning changes, it is a new term.

## Section 5 Design System — never written by an agent

Applies to every session. **Two paths, and only two:**

| Skill | When | Its limit |
|---|---|---|
| `design-settle` | Section 5 is empty **and** no component exists yet | Writes from the user's answers, before a single line of CSS exists |
| `design-settle` | Section 5 is filled, **or** it is empty while components already exist | Writes only what the user approved one by one — an old-versus-new diff, or a ratification of what the audit measured |

**Where `PRD.md` does not exist yet, `design-settle` may create it holding Section 5 alone**, with one header line naming Sections 1–4 as `[needs verification]` and `app-settle` as their writer; where it exists in another shape, `design-settle` writes Section 5 under its own heading and touches nothing else. Section 5 is the only section a skill other than `app-settle` ever creates.

What is protected is not who types it, but the **derivation direction user → PRD → CSS**. If a session that just wrote a deviation were allowed to edit Section 5, it could legalize its own deviation and the direction collapses. Both skills above follow that direction: both start from a user decision rather than from code, and both stop for approval before writing.

The second row's empty-Section-5 case is a repo that arrived through `app-settle`'s document mode, and it does **not** bend that direction. The audit hands the user measured values; the user ratifies or overrules each one; only what is ratified becomes a line. A measurement is evidence put to the user, never a norm written by the code. Where the audit measured nothing coherent there is nothing to ratify, and the entry is asked as an ordinary question.

A session outside those two that finds Section 5 empty or deviating **may not touch it**. The correct move: stop, point the user to the right skill.

An audit that finds the code deviating is never permission to change Section 5 — it is a finding. Deviating code is not a new norm, however much of it there is.

## Section 6 Prohibitions — propose, then STOP

Adding **and** removing both stop and wait for the user's answer. Never written unprompted, however obvious the prohibition feels and even when it was born from a mistake made in this very session.

Present it whole: the prohibition sentence, its reason, and — when removing — what made it no longer apply.

**Not append-only.** A lifted prohibition is deleted, not left behind as a cancelled entry.

Test before proposing: *could a later session undo this out of ignorance?* No → do not propose it. Already normative in Section 1, 3, or 5 → that is where it belongs; this section takes no copies.

## Restructuring — allowed, but STOP first

Adding or removing a section, moving content between sections, changing a table's shape: state what changes and why, then wait for the user's answer.

Not out of incapacity, but because structure changed without deliberation produces a thin PRD — and thin is more dangerous than absent: it looks like the thing was recorded.

## Shape prohibitions

Zero status fields. No checkmarks, no progress column, no "not tested yet" — without exception.

No technical identifiers. Name the concept; Section 4 is the bridge.

Environment variables: names only, never values.
