# The gate — Step 6, where UI exists

The **single stop** authorizing the change. One message, then a hard stop answered in chat, never an AskUserQuestion. Open `.design-audit/audit.md` now — the drawing session's blindness ends here. Approved, the block is saved as `.design-audit/gate.md` (`pass.md`).

## A redesign — four parts

**1. `DESIGN.md` as a diff**, and each decision record the stack answers write. Only what changes, old beside new, removals included:

```
Accent color : blue #2563EB  →  green #059669
Text steps   : five          →  four (merge section title and body)
Radius       : 8px           →  0
Signature    : ledger seam, sole vertical rule  →  removed
```

An old line nothing re-created leaves as `→ removed`, never by omission. Where no `DESIGN.md` existed, the *old* column is the **measured** value, marked as such — `Radius : 8px (measured) → 0`.

**2. The file plan.** Each page line reads `replaced by its canvas file` or `retoken only — no canvas frame`, never a third label.

- **In a redesign `retoken only` is unavailable**: an undrawn component is `deleted` (anything still needing it is drawn), a thin passthrough whose child was redrawn is deleted, its callers reaching the redrawn child directly.
- An unaccounted file is an inventory failure. A page with a canvas file listed `retoken only` is its own question.
- **Shared canvas files get their own line under their header's production path**, checked against the components folder now; a path already taken is its own decision line.
- Every file that is not a page — chrome, shared components, styling files, linter config, `AGENTS.md`, a file changed only at the data seam — takes a line naming what changes; `UNTOUCHED` files are listed.
- Close with the **seam points** from `pass.md`'s order, never a time estimate.

```
PASS — [n] files
LeadTable.tsx    replaced by its canvas file
wizard.tsx       → src/components/import-wizard.tsx · shared by 7 pages · replaced by its canvas file
StatusChip.tsx   retoken only — no canvas frame · 4 status colors updated
index.css        11 tokens replaced · 3 deleted · fonts now load here
App.tsx          replaced by its canvas file (chrome)
UNTOUCHED        PhoneContact.tsx
```

**3. The detector's audit count** and how many hits the canvas removes; the rest listed by rule, returning at Step 8.

**4. What approval orders, contradicts, and removes.** Every line carries a recommendation and its trade-off.

- **Ratified elements lacking data**, one line each — element, page, the work ordered (column · RPC · migration · a query, where the data exists and nothing reads it), and that the element renders waiting until that work runs.
- **Deviations**: canvas elements the real flow contradicts and real controls the canvas never drew, one decision line each.
- **Removals, confirmed item by item** — every function or control leaving, plus every part in `audit.md`'s frame inventory that no canvas page carries; with a routes-only inventory, every route no canvas page carries, under `frame coverage unverified — the running app could not be walked`. *Approve everything* never covers this group; a reply naming its items — each ID, or a range such as X1–X12 — does. Removals a reply leaves unnamed are shown again alone, in a message holding nothing else, and a clear yes to that message covers them all.

End the turn and wait for the chat reply; lines may be approved or rejected by name. A rejected value opens its question first, as a cancelled value line does (`ratify.md`); a rejected file-plan, ordered-work or deviation line is asked in chat what stands instead. Rejected values and rejected removals return to Step 5, the other three only where the answer changes what is drawn, nothing written; after the redraw the gate is shown again whole, its changed lines marked, and a line approved before and unchanged stays approved. All approved → the pass. Nothing changed → close at Step 9.

## Fix the drift, or `Keep — today's look`

**Nothing is redrawn and nothing leaves on this gate**: it has no file plan beyond the findings' files and no removals — the frame inventory is read against canvas pages only in a redesign.

**Keep with no `DESIGN.md` opens with `DESIGN.md` as it will be written**, one line per ratified value (`ratify.md`) — `Radius : 8px (measured) → kept`, or `Radius : scattered (measured) → 8px` where the answer differs — then the findings list, one finding per place that departs from an answered value. A rejected value line reopens that value's question, never Step 5. Approval writes `DESIGN.md` as the pass's first act even where the list is empty, never closing at Step 9 with it unwritten; from here on that Keep is fix-the-drift against the `DESIGN.md` just approved, and every rule naming fix-the-drift binds it.

The same gate shows the findings list:

```
REPAIR — [n] findings
1  Usage.tsx:185-188   gradient text           impeccable · craft floor, Refuse
   3 sentences  →  removed
2  StatusChip.tsx:19   label 15 chars          S5 · Repeated label length
   "Belum dihubungi"  →  icon only, text to aria-label
```

STOP for approval per item; a rejected item stays a finding, reported at Step 9. Merging two `DESIGN.md` roles at one value is approved line by line here. The archetype table, where `DESIGN.md` lacks one, is filled from `audit.md` and ratified here at repair scale (`interview.md`).

Approved → `pass.md`.
