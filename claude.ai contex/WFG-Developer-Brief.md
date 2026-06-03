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

## 6. User Stories (how each role operates)

Format: *As a [role], I want [capability], so that [benefit].* These map to the in-scope features above — they describe behaviour, not new scope.

### 6.1 Visitor / Prospect (not logged in)
- As a visitor, I want to browse the landing page, featured courses, and featured speakers, so that I can understand the platform before committing.
- As a visitor, I want to sample free-tier (teaser) content without paying, so that I can judge the value first.
- As a visitor, I want to move between the ELI and WorkingForGod.org experiences, so that I land on the brand that fits me.
- As a visitor, I want to register and subscribe as an individual or as an organization, so that I can unlock full content.

### 6.2 Individual Learner
- As a learner, I want to enrol in courses and structured programs, so that I can follow a guided learning journey.
- As a learner, I want to watch 5–10 minute modules with chapter navigation and "Continue Watching", so that I can learn in short sessions and resume where I stopped.
- As a learner, I want to unlock the optional Christian "deep-dive" via "Learn More", so that I can go deeper when I choose to.
- As a learner, I want to take pre-, during-, and post-module assessments and see my pass/benchmark result, so that I can confirm my understanding.
- As a learner, I want a dashboard showing my progress, completion rates, and course history, so that I can see how far I've come.
- As a learner, I want personalised recommendations, so that I can discover relevant next courses.
- As a learner, I want to bookmark articles/lessons and download resources (PDF, Excel, Word, video, audio), so that I can revisit them.
- As a learner, I want to post a dilemma anonymously in the forum and read moderated feedback, so that I can get guidance safely.
- As a learner, I want a certificate of completion for each learning journey, so that I have proof of completion.
- As a learner, I want to manage my subscription (monthly/yearly) and receive automated receipts, so that I stay in control of billing.

### 6.3 Organization Admin
- As an org admin, I want to subscribe on a seat-based plan, so that I can enrol my team.
- As an org admin, I want to assign staff to seats and to cohorts, so that groups can learn together.
- As an org admin, I want to track my team's group progress and participation from an admin dashboard, so that I can monitor engagement.
- As an org admin, I want to manage seats and the organization subscription, so that I can scale up or down.

### 6.4 Content Admin / CMS Manager
- As a content admin, I want to upload videos, articles, and multi-format resources, so that the libraries stay current.
- As a content admin, I want to tag content for ELI, WFG, or shared distribution, so that each front-end surfaces the right material.
- As a content admin, I want to group courses into programs and define assessments with pass/benchmark logic, so that learning journeys are structured.
- As a content admin, I want to manage users and monitor subscriptions, so that access stays accurate.
- As a content admin, I want analytics and benchmarking on engagement, completion, and cohort performance, so that I can measure impact.

### 6.5 Moderator
- As a moderator, I want to review AI-flagged forum submissions before they publish, so that only appropriate, helpful content goes live.
- As a moderator, I want to approve, reject, and categorise dilemmas, so that the forum stays organised and safe.
- As a moderator, I want submitter anonymity preserved at all times, so that users feel safe posting.

### 6.6 System (automated behaviour)
- As the system, I run AI first-line moderation on new forum posts and route them to a human for review/approval, so that moderation scales without losing oversight.
- As the system, on confirmed payment I issue a receipt/invoice and unlock access, so that onboarding is instant.
- As the system, I track learner progress automatically and issue the completion certificate when a journey is finished, so that no manual step is required.

---

## 7. Technical Constraints (as agreed — build on this stack)

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

## 8. Out of Scope (do NOT build)
These are explicitly **not** part of this delivery. Architect cleanly so they could be added later, but do not implement:
- University credit / accreditation integrations.
- Native mobile apps (the responsive web app covers mobile).
- External content-partner / third-party licensed-library integrations.
- LinkedIn (or any external) certificate issuance/verification.

---

## 9. Handover Deliverables
- Both front-ends + shared backend deployed on Azure.
- Full source code and admin access (no vendor lock-in).
- Deployment, QA, and a comprehensive manual.
- Staff training session.

---

## 10. What Unblocks the Build (from the client)
Development commences on signing of the Agreement; content is supplied during the build (not required to start). For go-live we need: domain access (ethicalleadershipinstitute.org + workingforgod.org), course/article/speaker content, settlement bank account + tax/VAT treatment, and the free-tier definition. See the Requirements List for the full set.
