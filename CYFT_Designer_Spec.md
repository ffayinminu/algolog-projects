# CYFT Facility Health Inspection System
## Designer Specification Document

**Project:** CYFT Facility Health Inspection Platform
**Version:** 1.0
**Date:** January 14, 2026
**Prepared by:** Algolog Limited
**For:** Algolog Design Team

---

## 1. Design Overview

### 1.1 Product Summary
A digital facility health inspection system for healthcare facilities. Inspectors use a mobile app to conduct on-site assessments across 11 categories, then the system generates professional PDF reports with scores, issues, and recommendations.

### 1.2 Design Goals
| Goal | Description |
|------|-------------|
| **Clarity** | Inspectors can quickly understand and complete checklists |
| **Efficiency** | Minimal taps/clicks to complete an inspection |
| **Professionalism** | Reports look polished and trustworthy |
| **Consistency** | Unified visual language across mobile app, dashboard, and reports |

### 1.3 Target Platforms
- **Mobile App:** Android (primary), iOS (secondary)
- **Admin Dashboard:** Web (Chrome, Safari, Edge)
- **Client Portal:** Web (responsive)
- **Reports:** PDF and DOCX output

---

## 2. Brand Guidelines

### 2.1 Color Palette

**Primary Colors:**
| Color | Hex | Usage |
|-------|-----|-------|
| CYFT Blue | #1E3A5F | Headers, primary buttons, branding |
| CYFT Teal | #2AA198 | Secondary actions, accents |
| White | #FFFFFF | Backgrounds, cards |
| Dark Gray | #333333 | Body text |

**Status Colors (Critical for this app):**
| Status | Color | Hex | Background | Usage |
|--------|-------|-----|------------|-------|
| Excellent | Green | #22C55E | #D1FAE5 | Score 90-100 |
| Good | Yellow/Amber | #F59E0B | #FEF3C7 | Score 70-89 |
| Fair | Orange | #F97316 | #FFEDD5 | Score 50-69 |
| Critical | Red | #EF4444 | #FEE2E2 | Score 0-49 |

**Priority Badge Colors:**
| Priority | Text Color | Background | Usage |
|----------|------------|------------|-------|
| HIGH | White | #F97316 (Orange) | Urgent attention needed |
| MEDIUM | Black | #FCD34D (Yellow) | Standard priority |
| LOW | White | #22C55E (Green) | Minor/routine items |

**Supporting Colors:**
| Color | Hex | Usage |
|-------|-----|-------|
| Light Gray | #F5F5F5 | Backgrounds, dividers |
| Medium Gray | #9CA3AF | Placeholder text, icons |
| Success | #10B981 | Completed states |
| Warning | #FBBF24 | Attention needed |
| Error | #DC2626 | Errors, critical issues |

---

### 2.2 Typography

**Mobile App:**
| Element | Font | Size | Weight |
|---------|------|------|--------|
| Screen Title | Inter | 24px | Bold |
| Section Header | Inter | 18px | SemiBold |
| Body Text | Inter | 16px | Regular |
| Caption/Label | Inter | 14px | Regular |
| Small Text | Inter | 12px | Regular |

**Dashboard/Web:**
| Element | Font | Size | Weight |
|---------|------|------|--------|
| Page Title | Inter | 32px | Bold |
| Section Header | Inter | 24px | SemiBold |
| Card Title | Inter | 18px | Medium |
| Body Text | Inter | 16px | Regular |
| Table Text | Inter | 14px | Regular |

**Reports (PDF):**
| Element | Font | Size | Weight |
|---------|------|------|--------|
| Report Title | Arial | 28pt | Bold |
| Section Header | Arial | 18pt | Bold |
| Subsection | Arial | 14pt | Bold |
| Body Text | Arial | 11pt | Regular |
| Table Text | Arial | 10pt | Regular |
| Footer | Arial | 9pt | Regular |

---

### 2.3 Iconography

**Icon Style:** Outlined, 2px stroke, rounded corners

**Category Icons (use consistent icon set):**
| Category | Icon Suggestion |
|----------|-----------------|
| Generator | Lightning bolt / Power |
| HVAC | Snowflake / AC unit |
| Medical Equipment | Heart monitor / Stethoscope |
| Water Systems | Water droplet |
| Electrical | Plug / Circuit |
| Plumbing | Pipe / Wrench |
| Medical Waste | Biohazard symbol |
| Fire Safety | Fire extinguisher / Flame |
| Pest Control | Bug / Ant |
| Cleanliness | Sparkle / Broom |
| General Maintenance | Tool / Wrench |

