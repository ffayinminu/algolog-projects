# Algolog Proposal Management System
## Notion Database Setup Guide

**Purpose:** Manage 250+ proposals across multiple industries and companies
**Prepared for:** Algolog Limited Q4 Strategy

---

## Database Architecture

You'll need **3 linked databases**:

```
1. Companies Database (Master list of all prospects)
        ↓ (linked)
2. Proposals Database (Individual proposals sent)
        ↓ (linked)
3. Follow-ups Database (Track all interactions)
```

---

## Database 1: Companies

### Properties (Fields)

| Property Name | Type | Options/Format |
|---------------|------|----------------|
| **Company Name** | Title | - |
| **Industry** | Select | Government, Hospitality, Automotive, Events, Real Estate, Co-working, Health, Education, Construction |
| **Company Type** | Select | Hospital, Hotel, Apartment, Office, School, Government Agency, Construction, Real Estate Developer |
| **Contact Person** | Text | Full name |
| **Contact Title** | Text | CEO, MD, Director, Manager, etc. |
| **Email** | Email | - |
| **Phone** | Phone | - |
| **Address** | Text | - |
| **City** | Select | Abuja, Lagos, Kano, Port Harcourt, Kaduna, Other |
| **Website** | URL | - |
| **LinkedIn** | URL | Company or contact LinkedIn |
| **Company Size** | Select | 1-10, 11-50, 51-200, 201-500, 500+ |
| **Lead Source** | Select | Web Research, Referral, Cold Outreach, Event, LinkedIn |
| **Lead Status** | Select | New, Contacted, Interested, Not Interested, Customer |
| **Priority** | Select | High, Medium, Low |
| **Notes** | Text | General notes about company |
| **Proposals** | Relation | → Links to Proposals Database |
| **Created Date** | Created time | Auto |
| **Last Updated** | Last edited time | Auto |

---

## Database 2: Proposals

### Properties (Fields)

| Property Name | Type | Options/Format |
|---------------|------|----------------|
| **Proposal Title** | Title | e.g., "CYFT Facility Health System - Cedar Crest Hospital" |
| **Company** | Relation | → Links to Companies Database |
| **Product/Service** | Select | Spacer (Hospitality), Spacer (Co-working), CYFT Health Inspection, Tracer (Garment), Custom Development, AI Forecasting |
| **Proposal Type** | Select | Initial Proposal, Revised Proposal, Follow-up, Contract |
| **Proposal Value** | Number | Currency (₦) |
| **Status** | Select | Draft, Ready to Send, Sent, Opened, Under Review, Negotiating, Won, Lost, On Hold |
| **Sent?** | Checkbox | ✓ or ✗ |
| **Date Sent** | Date | - |
| **Response Received?** | Checkbox | ✓ or ✗ |
| **Response Date** | Date | - |
| **Client Feedback** | Text | Current feedback/objections |
| **Next Action** | Text | What needs to happen next |
| **Next Action Date** | Date | Deadline for next action |
| **Assigned To** | Person | Team member responsible |
| **Proposal Document** | Files & Media | Attach PDF/DOCX |
| **Follow-ups** | Relation | → Links to Follow-ups Database |
| **Win Probability** | Select | 10%, 25%, 50%, 75%, 90% |
| **Lost Reason** | Select | Price, Timing, Competitor, No Budget, No Response, Other |
| **Contract Signed?** | Checkbox | ✓ or ✗ |
| **Contract Value** | Number | Final contract amount (₦) |
| **Created Date** | Created time | Auto |
| **Last Updated** | Last edited time | Auto |

### Status Workflow

```
Draft → Ready to Send → Sent → Opened → Under Review → Negotiating → Won/Lost/On Hold
```

**Status Colors:**
- Draft = Gray
- Ready to Send = Blue
- Sent = Yellow
- Opened = Orange
- Under Review = Purple
- Negotiating = Pink
- Won = Green
- Lost = Red
- On Hold = Brown

---

## Database 3: Follow-ups

### Properties (Fields)

