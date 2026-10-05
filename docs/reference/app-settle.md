# app-settle

Running it settles an app repo at the app level — what the app is for, who uses it, the rules it enforces, the stack it runs on — writes the documents that hold it, and brings an existing repo back onto the installed rules.

| | |
|---|---|
| Kind | Settle skill — runs only when you invoke it |
| Run | `/raizen-norms:app-settle` |
| Run it when | You start an app, document or migrate an existing one, check whether a repo follows the current rules, or want to re-plan one |
| Needs first | Nothing in an empty directory. Migrate and Align need a git repo with a clean working tree. A session never works on `main` |
| Writes | By mode: `docs/PRD.md` and the living documents it seeds, `CLAUDE.md`, `AGENTS.md`, `.claude/settings.json`, the root `README.md`. Align also changes existing code and agent files |
| Commits | Yes, by the `GIT` block of the session norms, paths named, when a mode has finished writing. Align makes one commit per finding |
| Source | `skills/app-settle/SKILL.md`, `skills/app-settle/references/` |

## What happens

Step 0 reads the directory and the code first, the documents as evidence. It prints one block — `Directory`, `Documents`, `CLAUDE.md`, `AGENTS.md`, `Git`, `Plugin`, `Mode`, `Owed after`, `Flow` — and names the fact that produced the mode. You can overrule the mode in one line.

| Step 0 finds | Mode | Kind | What it does |
|---|---|---|---|
| Nothing | **Bootstrap** | Decision | Interviews the domain and the stack from zero, writes `docs/PRD.md`, seeds the living documents, scaffolds, runs `git init` |
| Application code, no PRD in either form | **Document** | Decision | Writes the documents; changes nothing about the app |
| A root `PRD.md` | **Migrate** | Mechanical | Moves the legacy documents into the `docs/` form, word for word, in one commit |
| `docs/PRD.md`, no change asked for | **Align** | Mechanical | Audits the repo against the installed rules, ranks the findings, fixes the ones you pick |
| `docs/PRD.md`, you want the app itself to change | **Rework** | Decision | Re-runs the interview, every decision starting from what the app already does |

One session runs one mode, in the order a repo owes them: Document, then Migrate, then Align or Rework. Decision work changes no existing code; every line it writes comes from one of your answers. Mechanical work changes what exists only where an installed rule already says how, and drops whatever turns out to need a decision. A `docs/PRD.md` with a living document missing gets only those documents seeded and reported, and the run closes.

### Bootstrap — N1 to N6

1. **N1, the domain.** One invitation to talk freely, then a one-paragraph reading and a stop for your correction. Then six themes, asked openly with no options: the problem before the app, who uses it and how they work without the app, the work each role must finish, business rules **and the reason behind each number**, domain terms easy to misread, non-goals.
2. **N2, the stack.** Eight questions, up to four per call: kind of app, platform, framework and rendering, frontend hosting, database and login, which database, database environments, testing. Each option carries a one-sentence consequence, and each question a marked recommendation except frontend hosting and which database, which carry none. Then the derived lines (language, package manager, migrations, styling) and the defaults not asked, in one message for you to change. The component library is not asked here; `design-settle` asks it.
3. **N3, the summary.** One message, then a stop for your approval.
4. **N4, `docs/PRD.md`.** Frozen from the moment it is written. It seeds `docs/product.md`, `docs/rules.md`, `docs/glossary.md` and one record per answered stack question in `docs/decisions/`, then `docs/README.md` and the root `README.md`.
5. **N5, scaffold.** `CLAUDE.md`, `AGENTS.md`, `.claude/settings.json`; `supabase/config.toml` for Supabase Cloud only; a host rewrite rule for a static SPA only; a CI workflow only if you ask. Every file is written for your answers, never copied. Then `git init`, `git branch -M main`, the one commit `main` ever takes directly, and `development` created and switched to.
6. **N6, close.** The files created, and what you must do by hand: create the database project (and its staging counterpart if question 7 asked for one) and connect it. It says plainly when there is no staging. It offers `/logic-settle`, then `/design-settle`, unless the product has no UI. `raizen-norms` becomes active once the next session starts in this repo.

**Pioneer and Not ready.** A Pioneer option opens with `Pioneer —` and what does not exist for it yet. Picking one, or typing a platform outside the list, adds three lines — no rubric row, no repo that has run it, what the destructive guard covers — and one confirmation; declining routes back to a Ready platform (`references/pioneer.md`). A Not ready option is never offered, but one you name is accepted with what you must set up yourself. A non-SQL store first gets a notice that the destructive guard does not cover it, then a question whether to proceed.

### Document — D1 to D6

1. **D1.** A subagent reads the stack from the repo into a `STACK` block. Nothing in it is asked.
2. **D2 and D3.** The story and reading as above; the reading says which parts drew on the code. Roles, rule values and terms read from code are shown with their `file:line` and confirmed. The problem before the app, how the work was done then, and the non-goals are asked openly. The locale is confirmed.
3. **D4.** The summary, then a stop. **D5.** `docs/PRD.md`, the living documents, `CLAUDE.md`, `AGENTS.md`, `.claude/settings.json`, then a commit. The stack is recorded as found and no decision record is seeded. An existing `CLAUDE.md`, `AGENTS.md` or root `README.md` is never overwritten.
4. **D6.** A block — `Written`, `Not read`, `Unverified`, `Findings`, `DESIGN.md` — then `/logic-settle`, `/design-settle` and `/app-settle` in that order. `Findings` holds only concrete stack findings; "you would have picked differently" is not one.

