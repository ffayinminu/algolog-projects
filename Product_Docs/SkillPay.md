# SkillPay — Digital Product Marketplace

**Status:** Live & Operational
**Domain:** skillpay.link
**Version:** 5.0.0
**Tagline:** "Get paid for your skills"

---

## What It Is

SkillPay is a digital product marketplace where skilled Nigerians sell what they know. Upload a digital product (template, course, guide, toolkit), get a shareable link, and earn when people buy. Automatic delivery, direct Nigerian bank settlement via Paystack, and conversion-optimized funnel pages for premium products.

**Note:** SkillPay's backend (`anosend` repo) is a shared infrastructure also powering PrivateTransfer, BuyMeAShawarma, BuyMeABeverage, Pledged, and DashMe1k — but each is a separate product with its own brand, domain, and positioning.

---

## Tech Stack (from `anosend` repo)

### Backend (server/)
- **Framework:** NestJS + Express
- **Database:** MySQL 8.0 + TypeORM
- **Language:** TypeScript
- **Auth:** JWT + Passport + Magic Links + 2FA (TOTP)
- **Payments:** Paystack (initialization, verification, transfers, webhooks, subaccounts)
- **Email:** Namecheap SMTP (primary) + Gmail SMTP (fallback)
- **API Docs:** Swagger/OpenAPI
- **Containerization:** Docker & Docker Compose
- **CI/CD:** GitHub Actions (staging, production, release pipelines)

### Frontend (frontend/)
- **Framework:** Next.js 15.2 + React 18.3
- **UI:** Radix UI components + Tailwind CSS
- **State:** Zustand
- **Data Fetching:** TanStack React Query
- **Forms:** React Hook Form + Zod validation
- **Animations:** Framer Motion
- **Hosting:** Vercel

---

## Products Powered by SkillPay Backend

1. **skillpay.link** — Primary platform
2. **buymeshawarma.com** — Food gifting (brand skin)
3. **buymeabeverage.com** — Beverage gifting (brand skin)
4. **autogiving.ng** — Pledged church giving (extends with recurring payments)
5. **DashMe1k** — Creator tipping (in development)

---

## Core Features

### Sell Digital Products
- Upload product URL (Google Drive, Dropbox, any link), set name and price (NGN 100-100,000)
- Generate unique seller slug and shareable product link (skillpay.link/u/[slug])
- Automatic delivery: buyer pays → receives product URL via email
- "More from this seller" feature shows other products by same seller
- Buyer rating system (1-5 stars)
- Fee: 3% + NGN 200 (max NGN 4,000) deducted from seller

### Create Payment Links
- Create shareable links to receive payments without exposing bank details
- Customizable link title and purpose
- Fee: 3% + NGN 200 (max NGN 4,000) deducted from received amount

### Transaction Tracking
- Search by transaction reference and email
- View current status and processing stage
- Track transfer progress in real-time

---

## Funnel Feature (Conversion-Optimized Sales Pages)

Sellers can toggle between standard product page and a full funnel display mode:

**Funnel Structure:**
Hook (headline + subheadline) → Problem (intro + 2-4 pain points) → Solution (transformation) → Benefits (3-6 items) → Price + CTA

**Data Model:** `display_mode` (standard | funnel) + `funnel_content` JSON on `public_link` table

**Sprint Roadmap:**
- Sprint 1: Product mockup image, testimonials (1-3), FAQ (2-4)
- Sprint 2: Hero image, seller photo, bonus stack (1-5 items)
- Sprint 3: Video embed, social proof stats

---

## Backend Modules (from server/src/)

| Module | Purpose |
|--------|---------|
| `auth` | JWT authentication, magic links, 2FA |
| `transactions` | Core transaction processing |
| `payment` | Paystack integration (init, verify, transfer, webhooks) |
| `public-links` | Payment link and product link management |
| `recipients` | Recipient bank account management |
| `banks` | Bank list and validation |
| `fraud` | Real-time fraud detection engine |
| `admin` | Admin dashboard, approvals, refunds |
| `support` | Support ticket system |
| `notifications` | Email/SMS notifications |
| `mailer` | Email service (Namecheap + Gmail SMTP) |
| `brand` | Multi-brand/tenant configuration |
| `church` | Pledged/AutoGiving church module |
| `org` | Organization management |
| `cron` | Scheduled jobs |
| `health` | Health check endpoints |

---

## Frontend Routes (from frontend/app/)

| Route | Purpose |
|-------|---------|
| `/` | Homepage |
| `/u/[slug]` | Public product/payment link page |
| `/send` | Gift Privately flow |
| `/create-link` | Create payment link |
| `/track` | Transaction tracking |
| `/rate` | Rate a purchased product |
| `/manage` | Manage your links/products |
| `/payment` | Payment processing |
| `/admin` | Admin dashboard |
| `/about` | About page |
| `/faq` | FAQ |
| `/contact` | Contact |
| `/privacy` | Privacy policy |
| `/terms` | Terms of service |

---

## Security & Admin

- Real-time fraud detection engine (IP velocity, amount analysis, suspicious content, recipient frequency)
- IP blocking/whitelisting with expiration
- Admin dashboard: transaction approvals, refunds, manual transfers
- Role-based admin access (SUPER_ADMIN, ADMIN, VIEWER)
- Complete audit logging of all admin actions
- Rate limiting: 100 requests per 60 seconds

## Database Entities
Transaction, PublicLink, ProductRating, AdminUser, MagicLink, AuthLog, AdminAction, Recipient, Bank, FraudCheck, BlockedIP, SupportRequest, Notification, TransferLog

---

*Based on codebase analysis of `anosend` repo + docs/about.md + docs/feature-funnels/ + Product_Context/SkillPay.md*
