# BACKEND — what the backend chain adds

Read this before the first page of a backend batch, or of an app that never split its work. A UI batch does not need it.

## The rule test, before the wiring

Write the rule test from the rule, against the enforcement point, while the page cannot yet vouch for it — a test written to agree with running code agrees with its bugs. A page implementing no rule has no such step. A repo with no test runner raises it once under `logic-build` and records what stays unproven as `Prove: <topic>` lines in the queue.

## Wiring a page built in a UI batch

The query must return the contract type. Three rules, and the first is the one broken quietly:

- **No `as any`, no `as unknown as`, no widening a type to make it fit** — a cast hides a decision that belongs to the user.
- **A query that cannot satisfy the contract changes the contract**, and the page it belongs to goes back into `docs/queue.md` — a stated decision, never a side effect of wiring.
- **Replace the mocked session; never leave it beside the real one.** Two sources of role is one too many.

## Retiring a page's canvas file

`src/design-canvas/<page>` still standing means the design session ratified this page and left the file for comparison. After the wiring walk passes at both widths:

1. Put the real page beside its canvas file and fix what silently diverged.
2. **Propose the deletion at a chat stop** — naming the page and inviting the side-by-side look — and delete only on the user's granted confirmation (`design-settle`'s canvas lifecycle: never delete unasked).
3. Propose it in this same session: kept past its verified page, the file becomes a second source of values.

The last page file to go takes the canvas index route, its foundations board, its CSS, and `.design-audit/` with it.
