# Spacer — Complete Value Stack (Platform + Service Extensions + Partner Ecosystem)

**Purpose:** Comprehensive value-proposition reference covering the Spacer platform itself, the managed services being layered on top, the partner ecosystem powering them, bonus content assets, and the commercial structure that ties it all together. Used for proposals, closes, and internal alignment.

**Status:** Core platform items are **LIVE**. Service-extension items are **IN DESIGN** — pricing and structural decisions still open (see Part 8).

**Companion doc:** `Proposals/Spacer-Value-Stack.md` (the original 10-module platform value stack, anchored to the codebase).

---

## Part 1 — The Core Spacer Platform (LIVE)

The base of every Spacer deployment. Each module is shipping in the production codebase and powering live revenue at Saadatu's Apartment (Kaduna), Alegre Farms (Bwari, Abuja), DuloWork (Lagos), and Qas Luxury Apartments (Abuja).

| # | Module | What the Client Receives | Build-Equivalent Value (₦) |
|---|---|---|---:|
| 1 | Multi-Tenant Platform Core | Branded URL, JWT auth, RBAC, audit logging, real-time WebSocket | 8,000,000 |
| 2 | Multi-Tier Booking Engine | Hourly through annual tiers, conflict prevention, calendar integration | 7,000,000 |
| 3 | Payment Infrastructure | Paystack card + transfer, auto invoices/receipts, refunds, abandonment recovery | 6,000,000 |
| 4 | Smart Lock Automation | Tuya cloud-synced online codes, auto-expiry, QR check-in | 5,000,000 |
| 5 | Auto-Generated Marketing Website | Branded hero, gallery, 360° tour, mobile-first | 4,500,000 |
| 6 | Management Dashboard & Intelligence | Real-time occupancy, revenue analytics, exports | 5,500,000 |
| 7 | Operations & Staff Management | Role scoping, audit trail, multi-location support | 4,000,000 |
| 8 | Automated Notifications | Booking, renewal, receipt, abandonment recovery emails | 3,000,000 |
| 9 | Cloud Infrastructure & Hosting (Year 1) | Azure Storage, Netlify, SSL, backups, monitoring | 2,500,000 |
| 10 | Onboarding, Training & 12-Month Support | Deployment, staff training, continuous support | 2,500,000 |
| | **SUBTOTAL — PLATFORM VALUE** | | **₦48,000,000** |

**Live Investment Anchor:** ₦3,000,000 (hospitality) / ₦2,000,000 (apartments) — one-off.

**Ratio:** 16× to 24× value delivered against price paid, before any service extensions are layered on.

(Full per-module breakdown including module-level capability lists is in `Proposals/Spacer-Value-Stack.md`.)

---

## Part 2 — Managed Service Extensions (IN DESIGN)

These convert Spacer from a tool into a managed operating layer. Algolog runs them on the operator's behalf, with Spacer as the workflow backbone — so every job, schedule, review, and incident is captured inside the same dashboard the operator already uses.

### 2.1 Cleaning & Kitchen Staff Service

**What it is:** Fully managed cleaning rotations and kitchen staffing supplied by vetted partner crews, scheduled directly through Spacer's calendar.

**What's included:**
- Vetted partner agencies under contract
- Schedules synced to the booking calendar — no clean, no check-in code released
- SLA-backed turnaround times
- Performance tracking inside the operator dashboard
- Replacement cover within a defined window on no-shows

**Why it matters:**
- Operator: zero hiring overhead, no payroll, no recruitment, no quality drift
- Guest: consistent room and meal experience every stay

**Replaces:** In-house housekeeping coordinator (typical Nigerian cost ₦80K–₦200K/month) and ad-hoc catering bookings.

---

### 2.2 Media Automation for Social Media

**What it is:** Automated capture, scheduling and posting of property content across Instagram, Facebook, TikTok and Google Business Profile.

**What's included:**
- Auto-scheduled posts tied to bookings, reviews and events
- Branded post templates pre-loaded
- Monthly content calendars
- Review-to-post conversion — five-star guest reviews auto-become social proof posts
- Optional paid-ad spend management layer

