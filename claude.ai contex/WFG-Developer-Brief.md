# WorkingForGod.org / Ethical Leadership Institute — Developer Brief

**Project:** ELI (lead brand) + WorkingForGod.org (associated brand) learning platform
**Prepared by:** Algolog Limited
**Audience:** Development team
**Scope basis:** Signed Agreement (Scope of Work & Deliverables). This brief describes **only** what is in the agreed scope — do not add features beyond what is listed here.

---

## 1. What We Are Building

A faith-and-ethics learning platform delivered as **two front-ends sharing one backend and one database**:

- **Ethical Leadership Institute (ELI)** — the primary, corporate-facing brand (ethicalleadershipinstitute.org)
- **WorkingForGod.org (WFG)** — the associated Christian-facing brand (workingforgod.org)

**Each brand is served on its own domain.** The domain a visitor arrives on decides which experience they get — opening the ELI link lands them in the ELI front-end, and opening the WorkingForGod.org link lands them in the WFG front-end. There is no manual "pick a brand" step; the entry domain selects it. Cross-links between the two domains then let users move from one to the other.

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

### 3.3 Live Sessions (Occasional)
- Support for **occasional live (real-time) sessions** alongside the standard pre-recorded courses.
- An integrated live-session tool that handles **scheduling, participant access, and live delivery**.
- Enrolled **learners and cohorts** can join scheduled live sessions from within the platform.
- Live sessions sit alongside the course library — the platform stays primarily on-demand, with live used for special/occasional sessions.

### 3.4 Learning Programs & Assessments
- Group individual courses into structured **learning programs / journeys**.
- **Pre-, during-, and post-module assessments.**
- Pass / benchmark logic to track understanding and learning milestones.

### 3.5 Cohorts & Group Learning
- Support both **individual learner profiles** and **group (cohort) profiles**.
- Assign learners to cohorts that take courses/programs together.
- Group progress tracking and reporting.

### 3.6 Article & Resource Library
- Articles categorized by theme.
- Search and filter functionality.
- Grid/list view with thumbnails, titles, and summaries.
- **Multi-format resources:** PDF, Excel, Word, video, and audio.
- Embedded content support (YouTube sermons / teaching clips).

### 3.7 Community Forum
- **"Post a Dilemma"** — users anonymously submit real ethical/workplace issues.
- Moderated forum with feedback from trusted contributors.
- **AI-assisted first-line moderation** with human review and approval before publishing.
- Categorized discussions.

### 3.8 Speakers, Leaders & Events
- Speaker & leader profiles highlighting marketplace credibility and faith journeys.
- Upcoming conferences and speaker lineup.
- Faith-based workplace event promotions and announcements.

### 3.9 Certificates & Credentials
- **Certificate of completion** issued for each learning journey.
- (No external/LinkedIn issuance — out of scope.)

### 3.10 Subscription & Payment System
- **Individual plans:** Monthly and Yearly options.
- **Organization plans:** tiered pricing based on number of seats, with an **admin dashboard** for organizations to monitor staff participation.
- **Free tier** (teaser access).
- Payment gateway integration via **Paystack** (card + transfer).
- Automated receipts/invoices on successful payment.

### 3.11 User Profile & Dashboard
- Track completed courses, progress, and completion rates.
- **Personalised recommendations** ("others who learned this also learned…").
- Save/bookmark articles and favourite lessons.
- Subscription management.
- Course history.

### 3.12 About Us & Mission Page
- Vision and mission statement.
- Core scriptures that guide the platform.
- Platform goals, narrative, and connection to AiMP and WFG.

### 3.13 Content Management System (CMS) & Analytics
- Admin panel for uploading videos, articles, and resources.
- User management and subscription monitoring.
- **Content tagging for dual-brand (ELI + WFG) distribution.**
- **Analytics & benchmarking** — engagement, completion, and cohort performance.
- Forum moderation tools.

### 3.14 Scalable Data Architecture
- Database structured to hold **500,000+ profiles**.
- Cleanly sectioned for reporting, analysis, and benchmarking.
- Built to scale for rapid expansion.

---

## 4. Network Integration & Cross-Linking
- Each brand has its **own domain** (ethicalleadershipinstitute.org and workingforgod.org); the domain visited determines the front-end shown.
- "AiMP initiative / join the network" calls-to-action woven through the content.
- Cross-linking between the two domains (ELI ↔ WorkingForGod.org) lets users move from one brand to the other and funnels users in both directions.
- SEO setup under both domains.

---

