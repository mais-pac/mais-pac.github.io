-- MAIS PAC — Supabase setup for mais-pac-members
-- Run this in Supabase Dashboard → SQL Editor → New query → Paste → Run
-- Project: https://gzfristpisxqxtesalkc.supabase.co

-- 1) Create a private table. Only signed-in users can read it (RLS).
create table if not exists public.members (
  id uuid primary key default gen_random_uuid(),
  name text not null,
  role text,
  note text,
  email text,
  created_at timestamp with time zone default now()
);

-- Enable RLS (critical for GitHub Pages security)
alter table public.members enable row level security;

-- Drop old policies if re-running
drop policy if exists "Allow authenticated read" on public.members;
drop policy if exists "Allow owner insert" on public.members;
drop policy if exists "Allow owner update" on public.members;
drop policy if exists "Allow owner delete" on public.members;

-- Only authenticated users can SELECT
create policy "Allow authenticated read"
  on public.members for select
  to authenticated
  using (true);

-- Only authenticated users can INSERT/UPDATE/DELETE
-- Tighten later to owner-only if you add an owner_id column.
-- For strict owner-only (recommended once you know your user id):
-- 1) add column owner_id uuid references auth.users(id)
-- 2) replace policies with: using (auth.uid() = owner_id)

create policy "Allow owner insert"
  on public.members for insert
  to authenticated
  with check (true);

create policy "Allow owner update"
  on public.members for update
  to authenticated
  using (true)
  with check (true);

create policy "Allow owner delete"
  on public.members for delete
  to authenticated
  using (true);

-- 2) Example data (visible only when signed in)
insert into public.members (name, role, note) values
  ('MAIS PAC Founders', 'Club', 'Private welcome — only members see this'),
  ('Example member', 'Student', 'Edit or delete me in Table Editor')
on conflict do nothing;

-- 3) Auth: create your login user manually (do NOT put password in code)
-- Go to: Supabase Dashboard → Authentication → Users → Add user → Create new user
-- - Email: your email
-- - Password: STRONG new password (set in Supabase, never in chat or GitHub)
-- - Auto Confirm User: ON
-- Then log in at https://mais-pac.github.io/members.html (or your Vercel URL)

-- 4) Optional: harden to single owner (uncomment after you create your user)
-- Find your user id: Authentication → Users → copy UID
-- alter table public.members add column if not exists owner_id uuid references auth.users(id);
-- update public.members set owner_id = 'PASTE_YOUR_UID_HERE' where owner_id is null;
-- drop policy if exists "Allow authenticated read" on public.members;
-- create policy "Owner read"
--   on public.members for select to authenticated using (auth.uid() = owner_id);
