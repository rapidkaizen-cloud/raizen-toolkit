# Ratification — Step 6

**Approving the canvas is the approval.** Read the values behind it, library-rendered ones included — palette and steps, type scale, spacing, radius, shadow, density numbers, and the picked frame's source — and report them as derived decisions, one cancellable line each; a cancelled line reopens that value as a question. No second gate over the same pixels.

- **Where no UI exists, write here**, in this order: the font, `DESIGN.md`, the decision records, the styling files, the scan. There is no second gate.
- **Where UI exists, write nothing here.** The values are the *new* column of `gate.md`'s diff — read that file next; the font install, `DESIGN.md` and the scan wait for the pass's Foundations, on its branch.

## Contrast — computed, never recalled

**Calculate every pair** — each foreground on each background it renders on, a library's calculated slots and chrome compositions included, a pair `DESIGN.md` forbids excepted — in every ratified theme mode, with the WCAG relative-luminance formula, where the foundations board renders, so numbers and chips share one source. **Choose each semantic family's dark shade by measuring it against its own light shade until it clears 4.5**, never by stepping along the ramp. Put a failing pair to the user, never silently passed or fixed (in Fast: `SKILL.md`, Fast or Full); a passing pair still prints its number.

## Where `Keep — today's look` was picked and no `DESIGN.md` exists

Open `.design-audit/audit.md` now: a Keep pick ends the blindness. **Ratify what its block measured and nothing else** — colours, text steps, spacing values, radii, the icon family with its sizes and weights, the fonts loaded. What the audit does not measure — shadow, motion, density, the behaviors under What the designer settles — is never invented on a Keep: its `DESIGN.md` line is `[needs verification]`. The stack and product calls are written as answered. The audit decides how each entry is put:

| What the audit measured | How the entry is put |
|---|---|
| **A coherent value** — a real scale, one family, a consistent radius | **Confirmation.** Show the measured value; first and recommended is an option naming the action plainly — `Keep this value — 8px` |
| **Nothing coherent** — scattered raw values, no scale, contradictory usage | **A real question**, with real options invented for this app |

Batch confirmations and questions through AskUserQuestion. **Write a ratified value exactly as measured**, never tidied. Unanswered → `[needs verification]`, out of the pass. **An answer differing from the measurement is a repair, never a redraw**: its line in the gate's `DESIGN.md` list shows both, every place that departs from it is a finding in the gate's list (`gate.md`), and the pass retokens them.

- **The five rules below bind only an answered value.** A value confirmed as measured is written as it stands, no ramp or alias layer manufactured over it; scattered colours answered onto a ramp get that ramp and its aliases in the pass's Foundations.
- **An answered width or theme mode the running app does not hold collides with the Keep pick**: put both in one question (`interview.md`, reconcile) — record what the app holds today, or keep the answer and take the gap as findings.
- **The product draft's proposals end here.** Nothing draws them, so none is ratified: name them once in the Step 9 block, and withdraw an engine answer only a proposal fired — no decision record, its package removed in the pass.

## What is written

| Written in | Contents |
|---|---|
| `DESIGN.md` | **The tokens**, every value the design system fixes, and in prose **the rules and scale** — how many may exist, what is forbidden — written from what the user ratified, never from a stock phrasing (`design-md.md`) |
| `docs/decisions/` | One record per stack dialog answered — component library, styling, icon pack, each engine — its options with their consequences, the answer, the reason; a *keep* whose record already stands writes none. None in a legacy repo |
| Styling files (`tailwind.config`, CSS variables, the component library's theme file) | **A copy of the tokens** under the same names, written in the same edit, plus what tokens do not carry — font loading, element rules, motion |

- **The font is one install line approved in chat**, where the face needs a package — the only install outside Step 4. Refused → the face opens as a normal dialog, the same face loaded by link first; a different face is redrawn as a correction round (`canvas.md`, Judging).
- **Write `DESIGN.md` first, then scan** — to `design-md.md`, with any sidecar `impeccable`'s document reference puts beside it, read at write time; in a legacy repo, Section 5 and the `DESIGN.md` generated from it (`docs-format`, `references/legacy.md`). Then run the detector over the styling files and report the count; a hit on a just-ratified value is named and left standing.
- **Every line of `DESIGN.md` traces to an interview answer, a reported derived decision, or a ratified canvas value**; nothing else is written. **A written `DESIGN.md` is rebuilt from zero, never patched**: an old line survives only through *keep* or re-ratification, otherwise it is a removal in the gate's diff.
- **Only this skill writes it, and it is rewritten whenever a ratified value changes**; a hand edit, or an `impeccable` refresh from the built code, is a finding.

## Five rules bind the canvas variables, so the styling files are a copy

**They bind from the refactor after the pick** (`canvas.md`), so the approved canvas already holds them; ratification copies its values and never re-derives one.

1. **The palette is two layers, and the second one is the system.**
   - **A ramp per functional hue**, holding only the steps something reads, so hover, active, subtle fill, border and text-on-fill each land on **an existing step** — a state the library computes from its base (a colour-mix hover) stays the library's. **Derived, never typed**: from the picked accent and its pulled neutral, in OKLCH per `impeccable`. **Named on the stack's convention** (Tailwind's `50 … 950`), never a parallel scale.
   - **At least three shades per semantic family** — light, base, dark, and more where the canvas draws more; the dark chosen as Contrast rules.
   - **A semantic alias layer, and product code reads only that** — surfaces, text, borders, focus ring by role, each pointing at a step.
   - **The chart palette belongs to the token set**, chosen once; `dataviz`, where loaded, assigns series colours from it.
   - State the step count and the alias list in `DESIGN.md`'s Colors.
2. **Every semantic slot the component library exposes is mapped**, the neutral `default` included — list the slots first; library slots are exempt from the next rule.
3. **A token nothing reads is not written**, nor a layout constant components duplicate as a utility class.
4. **Two roles with the same value collapse into one** before a round is shown.
5. **One palette, two consumers.** A utility-CSS theme and a library theme are both written from `DESIGN.md`'s colour tokens in the same edit.

No UI → `pass.md`. UI exists → `gate.md`.