| Property Name | Type | Options/Format |
|---------------|------|----------------|
| **Follow-up Title** | Title | e.g., "Call - Discussed pricing" |
| **Proposal** | Relation | → Links to Proposals Database |
| **Company** | Rollup | From Proposal → Company |
| **Type** | Select | Email, Phone Call, Meeting, WhatsApp, LinkedIn Message, Site Visit |
| **Date** | Date | When it happened |
| **Direction** | Select | Outbound (we contacted), Inbound (they contacted) |
| **Summary** | Text | Brief description of interaction |
| **Outcome** | Select | Positive, Neutral, Negative, No Response |
| **Next Step** | Text | What to do next |
| **Reminder Date** | Date | When to follow up again |
| **Logged By** | Person | Team member who logged this |
| **Attachments** | Files & Media | Screenshots, recordings, etc. |
| **Created Date** | Created time | Auto |

---

## Views to Create

### Companies Database Views

| View Name | Type | Filter/Sort | Purpose |
|-----------|------|-------------|---------|
| **All Companies** | Table | None | Master list |
| **By Industry** | Board | Group by Industry | Visual industry breakdown |
| **Hot Leads** | Table | Priority = High | Focus on priority prospects |
| **Abuja Companies** | Table | City = Abuja | Location filter |
| **Lagos Companies** | Table | City = Lagos | Location filter |
| **New Leads** | Table | Lead Status = New | Uncontacted prospects |
| **Active Customers** | Table | Lead Status = Customer | Current clients |

### Proposals Database Views

| View Name | Type | Filter/Sort | Purpose |
|-----------|------|-------------|---------|
| **All Proposals** | Table | None | Master list |
| **Pipeline Board** | Board | Group by Status | Visual sales pipeline |
| **Ready to Send** | Table | Status = Ready to Send | Proposals waiting to go out |
| **Awaiting Response** | Table | Sent = ✓, Response = ✗ | Need follow-up |
| **This Week's Actions** | Table | Next Action Date = This Week | Weekly to-do |
| **Won Deals** | Table | Status = Won | Closed deals |
| **Lost Deals** | Table | Status = Lost | Analyze losses |
| **By Product** | Board | Group by Product/Service | Product performance |
| **By Team Member** | Board | Group by Assigned To | Team workload |
| **High Value** | Table | Proposal Value > ₦5M | Big opportunities |

### Follow-ups Database Views

| View Name | Type | Filter/Sort | Purpose |
|-----------|------|-------------|---------|
| **All Follow-ups** | Table | Sort by Date DESC | Activity log |
| **Today's Reminders** | Table | Reminder Date = Today | Daily tasks |
| **This Week** | Calendar | Reminder Date | Weekly calendar |
| **By Type** | Board | Group by Type | Activity breakdown |

---

## Dashboard Setup

Create a **Dashboard Page** with these embedded views:

### Section 1: Key Metrics (Use Notion Formulas or Linked Databases)
```
┌─────────────────────────────────────────────────────────────┐
│  PROPOSAL PIPELINE DASHBOARD                                │
├─────────────┬─────────────┬─────────────┬─────────────────┤
│  Total      │  Sent       │  Won        │  Pipeline Value │
│  Proposals  │  This Month │  This Month │  (Open Deals)   │
│     127     │     23      │      5      │   ₦45,000,000   │
└─────────────┴─────────────┴─────────────┴─────────────────┘
```

### Section 2: Pipeline Board (Embed)
- Embed "Pipeline Board" view from Proposals database

### Section 3: Action Items
- Embed "This Week's Actions" view
- Embed "Today's Reminders" view

### Section 4: Recent Activity
- Embed "All Follow-ups" view (limited to last 10)

---

## Templates

### Proposal Page Template

When you create a new proposal, use this template:

```markdown
# {Proposal Title}

## Company Info
**Company:** {Linked from relation}
**Contact:** {Auto-filled from company}
**Email:** {Auto-filled}
**Phone:** {Auto-filled}

---

## Proposal Details

### Problem Statement
[What problem are we solving for this client?]

### Proposed Solution
[What are we offering?]

### Pricing
| Item | Cost |
|------|------|
| Implementation | ₦X |
| Training | ₦X |
| Support (Annual) | ₦X |
| **Total** | **₦X** |

### Timeline
[Proposed implementation timeline]

---

## Internal Notes

### Client Pain Points
-
-

### Competition
[Who else might they be considering?]

### Decision Makers
[Who needs to approve this?]

### Budget
[Do we know their budget?]

---

## Activity Log
[Linked Follow-ups will appear here]
```

---

## Automation Ideas (Notion Automations or Zapier)

### 1. New Lead Alert
**Trigger:** New company added to Companies database
**Action:** Send Slack/Email notification to sales team

### 2. Follow-up Reminder
**Trigger:** Reminder Date = Today
**Action:** Send notification to assigned person

