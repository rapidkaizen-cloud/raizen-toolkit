# L4 — Error reporting destination

`logic-build` §5 already mandates that the log gets the detail — this question decides where the log goes.

**The options are destination categories, researched into named services at decision time:**

| Category | Fits when | Consequence shape |
|---|---|---|
| **Host's built-in logs** | Experiment stage, or failures are noticed by users faster than by dashboards | Nothing to install; logs expire with the host's retention and are hard to search |
| An error-triage service | Someone must be told when production breaks, with stack traces grouped | One more service and one more credential to manage — research which service currently owns this category |
| A structured log drain | The need is searchable history rather than alerting | Queryable logs; alerting still has to be built on top |

**Recommendation rule:** host logs until the app is operational and someone is on the hook for its failures; then the researched triage service. The reason in the decision record must name **who reads the errors** — a destination nobody reads is the host log with extra cost.
