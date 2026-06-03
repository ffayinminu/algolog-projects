# WorkingForGod.org / Ethical Leadership Institute — Developer Brief

**Project:** ELI (lead brand) + WorkingForGod.org (associated brand) learning platform
**Prepared by:** Algolog Limited
**Audience:** Development team
**Scope basis:** Signed Agreement (Scope of Work & Deliverables). This brief describes **only** what is in the agreed scope — do not add features beyond what is listed here.

---

## 1. What We Are Building

A faith-and-ethics learning platform delivered as **two front-ends sharing one backend and one database**:

- **Ethical Leadership Institute (ELI)** — the primary, corporate-facing brand (ethicalleadershipinstitute.org)
- **WorkingForGod.org (WFG)** — the associated Christian-facing brand

Both brands draw from the **same content library, user base, and backend services**. Branding, theming, and content tagging differentiate what each front-end surfaces.

The UI/UX has already been designed and approved as a high-fidelity Figma prototype covering all core screens and flows. **Build to the approved prototype.**

---

## 2. Core Content Model (applies across all modules)

- **Two-tier content:** every course/module has a **neutral core** (ethics, leadership, marketplace) and an **optional Christian "deep-dive"** unlocked via a "Learn More" prompt after the core content. ELI surfaces the neutral core; WFG surfaces both tiers.
- **Microlearning format:** courses are delivered as **5–10 minute video modules** with chapter/section navigation.
- **Content tagging:** backend tags content for **dual-brand distribution** (ELI vs WFG vs shared) so each front-end renders the correct set.

---

## 3. Feature Modules (functional descriptions)

### 3.1 Landing / Home Page
- Faith-aligned hero section with mission tagline.
- Featured Speakers & Leaders section (photos + short bios).
- Featured courses section with thumbnails.
- Testimonials slider.
- Dual call-to-action for **individuals** and **organizations**.
- Dynamic counters (e.g., course count) and speaker highlights.

### 3.2 Course Library & Training Modules
- Curated courses segmented by theme (Leadership, Career Growth, Integrity, Business Ethics).
- 5–10 minute microlearning video modules with chapter/section navigation.
- Two-tier content (neutral core + optional Christian deep-dive via "Learn More").
- Per-course progress bar tracking.
- "Continue Watching" for returning users.
- Reflection / discussion questions after each video segment.
- Downloadable resources per course (PDF guides, scripture references).
- Bookmarking and a related-courses feature.
- Free-tier access for teaser content.

### 3.3 Learning Programs & Assessments
- Group individual courses into structured **learning programs / journeys**.
- **Pre-, during-, and post-module assessments.**
- Pass / benchmark logic to track understanding and learning milestones.

### 3.4 Cohorts & Group Learning
- Support both **individual learner profiles** and **group (cohort) profiles**.
- Assign learners to cohorts that take courses/programs together.
- Group progress tracking and reporting.

### 3.5 Article & Resource Library
- Articles categorized by theme.
- Search and filter functionality.
- Grid/list view with thumbnails, titles, and summaries.
- **Multi-format resources:** PDF, Excel, Word, video, and audio.
- Embedded content support (YouTube sermons / teaching clips).

### 3.6 Community Forum
- **"Post a Dilemma"** — users anonymously submit real ethical/workplace issues.
- Moderated forum with feedback from trusted contributors.
- **AI-assisted first-line moderation** with human review and approval before publishing.
- Categorized discussions.

### 3.7 Speakers, Leaders & Events
- Speaker & leader profiles highlighting marketplace credibility and faith journeys.
- Upcoming conferences and speaker lineup.
- Faith-based workplace event promotions and announcements.

### 3.8 Certificates & Credentials
- **Certificate of completion** issued for each learning journey.
- (No external/LinkedIn issuance — out of scope.)

### 3.9 Subscription & Payment System
- **Individual plans:** Monthly and Yearly options.
- **Organization plans:** tiered pricing based on number of seats, with an **admin dashboard** for organizations to monitor staff participation.
- **Free tier** (teaser access).
- Payment gateway integration via **Paystack** (card + transfer).
- Automated receipts/invoices on successful payment.

### 3.10 User Profile & Dashboard
- Track completed courses, progress, and completion rates.
- **Personalised recommendations** ("others who learned this also learned…").
- Save/bookmark articles and favourite lessons.
- Subscription management.
- Course history.

### 3.11 About Us & Mission Page
- Vision and mission statement.
- Core scriptures that guide the platform.
- Platform goals, narrative, and connection to AiMP and WFG.

### 3.12 Content Management System (CMS) & Analytics
- Admin panel for uploading videos, articles, and resources.
- User management and subscription monitoring.
- **Content tagging for dual-brand (ELI + WFG) distribution.**
- **Analytics & benchmarking** — engagement, completion, and cohort performance.
- Forum moderation tools.

### 3.13 Scalable Data Architecture
- Database structured to hold **500,000+ profiles**.
- Cleanly sectioned for reporting, analysis, and benchmarking.
- Built to scale for rapid expansion.

---

## 4. Network Integration & Cross-Linking
- "AiMP initiative / join the network" calls-to-action woven through the content.
- Cross-linking between ELI and WorkingForGod.org (funnel users in both directions).
- SEO setup under the new domains.

---

## 5. Roles & Access (cross-cutting)
- **Learner (individual)** — browse, subscribe, take courses/programs, forum, dashboard.
- **Organization admin** — manage seats, monitor staff participation.
- **Content admin / moderator** — CMS, content tagging, forum moderation (incl. reviewing AI-flagged posts).
- Role-based access control enforced across the backend.

---

## 6. Technical Constraints (as agreed — build on this stack)

| Component | Technology |
|---|---|
| Server runtime | Node.js |
| Backend framework | NestJS |
| Frontend framework | Next.js + React |
| Database | PostgreSQL |
| Cloud hosting | Microsoft Azure |
| Infrastructure | Terraform (IaC) |
| Security standard | OWASP Top 10 compliance |
| Video delivery | HLS streaming + YouTube embeds |
| Payments | Paystack (or equivalent) |

**Key commitments:**
- Fully responsive (desktop, tablet, mobile).
- OWASP Top 10 compliance.
- Scalable Azure infrastructure with regular backups.
- CDN for optimized video streaming.
- Rate limiting and DDoS protection.

> Note: hosting and data costs (servers, storage, bandwidth, CDN) are billed to the client by the cloud provider — provision infrastructure accordingly but do not bundle these costs into the build.

---

## 7. Out of Scope (do NOT build)
These are explicitly **not** part of this delivery. Architect cleanly so they could be added later, but do not implement:
- University credit / accreditation integrations.
- Native mobile apps (the responsive web app covers mobile).
- External content-partner / third-party licensed-library integrations.
- LinkedIn (or any external) certificate issuance/verification.

---

## 8. Handover Deliverables
- Both front-ends + shared backend deployed on Azure.
- Full source code and admin access (no vendor lock-in).
- Deployment, QA, and a comprehensive manual.
- Staff training session.

---

## 9. What Unblocks the Build (from the client)
Development commences on signing of the Agreement; content is supplied during the build (not required to start). For go-live we need: domain access (ethicalleadershipinstitute.org + workingforgod.org), course/article/speaker content, settlement bank account + tax/VAT treatment, and the free-tier definition. See the Requirements List for the full set.
