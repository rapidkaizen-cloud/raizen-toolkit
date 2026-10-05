# Migrate — a legacy repo moves to the `docs/` form

Mechanical work: every sentence lands in the document `docs-format`'s legacy map sends its section to, **word for word**. Only headings change, to the ones the shapes name. Nothing is re-decided, improved, reworded, or translated; what looks wrong is a line in the close block.

## M1 — Read, then say whether it can move

Read in one turn: `PRD.md` whole, `QUEUE.md`, a root `DESIGN.md`, `CLAUDE.md`, `AGENTS.md`, and of `docs-format` both `references/legacy.md` and `references/shapes.md`. Search the repo for every other file naming `PRD.md`, `QUEUE.md`, or a PRD section number. Print one block:

```
MIGRATE
PRD.md     : [N lines · six sections located]  or  [off-shape — the section that cannot be located]
Section 3  : [N rules — table rows and list items — in N groups]
Section 4  : [N terms]
Section 5  : [ratified / every line [needs verification] / absent / adopted-whole]
DESIGN.md  : [generated copy at the root / none]
Decisions  : [N decision lines in Section 1]
QUEUE.md   : [N lines / absent]
Names it   : [N files outside the documents naming PRD.md, QUEUE.md or a section number]
```

**A section is located by its number, whatever language or decoration its heading carries.**

**Two repos cannot move mechanically, and stay legacy for this run:**

- **Off-shape** — a section cannot be located, so its sentences have no known destination. Reshaping `PRD.md` to `legacy.md`'s shape clears it.
- **Section 5 of the adopted-whole shape** — the `docs/` form has no place for it. `design-settle` replaces it with a ratified one, and that clears it.

Name the blocker and what clears it, change nothing, and offer align or rework on the repo as it stands.

Otherwise carry on without asking: the whole move is one commit, and `git revert` undoes it.

## M2 — Move

`git mv PRD.md docs/PRD.md`, and `git mv QUEUE.md docs/queue.md` where it exists. Under the title of `docs/PRD.md` add one line, and change nothing else in it, ever:

```
Frozen YYYY-MM-DD — the legacy PRD as it stood when this repo moved to the docs/ form. History, not current truth: the living documents are listed in docs/README.md.
```

Then write the living documents from it, each under the headings `shapes.md` gives. **Match a part by what it holds** — its own heading or bold label, in whatever language, is dropped for the shape's.

| From | To | How |
|---|---|---|
| Section 1 — the Context table, the Proof profile, problem, success, non-goals | `docs/product.md` | Copied under the headings of its shape. No Proof profile in the PRD → none is written |
| Section 1 — the decision lines | `docs/decisions/`, one record per line | The choice and its reason as the outcome; `date` is today's. A non-goal naming an alternative rejected for that choice moves into the record as a considered option. A part of the shape the line gives nothing for is left out, never invented |
| Section 2 | `docs/product.md` — Roles | Copied |
| Section 3 | `docs/rules.md` | Below |
| Section 4 | `docs/glossary.md` | Copied |
| Section 5, ratified | `DESIGN.md` | M3 |
| Section 6 | `docs/product.md` — Prohibitions | Copied |

**Section 3: each sub-section becomes a `##` group, each rule a `###` topic with its text under it, whole.**

- **A table row** → the topic is its first cell, verbatim, because a rule test's title quotes it. The other cells follow as `<column>: <cell>` lines, a `Why` column as `Why:`.
- **A list item or a paragraph** → the topic is its bold lead-in, or without one its first sentence, verbatim. The rest follows unchanged.
- **No `Why` column → no `Why:` line.** A reason the rule's own text gives stays in that text; none is extracted and none invented.
- **A sub-section's lead paragraph stays under its group heading.**

Four rules for the whole move:

- **A number, a term, a name leaves exactly as it arrived.**
- **A paragraph the map sends nowhere** — status, history, a list of screens, a part the shape has no heading for — enters no living document. It stays in `docs/PRD.md`; name it in the close block.
- **Write `docs/README.md` last** — the index of what now exists.
- **Write no `docs/guide/`, `docs/whats-new.md` or `docs/changes/`**: they describe pages and changes, and align lists the guide pages the app now owes.

