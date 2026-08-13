---
name: build-flow
description: Rules for building an app — the QUEUE.md queue, how much one session delivers, proposing what a page holds before it is built, the UI and backend batches, the order of work inside one page, and the closed list of reasons to stop. Use before starting any page or feature, and when deciding what to build next.
---

# build-flow — what is next, and when a unit is finished

The other norms answer *"if you touch X, obey Y"*. This one answers *"what is next, and when is one unit finished"*.

## 0 — Orient before anything

A session that is going to build opens with one block, before asking anything and before touching code:

```
Batch      : UI
Usable now : Request list · Create request · Request detail
Queue left : 3 lines
Next       : Approval inbox — Approver
```

The `Batch` line names which batch is running, and therefore what *usable* means in this session — Section 2 holds the definition. An app that never split its work runs a single batch and the line says so.

**"Usable now" is never taken from a record.** Two sources, both of them reality:

- `git log --oneline -- QUEUE.md` — every line that disappeared in a commit is one line finished, dated and tied to the commit that built it
- the routes actually present in the repo — plus live schema introspection in a backend batch, and the contract files in a UI batch, where no schema exists yet

This is why deleting a line beats ticking one. A tick only says *somebody marked this done*. A live route plus its commit proves the page exists.

**Read the working tree as well as the history.** Commits wait for the user in this repo, so yesterday's deletion may still be uncommitted. Orientation reads `git log` **and** `git diff` — otherwise a page finished yesterday is reported as unbuilt.

## 1 — The unit is what fits in one context window

One session delivers pages that can be opened and whose work their role can actually finish.

Page rather than feature, for a mechanical reason and not an aesthetic one: **a page is bounded and a feature is not.** A unit that does not fit is a unit that ends half-built.

How many pages fit depends on what one page costs in the batch that is running:

| Batch | What one page carries | Pages per session |
|---|---|---|
| Backend | migration · RLS · role test · types · query · wiring | One |
| UI | contract · fixtures · the page and its states | As many as fit |

The bound is the window, never a number. A UI page carries none of the backend chain, so several of them fit where one full-stack page did — and taking several at once is what makes the shell, the table pattern, and the wording of the empty states **one decision rather than one decision per session.** A decision taken again in a later session drifts, and that drift is what produces one screen built lavishly and its neighbour built bare.

Order inside the session still matters: the pages that establish a pattern go first — the shell and navigation, one table page, one form page — and the rest reuse them.

Taking several pages at once is only safe because a finished line is deleted the moment it is finished (Section 2). A session that dies on the third page has already recorded the first two.

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
| Line finished | **Delete it at that moment**, not at the end of the session. Never tick it |
| What a line may be | A page, or a step inside one — provided it passes the Section 7 test |
| History | `git log QUEUE.md`. One deleted line per line finished, tied to the commit that built it |
| File runs empty | Delete the file. Never leave an empty `QUEUE.md` |
| Status columns, checkboxes, dates | **Forbidden.** The presence of a line is the status |

The reason for that last row is the one behind `prd-format`'s ban on status: what makes a document go stale is a field somebody has to keep updating, and a shrinking queue has no such field. A tick can also be wrong — a page ticked and later broken still reads as done. A deleted line cannot lie.

**Deleted when finished, not when the session closes.** Deletions saved up for the end are written about work nobody is looking at any more, and the temptation is to clear a line that is close enough. Deleted at the moment the work is finished, the deletion is a claim that is true at the instant it is written. It also survives a session that dies early, because Section 0 orients from the working tree as well as the history.

**A line may be finer than a page**, and Section 7 already holds the test — a legitimate line is one whose deletion leaves every page that used to work still working. A contract and its fixtures pass it. So does a drill-down the page works fine without. What fails it is anything that changes something already standing: a shared column, a component's contract, a table's pagination.

A step that fails the test is not a queue line — it is an entry in the session's todo list (Section 5). The difference is what each one survives: **the queue outlives the session, the todo list dies with it.** A step that fails the test and is left half-done disappears without a trace, and that is precisely why it may not stand alone in the queue.

