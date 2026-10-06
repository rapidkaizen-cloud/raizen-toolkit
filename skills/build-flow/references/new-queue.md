# QUEUE — where one comes from, and the shape of its file

Read this when `docs/queue.md` is absent or has just run empty, and when the user asks for what it does not hold. A session building from a standing queue does not need it.

**The queue belongs to a batch of work, not to the app**: born whenever pages are outstanding, deleted when none are, and **born again** for the next batch. Deleting it loses nothing — `git log docs/queue.md` follows the path, so every incarnation shows in one history.

## Three routes, chosen from the state of the repo

**No application code yet** → build the queue from `docs/product.md`'s Roles (work per role) and `docs/rules.md`.

**Code present, the app was never finished** → **discovery first.** Read the routes that exist and introspect the live schema, decide which pages are already usable and which are half-built, then build the queue from what is left. A half-built page gets its own line naming **what is missing**, deleted like any other once the page is usable:

```markdown
- Approval inbox — Approver — renders, but cannot reject yet and has no failed state
- Request detail — Requester — renders, but Finance can still read every row (RLS untested)
```

**The app works and the user wants something new** → the queue comes from **the request**, never from discovery, which finds nothing missing. Three things come before the queue:

- **A big change opens its record first.** More than one page, more than one session, or a new role or data kind → write `docs/changes/<date>-<slug>.md` to `docs-format`'s shape, holding the document lines and the queue it proposes; the approval below covers both, and only then are the lines written into the documents and the queue. After an `app-settle` rework the record quotes the lines the rework already wrote. Below that threshold, no record. A legacy repo writes none.
- **Write the business rules into `docs/rules.md` and new terms into `docs/glossary.md` first** — `docs-format` allows both only *before* implementation, so a rule is a decision rather than a description of code.
- **Run Section 1's spread test against each existing page before setting the order** — a working app has many pages that can break.

**A Help row in `docs/product.md` that opens with `in-app` owes the help page at its route one line, on every route, until that page exists.**

**All three routes end the same way: show the whole queue, STOP, and wait for the user's approval before writing the file.** The order is agreed once, up front.

## Splitting the work into a UI batch and a backend batch

A batch may deliver **UI only** — every page built against a hand-written contract and its fixtures, with no database behind it. The backend batch follows and wires them.

- **A new app is built UI batch first, then backend** — revising a page is cheap while nothing is wired behind it, and screens judged together show the one that answers too little.
- **An app that already runs splits only when the split pays.** Either condition is enough: **three or more new pages at once**, or **a requirement still vague**. Below that, one batch and full-stack per page — a single UI-only page in a wired app is a half-dead page, easy to mistake for a finished one.
- **The UI queue running empty is the freeze.** The commit that deletes the file is the moment the contracts stop moving, dated in `git log docs/queue.md` — no separate mechanism, no ceremony. After the freeze a contract changes only as a stated decision: the page it belongs to goes back into the queue.
- **Contracts are never retrofitted.** A page that already has a real query has a real data shape; contracts are born only for pages built in a UI batch.

## The file

Open the file with its batch's title and three header lines: they stop a later session adding a status column, or reading a UI batch as a backend one. The examples are English only because this skill is.

A backend batch, and any app that never split its work:

```markdown
# QUEUE

Pages not yet usable, in order. A line gone means that page is usable — deleted
the moment it was. History is in `git log docs/queue.md`. Do not add status,
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
finished — deleted the moment it was. History is in `git log docs/queue.md`.
Do not add status, checkboxes, or dates.

- Contract + fixtures: request list — six cases, rows copied from the file this app replaces
- Request list — Requester — see their own requests and where each one stands
- Create request — Requester — file a new request with its attachments (needs: Request list)
- Contract + fixtures: approval inbox
- Approval inbox — Approver — approve or reject requests inside their authority limit
```