**Status Icons:**
| Status | Icon | Color |
|--------|------|-------|
| Excellent | Checkmark in circle | Green |
| Good | Checkmark | Yellow |
| Fair | Warning triangle | Orange |
| Critical | X in circle | Red |

---

## 3. Mobile App Design

### 3.1 Screen Flow

```
[Login] → [Dashboard] → [Inspection List] → [Select Inspection]
                                                    ↓
                                            [Facility Info]
                                                    ↓
                                            [Category 1: Generator]
                                                    ↓
                                            [Category 2: HVAC]
                                                    ↓
                                                  ...
                                                    ↓
                                            [Category 11: Maintenance]
                                                    ↓
                                            [Summary & Review]
                                                    ↓
                                            [Submit Confirmation]
```

---

### 3.2 Screen Specifications

#### **Screen 1: Login**

**Layout:**
- CYFT logo (centered, top 30%)
- Email input field
- Password input field
- "Login" button (primary)
- "Forgot Password?" link

**Design Notes:**
- Full-screen gradient background (CYFT Blue to Teal)
- White card for form inputs
- Logo should be prominent

---

#### **Screen 2: Dashboard**

**Layout:**
- Header: "My Inspections" + Profile icon
- Quick stats row:
  - Pending inspections count
  - Completed this month
  - Average score
- Upcoming inspections list (card format)
- "Start New Inspection" floating action button

**Card Design (Inspection Card):**
```
┌─────────────────────────────────────────┐
│  [Hospital Icon] Cedar Crest Hospital   │
│  📍 Abuja, FCT                          │
│  📅 Jan 15, 2026 · 10:00 AM             │
│  Status: [Scheduled] ───────────────────│
│                          [Start →]      │
└─────────────────────────────────────────┘
```

---

#### **Screen 3: Facility Information**

**Layout:**
- Header: "Facility Details" + Back arrow
- Form fields (vertical stack):
  - Hospital/Clinic Name (text input)
  - Address (text area)
  - Contact Person (text input)
  - Contact Phone (phone input)
  - Inspection Date (date picker)
  - Inspector Name (auto-filled, read-only)
- "Continue to Inspection" button

**Design Notes:**
- Use floating labels for inputs
- Auto-save indicator ("Saved" badge)
- Validation on required fields

---

#### **Screen 4: Category Checklist**

**This is the core screen — used 11 times (one per category)**

**Layout:**
```
┌─────────────────────────────────────────┐
│  ← Generator Health           1/11      │
│  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ │
│  Max Points: 50                         │
├─────────────────────────────────────────┤
│                                         │
│  ▼ 1. Load Testing (15 pts)             │
│  ┌─────────────────────────────────────┐│
│  │ ☐ Run generator at 100% capacity   ││
│  │ ☐ Check voltage output (220-240V)  ││
│  │ ☐ Monitor frequency stability      ││
│  │ ☐ Observe for unusual vibrations   ││
│  │ ☐ Check exhaust temperature        ││
│  │ ☐ Test automatic transfer switch   ││
│  │                                     ││
│  │ Checkpoints: 0/6 · Points: 0/15    ││
│  │                                     ││
│  │ Notes: [________________]           ││
│  │ Cost: ₦ [__________]                ││
│  │ [📷 Add Photo]                      ││
│  └─────────────────────────────────────┘│
│                                         │
│  ▶ 2. Oil Quality (10 pts)              │
│  ▶ 3. Battery Condition (10 pts)        │
│  ▶ 4. Fuel System (10 pts)              │
│  ▶ 5. Maintenance Records (5 pts)       │
│                                         │
├─────────────────────────────────────────┤
│  Category Score: 0/100                  │
│  Status: [Select Status ▼]              │
│                                         │
│  [← Previous]          [Next →]         │
└─────────────────────────────────────────┘
```

**Design Elements:**

**Checkbox Style:**
- Unchecked: Empty square with gray border
- Checked: Filled square with checkmark (CYFT Blue)
- Size: 24x24px with 16px touch padding

