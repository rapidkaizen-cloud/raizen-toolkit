# Anti-patterns — material for PRD Section 5

Distilled from `design-taste-frontend`. Used as **material copied once** into the Anti-patterns sub-section, not as a skill invoked every session.

Take only what is relevant to this kind of app. An anti-pattern that cannot occur in this app should not be written — a long list where half does not apply makes the whole thing stop being read.

Write them into the PRD as prohibition sentences, not as quotations. Section 5 holds this app's norms, not a record of where those norms came from.

**Carry the qualifier across with the prohibition.** Most entries below forbid something narrow, not a whole category: a purple-blue gradient *as the default*, a *pure black* shadow on a *light* ground. Drop the qualifier and the PRD ends up banning gradients and shadows outright — tools the app was never meant to lose, refused by every session from then on. A prohibition that reaches Section 5 without its qualifier is a finding.

## Applies to every kind of app

**A purple-blue gradient as the default.** The most recognizable reflex in model-generated UI. A neutral (cool gray, warm gray, or pure gray) plus one high-contrast accent is always a better starting point.

**Serif chosen because it "feels premium".** That is not a reason. Serif belongs only when the brand names it or the product is genuinely editorial.

**Emoji as icons.** Their size cannot be controlled, their color differs per operating system, and screen readers read them as prose.

**Hand-drawn icons, or two icon families mixed.** Their stroke weights will never match. An icon missing from the chosen family is a finding, not permission to draw one.

**A placeholder used as a label.** The label disappears the moment the user starts typing, exactly when it is most needed.

**The accent changing mid-app.** One accent is locked for the whole app. A save button that is blue on one page and green on another means the user has to re-read every screen.

**Mixed radii with no rule.** A pill button on a page of sharp corners. Tiering is fine, as long as the rule is written down and followed everywhere.

**Pure black shadow on a light ground.** Tint the shadow toward the background, or drop shadows entirely.

**A button whose text fails contrast against the button itself.** Including transparent buttons over photographs. Check every button before finishing.

**The theme flipping mid-page.** One light section between dark ones makes the user feel they walked into a different site.

**Fake-precise numbers.** `92%`, `4.1×`, `13.4 kg` that come from no data at all. Numbers come from data, or are clearly marked as examples.

**Cards inside cards inside cards.** Three levels of nested boxes means the grouping is wrong, not that a box is missing.

**Animation with no reason you can state in one sentence.** Valid reasons: hierarchy, narrative order, feedback, state change. "It looked cool" is not one.

**Color as the only status marker.** Already a rule under Section 5 Color; do not write it twice.

## Public sites only

For dashboards and internal tools these four do not apply — do not write them into that PRD.

**A small uppercase label above every section heading.** At most one per three sections. Most sections need no label at all.

**A fake product screenshot assembled from `<div>` elements.** Use a real screenshot, or skip it entirely.

**Two call-to-action buttons that mean the same thing** ("Contact us" and "Let's talk" on one page). One intent, one label, used everywhere.

**Text-and-image alternating more than twice in a row.** The third one has to be a different layout family.

## What was deliberately left out

`design-taste-frontend` also prescribes a stack (Next.js, RSC, Motion, GSAP) and advises against `lucide-react`. Neither is used: the stack is decided in `app-init`, and the icon pack is chosen by the user at decision 7 — where the recommendation is always the icon set bundled with the chosen component library, whichever it is, because one fewer dependency outweighs an opinion about stroke weight.
