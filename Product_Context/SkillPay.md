# SkillPay - Shared Payment & Commerce Backend

## Overview
SkillPay is the shared backend infrastructure that powers multiple Algolog consumer-facing products. It handles payment processing, user accounts, transaction tracking, and multi-brand/tenant support.

## Products Powered by SkillPay Backend
1. **skillpay.link** — Primary SkillPay platform
2. **buymeshawarma.com** — BuyMeAShawarma (food gifting/ordering)
3. **buymeabeverage.com** — BuyMeABeverage (beverage gifting/ordering)
4. **autogiving.ng / Pledged** — Church recurring giving platform (newest addition)

## Existing Backend Capabilities
| Capability | Status |
|---|---|
| User/merchant account creation | Available |
| Paystack integration | Available |
| Custom link generation | Available |
| Transaction logging | Available |
| Payout to bank account | Available |
| Multi-brand/tenant support | Available (serves 3+ brands) |

## New Capabilities Added for Pledged
- Recurring payment subscriptions (Paystack charge_authorization)
- Paystack subaccount support (for direct church settlement)
- Giving categories
- Member giving history
- Church admin dashboard

## Tech Stack
- Next.js frontend
- ShadCN UI design system
- Standard Algolog stack (Zustand, React Query, React Toastify, Axios, Recharts, React Hook Form, Motion)

## Design Workflow
SOP Path: B1 -> B2 -> B3

## Status
Built and operational — actively serving multiple products.

---
*Last updated: 2026-02-24*
