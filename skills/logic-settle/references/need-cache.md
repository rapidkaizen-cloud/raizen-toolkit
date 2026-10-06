# L1 — Server-state cache

**Candidates are measured on:** cross-screen invalidation, optimistic-update support, the discipline the cache imposes (a root provider, a cache-key convention every screen follows), and whether a library family rides along — a family is a consequence to name, in both directions.

**Recommendation rule:** handwritten (effect + state) below roughly three list screens — zero dependencies, at the price of every screen re-implementing loading, error, and cancellation, with manual invalidation; the researched de-facto standard at or above three. **Count only the list screens fetched on the client**: one the framework renders and caches on the server is the ladder's first rung (`logic-rubric.md`), and where every list screen is one, "none" is the recommendation. A realtime mention in the story adds one note, not one candidate: the chosen cache's invalidation is the natural place to hang a realtime subscription.