**Why it matters:**
- Operator: replaces the need for an in-house social media manager (typical Nigerian cost ₦150K–₦400K/month)
- Guest: discovers the property in the first place — higher top-of-funnel reach

**Replaces:** Social media manager + content creator + scheduling tool subscription.

---

### 2.3 Guest Review Service

**What it is:** Managed review request, follow-up, and reputation workflow across Google, Booking.com, Airbnb, and direct booking channels.

**What's included:**
- Auto-trigger review requests after checkout
- Negative-review interception — private complaint flow surfaces the issue *before* it goes public
- Monthly reputation scorecard
- Response templates and managed replies
- Star-rating recovery playbook on dips

**Why it matters:**
- Operator: higher star ratings drive ADR uplift directly — every 0.5-star improvement is measurable revenue
- Guest: bad experiences get resolved, voice is heard

**Replaces:** Reputation manager + manual review chasing + crisis response.

---

### 2.4 Executive Hostess Service

**What it is:** Concierge-level guest welcome and on-property experience, delivered by trained hostesses available on call or on rotation.

**What's included:**
- Greeting, key handover assistance, property orientation
- Day-of guest support
- Local recommendations and bookings
- Premium experience signalling for luxury units

**Why it matters:**
- Operator: premium positioning without a permanent hire — used selectively for high-value bookings
- Guest: a real human presence in what's otherwise a self-service flow

**Replaces:** Full-time front-desk staff for properties that don't have the volume to justify one.

---

## Part 3 — Partner Ecosystem (IN DESIGN)

Algolog assembles and governs a vetted partner network so the operator never has to manage humans they don't directly employ.

### 3.1 Partner Categories

- Cleaning agencies
- Catering / kitchen staffing
- Maintenance and repairs (plumbing, electrical, AC, smart-lock service)
- Laundry
- Logistics / airport pickup
- Photographers and content crews (feeding the media service)

### 3.2 Partner Governance Layer

- Vetting and onboarding handled by Algolog
- SLAs and pricing pre-negotiated
- Jobs routed through Spacer (ticketed, not WhatsApp-based)
- Performance ratings tracked across every job
- Defaulting partners replaced without operator involvement

### 3.3 Executive Assistant (EA) Layer

An EA function — internal to Algolog — owns the operational choreography of the partner network for each operator:
- Maps the operator's partner stack at onboarding
- Coordinates routing rules per property
- Handles escalations as they emerge
- Acts as the operator's single point of contact

### 3.4 Lawyer-At-Call Layer

A retained legal touchpoint handles partner default cases:
- Demand letters
- Contract enforcement
- Settlement coordination
- Operator never has to chase a defaulting partner directly

---

## Part 4 — Bonus Features

### 4.1 360° Panoramic Virtual Tours

- Already shipping in the codebase (Panolens + Three.js)
- Positioned as a **bonus on close** when the prospect's pain is premium positioning, luxury units, or remote bookers
- Deliberately *not* commoditised by including it in every demo — kept as a deal lever

### 4.2 Operator Ebook Library

Operational playbooks delivered as part of Tier 1 onboarding:
- How to price an apartment in Abuja / Lagos / Kaduna
- Direct-booking conversion playbook
- Reducing no-shows and chargebacks
- Smart-lock incident response
- Tax and statutory compliance for short-let operators
- Staff hiring, performance management, and termination scripts

### 4.3 Webinars (Physical and Virtual)

Monthly profit-maximisation and risk-reduction sessions:
- Topics rotate across pricing, occupancy, marketing, operations, compliance
- Physical sessions in Abuja and Lagos
- Virtual sessions for nationwide reach
- Open to all paying Spacer clients across both tiers

---

## Part 5 — Commercial Structure

### 5.1 Tier Layout

**Tier 1 — Platform Essentials (LIVE)**
- Full Spacer platform (all 10 live modules)
- Operator ebook library
- Webinar access
- 12 months of technical support
- Investment: ₦3M hospitality / ₦2M apartments

