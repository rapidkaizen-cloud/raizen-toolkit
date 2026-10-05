# Quickstart

Pick the case that matches your repo, run the command, and answer what the session asks.

## A new app

1. **Open Claude Code in an empty directory.**
2. **Run `/raizen-norms:app-settle`.** It reads the directory, finds it empty, and bootstraps the app: an interview, the documents, a scaffold, `git init`.
3. **In the new repo, run `/raizen-norms:logic-settle`**, then **`/raizen-norms:design-settle`**.
4. **Ask for the first page.** `build-flow` needs no command; it loads in every app session and builds from `docs/queue.md`.

The long version: [Start a new app](../guide/new-app.md).

## An app that already exists

1. **Open Claude Code in the repo and run `/raizen-norms:app-settle`.** It reads the repo and runs the one mode it owes next:

   | It finds | It does |
   |---|---|
   | Code, no documents | Documents the app, changing nothing about it |
   | A root `PRD.md` | Migrates it to the `docs/` form, in one commit |
   | Documents in place | Audits the repo against the rules and fixes what you pick, one finding per commit |
   | Documents in place, and you ask for a change | Reworks the app's decisions, keeping first |

2. **Then run `logic-settle` and `design-settle`**, or only the one whose layer you want settled.

> [!WARNING]
> The migrate and align modes have never run in a real app. Run them on a copy first. See [What is proven](../reference/status.md).

The long version: [Bring in an existing app](../guide/existing-app.md).

## What you will notice in every session after

- **It starts already knowing the norms.** Language, scope, git, asking and decisions are printed before your first message. See [Session norms](../concepts/session-norms.md).
- **It commits by itself.** A finished scope item is committed in the same turn, with named paths.
- **It does not publish by itself.** A push or a pull request waits for your reply in chat.
- **It does not destroy data by itself.** Destructive SQL waits for a number you approve.

The last two are the [gates](../concepts/gates.md).

## Stuck?

Run `/raizen-norms:norms-help`, or ask a session in your own words which command to run. See [norms-help](../reference/norms-help.md).
