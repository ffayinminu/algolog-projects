# WorkingForGod.org (WFG) — Product Context

## Overview
**WorkingForGod.org** is a Christian-based professional development and training platform. It provides curated video-based courses, articles, and resources aimed at empowering Christians to excel in the workplace while staying rooted in their faith. The platform targets both **individuals** and **organizations**, offering tailored subscription models for each.

**Tagline:** "Master Your Career, Honor God"

**Design Inspiration:** Masterclass.com, LinkedIn Learning — premium, elegant, with a distinct Christian identity.

**Status:** Figma prototype complete. Pre-development.

---

## Core Product Features

### 1. Video-Based Training Modules (Masterclass-Style)
- Curated courses from faith-driven professionals across industries
- Sectionalized video chapters (short segments per topic)
- Progress bar tracking per course
- "Continue Watching" functionality for returning users
- Reflection/discussion questions after each video segment
- Downloadable resources per course (PDF guides, scripture references)

### 2. Article & Written Resources Library
- Categorized by theme: Career Excellence & Faith, Integrity in Business, Biblical Wisdom for Professionals
- Search and filter by topic
- Grid/list view with thumbnails, titles, and summaries
- Bookmarking functionality

### 3. Subscription System (Dual Model)
**For Individuals:**
- Monthly / Yearly subscription
- Full access to all courses, articles, and community reflections

**For Organizations:**
- Tiered pricing based on number of employees/seats
- Admin dashboard to monitor staff participation and progress
- PSS (Per Seat Subscription) number tracking

### 4. User Profile & Dashboard
- Track completed courses and progress
- Save/bookmark articles and favourite lessons
- Subscription management
- Course history and certificates (future)

### 5. Community & Reflection
- Discussion/reflection questions under each video segment
- Community hub for dilemmas, testimonies, and mentorship (future expansion)

---

## Platform Structure & Screens

### Screen 1: Home / Landing Page
- Hero section with mission tagline: "Master Your Career, Honor God"
- Brief intro text + CTA buttons: **Explore Courses | Subscribe | About Us**
- Featured Trainers section (photos + short bios)
- Featured Courses section with thumbnails
- Testimonials slider
- Dual CTA: Join as Individual | Subscribe as Organization

### Screen 2: Course Library Page
- Search bar + filter by topic
- Grid/list view toggle
- Course cards: image, title, trainer name, brief overview

### Screen 3: Course Detail Page
- Banner with course title + trainer headshot/bio
- Video player section
- Chapter/section navigation (sidebar or bottom listing)
- Reflection questions and discussion prompts under each video
- Downloadable resources section (PDFs, scripture guides)

### Screen 4: Article Library
- Grid/list of articles categorized by themes
- Search and filter functionality
- Article thumbnails with title and summary

### Screen 5: Subscription / Pricing Page
- Individual vs Organization plans side by side
- Feature breakdown per plan
- Visual distinction between tiers
- CTA for each plan

### Screen 6: User Profile Dashboard
- Progress tracking (courses in progress, completed)
- Saved articles and bookmarked courses
- Subscription management section

### Screen 7: About Us Page
- Vision and mission statement
- Core scriptures that guide the platform
- Platform goals and narrative

### Navigation
Top nav bar: **Home | Courses | Articles | Subscribe | About | Login**

---

## Sample Content (Placeholders)

### Speakers / Trainers
1. **Tara Fela-Durotoye** — "Owning Your Faith in Competitive Workspaces"
2. **Cosmas Maduka** — "Building Godly Businesses in Nigeria"
3. **Debola Deji-Kurunmi** — "Strategic Leadership with Kingdom Principles"
4. **Laju Iren** — "Managing Personal Growth While Staying Rooted in Faith"
5. **Moyo Akin-Ojo** — "Entrepreneurship and Faith"

### Sample Course
- **Title:** "Thriving Without Compromise: Faith in Business"
- **Modules:**
  1. What It Means to Thrive as a Christian
  2. Building a Brand on Integrity
  3. Negotiating Without Compromising Values
  4. Maintaining Devotion Amidst Career Growth

### Sample Articles
- "Why Joseph's Leadership is a Blueprint for Today's Executives"
- "Esther: Courage and Influence in a Corporate World"

### Sample Course Segments (Module Example)
- Introduction: What Does it Mean to Work for God?
- Segment 1: Competing in the Workplace with Christian Values
- Segment 2: Navigating Office Politics without Compromise
- Segment 3: Witnessing through Excellence at Work

