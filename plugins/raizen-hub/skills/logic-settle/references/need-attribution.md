# L6 — Change attribution

**This question picks no package, and neither the research duty nor the admission rule of `logic-rubric.md` applies to it**: the mechanism is a trigger against a Postgres API stable for a decade, so "actively maintained" has nothing to attach to — and a fresh research pass gets the two product names below backwards, surfacing pgaudit as if it answered this question and rejecting supa_audit for being archived.

## The options

**Resolve the trigger option from the database already chosen in `app-settle`, and present the resolved option, never a cross-platform menu** — the only layer that knows which application user made a change is the one the database itself provides.

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

**Recommendation rule:** the trigger, whenever the need scored yes. This is the one question where "none" is not the platform-ladder default — the platform provides the mechanism, so choosing it *is* the ladder stopping at rung one. The app-layer option is reached for only as a **second** table alongside the trigger, and only once someone has read the audit and found the raw diff unreadable.

**Never offer pgaudit as an alternative**: it logs statements rather than values, and answers a different question.

## Three consequences, stated when the question is asked

**The snapshot outranks RLS.** An audit row holds the whole record as jsonb, and neither the base table's RLS nor its column privileges reach inside it: once a role that cannot see a column may read that record's history, the audit table is the way around the restriction. Before this question is closed, check the tables about to be tracked for columns not every role may read; if any exist, say so and hand the user the fork: filter on read (the audit stays complete, the view is narrowed) or filter on write (simpler, and the evidence is permanently incomplete). Recommend filtering on read — an audit with holes is not an audit.

**The `service_role` gap.** Under `service_role` — Edge Functions, cron, admin scripts — `auth.uid()` is null, and those are the paths that make the largest changes. The trigger falls back twice: a request header for writes through the API, where supabase-js runs each call in its own transaction so a session setting is gone before the write; and a transaction-local setting for SQL paths — a cron job, a migration, the SQL editor. The header counts only under `service_role`, or any client could name its own actor:

```sql
-- server, supabase-js: createClient(url, secretKey, { global: { headers: { 'x-actor-id': actorId } } })
-- SQL paths, in the write's own transaction:
select set_config('app.actor_id', '<uuid>', true);
-- in the trigger (nullif: a reset setting reads '' in a pooled session, and ''::jsonb raises)
coalesce(
  auth.uid(),
  case when nullif(current_setting('request.jwt.claims', true), '')::jsonb->>'role' = 'service_role'
       then nullif(nullif(current_setting('request.headers', true), '')::jsonb->>'x-actor-id', '')::uuid end,
  nullif(current_setting('app.actor_id', true), '')::uuid
)
```

**Tracking is per table, never global.** Track only the tables whose changes people argue about — tracking everything buys a storage bill whose output nobody reads.

## Once the trigger is chosen

- **Copy the design, never install it.** Supabase's own [supa_audit](https://github.com/supabase/supa_audit) is archived and is still the right design to copy: one `audit.record_version` table, a `record_id` derived from the primary key so one record's history is an indexed lookup rather than a scan, and an index on `table_oid`. Copy the SQL into a migration and own it.
- **The audit is read through one function, never by exposing its schema.** The `audit` schema stays out of the API; the reader the Roles name gets one `SECURITY DEFINER` function in an exposed schema that checks that role inside and returns one record's history by `record_id`. Filtering on read lives in that function.
- **Step 4 — the record.** A trigger is not a library, so nothing goes in the Stack table: the decision record and the migration are the whole record. Its reason names **what the audit settles**; who reads it is the Roles line handed over at Step 8, never repeated in the record. Write the tracked tables as a criterion, never as a list — "tracked wherever one role can change another role's records" — because table names go stale on the next feature.
- **Step 5 — the block.** The trigger installs nothing: it goes in the same block, named as a migration rather than a package, and is applied the way every other schema change in this repo is applied.
- **Its smoke check**, because a trigger never passes through the compiler: as an authenticated user, not `service_role`, write and then delete one throwaway row in a tracked table, and confirm three audit rows exist with the actor filled in. Where the app writes under `service_role`, repeat it through that client carrying the actor header. A null actor means the fallback is wired wrong. Then delete the throwaway rows from the audit table too — the only moment deleting from it is correct.
- **Step 8 — the Roles line.** Who may read the audit, and whose records they may read, belongs to the Roles in `docs/product.md`, which this skill does not write. Hand the user the line the Roles now need and say plainly that it is theirs to add — a recording nobody is allowed to read costs the same as no recording.
