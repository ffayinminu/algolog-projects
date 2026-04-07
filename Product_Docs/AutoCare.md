# AutoCare — Automated Service Reminders for Auto Workshops

**Status:** Built & Demo-Ready
**Repo:** `autocare`
**Contact:** autocarenigeria@algolog.co

---

## What It Is

A platform helping automotive businesses automatically notify customers when vehicles are due for servicing. Combines a no-code operational backend (Airtable + Zapier) with a polished marketing website (Next.js).

---

## Two Implementations

### 1. No-Code Stack (Operational)
- **Database:** Airtable (customer/vehicle records, interface for staff)
- **Automation:** Zapier (triggers reminders based on service dates)
- **WhatsApp:** SyncMate (WhatsApp integration for reminder delivery)
- **Reminders:** Automated at 7 days and 3 days before service due date
- **Multi-tenant:** Personalized dashboards per workshop

### 2. Marketing Website (from `autocare` repo)

**Tech Stack:**
- **Framework:** Next.js 16 (App Router, `src/` directory)
- **Language:** TypeScript
- **Styling:** Tailwind CSS v4
- **UI:** ShadCN UI (new-york style, Lucide icons)
- **Hosting:** Netlify

**Design System:**
- **Fonts:** Outfit (primary) + DM Mono (monospace accents)
- **Theme:** Always dark — no light/dark toggle
- **Colors:** Dark backgrounds (#0C0E12, #13161C, #1A1D25) with amber/gold accent (#F59E0B)
- **Animations:** Custom scroll-reveal via IntersectionObserver, fadeUp, pulse-glow, gearSpin, float keyframes
- **Noise overlay:** SVG noise texture on body

**Page Sections:**
Nav → Hero (with phone mockup) → Problem → How It Works → Features → Testimonials → Pricing → CTA → Footer

**Also includes:** `autocare.html` — original static HTML file kept for reference

---

## App Structure (from codebase)

```
src/
├── app/
│   ├── layout.tsx      — Root layout (fonts, metadata)
│   ├── globals.css     — Tailwind v4 config, animations
│   ├── page.tsx        — Landing page (all sections)
│   ├── api/            — API routes
│   ├── contact/        — Contact page
│   └── not-found.tsx   — 404 page
├── components/
│   └── ui/button.tsx   — ShadCN Button
├── hooks/
│   └── use-scroll-reveal.ts  — IntersectionObserver animation hook
└── lib/
    └── utils.ts        — cn() utility
```

---

## Core Features (Product)

- Personalized dashboard with all customers and vehicles
- Automated WhatsApp reminders at 7 days and 3 days before service due
- Complete service history per vehicle (date, type, mileage, notes)
- Activity logs showing when reminders were sent
- Custom messaging for promotions and seasonal offers
- Zero app downloads — browser-based interface

---

## Target Market

Auto-mechanic workshops, car service centers, fleet management companies in Nigeria.

---

*Based on codebase analysis of `autocare` repo (CLAUDE.md, src/ structure, package.json) + Product_Context/Autocare.md*
