---
name: logic-build
description: Rules for the layer between the database and the UI — API keys and what may reach the client, where a business rule is allowed to live, validating input crossing a trust boundary, transaction boundaries, the shape of an error returned to the UI, the one folder every database call lives in, the lint floor that holds it there, and the test every business rule leaves behind. Use before writing a query, a server action, a route handler, an edge function, or any environment variable.
---

# logic-build — between the database and the UI

Documents are named by their path in the `docs/` form; a repo with a root `PRD.md` reads each through `docs-format`'s legacy map.

`db-ops` owns the database. `ui-build` owns the screen. This owns what runs in between —
the queries, actions, handlers, and rules that neither of the other two claims.

Its first section is the one that decides whether the other two mean anything: every role
test in `db-ops` is worth nothing if the client holds a key that bypasses RLS.

## 1 — Keys and what reaches the client

Two kinds of key, and confusing them is the most expensive mistake available in this stack.

| Key | Bypasses RLS | Where it belongs |
|---|---|---|
| anon / publishable | No | The client. It is **designed** to be public — RLS is the only thing protecting it |
| `service_role` / secret | **Yes, entirely** | Server-only environment, or an edge function secret. Never anywhere a browser can reach |

`service_role` in client code does not weaken RLS — it **removes** it. Every policy, every
negative role test, every `qual` predicate stops applying. The app keeps working and
looks correct, which is why this is never caught by using the app.

**A variable named `VITE_*`, `NEXT_PUBLIC_*`, or `PUBLIC_*` is shipped to every visitor.**
That is what the prefix means. Vite additionally freezes its value at **build** time, so
rotating the secret does not clear the one already baked into a deployed bundle. Never
give one of these prefixes to a secret, whatever else the name says.

Before writing any environment variable, answer one question out loud: *can whoever
holds the client read this?* Yes and it is a secret → stop, it needs a server surface (Section 3).

**A secret already committed is a stop, not a fix.** Deleting the line does not un-leak it:
it stays in git history and in every bundle already built. Report it, name the key, and
tell the user to **rotate it first** — the cleanup is worthless until they do.

Values never appear in a document, a commit message, or a report. Names only.

## 2 — Where a rule is allowed to live

One rule, one place. A rule implemented twice diverges silently, and only one of the two
copies is ever the one actually enforced.

| Kind of rule | Where it lives | Why not elsewhere |
|---|---|---|
| **Access** — who may read or change which row | **RLS, always** | Re-implementing it in application code creates a second copy that is not enforced. The database is reached by more than one path |
| **Computation or workflow** — limits, totals, state transitions | One named place — see Section 3 and 4 | Split across query and component, no single place answers "what is the rule" |
| **Anything in client code** | Convenience only | A hostile client is not a hypothesis; it is a browser with devtools open |

A client-side check that mirrors a real rule is allowed as UX — instant feedback beats a
round trip. It is **never the enforcement**, and the code says so: name it as a mirror of
the rule it copies, so a later session does not read it as the rule itself.

**A rule that is not in `docs/rules.md` is a legitimate stop** in `build-flow`
Section 6 — one of three in a backend batch, and the only one in a UI batch. Do not invent it, and do not write it there afterwards — `docs-format`
allows rules only *before* implementation, precisely so a rule stays a
decision rather than a description of code.

## 3 — No server layer, the client reaches the database directly (a static SPA on the web)

The client speaks to the database directly. There is no place in this app to hide a
secret and no code path the user cannot reach. It follows that:

> **Everything the client can do, a hostile client can do.** Enforcement lives in the
> database or it does not exist.

The tools, in order of reach:

| Need | Use |
|---|---|
| Who sees which row | RLS policy |
| A value that must always hold | `CHECK` constraint, `NOT NULL`, FK |
| A rule spanning rows or tables on write | Trigger, or an RPC the client calls instead of writing directly |
| Something the client must not be able to do at all | A server surface — see below |

An RPC marked `SECURITY DEFINER` runs as the owner and therefore **bypasses RLS inside
its own body**. That is sometimes exactly the point, and it is also how a leak gets
written by accident. Use it only when the reason is named, keep the body narrow, and
role-test it like any policy — `db-ops` role testing applies to the RPC, not just to the
tables under it.

