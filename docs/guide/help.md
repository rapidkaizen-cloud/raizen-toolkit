# Help — the commands, the pages, the version

Ask any session for help with these skills: type `/raizen-norms:norms-help`, or ask in your own words — which command to run, what version this is, what changed.

You get one card, in your language:

| Part | Holds | Taken from |
|---|---|---|
| Version | The number of the copy this session runs | The plugin's manifest |
| Commands | What to run in which situation | `README.md`, `Use` |
| Pages | Every page under `docs/`, and what it holds | `docs/README.md` |
| Last change | The newest changelog entry, with what it asks you to act on | `CHANGELOG.md` |

- **Ask a question with it** — "how does the push stop work" — and the session answers from the page that covers it and names the file. Where no page does, it answers from the skill itself and says so.
- **The version is its number and that one entry.** Whether a newer version exists is not checked: a machine with `autoUpdate` on gets it at its next start, and `README.md` holds the update under `Update`.
- **The card is about the copy the session loaded**, not the newest one on the machine: a project-scope install can sit versions behind the user-scope one.
- **Nothing is changed.** A `To act on` line is shown, and acted on only when you ask.

The skill: `skills/norms-help/SKILL.md`. The script: `scripts/norms_help.py`.
