# Spacer — Smart Hospitality & Workspace Management Platform

**Status:** Live & Revenue-Generating
**Domain:** spacer.so
**Pricing:** NGN 2M-3M per deployment
**Version:** 3.19.5

---

## What It Is

Spacer is Algolog's flagship product — an enterprise-grade, multi-tenant SaaS platform that enables organizations to manage and monetize physical spaces through automated booking, payment processing, and smart access control. Originally built for coworking spaces, it has found strong product-market fit in the Nigerian hospitality sector (serviced apartments, hotels, resorts).

---

## Tech Stack (from codebase)

### Frontend (spacer monorepo — `frontend/`)
- **Framework:** Next.js 14 + React 18
- **UI:** Radix UI primitives (dialog, dropdown, tabs, select, switch, checkbox, popover, alert-dialog, toggle) + NextUI + Tailwind CSS
- **State/Data:** SWR, Axios, js-cookie, jwt-decode
- **Charts:** Recharts + Chart.js (react-chartjs-2)
- **Rich Text:** TipTap editor
- **Calendar:** @event-calendar (core + list), react-big-calendar, react-datepicker, react-day-picker
- **QR:** react-qr-code, react-qrcode-scanner
- **PDF/Export:** jspdf, html2pdf.js, html2canvas, dom-to-image-more
- **Animations:** Framer Motion
- **3D/Panorama:** Three.js, Panolens (360-degree virtual tours)
- **Real-time:** Socket.io client, WebSocket (ws)
- **Encryption:** CryptoJS
- **Carousel:** Swiper
- **Payments:** @paystack/inline-js
- **Hosting:** Netlify

### Backend (spacer monorepo — `server/`)
- **Framework:** NestJS 10 + Express
- **Database:** MySQL (mysql2) + TypeORM + Prisma
- **Auth:** JWT + Passport + bcrypt + express-session
- **Cloud:** Azure Storage Blob
- **IoT:** @tuya/tuya-connector-nodejs (smart locks)
- **Payments:** Paystack (via Axios)
- **Email:** Nodemailer (@nestjs-modules/mailer)
- **Scheduling:** @nestjs/schedule (cron jobs for renewals, reminders)
- **Google APIs:** googleapis (calendar, sheets integration)
- **Real-time:** @nestjs/websockets + @nestjs/platform-socket.io
- **API Docs:** @nestjs/swagger
- **Health Checks:** @nestjs/terminus
- **Validation:** class-validator + class-transformer

### Related Repos
| Repo | Purpose |
|------|---------|
| `spacer` | Main monorepo (frontend + server) |
| `spacer-frontend` | Standalone booking portal frontend (Next.js) |
| `spacer-api` | Standalone NestJS backend API |
| `spacer-website` | Marketing site generator (Next.js) |
| `Admin-spacer` | Super admin panel (Next.js + ShadCN) |
| `alegrefarm` | Alegre Farms custom deployment (Next.js + ShadCN) |

---

## Backend Modules (from server/src/)

| Module | Purpose |
|--------|---------|
| `auth` | JWT authentication, login, registration |
| `bookings` | Core booking engine (create, manage, check-in/out) |
| `payments` | Paystack integration, payment processing |
| `invoices` | Invoice generation and management |
| `receipts` | Receipt generation and delivery |
| `smartlocks` | Tuya IoT smart lock integration (code generation, expiry) |
| `subscriptions` | Recurring subscription management (all tier types) |
| `renewal` | Automated renewal reminders and processing |
| `dashboard` | Real-time occupancy, availability, financial reporting |
| `org-website` | Auto-generated property marketing websites |
| `user-management` | Staff roles, permissions, multi-tenant user management |
| `rbac` | Role-based access control |
| `notifications` | Email/SMS notifications, booking confirmations |
| `settings` | Organization settings, branding, configuration |
| `cron` | Scheduled jobs (renewals, reminders, expiry checks) |
| `cart-abandonment` | Cart abandonment tracking and recovery |
| `erps` | ERP integrations |
| `integrations` | Third-party integrations |
| `audit` | Audit logging |
| `arbitrary_invoices` | Custom/manual invoicing |
| `admin` | Super admin operations |
| `banks` | Bank account management |

---

## Frontend Routes (from frontend/app/)

| Route | Purpose |
|-------|---------|
| `/` | Homepage |
| `/[customUrl]` | Public booking portal for each property |
| `/site` | Marketing site generator |
| `/admin` | Admin dashboard |
| `/auth` | Authentication flows |
| `/login` | Login page |
| `/registration` | User registration |
| `/payment` | Payment processing |
| `/guest-payment` | Guest payment flow |
| `/pricing` | Pricing pages |
| `/createspace` | Space creation wizard |
| `/company` | Company/organization management |
| `/availabilityhour` | Availability hour configuration |
| `/googleform` | Google Form integration |
| `/welcome` | Welcome/onboarding |
| `/support` | Support pages |
| `/solution` | Solution pages |
| `/resources` | Resource pages |
| `/unsubscribe` | Email unsubscribe |

---

## Core Features

- **Multi-tenant architecture** — each property gets custom branding, URL, and auto-generated marketing website
- **Property marketing website** (`/site/[orgSlug]`) — auto-generated luxury site with hero, gallery, room showcase, contact info
- **Booking portal** (`/[customUrl]`) — guests browse spaces, select dates, book, and pay online
- **Multi-tier booking engine** — hourly, daily, weekly, monthly, quarterly, bi-annual, annual
- **Paystack payment integration** — card and bank transfer, instant confirmation
- **Smart lock automation** — generates unique Tuya access codes, sent to guests, auto-expire at checkout
- **QR check-in** — guests scan to check in, validated against active bookings
- **Invoice and receipt generation** — automatic for all booking types
- **Real-time dashboard** — occupancy, availability, financial reporting via WebSocket
- **Conflict management** — prevents double-bookings with admin override toggle
- **Automated renewals and notifications** — reminders for all subscription types
- **Staff role management** — role-based access (receptionist, manager, cashier)
- **360-degree virtual tours** — Panolens/Three.js integration
- **Cart abandonment tracking** — recover incomplete bookings
- **PDF export** — invoices, receipts, reports exportable as PDF
- **Luxury design system** — sharp 90-degree corners, monochrome slate palette, purple CTAs, 500-700ms animations

## In Development
- Unified gallery view (multiple identical units as single listing)
- Virtual spaces (subspace packages — e.g., 1BR/2BR under 3BR parent)
- Admin approval workflow for virtual space bookings
- Automatic conflict prevention between parent/child spaces

---

## Active Deployments

| Client | Location |
|--------|----------|
| Saadatu's Apartment | Kaduna |
| Alegre Farms | Bwari, Abuja |
| DuloWork | Lagos |
| Qas Luxury Apartments | Abuja |

---

## Business Value

- Replaces WhatsApp/Excel-based property management
- Direct bookings reduce OTA commission (15% Airbnb fee → 0%)
- Smart lock automation eliminates key handover logistics
- Auto-generated marketing websites cost ~NGN 0 to deliver but worth NGN 500K+ to the client
- Premium website positioning drives 20-35% higher ADR

---

*Based on codebase analysis of 6 repositories under algologai organization + Product_Context/Spacer.md*