**Needing a real secret means needing a server surface** — a Supabase Edge Function, or a
framework with a server layer. Both change the shape of the repo and the deploy, so this
is raised with the user as a stack change. Never added quietly mid-page.

## 4 — With a server layer (Next.js, Nuxt, SvelteKit, an edge function)

**Input crossing the boundary is untrusted, including input from your own frontend.**
The frontend is not a boundary; the network is. Parse it into a known shape at the entry
point of the handler and reject what does not fit, before any of it reaches a query.

**Every handler checks authorization itself.** Two reasons, and the second is the one
that bites: a handler is reachable directly, whatever the UI links to; and a handler that
uses `service_role` has **no RLS underneath it**, so its own check is the only one left.
Prefer running the handler with the user's own token so RLS still applies — reach for
`service_role` only when the operation genuinely must exceed the user's rights, and say
in the code why.

**A write that spans more than one statement runs in one transaction**, or as a single
RPC. Half-applied writes are found weeks later, by which time the correct end state is
no longer knowable.

## 5 — Errors crossing the boundary

Two audiences, two shapes, one event:

- **The user** gets a sentence they can act on. `ui-build` owns where it is shown.
- **The log** gets the detail: the operation, the identifiers, the underlying error.

Raw database error text never reaches the UI. It leaks table and column names, and it
tells the user nothing they can do.

**Never swallow.** A caught error that returns an empty list is indistinguishable from
no data, and the failed state `ui-build` requires will never render. Catching in order to
add context and re-raise is fine; catching in order to continue is a finding.

## 6 — Which libraries this layer uses

Decided once, by the `logic-settle` skill in `raizen-hub` — cache, validator, dates, error destination, job placement, change attribution. The names live in the Stack table of `CLAUDE.md`; the choice and its reason live in `docs/decisions/`, one record each, including every deliberate "none".

Three rules bind every session after that:

- **A recorded "none" is a decision, not a gap.** Handwritten fetching in a repo whose decision record says "cache: none — two screens" is the norm being followed, not a finding.
- **A need surfacing that `logic-settle` never scored** — a screen that now wants caching, a handler appearing where none existed — is **raised to the user, never solved by a quiet install**. One question re-opens; the interview does not. Several at once, or a library that is the wrong tool rather than a missing one, re-opens `logic-settle` in `raizen-hub` — still the user's to start, never yours.
- **A library's defaults are the decision.** `staleTime`, `retry`, `refetchOnWindowFocus`, preload behaviour, and their equivalents ship with an answer, and it holds until a decision record gives a reason to change it — the same standing `ui-build` gives component defaults. These knobs decide how much traffic reaches the database and how stale a screen may be, so an unrecorded change to one is a finding, not a tuning detail.

## 7 — Reuse, and types

A query or a rule appearing a **second** time is extracted, not copied — the same trigger
`ui-build` applies to components. Two copies of a filter is how one of them silently stops
matching the policy behind it.

Types come from `db-ops`: regenerated from the live schema after every schema change,
before any of this layer is touched. An `as any` on a call missing from the types file is
a finding to report, not a pattern to follow.

## 8 — Where this layer lives

**Every call to the database — a query, a mutation, an RPC — lives in one folder, and nothing outside it holds the database client.** A page, a component, a route handler calls a function from that folder; it never builds a query of its own. The folder is this app's, recorded by `logic-settle` as the `Data layer` row of `CLAUDE.md`'s Stack table — read it there, never assume a name.

This is the rule Section 7 cannot hold without. *A query appearing a second time is extracted* only works if the first one can be found, and a query written inline in a page is found by nobody: the next session writes it again with a filter that differs by one condition, and one of the two silently stops matching the policy behind it. One folder is also what makes the rest mechanical — the lint floor below has a path to scope to, and the session-start block lists the folder's functions before the first query is written.

**Read the listing first, then the file.** The session-start block carries the folder's files and their exported functions wherever the row exists. It stands in for the listing, never for reading the file a new query belongs in.

- **Split by domain, never by page.** `leads`, `payouts`, `periods` — a file per page rebuilds the scatter this rule exists to end, one level down.
- **A computation or workflow rule that lives in application code lives here** — wherever Sections 3 and 4 allow it in application code at all; on a static SPA the enforced copy is in the database and this folder holds the call to it. A rule computed inside a component is a rule no test can reach.
- **A framework entry point stays where the framework puts it** — a route handler, a server action, an edge function. It parses, authorizes, and calls this folder; it does not query.
- **A contract's query returns the contract type from here**, so the page built in a UI batch is wired by changing one import.

