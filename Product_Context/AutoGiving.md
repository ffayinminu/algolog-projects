# Pledged (formerly AutoGiving) - Church Recurring Giving Platform

## Overview
Pledged is a church-branded recurring giving platform powered by the **SkillPay backend**. A church signs up, connects their bank account via Paystack subaccount, gets a custom link at `autogiving.ng/[church-slug]`. Members visit that link, set up their giving (amount + frequency), and it runs automatically. Funds go straight to the church's bank account.

**This is NOT a standalone backend.** Pledged plugs into the existing SkillPay backend that already serves skillpay.link, buymeshawarma.com, and buymeabeverage.com. SkillPay handles payment processing, user accounts, and transaction tracking. Pledged adds a new frontend skin + a recurring payment layer on top.

## Domain
**autogiving.ng**

## Key Design Principle
**Lowest possible TTV (Time to Value)** — Signup to first scheduled giving should feel instant. As few clicks as possible.

## Strategic Advantage
Churchgoers set it up themselves — Algolog doesn't need churches to formally adopt. Individual members can start using it independently (giver-initiated adoption).

---

## User Roles

### Church Admin
- Creates church account
- Connects bank account (via Paystack subaccount for direct settlement)
- Sets church name, logo, brand color
- Defines giving categories (Tithes, Offerings, Building Fund, Missions, etc.)
- Views all transactions, dashboard totals, exports CSV
- Shares the church giving link

### Member (Giver)
- Visits `autogiving.ng/[church-slug]` — no app download needed
- One-time giving: no account required (just name, email, amount, pay)
- Recurring giving: creates simple account (email + phone + name)
- Sets amount and frequency (one-time, weekly, monthly)
- Views giving history, pauses/adjusts/cancels subscriptions
- Receives email/SMS receipts

### Algolog Admin (Internal)
- Views all churches on platform
- Monitors transaction health
- Assists onboarding

---

## Core Flows

### Church Onboarding
1. Church admin visits autogiving.ng/churches/signup
2. Enters church name, location, email, phone, bank details
3. System creates Paystack subaccount (funds settle directly to church)
4. Sets logo, brand color, giving categories
5. System generates giving link: `autogiving.ng/[church-slug]`

### One-Time Giving
Member visits link → selects category → enters amount → selects "One-Time" → enters name/email/phone → Paystack popup → payment processed → receipt sent → logged in church dashboard.

### Recurring Giving (Core Feature)
Member visits link → selects category → enters amount → selects frequency → creates/logs into account → Paystack popup (first charge + card tokenization) → card token stored → system schedules recurring charges → confirmation sent.

**Recurring mechanics:**
- Card tokenization via Paystack `authorization_code` from first charge
- Subsequent charges via `charge_authorization` endpoint
- Weekly: every 7 days from first payment
- Monthly: same day each month
- Failed payment: retry once after 24h, if fails again notify member, do NOT retry further
- Member can pause, adjust amount/frequency, or cancel at any time

---

## Data Models

