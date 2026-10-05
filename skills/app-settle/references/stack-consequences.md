# Consequences per choice

Say each one when its choice is made — do not wait to be asked.

## Cloudflare Workers + Vite

Vite freezes `VITE_*` variables at **build** time, not at runtime, and Cloudflare Workers Builds does not yet separate production and preview branch configuration natively: a preview pointing at the staging database needs Wrangler Environments plus a separate build command. Per-PR previews not needed → this consequence disappears and Cloudflare is an equal choice.

## Vercel Hobby

**Say this when the user picks Vercel** — it decides cost, not code shape. Hobby forbids commercial use: a licensing restriction, not a technical limit, and their fair use guidelines define "commercial" broadly — an app that runs business operations falls under it. Cloudflare has no equivalent clause. The tightest Hobby limit is build minutes per month, which per-PR previews consume too; exceeded → the project is paused, not billed.

## Supabase free tier

No backups — for an app whose data is operational, the main reason to move to a paid plan, not capacity. A project untouched for seven days is auto-paused; migrations running regularly through CI prevent it.

## Staging as a second cloud project

Preview deployments run on the hosting provider's servers, so they cannot reach a database on `localhost`: a local database serves development on your own machine, never a preview target.

## Migrations through GitHub Actions

Schema gets versioned in git, and staging stays in sync with `main` without a manual step. **Schema gets git, data does not**: a `DROP COLUMN` can be undone with a new migration, a deleted row cannot. The destructive gate still applies in full to `DELETE`, `TRUNCATE`, and `UPDATE` without a narrow `WHERE`.

## Static SPA on any host

Every path must be rewritten to `index.html`, otherwise refreshing on a nested route returns a 404. The session writes it for the host chosen at question 4: a `rewrites` entry in `vercel.json`, a `redirects` line in `netlify.toml`, or one `try_files $uri /index.html;` on an own server.

## Tauri or Electron as the desktop shell

**Say this when the shell is chosen** — it decides which OS the design proof covers, not the design itself. Tauri renders through the webview the OS already ships — WebView2 (Chromium) on Windows, WKWebView on macOS, WebKitGTK on Linux — so a canvas proven in Chrome is proven for Windows alone; fonts, form controls, and newer CSS can land differently on macOS and Linux, and each needs its own capture in the Proof profile before the app is called proven there. Electron bundles its own Chromium: identical rendering on every OS, at the cost of a far larger binary. Neither is Ready: the first repo that ships on one writes its distribution path into the rubric.
