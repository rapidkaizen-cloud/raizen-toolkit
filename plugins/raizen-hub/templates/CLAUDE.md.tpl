# CLAUDE.md — {{APP_NAME}}

This file holds **what is true of this app alone**. Norms that hold in every app repo — build order, scope, git, the closing report, which skill to read before touching what — are printed by the `raizen-norms` plugin at the start of every session. They are deliberately not copied here: a norm that exists in two places is a norm that will disagree with itself.

Do not add a norm to this file. If a rule would hold in every app, it belongs in the plugin.

## Locale

| | |
|---|---|
| On screen | {{UI_LANGUAGE}} — page titles, labels, buttons, messages, empty states |
| In the code | English — comments, identifiers, file names, URL routes, API endpoint paths, and every database name: tables, columns, views, enum types, functions, policies, migration file names |
| Dates | {{DATE_FORMAT}} |
| Numbers | {{NUMBER_FORMAT}} |

The two first rows are separate on purpose. "UI in {{UI_LANGUAGE}}" is not a licence for a component file named after a screen label, a route named after a menu item, or a view named after a PRD term. A route is an identifier the user happens to see; the menu label above it is the thing written for them.

`PRD.md` is written in the user's language, and a term it uses for a thing in the code is translated on the way in — not copied.

Enum values are the one judgement call: they are stored data rather than a name, so weigh readability against rewriting every existing row, and map them to English keys at the boundary either way. Record the decision here when one is made.

Reply language is not set here — it follows whichever language the user writes in.

## Stack

| Aspect | Choice |
|---|---|
| Frontend | {{FRONTEND}} |
| Hosting | {{HOSTING}} |
| Database | {{DATABASE}} |
| Auth | {{AUTH}} |
| Component library | {{COMPONENT_LIB}} — filled in by `/design-init`, not at bootstrap |
| Environments | {{ENVIRONMENTS}} |
| Migrations | {{MIGRATIONS}} |

**This app's** stack is locked as of bootstrap. The choices themselves are not uniform across apps — they were assembled from this app's needs when `/app-init` ran. What is locked is the outcome, not the menu.

Do not add a library or dependency without the user's approval in this session.

## Ground truth

The code and the live database are ground truth for **facts**. `PRD.md` is ground truth for **intent and prohibitions**. Conflict about what exists → the code wins. Conflict about what ought to be → the PRD wins, and the code is a finding.

## Gate

PRD Section 5 still `[needs verification]` → the visual direction is not set. Run `/design-init` first; `ui-build` will refuse to write components until that is done.

This gate and the ground-truth rule above stay in this file on purpose. They must still bite in a session where the plugin is absent, disabled, or failed to start.

## Rules for this app only

_Empty at bootstrap. Add only rules that would be wrong in another app._
