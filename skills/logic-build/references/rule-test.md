# The rule test — what it attacks, and a repo with no runner

Read before writing a test for a `docs/rules.md` topic, and at the first rule implemented in a repo with no test runner. `SKILL.md` Section 10 holds the test's title and what a failing one means.

## What the test attacks

| The rule is enforced by | The test |
|---|---|
| RLS — an access rule | The `db-ops` role test, already mandatory on every policy change. Not duplicated here |
| A constraint, a trigger, or an RPC | Attempts the forbidden write as the role the rule binds and expects the refusal, then the permitted one and expects it to land. Run through the database's own test harness where the stack has one — verified live, never recalled — else through the app's runner over the same client path a user takes |
| A computation in the data layer — a formula, a limit, a state transition | Calls the function with the rule's value, the value just inside it, and the value just outside — a number in a rule is a boundary, and one tidy value in the middle proves nothing about it |

It tests the rule — not the UI, not the library, and not the reason, which no test can reach.

## No test runner in the repo

`app-settle` recommends deferring one on a first app, so the first rule implemented is the moment *later* arrived. **Raise it once, through AskUserQuestion, bundled with the questions `build-flow` Section 4 already collects for that page**, never as a turn of its own:

- **Install the runner now** — recommended by that question's own rule wherever the app carries money, permissions, or a rule expensive to get wrong.
- **Carry on unproven** — a real answer, recorded where it stays visible: one `docs/queue.md` line per rule, `Prove: <topic>`. Such a line passes `build-flow`'s test for a line finer than a page: a test added changes nothing that stands.
