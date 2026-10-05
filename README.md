# raizen-toolkit

`raizen-norms` is a plugin for Claude Code and Antigravity. Three interview skills decide with you an app's scope and stack, its logic layer and its look, and write the answers into the repo; rule skills, session norms and guard hooks hold every later session to those answers.

## Install

Claude Code:

```
/plugin marketplace add rapidkaizen-cloud/raizen-toolkit
/plugin install raizen-norms@raizen
```

Antigravity:

```
agy plugin install https://github.com/rapidkaizen-cloud/raizen-toolkit
```

Requirements and companion skills: [Claude Code](docs/start/install.md), [Antigravity](docs/guide/antigravity.md).

## Use

In an empty folder, run `/raizen-norms:app-settle`, then `/raizen-norms:logic-settle` and `/raizen-norms:design-settle` in the repo it creates. After that, ask for a page; the rule skills load by themselves.

An app that already exists: [Quickstart](docs/start/quickstart.md). Every command: [Commands](docs/reference/commands.md).

## Documentation

<https://rapidkaizen-cloud.github.io/raizen-toolkit/>, or the same pages under [`docs/`](docs/README.md). What changed: [CHANGELOG.md](CHANGELOG.md). In a session: `/raizen-norms:norms-help`.
