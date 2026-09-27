# CONTRACT — the UI batch's stand-in for a backend

Read this in a UI batch. A backend batch does not need it.

A UI batch builds pages with no database behind them. The risk that carries is one thing only: **a page shaped around data that was never declared.** Invented data is always well formed — no nulls, short strings, five tidy rows — so a page approved against it breaks the day real data arrives. A contract is what stops a page being shaped by data whose shape nobody wrote down.

## The two files

```
src/contracts/<page>.ts            types only, no runtime
src/contracts/<page>.fixtures.ts   the six cases
```

The contract holds three things: the data the page reads, the actions it fires, and the role of whoever is reading. Role is an input to the page like any other — a page that learns about roles later grows its role handling as a patch, and patched role handling is where leaks live.

**A page imports from its contract and from nothing else that carries data.** During a UI batch, no file under `src/pages` may import the database client or the generated database types. One grep at the close of the session, and a hit is a finding:

```
grep -rE "lib/supabase|database\.types" src/pages
```

## The six cases

A page is not accepted until all six render without the layout breaking. They are a closed floor, so this is a checklist rather than a judgement; a page adds a named case only for a form branch or a busy state it shows:

| Case | What it proves |
|---|---|
| `loading` | A skeleton shaped like the result, not a spinner |
| `empty` | The empty state says why it is empty and what comes next |
| `single` | One row does not leave the layout stranded |
| `bulk` | 500+ rows — pagination, scrolling, column widths, and the density `DESIGN.md` asked for |
| `messy` | Null in every nullable field, the longest string that really occurs, the widest number |
| `failed` | The failure sits next to its cause, with a way to retry |

`bulk` and `messy` are the two usually skipped and the two that catch the most. A page designed against three tidy rows is how a screen ends up mostly empty space.

**Fixtures are copied from the document the app replaces, not invented.** These apps replace a process that already runs somewhere — a spreadsheet, an export, a paper form. Its rows are the fixture: real column widths, real name lengths, real edge cases, and figures whose correct answer the user already knows. A user judging a screen against numbers they already trust is judging the screen; a user judging invented numbers is judging nothing.

Where no real document can be used, say so in the session and name what was substituted.

## Switching cases

Two switches — one for the fixture case, one for the role — reachable without a rebuild, and no tooling beyond them. On the web they are two search params; elsewhere they are whatever the **Cases** line of the Proof profile in `docs/product.md` names:

```
?fixture=messy
?role=approver
```

No Storybook, no mock server, no fixture generator, on any platform. If two switches ever stop being enough, that is the moment to reach for more — not before.

## Wiring, in the backend batch

The query must return the contract type. Three rules, and the first is the one broken quietly:

- **No `as any`, no `as unknown as`, no widening a type to make it fit.** A cast here hides a decision that belongs to the user.
- **A query that cannot satisfy the contract changes the contract**, and the page it belongs to goes back into `docs/queue.md`. A stated decision, not a side effect of wiring.
- **The mocked session is replaced, not left beside the real one.** Two sources of role is one too many.

## What a contract does not cover

Behaviour that crosses screens — editing a figure on one page and watching another page change — cannot be proven by fixtures. It is verified in the backend batch, and it is stated as a limit rather than faked with in-memory state. A fake backend is always tidier than the real one, which is what makes anything it proves worthless.