---

## Design System

### Color Palette
| Color | Hex | Usage |
|-------|-----|-------|
| White | `#FFFFFF` | Primary background, clean spaces |
| Black | `#000000` | Text, headings, key UI elements |
| Deep Maroon/Crimson | `#7B1F25` | Action buttons, highlights, overlays |
| Gold | `#CFAF5F` | Premium accents, subtle highlights, value/royalty |
| Light Grey | `#F5F5F5` | Section dividers, secondary backgrounds |

**Palette meaning:** Purity (white), Seriousness (black), Passion & Reverence (crimson), Value & Excellence (gold).

### Typography
- **Headlines:** Playfair Display / Georgia (elegance)
- **Body Text:** Open Sans / Inter (readability)

### Branding Elements
- Subtle Christian symbols (cross watermark patterns, scripture references as section dividers)
- Logo positioned top-left of navigation bar
- Minimalist, elegant visual style with Christian symbolism subtly woven into UI
- Mobile-responsive design (mobile-first for video and reading)

### Interactive Elements
- Hover effects on course cards and articles
- Progress trackers on courses
- "Continue Watching" for returning users
- Accessibility standards: appropriate font sizes, contrast ratios

---

## Target Users

### Individuals
- Christian professionals across industries
- Faith-driven entrepreneurs
- Church leaders looking for marketplace skills
- Young professionals seeking career + faith alignment

### Organizations
- Churches wanting professional development for staff/members
- Christian organizations investing in employee growth
- Businesses with faith-based values seeking team training

---

## Business Model

### Revenue: Subscription-Based
- **Individual Plan:** Monthly / Yearly — full access to all content
- **Organization Plan:** Tiered pricing by number of seats — admin dashboard, staff monitoring, PSS tracking

### Pricing (Internal — Client-Facing)
This is an **SDS (Solutions Development Services)** build for an external client.

**Prototype Phase:**
- UI/UX Design + Interactive Figma Prototype: NGN 1,200,000

**Full Platform Development (Post-Approval):**
| Component | Cost |
|-----------|------|
| Frontend Development | NGN 2,500,000 |
| Backend Development | NGN 2,000,000 |
| Subscription & Payment Integration | NGN 500,000 |
| Content Management System Setup | NGN 500,000 |
| Deployment & Testing | NGN 500,000 |
| **Total Development** | **NGN 6,000,000** |

**Maintenance & Support:** NGN 150,000/month (minor updates, bug fixes, server health checks)

### Delivery Phases
1. Share Figma prototype with client for feedback
2. Upon approval, sign development contract
3. Begin phased development

---

## Tech Considerations (For Development Phase)

### Suggested Stack
- **Frontend:** Next.js, ShadCN UI (Algolog standard stack)
- **Video:** HLS streaming / embedded player with chapter markers
- **CMS:** Headless CMS for courses and articles (Strapi or similar)
- **Payments:** Paystack for subscriptions (individual + organizational tiers)
- **Auth:** NextAuth or similar — individual accounts + organization admin accounts
- **Database:** PostgreSQL (users, subscriptions, progress tracking, org management)

### Key Technical Requirements
- Video streaming with chapter navigation and progress tracking
- Dual subscription model (individual vs. organization with seat management)
- Admin dashboard for organizations (monitor staff participation)
- Search and filtering for courses and articles
- Mobile-responsive, accessibility-compliant
- Downloadable resource management (PDFs, scripture guides)

---

## Wireframe Flow
1. Home/Landing
2. Course Listing (Library)
3. Course Details with Chapters
4. Video Player + Chapter Navigation
5. Articles Hub
6. Pricing & Subscription
7. Profile Dashboard
8. About Page

---

## Key Differentiators
- **Not a general e-learning platform** — specifically positioned at the intersection of faith and professional development
- **Masterclass-level production quality** — premium feel, not a church website aesthetic
- **Dual audience model** — individuals AND organizations (churches, Christian businesses)
- **Nigerian context** — speakers are recognizable Nigerian Christian professionals and business leaders
- **Reflection-driven learning** — not just passive video consumption; guided questions after each segment

---

## Files & References
- **Product Context:** `Product_Context/WorkingForGod.md` (this file)
- **Figma Prototype PDF:** `claude.ai contex/WorkinForGod.pdf` (16-page high-fidelity UI prototype — image-based, view visually)

---
*Last updated: 2026-04-02*