## 5. Roles & Access (cross-cutting)
- **Learner (individual)** — browse, subscribe, take courses/programs, forum, dashboard.
- **Organization admin** — manage seats, monitor staff participation.
- **Content admin / moderator** — CMS, content tagging, forum moderation (incl. reviewing AI-flagged posts).
- Role-based access control enforced across the backend.

---

## 6. User Stories & Feature Walkthroughs (how each role operates)

Each capability below is written as a user story — *As a [role], I want [capability], so that [benefit]* — followed by a plain-language, **step-by-step walkthrough of how the feature behaves** in the product. These describe the experience and behaviour only; implementation choices are left to the development team. Nothing here adds scope beyond Section 3.

---

**A. Front-End (User-Facing) Roles**

### 6.1 Visitor / Prospect (not logged in)

**6.1.1 Explore the platform before committing**
*As a visitor, I want to browse the landing page, featured courses, and featured speakers, so that I understand the platform before committing.*
1. The visitor arrives on the home page and sees the hero section with the mission tagline.
2. They scroll through Featured Speakers & Leaders (photo + short bio each), Featured Courses (thumbnails), and a testimonials slider.
3. Dynamic counters surface platform activity (e.g., number of courses, learners).
4. Two clear calls-to-action invite them to continue as an **individual** or as an **organization**.

**6.1.2 Land on the right brand by its domain, and cross over when wanted**
*As a visitor, I want the link I open to take me straight to the matching brand, so that I land on the one that fits me without choosing manually.*
1. The visitor opens a link and lands directly in the brand tied to that domain — the ELI domain opens the corporate-facing ELI experience; the WorkingForGod.org domain opens the Christian-facing WFG experience.
2. Each brand carries its own theming and surfaces its own set of content — ELI shows the neutral core; WFG shows both the core and the Christian deep-dive.
3. Cross-links within each brand let the visitor move over to the other domain when they want to, funnelling users in both directions.

**6.1.3 Sample free-tier (teaser) content**
*As a visitor, I want to try teaser content without paying, so that I can judge the value first.*
1. Selected courses/lessons are marked as free-tier.
2. The visitor can open and watch this teaser content without registering or paying.
3. When they reach paid content, they are prompted to register and subscribe.

**6.1.4 Register and subscribe**
*As a visitor, I want to register and subscribe as an individual or an organization, so that I can unlock full content.*
1. The visitor chooses an individual plan (monthly or yearly) or an organization (seat-based) plan.
2. They complete registration and pay via the payment gateway (card or transfer).
3. On successful payment, access is unlocked immediately and a receipt is sent.

**6.1.5 Understand the mission and the network**
*As a visitor, I want to read the platform's mission and how it connects to the wider network, so that I understand what I'm joining.*
1. The visitor opens the About Us & Mission page and reads the vision, mission, guiding scriptures, and platform goals.
2. The page explains the connection to AiMP and WorkingForGod.org.
3. "Join the network / AiMP initiative" calls-to-action are woven through the content, and cross-links let the visitor move between the ELI and WFG experiences.

---

### 6.2 Individual Learner

**6.2.1 Enrol in courses and structured programs**
*As a learner, I want to enrol in courses and programs, so that I can follow a guided learning journey.*
1. The learner browses the Course Library, filtered by theme (Leadership, Career Growth, Integrity, Business Ethics).
2. They open a course to see its overview, instructor, length, and the modules it contains.
3. They enrol in a single course or in a structured **program/journey** that groups several courses in sequence.
4. The course/program appears on their dashboard for easy resumption.

**6.2.2 Watch microlearning modules and resume later**
*As a learner, I want 5–10 minute modules with chapter navigation and "Continue Watching", so that I can learn in short sessions and pick up where I stopped.*
1. Each module plays as a short 5–10 minute video.
2. A chapter/section list lets the learner jump between segments.
3. A progress bar fills as they advance through the course.
4. When they return, "Continue Watching" takes them straight back to where they left off.

**6.2.3 Unlock the optional Christian deep-dive**
*As a learner, I want to open the deep-dive via "Learn More", so that I can go deeper when I choose to.*
1. After completing the neutral core of a module, the learner sees a "Learn More" prompt.
2. Selecting it reveals the optional Christian deep-dive layer for that topic.
3. On WFG this is surfaced naturally; on ELI it remains an opt-in choice.

