# Changelog

All notable changes to the `raizen-hub` and `raizen-norms` plugins, newest first. The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/). Versions before these are in `git log`.

## [raizen-hub 0.65.0, raizen-norms 0.31.0] - 2026-09-28

### Changed

- `ui-ux-pro-max` is Required, level with `impeccable`: a session without it asks before continuing.
- `ui-build`: where both skills set a UX floor, the stricter one applies; any other contradiction is reported to the user; `DESIGN.md` outranks both.
- `design-settle`: style, colour, and typography search runs once per frame, with that frame's direction as the query.
- `design-settle`: every frame and canvas round meets the UX floor. Step 8 checks Critical and High don'ts per interaction on every promoted page; Step 9 reports any left standing.

### Removed

- `design-settle`: the pure frame, its draw question, and the rule that one frame is drawn without `ui-ux-pro-max`.
