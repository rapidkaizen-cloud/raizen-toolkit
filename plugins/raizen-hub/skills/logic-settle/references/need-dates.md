# L3 — Dates and timezones

**Candidates are measured on:** what they cover beyond `Intl` and Temporal, tree-shakeability and footprint, and how visibly the platform is in the process of absorbing them — a date library is a dependency the web is actively replacing, and that is a consequence to state.

**Recommendation rule:** platform first, always — `Intl` for formatting and day boundaries, Temporal where shipped (it still needs feature detection, and its polyfill is heavy). A library enters only when a concrete rule exceeds what the platform covers — name that rule when recommending. Whatever is chosen, the date helpers live in one extracted module (`logic-build` §7: the second occurrence extracts), so a later move to Temporal touches one file.
