# Court 474 Ltd — Solution Brief
## Court474 — AI-Powered Short-Let Property Management & Guest Distribution System

---

## 1. THE BUSINESS

Court 474 Ltd operates a short-let (Airbnb-style) property consisting of:
- **25 x 1-bedroom apartments** (owned by different subscribers/property owners)
- **4 x 2-bedroom apartments** (owned by different subscribers/property owners)
- **1 x 40-seater conference room** (meetings, seminars, retreats, trainings)

Court 474 manages the facility on behalf of the individual apartment owners. There are two layers of service:

**Layer 1 — General Facility Management (all units):**
- Security, water supply, cleaning of external premises and common areas
- Charged at a pre-agreed fixed service charge to all apartment owners

**Layer 2 — Individual Apartment Management (opt-in):**
- Short-letting, guest management, cleaning of individual apartments
- Charged at an agreed fee per apartment
- This is the revenue-generating layer where technology has the most impact

---

## 2. THE PROBLEMS TO SOLVE

### A. Fair Guest Distribution
With 29 apartments owned by different people, how do you ensure bookings are distributed evenly? Without a system:
- Some apartments get overbooked while others sit empty
- Owners complain about unequal treatment
- Manual allocation is time-consuming and biased (consciously or not)
- No transparency for owners to verify fair distribution

### B. Revenue Splitting
Each booking generates revenue that needs to be split between:
- The apartment owner (their share)
- Court 474 (management fee)
- This needs to happen automatically, transparently, and with full audit trail

### C. Operations Cost
Running 29 apartments + a conference room with traditional staffing is expensive:
- Receptionist/front desk for check-in/out
- Manual booking tracking (WhatsApp, spreadsheets, calls)
- Manual cleaning scheduling
- Manual procurement tracking
- Manual invoicing and payment reconciliation

### D. Conference Room Management
The 40-seater conference room is a separate revenue stream that needs:
- Its own booking system (hourly/daily)
- Availability calendar visible to potential clients
- Payment processing
- No conflicts with other bookings

---

## 3. THE SOLUTION

### Court474 — Custom-Built Platform

A purpose-built platform for Court 474's multi-owner short-let model. It manages the entire operation: bookings, AI guest distribution, owner settlements, conference room, and facility operations — all from one system.

---

### Module 1: AI Guest Queuing & Distribution Engine

**How it works:**

The system maintains a **fairness score** for each apartment. When a new booking request comes in, the AI engine allocates it based on:

1. **Occupancy balance** — Which apartments have had the fewest bookings this period? Those get priority.
2. **Revenue balance** — Which owners have earned the least? The system balances revenue, not just bookings (since 2-beds earn more than 1-beds).
3. **Apartment type match** — Guest requests a 1-bed → only 1-bed apartments are considered. Guest requests a 2-bed → only 2-bed apartments.
4. **Availability** — Only apartments that are actually available for the requested dates.
5. **Cleaning status** — Only apartments that are cleaned and ready.
6. **Owner preferences** — Some owners may block certain dates (personal use, maintenance).

**The result:** Every owner gets a fair share of bookings. The system can show each owner exactly how many bookings they've received vs. the average, and why a particular apartment was chosen for a particular guest.

**Distribution modes:**
- **Round-robin** — Strict rotation (Apartment 1, then 2, then 3...)
- **Weighted fair share** — Balances by revenue earned, not just count
- **Priority override** — Admin can manually assign a specific apartment when needed (with audit log)

---

### Module 2: Owner Dashboard & Revenue Distribution

Each property owner gets a portal showing:

- **Live occupancy status** of their apartment(s)
- **Booking history** — who stayed, when, how long, how much
- **Revenue earned** — gross booking amount, Court 474 management fee deducted, net owner earnings
- **Automatic settlement reports** — weekly/monthly statements
- **Fairness transparency** — their booking count vs. property average, revenue vs. average
- **Calendar blocking** — owners can block dates for personal use
- **Maintenance requests** — flag issues in their apartment

**Revenue split flow:**
1. Guest pays for booking → money lands in Court 474 account
2. System calculates: Gross amount → Management fee (%) → Owner net
3. Settlement report generated automatically
4. Court 474 disburses to owner on agreed schedule (weekly/monthly)
5. Full audit trail — every naira accounted for

---

### Module 3: Guest Booking & Management

**For guests:**
- Online booking portal — browse available apartments, see photos, select dates, pay online
- Instant booking confirmation via email/SMS
- Smart lock access code — generated automatically, sent to guest, expires at checkout
- QR check-in — scan on arrival, validated against active booking
- No front desk needed for standard check-ins

