# Logic rubric — categories, criteria, and the research duty

Used in Step 3 of `logic-settle`. There is no database for this layer. **This file names no candidates.** It holds the questions, the criteria a candidate must meet, and the rules for recommending; the candidates themselves are assembled live, per the research duty below. A product name written here would only go stale and then anchor the interview to its staleness.

## Assembling candidates — the research duty

Candidates are assembled at decision time, per scored need:

1. **The model's own knowledge proposes** — the libraries a working developer would name for this category today.
2. **Web research verifies every candidate before it may be offered.** Per candidate: adoption still broad, maintenance still alive, no fresh supply-chain event or advisory, and what it brings versus what it leaves out — that last pair becomes the option's one-sentence consequence. One research pass may cover all candidates of the interview; what is mandatory is the coverage per option, never one search per option.

**An option without researched backing is not shown.** Zero candidates surviving verification → say so plainly and offer handwritten; never pad the list, and never present memory alone as if verified.

## Admission rule

A candidate earns a place in the options only with all three:

1. **Broad adoption** — widely used in production by many teams, not a one-maintainer experiment.
2. **Actively maintained** — recent releases, security response, no abandonment signal.
3. **Proven at scale** — known to hold up as the app grows, not just in a demo.

This rule is what keeps the research pass from seating this week's trending library. The user naming a candidate that fails it still gets it — with the failure stated as its consequence.

## The platform ladder

Before any candidate is offered, answer in order — stop at the first rung that holds:

1. Does the platform already provide it? (native `fetch`, `Intl`, Temporal, a DB extension)
2. Does an already-installed dependency provide it?
3. Only then: researched candidates.

This ladder is why the "none" option appears in every question, and why it is the recommendation — and therefore listed first — whenever the ladder stops before the library rung. A library must beat the platform, not merely equal it; when one does, that library is the recommendation and takes the first slot, with "none" still in the list.

A candidate that belongs to a library family names that family in its consequence — the family is part of what is being chosen, because an installed member shifts later recommendations (`design-init` reads PRD Section 1). The ecosystem question is never asked on its own; it is decided inside the need's question, in the open.

---

## L1 — Server-state cache

*Asked when Section 2 has a role that reads, searches, or filters records.*

**Candidates are measured on:** cross-screen invalidation, optimistic-update support, the discipline the cache imposes (a root provider, a cache-key convention every screen follows), and whether a library family rides along — a family is a consequence to name, in both directions.

**Recommendation rule:** handwritten (effect + state) below roughly three list screens — zero dependencies, at the price of every screen re-implementing loading, error, and cancellation, with manual invalidation; the researched de-facto standard at or above three. A realtime mention in the story adds one note, not one candidate: the chosen cache's invalidation is the natural place to hang a realtime subscription.

## L2 — Validation at the trust boundary

*Asked when a server surface exists. `logic-build` §4 already mandates the parsing itself — this question only decides the tool.*

**Candidates are measured on:** first-class type inference, shipped bundle size, and runtime fit — a validator that is comfortable on Node may be heavyweight for Edge or for shipping to the client.

**Recommendation rule:** the runtime decides — Node → the ecosystem standard; Edge, or a validator that ships to the client where bytes count → the smallest shipped size that holds the admission rule. Prefer candidates implementing Standard Schema, so the choice does not lock the surrounding tools — say so in the consequence. Handwritten parsing fits one handler with one or two fields, and its consequence is that the checks drift from the types as fields accrete.

## L3 — Dates and timezones

*Asked when Section 3 Timing & Deadlines is non-empty.*

**Candidates are measured on:** what they cover beyond `Intl` and Temporal, tree-shakeability and footprint, and how visibly the platform is in the process of absorbing them — a date library is a dependency the web is actively replacing, and that is a consequence to state.

**Recommendation rule:** platform first, always — `Intl` for formatting and day boundaries, Temporal where shipped (it still needs feature detection, and its polyfill is heavy). A library enters only when a concrete rule in Section 3 exceeds what the platform covers — name that rule when recommending. Whatever is chosen, the date helpers live in one extracted module (`logic-build` §7: the second occurrence extracts), so a later move to Temporal touches one file.

## L4 — Error reporting destination

*Asked when a server surface exists **and** Section 1 reads operational rather than experiment. `logic-build` §5 already mandates that the log gets the detail — this question decides where the log goes.*

**The options are destination categories, researched into named services at decision time:**

| Category | Fits when | Consequence shape |
|---|---|---|
| **Host's built-in logs** | Experiment stage, or failures are noticed by users faster than by dashboards | Nothing to install; logs expire with the host's retention and are hard to search |
| An error-triage service | Someone must be told when production breaks, with stack traces grouped | One more service and one more credential to manage — research which service currently owns this category |
| A structured log drain | The need is searchable history rather than alerting | Queryable logs; alerting still has to be built on top |

