# taste — the direction, and the defaults it must not fall into

Read before the taste batch, together with `frontend-design` where that is installed — not at the canvas phase. The batch's options are the first place taste is exercised, and an option written before this file is read is written out of the defaults it exists to close. **Material, never an authority**: where this file collides with a user's answer or a ratified value, the user wins.

It never names the look this app should have. It narrows the space the look is chosen from, and it names the method for choosing — which is why it is loaded for every app without making every app look the same. A file that named the look would do the opposite.

## Commit to a direction before drawing

Three answers, settled before the first file is written:

- **Purpose** — what problem this app solves, and for whom.
- **Tone** — one extreme, named and held. A starting vocabulary: brutally minimal · maximalist chaos · retro-futuristic · organic · luxury · playful · editorial · brutalist · art deco · soft/pastel · industrial. It is a vocabulary, not a menu — a tone this app's own domain suggests beats one lifted from the list.
- **Differentiation** — what makes this app memorable rather than adequate.

Maximalism and refined minimalism both work. **What is judged is intentionality, not intensity** — and a direction that would describe any internal tool is not a direction.

These three ride the design plan `design-init` Step 3 narrates. The tone chosen is what the assumption lines and the judgement are read against afterwards.

## Colour

- **Accents: none, one, or two.** This counts **hues, not values** — each hue still gets its full ramp, and how deep that ramp runs is `design-init` Step 6's rule, not a taste decision. Expressed in `oklch`. Where there is more than one, **every accent shares the same chroma and lightness and varies only in hue** — that is what makes two accents read as one family instead of two separate decisions.
- **Whites and blacks are toned, never neutral by default.** Pick a temperature — warm, cool, or deliberately flat — and hold it across the whole ground. **Saturation above 0.02 on a white is a tint, not a white.**
- **Colour is derived, not invented.** Where a brand palette exists, everything else is derived from it in `oklch`. Where none exists, the accent is chosen first and the neutrals are pulled toward it. A hex picked from nothing is the one that will not sit with the rest.
- **A dominant colour with a sharp accent beats an even, timid palette.** A palette where every role carries equal weight has made no decision.

## Type

- **Never the default four**: `Inter`, `Roboto`, `Arial`, `Fraunces`. Choosing one of them is a failed choice, not a safe one.
- **A display face with character, paired with a body face that stays quiet.** A third family is allowed only for a real job — numerals, code, captions. Three is the ceiling.
- **Every family carries a fallback stack with close metrics**, and the loading is verified in the browser at the promotion pass rather than assumed.
- The type treatment is part of the design, not a neutral vehicle for the words.

## Composition and depth

- **Asymmetry, overlap, diagonal flow, elements that break the grid** are available and almost always unused. A page built entirely from centred, evenly spaced rows has defaulted rather than decided.
- **Generous negative space or controlled density — not the middle.** Density is a direction; halfway is the absence of one.
- **Atmosphere over flat fill**, where the tone calls for it: layered transparency, grain, noise, pattern, a gradient that is a mesh rather than a two-stop ramp, shadow used as depth rather than as a substitute for a border.
- **Execution complexity follows the vision.** A maximalist direction needs elaborate work; a minimal one needs precision in spacing and type. Elegance is executing the chosen vision well, never choosing the smaller vision.

## Spend the boldness in one place

One **signature** — the single element this app is remembered by — carries the risk, and everything around it stays quiet and disciplined. A design where three elements compete to be the signature has none. Cut every decoration that does not serve the direction.

## Defaults to avoid

These read as generated whatever the brief says:

- Aggressive gradient backgrounds.
- Emoji, unless the brand itself uses them.
- A rounded container with a coloured accent bar down its left edge.
- Icons drawn as emoji or dingbat glyphs — icons are inline SVG, stroke-based, on a 16/20/24 grid, one style throughout (`ui-build` holds the one-family rule).
- Numbered markers (01 / 02 / 03) where the content is not actually a sequence.
- The three clusters `frontend-design` names: a cream ground with a high-contrast serif and a terracotta accent · near-black with a single acid accent · broadsheet hairlines with zero radius. Each is legitimate for some brief, and none of them is a choice when it arrives regardless of subject.

## Do not converge

Vary tone, palette family, and type pairing **between apps**. Two internal tools by the same hand that look like the same tool have both lost their direction. Where an earlier app already took a direction, this one takes a different one, and the difference is named in the design plan.
