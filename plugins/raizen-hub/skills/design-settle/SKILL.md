---
name: design-settle
description: Settle the visual direction and component library of an app, whether it has UI already or none at all. One path for every repo — Step 0 reads two facts, whether UI components exist and whether PRD Section 5 is filled, and those two facts switch steps on or off rather than choosing a mode. Where UI exists the code is audited first and today's look is one of the candidates; where Section 5 is filled the user may choose to only fix the drift. Then one reference question, multi-select, whose ticks anchor the frames; the stack recommended in a single install block rather than asked; 2-4 full-fidelity direction frames drawn in every session with the real packages that the user picks from on screen — nothing about the look is asked after the pick, and every option is invented for this app. A temporary in-repo canvas renders the answers as every page of the app in production-grade code, judged in the real browser, approved at one gate, then relocated into the app — the only difference between canvas and production is the data. Use before the first UI component of a repo is written, and whenever the user wants to redesign, restyle, or overhaul the look of an app that already has one.
---

# design-settle — the visual direction, from nothing or from what exists

`app-settle` writes the PRD. `logic-settle` decides the layer under the UI. This decides how the app looks, and it is the only skill allowed to write **PRD Section 5**.

**One skill, one path, two facts.** There is no mode to pick and no second skill to route to. Step 0 reads two things — whether **UI components exist**, and whether **Section 5 is filled** — and every step below says what it does under each. A repo with neither runs the shortest form of the path; a repo with both runs all of it. Nothing else changes between them.

| UI components | Section 5 | What switches on |
|---|---|---|
| none | empty | The shortest path: reading → interview → frames → canvas → ratify → promote in place → verify. Nothing to audit, nothing to protect, nothing to branch from |
| present | empty | The audit, the function and frame inventories, `Keep — today's look` as one candidate, the gate before any real page moves, the pass on its own branch, parity checks. This is the `app-settle` document-mode case: a look nobody decided, only accumulated |
| present | filled | All of the above, plus the fix-or-redesign question before the interview and the Section 5 diff at the gate |
| none | filled | STOP — ask whether the user really means to redesign an app whose UI was removed, and treat the answer as the row above |

**Two words are used below for these switches, and only these two:** *UI exists* and *Section 5 filled*. A step with no such marker runs identically for every repo.

## Hard limits

**The confirmed reading is the precondition, not the PRD.** `PRD.md` missing, or present in a shape `prd-structure.md` does not describe — a template app, a repo documented by hand — does not stop this skill: Step 1 builds the reading from what the user said explicitly first, from the code where the user was silent, from the PRD where the code is too, and asks only for what none of the three settled — and **nothing is asked about the look and nothing is drawn until the user has confirmed that reading**. That confirmation is the hard gate. What this skill writes stays Section 5 alone (Step 6 says where it lands when no PRD exists), and the close names the PRD sections `app-settle` still owes — `build-flow` opens pages from Sections 2–3 and will stop until they are written.

**Section 5 is never written from existing code.** That direction — `CSS → PRD` instead of `user → PRD → CSS` — turns every accident in the stylesheet into an official norm nobody decided on. The audit produces **findings**; a finding becomes a Section 5 line only once the user ratifies it. Section 5 changes only by **explicit user decision**, line by line.

**Section 5 is written once, and never before its stop.** Where no UI exists, it is written at Step 6 once the canvas is ratified. Where UI exists, it is written exactly once, only after the Step 6 gate approves it — as the first act of the pass, on the pass's own branch. Until then nothing touches it, and no draft document stands in for it: the canvas is the draft, its variables and foundations board carry every value the user can inspect. Approval writes Section 5 in full; rejection leaves the PRD exactly as it was.

Four places may be written, and no fifth: **PRD Section 5**; the **Component library row of `CLAUDE.md`** when the library line is settled as something other than *keep*; and the **generated `DESIGN.md`** of Step 6 — frontmatter tokens derived from ratified Section 5 for `impeccable`'s detector, never a decision of its own, never hand-edited; and the **`## UI` part of `AGENTS.md`** at Step 6 — the pointer an agent without the plugin reads, holding paths and a command, never a value. Do not create `MASTER.md`, `design-system/`, a staging PRD, or an audit report as a file, and never a `DESIGN.md` written from code. If another skill in this session produces a document, it is not committed and not referenced.

**The canvas is the final front-end, staged** (`references/canvas.md`). Its files are the future pages, written production-grade — the user approves code, not pictures, and promotion relocates that code instead of imitating it. The one legitimate difference between a canvas file and its live page is the data flowing through it; everything else is a failure to fix or a deviation the user has named.

**Two phases, two safety rules.** The canvas phase only adds files under `src/design-canvas/` — it runs safely beside any other session, and no other session touches that folder. Where UI exists the pass rewrites the app, so it runs **isolated on its own branch or worktree**, and parallel feature work continues undisturbed in the main tree. Where no UI exists there is nothing to isolate from, and the pass runs in place.

**Keeping everything is a valid ending, not a failure**, wherever there was something to keep. Answering *keep* to every question, picking `Keep — today's look`, or reverting after the canvas, closes this skill with the PRD unchanged and the code untouched. Say so plainly and report the audit findings; do not manufacture a change to justify the session.

**A code-minimizing session mode governs the how, never the what.** A user rule or mode that asks for the shortest working code — YAGNI, fewest lines, no speculative abstraction, reuse before new, no dependency outside the block — is welcome inside every file this skill writes: a canvas page, a shared component, a theme file is written as lean as it can be and still hold. What such a mode never removes is what this skill names, because installing the skill is the user's explicit request for it: the full product draft with its proposals tagged, every state drawn, the fixtures file that closes, the two-layer palette and the component-token table, the `/styleguide` route, the compare page, the signature, and an engine or library the user approved in the install block used where it covers the job. Those are not scaffolding for later; they are the deliverable, and a page that arrives without them is thin, not lean. The mode's own exemption for what was explicitly requested is what makes the two compatible, and this paragraph is where that request is written down.

Do not commit and do not push. Staging is fine; the commit waits for the user, and where the pass ran on its own branch its commit is **proposed at the close, on that branch**. Never push, never merge, never open a PR.

Not decided by the user → `[needs verification]`.

## Step 0 — Preconditions

```
Skill build     : [raizen-hub x.y.z — read from this plugin's own .claude-plugin/plugin.json]
PRD.md          : [present / missing / present, outside prd-structure's shape]
Section 5       : [filled / empty / absent / product without UI]
UI components   : [file count — 0 on a repo with no UI]
Kind of app     : [from Section 1, else read from the code, else asked at Step 1 — a label, never a branch]
Register        : [first visit / tenth use / both, per page group — from Section 2, else from the routes]
Platform        : [from Section 1 Surface, else from the manifest and platform files — web, or the
                   platform found; a non-web value routes every browser-named check below to that
                   Surface's Proof profile line, or to the platform's own tooling where none is written]
Primary role    : [from Section 2, else from the roles the code enforces, else asked at Step 1]
Design material : [impeccable present/absent · frontend-design present/absent — both Required]
Branch          : [name · clean or has uncommitted changes]
Leftover        : [none / canvas alive / pass applied — from src/design-canvas/ and git state]
Switches        : [UI exists: yes/no · Section 5 filled: yes/no]
Reading         : [one sentence — see Step 1]
Flow            : load impeccable + frontend-design → reading (+ audit where UI exists)
                  → fix or redesign (where Section 5 filled) → reference slot, alone
                  → stack recommended (library · icons · engines) → install
                  → direction frames, one per tick, always 2–4, today's look among them
                  where UI exists → pick → refine (only if the pick carries a change)
                  → design plan → canvas rounds → ratify (+ gate where UI exists)
                  → pass (in place, or on its own branch where UI exists) → verify → close
```

**The block is printed on every invocation** before any work beyond the reads that fill it. A session that starts editing, or even auditing, without having shown this block has routed itself in the dark, and everything it concludes about where the flow stands is a private guess the user never saw.