No `Data layer` row → the repo predates this rule. Say so in one line, write new queries beside the existing ones rather than founding a second location, and carry on — naming the folder is `logic-settle`'s, and moving old call sites into it is a migration the user approves there, never a drive-by. An app with no database and no remote API has no data layer, and this section does not apply to it.

## 9 — The lint floor — what the repo itself refuses

Everything above is obeyed by judgement, and an agent that never loads this file obeys none of it. Five failures are refused by the repo's own linter instead, where they reach every session and every agent:

1. **The database client imported or called outside the data layer folder.**
2. **A secret on its way to the client** — a variable carrying a public prefix whose name says secret, service role, or private key, and any reference to the service-role key from code a browser can reach. Section 1 says why this one cannot wait for a review.
3. **A second library for a need `logic-settle` settled** — a second validator, a second date library, a second cache. It refuses the import even after a quiet install, which is the install Section 6 forbids.
4. **A cast that erases a database type** — `as any`, `as unknown as`, on anything this layer returns.
5. **A swallowed error** — an empty `catch`, or a `catch` whose whole body returns a default.

`logic-settle` writes the floor, derived from this app's folder and its settled libraries; a repo that has none gets it from `app-conform`. It is lived with the way `ui-build` lives with its own: **run the repo's lint command before committing any scope item in this layer**; an inline disable of a floor rule, or a floor rule lowered to a warning, is a finding; a refusal that is wrong is narrowed in the config on the user's word, never silenced at the call site. No floor in the repo → say so in one line and carry on. **A hook refusing a write to the linter config** (another plugin guarding config files) → hand the user the change as a patch in chat and wait; never write it through a shell or another tool.

What the floor cannot see is where a rule lives, a rule `docs/rules.md` never stated, and a query written twice under two names. The first two are Section 2's; the third is what the listing in Section 8 is for.

## 10 — A rule is proven by a test that names it

`docs/rules.md` is the one part of an app a later session — or another agent — can break while every page still renders. A rule re-implemented from a session's own reading passes the build, passes the walk, and is wrong. The only thing that refuses it without anyone reading anything is a test.

**Every rule a backend batch implements leaves one test behind, and the test's title quotes the rule's topic heading exactly as `docs/rules.md` writes it** — in that document's language. It is the one string in the test files that is not English, because it is a reference to look up, not an identifier. That quote is what makes coverage a search rather than an opinion: a topic no test title carries is an unproven rule. Rename the topic → rename the title in the same commit.

**The test attacks the enforcement point, never a mirror of it:**

| The rule is enforced by | The test |
|---|---|
| RLS — an access rule | The `db-ops` role test, already mandatory on every policy change. Not duplicated here |
| A constraint, a trigger, or an RPC | Attempts the forbidden write as the role the rule binds and expects the refusal, then the permitted one and expects it to land. Run through the database's own test harness where the stack has one — verified live, never recalled — else through the app's runner over the same client path a user takes |
| A computation in the data layer — a formula, a limit, a state transition | Calls the function with the rule's value, the value just inside it, and the value just outside. A number in a rule is a boundary, and a test on one tidy value in the middle proves nothing about it |

It tests the rule — not the UI, not the library, and not the reason, which no test can reach.

**A failing rule test is never fixed by editing the test.** The rule changed → the user changed it, and the test follows the rule in the same commit. The rule did not change → the code is wrong. A session that edits the expected value to match its code has rewritten a business rule without the user, which is the exact failure this section exists to catch.

**No test runner in the repo** — `app-settle` recommends deferring one on a first app — → the first rule implemented is the moment *later* arrived. Raise it once, through AskUserQuestion, bundled with the questions `build-flow` Section 4 already collects for that page rather than as a turn of its own: install the runner now, recommended by that question's own rule wherever the app carries money, permissions, or a rule expensive to get wrong; or carry on unproven. Unproven is a real answer, and it is recorded where it stays visible — one `docs/queue.md` line per rule, `Prove: <topic>` — never as a quiet install and never as silence. Such a line passes `build-flow`'s test for a line finer than a page: a test added changes nothing that stands.
