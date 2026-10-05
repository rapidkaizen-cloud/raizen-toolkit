# raizen-toolkit

One plugin, `raizen-norms`, and the marketplace `raizen`, in the public repo `rapidkaizen-cloud/raizen-toolkit`. It settles an app one layer at a time and holds every later session to what was settled. The repo root is the plugin, for Claude Code and for Antigravity.

| Holds | Loaded |
|---|---|
| `app-settle`, `logic-settle`, `design-settle` | When invoked |
| `build-flow`, `docs-format`, `ui-build`, `db-ops`, `logic-build` | By their descriptions |
| `norms-help` | When asked for help, which command to run, the version, or what changed |
| Session norms, guard hooks | Every session where the plugin is enabled — installed at user scope, every folder on that machine |

## Install

```
/plugin marketplace add rapidkaizen-cloud/raizen-toolkit
/plugin install raizen-norms@raizen
```

Requirements, the companion skills and the check: [docs/start/install.md](docs/start/install.md). On Antigravity: [docs/guide/antigravity.md](docs/guide/antigravity.md).

## Documentation

Every page is under [`docs/`](docs/README.md); the same pages are a site at <https://rapidkaizen-cloud.github.io/raizen-toolkit/>.

| You want | Read |
|---|---|
| What it is, and the first run | [Overview](docs/start/overview.md), [Quickstart](docs/start/quickstart.md) |
| What to run in which situation | [Commands](docs/reference/commands.md) |
| What a session will stop for | [Gates](docs/concepts/gates.md) |
| One page per skill and per hook | [The index](docs/README.md) |
| What changed in each version | [CHANGELOG.md](CHANGELOG.md) |
| What has run for real, and what has not | [What is proven](docs/reference/status.md) |

In a session: `/raizen-norms:norms-help`, or ask in your own words.