**For Court 474 staff:**
- Dashboard showing all active bookings, upcoming arrivals, departures
- Guest communication tools
- Issue/complaint tracking
- Automated reminders (checkout time, extension offers)

---

### Module 4: Conference Room Booking System

- Separate booking flow for the 40-seater conference room
- Hourly and daily booking options
- Online calendar showing availability in real time
- Payment processing (Paystack)
- Add-ons: projector, catering, breakout rooms (if available)
- Automated confirmation and access instructions
- Can be marketed separately from the apartments

---

### Module 5: AI Operations Manager

**Cleaning automation:**
- When a guest checks out → system automatically flags the apartment for cleaning
- Assigns cleaning staff based on availability and proximity
- Cleaning staff marks apartment as "ready" in the app
- Apartment only becomes bookable again once marked ready
- Track cleaning time, frequency, and cost per apartment

**Procurement:**
- Track consumables per apartment (toiletries, linens, cleaning supplies)
- Auto-generate restock alerts when inventory drops below threshold
- Monthly procurement reports — cost per apartment, cost trends
- Reduce waste by tracking actual usage vs. purchase

**Staff optimization:**
- AI suggests optimal staffing levels based on occupancy patterns
- Low occupancy week? Reduce cleaning staff schedule
- High occupancy weekend? Alert for additional support
- Track staff performance (cleaning time, guest ratings)

**Cost analytics:**
- Utility costs per apartment (electricity, water — if metered)
- Maintenance cost tracking per unit
- Revenue vs. cost per apartment — which units are most/least profitable
- Monthly P&L per apartment and for the facility overall

---

### Module 6: Facility Management Dashboard

**For Court 474 management:**
- Bird's eye view of the entire property — 29 apartments + conference room
- Real-time occupancy map (visual grid: occupied, available, cleaning, blocked)
- Financial overview — total revenue, management fees earned, pending settlements
- Maintenance tracker — open issues, resolved issues, cost
- Security log integration (if applicable)
- Service charge tracking — which owners have paid, who's overdue

---

## 4. TECHNICAL APPROACH

| Component | Technology |
|-----------|------------|
| Frontend | Next.js + React |
| Backend | Node.js (NestJS) |
| Database | PostgreSQL |
| AI Engine | Custom allocation algorithm (fairness scoring, occupancy balancing) |
| Payments | Paystack (guest payments, owner settlements) |
| Smart Access | IoT smart locks (auto-generated codes, auto-expiry) |
| Cloud | Microsoft Azure |
| Infrastructure | Terraform |
| Notifications | Email + SMS (booking confirmations, owner reports, staff alerts) |
| Security | OWASP standard, role-based access control |

**Algolog's experience:**
Algolog has built and deployed property management systems for hospitality businesses across Nigeria — handling bookings, payments, smart lock automation, and operational dashboards. Court474 is a custom build designed specifically for the multi-owner short-let model, with AI-powered guest distribution as its core differentiator.

---

## 5. WHAT COURT 474 GETS

| Without the system | With the system |
|---|---|
| Manual guest allocation (WhatsApp, calls, gut feel) | AI distributes guests fairly across all apartments automatically |
| Owners don't know if they're getting fair share | Every owner sees their stats vs. average in real time |
| Revenue splitting done manually in Excel | Automatic calculation, settlement reports, audit trail |
| Front desk needed for every check-in | Smart lock codes sent to guests automatically |
| Cleaning scheduled via phone calls | Auto-triggered cleaning workflow on checkout |
| No visibility into costs per apartment | Full P&L per apartment, per month |
| Conference room booked via calls/WhatsApp | Online booking with real-time availability and payment |
| Procurement tracked manually or not at all | Auto restock alerts, usage tracking, cost reports |
| High staff costs | AI suggests optimal staffing based on occupancy |

---

## 6. SUMMARY

Court 474's multi-owner model creates a unique challenge: **fairness**. Every owner needs to trust that their apartment is getting its fair share of bookings and revenue. At the same time, Court 474 needs to run operations as lean as possible.

This solution uses AI to solve both problems simultaneously — fair distribution builds owner trust and retention, while automation reduces the staff and manual effort needed to manage 29 apartments and a conference room.

The platform is purpose-built for Court 474's multi-owner model, developed by Algolog — a team with proven experience building and deploying property management systems in the Nigerian market.
