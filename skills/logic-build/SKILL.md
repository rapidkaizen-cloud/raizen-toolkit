---
name: logic-build
description: Rules for the layer between the database and the UI — API keys and what may reach the client, where a business rule lives, boundary validation, transactions, error shape, the data-layer folder, its lint floor, and the test each rule leaves. Use before writing a query, a server action, a route handler, an edge function, or any environment variable.
---

# logic-build — between the database and the UI

Documents are named by their `docs/` path; a repo with a root `PRD.md` reads each through `docs-format`'s legacy map.

`db-ops` owns the database, `ui-build` the screen; this skill owns what runs between them — the queries, actions, handlers, and rules neither claims.

## What a load costs — two rules

- **Run independent reads, searches and commands in one turn** — parallel calls, or one chained command — because every extra model call re-reads the whole session.
- **Never re-read what the session start printed** — its data-layer listing stands in for listing the folder (Section 8).

## 1 — Keys and what reaches the client

| Key | Bypasses RLS | Where it belongs |
|---|---|---|
| anon / publishable | No | The client. It is **designed** to be public — RLS is the only thing protecting it |
| `service_role` / secret | **Yes, entirely** | Server-only environment, or an edge function secret. Never anywhere a browser can reach |

**`service_role` in client code does not weaken RLS — it removes it.** Every policy, every negative role test, every `qual` predicate stops applying, while the app keeps working and looks correct — using the app never catches it.

**A variable named `VITE_*`, `NEXT_PUBLIC_*`, or `PUBLIC_*` is shipped to every visitor.** Never give one of these prefixes to a secret, whatever else the name says. Vite also freezes the value at **build** time, so rotating the secret does not clear the one baked into a deployed bundle.

**Before writing any environment variable, answer one question out loud: *can whoever holds the client read this?*** Yes and it is a secret → stop, it needs a server surface (Section 3).

**A secret already committed is a stop, not a fix.** Deleting the line does not un-leak it: it stays in git history and in every bundle already built. Report it, name the key, and tell the user to **rotate it first** — the cleanup is worthless until they do.

**Values never appear in a document, a commit message, or a report.** Names only.

## 2 — Where a rule is allowed to live

**One rule, one place** — a rule implemented twice diverges silently, and only one copy is enforced.

| Kind of rule | Where it lives |
|---|---|
| **Access** — who may read or change which row | **RLS, always** — a copy in application code is not enforced, because the database is reached by more than one path |
| **Computation or workflow** — limits, totals, state transitions | One named place — Sections 3 and 4 |
| **Anything in client code** | Convenience only — a hostile client is a browser with devtools open |

**A client-side check that mirrors a real rule is allowed as UX, never as the enforcement.** Name it in the code as a mirror of the rule it copies, so a later session does not read it as the rule itself.

**A rule that is not in `docs/rules.md` is a legitimate stop** in `build-flow` Section 6 — one of three in a backend batch, the only one in a UI batch. Never invent it, and never write it there afterwards: `docs-format` allows a rule only *before* its implementation.

## 3 — No server layer, the client reaches the database directly (a static SPA on the web)

**Everything the client can do, a hostile client can do: enforcement lives in the database or it does not exist.** The app has no place to hide a secret and no code path the user cannot reach.

The tools, in order of reach:

| Need | Use |
|---|---|
| Who sees which row | RLS policy |
| A value that must always hold | `CHECK` constraint, `NOT NULL`, FK |
| A rule spanning rows or tables on write | Trigger, or an RPC the client calls instead of writing directly |
| Something the client must not be able to do at all | A server surface — see below |

**An RPC marked `SECURITY DEFINER` runs as the owner and bypasses RLS inside its own body.** Use it only when the reason is named, keep the body narrow, and role-test it like any policy — `db-ops` role testing applies to the RPC, not just to the tables under it.

**Needing a real secret means needing a server surface** — a Supabase Edge Function, or a framework with a server layer. Both change the shape of the repo and the deploy: raise it with the user as a stack change, never add it quietly mid-page.

## 4 — With a server layer (Next.js, Nuxt, SvelteKit, an edge function)

**Input crossing the boundary is untrusted, including input from your own frontend** — the network is the boundary, not the frontend. Parse it into a known shape at the entry point of the handler and reject what does not fit, before any of it reaches a query.

**Every handler checks authorization itself**: it is reachable directly, whatever the UI links to, and a handler that uses `service_role` has **no RLS underneath it**, so its own check is the only one left. Prefer running the handler with the user's own token so RLS still applies; use `service_role` only when the operation must exceed the user's rights, and say in the code why.

**A write that spans more than one statement runs in one transaction, or as a single RPC** — a half-applied write is found weeks later, when the correct end state is no longer knowable.

## 5 — Errors crossing the boundary

One event, two shapes:

- **The user** gets a sentence they can act on. `ui-build` owns where it is shown.
- **The log** gets the detail: the operation, the identifiers, the underlying error.

**Raw database error text never reaches the UI** — it leaks table and column names and tells the user nothing they can do.

**Never swallow.** A caught error that returns an empty list is indistinguishable from no data, and the failed state `ui-build` requires never renders. Catching to add context and re-raise is fine; catching to continue is a finding.