**Collapsible Sections:**
- Accordion-style for each inspection item
- Expand/collapse with smooth animation
- Show summary when collapsed (e.g., "4/6 checkpoints passed")

**Score Calculation:**
- Auto-calculate as checkpoints are checked
- Display: "Checkpoints: 4/6 · Points: 10/15"
- Color-code based on percentage

**Photo Button:**
- Opens camera directly
- Shows thumbnail preview after capture
- Allow multiple photos per item
- Swipe to delete photos

**Status Dropdown:**
- Options: Excellent (green), Good (yellow), Fair (orange), Critical (red)
- Show color indicator next to selected status

---

#### **Screen 5: Photo Capture**

**Layout:**
- Full-screen camera view
- Capture button (bottom center)
- Flash toggle (top right)
- Gallery access (bottom left)
- Close button (top left)

**After Capture:**
- Preview image
- "Retake" and "Use Photo" buttons
- Caption input field
- "Save" button

---

#### **Screen 6: Summary & Review**

**Layout:**
```
┌─────────────────────────────────────────┐
│  ← Inspection Summary                   │
├─────────────────────────────────────────┤
│  Overall Score: 77/100                  │
│  [████████████░░░░]                     │
│  Status: 🟡 GOOD                        │
├─────────────────────────────────────────┤
│  Category Breakdown:                    │
│  ┌───────────────────────────────────┐  │
│  │ ⚡ Generator        85/100  🟡    │  │
│  │ ❄️ HVAC             70/100  🟡    │  │
│  │ 🏥 Equipment Env    80/100  🟡    │  │
│  │ 💧 Water Systems    65/100  🟠    │  │
│  │ ⚡ Electrical       58/100  🔴    │  │
│  │ 🚰 Plumbing         60/100  🟠    │  │
│  │ ☣️ Waste Mgmt       90/100  🟢    │  │
│  │ 🔥 Fire Safety      55/100  🟠    │  │
│  │ 🐜 Pest Control     85/100  🟡    │  │
│  │ 🧹 Cleanliness      95/100  🟢    │  │
│  │ 🔧 Maintenance      68/100  🟠    │  │
│  └───────────────────────────────────┘  │
├─────────────────────────────────────────┤
│  Critical Issues:                       │
│  1. Electrical panel overheating        │
│  2. 3 fire extinguishers expired        │
│  3. Low water pressure (2nd floor)      │
├─────────────────────────────────────────┤
│  Total Repair Costs: ₦1,245,000         │
├─────────────────────────────────────────┤
│  Photos: 47 captured                    │
├─────────────────────────────────────────┤
│  [Submit Inspection]                    │
└─────────────────────────────────────────┘
```

**Design Notes:**
- Large, prominent overall score
- Progress bar with gradient (red → yellow → green)
- Tappable category rows to edit
- Critical issues highlighted in red box
- Submit button is primary action

---

#### **Screen 7: Submit Confirmation**

**Layout:**
- Success animation (checkmark animation)
- "Inspection Submitted!" message
- Summary card (facility, date, score)
- "View Report" button
- "Return to Dashboard" button

---

### 3.3 Mobile UI Components

#### **Buttons**

