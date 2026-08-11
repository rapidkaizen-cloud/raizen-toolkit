# Logic rubric — candidates per question

Used in Step 2 of `logic-init`. There is no database for this layer — a `ui-ux-pro-max` query for it returns styling rows, nothing else — so this table is maintained by hand and **re-verified at decision time**, never trusted as written.

## Admission rule

A candidate earns a row only with all three, and keeps it only while all three hold:

1. **Broad adoption** — widely used in production by many teams, not a one-maintainer experiment.
2. **Actively maintained** — recent releases, security response, no abandonment signal.
3. **Proven at scale** — known to hold up as the app grows, not just in a demo.

At decision time, run a short web check per candidate before presenting it: adoption still broad, maintenance still alive, **no fresh supply-chain event**. The check outranks the table — the axios npm compromise of March 2026 is exactly the kind of fact a static table cannot know. A candidate that fails the check is dropped from the options and reported as a finding against this file.

## The platform ladder

Before any row is offered, answer in order — stop at the first rung that holds:

1. Does the platform already provide it? (native `fetch`, `Intl`, Temporal, a DB extension)
2. Does an already-installed dependency provide it?
3. Only then: the rows below.

This ladder is why the "none" option appears in every question, and why it is the recommendation — and therefore listed first — whenever the ladder stops before the library rung. A library must beat the platform, not merely equal it; when one does, that library is the recommendation and takes the first slot, with "none" still in the list.

---

## L1 — Server-state cache

*Asked when Section 2 has a role that reads, searches, or filters records.*

| Option | Fits when | Consequence |
|---|---|---|
| **Handwritten** (effect + state) | One or two list screens, no cross-screen invalidation | Zero dependencies; every screen re-implements loading, error, and cancellation, and invalidation is manual |
| TanStack Query | Several screens read the same data, edits must reflect elsewhere, optimistic updates wanted | The de-facto standard; adds a provider at the root and a cache-key discipline every screen follows — and consciously opens the whole headless TanStack family for later needs (Table, Virtual, Form among them, not limited to them) |
| SWR | Same needs, smaller surface preferred, mutation story can stay simple | Lighter API; less machinery for optimistic updates and fine-grained invalidation; no library family behind it |

**Recommendation rule:** handwritten below roughly three list screens; TanStack Query at or above. A realtime mention in the story adds one note, not one row: the chosen cache's invalidation is the natural place to hang a realtime subscription.

A candidate that belongs to a library family names that family in its consequence — the family is part of what is being chosen. The ecosystem question is never asked on its own; it is decided inside this question, in the open.

## L2 — Validation at the trust boundary

*Asked when a server surface exists. `logic-build` §4 already mandates the parsing itself — this question only decides the tool.*

| Option | Fits when | Consequence |
|---|---|---|
| **Handwritten parse** | One handler, one or two fields | No dependency; every new field is hand-checked, and the checks drift from the types |
| Zod | Node runtime (the common case), schemas shared with the frontend | Standard choice with first-class TS inference; full build is heavyweight for Edge |
| Valibot | Edge runtime, or the validator ships to the client and bytes count | Far smaller shipped size; smaller ecosystem around it |

**Recommendation rule:** the runtime decides — Node → Zod, Edge or client-shipped → Valibot. Both implement Standard Schema, so the choice does not lock the surrounding tools; say so in the consequence.

## L3 — Dates and timezones

*Asked when Section 3 Timing & Deadlines is non-empty.*

| Option | Fits when | Consequence |
|---|---|---|
| **Platform** — `Intl` + Temporal where shipped | Formatting, day boundaries, simple arithmetic | Zero dependencies; Temporal still needs feature detection while Safari catches up, and the polyfill is heavy |
| date-fns | Arithmetic and parsing beyond what `Intl` covers, today, on every browser | Tree-shakeable and everywhere; a dependency the platform is visibly in the process of replacing |
| Day.js | Same, smallest possible footprint preferred | Tiny; plugin system carries the less-common needs |

**Recommendation rule:** platform first, always. A library enters only when a concrete rule in Section 3 exceeds `Intl` — name that rule when recommending. Whatever is chosen, the date helpers live in one extracted module (`logic-build` §7: the second occurrence extracts), so a later move to Temporal touches one file.

## L4 — Error reporting destination

*Asked when a server surface exists **and** Section 1 reads operational rather than experiment. `logic-build` §5 already mandates that the log gets the detail — this question decides where the log goes.*

| Option | Fits when | Consequence |
|---|---|---|
| **Host's built-in logs** | Experiment stage, or failures are noticed by users faster than by dashboards | Nothing to install; logs expire with the host's retention and are hard to search |
| Sentry | Someone must be told when production breaks, with stack traces grouped | The standard for error triage; one more service, one more DSN to manage |
| Axiom / structured log drain | The need is searchable history rather than alerting | Queryable logs; alerting still has to be built on top |

**Recommendation rule:** host logs until the app is operational and someone is on the hook for its failures; then Sentry. The reason recorded in the PRD must name **who reads the errors** — a destination nobody reads is the host log with extra cost.

## L5 — Where scheduled work runs

*Asked when Section 3 names a recurring run. The question is placement, not package.*

| Option | Fits when | Consequence |
|---|---|---|
| **Not yet** | The recurring rule can start as a manual action | Nothing to operate; the schedule lives in someone's calendar until automated |
| pg_cron (in the database) | The work is a query — cleanup, aggregation, expiry | No new surface; Supabase ships it; the job is invisible outside the database |
| Host cron (scheduled function) | The work calls external APIs or app code | Runs app code; one more deploy artifact, and the host's scheduler is the dependency |

**Recommendation rule:** not yet, until a rule in Section 3 actually fires on a clock nobody wants to watch. Then: pure SQL → pg_cron; anything touching an external API → host cron.

---

## Maintaining this file

A row is added or dropped only with the admission rule re-checked, and the change says why — the same discipline as the stack rubric in `app-init`. Category names (the L-numbers and their questions) are the stable part; candidate names are expected to turn over.
