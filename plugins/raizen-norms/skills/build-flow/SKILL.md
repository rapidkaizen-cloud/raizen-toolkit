---
name: build-flow
description: Rules for building an app page by page — the QUEUE.md queue, what one session must deliver, the order of work inside a single page, and the closed list of reasons to stop. Use before starting any page or feature, and when deciding what to build next.
---

# build-flow — one page per session

The other norms answer *"if you touch X, obey Y"*. This one answers *"what is next, and when is one unit finished"*.

## 0 — Orient before anything

A session that is going to build opens with one block, before asking anything and before touching code:

```
Usable now : Request list · Create request · Request detail
Queue left : 3 pages
Next       : Approval inbox — Approver
```

**"Usable now" is never taken from a record.** Two sources, both of them reality:

- `git log --oneline -- QUEUE.md` — every line that disappeared in a commit is one page finished, dated and tied to the commit that built it
- the routes actually present in the repo, plus live schema introspection — what actually stands right now

This is why deleting a line beats ticking one. A tick only says *somebody marked this done*. A live route plus its commit proves the page exists.

**Read the working tree as well as the history.** Commits wait for the user in this repo, so yesterday's deletion may still be uncommitted. Orientation reads `git log` **and** `git diff` — otherwise a page finished yesterday is reported as unbuilt.

## 1 — The unit is one page

One session delivers one page that can be opened and whose work its role can actually finish.

Page rather than feature, for a mechanical reason and not an aesthetic one: **one page fits in one context window, one feature is not guaranteed to.** A unit that does not fit is a unit that ends half-built.

### When the feature spreads to other pages

One test, and only one:

> *If I stop here, does any page that used to work stop working?*

**Yes → finish it in this same session.** That covers a shared column or table changing, a shared component changing its contract, a query other pages depend on, and a page that cannot be reached on its own (a detail with no list). Deferring it makes the queue lie: a line removed from `QUEUE.md` would no longer mean *usable*.

**No → it becomes a new line in `QUEUE.md`.** A page that *could* also use the new thing but works fine without it is separate work, not spread.

This test sets the size of the session. Counting pages does not.

## 2 — `QUEUE.md` is a queue, not a record

At the repo root, one copy. It holds only pages that are **not yet usable**, in build order, one line each.

```
- <page> — <role> — <the work that can be finished there>
```

Add `(needs: <page>)` only where a real dependency exists.

| Rule | |
|---|---|
| Page finished | **Delete its line.** Never tick it |
| History | `git log QUEUE.md`. One deleted line per page, tied to the commit that built it |
| File runs empty | Delete the file. Never leave an empty `QUEUE.md` |
| Status columns, checkboxes, dates | **Forbidden.** The presence of a line is the status |

The reason for that last row is the one behind `prd-format`'s ban on status: what makes a document go stale is a field somebody has to keep updating, and a shrinking queue has no such field. A tick can also be wrong — a page ticked and later broken still reads as done. A deleted line cannot lie.

`QUEUE.md` never carries PRD content. Business rules, reasons, and glossary stay in `PRD.md`. A line that needs more than one sentence of explanation is a sign the rule behind it is missing from the PRD.

The file is written in the app's own locale, like the rest of the app repo — the example below is English only because this skill is.

### Shape

```markdown
# QUEUE

Pages not yet usable, in order. A line gone means that page is usable.
History is in `git log QUEUE.md`. Do not add status, checkboxes, or dates.

- Request list — Requester — see their own requests and where each one stands
- Create request — Requester — file a new request with its attachments (needs: Request list)
- Request detail — Requester, Approver — read one request whole, with its decision history (needs: Request list)
- Approval inbox — Approver — approve or reject requests inside their authority limit
- Monthly recap — Finance — close a period and export the approved requests
- User admin — Admin — set roles and approver authority limits
```

Those three header lines stay at the top for the life of the file. They are what stops a later session from adding a status column.

## 3 — Where a queue comes from

**The queue belongs to a batch of work, not to the app.** It is born whenever pages are outstanding, deleted when none are, and **born again** for the next batch. Deleting it loses nothing: `git log QUEUE.md` follows the path, so every incarnation shows up in one history.

Three routes, chosen from the state of the repo:

**No application code yet** → build the queue from `PRD.md` Section 2 (work per role) and Section 3.

**Code present, the app was never finished** → **discovery first.** Read the routes that exist and introspect the live schema, decide which pages are already usable and which are half-built, then build the queue from what is left. A half-built page gets its own line naming **what is missing**:

```markdown
- Approval inbox — Approver — renders, but cannot reject yet and has no failed state
- Request detail — Requester — renders, but Finance can still read every row (RLS untested)
```

Once such a page is genuinely usable, its line is deleted like any other.

**The app works and the user wants something new** → the queue comes from **the request**, not from the repo. Discovery is the wrong tool here: it finds nothing missing, because nothing is missing — what is wanted has never existed. Two things come before the queue:

- **The business rules go into `PRD.md` first.** `prd-format` allows Sections 3 and 4 only *before* implementation, precisely so a rule is a decision rather than a description of code that already exists. Writing them after the pages are built inverts that.
- **Section 1 of this skill matters more than usual.** A working app has many pages that can break, so run the spread test against each one before setting the order.