### Migrate — M1 to M5

1. **M1.** Reads, prints a `MIGRATE` block of counts, and says whether the repo can move. An off-shape `PRD.md`, or a Section 5 of the adopted-whole shape, cannot: it names the blocker and what clears it, changes nothing, and offers Align or Rework.
2. **M2 and M3.** `git mv` of `PRD.md` and `QUEUE.md` into `docs/`, one `Frozen` line under the PRD's title, then the living documents written from it. `DESIGN.md` is written from Section 5 as a change of format, never of design; with Section 5 empty, absent or all `[needs verification]`, none is written.
3. **M4.** Corrects what still names the old form, in `CLAUDE.md`, `AGENTS.md`, `README.md` and other files, and writes `docs/README.md` last.
4. **M5.** Proves the counts, the rule-test titles, the linter and the session start, then makes one commit and prints `MIGRATED`. `git revert` undoes it.

### Align — A1 to A5

1. **A1.** One subagent audits the repo against the installed plugin copy and returns an `AUDIT` block: `C1 platform residue`, `C2 agent files`, `C3 language split`, `C4 guard coverage`, `C5 documents`, `C6 lint floor`, `C7 rule coverage`. Every row reports, a clean one included.
2. **A2 and A3.** A table ranked by what breaks without anyone noticing, in three bands: a guarantee that does not hold, a rule that points somewhere wrong, drift that is merely untidy. You pick through a question: band 1 only, bands 1 and 2, everything, or nothing.
3. **A4.** One finding per commit, named paths. A build or run config gets one real run first; a lint floor is proven before its commit.
4. **A5.** An `ALIGN` block: `Fixed`, `Dropped`, `Left`, `Still silent`, `Verified`, `For app-eval`. An empty audit is a normal ending.

### Rework — R1 to R6

1. **R1 and R2.** A subagent reads the stack and returns a `DRIFT` block; then what hurts, and a reading you correct. A rework touching only the design system closes and points to `design-settle`.
2. **R3.** Only the decisions the story touched, plus those their change forces open. Each shows what the app does today, with `keep` as the first option at no cost; a domain question shows the current value and asks openly for the changed value. The stack is on trial here.
3. **R4 to R6.** A summary and a stop, then edits to the sections touched, then a block of `Changed`, `Kept`, `Drift`, `Execution`, `Unverified`, `DESIGN.md`. The execution is named, never started.

## What it asks you

| Question | What your answer decides |
|---|---|
| The mode, when Step 0 reads it wrong | One line overrules it |
| Align or Rework | A wish to change what the app does, whom it serves or what it runs on makes it Rework; none stated, Align |
| Continue here or move | Whether bootstrap runs in a directory holding files that are neither code nor a PRD |
| Create `development` from `main`; `git init` | Where the session works; Migrate and Align need a repo |
| The six themes | The documents' content; no options, because options would steer the answer |
| The eight stack questions | The stack, with `docs/decisions/` records of the choice |
| Which bands to fix (Align) | What gets one commit each |
| Keep or change, per decision (Rework) | What the documents record; a changed number needs a reason of its own |

## Where it stops

- **Step 0.** Files that are neither code nor a PRD in a directory read as bootstrap; branch `main`; no git repo before Migrate or Align; a dirty working tree before Migrate or Align (until you commit or stash).
- **The reading.** After N1, D2 or R2, until you correct or confirm it.
- **The summary.** N3, D4 and R4 are one message each. No file is written until you approve.
- **Align's ranked table.** Until you pick, including "nothing".

## What it never does

- **Open on its own initiative.** A session that finds a problem reports it in one line, or offers this skill once with the evidence. Declining closes the matter for that session.
- **Write outside `docs-format`'s closed list.** No `ARCHITECTURE.md`, `CHANGELOG.md`, interview summary or audit report as a file. `docs/queue.md`, `docs/guide/`, `docs/whats-new.md` and `docs/changes/` are written by building sessions; Migrate moves a root `QUEUE.md` and Align writes queue lines.
- **Write `DESIGN.md`** apart from Migrate's conversion of Section 5. It stays absent after Bootstrap and Document and untouched after Rework.
- **Invent.** An unsettled point is written `[needs verification]`. "I don't know" to a reason is written as given.
- **Put a secret in a file**, or ask for a token: it names the variable.
- **Change the app in Document or Rework.** No dependency, refactor, migration or bug fix; code catches up in building sessions. Bootstrap adds no dependency without your approval.
- **Re-open a decision in Align**, or edit a frozen record. A finding that needs a decision is dropped and reported.

## Related

- [logic-settle](logic-settle.md) and [design-settle](design-settle.md), the next two sessions
- [Documents](../concepts/documents.md) and [docs-format](docs-format.md), what gets written
- [Session norms](../concepts/session-norms.md), the `GIT` block
- [Starting an app](../guide/new-app.md), [existing app](../guide/existing-app.md), [maintain app repos](../guide/maintain-app-repos.md)