**6.2.4 Take assessments and confirm understanding**
*As a learner, I want pre-, during-, and post-module assessments with a pass/benchmark result, so that I can confirm my understanding.*
1. Before a module, a short pre-assessment gauges starting knowledge.
2. During the module, check-point questions reinforce learning.
3. After the module, a post-assessment measures what was learned.
4. The learner sees a pass/benchmark result that marks the milestone as achieved.

**6.2.5 Reflect after each segment**
*As a learner, I want reflection/discussion questions after each video, so that I can apply what I learned.*
1. At the end of a segment, reflection or discussion questions are presented.
2. The learner works through them before moving on to the next segment.

**6.2.6 Track progress on a personal dashboard**
*As a learner, I want a dashboard of my progress, completion rates, and history, so that I can see how far I've come.*
1. The dashboard shows courses in progress, completion percentages, and a full course history.
2. Completed journeys and earned certificates are listed.
3. Subscription status is visible from the same place.

**6.2.7 Discover relevant next courses**
*As a learner, I want personalised recommendations, so that I can find what to learn next.*
1. Based on what the learner has taken, the platform suggests related courses ("others who learned this also learned…").
2. Recommendations appear on the dashboard and within course pages.

**6.2.8 Bookmark and download resources**
*As a learner, I want to bookmark lessons/articles and download resources, so that I can revisit them.*
1. The learner bookmarks any course, lesson, or article to find it again quickly.
2. Each course can offer downloadable resources in multiple formats (PDF, Excel, Word, video, audio), including scripture references where relevant.
3. Bookmarked items appear in the learner's profile.

**6.2.9 Browse the article & resource library**
*As a learner, I want a searchable article library, so that I can read and learn outside of video courses.*
1. The learner opens the Article & Resource Library, organised by theme.
2. They search and filter to find a topic, viewing results as a grid/list with thumbnails, titles, and summaries.
3. Articles may embed teaching clips (e.g., YouTube sermons) and link to downloadable resources.

**6.2.10 Post a dilemma anonymously and get guidance**
*As a learner, I want to post a workplace/ethical dilemma anonymously and read moderated feedback, so that I can get guidance safely.*
1. The learner submits a dilemma through "Post a Dilemma"; their identity is never shown.
2. The post is screened by AI first-line moderation and then reviewed by a human moderator before publishing.
3. Once approved, it appears under the right category with trusted feedback the learner can read and respond to.

**6.2.11 Browse speakers, leaders, and events**
*As a learner, I want to see speaker profiles and upcoming events, so that I can engage beyond the courses.*
1. The learner views speaker/leader profiles highlighting their marketplace credibility and faith journeys.
2. They see upcoming conferences, the speaker lineup, and faith-based workplace event announcements.

**6.2.12 Earn a certificate of completion**
*As a learner, I want a certificate for each completed journey, so that I have proof of completion.*
1. When the learner finishes all modules and assessments in a journey, the system marks it complete.
2. A certificate of completion is issued automatically and made available from their dashboard.

**6.2.13 Manage subscription and billing**
*As a learner, I want to manage my monthly/yearly subscription and receive receipts, so that I stay in control of billing.*
1. The learner views and changes their plan from the profile area.
2. Payments are processed via the gateway; a receipt/invoice is sent automatically on each successful charge.

**6.2.14 Join an occasional live session**
*As a learner, I want to join scheduled live sessions from within the platform, so that I can take part in real-time sessions alongside the recorded courses.*
1. When a live session is scheduled, the learner sees it surfaced in the platform (e.g., on their dashboard or alongside the related course/program), with its date and time.
2. Eligible learners — and learners who belong to an assigned cohort — are granted access to that session.
3. At the scheduled time, the learner joins the live session directly from within the platform, without leaving for a separate tool.
4. After the session, the learner continues with the standard on-demand courses as usual; live sessions remain occasional rather than the primary mode.

---

**B. Admin & Management Roles (back-office)**

### 6.3 Organization Admin

**6.3.1 Subscribe on a seat-based plan**
*As an org admin, I want a seat-based plan, so that I can enrol my team.*
1. The org admin selects an organization plan priced by number of seats.
2. They complete payment and receive their organization workspace and admin dashboard.

**6.3.2 Assign staff to seats and cohorts**
*As an org admin, I want to assign staff to seats and group them into cohorts, so that teams learn together.*
1. The admin adds staff members and assigns each to a seat.
2. They group learners into cohorts that take the same courses/programs together.

**6.3.3 Track team progress**
*As an org admin, I want a dashboard of my team's progress and participation, so that I can monitor engagement.*
1. The admin dashboard shows group/cohort progress, completion rates, and participation.
2. The admin can identify who is on track and who is falling behind.