`QUEUE.md` never carries PRD content. Business rules, reasons, and glossary stay in `PRD.md`. A line that needs more than one sentence of explanation is a sign the rule behind it is missing from the PRD.

The file is written in the app's own locale, like the rest of the app repo — the example below is English only because this skill is.

### Shape

The three header lines name the batch and what *usable* means inside it. They stay at the top for the life of the file: they are what stops a later session from adding a status column, and what stops the next session from reading a UI batch as though it were a backend one.

A backend batch, and any app that never split its work:

```markdown
# QUEUE

Pages not yet usable, in order. A line gone means that page is usable — deleted
the moment it was. History is in `git log QUEUE.md`. Do not add status,
checkboxes, or dates.

- Request list — Requester — see their own requests and where each one stands
- Create request — Requester — file a new request with its attachments (needs: Request list)
- Request detail — Requester, Approver — read one request whole, with its decision history (needs: Request list)
- Approval inbox — Approver — approve or reject requests inside their authority limit
- Monthly recap — Finance — close a period and export the approved requests
- User admin — Admin — set roles and approver authority limits
```

A UI batch, where *usable* is a narrower claim and the contracts are lines of their own:

```markdown
# QUEUE — UI

Pages whose UI is not accepted yet, in order. A line gone means that work is
finished — deleted the moment it was. History is in `git log QUEUE.md`.
Do not add status, checkboxes, or dates.

- Contract + fixtures: request list — six cases, rows copied from the file this app replaces
- Request list — Requester — see their own requests and where each one stands
- Create request — Requester — file a new request with its attachments (needs: Request list)
- Contract + fixtures: approval inbox
- Approval inbox — Approver — approve or reject requests inside their authority limit
```

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

### Splitting the work into a UI batch and a backend batch

A batch may deliver **UI only** — every page built against a hand-written contract and its fixtures, with no database behind it. The backend batch follows and wires them.

**A new app is built this way: UI batch first, then backend.** Revising a page is cheap while nothing is wired behind it and expensive once a migration, RLS, generated types and a query stand behind it — and a first app is revised most, because the requirement is at its vaguest exactly when the first screens appear. Building every screen first also lets them be judged together, which is the only way a page that answers too little shows up at all: alone it looks finished, beside its neighbours it does not.

**An app that already runs splits only when the split pays.** Either condition is enough:

- **Three or more new pages at once** — enough for a pattern decided once to be worth deciding once
- **A requirement still vague** — the content of the pages is not known yet, so revisions are certain

Below that, one batch and full-stack per page. A single UI-only page dropped into an app where everything else is wired is a half-dead page, easy to forget and easy to mistake for a finished one.

**The UI queue running empty is the freeze.** The commit that deletes the file is the moment the contracts stop moving, dated in `git log QUEUE.md` — no separate mechanism, no ceremony. After the freeze a contract may still change, but as a stated decision: the page it belongs to goes back into the queue.

**Contracts are never retrofitted.** A page that already has a real query has a real data shape; writing a contract for it is work with no result. Contracts are born only for pages built in a UI batch.

## 4 — Before touching code: propose the content, collect the questions once

**What a page holds is decided before it is built, never discovered afterwards as a shortfall.** A page built to satisfy one sentence of queue line satisfies that sentence and stops. What it leaves behind is a screen that renders and answers almost nothing — and that failure is invisible, because a page that renders looks finished.

This step runs for **any page entering the queue**, new or long since built. A page that already exists brings more to work with, not less: what it shows now is on screen, so the proposal takes the shape of *what is missing from this page* rather than a list assembled from nothing.

### The proposal opens by naming the archetype

PRD Section 5's Page Composition holds the screen archetype table. **The page being proposed names which archetype it belongs to**, and that archetype's shell layout, components, and density profile are the skeleton the two lists below hang on. This is what makes a bare page impossible to propose by accident: the archetype already carries the filter bar, the summary row, or the stepper before a single optional item is weighed.

