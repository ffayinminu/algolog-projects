# Pledged (AutoGiving) — Church Recurring Giving Platform

**Status:** Frontend Prototype Complete, Backend Integration In Progress
**Domain:** autogiving.ng
**Repo:** `Pledged`
**Backend:** Extends SkillPay (`anosend` repo)

---

## What It Is

Pledged is a church-branded recurring giving platform. Churches sign up, connect their bank account via Paystack subaccount, and get a custom giving link (autogiving.ng/[church-slug]). Members visit the link, set up their giving (amount + frequency), and it runs automatically. Funds settle directly to the church's bank account — Algolog never touches the money.

**Key design principle:** Lowest possible Time-to-Value (TTV) — signup to first scheduled giving should feel instant.

**Strategic advantage:** Churchgoers can set it up themselves — Algolog doesn't need churches to formally adopt. Individual members can start using it independently (giver-initiated adoption).

---

## Tech Stack (from `Pledged` repo)

- **Frontend:** Next.js 15 + React 18 + ShadCN UI (Radix) + Tailwind CSS + Zustand + TanStack Query + React Hook Form + Zod + Motion + Recharts
- **Backend:** Plugs into SkillPay (not standalone) — adds church module, recurring payment layer
- **Payments:** Paystack (subaccounts for direct settlement, charge_authorization for recurring) + Monnify (alternative)
- **Theming:** Light/dark mode via next-themes
- **Hosting:** Netlify

---

## Frontend Routes (from codebase)

| Route | Purpose |
|-------|---------|
| `/` | Landing page |
| `/[slug]` | Church-branded giving form (e.g., `/grace-revolution`) |
| `/churches/signup` | Church registration wizard (4 steps) |
| `/login` | Member login/signup |
| `/me` | Member dashboard (subscriptions, giving, history) |
| `/admin/login` | Church admin login |
| `/admin` | Church admin dashboard (overview, transactions, members, categories, settings) |
| `/internal` | Algolog internal admin panel (manage all churches) |

---

## User Roles

### Church Admin
- Creates church account, connects bank (Paystack subaccount)
- Sets church name, logo, brand color, giving categories
- Views all transactions, dashboard totals, exports CSV
- Shares the church giving link

### Member (Giver)
- Visits autogiving.ng/[church-slug] — no app download needed
- One-time giving: no account required
- Recurring giving: creates simple account, sets amount + frequency
- Views giving history, pauses/adjusts/cancels subscriptions
- Receives email/SMS receipts

### Algolog Admin (Internal)
- Views all churches on platform
- Monitors transaction health
- Assists onboarding

---

## Recurring Payment Mechanics

- Card tokenization via Paystack `authorization_code` from first charge
- Subsequent charges via `charge_authorization` endpoint
- Weekly: every 7 days from first payment
- Monthly: same day each month
- Failed payment: retry once after 24 hours, then notify member. No further retries.
- Member can pause, adjust amount/frequency, or cancel anytime
- Daily cron job at 6:00 AM WAT processes all due subscriptions

---

## Data Models

- **Church** — name, slug, logo, brand_color, paystack_subaccount_code, bank details, is_active
- **Giving Category** — church_id, name, description, sort_order (e.g., Tithes, Offerings, Building Fund)
- **Member** — name, email, phone, password_hash (platform-wide, can give to multiple churches)
- **Subscription** — member_id, church_id, category_id, amount, frequency, paystack_auth_code, next_charge_date, status
- **Transaction** — church_id, member_id, category_id, subscription_id, amount, type, status, paystack_reference

---

## Revenue Model

Algolog revenue from Paystack subaccount `percentage_charge` (configurable per church). Funds never touch Algolog — direct settlement to church bank.

---

## Distribution

- Active campaign: 181+ churches in Abuja, 84 nationwide
- Email campaign infrastructure built (Google Apps Script)
- Privacy rule: Church client names anonymized in all marketing materials (Church A*, B*, C*)

---

*Based on codebase analysis of `Pledged` repo (CLAUDE.md, projectdoc.md, package.json, app routes) + Product_Context/AutoGiving.md*
