# BuyMeAShawarma — Food Gifting & Creator Tipping Platform

**Status:** Live
**Domain:** buymeshawarma.com
**Repo:** `buymeshawarma`
**Backend:** Shared with SkillPay (`anosend` repo)

---

## What It Is

A culturally Nigerian tipping/gifting platform where creators, freelancers, and community builders create a custom link and let supporters "buy them a shawarma" as a fun way to show appreciation. Direct bank settlement via Paystack. The Nigerian alternative to Ko-fi and Buy Me a Coffee — built for Naira, no international payment friction.

---

## Tech Stack (from codebase)

- **Frontend:** Next.js + React + Tailwind CSS + ShadCN-style components
- **Backend:** Shared SkillPay backend (NestJS + MySQL + Paystack)
- **Hosting:** Netlify
- **Design origin:** Figma (figma.com/design/cxOocKo5x4d9QTJLzZlkrP/BuyMeShawarma-UI)

### Frontend Structure
```
app/          — Next.js app router pages
components/   — Reusable UI components
config.ts     — App configuration
lib/          — Utilities
guidelines/   — Design/brand guidelines
imports/       — Shared imports
```

---

## Core Features

- Custom public link: buymeshawarma.com/[yourname]
- Direct bank settlement via Paystack — no holding period
- No app download — supporters pay in seconds from browser
- Mobile-responsive design
- Transaction history and supporter tracking
- Fun, culturally relevant experience ("buy me a shawarma")

---

## Target Users

- Content creators (YouTube, Twitter/X, Instagram)
- Freelance designers, writers, educators
- Podcast hosts
- Open-source developers
- Anyone building an audience who wants a simple way to accept support

---

*Based on codebase analysis of `buymeshawarma` repo + Product_Context/BuyMeAShawarma.md*