### 3. Stale Proposal Alert
**Trigger:** Proposal Status = "Sent" AND Last Updated > 7 days ago
**Action:** Send reminder to follow up

### 4. Won Deal Celebration
**Trigger:** Status changed to "Won"
**Action:** Send team notification + add to "Wins" channel

### 5. Weekly Report
**Trigger:** Every Monday 9 AM
**Action:** Generate summary of last week's activities

---

## Quick Setup Steps

### Step 1: Create Databases (15 min)
1. Create "Companies" database with all properties
2. Create "Proposals" database with all properties
3. Create "Follow-ups" database with all properties
4. Link them using Relation properties

### Step 2: Create Views (10 min)
1. Add all views listed above to each database
2. Set up filters and groupings

### Step 3: Create Dashboard (10 min)
1. Create new page called "Proposal Dashboard"
2. Embed key views
3. Add any header/metrics blocks

### Step 4: Import Existing Data (20 min)
1. Import the 20 companies from Abuja_Company_Contacts.md
2. Add any existing proposals

### Step 5: Create Templates (10 min)
1. Create proposal page template
2. Save as default template

---

## Import Your 20 Companies

Copy this data into your Companies database:

| Company Name | Industry | Contact Person | Contact Title | Phone | Email |
|--------------|----------|----------------|---------------|-------|-------|
| PW Nigeria Limited | Construction | Sabau Din | CEO | Website | Website |
| Reynolds Construction Company | Construction | David Amrami | Director of Finance | Directory | - |
| Arab Contractors Nigeria | Construction | Eng. Wael Farouk | Manager | +234 702 984 7612 | - |
| Dantata & Sawoe | Construction | Dantata Nasiru | Executive Director | +234 9 330 0000 | - |
| Quantum Construct Ltd | Construction | Yusuf Abubakar | COO & Founder | Website | - |
| NEJOLE Construction | Construction | - | - | - | - |
| SABC Limited | Construction | Emmanuel Adejo | CEO | Partial | - |
| AG Vision Construction | Construction | Tony Abou Ghazale | CEO | +234 803 595 0491 | info@agvisionconstruction.com |
| Setraco Nigeria | Construction | Michael Hachenberg | MD | +234 806 944 7441 | info@setraco.net |
| Monier Construction | Construction | - | - | Partial | - |
| Constrix Real Estate | Real Estate | Nura Danmusa | CEO | +234 9 290 9176 | - |
| Mshel Homes | Real Estate | Barka Mshelia | CEO | +234 807 491 8900 | - |
| Bilaad Realty | Real Estate | Aliyu Aliyu | CEO | +234 700 222 2111 | info@bilaadnigeria.com |
| Lead Property Mall | Real Estate | - | - | +234 802 056 5929 | - |
| DITTO GROUP | Real Estate | Engr. Bolaji Abayomi | CEO | 0907 722 6258 | - |
| Double J Properties | Real Estate | - | - | Website | - |
| Rotimi Olu & Co | Real Estate | Cosmas Mbarga | CAO | +234 805 399 9228 | - |
| A.A Gulak & Co | Real Estate | - | - | - | - |
| The MLS Properties | Real Estate | - | - | 070-561-44444 | office@themlsproperties.com |
| Ayeye & Co | Real Estate | Victor Ayeye | CEO | +234 803 354 3027 | - |

---

## Success Metrics to Track

### Weekly
- Proposals sent
- Responses received
- Meetings scheduled
- Follow-ups completed

### Monthly
- Total proposals sent
- Win rate (Won / Total Closed)
- Average deal value
- Pipeline value
- Revenue closed

### Q4 Target
- **Goal:** 250 proposals
- **Industries:** 8 (Government, Hospitality, Automotive, Events, Real Estate, Co-working, Health, Education)
- **Track progress** weekly against target

---

## Pro Tips

1. **Use Quick Add** — Pin the Proposals database to your sidebar for fast entry
2. **Keyboard Shortcuts** — Learn Notion shortcuts (Cmd+N, Cmd+P, etc.)
3. **Mobile App** — Log follow-ups immediately after calls
4. **Weekly Review** — Every Friday, review pipeline and plan next week
5. **Templates** — Create templates for each product (Spacer, CYFT, Tracer)
6. **Tags** — Use multi-select for additional categorization if needed

---

**Created by:** Algolog Limited
**For:** Q4 2026 Proposal Management
**Contact:** support@algolog.co