**No archetype fits → that is the first of the bundled questions below**, put to the user in the same single turn: either a new archetype enters Section 5 — a user decision, like any Section 5 change — or the page is reshaped to fit an existing one. A bespoke layout invented silently is how the archetype table dies one page at a time.

**Section 5 has no archetype table** (the app predates the rule) → the proposal still runs on the two derived lists alone, and the missing table is reported as a finding pointing at `design-rework`, which retrofits it.

### The two lists are derived, never invented

**Bound** — taken from PRD Sections 2 and 3, and not a choice. Presented as a statement, not a checkbox.

Business rules carry screen content inside them, and it is routinely never harvested. An invariant demanding a reconciliation is demanding a figure on screen. A rule saying an unregistered code still appears, marked, is describing a row and its marker. *Every figure can be traced back to the transactions behind it* is a drill-down. None of that reads as content until somebody reads it as content, which is what this step is.

Unchecking one of these means changing the PRD. That is a separate decision and it is the user's.

**Optional** — everything else that fits. Presented as a multi-select with **every item already selected**; the user removes what is not wanted.

Pre-selected is the whole point of the step. The old bias builds the minimum that passes; this one proposes the full page and lets the user cut it down. Thin pages are born of the first bias, and no later check recovers what was never proposed.

Where the PRD runs out, optional candidates come first from the components of the page's archetype in Section 5, then from the product-type database `design-init` already queries live. Same sources the app was designed from, no new one.

**Both lists coming out short is an answer, not a problem.** Login screens and small settings pages are legitimately quiet, and padding them is worse than leaving them alone. The lists are derived, so a sparse page produces sparse lists by itself — no separate judgement about whether emptiness is acceptable, and none invented on the user's behalf.

### How full is full enough

The reference page `design-init` built is the bar. It was deliberately built rich — summary cards, filters, badges — because a bare table proves nothing about density. Every later page is judged against it, and a page far emptier than it is a page to go back to, not a new norm.

**The tested widths are fixed by Section 5, not chosen per session:** the desktop breakpoint it names — 1440px when it names none — and the supported lower bound. A width picked ad hoc lets a narrow window pass a page that dies on the screens people actually use.

Two questions decide, and both have answers:

> With the `bulk` fixture, at the desktop width: is there dead space taller than one table row carrying nothing?

> Once this role has finished reading this page, what do they ask next — and is the answer here, or does it force a navigation?

The second is the one that produces the summary row, the reconciliation figure, and the drill-down. Taste produces none of them.

### Then the questions

Read `PRD.md` and the live schema, then ask **everything** still unclear about this page **in a single turn**, together with the content proposal.

Bundling is correct here. `app-init` asks one at a time because bootstrap answers steer each other; a page's unknowns are independent, and asking them one per turn is exactly the stop-start this skill exists to end.

Everything else is decided by you, with the defaults **announced** — a default left unspoken becomes a norm through the back door.

### Where the decision is recorded

**Not in the PRD.** `prd-format` bans enumeration for a reason, and a per-page list of sections is the first kind of sentence to go stale.

It records itself in code. In a UI batch the chosen sections are the shape of the page's contract type — the data the page reads is the content it shows. In a backend batch they are the query and the page. Either way the record is something a compiler checks, not a list somebody has to maintain.

## 5 — The order inside one page

Two chains, one per batch. The backend one extends the chain already fixed by `db-ops` (`migration → run → introspect → types → frontend`), which owns the detail:

```
UI batch
  contract → fixtures, six cases → page + loading, empty, failed states
    → walk all six cases in a browser
    → screenshot the bulk case at both Section 4 widths, judged beside the reference page

Backend batch
  PRD rules → migration + RLS → role test → regenerate types
    → query returning the contract type → wire the page → walk the flow in a browser
```

**The walk ends with proof, not recall.** Screenshot the `bulk` case at the two widths Section 4 fixes, with the browser tooling available to the session, and put the desktop shot beside the reference page at the same width — the density questions in Section 4 are answered from those screenshots, never from memory of how the page looked while building it. Dead space taller than one table row at the desktop width → fix the page in this session; it is not a finding to record and move past. No browser tooling in the session → say so and walk the widths live at the dev server instead — the one thing forbidden is claiming the widths were judged when neither happened.