**Primary Button:**
- Background: CYFT Blue (#1E3A5F)
- Text: White, 16px, SemiBold
- Height: 48px
- Border radius: 8px
- Full width on mobile

**Secondary Button:**
- Background: White
- Border: 1px CYFT Blue
- Text: CYFT Blue, 16px, SemiBold
- Height: 48px
- Border radius: 8px

**Floating Action Button (FAB):**
- Background: CYFT Teal
- Icon: White, 24px
- Size: 56px diameter
- Shadow: 0 4px 12px rgba(0,0,0,0.15)

---

#### **Input Fields**

**Text Input:**
- Height: 48px
- Border: 1px #E5E5E5
- Border radius: 8px
- Padding: 12px 16px
- Focus state: 2px CYFT Blue border
- Error state: 2px red border + error message below

**Text Area:**
- Min height: 80px
- Same styling as text input
- Expandable

**Dropdown/Select:**
- Same styling as text input
- Chevron icon on right
- Opens bottom sheet on mobile

---

#### **Cards**

**Standard Card:**
- Background: White
- Border radius: 12px
- Shadow: 0 2px 8px rgba(0,0,0,0.08)
- Padding: 16px

**Category Card:**
- Same as standard card
- Left border accent (4px, status color)
- Icon on left (category icon)

---

#### **Progress Indicators**

**Linear Progress Bar:**
- Height: 8px
- Background: #E5E5E5
- Fill: Gradient based on score (red → yellow → green)
- Border radius: 4px

**Circular Progress:**
- For overall score display
- Large: 120px diameter
- Stroke width: 8px
- Score number in center

**Step Indicator:**
- For category navigation (1/11, 2/11, etc.)
- Dots or numbered steps
- Completed steps filled, current highlighted

---

### 3.4 Animations & Transitions

**Screen Transitions:**
- Slide left/right for forward/back navigation
- Duration: 300ms
- Easing: ease-out

**Checkbox Animation:**
- Scale up on check (1.0 → 1.2 → 1.0)
- Checkmark draws in
- Duration: 200ms

**Score Updates:**
- Number counts up/down smoothly
- Progress bar animates
- Duration: 400ms

**Success Animation:**
- Checkmark draws in circular path
- Confetti effect (optional)
- Duration: 800ms

---

## 4. Admin Dashboard Design

### 4.1 Layout Structure

**Sidebar Navigation:**
```
┌──────────────────┐
│  CYFT Logo       │
├──────────────────┤
│  📊 Dashboard    │
│  🏥 Facilities   │
│  📋 Inspections  │
│  📄 Reports      │
│  👥 Users        │
│  ⚙️ Settings     │
├──────────────────┤
│  👤 Profile      │
│  🚪 Logout       │
└──────────────────┘
```

**Main Content Area:**
- Header with page title and actions
- Content cards/tables
- Responsive: sidebar collapses on tablet

---

### 4.2 Dashboard Screen

**Layout:**
```
┌─────────────────────────────────────────────────────────────────┐
│  Dashboard                                      [+ New Inspection]│
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  ┌──────────────┐ ┌──────────────┐ ┌──────────────┐ ┌──────────┐│
│  │ Total        │ │ This Month   │ │ Pending      │ │ Avg Score││
│  │ Facilities   │ │ Inspections  │ │ Reports      │ │          ││
│  │    45        │ │     12       │ │      3       │ │   78%    ││
│  │ +3 this mo   │ │ ↑ 20% vs LM  │ │              │ │ ↑ 5%     ││
│  └──────────────┘ └──────────────┘ └──────────────┘ └──────────┘│
│                                                                  │
│  ┌────────────────────────────────┐ ┌────────────────────────┐  │
│  │ Recent Inspections             │ │ Score Distribution     │  │
│  │                                │ │                        │  │
│  │ • Cedar Crest - 77/100 - Jan 12│ │    [PIE CHART]         │  │
│  │ • Unity Hospital - 85/100 - Jan│ │                        │  │
│  │ • Grace Clinic - 62/100 - Jan 8│ │  🟢 Excellent: 15%     │  │
│  │ • Hope Medical - 91/100 - Jan 5│ │  🟡 Good: 55%          │  │
│  │                                │ │  🟠 Fair: 25%          │  │
│  │ [View All →]                   │ │  🔴 Critical: 5%       │  │
│  └────────────────────────────────┘ └────────────────────────┘  │
│                                                                  │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │ Upcoming Inspections                                      │   │
│  │ ┌─────────────────────────────────────────────────────┐  │   │
│  │ │ Cedar Crest Hospital │ Jan 15, 10AM │ Ibrahim │ [→] │  │   │
│  │ │ Unity Medical Center │ Jan 16, 2PM  │ Chidi   │ [→] │  │   │
│  │ │ Grace Clinic         │ Jan 17, 9AM  │ Ibrahim │ [→] │  │   │
│  │ └─────────────────────────────────────────────────────┘  │   │
│  └──────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────┘
```

---

### 4.3 Inspection Details Screen

**Layout:**
```
┌─────────────────────────────────────────────────────────────────┐
│  ← Back to Inspections                                          │
│                                                                  │
│  Cedar Crest Hospital                                           │
│  Inspection: January 12, 2026                                   │
│  Inspector: Ibrahim Yusuf                                       │
│                                                                  │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │  OVERALL SCORE                                            │   │
│  │                                                           │   │
│  │         ┌───────────────┐                                │   │
│  │         │      77       │  🟡 GOOD                       │   │
│  │         │    /100       │                                │   │
│  │         └───────────────┘                                │   │
│  │                                                           │   │
│  │  Critical Repairs: ₦115,000                               │   │
│  │  Total Recommendations: ₦605,000                          │   │
│  └──────────────────────────────────────────────────────────┘   │
│                                                                  │
│  Category Scores                                                 │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │ Category          │ Score  │ Status │ Cost    │ Actions │   │
│  ├───────────────────┼────────┼────────┼─────────┼─────────┤   │
│  │ Generator         │ 85/100 │ 🟡     │ ₦20,000 │ [View]  │   │
│  │ HVAC              │ 70/100 │ 🟡     │ ₦70,000 │ [View]  │   │
│  │ Electrical        │ 58/100 │ 🔴     │ ₦32,000 │ [View]  │   │
│  │ ...               │        │        │         │         │   │
│  └──────────────────────────────────────────────────────────┘   │
│                                                                  │
│  [Download PDF Report]  [Download DOCX]  [Email to Client]      │
└─────────────────────────────────────────────────────────────────┘
```

---

### 4.4 Report Preview Screen

**Layout:**
- Full-width preview of generated report
- Toolbar: Download PDF, Download DOCX, Print, Email
- Editable mode toggle (for corrections)
- Side panel with export options

---

## 5. Report Design (PDF Output)

### 5.1 Report Layout

**Page Size:** A4 (210 x 297 mm)
**Margins:** 25mm all sides
**Header Height:** 30mm
**Footer Height:** 15mm

---

### 5.2 Cover Page / First Page

```
┌─────────────────────────────────────────────────────────────┐
│                                                              │
│  Cedar Crest Hospital, Abuja - FACILITY HEALTH REPORT       │
│  (Blue header bar, white text, bold)                         │
│                                                              │
│              Overall Health Score: 80/100                    │
│              (Large, blue text, centered)                    │
│                                                              │
│  ─────────────────────────────────────────────────────────  │
│                                                              │
│  ENHANCED CATEGORY PERFORMANCE OVERVIEW                      │
│  (Section header, bold)                                      │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

### 5.3 Enhanced Category Performance Overview Table

**This is the primary report table - design must match PDF exactly**

```
┌──────────────┬────────┬────────┬────────┬─────────┬──────────┬─────────┐
│   Category   │ Score  │ Status │ Issues │ Repair  │ Priority │  Last   │
│              │        │        │ Found  │ Costs   │          │ Service │
├──────────────┼────────┼────────┼────────┼─────────┼──────────┼─────────┤
│ Generator    │ 82/100 │ 🟡GOOD │ 2      │ ₦80,000 │ MEDIUM   │ Over 30 │
│ Health       │        │        │ issues │         │          │ days    │
├──────────────┼────────┼────────┼────────┼─────────┼──────────┼─────────┤
│ HVAC         │ 70/100 │ 🟡GOOD │ 3      │₦340,000 │ MEDIUM   │ Over 30 │
│ Systems      │        │        │ issues │         │          │ days    │
├──────────────┼────────┼────────┼────────┼─────────┼──────────┼─────────┤
│ Fire Safety  │ 67/100 │ 🟠FAIR │ 3      │₦160,000 │ HIGH     │ Over 30 │
│              │        │        │ issues │         │          │ days    │
├──────────────┼────────┼────────┼────────┼─────────┼──────────┼─────────┤
│ Medical      │ 96/100 │🟢EXCEL │ None   │ ₦8,000  │ LOW      │ Over 30 │
│ Waste Mgmt   │        │  LENT  │        │         │          │ days    │
├──────────────┴────────┴────────┼────────┼─────────┼──────────┴─────────┤
│              TOTAL:            │ 15     │₦1,284,  │   All Categories   │
│                                │ total  │   000   │                    │
└────────────────────────────────┴────────┴─────────┴────────────────────┘
```

**Table Design Specifications:**

| Element | Specification |
|---------|---------------|
| Header Row | Blue background (#1E88E5), white text, bold |
| Status Cell | Colored background based on status (see Status Colors) |
| Priority Badge | Rounded pill shape, colored background |
| Score Column | Black text, format "XX/100" |
| Cost Column | Right-aligned, Naira symbol (₦) |
| TOTAL Row | Light gray background, bold text |
| Cell Padding | 12px vertical, 8px horizontal |
| Border | Light gray (#E5E5E5), 1px |
| Row Height | Minimum 48px |

**Status Badge Design:**
```
┌─────────────────┐
│ 🟡              │  Yellow background (#FEF3C7)
│ GOOD            │  Text: Bold, centered
└─────────────────┘

┌─────────────────┐
│ 🟢              │  Green background (#D1FAE5)
│ EXCELLENT       │  Text: Bold, centered
└─────────────────┘

┌─────────────────┐
│ 🟠              │  Orange background (#FFEDD5)
│ FAIR            │  Text: Bold, centered
└─────────────────┘
```

**Priority Badge Design:**
```
┌──────────┐
│  HIGH    │  Orange background, white text, rounded corners (4px)
└──────────┘

┌──────────┐
│ MEDIUM   │  Yellow background, black text, rounded corners (4px)
└──────────┘

┌──────────┐
│  LOW     │  Green background, white text, rounded corners (4px)
└──────────┘
```

---

### 5.4 Key Insights Section

**Placed immediately after the category table**

```
┌─────────────────────────────────────────────────────────────┐
│  KEY INSIGHTS                                                │
│  (Bold header)                                               │
│                                                              │
│  • Total repair/maintenance budget required: ₦1,284,000     │
│  • Categories requiring immediate attention: 0               │
│  • Highest cost category: HVAC Systems                       │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

**Design:**
- Bullet points with standard spacing
- Bold numbers/values for emphasis
- 16px padding all around
- Light background optional (#F9FAFB)

---

### 5.5 Executive Summary Page (Detailed Reports)

```
┌─────────────────────────────────────────────────────────────┐
│  EXECUTIVE SUMMARY                                           │
│  ───────────────────────────────────────────────────────────│
│                                                              │
│  This comprehensive facility health assessment was conducted │
│  on [DATE] at [FACILITY NAME]. The inspection evaluated 10  │
│  critical facility management categories.                    │
│                                                              │
│  ┌─────────────────────────────────────────────────────────┐│
│  │ Category Performance Overview                            ││
│  ├──────────────────────────┬─────────┬────────────────────┤│
│  │ Category                 │ Score   │ Status             ││
│  ├──────────────────────────┼─────────┼────────────────────┤│
│  │ Generator                │ 85/100  │ 🟡 Good            ││
│  │ HVAC                     │ 70/100  │ 🟡 Good            ││
│  │ Water Systems            │ 65/100  │ 🟠 Fair            ││
│  │ Electrical               │ 58/100  │ 🔴 Critical        ││
│  │ ...                      │         │                    ││
│  └──────────────────────────┴─────────┴────────────────────┘│
│                                                              │
│  ┌─────────────────────────────────────────────────────────┐│
│  │ 🔴 CRITICAL ISSUES REQUIRING IMMEDIATE ATTENTION        ││
│  │                                                          ││
│  │ 1. Three fire extinguishers expired - ₦45,000           ││
│  │ 2. Electrical panel overheating - ₦120,000              ││
│  │ 3. Two toilets running water - ₦40,000                  ││
│  │                                                          ││
│  │ Total Critical Repairs: ₦205,000                        ││
│  └─────────────────────────────────────────────────────────┘│
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

---

### 5.4 Category Detail Page

```
┌─────────────────────────────────────────────────────────────┐
│  1. GENERATOR HEALTH                                         │
│  ───────────────────────────────────────────────────────────│
│                                                              │
│  ┌──────────────────────────────┐                           │
│  │ SCORE: 85/100  🟡 GOOD       │                           │
│  └──────────────────────────────┘                           │
│                                                              │
│  Issues Found:                                               │
│  • Oil slightly dark                                         │
│  • Battery terminals have minor corrosion                    │
│                                                              │
│  Detailed Notes:                                             │
│  Generator is in good operational condition. Load test       │
│  passed successfully. Oil level adequate but color indicates │
│  it's nearing change interval. Battery voltage at 12.6V     │
│  which is acceptable. No fuel leaks detected.               │
│                                                              │
│  Recommendations:                                            │
│  ┌─────────────────────────────────────────────────────────┐│
│  │ Item                              │ Estimated Cost       ││
│  ├───────────────────────────────────┼──────────────────────┤│
│  │ Oil change                        │ ₦15,000              ││
│  │ Battery terminal cleaning         │ ₦5,000               ││
│  ├───────────────────────────────────┼──────────────────────┤│
│  │ Category Total                    │ ₦20,000              ││
│  └───────────────────────────────────┴──────────────────────┘│
│                                                              │
│  [PHOTO THUMBNAIL]  [PHOTO THUMBNAIL]                       │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

---

### 5.5 Financial Summary Page

```
┌─────────────────────────────────────────────────────────────┐
│  FINANCIAL BREAKDOWN                                         │
│  ───────────────────────────────────────────────────────────│
│                                                              │
│  ┌─────────────────────────────────────────────────────────┐│
│  │ Category               │ Est. Cost  │ % of Total │ Pri  ││
│  ├────────────────────────┼────────────┼────────────┼──────┤│
│  │ HVAC Systems           │ ₦340,000   │ 27.3%      │ MED  ││
│  │ Electrical Systems     │ ₦220,000   │ 17.7%      │ URG  ││
│  │ Fire Safety            │ ₦160,000   │ 12.9%      │ HIGH ││
│  │ ...                    │            │            │      ││
│  ├────────────────────────┼────────────┼────────────┼──────┤│
│  │ TOTAL                  │ ₦1,245,000 │ 100%       │      ││
│  └────────────────────────┴────────────┴────────────┴──────┘│
│                                                              │
│  Priority Breakdown:                                         │
│  • URGENT (Within 7 days): ₦420,000 (34%)                   │
│  • HIGH (This Month): ₦560,000 (45%)                        │
│  • MEDIUM (This Quarter): ₦265,000 (21%)                    │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

---

### 5.6 Report Footer

```
┌─────────────────────────────────────────────────────────────┐
│  CYFT Consulting Limited | info@cyftconsulting.com | Page X │
└─────────────────────────────────────────────────────────────┘
```

---

## 6. Design Assets Required

### 6.1 Icons (SVG)
- [ ] 11 category icons
- [ ] 4 status icons (Excellent, Good, Fair, Critical)
- [ ] Navigation icons (back, menu, settings, etc.)
- [ ] Action icons (camera, upload, download, print, email)
- [ ] Form icons (checkbox, radio, dropdown)

### 6.2 Illustrations
- [ ] Empty state illustration (no inspections)
- [ ] Success illustration (inspection submitted)
- [ ] Error illustration (something went wrong)
- [ ] Onboarding illustrations (3-4 screens)

### 6.3 Logo Variations
- [ ] CYFT full logo (horizontal)
- [ ] CYFT icon only (for app icon, favicon)
- [ ] CYFT white version (for dark backgrounds)

### 6.4 Report Templates
- [ ] Cover page design
- [ ] Executive summary layout
- [ ] Category detail layout
- [ ] Financial summary layout
- [ ] Action plan layout

---

## 7. Responsive Breakpoints

| Device | Width | Layout |
|--------|-------|--------|
| Mobile | < 768px | Single column, bottom nav |
| Tablet | 768-1024px | Sidebar collapsed, 2 columns |
| Desktop | > 1024px | Full sidebar, 3+ columns |

---

## 8. Accessibility Requirements

- Minimum touch target: 44x44px
- Color contrast ratio: 4.5:1 minimum
- All images have alt text
- Form fields have proper labels
- Status conveyed by icon + color + text (not color alone)
- Screen reader compatible

---

## 9. Deliverables Checklist

### Mobile App
- [ ] Login screen design
- [ ] Dashboard screen design
- [ ] Facility information form
- [ ] Category checklist screen (template)
- [ ] Photo capture flow
- [ ] Summary screen
- [ ] Success/confirmation screen
- [ ] All component specifications

### Admin Dashboard
- [ ] Dashboard overview
- [ ] Facilities list and detail
- [ ] Inspections list and detail
- [ ] Report preview and export
- [ ] User management
- [ ] Settings

### Reports
- [ ] Cover page template
- [ ] All page layouts
- [ ] Table styles
- [ ] Chart styles

### Assets
- [ ] Icon set (SVG)
- [ ] Illustrations
- [ ] Logo variations
- [ ] Style guide document

---

**Prepared by:** Algolog Limited
**For:** CYFT Consulting Limited
**Contact:** support@algolog.co
