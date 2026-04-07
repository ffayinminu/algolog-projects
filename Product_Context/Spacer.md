# Spacer - Workspace & Hospitality Management Platform

## Overview
Spacer is Algolog's flagship product — a smart management platform for coworking spaces, shared offices, serviced apartments, and hospitality businesses. It automates bookings, payments, access control, and operational management.

## Core Features
- **Multi-tier Booking Engine** — Supports hourly, daily, weekly, monthly, quarterly, bi-annual, and annual memberships
- **Centralized Reservations** — All bookings managed from one dashboard (replaces scattered WhatsApp, calls, notes)
- **Payment Automation** — Integrated with Paystack (1.5% capped at NGN 2,000); supports card, transfer, and walk-in payments
- **Admin Dashboard** — Real-time occupancy, availability, and financial reporting
- **Customer Portal** — Progress tracking, invoices, personalized reminders (email/WhatsApp)
- **QR Check-In** — Customers scan to check in, validated against active bookings
- **Smart Lock Automation** — Generates unique access codes via Tuya/SmartLife API; codes sent to guests and auto-expire at checkout
- **Invoice Generation** — Automatic invoicing for all booking types
- **Conflict Management** — Prevents double-bookings with admin override toggle
- **Automated Renewals & Notifications** — Renewal reminders for all subscription types
- **Staff Role Management** — Role-based access for receptionist, manager, cashier, etc.

## New Features (In Development)
1. **Unified Gallery View** — Multiple identical units displayed as a single listing
2. **Virtual Spaces** — Subspace packages (e.g., 1BR/2BR under 3BR parent) with inherited metadata
3. **Admin Approval Workflow** — Manager approval required for virtual space bookings
4. **Conflict Prevention** — Automatic double-booking prevention between parent/child spaces

## Payment Flow (Walk-in Bookings)
1. Receptionist creates booking from walk-in account
2. Goes to Invoices & Receipts -> Pay Now
3. Options: Pay by Card OR Pay by Transfer
4. Transfer generates temporary account (valid 30 minutes)
5. Payment confirmation auto-locks booking

## Smart Lock Flow
1. Receptionist clicks "Check-In" on dashboard
2. System generates unique access code via SmartLife API
3. Code sent to guest via WhatsApp/SMS
4. Code expires automatically at checkout

## Target Markets
- Coworking spaces
- Serviced apartments
- Hotels & hospitality
- Event venues
- Shared offices

## Active Deployments
1. **Saadatu's Apartment (Kaduna)** — Deployed; HMIS with smart lock automation, staff trained. Price: NGN 2,000,000
2. **Alegre Farms (Bwari)** — Resort booking platform. Price: NGN 3,000,000
3. **KA_WI Limited (Abuja)** — Proposal sent; real estate with apartment buildings. Price: NGN 2,000,000/property
4. **Yanna Apartments by Khaliques (Abuja)** — In progress; migrating from Yanolja Cloud

## Value Proposition
Spacer increases revenue, reduces operational leaks, and creates a premium customer experience for workspace and hospitality operators.

## Lead Generation (Hormozi $100M Leads Framework)

### Scorecard (12-Index Matrix)
File: `Spacer_Lead_Magnet_Scorecard.md`
Framework: Alex Hormozi's $100M Leads, Ch.2 — 7 Steps to Creating an Effective Lead Magnet
Scale: 1-5 per index (60 max). Minimum viable: 45/60.

| Rank | Lead Magnet | Type | Score |
|------|------------|------|-------|
| 1 | **Commission Leakage Calculator** | Reveal x Software (Google Sheet + Loom) | **58/60** |
| 2 | **Kill the Key Handover** | Reveal x Info (7-page PDF) | **55/60** |
| 3 | **Rooms You're Paying For But Not Selling** | Reveal x Info (7-page PDF) | **54/60** |
| 4 | **Free Property Operations Audit** | Reveal x Services (30-min review) | **52/60** |
| 5 | **Is Your Apartment Actually Profitable?** | Reveal x Info (8-page PDF) | **52/60** |
| 6 | **Direct Booking Playbook** | One Step x Info (15-20 page PDF) | **49/60** |

### Deployment Strategy (Updated per Mike — March 3, 2026)
| Role | Lead Magnet | Why |
|------|------------|-----|
| **Primary (all outreach)** | Free Property Operations Audit | Mike's preferred pick — broad reach, works for all properties |
| **Secondary (high-end targets)** | Commission Leakage Calculator | Highest score, but smart lock content limits audience to high-end |
| **Supporting (content/SEO)** | Kill the Key Handover + Rooms Not Selling | Already built, scalable for content distribution |

### Distribution Channels (Mike's Decision)
**Focus: Cold Outreach + Paid Ads** (skip warm outreach and content for now)
- Full Assembly Line: `claude.ai contex/Spacer-Distribution-Lite-Template.md`
- Existing prospect lists: `abuja_50_apartments.xlsx`, `abuja_150_additional_apartments.csv`

### Lead Magnet Files (Created March 2, 2026)
**Markdown guides** (in `claude.ai contex/`):
- `Lead-Magnet-5-Revenue-Leaks.md` — 5 hidden revenue leaks self-diagnostic
- `Lead-Magnet-Kill-The-Key-Handover.md` — Smart lock playbook
- `Lead-Magnet-Rooms-Not-Selling.md` — Occupancy visibility guide
- `Lead-Magnet-Actually-Profitable.md` — Financial health check (5 metrics)

**PDF generators** (project root):
- `generate_lead_magnet_1.py` → `generate_lead_magnet_4.py`

**Finished PDFs** (in `Proposals/`):
- `Lead-Magnet-5-Revenue-Leaks.pdf`
- `Lead-Magnet-Kill-The-Key-Handover.pdf`
- `Lead-Magnet-Rooms-Not-Selling.pdf`
- `Lead-Magnet-Actually-Profitable.pdf`

### Hormozi Structure (all magnets follow)
Hook → Problem revelation → Cost calculation (NGN) → Free fix (give away the secret) → Automated fix (Spacer) → CTA (free 15-min audit with Yasmin Umar)

---

## Key Documents Created
- Spacer Pitch Guides (Mafia Offer style — Hospitality & Co-working versions)
- Spacer Proposal Template
- Feature Requirements Document (FRD) for Virtual Spaces
- User Story Document
- Technical Specification
- Designer Specification Document
- Traceability Document (test checklist)
- Staff Training Guides
- Project Sign-off Documents
- Spacer Lead Magnet Scorecard (`Spacer_Lead_Magnet_Scorecard.md`)
- 4 Lead Magnet PDFs + generators (see Lead Generation section above)

---
*Last updated: 2026-03-03*
