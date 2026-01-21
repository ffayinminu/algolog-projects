# CYFT Facility Health Inspection System
## Demo Guide

**Version:** 1.0
**Date:** January 2026
**Prepared by:** Algolog Limited
**For:** CYFT Consulting Limited & Demo Teams

---

## Table of Contents

1. [Pre-Demo Preparation](#1-pre-demo-preparation)
2. [Demo Environment Setup](#2-demo-environment-setup)
3. [Demo Script - Standard Flow](#3-demo-script---standard-flow)
4. [Feature Showcase Sections](#4-feature-showcase-sections)
5. [Handling Common Questions](#5-handling-common-questions)
6. [Post-Demo Actions](#6-post-demo-actions)

---

## 1. Pre-Demo Preparation

### 1.1 Know Your Audience

Before the demo, understand who you're presenting to:

| Audience Type | Focus Areas | Key Pain Points |
|--------------|-------------|-----------------|
| Hospital Administrator | ROI, compliance, cost savings | Manual processes, compliance risk |
| Facility Manager | Ease of use, reporting, tracking | Paper checklists, lost documentation |
| Finance/Procurement | Cost visibility, budgeting | Unexpected repairs, no cost tracking |
| IT/Technical | Integration, security, deployment | System compatibility, data security |

### 1.2 Demo Checklist

**Before the demo, ensure:**

- [ ] Demo environment is accessible and loaded with sample data
- [ ] Test all features you plan to show (login, inspection, reports)
- [ ] Prepare sample facility: "Demo Hospital" or use client's actual facility name
- [ ] Have sample inspection data pre-loaded for at least 2-3 categories
- [ ] Prepare sample photos showing issues (generator, AC unit, electrical panel)
- [ ] Test report generation and download
- [ ] Ensure stable internet connection (or have offline mode ready)
- [ ] Prepare backup: screenshots/video walkthrough in case of technical issues

### 1.3 Demo Device Setup

**Recommended devices to have ready:**

1. **Laptop/Desktop** — For Admin Dashboard demo
2. **Tablet** — For Mobile Inspection App demo (field inspector view)
3. **Phone** — To show responsive design and notifications

---

## 2. Demo Environment Setup

### 2.1 Sample Facility Data

Pre-load the demo with this sample facility:

```
Facility Name: Cedar Crest Medical Center
Address: Plot 123, Central Business District, Abuja
Contact Person: Dr. Amina Hassan
Contact Phone: +234 801 234 5678
Last Inspection: December 15, 2025
```

### 2.2 Sample Inspection Scores

Have these scores pre-loaded to demonstrate the dashboard:

| Category | Score | Status | Issues | Est. Cost |
|----------|-------|--------|--------|-----------|
| Generator Health | 72/100 | Good | 2 | ₦95,000 |
| HVAC/AC Systems | 58/100 | Fair | 3 | ₦180,000 |
| Electrical Systems | 85/100 | Good | 1 | ₦45,000 |
| Water Systems | 45/100 | Critical | 4 | ₦320,000 |
| Fire Safety | 90/100 | Excellent | 0 | ₦0 |
| **Overall** | **70/100** | **Good** | **10** | **₦640,000** |

### 2.3 Sample Issues for Drill-Down Demo

**Generator Health - Cost Breakdown (₦95,000):**
| Item | Qty | Unit Price | Total |
|------|-----|------------|-------|
| Engine Oil (Shell Rimula) | 10L | ₦5,000 | ₦50,000 |
| Oil Filter | 1 | ₦15,000 | ₦15,000 |
| Air Filter | 1 | ₦12,000 | ₦12,000 |
| Labor | 1 | ₦18,000 | ₦18,000 |

**Water Systems - Issues Found (4 issues):**
1. Overhead tank showing rust patches - Severity: HIGH
2. Water pump making unusual noise - Severity: MEDIUM
3. Borehole pressure dropping - Severity: HIGH
4. Treatment system filter overdue - Severity: LOW

---

## 3. Demo Script - Standard Flow

### 3.1 Opening (2-3 minutes)

**Introduction:**

> "Thank you for joining us today. I'm going to show you how the CYFT Facility Health Inspection System can transform how you monitor, manage, and maintain your healthcare facility.
>
> The system was designed specifically for Nigerian healthcare facilities, addressing the unique challenges you face - from generator maintenance to compliance documentation.
>
> By the end of this demo, you'll see how CYFT can help you:
> - Reduce facility downtime by catching issues early
> - Save money through better maintenance planning
> - Generate professional reports in minutes, not hours
> - Track every naira spent on maintenance
>
> Let me show you how it works..."

---

### 3.2 Dashboard Overview (3-4 minutes)

**Navigation:**

1. **Login** — Show the secure login screen
   > "Each user has role-based access. Administrators see everything, while clients only see their own facilities."

2. **Main Dashboard** — Show overall facility health
   > "This is your command center. At a glance, you can see the health of your entire facility across 11 critical categories."

3. **Visual Score Display** — Point to the overall score
   > "Cedar Crest Medical Center currently has an overall health score of 70 out of 100, which is in the 'Good' range. But you'll notice Water Systems is in the critical zone at 45 - this needs immediate attention."

4. **Color-Coded Status** — Explain the visual system
   > "We use a simple traffic light system:
   > - Green (90-100) = Excellent
   > - Yellow (70-89) = Good
   > - Orange (50-69) = Fair
   > - Red (0-49) = Critical, needs immediate action"

---

### 3.3 Interactive Features Demo (5-7 minutes)

**This is the key differentiator - show the drill-down capabilities:**

#### A. Clickable Repair Costs

> "Now, here's something powerful. You see Water Systems has an estimated repair cost of ₦320,000. But where does that money go? Just click on the amount..."

**[Click on the cost]**

> "...and you get a complete itemized breakdown:
> - Tank replacement: ₦150,000
> - Pump repair: ₦80,000
> - Filter replacement: ₦50,000
> - Labor: ₦40,000
>
> Every naira is accounted for. You can even see receipt photos attached for verification."

#### B. Clickable Issues Found

> "Similarly, clicking on '4 issues' shows you exactly what was found..."

**[Click on issues count]**

> "Each issue shows:
> - What the problem is
> - How severe it is
> - What we recommend
> - Photo evidence
>
> No more vague reports. You know exactly what needs fixing."

#### C. Expandable Rows

> "Want even more detail? Click anywhere on the category row to expand it..."

**[Expand a category row]**

> "Now you see every checkpoint that was inspected, which passed, which failed, and the inspector's notes. Complete transparency."

---

### 3.4 Mobile Inspection App (4-5 minutes)

**Switch to tablet/phone:**

> "Now let me show you how inspections are conducted in the field. This is what your inspector sees on their tablet..."

1. **Select Inspection** — Open an assigned inspection
   > "The inspector sees their assigned inspections. They tap to open Cedar Crest..."

2. **Category Selection** — Show the 11 categories
   > "All 11 categories are listed. Let's go into Generator Health..."

3. **Checkpoint Entry** — Demonstrate filling in data
   > "For each item, the inspector:
   > - Checks each checkpoint (pass/fail)
   > - Takes photos of any issues
   > - Enters cost estimates
   > - Adds notes
   >
   > The score calculates automatically."

4. **Photo Capture** — Take a demo photo
   > "Photos are geotagged and timestamped - you know exactly when and where it was taken. This prevents fraud."

5. **Offline Mode** — Mention this capability
   > "And this works offline too. In areas with poor network, inspectors can complete the entire inspection and sync when they have connectivity."

---

### 3.5 Report Generation (3-4 minutes)

**Back to Admin Dashboard:**

> "Once the inspection is complete, generating a professional report takes seconds..."

1. **Click Generate Report**
   > "I'll click 'Generate Report' and select the Standard Report format..."

2. **Show Report Preview**
   > "Within seconds, you have a professional PDF report ready to share with your client. It includes:
   > - Executive summary with overall score
   > - Category breakdown table
   > - Critical issues highlighted
   > - Cost summary
   > - Recommended action plan
   > - All supporting photos"

3. **Download/Share Options**
   > "You can download as PDF, Word, or email directly to the client. The report is automatically branded with CYFT's logo."

---

### 3.6 Quality Verification & Audit Trail (2-3 minutes)

> "One of the most important features for preventing fraud and ensuring accountability..."

1. **Show Audit Trail**
   > "Every data point is tracked. You can see:
   > - Who entered the data
   > - When it was entered
   > - Any changes made
   > - Who approved the report"

2. **Quality Verification**
   > "For items like oil changes, the system requires:
   > - Photo of the oil brand/container
   > - Receipt upload
   > - Before/after photos
   >
   > If something looks suspicious - like reporting a ₦50,000 oil change but no receipt - the system flags it automatically."

---

### 3.7 Historical Tracking (2-3 minutes)

> "Finally, let me show you how the system tracks improvements over time..."

1. **Show Trend Chart**
   > "This chart shows Cedar Crest's facility health over the past 6 months. You can see:
   > - Overall score improved from 58 to 70
   > - Generator Health jumped from 45 to 72 after maintenance
   > - Water Systems needs attention - it's declining"

2. **Comparison Report**
   > "You can generate a comparison report showing current vs previous inspection, making it easy to track whether issues are being resolved."

---

### 3.8 Closing (2 minutes)

> "That's the CYFT Facility Health Inspection System. To summarize what you've seen:
>
> ✓ **Complete Visibility** — See your entire facility health at a glance
> ✓ **Drill-Down Details** — Click any number to see exactly what's behind it
> ✓ **Mobile-First** — Inspect from anywhere, even offline
> ✓ **Professional Reports** — Generated in seconds, not hours
> ✓ **Fraud Prevention** — Quality verification and full audit trail
> ✓ **Trend Tracking** — See improvements over time
>
> Do you have any questions about what you've seen?"

---

## 4. Feature Showcase Sections

Use these modules for specific audience interests:

### 4.1 For Finance Teams - ROI Focus

**Key points to emphasize:**
- Every cost is itemized and verifiable
- Budget forecasting based on inspection data
- Cost comparison between facilities
- Vendor price benchmarking

**Demo path:** Dashboard → Costs → Breakdown → Historical Costs → Budget Report

### 4.2 For Facility Managers - Operations Focus

**Key points to emphasize:**
- Simplified inspection process
- Mobile app ease of use
- Automatic calculations
- Photo documentation

**Demo path:** Mobile App → Checklist → Photo Capture → Auto-scoring → Submit

### 4.3 For Executives - Strategic Focus

**Key points to emphasize:**
- Portfolio-wide visibility (multiple facilities)
- Compliance and risk mitigation
- Executive summary reports
- Trend analysis

**Demo path:** Dashboard → Portfolio View → Executive Report → Trends

### 4.4 For IT Teams - Technical Focus

**Key points to emphasize:**
- Cloud-based, no installation required
- Role-based access control
- Data encryption and security
- Offline capability with sync
- API integration possibilities

**Demo path:** Settings → Security → User Management → Integrations

---

## 5. Handling Common Questions

### Q: "How long does an inspection take?"

> "A full 11-category inspection typically takes 2-3 hours on-site. The digital system is faster than paper because scores calculate automatically, photos attach instantly, and reports generate immediately after."

### Q: "Can we customize the checklist categories?"

> "Yes, categories and checkpoints can be customized. If you have specific equipment or compliance requirements unique to your facility, we can add those."

### Q: "What happens if there's no internet?"

> "The mobile app works fully offline. Inspectors can complete the entire inspection without internet. When they reconnect, all data syncs automatically to the cloud."

### Q: "How secure is our data?"

> "All data is encrypted in transit and at rest. We use role-based access control, and every action is logged for audit purposes. Your data never leaves Nigeria's jurisdiction."

### Q: "Can we see a sample report before committing?"

> "Absolutely. We can run a pilot inspection at your facility and provide a real report - at no cost - so you can see exactly what you'll receive."

### Q: "What's the pricing model?"

> *[Defer to commercial discussion - do not quote prices during demo]*
> "Pricing depends on the number of facilities and inspection frequency. Let's schedule a follow-up call to discuss a package that fits your needs."

---

## 6. Post-Demo Actions

### 6.1 Immediate Follow-Up (Within 24 hours)

- [ ] Send thank you email with demo summary
- [ ] Attach sample report PDF
- [ ] Include link to schedule pilot inspection
- [ ] Provide contact information for questions

### 6.2 Demo Summary Email Template

```
Subject: CYFT Demo Follow-Up - [Facility Name]

Dear [Name],

Thank you for taking the time to see the CYFT Facility Health Inspection System today.

As discussed, here's a quick summary of key benefits:
• Complete facility health visibility across 11 categories
• Clickable drill-downs for costs and issues
• Professional reports generated in seconds
• Full audit trail for accountability

Next Steps:
We'd love to conduct a complimentary pilot inspection at your facility
so you can see real results with your own data.

Please let me know a convenient time to schedule this.

Best regards,
[Your Name]
CYFT Consulting Limited
```

### 6.3 Track Demo Outcomes

Record after each demo:
- Attendee names and roles
- Questions asked
- Concerns raised
- Interest level (Hot/Warm/Cold)
- Follow-up date scheduled
- Pilot inspection requested (Y/N)

---

## Appendix: Quick Reference Card

### Demo Flow (20-25 minutes)

| Section | Duration | Key Points |
|---------|----------|------------|
| Opening | 2-3 min | Set the scene, state benefits |
| Dashboard | 3-4 min | Overall view, color coding |
| Interactive Features | 5-7 min | **STAR OF THE SHOW** - clickable costs/issues |
| Mobile App | 4-5 min | Field inspection workflow |
| Reports | 3-4 min | Generate and show PDF |
| Quality/Audit | 2-3 min | Fraud prevention, accountability |
| History | 2-3 min | Trends over time |
| Close | 2 min | Summarize, Q&A |

### Must-Show Features

1. ⭐ **Clickable Repair Costs** — Itemized breakdown
2. ⭐ **Clickable Issues** — Detailed issue list
3. ⭐ **Photo Documentation** — Evidence capture
4. ⭐ **Instant Report Generation** — PDF in seconds
5. ⭐ **Audit Trail** — Who did what, when

---

**Document Control**

| Version | Date | Author | Notes |
|---------|------|--------|-------|
| 1.0 | January 2026 | Algolog Limited | Initial Demo Guide |

---

**Prepared by:** Algolog Limited
**For:** CYFT Consulting Limited
**Contact:** support@algolog.co