The `Design material` line exists for the same reason the `Skill build` line does: both skills are Required installs, they carry the craft rules this skill and `ui-build` no longer state, and a session missing one writes its options out of the very defaults that material exists to close. **An absence is asked, not merely printed** — Step 1 holds the rule and the question's contents, and this row is the step that fires it. The session still does not block: continuing without the material is one of the two answers, and a redesign that refuses to start until an npm install lands costs more than the gap does. What changed is who spends the material — the user, in a dialog naming what is lost, instead of a row nobody read.

The `Skill build` line exists so a stale install is visible before the pass, not after: rules fixed in the toolkit reach an app repo only through `/plugin update`, and a session on an old build re-makes exactly the mistakes the fix closed. The user sees the version and decides; the skill does not block on it.

**Re-entry is a gate, never an inference.** A leftover from a previous session — `src/design-canvas/` still present, or a pass already applied on a branch or in the working tree — means this invocation *may* be a continuation, and prior-session summaries or repo state make that likely, not decided. When the `Leftover` line is not `none`, one mandatory AskUserQuestion follows the block, before any other work:

- **Continue** — resume the unfinished flow at the step the state shows: a pass applied but unverified resumes at Step 8; a canvas ratified but not promoted resumes at Step 7; a canvas mid-rounds resumes at Step 5; frames drawn but not picked resumes at the pick. Announce the resumed step and what remains before touching anything.
- **Start over** — the full path from Step 1, exactly as a first run. The leftover canvas is an audit finding; its deletion is proposed at the same chat-stop confirmation Step 8 uses, never assumed.
- **Stop** — report the detected state in one block and close.

A session that skips this dialog and routes itself — because the state "obviously" says where the flow stands — re-makes exactly the mistake this gate exists to close: the user watches edits land without ever having chosen the path.

`PRD.md` missing, or outside `prd-structure.md`'s shape → **not a stop**: say so in the block, read around it as Step 1 describes, and name at the close what `app-settle` still owes. Product without UI → **STOP**, this skill does not apply. Branch `main` → **STOP**; the git guard will refuse it, and that refusal is correct. **Working tree not clean, where UI exists → say it and carry on.** Name the dirty paths in one line. The pass branches from a committed base, so what a dirty tree costs is the base itself: uncommitted work is invisible to the pass's branch, and the promoted app will not carry it until the user commits and the branches meet. Advice, not a gate: the user decides.

## Step 1 — The reading, and the audit where UI exists

**Load the two materials first, before the reading sentence is written**: the Required installs `impeccable` and `frontend-design`. `canvas.md` names which of `impeccable`'s reference files carry the material and draws the boundary. **One absent is asked, never merely reported**: through AskUserQuestion at the step that prints the `Design material` row, naming in the question itself what is lost — `impeccable`'s ban list, its display-face and convergence calibrations, the Operate register, and every detector count from this point on; `frontend-design`'s direction method and its restraint — and offering continuing without it against stopping so it can be installed (`npx impeccable install`). Continuing is a real answer, and the recommended one wherever installing is not available in this session; what is refused is the session spending the material silently on the user's behalf. The answer rides the ratification report as its own line, so a direction settled on half the material says so where anyone reading Section 5 later can see it. Step 0 has already routed, so nothing is read for a session that stops.

They come first because **the reading sentence is itself the first taste output** — its *leaning* clause is a judgement about how this app should feel, and every option and every frame is invented from the corrected reading. A leaning written before the material is read seeds everything that follows out of the same defaults the material exists to close, and the session then offers the user a menu of them: a reference slot proposing whichever product came to mind first, a frame set in Inter, a frame on a cream ground with a serif and a terracotta accent. **A choice never offered is not recovered by any later round** — the judgement can reject what was drawn, but it cannot reach an option that was never written. Where UI exists the pull toward the defaults is stronger, not weaker: the audit below fills the session with the app's current values, and every one of them is a default asking to be offered back.

Both are divergence guidance: they name the defaults that read as generated and the method for choosing a direction, never the direction itself; `canvas.md` holds the rule and where the line falls. No skill that prescribes a fixed look — a fixed palette, a fixed pairing, a card recipe — is read. They stay in hand for the rest of the flow: the design plan at Step 5, the canvas, the judgement.

**Where the reading comes from — the user first, the code second, the PRD third.** What the user said explicitly — in the request that opened the session, or at the correction below — is the source, and nothing outranks it. Where the user was silent, the code: what exists is read from it and never from the PRD, as `prd-format` already fixes — the router for the pages, the manifest and platform files for the platform, the auth and guard code for the roles it enforces, the rendered strings for the locale, the dependency file for the stack. Where the code is silent too, PRD Sections 1–2 where they exist in a readable shape — what the app is for, who comes back to it and how often, the register. Where all three are silent, the gap is named inside the reading and settled at its correction, in the same dialog, never as a question of its own. **A conflict is a finding named in the reading, never a silent pick**: an explicit user statement that contradicts the code is followed and the contradiction reported; between code and PRD, about what exists the code is right and the PRD line is reported, about what ought to be the PRD is right and the code is reported. On a template app the router and the manifest are the whole reading, and the correction is where the domain enters — that is the case this order exists for.

**Reading** is your own conclusion before asking anything, one sentence, shaped as: *"I read this as [kind of app] on [platform] for [who uses it], leaning [the feel that fits], because [reason from the PRD]."*

**The platform slot is not decoration.** Where PRD Section 1 holds the platform it is never asked again; where it does not, the platform is read from the code — the manifest, the platform files — and confirmed inside the reading, still never as a question of its own. It rides in this sentence because the corrected reading is what every option and every frame is invented from, so one word here is what puts the platform into all of them at once. Left out, the options and the frames arrive in the web's vocabulary and no later decision can tell that anything was lost.

Concluding first beats asking from nothing: the user only corrects what missed, and the correction carries more than an empty question would. A wrong reading is not a failure — it draws out detail that no question would surface.

State the reading, ask for correction, then continue — **and nothing after this line runs before the correction is answered**: no reference question, no stack line, no frame. On a repo whose PRD could not supply the reading, this dialog is the only place the app's purpose and its users are ever stated, and every option below is invented from it. When the correction is asked through AskUserQuestion, **the full reading sentence goes inside the question field itself** — the dialog may render without the prose around it, so a question that points at text "above" can arrive pointing at nothing.

The reference options, the frames, and the canvas's values come from the model's own design knowledge of this app and its platform, sharpened by the two materials above, and the user's judgement on screen is what checks the result.

### The audit — where UI exists

Read what the code actually uses, not what the PRD says, **before the reading is put for correction** — the reading of an existing app is written against what the audit found. Report one block:

```
AUDIT
Tokens defined      : [how many colors · text steps · spacing values · radii]
Token health        : [how many never read · duplicate roles · library slots unmapped]
Stray raw values    : [how many hex · font sizes · spacings, across how many files]
Slop detectors      : [how many hits · how many rules, from `npx impeccable detect` on the
                       source tree — the source tier only; the full set needs the running app.
                       `n/a — native surface` where Section 1's Surface is not web technology]
Icons               : [families, named · how many sizes · how many weights]
Fonts loaded        : [from the styling files AND the HTML entry — a family named in CSS
                       but never loaded renders as its fallback, and only this row sees it]
UI stack            : [component library · icon pack · engines — chart, table, date,
                       drag-and-drop — with versions, from the dependency file]
Repeated labels     : [longest · median · how many repeat per screen]
Supporting text     : [how many paragraphs · the longest in sentences]
Frame inventory     : [routes counted from the router · parts and states named per route,
                       or `routes only — the running app could not be walked`]
Deviates from S5    : [list, per rule broken — Section 5 filled only]
Components affected : [file count that will be touched if tokens change]
```

That last number matters most — it decides the size of the final pass, and the user is entitled to see it before deciding anything.

**The `UI stack` row is the canvas's import whitelist** (`canvas.md`, declared stack). A job the brief needs that no installed engine covers becomes an install question at Step 4; an engine installed but unused is a finding.

