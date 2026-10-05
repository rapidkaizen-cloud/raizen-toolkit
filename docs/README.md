# docs — raizen-toolkit

For the people who install the plugin. What an agent obeys is in `skills/` and `scripts/`; nothing here is a rule, and where a page and a skill disagree the skill is right and the page is the defect.

| File | Holds |
|---|---|
| [guide/gates.md](guide/gates.md) | The two stops a hook enforces — publishing, and destructive SQL: what you see, what you answer, what the hook checks and what it does not |
| [guide/documents.md](guide/documents.md) | The documents an app repo keeps: where to look for what, and what gets each one written — the rule, the reminder after a commit, the audit |
| [queue.md](queue.md) | Toolkit work not done, or done and not proven |
| [../CHANGELOG.md](../CHANGELOG.md) | What changed in each version, newest first. Kept at the root, where an installed copy's `norms-version` fetches it |
| [../README.md](../README.md) | What the plugin is, how to install and update it, the two hosts |

A feature with no page under `guide/` has its skill as the only source: `skills/<name>/SKILL.md`.