**Tier 2 — Platform + Managed Services (IN DESIGN)**
- Everything in Tier 1
- Cleaning + Kitchen Staff Service
- Media Automation
- Guest Review Service
- Executive Hostess access
- Partner ecosystem routing
- EA + Lawyer-at-call coverage
- Investment: **TBD** *(see Part 8)*

### 5.2 Free Trial Pathways

Operators can take a no-payment runway up front:
- **30 days** — fastest commitment
- **3 months** — soft trial
- **6 months** — extended trial *(no deposit discount applies)*

Operator can cancel at any point during trial without penalty.

### 5.3 Pay-Deposit-On-Call Discount

- Operators who commit deposit during the sales call receive a discount.
- Operators who route through the 6-month free trial forfeit the discount.
- Trade: certainty for cash.

### 5.4 5% to Charity Commitment

- 5% of every deployment fee — and a defined portion of Tier 2 ongoing revenue — is committed to charity.
- Specific charity selection, audit method, and accounting treatment are still open design items (see Part 8).

---

## Part 6 — Outcomes & Guarantees

### Tier 1 Guarantees (LIVE)

- Go-live in 7–10 days
- 12 months of technical support included
- Continuous platform improvements at no recharge
- Nigerian support team — local response, no offshore delays

### Tier 2 Guarantees (IN DESIGN)

- All Tier 1 guarantees
- Cleaning SLA: cover within a defined window of any no-show
- Reputation guarantee: managed response to every review within a defined window
- Partner default coverage: legal touchpoint absorbed by Algolog
- 5% of fees committed to charity, reported quarterly

### Ongoing Business Outcomes (Compound Over Time)

These are not line items in the value table — they compound beyond it:

- **OTA commission elimination** — direct bookings replace 15% Airbnb / Booking.com fees. A property doing ₦20M/year saves ₦3M/year, every year.
- **Premium positioning uplift** — branded website and smooth booking flow drive 20–35% higher ADR.
- **Eliminated key handover labour** — smart codes remove the cost and risk of physical key management.
- **Reduced no-shows** — payment-first booking model removes ghost reservations entirely.
- **Cart abandonment recovery** — recovered bookings typically equal 10–30% of incomplete attempts.
- **Hire cost displacement (Tier 2)** — managed services replace housekeeping coordinators, social media managers, and front-desk staff, which is typically the single biggest hidden cost in short-let operations.

---

## Part 7 — Why This Defeats the Price Objection

When a prospect challenges price:

- **Tier 1 alone delivers ₦48M of build-equivalent value for ₦2M–₦3M.**
- The booking engine alone costs more to build than the entire deployment fee.
- The auto-generated marketing website alone is worth most of the fee.
- The smart lock automation alone justifies the fee for any apartment doing more than a few bookings a month.
- Every other module is bonus value.

When a prospect challenges Tier 2 price:

- The cleaning service alone replaces a hire that costs more per month than Tier 1's full one-off fee.
- The media service replaces a hire that costs ₦150K–₦400K/month.
- The partner ecosystem removes the operator's biggest hidden cost: managing humans they don't directly employ.
- The legal touchpoint alone is value that operators never even price.

**Spacer is not priced against what it cost to build. It is priced against what it costs the operator NOT to have it.**

---

## Part 8 — Open Design Questions (Internal)

These need decisions before Tier 2 can be quoted, contracted, or sold externally. This section is the single source of truth for what's still open.

1. **Free-trial-vs-fee tension** — does the 30/90/180-day free trial replace the ₦3M up-front model, or run alongside it as a separate optional path?
2. **Partner revenue cut** — what % of partner job value does Algolog take? Fixed retainer, per-job markup, or revenue share?
3. **Charity 5% source** — comes out of Algolog's margin, off the top of operator fees, or off Tier 2 monthly revenue only?
4. **Tier 2 price** — fixed monthly retainer per property? Per-room? Bundled into a higher one-off?
5. **EA & lawyer cost structure** — internal Algolog hires absorbed into Tier 2 fee, or rate-card pass-through to the operator?
6. **Panoramic positioning** — bonus on close-deal, or always-on feature in the demo?

Each resolved decision should update this document in place.

---

*Living document. Tier 2 specifications will firm up as the open design questions are resolved. Last structural update: this version.*
