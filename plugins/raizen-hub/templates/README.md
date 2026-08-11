# templates/

Copied by `app-init` into a new app repo. `{{...}}` placeholders are filled from the interview answers.

Nothing here is a secret, and nothing here is a placeholder *for* a secret. The only value filled in is `{{SUPABASE_PROJECT_REF}}`, an identifier — Supabase access is granted by a browser login, and the CI database URLs live in GitHub secrets. This repo is private, but what it copies lands in app repos that may not be, so a template that asks for a token is a template that eventually gets committed with one in it.
