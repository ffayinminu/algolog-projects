# PrivateTransfer — Anonymous Money Transfer Platform

**Status:** Live
**Domain:** privatetransfer.ng
**Backend:** Shared with SkillPay (`anosend` repo)

---

## What It Is

PrivateTransfer is an anonymous money transfer platform. Users can send money to any Nigerian bank account without revealing their identity, or create shareable payment links to receive money without exposing their bank details. Direct bank settlement via Paystack.

Originally branded as AnonSend, now operates as PrivateTransfer (privatetransfer.ng) with the "Gift Privately" feature as its core product.

---

## Tech Stack

Runs on the shared SkillPay backend — see SkillPay.md for full tech stack details.

- **Backend:** NestJS + MySQL 8.0 + TypeORM
- **Frontend:** Next.js 15 + React 18 + Radix UI + Tailwind
- **Payments:** Paystack (direct bank transfer)
- **Hosting:** Vercel (frontend), custom servers (backend)

---

## Core Features

### Gift Privately (Send Money Anonymously)
- Send money to any Nigerian bank account (NGN 100-100,000)
- Recipient sees only the payment, not the sender's identity
- Sender provides only an email for tracking — no account required
- Optional narration and personal notes
- Flat NGN 1,000 fee added to sender's payment
- Direct bank settlement via Paystack

### Receive Anonymously (Payment Links)
- Create shareable payment links to receive money (NGN 1,000-100,000)
- Bank details remain completely hidden from payers
- Customizable link title and purpose
- Share on social media, WhatsApp, anywhere
- Fee: 3% + NGN 200 (max NGN 4,000) deducted from received amount
- Email notifications for each payment received

### Transaction Tracking
- Search by transaction reference and email
- View current status and processing stage
- Track transfer progress in real-time

---

## Use Cases

- **Fundraising** — weddings, emergencies, causes — without exposing bank details
- **Creator tips** — content creators add link to bio for fan support
- **Anonymous gifts** — send money to someone without them knowing who sent it
- **Freelancer payments** — collect payments via link instead of sharing bank details each time

---

## Security

- Real-time fraud detection (IP velocity, amount analysis, suspicious content)
- IP blocking/whitelisting
- Rate limiting: 100 requests per 60 seconds
- All transfers processed through Paystack's secure infrastructure

---

*Based on codebase analysis of `anosend` repo + Product_Context/PrivateTransfer.md + Product_Context/AnonSend.md*
