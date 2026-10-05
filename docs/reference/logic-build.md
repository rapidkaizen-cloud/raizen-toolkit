# logic-build

A session keeps secrets off the client, gives each business rule one place to live, treats every input crossing the boundary as untrusted, keeps every database call in one folder, and leaves a test behind for each rule it implements.

| | |
|---|---|
| Kind | Rule skill — a session loads it by its description; there is no command |
| Loads when | Before writing a query, a server action, a route handler, an edge function, or any environment variable |
| Governs | The layer between the database and the UI: keys, where a rule lives, boundary validation, transactions, error shape, the data-layer folder, its lint floor, rule tests |
| Reads | `docs/rules.md`, `docs/decisions/`, the Stack table of `CLAUDE.md` (its `Data layer` row), the data-layer listing the session start prints |
| Source | `skills/logic-build/SKILL.md`, with `references/rule-test.md` |

`db-ops` owns the database and `ui-build` the screen. This skill owns what runs between them.

## What a session is held to

**Keys and the client** (Section 1). The anon or publishable key belongs on the client; RLS is all that protects it. The `service_role` or secret key belongs in a server-only environment or an edge function secret. In client code it does not weaken RLS, it removes it, and the app keeps looking correct.

- **A variable named `VITE_*`, `NEXT_PUBLIC_*` or `PUBLIC_*` reaches every visitor.** A secret never gets one of those prefixes.
- **One question before any environment variable:** can whoever holds the client read this? If yes and it is a secret, the session stops.
- **A secret already committed is a stop, not a fix.** The session names the key and tells you to rotate it first.
- **Values never appear** in a document, a commit message or a report. Names only.

**One rule, one place** (Section 2). Access rules live in RLS, always. Computation and workflow rules live in one named place. Client code is convenience only. A client-side check that mirrors a real rule is allowed as UX and is named in the code as a mirror.

**No server layer** (Section 3, a static SPA on the web). Enforcement lives in the database or it does not exist. A rule spanning rows or tables on write is a trigger or an RPC the client calls instead of writing directly. An RPC marked `SECURITY DEFINER` is used only for a named reason, with a narrow body, and is role-tested like a policy. Needing a real secret means needing a server surface, which the session raises with you as a stack change and never adds quietly.

**With a server layer** (Section 4). Input is parsed into a known shape at the entry of the handler and rejected before it reaches a query, even from your own frontend. Every handler checks authorization itself, and prefers the user's own token so RLS still applies. A handler uses `service_role` only when the operation must exceed the user's rights, with the reason in the code. A write spanning more than one statement runs in one transaction or as a single RPC.

**Errors** (Section 5). You get a sentence you can act on; the log gets the operation, the identifiers and the underlying error. Raw database error text never reaches the UI. An error is not swallowed: catching to add context and re-raise is fine, catching to continue is a finding.

**Libraries** (Section 6). `logic-settle` decides them once. The names are in the Stack table of `CLAUDE.md`, each with a record in `docs/decisions/`.

- **A recorded "none" is a decision, not a gap.**
- **A need `logic-settle` never scored** is raised to you, never solved by a quiet install.
- **A library's defaults are the decision.** A change to `staleTime`, `retry` or the like needs a decision record, or it is a finding.

**Reuse and types** (Section 7). A query or rule appearing a second time is extracted. Types come from `db-ops`, regenerated after every schema change.

**One data-layer folder** (Section 8). Every query, mutation and RPC lives in one folder, and nothing outside it holds the database client. The folder is the `Data layer` row of `CLAUDE.md`'s Stack table. It splits by domain, never by page. A route handler, server action or edge function stays where the framework puts it, parses, authorizes and calls the folder. A contract's query returns the contract type from here. Without a `Data layer` row the session says so in one line, writes beside the existing queries, and carries on.

**The lint floor** (Section 9). Five refusals live in the repo's own linter: the database client used outside the data-layer folder; a secret on its way to the client; a second library for a need `logic-settle` settled; a cast that erases a database type; a swallowed error. `logic-settle` writes it, and a repo with none gets it from `app-settle`'s align mode. Lint runs before any scope item in this layer is committed. An inline disable or a rule lowered to a warning is a finding. A wrong refusal is narrowed in the config only on your word.

**A rule is proven by a test that names it** (Section 10, `references/rule-test.md`). Each rule a backend batch implements leaves one test, and its title quotes the rule's topic heading exactly as `docs/rules.md` writes it. A topic no test title carries is an unproven rule.

| The rule is enforced by | The test |
|---|---|
| RLS | The `db-ops` role test, not duplicated |
| A constraint, trigger or RPC | The forbidden write as the bound role, expecting refusal; then the permitted one, expecting it to land |
| A computation in the data layer | The rule's value, the value just inside it and the value just outside it |

A failing rule test is never fixed by editing the test. If the rule changed, you changed it, and the test follows in the same commit. If not, the code is wrong.

## What you will see

- **A test-runner question**, once, at the first rule implemented in a repo with none, bundled with the questions `build-flow` already asks for that page. Its two options are to install the runner, recommended where the app carries money, permissions or a rule expensive to get wrong, or to carry on unproven.
- **`Prove: <topic>` lines** in `docs/queue.md`, one per rule, when you carry on unproven.
- **One-line notes** where a repo has no lint floor or no `Data layer` row.
- **A patch in chat** when a hook refuses a write to the linter config. The session waits and never writes it another way.

## Where it stops

- **A secret already committed.** The session reports it, names the key and tells you to rotate it first; the cleanup is worthless until you do.
- **A rule not in `docs/rules.md`.** It is a `build-flow` stop; the session never invents it and never writes it afterwards.
- **A secret the client would need.** The session raises the server surface as a stack change.
- **A need `logic-settle` never scored.** It is raised to you. One question re-opens only that choice; several at once, or a library that is the wrong tool, re-open `logic-settle`, which only you start.

## What it does not cover

- **The lint floor cannot see** where a rule lives, a rule `docs/rules.md` never stated, or a query written twice under two names. The Section 8 listing is for the last.
- **The rule test does not test** the UI, the library or the reason behind a rule.
- **An app with no database and no remote API** has no data layer.

## Related

[db-ops](db-ops.md) · [ui-build](ui-build.md) · [build-flow](build-flow.md) · [logic-settle](logic-settle.md) · [app-settle](app-settle.md) · [docs-format](docs-format.md) · [Gates](../concepts/gates.md)
