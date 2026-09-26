# Agent account — a Supabase login created by SQL

Read when a session must sign in to an app and holds no account for it, or when the role test needs a user of a role nobody holds. Supabase Auth only; another auth service has no SQL route here — use the repo's own seed script, or ask the user.

**Take the email and password from the session's own instructions; write neither into any repo file, migration, or commit.**

**Run it directly, never as a migration** — Cloud through the Supabase MCP `execute_sql`, self-hosted through `psql` in the database container — because a migration keeps the password in its history. It is a data insert: the destructive gate does not apply, the introspect-after rule does.

1. **Introspect first**: the columns of `auth.users` and `auth.identities`, every trigger on `auth.users`, and whether the email already exists. A trigger that creates the app's profile row decides step 3.
2. **Insert the user and its identity in one statement**, adjusted to what step 1 read:

```sql
with u as (
  insert into auth.users (
    instance_id, id, aud, role, email, encrypted_password, email_confirmed_at,
    raw_app_meta_data, raw_user_meta_data, created_at, updated_at,
    confirmation_token, recovery_token, email_change_token_new, email_change
  ) values (
    '00000000-0000-0000-0000-000000000000', gen_random_uuid(), 'authenticated', 'authenticated',
    '<email>', extensions.crypt('<password>', extensions.gen_salt('bf')), now(),
    '{"provider":"email","providers":["email"]}', '{}', now(), now(),
    '', '', '', ''
  ) returning id, email
)
insert into auth.identities (user_id, provider_id, provider, identity_data, last_sign_in_at, created_at, updated_at)
select id, id::text, 'email', jsonb_build_object('sub', id::text, 'email', email, 'email_verified', true), now(), now(), now()
from u
returning user_id;
```

   Keep the four token columns `''`, never null — Auth fails every sign-in of such a user with `converting NULL to string is unsupported`. Never insert `auth.identities.email`; it is generated.
3. **Give it the role** through the app's own profile or role row, its display name prefixed `[CLAUDE]`. Where a trigger created the row, update that row only.
4. **Prove it**: select both rows back, then sign in once through the app.

The account stays after the session; it is the agent's, reused by every later session. A magic link, OTP, OAuth, SSO, or required MFA has no SQL route — the user creates the account.
