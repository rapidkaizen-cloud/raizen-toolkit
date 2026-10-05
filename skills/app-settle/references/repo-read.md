# Reading the repo — D1 and R1, the subagent's brief

**Run by one subagent** (`SKILL.md`, What a run costs), handed this file, the repo root, and the mode. Everything here is read from the repo, never asked. **Return only the blocks below, filled** — no file contents, no commentary.

## The STACK block — both modes

```
STACK — read from the repo
Framework     : [name · version — from which file]
Language      : [and whether types are enforced]
Surface       : [platform — web / desktop / mobile, and the files that decided it · then
                server routes or static SPA where it is web]
Database      : [name · how it is reached · migrations present or not]
Hosting       : [from config present, or "not readable"]
Auth          : [library or service / handwritten / none found]
Logic layer   : [the six of logic-settle — cache · validator · dates · errors · jobs · attribution, each named or "none"]
UI components : [file count] · [library · version, or "none"]
Styling       : [tokens defined / raw values only]
Tests         : [runner · how many files, or "none"]
Locale in UI  : [language · date format · separators, from the strings actually rendered]
```

- **Every row names where it was read from** — a row nobody can trace back to a file is a guess.
- **A row that cannot be read is written `not readable`**, never guessed.
- **Measure the Locale row from the strings actually rendered.**

## Document mode — what the code already answers

Return three lists, each line with the `file:line` it was read from, as `rls/approvals.sql:14`:

- **Roles** — from the auth tables and the RLS policies.
- **Rule values** — from constraints, RLS predicates, and constants. The value only: a reason is never read from code.
- **Terms** — from table and column names.

Then the routes and the tables by name, one line each — what the session's reading may draw on.

## Rework mode — the drift

Read the documents for the intent — the living documents in the `docs/` form, `PRD.md` in the legacy form — and the repo for the reality. Put the two side by side and return the drift, one line per mismatch:

```
DRIFT — documents say · code does
[document: claim]  : [what the code actually does — file:line]
[in no document]   : [something load-bearing the code does that no document covers]
```

No drift found → one line saying so. Report a mismatch, never fix it in either direction.
