---
name: logic-build
description: Rules for the layer between the database and the UI — API keys and what may reach the client, where a business rule is allowed to live, validating input crossing a trust boundary, transaction boundaries, and the shape of an error returned to the UI. Use before writing a query, a server action, a route handler, an edge function, or any environment variable.
---

# logic-build — between the database and the UI

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

Before writing any environment variable, answer one question out loud: *can a visitor
read this?* Yes and it is a secret → stop, it needs a server surface (Section 3).

**A secret already committed is a stop, not a fix.** Deleting the line does not un-leak it:
it stays in git history and in every bundle already built. Report it, name the key, and
tell the user to **rotate it first** — the cleanup is worthless until they do.

Values never appear in `PRD.md`, in a commit message, or in a report. Names only.

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

**A rule that is not in `PRD.md` is one of the three legitimate stops** in `build-flow`
Section 6. Do not invent it, and do not write it into the PRD afterwards — `prd-format`
allows Sections 3 and 4 only *before* implementation, precisely so a rule stays a
decision rather than a description of code.

## 3 — No server layer (static SPA)

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

Decided once, by the `logic-init` skill in `raizen-hub` — cache, validator, dates, error destination, job placement, change attribution. The names live in the Stack table of `CLAUDE.md`; the choice and its reason live in `PRD.md` Section 1, including every deliberate "none".

Two rules bind every session after that:

- **A recorded "none" is a decision, not a gap.** Handwritten fetching in a repo whose PRD says "cache: none — two screens" is the norm being followed, not a finding.
- **A need surfacing that `logic-init` never scored** — a screen that now wants caching, a handler appearing where none existed — is **raised to the user, never solved by a quiet install**. One question re-opens; the interview does not.

## 7 — Reuse, and types

A query or a rule appearing a **second** time is extracted, not copied — the same trigger
`ui-build` applies to components. Two copies of a filter is how one of them silently stops
matching the policy behind it.

Types come from `db-ops`: regenerated from the live schema after every schema change,
before any of this layer is touched. An `as any` on a call missing from the types file is
a finding to report, not a pattern to follow.
