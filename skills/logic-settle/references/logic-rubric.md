# Logic rubric — the research duty, the admission rule, the ladder

Used at Step 3 of `logic-settle`, beside one need file per need asked. There is no database for this layer. **This file and the need files name no candidates** — they hold the questions, the criteria a candidate must meet, and the rules for recommending; a product name written here goes stale and then anchors the interview to its staleness.

## Assembling candidates — the research duty

Per scored need, at decision time:

1. **The model's own knowledge proposes** — the libraries a working developer would name for this category today.
2. **A verification pass checks a candidate live before it counts as verified**, in one subagent (`SKILL.md`, What a run costs) briefed with this file, the need files asked, and the candidates. Per candidate: adoption still broad, maintenance still alive, no fresh supply-chain event or advisory, and what it brings versus what it leaves out — that last pair becomes the option's one-sentence consequence. One pass covers every candidate handed to it, never one search per option.
3. **It returns one line per candidate**: the verdict on each admission point · any supply-chain event or advisory · what it brings · what it leaves out.

**Verify the recommendation of every question before it is asked.** Offer every other option from model knowledge, marked `unverified` in its description, and verify it only when it is picked — one pass for everything picked. A pick that fails verification re-opens that question once, naming what failed.

**Never present memory as verified, and never pad the list.** A recommendation that fails is replaced, and its replacement verified; zero candidates surviving → say so plainly and offer handwritten.

## Admission rule

A candidate earns a place in the options only with all three — this is what keeps this week's trending library out:

1. **Broad adoption** — widely used in production by many teams, not a one-maintainer experiment.
2. **Actively maintained** — recent releases, security response, no abandonment signal.
3. **Proven at scale** — known to hold up as the app grows, not just in a demo.

A candidate the user names that fails it is still used — with the failure stated as its consequence.

## The platform ladder

Before any candidate is offered, answer in order and stop at the first rung that holds:

1. Does the platform already provide it? (native `fetch`, `Intl`, Temporal, a DB extension)
2. Does an already-installed dependency provide it?
3. Only then: researched candidates.

**"None" is an option in every question.** It is the recommendation, and therefore listed first, whenever the ladder stops before the library rung. A library must beat the platform, not merely equal it; one that does is the recommendation and takes the first slot, "none" still in the list.

**A candidate that belongs to a library family names that family in its consequence**, because an installed member shifts later recommendations (`design-settle` reads the decision records). Never ask the ecosystem question on its own: decide it inside the need's question, in the open.

## Maintaining the rubric

The stable part is the L-numbers and their questions, the admission rule, the ladder, and the per-need criteria. **Never write a candidate name back into this file or a need file** — a session that learns one records the choice and its reason in the app's decision records, and the next session researches fresh. Add or drop a criterion only with a stated reason — the same discipline as the stack rubric in `app-settle`.
