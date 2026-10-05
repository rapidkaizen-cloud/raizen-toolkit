# L2 — Validation at the trust boundary

`logic-build` §4 already mandates the parsing itself — this question only decides the tool.

**Candidates are measured on:** first-class type inference, shipped bundle size, and runtime fit — a validator that is comfortable on Node may be heavyweight for Edge or for shipping to the client.

**Recommendation rule:** the runtime decides — Node → the ecosystem standard; Edge, or a validator that ships to the client where bytes count → the smallest shipped size that holds the admission rule. Prefer candidates implementing Standard Schema, so the choice does not lock the surrounding tools — say so in the consequence. Handwritten parsing fits one handler with one or two fields, and its consequence is that the checks drift from the types as fields accrete.
