# L5 — Where scheduled work runs

The question is placement, not package — every option is a platform rung, and nothing here is researched as a product.

| Option | Fits when | Consequence |
|---|---|---|
| **Not yet** | The recurring rule can start as a manual action | Nothing to operate; the schedule lives in someone's calendar until automated |
| pg_cron (in the database) | The work is a query — cleanup, aggregation, expiry | No new surface; Supabase ships it; the job is invisible outside the database |
| Host cron (scheduled function) | The work calls external APIs or app code | Runs app code; one more deploy artifact, and the host's scheduler is the dependency |

**Recommendation rule:** not yet, until a rule actually fires on a clock nobody wants to watch. Then: pure SQL → pg_cron; anything touching an external API → host cron.
