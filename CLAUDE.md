# CLAUDE.md — repo raizen-toolkit

This repo is not an application. It holds plugins that govern other repos, so a mistake here spreads to every app.

## Language

All files in this repo — `SKILL.md`, references, templates, README — are written in English, so they work for anyone who installs them.

Reply language is not fixed. Follow whichever language the user writes in.

## Rules

Skills and norms here are read by other agents, not by humans. Write them as direct instructions, not as observations.

Keep every rule short. One rule is one imperative sentence. Give its reason in one clause, only when an agent would otherwise break the rule. Cut any paragraph that argues, defends, or restates. State each rule in one file only; other files point to it by name.

Do not add a skill to `raizen-norms` without naming what would be lost if it did not exist. Every skill pays a context cost in every session through its description, including the sessions that never use it.

Hooks block without being able to ask. A new hook must first be tested against the cases that **should pass**, not only the ones that must be refused. A hook that is too strict costs more than no hook.

This plugin ships no templates. What a new app repo gets is written by `app-settle` for that repo's answers — never a stock file, which is a decision taken before its question was asked and goes stale without anyone re-reading it. Whatever a skill here tells a session to write lands in app repos that may not be private, so a rule that produces a file must never produce a secret in it: name the variable, never its value.

## Proof runs

A proof run tests these skills on a throwaway copy of an app in the scratchpad. Write only the public client values into the copy's `.env` — the URL and the publishable key; never copy the real `.env`. A server key reaches the copy only by the user's own hand: a key created for the run and revoked after it. Without one, report every server route `not verified — no server key in the proof copy`.

## Git

Commit only when the user says so. Do not push, do not open a PR on your own initiative.

A commit that changes a plugin bumps that plugin's `version` in the same commit, because `/plugin update` compares version numbers only; `.githooks/pre-commit` refuses it otherwise, so run `git config core.hooksPath .githooks` once per clone.

A commit reaches app sessions only after it is pushed to `origin`, and the user decides every push.