**6.3.4 Manage seats and subscription**
*As an org admin, I want to manage seats and the subscription, so that I can scale up or down.*
1. The admin adds or removes seats as the team changes.
2. Subscription and billing for the organization are managed from the same dashboard.

### 6.4 Content Admin / CMS Manager

**6.4.1 Upload and maintain content**
*As a content admin, I want to upload videos, articles, and multi-format resources, so that the libraries stay current.*
1. The admin uploads video modules, articles, and resources (PDF, Excel, Word, video, audio) through the CMS.
2. They organise content by theme and attach downloadable resources to courses.

**6.4.2 Tag content for the right brand**
*As a content admin, I want to tag content for ELI, WFG, or shared, so that each front-end surfaces the right material.*
1. For each item, the admin sets a dual-brand tag (ELI, WFG, or shared) and a content tier (neutral core vs Christian deep-dive).
2. Each front-end then renders only the content meant for it.

**6.4.3 Build programs and assessments**
*As a content admin, I want to group courses into programs and define assessments, so that learning journeys are structured.*
1. The admin groups individual courses into a structured program/journey.
2. They attach pre-, during-, and post-module assessments and set the pass/benchmark logic.

**6.4.4 Manage users and subscriptions**
*As a content admin, I want to manage users and monitor subscriptions, so that access stays accurate.*
1. The admin views users, their plans, and access levels.
2. They adjust access and monitor active/expired subscriptions.

**6.4.5 Review analytics and benchmarking**
*As a content admin, I want analytics on engagement, completion, and cohort performance, so that I can measure impact.*
1. The admin opens dashboards showing engagement, completion rates, and cohort/benchmark comparisons.
2. Data can be reviewed for reporting and to guide content decisions.

**6.4.6 Schedule and run occasional live sessions**
*As a content admin, I want to schedule live sessions and control who can join, so that I can deliver real-time sessions alongside the recorded courses.*
1. The admin creates a live session using the integrated live-session tool, setting its title, date, and time.
2. They set participant access — which learners and/or cohorts are allowed to join the scheduled session.
3. The session is surfaced to the eligible learners/cohorts within the platform ahead of time.
4. At the scheduled time, the admin runs the live session and the granted participants join from within the platform; this sits alongside the standard pre-recorded library and is used occasionally rather than as the default delivery mode.

### 6.5 Moderator

**6.5.1 Review AI-flagged submissions**
*As a moderator, I want to review AI-flagged forum posts before they publish, so that only appropriate, helpful content goes live.*
1. New dilemmas are first screened by AI and queued for the moderator.
2. The moderator reads each queued post and decides whether it is suitable.

**6.5.2 Approve, reject, and categorise**
*As a moderator, I want to approve/reject and categorise dilemmas, so that the forum stays organised and safe.*
1. The moderator approves a post (it publishes), rejects it, or sends it back.
2. Approved posts are filed under the correct category.

**6.5.3 Preserve anonymity**
*As a moderator, I want submitter anonymity preserved at all times, so that users feel safe posting.*
1. At no point is the submitter's identity shown — to other users or in the moderation view.

---

**C. Automated (System) Behaviour**

### 6.6 System (automated behaviour)

**6.6.1 First-line forum moderation**
*As the system, I screen new forum posts with AI and route them to a human, so that moderation scales without losing oversight.*
1. A new post is automatically checked by AI for tone and appropriateness.
2. It is placed in the moderator queue for human approval before going live.

**6.6.2 Instant onboarding on payment**
*As the system, I issue a receipt and unlock access on confirmed payment, so that onboarding is instant.*
1. When a payment is confirmed, access is unlocked immediately.
2. A receipt/invoice is generated and sent automatically.

**6.6.3 Automatic progress tracking and certification**
*As the system, I track progress and issue the certificate when a journey is finished, so that no manual step is required.*
1. The system records module completion and assessment results as the learner progresses.
2. When a full journey is complete, the certificate is issued automatically.

**6.6.4 Personalised recommendations**
*As the system, I generate recommendations from learning history, so that learners always have a relevant next step.*
1. The system reviews what a learner has taken and completed.
2. It surfaces related courses on the dashboard and course pages.

**6.6.5 Dual-brand content surfacing**
*As the system, I render content by brand tag, so that each front-end shows the right material.*
1. The system reads each item's brand tag and content tier.
2. ELI receives the neutral core; WFG receives both the core and the Christian deep-dive; shared content appears on both.

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