## 6 — Which libraries this layer uses

`logic-settle` decides them once — cache, validator, dates, error destination, job placement, change attribution. The names are in the Stack table of `CLAUDE.md`; each choice and its reason is one record in `docs/decisions/`, every deliberate "none" included.

- **A recorded "none" is a decision, not a gap** — handwritten fetching where the record says "cache: none — two screens" is the norm followed, not a finding.
- **A need `logic-settle` never scored** — a screen that now wants caching, a handler appearing where none existed — **is raised to the user, never solved by a quiet install.** One question re-opens, not the interview; several at once, or a library that is the wrong tool rather than a missing one, re-opens `logic-settle` — the user's to start, never yours.
- **A library's defaults are the decision.** `staleTime`, `retry`, `refetchOnWindowFocus`, preload behaviour, and their equivalents hold until a decision record gives a reason to change one — the standing `ui-build` gives component defaults. They decide how much traffic reaches the database and how stale a screen may be, so an unrecorded change is a finding.

## 7 — Reuse, and types

**A query or a rule appearing a second time is extracted, not copied** — the trigger `ui-build` applies to components — because one of two copies of a filter silently stops matching the policy behind it.

**Types come from `db-ops`**: regenerated from the live schema after every schema change, before any of this layer is touched. An `as any` on a call missing from the types file is a finding to report, not a pattern to follow.

## 8 — Where this layer lives

**Every call to the database — a query, a mutation, an RPC — lives in one folder, and nothing outside it holds the database client.** A page, a component, a route handler calls a function from that folder and never builds a query of its own, because Section 7 can only extract a query that can be found. The folder is this app's, recorded by `logic-settle` as the `Data layer` row of `CLAUDE.md`'s Stack table — read it there, never assume a name.

**Read the listing first, then the file.** The session-start block carries the folder's files and their exported functions wherever the row exists; it stands in for listing the folder, never for reading the file a new query belongs in.

- **Split by domain, never by page** — `leads`, `payouts`, `periods`; a file per page rebuilds the scatter one level down.
- **A computation or workflow rule that lives in application code lives here**, wherever Sections 3 and 4 allow it in application code at all; on a static SPA the enforced copy is in the database and this folder holds the call to it. A rule computed inside a component is a rule no test can reach.
- **A framework entry point stays where the framework puts it** — a route handler, a server action, an edge function. It parses, authorizes, and calls this folder; it does not query.
- **A contract's query returns the contract type from here**, so the page built in a UI batch is wired by changing one import.

**No `Data layer` row → the repo predates this rule.** Say so in one line, write new queries beside the existing ones rather than founding a second location, and carry on: naming the folder is `logic-settle`'s, and moving old call sites into it is a migration the user approves there, never a drive-by. An app with no database and no remote API has no data layer, and this section does not apply to it.

## 9 — The lint floor — what the repo itself refuses

Five refusals live in the repo's own linter, where they reach every session and every agent, this file loaded or not:

1. **The database client imported or called outside the data layer folder.**
2. **A secret on its way to the client** — a variable carrying a public prefix whose name says secret, service role, or private key, and any reference to the service-role key from code a browser can reach (Section 1).
3. **A second library for a need `logic-settle` settled** — a second validator, a second date library, a second cache. It refuses the import even after the quiet install Section 6 forbids.
4. **A cast that erases a database type** — `as any`, `as unknown as`, on anything this layer returns.
5. **A swallowed error** — an empty `catch`, or a `catch` whose whole body returns a default.

`logic-settle` writes the floor, derived from this app's folder and its settled libraries; a repo that has none gets it from `app-align`.

- **Run the repo's lint command before committing any scope item in this layer.**
- An inline disable of a floor rule, or a floor rule lowered to a warning, is a finding.
- A refusal that is wrong is narrowed in the config on the user's word, never silenced at the call site.
- No floor in the repo → say so in one line and carry on.
- **A hook refusing a write to the linter config** (another plugin guarding config files) → hand the user the change as a patch in chat and wait; never write it through a shell or another tool.

The floor cannot see where a rule lives or a rule `docs/rules.md` never stated — Section 2's — nor a query written twice under two names, which the listing in Section 8 is for.

## 10 — A rule is proven by a test that names it

**Every rule a backend batch implements leaves one test behind, and the test's title quotes the rule's topic heading exactly as `docs/rules.md` writes it** — in that document's language, the one string in the test files that is not English, because it is a reference to look up, not an identifier. A topic no test title carries is an unproven rule. Rename the topic → rename the title in the same commit.

**The test attacks the enforcement point, never a mirror of it.** Before writing one, read `references/rule-test.md` — what the test does where the rule is enforced by RLS, by a constraint, trigger or RPC, or by a computation in the data layer.

**A failing rule test is never fixed by editing the test.** The rule changed → the user changed it, and the test follows the rule in the same commit. The rule did not change → the code is wrong: editing the expected value to match the code rewrites a business rule without the user.

**No test runner in the repo → raise it once, at the first rule implemented, as `references/rule-test.md` says** — never a quiet install, never silence.