All three routes end the same way: show the whole queue, **STOP**, and wait for the user's approval before writing the file. The order is agreed once, up front — that is what replaces the urge to build everything at once.

## 4 — Before touching code: collect the questions once

Read `PRD.md` and the live schema first, then ask **everything** still unclear about this page **in a single turn**.

Bundling is correct here. `app-init` asks one at a time because bootstrap answers steer each other; a page's unknowns are independent, and asking them one per turn is exactly the stop-start this skill exists to end.

Everything else is decided by you, with the defaults **announced** — a default left unspoken becomes a norm through the back door.

## 5 — The order inside one page

An extension of the chain already fixed by `db-ops` (`migration → run → introspect → types → frontend`), which owns the detail:

```
PRD rules → migration + RLS → role test → regenerate types
  → query/action → page + loading, empty, failed states → walk the flow in a browser
```

Backend first **inside one page**, never backend first across the whole app.

Loading, empty, and failed states are not follow-up work — `ui-build` already binds them to the component they belong to.

**Write this chain as a visible todo list the moment the page starts**, one entry per step above, plus one entry per spread page that passed the test in Section 1. Required, not optional: this is what lets the user see the next step at any moment without asking. The todo list dies with the session, so anything unfinished **must land as a `QUEUE.md` line** before the session closes.

## 6 — Do not stop; the list of legitimate stops is closed

Three, and the list is **closed**:

| Legitimate stop | Why it cannot be dropped |
|---|---|
| The `db-ops` destructive gate | The user approves a **number**, not an intent — lost data does not come back |
| A role test that misses | RLS fails silently; carrying on to the frontend locks the leak in |
| A business rule that is not in the PRD | Guessing it invents a norm through the back door |

Anything else: keep going until the page is usable. Report at the end, not between steps.

This does not override the `ui-build` Section 5 gate. Section 5 still `[needs verification]` → the page is not started at all, which is a refusal to begin rather than a stop in the middle.

## 7 — Too big: split, but only where nothing breaks

Splitting is always allowed. What is constrained is **where**:

> A legitimate split point is one where **every page that used to be usable still is.**

So the spread from Section 1 is never a split point — splitting there ends the session with a broken page. What may be split off is work that *adds*; what may not is work that *changes a shared contract*. No legitimate split point exists → build it whole, that is the real size of the unit.

After splitting: replace the line in `QUEUE.md` with two lines that each stand alone, finish the first, and let the rest rise to the next session. A half-built page is never left unrecorded in the queue.

## 8 — Closing the session

The closing block is not defined here. It is printed in full by `raizen-norms` at the
start of every session, under `CLOSING THE SESSION`, and it covers every session rather
than only the ones that build a page. Report it as written there.

Two of its lines exist because of this skill, and mean nothing without it:

- **Which page is usable now, and at which route.** A claim of *done* with no address
  cannot be checked.
- **Unfinished steps written as `QUEUE.md` lines, not as sentences.** A sentence in the
  transcript dies with the session; a queue line does not.

Committing the page is part of finishing it, not a separate request — see the git norms
that `raizen-norms` prints at the start of the session. Stopping for one of the three
stops in Section 6 means the opposite: leave the working tree dirty, so that the state
of the repository itself says something is waiting on the user.

## 9 — Before the app has ever shipped

**This section applies only while `main` carries nothing beyond the bootstrap commit.** In this toolkit `main` is production — `migrate-production.yml` triggers on a push to it — so anything merged there means the app has shipped at least once. Once it has, this section stops applying entirely and deploy is ordinary business.

**`QUEUE.md` is not the test for that.** A running app growing a new feature also has a queue. The queue answers *what is not built yet*; `main` answers *has this app ever shipped*. Going quiet about deploy for an app that is already live would be nonsense.

Inside a never-shipped app, the queue decides one thing only — whether it is time yet:

| `QUEUE.md` | What to do about deploy |
|---|---|
| Still has lines | **Do not raise deploy, hosting, CI, or production environment variables on your own initiative.** None of them is needed to build a page and use it locally, and an app whose RLS has not been role-tested does not belong on the internet. Bootstrap already wrote `vercel.json` and the CI workflows — inert files, simply not wired up yet |
| Gone | **Raise it, once.** Every page is usable, so this is the launch moment and the only time this skill brings deploy up by itself: name what is still unwired — hosting connection, production environment variables, CI migrations. Add that the host chosen at bootstrap may have a Claude connector automating the first of those — derived from the stack actually chosen, and worded as *may*, never as a promise that one exists. A shortcut offered, not a step required: deploying by hand works and nothing here waits on it. Then leave it to the user |

**The user asks to deploy → do it.** No lecture and no gate. One sentence naming any table whose RLS has not been role-tested, and only if such a table exists. RLS leaks are silent; nothing else will surface them.

**Commit is stated once, as a fact, in the close block** — `Uncommitted: 3 files`. Never *shall I commit?*, and never mid-session. Two reasons it is stated at all rather than dropped: uncommitted work cannot be recovered, and Section 0 orients from `git log QUEUE.md`, which an app with no commits does not have.
