# One pass, then verify — Step 6

- **One session, every call site of one decision** — not staged, and no old library left alive beside the new one.
- **Move the call sites → confirm the build → only then remove the old library.** Removed first, every remaining site becomes a build error and hides which of them was real work.
- **A replacement too large to finish in this session is not started.** Its size was measured at Step 1; where the call-site count does not fit, the decision still stands and the migration becomes a `docs/queue.md` line under `build-flow` — half a migration leaves two libraries doing one job, the `Duplicates` finding this skill exists to remove.
- **Slip in no unrelated fix**: one mistake hides among hundreds of legitimate changes.
- **Name again every dirty path from Step 0 that is a call site this pass rewrites.**

## Before reporting done

- **The build passes**, and `tsc --noEmit` or the stack's equivalent is clean.
- **Zero imports of the removed library remain** — searched again, not assumed.
- **Where the data layer moved: no database call remains outside the folder**, searched again, and every moved query returns what it returned before — the diff of a move shows an import changing and a body relocating, nothing else.
- **The unvalidated-boundary count from Step 1 has not grown.** It is allowed to stay; it is never allowed to rise.
- **A trigger chosen at L6 is smoke-checked** (`need-attribution.md`).

Any of them fails → fix it in the same session: a half-finished migration still runs, so nobody knows it is broken.

Then `floor.md`.
