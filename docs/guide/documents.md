# Documents — what an app repo keeps, and what gets them written

An app settled by `app-settle` keeps its documents under `docs/`. `docs/PRD.md` is the app as you first approved it and is frozen from then on; what the app is today lives in the files beside it, and each is corrected when it stops being true rather than appended to. The full list, with who writes each file and when, is the closed list in `skills/docs-format/SKILL.md`.

## Where to look

| You want | Read |
|---|---|
| What changed that users notice, newest first | `docs/whats-new.md` — one entry per commit users will notice |
| How a role gets one piece of work done | `docs/guide/<task>.md` — one page per task, written in the commit that makes its page usable |
| Why a choice was made | `docs/decisions/` — one record per decision you took, never edited afterwards |
| What a rule is, and why | `docs/rules.md` |
| What is not built yet | `docs/queue.md` |
| The app as first approved | `docs/PRD.md` |

## What gets a document written

In order, from the moment of the change to the latest it can be caught:

1. **The rule.** The commit that makes a document false carries its correction, never a later commit.
2. **The reminder.** After a commit that touched no document, the session is handed three questions: did a sentence in a document become false, did a page become usable with no guide page, will users notice. It answers by writing the document into that commit, or by reporting `Docs: none` for it. The reminder never blocks a commit. On Claude Code it arrives with the commit's result; on Antigravity, before the session's next step, once per commit.
3. **The closing report.** Every session ends on a `Docs:` line naming the documents it changed and what waits for your decision.
4. **Session start.** A path a living document names that no longer exists is listed before any work.
5. **The audit.** `app-settle`, run again on a settled app, counts the tasks with no guide page and the documents outside the list, and turns each into a queue line or a fix you pick.

Only the first is a rule; the rest exist because a rule alone gets skipped. None of them refuses a commit: most commits owe no document, and a hook cannot tell which do.

## What you will not find

- **Anything a reading of the code or the database gives back** — tables, columns, routes, components, whether something is built. A document answering those goes stale without failing anything.
- **Change history inside a living document.** History is `docs/whats-new.md`, the frozen records, and `git log`.
- **A help page inside the app**, unless you ask for one. The guide pages and `docs/whats-new.md` are written either way; the page rendering them is a queue line.
- **Guide pages and `docs/whats-new.md` in a repo still on a root `PRD.md`.** That form writes neither until `app-settle` migrates it; the reminder there asks about `PRD.md` and `QUEUE.md` instead.

The rules: `skills/docs-format/SKILL.md`, and `skills/build-flow/SKILL.md` Section 8. The reminder: `scripts/remind_docs.py`, called on Antigravity from `scripts/session_norms.py`.