### Church
id (UUID), name, slug, location, logo_url, brand_color (#1E3A5F default), admin_name, admin_email, admin_phone, paystack_subaccount_code, bank_name, account_number, is_active, created_at

### Giving Category
id (UUID), church_id (FK), name, description, is_active, sort_order, created_at

### Member
id (UUID), name, email (unique), phone, password_hash, created_at
*Note: A member can give to multiple churches. Account is platform-wide.*

### Subscription (Recurring Giving)
id (UUID), member_id (FK), church_id (FK), category_id (FK), amount (in kobo), frequency (weekly/monthly), paystack_auth_code, next_charge_date, status (active/paused/cancelled), created_at, paused_at, cancelled_at

### Transaction
id (UUID), church_id (FK), member_id (FK, nullable for anonymous), category_id (FK), subscription_id (FK, nullable for one-time), amount (in kobo), type (one_time/recurring), status (success/failed/pending), paystack_reference, giver_name, giver_email, giver_phone, created_at

---

## API Endpoints

### Public (No Auth)
- `GET /churches/:slug` — Church info + categories for giving page
- `POST /churches/:slug/give` — Process one-time giving
- `POST /auth/member/register` — Member signup
- `POST /auth/member/login` — Member login

### Member (Auth Required)
- `GET /me` — Member profile
- `GET /me/subscriptions` — List active subscriptions
- `POST /me/subscriptions` — Create new recurring subscription
- `PATCH /me/subscriptions/:id` — Update amount/frequency
- `POST /me/subscriptions/:id/pause` — Pause
- `POST /me/subscriptions/:id/resume` — Resume
- `POST /me/subscriptions/:id/cancel` — Cancel
- `GET /me/transactions` — Giving history

### Church Admin (Auth Required)
- `POST /auth/church/register` — Church signup
- `POST /auth/church/login` — Church admin login
- `GET /admin/dashboard` — Dashboard stats
- `GET /admin/transactions` — All transactions (filterable, paginated)
- `GET /admin/transactions/export` — CSV export
- `GET /admin/members` — All members who have given
- `GET/POST/PATCH/DELETE /admin/categories` — Category CRUD
- `PATCH /admin/settings` — Update church profile/bank/link

### Internal / Cron
- `POST /internal/process-recurring` — Daily cron: charge all subscriptions due today
- `POST /internal/retry-failed` — Retry failed charges (once, after 24h)

---

## Paystack Integration

### Subaccount Creation (Church Onboarding)
```
POST https://api.paystack.co/subaccount
{ "business_name": "Church Name", "bank_code": "058", "account_number": "0123456789", "percentage_charge": 0.5 }
```
Returns `subaccount_code` — stored on Church record. Paystack splits funds automatically.

### One-Time Giving
Standard `POST /transaction/initialize` with church's `subaccount` code.

### Recurring Giving
First payment captures `authorization_code`. Subsequent charges via:
```
POST https://api.paystack.co/transaction/charge_authorization
{ "authorization_code": "AUTH_xxxxx", "email": "...", "amount": 1000000, "subaccount": "ACCT_xxxxx" }
```

### Webhook Events
- `charge.success` → Log transaction, send receipt, update next_charge_date
- `charge.failed` → Log failure, schedule 24h retry, notify member

---

## Recurring Charge Cron Job
Runs daily at 6:00 AM WAT:
1. Query active subscriptions where next_charge_date <= today
2. Charge via Paystack charge_authorization
3. On success: log transaction, update next_charge_date (+7 days or +1 month), send receipt
4. On failure: log, set retry flag, notify member
5. Retry job (24h later): retry once. If fails again, notify and stop.

---

## Notifications
| Event | Channel | Recipient |
|-------|---------|-----------|
| Successful payment | Email + SMS | Member |
| Failed payment | Email + SMS | Member |
| New recurring subscriber | Email | Church Admin |
| Subscription cancelled | Email | Church Admin |
| Weekly summary | Email | Church Admin |

---

## Revenue Model
Algolog revenue from Paystack subaccount split. `percentage_charge` on subaccount = Algolog's take.
Example: 1.0% → on ₦10,000 giving, Paystack takes ~1.5%, Algolog takes 1%, church gets the rest.
Configurable per church.

---

## Business Rules
1. Funds never touch Algolog — direct to church via Paystack subaccount
2. No minimum giving amount
3. Member can give to multiple churches (platform-wide account)
4. Church can have multiple categories (minimum 1, default: "General Giving")
5. Recurring giving can be paused, adjusted, or cancelled anytime — no lock-in
6. One-time giving: no account required. Recurring giving: account required.
7. Failed recurring: retry once after 24h, then stop
8. Church admin cannot see member card details
9. All amounts stored in kobo (₦1 = 100 kobo)

---

## What to Reuse from SkillPay Backend
| Component | Reuse |
|-----------|-------|
| Paystack integration layer | Add subaccount + charge_authorization |
| User/auth system | Extend for church admin + member roles |
| Transaction model | Extend with type, subscription_id, category_id |
| Email service | Same transactional emails for receipts |
| Database | Same DB, new tables for churches, categories, subscriptions |
| Deployment | Same hosting, same CI/CD |

## New Code Needed
- Church model + API, Giving Category model + API, Subscription model + recurring logic
- Recurring charge cron job
- Church giving page (frontend), Member dashboard, Church admin dashboard

---

## Tech Stack (Frontend)
Next.js, ShadCN UI, next-themes, Zustand, React Query, React Toastify, Axios, Recharts, React Hook Form, Motion

## Payment Integrations
- **Paystack** — Primary (subaccounts for direct church settlement, charge_authorization for recurring)
- **Monnify** — Alternative (subaccount feature, Merchant Code: N49HJWD7N2FE)

## Active Campaigns
- Church proposal campaign (181+ churches targeted in Abuja)
- Nationwide church proposals (84 churches)

## FRD Reference
Full FRD: `claude.ai contex/AutoGiving-FRD-Prototype.md` (Document ID: FRD-AUTOGIVE-001)

## Lead Generation (Hormozi $100M Leads Framework)

### Lead Magnet Files (Created March 2, 2026)
**Markdown guides** (in `claude.ai contex/`):
- `Lead-Magnet-Pledged-Cash-Transparency.md` — "Where Did the Offering Go?" — 5 cash handling vulnerability points, cost calculations
- `Lead-Magnet-Pledged-Predictable-Church.md` — "What if you knew exactly how much was coming in next month?" — 3 income types, ideal mix (50-60% recurring)
- `Lead-Magnet-Pledged-Holiday-Offering.md` — "Why Your Offering Drops Every Holiday" — 12 reduced Sundays × 30% drop = NGN 3.6M/year loss

**PDF generators** (project root):
- `generate_pledged_lead_magnet_1.py` → `generate_pledged_lead_magnet_3.py`

**Finished PDFs** (in `Proposals/`):
- `Lead-Magnet-Pledged-Cash-Transparency.pdf`
- `Lead-Magnet-Pledged-Holiday-Offering.pdf`
- `Lead-Magnet-Pledged-Predictable-Church.pdf`

### Hormozi Structure (all magnets follow)
Hook → Problem revelation → Cost calculation (NGN) → Free fix (give away the secret) → Automated fix (Pledged/autogiving.ng) → CTA (free 15-min audit with Yasmin Umar, limited to 10/month)

### Target
Church finance teams and leadership — distributed via social media gated content, DM outreach, and content marketing.

---

## Status
In active development — SkillPay backend extension, frontend design completed, payment integration being set up.

---
*Last updated: 2026-03-03*