**The walk may also expose the logic layer bleeding** — handwritten data-fetching in UI files, hand-parsed dates, unvalidated inputs. That is not this skill's work: make the `logic-settle` offer under that skill's own rule — evidence, cost, and recommendation in one AskUserQuestion — and carry on with the audit either way.

**While walking the pages, screenshot one page per archetype at desktop width** — captured per PRD Section 1's Proof profile: the browser for web, the profile's Visual line elsewhere. Step 8 compares the finished pass against these; without a before, "it looks redesigned" is an assertion nobody can check. The screenshots are for that comparison and the judgement's before/after — they are not looked at while the canvas is drawn.

**The same walk writes the function inventory** — every function the app carries, one line each, page-agnostic: what can be done, not where it sits or how it looks. In a redesign this list is the canvas's brief-floor (`canvas.md`), and collecting it here is what lets the drawing phase keep the old pages closed: the audit is the last time they are opened before the pass.

**The same walk writes the frame inventory** — per route, the parts and states that render there, names only: the table, the filter row, the add dialog, the detail panel. **Routes come from the router file itself, never from memory**, so no page can be absent from the list; the walk then says what each one holds. In a redesign this list is what the canvas must cover — a part missing from it is a part the canvas will not draw and promotion will silently delete, and that loss is invisible to Step 8, whose diff compares the canvas against its own promoted page rather than against the page it replaced. **States real data cannot produce are listed anyway** — loading, empty, failed, and every role branch — because `ui-build` requires them of every component whether or not the walk could reach them. Names only, never pixels: the screenshots stay closed while the canvas is drawn, and this list is the one thing that crosses into it.

**The app could not be run, or there are no credentials → say so, here and at Step 6.** The inventory is then routes only, and the gate carries one line — `frame coverage unverified — the running app could not be walked`. A layer skipped in silence reads as a layer that passed.

The **UI stack** row exists because the library line builds its recommendation from measured numbers; **Repeated labels** and **Supporting text** are measured so the canvas's copy decisions are judged against real counts rather than guesses (`interview.md`, the designer-settles list). Measuring them here means the interview never stops to go looking.

**The `Slop detectors` row is deterministic and is the only row here that is** — and it runs only where the Surface is web technology, per `canvas.md`'s rule; a native Surface reports `n/a — native surface` here and at every later detector step. Run `impeccable`'s detector over the source tree and report both numbers. It is a **source-tier** scan: the rules that need a rendered page — measure, touch target, occlusion, nested containers — do not fire here, and Step 8 runs the full set against the running app. Its hits are **findings**, never repairs made on the way past: a finding becomes a Section 5 line only once the user ratifies it, like every other line in this block. `impeccable` absent → report the row as `n/a — not installed` and say so in the same breath.

**Token health** needs the library's own slot list, read from the installed package rather than remembered. Three numbers: tokens defined but never read, roles sharing one value, and semantic slots the theme file left unmapped. An unmapped slot means the app has been carrying a palette nobody chose, and it surfaces nowhere else in this block.

**An app on a stock Section 5 is the exception**, and Section 5 is read before this row is computed. A legacy repo whose Section 5 adopts the library defaults unmodified (a mode since retired — `prd-structure.md` holds the shape) has no theme file on purpose: report the row as `n/a — stock` and count no unmapped slots. Every slot there is unmapped by design, and reporting them as findings would push the user to write the very theme file that Section 5 refuses.

