# Install — Step 5

**One block, one approval, answered in chat at a hard stop — never an AskUserQuestion**, because a dialog covers the very block the user must read. Present it, end the turn, wait.

```
Will install:
  <library>          [which need, one line why]
  <linter>           [only where the repo carries none — Step 7's floor is written into it]
Will remove:
  <old library>      [at Step 6, after the call sites move — not now]
Will migrate:
  <need>             [N call sites across M files]
  data layer         [M files calling the database outside <folder> — moved into it at Step 6]
```

- **Refused → hand over the commands, then wait.**
- **Install nothing outside the block**; something extra turns out to be needed → ask again, never slip it in.
- **The data-layer line is a migration like any other: priced in files, and declinable.** Declined → those files are baselined at Step 7, and the floor still refuses every new one. Approved → each query moves into the folder unchanged in behaviour, its page importing the function instead; too large for this session → a `docs/queue.md` line under Step 6's rule (`pass.md`), never half a move.
- **A trigger chosen at L6 installs nothing** and has its own smoke check: `need-attribution.md`, Once the trigger is chosen.
- **After installing, one smoke check**: a single throwaway usage that exercises each library, `tsc --noEmit` (or the stack's equivalent) passing, then the throwaway is deleted.
- **Draw no canvas**: a library choice is judged by the build passing and by use, and its first real use arrives with the first page.
- When writing against a chosen library later, the installed `docs-lookup` skill (Context7) can pull current documentation — a pointer, not a dependency.

Something is replaced or moved → `pass.md`. Otherwise → `floor.md`.
