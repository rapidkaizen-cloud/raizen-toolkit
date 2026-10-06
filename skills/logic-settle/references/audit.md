# The audit — a subagent's brief, Step 1

You audit the logic layer an app runs today, for a session that decides what it adopts. **Read what the repo actually does, never what the decision records claim.** Change nothing and fix nothing: every hit is a finding. Write no file. Run independent reads, searches and commands in one turn. Documents are named by their `docs/` path; a repo with a root `PRD.md` reads each through `docs-format`'s legacy map.

## What you report back

Only the filled block, and under it the database client package and the paths behind `M unvalidated` and `M of them outside it`, one per line. No file contents, no advice.

```
AUDIT
L1 cache       : [library · version]  or  [handwritten — N fetch sites]  or  [no list screens]
L2 validation  : [library · version]  or  [handwritten — N boundary handlers, M unvalidated]  or  [no server surface]
L3 dates       : [library · version]  or  [platform Intl]  or  [raw Date arithmetic — N sites]
L4 errors      : [service]  or  [host log only]  or  [swallowed — N empty catch blocks]
L5 jobs        : [where they run]  or  [none found]
L6 attribution : [trigger on N tables]  or  [application-side]  or  [none]
Data layer     : [folder · N files call the database · M of them outside it]  or  [no database calls yet]
                 or  [n/a — no database and no remote API]
Health         : [unmaintained · past EOL · known advisory — per library, or "clean"]
Duplicates     : [two libraries covering one need]
Call sites     : [per library, how many files import it]
Deviates       : [per decision recorded that the code does not follow]
```

## How the rows are read

- **Fill every row on every repo.** No application code → every row empty, in one pass.
- **Count the unvalidated boundary handlers always** — route handlers, server actions, edge functions taking input — also where L2 names a library: a validator installed but not applied at every boundary is a security finding, not a library finding.
- **`Data layer` is measured**: count the files that import or call the database client, group them by folder, and name the folder holding most of them and how many sit outside it.
- **`Duplicates`** — two date libraries, or two validators. A library beside handwritten code for the same need is that need's question, never a duplicate.
- **`Deviates`** — one line per record under `docs/decisions/` the code does not follow.
