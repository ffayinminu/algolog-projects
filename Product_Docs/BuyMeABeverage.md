# BuyMeABeverage — Professional Tipping & Support Platform

**Status:** Live
**Domain:** buymeabeverage.com
**Repo:** `buymeabeverage`
**Backend:** Shared with SkillPay (`anosend` repo)

---

## What It Is

A tipping platform for professionals who share knowledge — open-source developers, newsletter writers, educators, and mentors. Same architecture as BuyMeAShawarma but positioned for a more professional audience. Create a custom link, add it to GitHub READMEs, newsletter footers, or social bios. Direct Nigerian bank settlement via Paystack.

---

## Tech Stack (from codebase)

- **Frontend:** Next.js + React + Tailwind CSS + ShadCN-style components
- **Backend:** Shared SkillPay backend (NestJS + MySQL + Paystack)
- **Hosting:** Netlify
- **Design origin:** Figma

### Frontend Structure
Same structure as BuyMeAShawarma:
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

- Custom public link: buymeabeverage.com/[yourname]
- Direct bank settlement via Paystack
- No app download — supporters pay from browser
- Mobile-responsive
- Transaction history and supporter tracking
- Professional positioning for knowledge workers

---

## Target Users

- Open-source developers (link in GitHub READMEs)
- Newsletter writers (link in newsletter footer)
- Online educators and mentors
- Consultants sharing free advice
- Anyone in the knowledge economy

---

## Differentiation from BuyMeAShawarma

Same backend, same features. Different brand positioning:
- **BuyMeAShawarma** = casual, fun, creator-focused
- **BuyMeABeverage** = professional, knowledge-worker-focused

---

*Based on codebase analysis of `buymeabeverage` repo + Product_Context/BuyMeABeverage.md*