**Recommendation rule:** host logs until the app is operational and someone is on the hook for its failures; then the researched triage service. The reason recorded in the PRD must name **who reads the errors** — a destination nobody reads is the host log with extra cost.

## L5 — Where scheduled work runs

*Asked when Section 3 names a recurring run. The question is placement, not package — every option is a platform rung, and nothing here is researched as a product.*

| Option | Fits when | Consequence |
|---|---|---|
| **Not yet** | The recurring rule can start as a manual action | Nothing to operate; the schedule lives in someone's calendar until automated |
| pg_cron (in the database) | The work is a query — cleanup, aggregation, expiry | No new surface; Supabase ships it; the job is invisible outside the database |
| Host cron (scheduled function) | The work calls external APIs or app code | Runs app code; one more deploy artifact, and the host's scheduler is the dependency |

**Recommendation rule:** not yet, until a rule in Section 3 actually fires on a clock nobody wants to watch. Then: pure SQL → pg_cron; anything touching an external API → host cron.

## L6 — Change attribution

*Asked when Section 2 gives a role the power to change or delete records another role created, or Section 3 Approval is non-empty.*

This question does not pick a package, and **it is deliberately exempt from the research duty**: its mechanism is a Postgres API stable for a decade, and the two product names below are trap warnings that a fresh research pass would get wrong — research surfaces pgaudit as if it answered this question, and rejects supa_audit for being archived, which is exactly backwards.

**The options are resolved from the database already chosen in `app-init`**, because the only layer that knows which application user made a change is the one the database itself provides, and that differs per platform. Present the resolved option, never a cross-platform menu.

| Database (Stack table of `CLAUDE.md`) | What the trigger option resolves to |
|---|---|
| Supabase | `SECURITY DEFINER` trigger; actor from `auth.uid()`, falling back to a session setting |
| Another Postgres | The same trigger; actor from a session setting only — there is no `auth.uid()` |
| No database | Not asked |

| Option | Fits when | Consequence |
|---|---|---|
| **Trigger → append-only audit table** | Someone will one day be asked who changed a record, and the answer has to exist | Cannot be bypassed — a write through the SQL editor, a scheduled function, or a migration is recorded like any other; costs write throughput and storage on every tracked table |
| Written by the app on the mutation path | The entry must carry intent — a reason, a ticket, a customer's phone call — which the database cannot see | Reads well for a human; every write that does not go through the app leaves no trace |
| **None** | No role touches another role's records, and nobody has asked who did what | Nothing to build; history before the day this is added is gone permanently and cannot be reconstructed |

**Recommendation rule:** the trigger, whenever the need scored yes. This is the one question where "none" is not the platform-ladder default — the platform does provide the mechanism, so choosing it *is* the ladder stopping at rung one. The app-layer option is reached for only as a **second** table alongside the trigger, and only once someone has read the audit and found the raw diff unreadable.

**The admission rule of this file does not apply to this question.** No maintained library is being chosen; the mechanism is a trigger against a Postgres API that has been stable for a decade, so "actively maintained" has nothing to attach to. Supabase's own [supa_audit](https://github.com/supabase/supa_audit) is archived and is still the right design to copy: one `audit.record_version` table, a `record_id` derived from the primary key so one record's history is an indexed lookup rather than a scan, and an index on `table_oid`. Copy the SQL into a migration and own it — do not install it. Do not offer pgaudit as an alternative here: it logs statements rather than values, and answers a different question.

The reason recorded in the PRD must name **who reads the audit and to settle what** — the same discipline as L4. An audit nobody opens is write throughput spent on storage.

Three consequences are stated when this question is asked, because all three are expensive to discover later.

**The snapshot outranks RLS.** An audit row holds the whole record as jsonb, and neither the base table's RLS nor its column privileges reach inside it. The moment a role that cannot see a column is allowed to read that record's history, the audit table becomes the way around the restriction. Before this question is closed, check the tables about to be tracked for columns not every role may read, and if any exist, say so and hand the user the fork: filter on read (the audit stays complete, the view is narrowed) or filter on write (simpler, and the evidence is permanently incomplete). Recommend filtering on read — an audit with holes is not an audit.

**The `service_role` gap.** Under `service_role` — Edge Functions, cron, admin scripts — `auth.uid()` is null, and those are the paths that make the largest changes. The trigger reads a session setting as fallback, and the server sets it before writing:

```sql
select set_config('app.actor_id', '<uuid>', true);
-- in the trigger
coalesce(auth.uid(), nullif(current_setting('app.actor_id', true), '')::uuid)
```

**Tracking is per table, never global.** Track only the tables whose changes people argue about. Tracking everything is the fastest route to a storage bill whose output nobody reads.

---

## Maintaining this file

What this file maintains is the stable part: the L-numbers and their questions, the admission rule, the ladder, and the per-question criteria. **Candidate names are never written back into it** — a session that learns a name records the choice and its reason in the app's PRD, and the next session researches fresh. A criterion is added or dropped only with a stated reason — the same discipline as the stack rubric in `app-init`.