## M3 — `DESIGN.md`, from a ratified Section 5

The one time this skill writes `DESIGN.md`: a change of format, never of design. Read `design-settle`'s `references/design-md.md`, and the format's live spec as that file orders.

- **The body is Section 5's sub-sections under the format's headings**, by the table in `legacy.md`, each matched by what it holds. The headings as the format writes them; the text under them untouched.
- **A sub-section that table sends nowhere stays a section of its own**, under its own heading, after the toolkit's two — the format keeps an unknown section.
- **A format heading Section 5 holds nothing for is left out.**
- **The lines above Section 5's first sub-section are not carried** — how it was decided, that the PRD is the source. They stay in `docs/PRD.md`.
- **Frontmatter.** A generated `DESIGN.md` at the root → keep its frontmatter: its tokens are the ratified values. None → `version`, `name`, and one `omitted` entry per token group, its `reason` that the values live in the styling files and `design-settle` writes the tokens.
- **Never derive a token here**: one transcribed wrong becomes the norm the styling files are then measured against.
- **Run the linter `design-md.md` names — zero errors.** An error only a design decision would clear → restore the working tree to `HEAD`, delete the files this run created, and treat the repo as one of M1's blocked ones.

**Section 5 empty, every line `[needs verification]`, or absent → write no `DESIGN.md`, and delete a generated one.** `ui-build`'s gate holds until `design-settle` runs, as it held before.

## M4 — What still names the old form

Read `scaffold.md` for the two shapes, then:

- **`CLAUDE.md`** — rewrite the lines naming `PRD.md`, a section number, or `QUEUE.md` to what its shape says of the `docs/` form. Nothing else in it moves.
- **`AGENTS.md`**, where present — its `## Read first` part, and the `## UI` and `## Logic` lines naming a section, to its shape. Absent → not created here; align's C2 owes it.
- **`README.md`** — correct a line naming `PRD.md` or `QUEUE.md`. Add nothing.
- **The moved text itself** — a pointer to `PRD.md` or to a section number is corrected to the document that now holds it. A sentence that is about the PRD rather than pointing at it is reported, never reworded.
- **Every other file M1 counted** — correct a path; report prose.

## M5 — Prove, then one commit

Commit nothing until all of these hold:

- **The counts match M1** — rules and topics, terms, decision lines and records, queue lines — and every role, non-goal and prohibition arrived.
- **Every rule-test title that quoted a Section 3 topic finds its `###` heading.**
- **`DESIGN.md` passes its linter**, where M3 wrote it.
- **No root `PRD.md` and no root `QUEUE.md` remain.**
- **The session start reads the `docs/` form**: run `scripts/session_norms.py` of the plugin folder this skill is read from, with `{"cwd": "<repo root>"}` on stdin. It opens with the `docs/` form's block and names no missing document. A stale path it names is the legacy text's own — report it, never fix it here.

One fails → fix the move, never the check. Then one commit, paths named.

```
MIGRATED
Moved       : PRD.md → docs/PRD.md, frozen · QUEUE.md → docs/queue.md
Written     : docs/README.md · product.md · rules.md [N topics] · glossary.md · decisions/ [N records]
              DESIGN.md [converted, tokens kept / converted, tokens owed by design-settle / absent — design-settle owes it]
Corrected   : [CLAUDE.md · AGENTS.md · README.md · other files — N lines each]
Not carried : [paragraphs left in docs/PRD.md only — or "none"]
Reported    : [sentences about the PRD left as they were · stale paths — or "none"]
No Why      : [N topics with no Why: line — the PRD marked none]
Verified    : [each check above, as run]
Commit      : [hash]
```

Say what the repo owes next, and run none of it: `/raizen-norms:app-settle` again audits it for align, where the guide pages it owes are listed.
