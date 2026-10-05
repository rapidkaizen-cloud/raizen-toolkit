---
name: norms-version
description: Report which raizen-norms version this session runs, when it was released and reached this machine, whether origin holds a newer one, and what its changelog says — and offer the update when it is behind. Use when the user asks what version the skills are, when they were last updated, whether they are up to date or an update exists, or what changed.
---

# norms-version — which copy this session runs

**Run `python3 <plugin folder>/scripts/norms_version.py` and relay what it prints.** The plugin folder is the one this skill is read from, two levels above this file — never another copy, because a machine keeps one folder per installed version and the script reports the folder it sits in.

- **Relay the five lines as printed, then each changelog entry in the user's language**, its `To act on` lines word for word and acted on only when the user asks.
- **The user asks for more history → pass the number of entries**: `norms_version.py 5`.
- **`behind` → say that this session keeps running this copy until the machine updates and the host restarts**, then ask in one AskUserQuestion whether to update now: `Update`, `Not now`.
- **`Update` → run the commands under `Update` in the plugin folder's `README.md`**, report what each printed, and say the host must restart. No update runs without that answer.
- **On Antigravity, ask nothing and report `behind` only**: its update removes the plugin this session's hooks run from, so it runs with no session open — the `README.md` holds it under `Antigravity`.
- **`not reachable` → say the comparison was not made.** Never name a newest version from memory.
- **Asked when one skill last changed → the newest entry of the plugin folder's `CHANGELOG.md` that names it**, found by search; every skill here carries the plugin's one version.
- **A companion skill installed beside this plugin is versioned by its own installer** and is not reported here; say so when asked.
