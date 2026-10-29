# MAIS PAC — How to use Supabase + GitHub Pages (or Vercel)

You now have a Supabase project: **mais-pac-members** (`https://gzfristpisxqxtesalkc.supabase.co`) — as in your screenshot.
Here’s how to turn it into a safe owner-only login without putting any password in the public repo.

> **Security rule for a public static site (GitHub Pages):**  
> A password check written in HTML/JS is visible to everyone and can be bypassed.  
> Real protection comes from **Supabase Authentication + Row Level Security (RLS)** — the server checks the login, not the page.

## Step 1 — Change the password you shared (do this now)
In Supabase, never reuse a password that was sent in chat or email.
Go to **Authentication → Users → Add user** and set a **new strong password there** — not in GitHub, not in chat.

## Step 2 — Get your publishable key (safe to be in the page)
1. Supabase Dashboard → your project **mais-pac-members**
2. Left sidebar → **Project Settings** (gear icon) → **API**
3. Under **Project API keys** copy **anon** / **public** key (long JWT starting with `eyJ...`)
4. Paste it into `assets/supabase-config.js`:
   ```js
   window.MAIS_PAC_SUPABASE = {
     url: "https://gzfristpisxqxtesalkc.supabase.co",
     anonKey: "PASTE_YOUR_ANON_KEY_HERE" // ← replace this
   };
   ```
   **Never** paste the `service_role` key in the repo — it bypasses all security.

## Step 3 — Enable email sign-in & create your account
1. **Authentication → Providers → Email** → Ensure **Enable Email provider** is ON
   - Disable “Confirm email” for now, or enable it if you want verification emails
2. **Authentication → Users → Add user → Create new user**
   - Email: your email
   - Password: your new strong password (set only here)
   - **Auto Confirm User: ON** → Create
3. Note your UID (you’ll need it for owner-only tightening later)

## Step 4 — Create the private table with RLS
1. Supabase Dashboard → **SQL Editor** → **New query**
2. Paste the full contents of `supabase-setup.sql` (in this repo) → **Run**
3. Verify: **Table Editor → members** → you should see 2 example rows

What RLS does:
- `enable row level security` + policy `to authenticated using (true)` means:
  - **Anonymous visitors (public)** → 0 rows
  - **Signed-in user** → can read rows
  - No password in the HTML can change that

To restrict to **only you** (owner-only):
Uncomment the last 5 lines of `supabase-setup.sql` and set `owner_id` to your UID, then re-run.

## Step 5 — Test the members portal (GitHub Pages)
1. Commit `assets/supabase-config.js` with your anon key and push to `main`
2. Wait ~1 min for GitHub Pages to deploy
3. Visit `https://mais-pac.github.io/members.html`
4. Sign in with the email + password you created in Step 3
5. You should see “Loaded 2 row(s) from Supabase (RLS-protected)”

If you see “Table not found” → you haven’t run `supabase-setup.sql` yet.  
If you see “RLS blocked access” → check the policies in **Authentication → Policies**.

---

## How to use Supabase day-to-day

- **Add members / private notes:** Table Editor → `members` → Insert row
- **Auth:** Authentication → Users (add/remove, reset password)
- **Data API:** Every table is auto-available as REST API, but blocked by RLS unless signed in
- **No backend code needed** for this portal — it’s just `supabase-js` from CDN + RLS

Common tasks:
```sql
-- Add a private announcement
insert into public.members (name, role, note) values ('Meeting 2025-11-10', 'Announcement', 'Lab at 16:00');

-- Make a new private table
create table public.resources_private (id uuid primary key default gen_random_uuid(), title text, url text, created_at timestamptz default now());
alter table public.resources_private enable row level security;
create policy "auth read" on public.resources_private for select to authenticated using (true);
```

---

## Vercel (free) — also works with this repo

You asked about Vercel — yes, you can publish this same GitHub repo there for free, and it’s a good upgrade path.

**Option A: Static only (easiest, same as GitHub Pages)**
1. Go to https://vercel.com/new → Import `mais-pac/mais-pac.github.io`
2. Framework Preset: **Other** → Build Command: empty → Output: `.` → Deploy
3. Same `members.html` + `assets/supabase-config.js` works — RLS still protects data

**Option B: With Environment Variables (recommended for Vercel)**
1. Vercel Dashboard → your project → **Settings → Environment Variables**
2. Add:
   - `VITE_SUPABASE_URL` = `https://gzfristpisxqxtesalkc.supabase.co`
   - `VITE_SUPABASE_ANON_KEY` = your `anon` key
3. Update `assets/supabase-config.js` to read from `import.meta.env` if you later move to Vite/Next.js
   - For now, hardcoding the `anon` key is fine — it’s publishable by design

**When Vercel adds value:**
- You want to protect **file downloads** (not just rows) → use Vercel Functions + `service_role` securely on the server, never in the browser
- You want server-side redirects for private routes → add `middleware.js` with Supabase Auth helpers

**When GitHub Pages is enough:**
- Your private content is rows in Supabase (members, notes, announcements)
- RLS is sufficient — no downloadable private files to protect

---

## Checklist before you publish login

- [ ] New password set in Supabase (not reused from chat)
- [ ] `anon` key pasted in `assets/supabase-config.js`
- [ ] `supabase-setup.sql` run in SQL Editor
- [ ] Test login at `/members.html` succeeds and shows private rows
- [ ] Public pages (`/`, `#about`, etc.) still visible to everyone (by design)

Need help? Send only the **anon key** (not service_role, not password) if you want me to wire it, or paste the UID to tighten to owner-only.