Backend first **inside one page**, never backend first across the whole app. Splitting the batches does not contradict that: a UI batch has no backend to put anywhere, and a backend batch still builds each page's backend before its wiring.

The six fixture cases and the rules governing contract files are in `references/contract.md`. Read it in a UI batch; a backend batch does not need it.

**A query that cannot return the contract type changes the contract**, and the page it belongs to goes back into the queue. It is never bridged with `as any` or `as unknown as`. A cast there converts a decision the user should have seen into a line nobody will ever read again.

Loading, empty, and failed states are not follow-up work — `ui-build` already binds them to the component they belong to.

**Write this chain as a visible todo list the moment the page starts**, one entry per step of this batch's chain, plus one entry per spread page that passed the test in Section 1. Required, not optional: this is what lets the user see the next step at any moment without asking. The todo list dies with the session, so anything unfinished **must land as a `QUEUE.md` line** before the session closes.

## 6 — Do not stop; the list of legitimate stops is closed

Three, and the list is **closed**:

| Legitimate stop | Why it cannot be dropped |
|---|---|
| The `db-ops` destructive gate | The user approves a **number**, not an intent — lost data does not come back |
| A role test that misses | RLS fails silently; carrying on to the frontend locks the leak in |
| A business rule that is not in the PRD | Guessing it invents a norm through the back door |

**In a UI batch only the third can occur.** There is no migration to gate and no RLS to test, so the first two do not apply — not because they were relaxed, but because the things they guard do not exist yet. Both return in full in the backend batch, and the role test returns stronger than it was: the UI already declares what each role sees, so the test has a written expectation to check against instead of an improvised one.

Anything else: keep going until the page is usable. Report at the end, not between steps.

This does not override the `ui-build` Section 5 gate. Section 5 still `[needs verification]` → the page is not started at all, which is a refusal to begin rather than a stop in the middle.

## 7 — Too big: split, but only where nothing breaks

Splitting is always allowed. What is constrained is **where**:

> A legitimate split point is one where **every page that used to be usable still is.**

The same test decides what may be a queue line at all (Section 2). Splitting work and writing a finer line are the same question asked twice.

So the spread from Section 1 is never a split point — splitting there ends the session with a broken page. What may be split off is work that *adds*; what may not is work that *changes something already shared* — a column, a component's props, a query other pages depend on. No legitimate split point exists → build it whole, that is the real size of the unit.

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

Inside a never-shipped app, the queue decides one thing only — whether it is time yet. **Read the table against the last batch, not the current one.** A UI queue running empty means every screen is accepted, not that the app works; raising deploy there would be offering to ship an app with no database behind it. The `Gone` row applies when no batch is left.

| `QUEUE.md` | What to do about deploy |
|---|---|
| Still has lines | **Do not raise deploy, hosting, CI, or production environment variables on your own initiative.** None of them is needed to build a page and use it locally, and an app whose RLS has not been role-tested does not belong on the internet. Bootstrap already wrote `vercel.json` and the CI workflows — inert files, simply not wired up yet |
| Gone | **Raise it, once.** Every page is usable, so this is the launch moment and the only time this skill brings deploy up by itself: name what is still unwired — hosting connection, production environment variables, CI migrations. Add that the host chosen at bootstrap may have a Claude connector automating the first of those — derived from the stack actually chosen, and worded as *may*, never as a promise that one exists. A shortcut offered, not a step required: deploying by hand works and nothing here waits on it. Then leave it to the user |

**The user asks to deploy → do it.** No lecture and no gate. One sentence naming any table whose RLS has not been role-tested, and only if such a table exists. RLS leaks are silent; nothing else will surface them.

**Commit is stated once, as a fact, in the close block** — `Uncommitted: 3 files`. Never *shall I commit?*, and never mid-session. Two reasons it is stated at all rather than dropped: uncommitted work cannot be recovered, and Section 0 orients from `git log QUEUE.md`, which an app with no commits does not have.
