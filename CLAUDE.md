# CLAUDE.md — repo raizen-toolkit

This repo is not an application. It holds plugins that govern other repos, so a mistake here spreads to every app.

## Language

All files in this repo — `SKILL.md`, references, templates, README — are written in English, so they work for anyone who installs them.

Reply language is not fixed. Follow whichever language the user writes in.

## Rules

Skills and norms here are read by other agents, not by humans. Write them as direct instructions, not as observations.

Do not add a skill to `raizen-norms` without naming what would be lost if it did not exist. Every skill pays a context cost in every session through its description, including the sessions that never use it.

Hooks block without being able to ask. A new hook must first be tested against the cases that **should pass**, not only the ones that must be refused. A hook that is too strict costs more than no hook.

Do not put secrets in `templates/`. This repo is private, but what it copies lands in app repos that may not be.

## Git

Commit only when the user says so. Do not push, do not open a PR on your own initiative.
