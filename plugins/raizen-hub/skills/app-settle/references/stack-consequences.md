# Consequences per choice

Research already paid for. Bring these up when the related choice is made — do not wait to be asked.

## Cloudflare Workers + Vite

Vite freezes `VITE_*` variables at **build** time, not at runtime. Cloudflare Workers Builds does not yet separate production and preview branch configuration natively, so a preview pointing at the staging database needs Wrangler Environments plus a separate build command.

If per-PR previews are not needed, this consequence disappears and Cloudflare becomes an equal choice.

## Vercel Hobby

Hobby forbids commercial use. This is a licensing restriction, not a technical limit, and the definition of "commercial" in their fair use guidelines is broad — an app that runs business operations falls under it. Cloudflare has no equivalent clause.

The tightest limit on Hobby: build minutes per month. Per-PR previews consume them too. Exceeded → the project is paused, not billed.

**Say this when the user picks Vercel; do not save it for later.** It decides cost, not code shape.

## Supabase free tier

No backups. For an app whose data is operational, this is the main reason to move to a paid plan — not capacity.

A project untouched for seven days is auto-paused. If migrations run regularly through CI, that activity alone prevents it.

## Staging as a second cloud project

Preview deployments run on the hosting provider's servers, so they cannot reach a database on `localhost`. A local database stays useful for development on your own machine, but it cannot be a preview target.

## Migrations through GitHub Actions

Schema gets versioned in git, and staging stays in sync with `main` without a manual step.

The consequence that changes other rules: **schema gets git, data does not.** A `DROP COLUMN` can be undone with a new migration; a deleted row cannot. The destructive gate still applies in full to `DELETE`, `TRUNCATE`, and `UPDATE` without a narrow `WHERE`.

## Static SPA on any host

Needs every path rewritten to `index.html`, otherwise refreshing on a nested route returns a 404. Nothing here scaffolds it — the session writes it for the host chosen at question 4: a `rewrites` entry in `vercel.json`, a `redirects` line in `netlify.toml`, or one `try_files $uri /index.html;` on an own server.