**Where Section 5 is filled, three more things hold.** A deviation from Section 5 is a **finding**, not a reason to change Section 5 — some of it may need fixing without any redesign at all, and Step 2 offers exactly that. Section 5 is audited too, not only the code: two roles named separately at the same value are one decision written twice, a finding against the PRD rather than the code, and merging them is repair work. And **a Section 5 without an archetype table is itself a finding** — apps older than the archetype rule have one shell decision and nothing about what pages hold. Derive the table from the routes that exist (grouped as `interview.md`'s archetype rule describes, usually 4–7 archetypes), and present it for ratification the way Step 6 presents measured values: ratify or correct, never adopt silently. A ratified table enters Section 5 at repair scale — it records what the pages already are, no visual direction changes — and every page falling far short of its archetype goes to `build-flow` Section 4 through the hand-over below, one `QUEUE.md` line each. Where the app has no `/styleguide` route, offer generating one as Step 6 specifies; the user decides.

**A page holding too little is not a finding, and not this skill's work.** The audit walks every page, so pages that answer very little are seen here — a screen on correct tokens, correct icons, correct spacing, and still mostly empty. That code breaks no rule. It renders faithfully a content decision nobody ever made, and no styling pass can invent one: what a screen should hold is a product decision belonging to the user. Do not report it as a deviation, and do not fill it. Hand it to `build-flow` Section 4, which derives candidate content from PRD Sections 2 and 3 and puts it to the user as a proposal — bound items as a statement, optional ones pre-selected to be cut. Name which pages were handed over, and carry on. **What is out of scope is the content, not the layout.** In a redesign the page is not exempt from the pass: its shell and arrangement are rebuilt to its archetype like every other page, using only the content it already has. What stays with `build-flow` is deciding what *else* the page should hold.

## Step 2 — Fix, or redesign — where Section 5 is filled

Section 5 empty → this step is not asked; there is nothing to repair against. Continue at Step 3.

One question, two options, with a recommendation:

| Choice | What changes | Questions asked | Components touched |
|---|---|---|---|
| **Fix the drift** | Zero new norms — only bringing code back in line with the existing Section 5 | None | Only the deviating ones |
| **Redesign** | **Section 5 is rebuilt from zero** — every line re-decided, archetype shells and visual-direction prose included; today's values survive only as *keep* answers. The app looks redesigned afterwards, not retuned | The reference question with `Keep — today's look` among its options, the library recommended *keep* in the install block, then 2–4 direction frames picked on screen and the canvas from the pick (`canvas.md`); every value it reads names the value it replaces | Every page, replaced by its canvas file |

There is no third option that narrows the scope, because **every decision carries a *keep* option** — today's look is a candidate at the pick, the library line recommends keeping, and every value line the redesign derives is cancellable back to today's value. Answering *keep* to the parts you do not want touched is what narrowing looks like here — scope is narrowed by answers, not by a mode chosen before the user has seen a single picture.

**Recommendation:** fix the drift, when the audit shows Section 5 is actually still right and the code is what strayed. Reworking a norm that was never followed solves nothing — it just produces a second norm that is also not followed.

**Consequence:** quote the affected-component count from the audit, and state that a redesign includes the component-library line. Answering that one with anything but *keep* rewrites every component whatever the tokens say, and revokes the stack lock recorded in `CLAUDE.md`. **State also what a redesign promises: the app looks different afterwards.** Name the pages the audit handed to `build-flow` — their shells will be rebuilt like every other page, but how much they *read* differently is capped until their content proposal lands, and the user hears that before choosing, not after the pass.

Fix the drift → jump to Step 6; the gate there shows the findings instead of a canvas. Section 5 is not touched, with one exception: two roles the audit found at the same value may be merged, because that removes a duplicate rather than adding a norm. The merge is still an explicit user decision, approved line by line like any other Section 5 change.

## Step 3 — The interview: the reference slot, then the stack

Read `references/interview.md` and run it in its order: **the reference slot alone, in its own turn, multi-select; then the stack, recommended in the install block (Step 4); then the direction frames — one per tick, drawn in every session — that the user picks from on screen (Step 5). Nothing about the look is asked after the pick.** Every option is invented for this app from the model's own design knowledge — no fixed list anywhere, and no research pass for taste — named in plain words with its consequence in parentheses, one real option marked "(Recommended)".

**The one question is the reference** — the app or site this one should feel like — multi-select, and its options are **real products named by you**, up to three that are arguable for this app, plus `Decide for me`. The recommended answer is a pair, both marked: the one recommended product and `Decide for me`. Every tick is a frame: a ticked product is drawn as one direction, `Decide for me` fills the rest of the set with the designer's own anchors, each named on its frame, and a lone tick is read twice so the set is never one frame. Nothing stands the frames down — not a product, not a brand palette, not Keep. A product the options missed, a screenshot, or a URL arrives through Other, and that is the best outcome rather than a deviation. `interview.md` holds the slot's own rules — how the ticks add up, what an anchor costs at the judgement, and the line between setting a direction and reproducing an interface.

**Where UI exists, `Keep — today's look` is the first option.** It is an option, never the recommendation, and its consequence is in its own text: ticked, the app as it runs today stands among the frames as one candidate — at its real routes, not redrawn — so what the user is keeping is judged beside what they could have, on screen. Where Section 5 is filled the label also names the reference Section 5 records. **A reference is drawn out here, not waited for**: an app being redesigned always has a reference in the user's head, and the audit's reading of what this app was reaching for is what the proposed products are argued from. Every product ticked becomes one frame's anchor, and the picked frame's anchor is the list the canvas is measured against at the judgement — drawing it out here is what cuts rounds later.

The picked frame is the user's preference and the canvas's baseline; everything the frame did not settle belongs wholly to the canvas's taste license. The canvas may depart from what was picked with a drawn, tagged, reasoned departure the user settles at the judgement (`canvas.md`), and the archetype table, the `/styleguide` route (Step 6), and real running pages are produced whatever was picked — what the pick changes is only where a value starts.

**Every question goes through the AskUserQuestion tool, never prose text** — the recommendation first and marked "(Recommended)" (on the reference slot, the pair `interview.md` names), the consequence in each option's description, everything the user needs inside the dialog itself. This holds in auto mode too: a prose question simply ends the turn unanswered.

**Nothing the user did not choose is silent.** Every value the canvas decides beyond the picked frame, and every derived value, surfaces as one line each with its basis — in the design plan and the canvas assumptions block before drawing, or the ratification report after approval — and the user may cancel any line; cancelling opens that value as a normal dialog. Where UI exists every such line names the value the app holds today, and cancelling it opens a dialog with `Keep — <today's value>` first. `interview.md` holds the list of what is derived and the floors that bind it.

**A canvas that misses twice escalates by re-opening this step:** `impeccable` and `frontend-design` are re-read first (`canvas.md`), then the reference slot is asked again with products chosen against what was rejected, **a fresh set of direction frames** is drawn to the new ticks, and the canvas is regenerated fresh from the new pick, never patched. The stack is not re-opened — it is installed, and nothing the two rejections said was about a package.

### The stack, recommended

Read `references/library-rubric.md` and `references/engine-rubric.md`. The stack is settled before the frames, because the frames are drawn with the real packages — and it is **recommended, not asked**: the install block of Step 4 carries one line per decision with its recommendation, its reason, and its alternatives, and the block's approval is the answer. The **component library** line names the recommended library with what it bundles and leaves out, and *own components* is always among its alternatives; the **icon pack** line exists only when that library bundles none; the **engine dialogs** whose triggers in `engine-rubric.md` have fired still run as dialogs here, before the block — nothing speculative; an app that trips no trigger hears no engine dialog. Candidates are **verified live** per the rubrics' duty — the one place research survives in this interview — because they install code. The family rule in `interview.md` shifts recommendations toward already-installed ecosystems. **Where UI exists the library line recommends *keep*** unless the audit indicts the library itself, and an installed engine the audit indicts is priced like the library line — *keep* first, and keep stays the recommendation unless the indictment stands.

**Draft the full product before the install block is shown** — `canvas.md`'s expansion duty, run here rather than at drawing time, because the draft is what trips draft-implied engine triggers: it existing now is what lets every engine ride this batch and the install block close complete the first time.

Replies outside the lines are always accepted. The user names something not on a line → verify it the same way, use it, state its consequence if you know it, or say you don't.

## Step 4 — Install, before anything is drawn

**The install block is its own chat gate, right after Step 3** — its contents are the stack recommendations and the engine answers, and everything is installed before a frame is drawn (`canvas.md`): the frames are the canvas's first round, and a frame drawn without its packages promises a component fidelity it cannot show. **The block is also where the stack is decided** — each line carries its recommendation, its reason in a clause, and its alternatives; approving the block settles them, and a reply naming an alternative rewrites that line and shows the block again. Do not ask twice, and **never put this block inside an AskUserQuestion** — a dialog covers the very block the user must read. Present the block, end the turn, and wait for the reply in chat.

One block, one approval:

```
Will install:
  npm install
  <component library>          [recommended under library-rubric.md — its reason and its
                                alternatives on the line, own components always one;
                                keep first where UI exists]
  <what the library omits>     [researched per candidate under library-rubric.md]
  <icon pack>                  [bundled by the library, or its own line when it bundles none]
  <engines>                    [chart · table · date · drag-and-drop — only what an
                                engine-rubric.md trigger decided, nothing speculative]
```

Wait for approval. Refused → hand over the commands for the user to run, then wait. Nothing to install — every line answered *keep* — → say so in one line and continue; a complete stack never stops the flow.

  <linter>                     [only where the repo carries none — Step 6's lint floor is
                                written into it, and a floor with nothing to run on is prose]
Install nothing outside that block. Something extra turns out to be needed → ask again, do not slip it in. The font is the one planned exception: the frames choose it after this block, and Step 6 installs it on its own approved line. **Where UI exists, the block also says what leaves**: an old library or engine whose decision changed is removed inside the pass (Step 7), never here.

## Step 5 — The canvas: rounds until final

Drawn and judged under `canvas.md` entire. **It opens with the direction frames** — 2–4 full-fidelity screens of the proving page — the page the designer names as the one the direction must survive, `canvas.md` — one per reference tick, drawn with the installed stack in `src/design-canvas/`, picked on screen, refined once where the pick carries a change (`canvas.md`, Directions first); then the design plan below, narrated in the turn after the pick; then the assumptions block and files written production-grade — every state drawn, fixtures in one contract-shaped file that closes arithmetically, imports only from the declared stack — the three-scan self-check before every round (imports · the render · the arithmetic), the signature drawn, tagged, and settled in a question of its own, tagged departures and proposals, the judgement through AskUserQuestion, two rounds then escalation.

**Where UI exists, today's look is one of the candidates and the canvas is drawn blind to it.** The `Keep — today's look` candidate is the running app at its real routes — captured at both widths and rendered in the compare page like any other frame, never redrawn as a canvas file — so the user judges what they have beside what they could have. Every other frame, and the canvas that follows the pick, is drawn under `canvas.md`'s blindness rule: today's design is not an input, Section 5's own prose included; the function inventory and the frame inventory are the brief's floor, and the audit's screenshots stay closed until the judgement's before/after. **Picking `Keep — today's look`** ends the drawing: nothing is redrawn, the unchosen frames are deleted, and the flow continues at Step 6 — as fix-the-drift where Section 5 is filled, as the ratification of measured values where it is empty. **A Keep pick carrying a change** (*keep it, but with the brand green*) is not Keep: it is a direction anchored to today's look, and the refine round draws it as a canvas file — the proving page redrawn to today's values with the change applied — after which the flow is a redesign like any other.

### Then state the design plan — narrated, not gated

Both materials were loaded at Step 1 and are already in hand. **Write the plan out in the turn after the pick, before the first full canvas file.** This is the step that separates a designed app from a competent average, and it is skipped by exactly the sessions that most needed it.

Five parts, short:

| Part | What is stated |
|---|---|
| Direction | Purpose · the one tone held · what makes this app memorable rather than adequate (`frontend-design`) · on a first-visit page group, the copy voice that tone speaks in (`ui-build`, Writing) |
| Colour | The named values with their roles — as many as the direction needs, no count fixed here — and where they came from — a brand palette, a reference, or an accent chosen first and the neutrals pulled toward it |
| Type | The pairing and each face's job. A face on `impeccable`'s calibration list is named with the reason it was still chosen |
| Layout | The shell and the composition in one or two sentences — where the density sits, what breaks the grid |
| Signature | The single element this app is remembered by (`canvas.md`, the taste licence) |

**The frames have already run by the time this step is reached, so the full plan is always written here** — to the candidate the user picked, and to the anchor its motivation line names. Nothing announces the plan earlier: the frames carry their own axes, one line of motivation and trade-off each, and that is all a user needs before voting. A plan that named a palette before the candidates were drawn would have decided the vote it was about to hold, which is the rigged set `canvas.md` forbids. Where UI exists, the recommended frame names what it departs from, and each of the plan's values names today's value beside it.

**Then critique it against the brief before drawing, in the same turn.** Work through what a session with a similar brief would produce; any part of the plan that arrives at the same place is a default rather than a decision. **Revise that part and say what changed and why** — one line. A plan reported without that pass has skipped the only step in it that does any work.

**It is a narration, not a gate: state it and keep going in the same turn.** Do not end the turn, do not open an AskUserQuestion, do not wait. What it buys is a decision the user can object to before the canvas exists, and a direction this session cannot quietly drift off later — the judgement still settles every value on screen.

The PRD is not touched during rounds. The foundations board is the living draft of every value.

## Step 6 — Ratification: Section 5, the styling files, `/styleguide` — and the gate where UI exists

**The font is installed here, not at Step 4.** The face was chosen on the picked frame and loaded by link until now; where it needs a package, that is one install line approved in chat before the styling files are written — the only install outside Step 4's block, and it is named as such.

**`DESIGN.md` is generated first, then the styling files are scanned.** The detector's design-system rules read their system from a token-bearing `DESIGN.md` frontmatter at the project root and from nothing else — without it they are silent, verified. So before the scan, write `DESIGN.md` from the ratified values — colours, typography, radius, spacing, and the component tokens Section 5 holds — **to the frontmatter schema `impeccable`'s own document reference describes at the time, read at write time, never recalled**, with a one-line body: `Generated from PRD Section 5 by design-settle — do not edit; Section 5 is the source.` This step alone regenerates it, whenever Section 5 changes; a hand edit, or an `impeccable` command offering to refresh it from the built world, is a finding. Then run the detector over the styling files and the styleguide route before this step is reported done, and report the count. A hit against a value the user just ratified is a finding, not a correction: name it and leave it standing.

**Approving the canvas is the approval.** The values behind the approved canvas are read and reported as derived decisions are reported — one line each, cancellable — then written (`canvas.md`, Ratification). **Where no UI exists there is no second gate**: no old Section 5 exists, so there is no diff to protect and no separate stop; Section 5 and the styling files are written here. **Where UI exists the report is not enough** — the values enter the gate below as the *new* column, and that line-by-line approval is the one gate; Section 5 is written only after it, as the first act of the pass.

**Where `Keep — today's look` was picked and Section 5 is empty, the values ratified are the measured ones.** Section 5 is empty, so the code has been making these decisions on its own. Walk every value `interview.md` names once — the reference, the library and engines, the values the frames would have decided (direction, palette, surface, density, typography, motion, shell), and the derived values its designer-settles list names. The audit decides **how** each entry is put to the user:

| What the audit measured | How the entry is put |
|---|---|
| **A coherent value** — a real scale, one family, a consistent radius | **Confirmation.** Show the measured value; first and recommended is an option naming the action plainly — `Keep this value — 8px` — never this file's vocabulary |
| **Nothing coherent** — scattered raw values, no scale, contradictory usage | **A real question**, with real options invented for this app |

The split is what keeps this honest in both directions. Re-interviewing everything produces answers that contradict the running app, and a PRD that does not describe its own app is worse than no PRD. Ratifying everything writes the stylesheet's accidents into the PRD as norms. Where the code has a real answer the user checks it; where the code has none, nobody may pretend otherwise — offering a "measured value" assembled from noise is inventing a norm and labelling it a finding. **Batch the confirmations and batch the questions**, every entry through AskUserQuestion. **A ratified value is written into Section 5 exactly as measured**, with no tidying on the way in — rounding a 14px step to 16px because the scale reads nicer is a change of direction disguised as transcription. An entry the user neither ratifies nor answers → `[needs verification]`; it stays out of the pass and `ui-build` keeps blocking on it. **Any entry answered differently from the measurement is a real change**: it gets the old-versus-new diff at the gate, and its pages return to Step 5 for the canvas to draw, like any other change of direction.

### What is written

The split is permanent:

| Written in | Contents |
|---|---|
| `PRD.md` Section 5 | **Rules and scale** — how many may exist, what is forbidden, written from what the user ratified — never from a stock phrasing |
| Styling files (`tailwind.config`, CSS variables, the component library's theme file) | **Values** — font name, icon pack name, hex, radius number, spacing number |

Color and spacing are the exception: their roles, values, and usage rules are written in Section 5, because contrast is a norm and not an implementation detail.

**The component-token table is the second exception, and it is written in Section 5.** A scale alone guarantees drift: two sessions given `radius: sm 4 · md 6 · lg 8 · xl 12` will pick differently for a card, and neither is wrong against the scale. So the table states the **per-component number**, one row each, for every component an archetype names: control height per size · input height · field padding · card padding and radius · row height and vertical padding for a table · header treatment · badge size and radius · modal radius · toast padding · focus ring. It lives in Section 5 rather than only in the theme file because `build-flow` Section 4 opens every later page from Section 5 and never reads the theme — a number the queue cannot see is a number the queue will re-decide.

**Where `PRD.md` does not exist, this step creates it** — holding Section 5 alone, under its own heading, with one header line above it naming Sections 1–4 as `[needs verification]` and `app-settle` as the skill that writes them; nothing else is invented for the file. **Where `PRD.md` exists in another shape**, Section 5 is written under its own heading at the end of the file and nothing else in it is touched — reshaping the rest is `prd-format`'s restructuring stop, and it belongs to `app-settle`. Follow the sub-section structure in `prd-structure.md` under `app-settle`. The Anti-patterns sub-section holds only prohibitions the user ratified — a canvas decision or an interview answer that forbids something — and may be empty; no stock ban list exists to copy from.

**Page Composition holds the ratified archetype table** — one row per archetype: shell layout, components, density profile, empty/loading wording, and the routes it owns. This table is what `build-flow` Section 4 opens every later page proposal from. Where a role split produced two density profiles, their numbers land under Breakpoints & Density.

**Every line in Section 5 traces back to one of three sources:** an interview answer, a derived decision already reported to the user, or a canvas value the user ratified. A rule belonging to none of them is not written, however sensible it looks — no question asks it, so nobody decided it. **Where Section 5 was filled, the new Section 5 is rebuilt from zero, not patched.** A line of the old Section 5 that none of the three re-created — a signature paragraph, an ornament rule, a reference-app list — does not carry over by default: it survives only through a *keep* answer or a canvas re-ratification, and otherwise it appears in the gate's diff as a removal. Silent carry-over is the mechanism by which a redesign stays caged by its predecessor, and one ratified sentence is enough bars.

### Five rules bind the styling files

**The palette is two layers, and the second one is the system.** A list of hexes is a palette; what makes it a design system is that product code never names one.

- **A ramp per functional hue, deep enough that nothing is improvised.** Hover, active, a subtle fill, a border, and text on that fill must each land on **a step that already exists** — a value invented mid-build is a value no board ever showed and no later page will find again. In practice that is around ten steps. **The ramp is derived, never typed**: from the value the picked frame carries — the accent, and the neutral pulled toward it — in OKLCH per `impeccable`'s colour derivation, so a later session can extend it by the same rule; ten hexes picked by hand are a ramp nobody can continue. **Where the stack carries a convention, follow it rather than inventing a parallel scale**: Tailwind's `50 … 950` is the one most component libraries already assume, and a second scale beside it means every future session picks between two answers.
- **Three shades per semantic family** — light, base, dark. The dark shade is not decoration: it is what makes text on the light fill clear 4.5, which is why Ratification chooses it by measuring it against its own light shade (`canvas.md`) rather than by stepping once along the ramp.
- **A semantic alias layer, and product code reads only that.** Surfaces, text, and borders are named by their role — the ground, the raised surface, the muted text, the focus ring — each pointing at a step. A component that names a numbered step has hard-coded a decision the alias layer exists to hold, and that is the line that has to move when the direction changes.
- **The chart palette belongs to the token set**, chosen once with the rest, not picked per chart. Where `dataviz` is loaded it decides series colour inside the plot; the token set is where those colours live.

State the step count and the alias list in Section 5's colour table, since colour is already Section 5's exception.

**Every semantic slot the component library exposes is mapped.** Libraries ship a full set of role colors, including a neutral one — usually named `default` — that every component falls back to when given no color. A slot left unmapped keeps the library's own value, so the app carries two neutral families: the one Section 5 chose, and the one nobody chose. List the library's slots before writing the theme file, then map all of them.

**A token nothing reads is not written.** A layout constant that the components duplicate as a utility class has two sources for one number, and the token is the one that will drift.

**Two roles with the same value collapse into one.** A palette naming both `danger` and `destructive` at the same hex has made one decision and written it twice. Merge before Section 5 is written.

**One palette, two consumers.** An app with both a utility-CSS theme and a component-library theme holds the same hex twice. The Section 5 color table is the source; both files are written in the same edit, never one alone.

### The `/styleguide` route

The route already exists — generated before the canvas was drawn (`canvas.md`) — and, importing production tokens, it follows the newly written values by itself; this step verifies it against the done-check below. Where UI exists and the route already rendered the old theme, it kept doing so until now and the canvas never looked at it; an older app with no route at all gets one inside the pass, from the new tokens, as Step 7 orders.

**One route file** (for example `src/pages/styleguide.tsx`), reachable at `/styleguide` in dev and kept out of the app's navigation and production build. It renders the whole visual language on one screen so the user corrects it here, while a correction is one token — not twenty screens later.

**It imports the production components and tokens.** Never hand-drawn copies, never a separate HTML file, never a second source of values. Deleting it later is deleting one file — offer that, never require it.

Sections, in order — each rendered from what the steps before actually decided, not from a fixed template:

| Section | Contents |
|---|---|
| Foundations | Color roles or scales as Section 5 defines them, with the semantic token list read from the styling files · every text step with a real sample sentence · spacing scale · the density profile table with its numbers, both profiles where a role split produced two · radius, shadow, breakpoints, motion · the contrast section, one row per pair with its computed ratio, in every ratified theme mode. **Rendered by `canvas.md`'s specimen rule, not as a table of names and values** — each token applied to itself with every other variable held constant, one caption treatment throughout printing the key and its resolved value together. This route outlives the canvas, so it is where that board's method has to survive |
| Components | Every component the app uses or an archetype names — variants, sizes, and states per component, including loading, empty, and failed where they apply, with a short real-usage snippet |
| Archetypes | The Section 5 archetype table, one card per archetype: shell sketch, components, routes |

**Done is measured against the table above, not against the page looking full.** Before reporting this route, check each row: every semantic token appears on the page; the component checklist is written first, not recalled — every component an archetype card names, each with its variants and states (inputs show default, focus, disabled, error; buttons show hover, focus, disabled, loading; mid-flow components — a stepper, a dialog, a dropzone — render in a static frame); every archetype card carries all three parts. When reporting the route, include the mapping **archetype → components it names → where each renders on this page**. The one legitimate absence is a component no archetype and no flow uses — stated, with that reason.

### The gate — where UI exists

Everything so far has been drawing and answers. This is the **single stop** where the user authorizes the change — Section 5, the file plan, and the known deviations together, because approving pixels is not the same as approving which files move.

### The lint floor

Section 5 and `ui-build` are obeyed by judgement, and an agent that is not Claude Code reads neither. What keeps a later session — any agent's — from re-deciding the design system is the repo refusing it: **the four refusals `ui-build` names under its lint floor, written into the stack's own linter, derived from this app and never pasted from a stock config.**

| Refusal | Derived from |
|---|---|
| Raw element | The shared set the pass promoted, plus what the library ships — only elements this app has a component for |
| Raw value | The utilities and style properties that carry a Section 5 value — colour, radius, font size, the spacing scale |
| Numbered ramp step | The ramp names in the styling files. Not written where a legacy stock Section 5 left no alias layer to read instead |
| Primitive import | The packages the shared set wraps. None → not written |

**Scoped by path.** The components folder is exempt from the first and the fourth, the styling files from the second and the third, and `src/design-canvas/` from all four — it is frozen and dies on its own schedule. On a JS or TS web stack ESLint's `no-restricted-syntax` and `no-restricted-imports` express all four; another stack uses its own analyzer's equivalent, **verified live at write time, never recalled**, and a refusal that analyzer cannot express is reported as `not enforceable on <stack>` — never dropped in silence. A repo with no linter got one in Step 4's block; fix-the-drift skips that step, so there it is one install line approved in chat and named as such, the way the font is.

**Proven on what must pass before what must fail.** Run the lint command over the promoted app first. A hit on a page the pass just wrote is either a real raw value to fix or a pattern too wide — a layout expression (`grid-cols-[1fr_auto]`, a `calc()`) is not a raw value, and a floor that refuses it is disabled within a week. Only then plant one violation of each refusal in a scratch page, see each one refused, and delete the file: a config whose glob matches nothing passes every run and guards nothing.

**Files the pass did not rewrite are baselined, never excused.** Fix-the-drift and `Keep — today's look` leave files standing with hits nobody approved fixing. Those go into the linter's own suppression baseline — verified live that it has one — so the floor refuses every new violation from its first commit. Never by lowering a rule to a warning: no agent reads a warning. The baseline's size is reported at the close, and it only ever shrinks.

**`AGENTS.md` gets its `## UI` part in the same act** — to the shape `app-settle` N5 gives that file, filled from what now exists: the file and folder holding the shared set, the library, the styling file, the `/styleguide` route, the lint command. Where the repo has no `AGENTS.md`, the whole file is written to that shape. It is the only thing an agent without the plugin ever reads about this design system, so a path in it that does not resolve is a failed item, not a typo.

**One floor, one command.** `logic-settle` Step 7 writes five refusals of its own into the same linter. Where that config already exists, these four join it; where it does not, this step founds it and `logic-settle` joins later. Two configs is two commands, and the second is the one no session runs.

The detector stays. It sees the rendered page and the craft floor; the lint floor sees four refusals, and is the only one of the two that runs for an agent with no hook.

**A redesign** — one message, four parts, then a hard stop answered in chat — never an AskUserQuestion:

1. **Section 5 as a diff.** Only what changes, old value beside new — and removals are changes:

```
Accent color : blue #2563EB  →  green #059669
Text steps   : five          →  four (merge section title and body)
Radius       : 8px           →  0
Signature    : ledger seam, sole vertical rule  →  removed
```

A line of the old Section 5 that no new answer, derivation, or canvas ratification re-created leaves through this diff as `→ removed`, never by omission. Where Section 5 was empty, the *old* column is the **measured** value and is marked as such — `Radius : 8px (measured) → 0`; there is no prior Section 5 line to diff against, and writing one as if there were would claim a decision nobody ever made.

2. **The file plan.** Every page line names its source: `replaced by its canvas file`, or `retoken only — no canvas frame` (a stray component the canvas never drew). Two labels, never a third. **In a redesign `retoken only` is not available at all**: a component the canvas never drew is `deleted`, and whatever still needs it is drawn. A redesign that repaints a file it never redrew has left the old design standing under new colour, in the one pass that exists to remove it — and a thin passthrough whose child was redrawn is deleted rather than framed, its callers reaching the redrawn child directly. Reaching this plan with a file unaccounted for is the audit's inventory failing, never a file that needs no verdict. **Shared canvas files carry their own line under the production path their header names** — a plan that lists only pages leaves the largest promotions unwatched, and a composition promoted as loose parts downgrades every page built on it. The plan closes with its **seam points** — where the pass may stop between sessions, read off Step 7's fixed order rather than chosen, and never an estimate of time: what the user needs before approving is where the app will sit half-migrated, not how long it takes. A page whose canvas file exists is replaced by it; listing it `retoken only` is proposing to break the ratified canvas, and that line is put to the user as its own question, never slipped through inside the list. Chrome and shared components created or replaced, styling files, the linter config, `AGENTS.md`, and `UNTOUCHED` files are all listed — a file that should have been listed and is not is a finding, not good news.

```
PASS — [n] files
LeadTable.tsx    replaced by its canvas file
wizard.tsx       → src/components/import-wizard.tsx · shared by 7 pages · replaced by its canvas file
StatusChip.tsx   retoken only — no canvas frame · 4 status colors updated
index.css        11 tokens replaced · 3 deleted · fonts now load here
App.tsx          replaced by its canvas file (chrome)
UNTOUCHED        PhoneContact.tsx
```

3. **The detector's audit count, and what the new direction does to it.** One line: the audit's number, and how many of those hits the canvas removes by construction. The user is about to approve a pass sized in files; this is the one number saying what it buys beyond the look. Hits the canvas does not remove are listed by rule — they survive the pass and return at Step 8.

4. **What approval orders, then what it contradicts.** Ratified elements whose data does not exist yet come first, one line each — element, page, and the work it orders (column · RPC · migration). **Approving the gate orders that work**, so its cost is read here rather than discovered mid-pass; these are not deviations, because the user has decided to build them. Then the deviations: every canvas element the real flow contradicts, and every real control the canvas never drew (`canvas.md`'s canvas-error rule) — one decision line each, answered here, never absorbed silently. **And what approval removes is its own group, confirmed item by item** — every function or control leaving the app because the canvas does not carry it. A blanket *approve everything* covers the other two groups; not this one. A wrong addition is visible on the screen the moment the page opens, and a wrong removal is visible to nobody.

**The gate is a chat stop, not a dialog.** End the turn on the four-part message and wait for the user's reply in chat. An AskUserQuestion here covers the very summary being approved — the user answers the dialog without having read the diff. Ending the turn is what keeps this safe in auto mode: nothing proceeds without an answer. The ban on prose questions elsewhere in this skill covers questions that let the turn carry on, not a gate that stops it.

The user may approve some lines and reject others, naming them in the reply. Rejected values return to the canvas rounds (Step 5) and nothing is written anywhere; approved everything → the pass. Nothing changed at all → say so and close at Step 9.

**Fix the drift, or `Keep — today's look` with Section 5 filled** — the same gate shows the findings list instead:

```
REPAIR — [n] findings
1  Usage.tsx:185-188   gradient text           impeccable · craft floor, Refuse
   3 sentences  →  removed
2  StatusChip.tsx:19   label 15 chars          S5 · Repeated label length
   "Belum dihubungi"  →  icon only, text to aria-label
```

STOP and wait for approval per item. A rejected item is not silently dropped — it stays a finding and is reported again at Step 9.

## Step 7 — The pass: every page, in one session

**Where UI exists, branch first.** Create the pass's own branch or worktree from a committed base (`design/rework-<date>` or the user's naming). Parallel work continues in the main tree untouched; the canvas folder, if untracked, is brought along into the worktree. Revert of the whole redesign is now one move — drop the branch — available at the user's word at any point, closing the session at Step 9. **First act: write Section 5** — the approved text, in full, rebuilt from zero. Then `CLAUDE.md`'s Component library row if the library answer changed. This is the only moment the PRD is written. **The gate block travels with the branch**: the pass's first commit carries it in its message body — Section 5 diff, file plan, ordered work, and the deviations the user answered. Chat scrollback does not survive the session, and a later session that cannot read what was approved cannot tell drift from a decision; neither can the user. `git log` is where this repo already keeps that kind of memory. **Second act: the freshness check.** Time may have passed between ratification and this session, and parallel work may have changed the app. Re-walk the function inventory against the current code; a flow that changed since the canvas was ratified is a new deviation line, put to the user **before** its page moves — the canvas is frozen, so reality has to win by decision, not by silence.

**Where no UI exists, no branch is needed** — a fresh repo has no parallel work to disturb; Section 5 was written at Step 6, and the pass runs in place.

**All canvas pages are promoted in one pass** — each file copied to its real route, the canvas wrapper removed, per `canvas.md`: element for element, in an order that cannot be reversed:

1. **Foundations.** The theme files take the new token values — old tokens **deleted**, not deprecated — and everything the canvas CSS carries beyond values lands with them: **the font loading itself** (link or package — a face the frames chose that needs a package is installed here where Step 6 has not already, one line approved in chat — then verify in the browser that the computed font-family resolves to the loaded webfont, not a fallback; a token grep cannot see a font that never loads), element-level rules, shadows, motion durations. The five styling-file rules of Step 6 bind here: the two-layer palette the canvas ratified, every semantic slot mapped, no unread tokens, duplicate roles collapsed, both theme files in the same edit.
2. **Chrome and shared components, from the canvas chrome.** Each shared component a canvas page imports lives in the production chrome before any page importing it counts as moved — the canvas markup is the component; the production logic (auth, navigation state, data) is wired into it, never the reverse. **Where they land follows `ui-build`'s placement rule**: the components that hold Section 5 rules in one file, a component carrying a flow of its own in its own file. Promotion is the moment that file comes into existence, and every later session is told to read it — scattering the set across fifteen files leaves that instruction pointing at nothing.
3. **Pages — the proving page first.** Each canvas file **copied to its real path**, the canvas wrapper removed. **Where a data layer exists**, the fixture import is swapped for it; the markup body does not change — that is what Step 8 will diff — and each page is checked at both widths for survival of real data: holding → report and continue; the first collapse → stop, a rework round of that page, two at most, then Section 5 reopens through `canvas.md`'s escalation. **Where there is no backend yet**, the pages keep their fixtures — reshaped into `build-flow`'s contract form (`src/contracts/<page>.ts` for the types, `src/contracts/<page>.fixtures.ts` for the cases, per `references/contract.md` of `build-flow`) — and **every promoted-but-unwired page gets a `QUEUE.md` line**, `wire <page> to real data`, written by this pass. An app full of fixture-driven pages looks finished while every number on it is fake; the queue lines and the close block are what keep that visible. Where `logic-settle` already chose the data layer, its loading, empty, and failed states come from the chosen cache when wiring happens — never from a handwritten effect.
4. **Components not on the canvas** — **fix-the-drift only**: retoken until zero raw values remain, and a component prop or theme value departing from what the library ships goes back to the library default in this same pass, unless a Section 5 line requires the departure. **In a redesign this step is empty by construction** — the gate gave every such file a `deleted` verdict. A file still standing here is a failed inventory to report, never a file to quietly retoken.
5. **`/styleguide`** — part of the pass: archetype cards updated to the ratified shells, every component the pass created rendering there, held to Step 6's done-check.
6. **Assets** locked to the old colors — where UI exists: inline SVG, favicon, images carrying brand color.
7. **The old library and engines are removed**, if their decisions changed.

**The proving page is the bar.** `build-flow` Section 4 judges every later page against it — building it thin lowers the bar for the whole app. Where it carries data, its fixtures must include `bulk` and `messy` cases: a direction that only holds for five tidy rows has not been proven. `ui-build` binds every promoted page in full — tokens only, zero raw values, states drawn.

Page running → **prove it at two widths with screenshots**: the desktop breakpoint from Section 5 and the ratified lowest supported width. Capture follows PRD Section 1's Proof profile — the browser is the web profile's answer; a platform whose profile names an emulator or a window capture proves the same two bounds through it. No capture tooling → say so and report the profile's run target with both widths named — never claim the widths were judged without either.
8. **The lint floor, then `AGENTS.md`'s `## UI` part** — last, because both are derived from the shared set and the styling files as they now stand. Step 6 holds the spec; fix-the-drift writes them too, since neither is a new norm — they make the existing Section 5 mechanical.

**The UI code is the pass's to rewrite — the behavior is not.** What must come out unchanged is the business behavior — the queries and mutations called, the guard conditions, the route paths, the outcome of every action a user can take. Do not slip in unrelated fixes: a redesign that also tidies logic produces a diff nobody can read, and one mistake will hide among hundreds of legitimate changes.

**Detector findings are deferred here, and this is where it matters most.** `impeccable`'s craft floor tells the model to act on hook findings as it edits; inside this pass that instruction is overridden. The canvas is already approved, so a hit is a difference the session would prefer — refused by the rule below, not weighed. Collect them and report them at Step 8, where there is already a fix loop and the user can see the whole list at once.

**The approved canvas is the specification, and the pass implements it rather than negotiating with it.** An element the canvas drew lands as drawn; an element it did not draw does not land, and prose the canvas left out is deleted rather than carried over — the user answered that by approving the drawing, so asking again re-opens a settled decision and is how the result drifts. A difference the session would prefer is refused, not raised as a question.

**One exception, and no other: an element the user ratified whose data does not exist yet.** The pass writes no query for it — that stays forbidden. It promotes the element **rendered empty and labelled as waiting**, and writes one `QUEUE.md` line naming the data it needs. Dropping it silently is a failed promotion, and so is hiding it behind a flag: a page that reads finished while an approved element is missing is the one state nobody can see.

**One thing still stops the pass**, and it is the freshness check above plus this: a drawn element that would make the app claim what it cannot do. That is a `build-flow` stop, not a design question.

**Rework rounds.** A page collapsing under its fixtures or its real data, or the user asking for a rework, is a rework round of that page. **Two rework rounds of the same page at most — a third does not run, and Section 5 reopens**: the reference slot is re-asked with sharpened options and the frames redrawn, and the canvas is regenerated fresh from the new pick, never patched. Section 5 changed → the styling values are updated with it, and the pages are rebuilt from the new tokens rather than patched.

**Fix the drift** runs here too, on the same isolated branch: fix the approved findings, nothing else.

## Step 8 — Verification: evidence, not eyes

A claim of parity from the session that produced the code is worth nothing on its own — every check below leaves something the user can inspect. All of them before reporting done:

- **The build passes.** It does not → stop, fix it, do not report done.
- **The structural diff per canvas file — the primary evidence.** Every canvas file, not every promoted page: a page whose body delegates to a shared file diffs empty, and the diff that matters moves to that shared file, under the production path its header names. The differences must be confined to the data seam — the fixture import swapped for the data layer, plus its loading and error wiring; with fixtures kept, only the removed canvas wrapper and the contract-shaped fixture import — and to lines the user answered at the gate. Any other difference is a failed item to fix now, whichever side reads better. Report the verdict per file; a file whose diff cannot be shown is not verified.
- **Computed styles probed in the browser.** The fonts resolve to the loaded webfonts, not a fallback stack — the canvas CSS carried the loading, and the production entry must carry it now; spot-check token slots on live surfaces against the theme files. (The web profile's check — a platform whose Proof profile names no browser verifies the equivalent through its Visual line, and says what could not be verified.)
- **The rendered structure matches, counted.** Both sides are live in the same dev server — the canvas at its dev route, the page at its real one. Read the element tree of each page body (element names and class lists, **text and numbers discarded** — discarding the text is what takes the data out of the comparison) and report one line per page: `canvas n · live n · differs n`. Anything above zero names the extra or missing elements and is a failed item now. "Richer than the canvas" is drift wearing a compliment, and this count is what sees it. Chrome the two sides do not share is excluded and said so; a page whose count cannot be produced is not verified.
- **Zero raw values** across every promoted page and component — search again for hex, font sizes, and raw spacing.
- **The styleguide passes its done-check** (the table in Step 6), its foundations rendered as specimens rather than as a table of names and values.
- **Every contrast ratio on the page was computed**, not recalled, in every ratified theme mode, and every semantic dark shade clears 4.5 against its own light shade.
- **The fixtures close** on every page still running on them — totals, percentages, bar widths, pagination — per `canvas.md`'s Coverage.
- **The detector ran against the running app**, not only against `src/` — `impeccable`'s full rule set needs a rendered page; point it at the dev server. Report the hit count — beside the audit's count where UI existed — and triage every hit in the same block: fixed, or left standing as a finding with one line saying why. A hit left standing is not a failure of this step; an unreported one is. `impeccable` absent → say the check could not run, and do not report the step as passed on silence.
- **The lint floor passes, and bites.** Zero hits outside the baseline, and each refusal was seen refusing its planted violation — reported per refusal, with `not enforceable on <stack>` named where the analyzer could not express one. Every path `AGENTS.md`'s `## UI` part names resolves.
- **The signature survived promotion**, on the pages that carry it. A signature that exists on the canvas and not in the app is a failed item, not a simplification.
- **The proving page holds at both widths**, screenshots taken.
- **Pages running on fixtures are listed by name.** This list matches the `QUEUE.md` wire lines one for one — a page on neither list does not exist.
- **Where UI existed — the file plan matched.** Every file listed at the gate changed, and no file outside that list did.
- **Where UI existed — the seeded walk.** Seed `[CLAUDE]`-prefixed rows first — an empty database renders empty states the canvas never drew, and a parity claim over empty tables is void. Then walk the proving page at desktop and at the lower bound, and compare one page per archetype against its audit screenshot: every archetype reads redesigned, unless everything behind it was answered *keep* and the gate said so.
- **Where UI existed — function parity holds.** Walk the audit's function inventory line by line: every function is still reachable **at both widths — a control hidden below the breakpoint is a missing function at the minimum width, not a responsive choice** — wherever it now lives. A line missing everywhere is a failed item to fix now, unless the user cut it at the judgement and the gate said so.

Any of them fails → fix it in the same session. A half-finished pass is worse than none: the app still runs, so nobody knows it is broken.

**The canvas files stay after promotion** — frozen references under `canvas.md`'s lifecycle. **All checks passing earns the right to propose deletion — never to delete.** Where UI existed and the pass wired real data in-session, one confirmation covers the whole canvas: report the diff verdict per page, invite the user to walk canvas and app side by side at `/design-canvas`, then end the turn and ask whether the canvas and the seed rows may go — a chat stop, never an AskUserQuestion, which would cover the verdict being read. Only a granted confirmation deletes — the page files, the entry route, the foundations board, and the canvas CSS together. The user refusing, or naming any page, turns each named page into a failed item of the pass to fix now; the canvas stays alive until a later confirmation clears it. Where pages left on fixtures, each canvas file dies only when its page is wired with real data, survives both widths, and the user confirms the side-by-side — `build-flow` carries that per page through the queue. Never delete unasked.

## Step 9 — Close

**Nothing stays a draft.** Every canvas page ends promoted into a real route; a page left in the repo unrouted is dead code that reads as finished work.

The close carries the detector's numbers — Step 8's count, beside the audit's where UI existed — and names every hit left standing with the one line that justified it. A design flow that ends without that number has verified its own work by assertion.

One block: the visual decisions that settled — the Section 5 lines that changed, where there was an old one · files changed, with their count, and files `UNTOUCHED` · each page's fate — promoted and wired, or promoted on fixtures with its `QUEUE.md` wire line · items the user rejected, still standing as findings · the canvas outcome and how many rounds it took · the verification results, per-page diff verdicts included · the canvas files still standing and the queue line that will retire each · the `/styleguide` route named as staying dev-only, deletable at the user's word · the lint floor — refusals written, the baseline's size, anything `not enforceable` · what is still `[needs verification]` · **the PRD sections `app-settle` still owes**, where the PRD was missing or off-shape — `build-flow` will not open a page until Sections 2–3 exist.

**A pass this session could not finish is written down, not implied.** Every page not yet promoted, and every verification item not yet passing, becomes a `QUEUE.md` line — one each. A truncated pass must read as unfinished in the repo itself; the canvas stays alive as the reference until those lines clear.

State that this gate **no longer applies** to later pages — from here on what binds is Section 5 and the component rules in `ui-build`.

**The commit waits for the user's word.** Where the pass ran on its own branch, propose it there — a diff of this size deserves a commit of its own, with nothing else riding along inside it; merging the branch back is also the user's move, and it is the single point where this work meets whatever parallel sessions built in the meantime. Never push, never open a PR.

Nothing changed — every answer was *keep*, today's look was picked, or the canvas was reverted → say that in one line and list the audit findings that remain. A session that changes nothing has still produced the audit, and that is worth writing down.
