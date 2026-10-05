# Documents — what an app repo keeps, and what gets them written

An app settled by `app-settle` keeps its documents under `docs/`. `docs/PRD.md` is the app as you first approved it and is frozen from then on; what the app is today lives in the files beside it, and each is corrected when it stops being true rather than appended to. The full list, with who writes each file and when, is the closed list in `skills/docs-format/SKILL.md`.

## Where to look

| You want | Read |
|---|---|
| How the parts connect, and where each kind of code lives | `docs/architecture.md` |
| How to deploy, roll back and restore, and what to check when it is down | `docs/runbook.md` |
| What changed in how the app behaves, newest first | `docs/changelog.md` — one entry per commit that changes behaviour |
| How a role gets one piece of work done | `docs/guide/<task>.md` — only in an app that keeps help for its users |
| Why a choice was made | `docs/decisions/` — one record per decision you took, never edited afterwards |
| What a rule is, and why | `docs/rules.md` |
| What is not built yet | `docs/queue.md` |
| The app as first approved | `docs/PRD.md` |

## What gets a document written

In order, from the moment of the change to the latest it can be caught:

1. **The rule.** The commit that makes a document false carries its correction, never a later commit. A commit that changes how the app behaves carries a `docs/changelog.md` entry. A commit that changes no document is reported `Docs: none` with its reason — no commit goes unreported.
2. **The reminder.** After a commit that touched no document, the session is handed its questions: did a sentence in a document become false, did the app's behaviour change, did it finish a queue line — and, in an app that keeps help for its users, did a page become usable with no guide page. It answers by writing the document into that commit, or by reporting `Docs: none` and why. The reminder never blocks a commit. On Claude Code it arrives with the commit's result; on Antigravity, before the session's next step, once per commit.
3. **The closing report.** Every session ends on a `Docs:` line naming the documents it changed and what waits for your decision.
4. **Session start.** A path a living document names that no longer exists is listed before any work.
5. **The audit.** `app-settle`, run again on a settled app, counts the documents that are missing or outside the list — and, where help is kept, the tasks with no guide page — and turns each into a queue line or a fix you pick.

Only the first is a rule; the rest exist because a rule alone gets skipped. None of them refuses a commit: most commits owe no document, and a hook cannot tell which do.

## What you will not find

- **Anything a reading of the code or the database gives back** — tables, columns, routes, components, whether something is built. A document answering those goes stale without failing anything.
- **Change history inside a living document.** History is `docs/changelog.md`, the frozen records, and `git log`.
- **Help for the app's users**, unless you ask for it. `app-settle` asks once: none, guide pages in the repo, or a help page inside the app. Until the answer is one of the last two, no `docs/guide/` page is written.
- **`docs/architecture.md`, `docs/runbook.md` and `docs/changelog.md` in a repo still on a root `PRD.md`.** That form writes none of them until `app-settle` migrates it; the reminder there asks about `PRD.md` and `QUEUE.md` instead.

The rules: `skills/docs-format/SKILL.md`, and `skills/build-flow/SKILL.md` Section 8. The reminder: `scripts/remind_docs.py`, called on Antigravity from `scripts/session_norms.py`.
