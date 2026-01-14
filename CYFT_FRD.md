# CYFT Facility Health Inspection System
## Functional Requirements Document (FRD)

**Project:** CYFT Facility Health Inspection Platform
**Version:** 1.0
**Date:** January 14, 2026
**Prepared by:** Algolog Limited
**Client:** CYFT Consulting Limited

---

## 1. Executive Summary

### 1.1 Purpose
This document defines the functional requirements for a digital Facility Health Inspection System designed for CYFT Consulting. The system enables facility managers and inspectors to conduct comprehensive health assessments of healthcare facilities (hospitals, clinics) and generate professional reports with scores, recommendations, and cost estimates.

### 1.2 Scope
The system covers:
- Digital inspection checklists for 11 facility categories
- Point-based scoring system (0-100 per category)
- Automated report generation with financial analysis
- Photo documentation management
- Historical tracking and trend analysis
- Multi-user access for inspectors and administrators

### 1.3 Target Users
| User Type | Description |
|-----------|-------------|
| Inspector | Field technician who conducts on-site inspections |
| Administrator | CYFT staff who manage inspections and generate reports |
| Client (Facility Manager) | Receives reports and tracks facility health over time |

---

## 2. System Overview

### 2.1 Business Context
CYFT Consulting provides facility management services to healthcare institutions in Nigeria. The current process uses paper checklists and manual report generation. This system will digitize the entire workflow to improve efficiency, accuracy, and client experience.

### 2.2 System Components
1. **Mobile Inspection App** — For on-site data collection
2. **Admin Dashboard** — For report generation and management
3. **Client Portal** — For clients to view reports and track progress
4. **Report Generator** — Automated PDF/Word report creation

---

## 3. Functional Requirements

### 3.1 Inspection Categories

The system must support 11 inspection categories:

| # | Category | Max Points | Checkpoints |
|---|----------|------------|-------------|
| 1 | Generator Health | 50 | 30 |
| 2 | HVAC/AC Systems | 60 | 26 |
| 3 | Medical Equipment Environment | 40 | 24 |
| 4 | Water Systems | 50 | 30 |
| 5 | Electrical Systems | 60 | 36 |
| 6 | Plumbing & Drainage | 50 | 30 |
| 7 | Medical Waste Management | 50 | 30 |
| 8 | Fire Safety | 50 | 31 |
| 9 | Pest Control | 20 | 24 |
| 10 | Cleanliness & Hygiene | 20 | 27 |
| 11 | General Maintenance | 30 | 28 |
| **TOTAL** | | **480** | **316** |

---

### 3.2 Facility Information Module

**FR-3.2.1** System shall capture the following facility details:
- Hospital/Clinic Name (required)
- Full Address including city (required)
- Contact Person name (required)
- Contact Phone number (required)
- Inspection Date (required, format: DD/MM/YYYY)
- Inspector Name (required)

**FR-3.2.2** System shall store facility records for historical tracking.

**FR-3.2.3** System shall allow editing of facility information by authorized users.

---

### 3.3 Inspection Checklist Module

**FR-3.3.1** For each category, the system shall display:
- Category name and maximum points
- List of inspection items with checkpoints
- Checkbox for each checkpoint (Pass/Fail)
- Notes field for issues found
- Photo upload capability
- Estimated repair cost field (in Naira)

**FR-3.3.2** Each inspection item shall include:
- Item name (e.g., "Load Testing Performance")
- Maximum points for the item
- 4-8 specific checkpoints to verify
- Scoring calculation: `(Checkpoints Passed / Total Checkpoints) × Max Points`

**FR-3.3.3** System shall auto-calculate points awarded based on checkpoints passed.

**FR-3.3.4** System shall support the following data entry for each category:
- Score (0-10 scale, converted to 0-100)
- Status (Excellent / Good / Fair / Critical)
- Issues Found (text, semicolon-separated for multiple)
- Issues Count (auto-calculated from Issues Found)
- Detailed Notes (free text)
- Recommendations with costs (format: "Action - Cost")
- Photo filename reference
- Priority Level (HIGH / MEDIUM / LOW)
- Last Service Date (auto-categorized as "Within 30 days" or "Over 30 days")

---

### 3.4 Scoring System

**FR-3.4.1** System shall calculate scores using the following formula:
```
Category Score = (Total Points Awarded / Maximum Points) × 100
```

**FR-3.4.2** System shall assign status based on score:
| Score Range | Status | Color Code |
|-------------|--------|------------|
| 90-100 | Excellent | Green |
| 70-89 | Good | Yellow |
| 50-69 | Fair | Orange |
| 0-49 | Critical | Red |

**FR-3.4.3** System shall calculate Overall Facility Health Score:
```
Overall Score = Average of all 11 category scores
```

**FR-3.4.4** System shall identify and flag critical issues:
- Any category with score < 50 = Critical
- Any safety violation (Fire, Electrical) = Urgent Priority

---

### 3.5 Photo Documentation Module

**FR-3.5.1** System shall allow photo uploads for each category (minimum 3, maximum 10 per category).

**FR-3.5.2** System shall support common image formats: JPG, PNG, HEIC.

**FR-3.5.3** System shall auto-generate filenames: `[facility]_[category]_[date]_[number].jpg`

**FR-3.5.4** System shall allow photo captions/descriptions.

**FR-3.5.5** System shall compress images for storage optimization while maintaining quality for reports.

---

### 3.6 Report Generation Module

**FR-3.6.1** System shall generate the following report types:
| Report Type | Description | Format |
|-------------|-------------|--------|
| Standard Report | Basic scores and recommendations | PDF/DOCX |
| Detailed Analysis | Full financial breakdown with ROI | PDF/DOCX |
| Executive Summary | 1-page overview for management | PDF |

**FR-3.6.2** Standard Report shall include:
- Executive Summary with overall score
- Enhanced Category Performance Overview table with columns:
  - Category name
  - Score (X/100)
  - Status (color-coded badge)
  - Issues Found (count)
  - Repair Costs (in Naira)
  - Priority (HIGH/MEDIUM/LOW badge)
  - Last Service (Within 30 days / Over 30 days)
- TOTAL row showing aggregate issues count and total costs
- Key Insights section with:
  - Total repair/maintenance budget required
  - Categories requiring immediate attention (count)
  - Highest cost category
- Critical issues section (highlighted)
- Detailed findings for each category (score, issues, notes, recommendations)
- Cost summary (Critical repairs + Total recommendations)
- Next steps and follow-up schedule
- Photo documentation (selected images)

**FR-3.6.3** Detailed Analysis Report shall additionally include:
- Financial breakdown by category (table format)
- Cost of inaction analysis (risk vs investment)
- ROI calculations for recommended repairs
- Month-over-month comparison (if previous data exists)
- Prioritized action plan (Week 1, Month 1, Quarter 1)
- Maintenance schedule recommendations
- Insurance and compliance considerations
- Vendor contact recommendations

**FR-3.6.4** Report shall include visual elements:
- Color-coded status indicators (emojis or icons)
- Score tables with category breakdown
- Priority badges (URGENT, HIGH, MEDIUM, LOW)

**FR-3.6.5** Report shall be branded with CYFT Consulting logo and contact information.

---

### 3.7 Critical Issues Tracking

**FR-3.7.1** System shall capture top 3 critical issues:
- Issue description
- Estimated cost to fix
- Priority level

**FR-3.7.2** System shall auto-calculate:
- Total Critical Repairs Cost (sum of top 3)
- Total All Recommendations Cost (sum across all categories)

**FR-3.7.3** System shall flag issues by timeline:
- Immediate (Within 7 days)
- Short-term (Within 30 days)
- Long-term (Within 90 days)

---

### 3.8 User Management

**FR-3.8.1** System shall support the following user roles:
| Role | Permissions |
|------|-------------|
| Super Admin | Full access, user management, system settings |
| Admin | Create/edit inspections, generate reports, view all facilities |
| Inspector | Create/edit assigned inspections, limited report access |
| Client | View own facility reports (read-only) |

**FR-3.8.2** System shall track inspector assignment per inspection.

**FR-3.8.3** System shall log all user actions for audit trail.

---

### 3.9 Notifications

**FR-3.9.1** System shall send email notifications for:
- Inspection scheduled (to facility contact)
- Inspection completed (to facility contact)
- Report ready for download (to facility contact)
- Follow-up reminders (to admin and facility)

**FR-3.9.2** System shall send SMS notifications (optional):
- Inspection appointment reminder (24 hours before)
- Report ready notification

---

### 3.10 Historical Data & Analytics

**FR-3.10.1** System shall store all inspection data for historical comparison.

**FR-3.10.2** System shall display trends:
- Score improvement/decline over time
- Cost trends (increasing/decreasing)
- Issue count trends
- Category-by-category progress

**FR-3.10.3** System shall generate comparative reports:
- Current vs Previous inspection
- Quarterly/Annual summary reports

---

## 4. Data Requirements

### 4.1 Data Model Overview

**Facilities Table:**
- facility_id (PK)
- name
- address
- contact_person
- contact_phone
- contact_email
- created_at
- updated_at

**Inspections Table:**
- inspection_id (PK)
- facility_id (FK)
- inspector_id (FK)
- inspection_date
- status (Draft / Completed / Approved)
- overall_score
- overall_status
- created_at
- updated_at

**Category Scores Table:**
- score_id (PK)
- inspection_id (FK)
- category_name
- score (0-100)
- status (Excellent/Good/Fair/Critical)
- issues_found (text)
- issues_count (integer, auto-calculated)
- detailed_notes (text)
- recommendations (text)
- estimated_cost (numeric)
- priority (HIGH/MEDIUM/LOW)
- last_service_date (date)
- last_service_status (Within 30 days / Over 30 days, auto-calculated)
- photo_filenames (text array)

**Critical Issues Table:**
- issue_id (PK)
- inspection_id (FK)
- issue_description
- estimated_cost
- priority (1, 2, 3)

**Users Table:**
- user_id (PK)
- name
- email
- phone
- role
- password_hash
- created_at

---

### 4.2 Data Entry Template Fields

| Field | Type | Required | Format/Options |
|-------|------|----------|----------------|
| Hospital/Clinic Name | Text | Yes | Free text |
| Address | Text | Yes | Free text |
| Contact Person | Text | Yes | Free text |
| Contact Phone | Text | Yes | Phone format |
| Inspection Date | Date | Yes | DD/MM/YYYY |
| Inspector Name | Text | Yes | Free text |
| [Category] Score | Number | Yes | 0-10 (converts to 0-100) |
| [Category] Status | Select | Yes | Excellent/Good/Fair/Critical |
| [Category] Issues Found | Text | No | Semicolon-separated list |
| [Category] Issues Count | Number | Auto | Count of issues (auto-calculated) |
| [Category] Detailed Notes | Text | No | Free text |
| [Category] Recommendations | Text | No | Format: "Action - Cost" |
| [Category] Photo Filename | Text | No | Filename reference |
| [Category] Priority | Select | Yes | HIGH/MEDIUM/LOW |
| [Category] Last Service Date | Date | No | DD/MM/YYYY |
| [Category] Last Service Status | Text | Auto | Within 30 days / Over 30 days |
| Critical Issue 1-3 | Text | No | Issue description |
| Critical Issue 1-3 Cost | Number | No | Naira amount |
| Total Critical Repairs Cost | Number | Auto | Sum of critical costs |
| Total All Recommendations Cost | Number | Manual | Sum of all recommendations |
| Overall Facility Condition | Select | Yes | Excellent/Good/Fair/Poor |
| Additional Comments | Text | No | Free text |
| Inspection Duration | Number | No | Minutes |

---

## 5. Non-Functional Requirements

### 5.1 Performance
- Mobile app shall load inspection form in < 3 seconds
- Report generation shall complete in < 30 seconds
- Dashboard shall display data in < 2 seconds
- System shall support 50+ concurrent users

### 5.2 Availability
- System shall maintain 99.5% uptime
- Mobile app shall work offline with sync capability
- Data backup shall occur daily

### 5.3 Security
- All data transmission shall use HTTPS/TLS encryption
- User passwords shall be hashed (bcrypt)
- Session timeout after 30 minutes of inactivity
- Role-based access control enforced

### 5.4 Usability
- Mobile app shall work on Android 8+ and iOS 12+
- Interface shall be intuitive for non-technical inspectors
- Forms shall save progress automatically (prevent data loss)

### 5.5 Scalability
- System shall handle 500+ facilities
- System shall store 5+ years of inspection history
- Photo storage shall scale to 100GB+

---

## 6. Integration Requirements

### 6.1 Export Capabilities
- Export inspection data to CSV
- Export reports to PDF and DOCX
- Export photos to ZIP archive

### 6.2 Cloud Storage
- Integration with Google Drive for photo backup
- Integration with cloud storage for report archiving

### 6.3 Email Integration
- SMTP integration for sending reports and notifications
- Email template customization

---

## 7. Inspection Workflow

### 7.1 Pre-Inspection
1. Admin creates new inspection record
2. Admin assigns inspector and facility
3. System sends appointment notification to facility
4. Inspector downloads/prints checklists (if paper backup needed)

### 7.2 On-Site Inspection
1. Inspector opens mobile app
2. Inspector selects assigned inspection
3. Inspector works through each category:
   - Checks each checkpoint
   - Takes photos of issues
   - Enters notes and cost estimates
   - Marks status
4. Inspector submits completed inspection
5. System calculates scores and generates draft report

### 7.3 Post-Inspection
1. Admin reviews draft report
2. Admin makes any corrections/additions
3. Admin approves and finalizes report
4. System generates PDF report
5. System emails report to facility contact
6. System schedules follow-up reminder

---

## 8. User Interface Requirements

### 8.1 Mobile App Screens
1. Login Screen
2. Dashboard (My Inspections)
3. Inspection List
4. Facility Details
5. Category Checklist (11 screens, one per category)
6. Photo Capture
7. Summary/Review
8. Submit Confirmation

### 8.2 Admin Dashboard Screens
1. Login
2. Dashboard (Overview, Stats)
3. Facilities List
4. Facility Details
5. Inspections List
6. Inspection Details
7. Report Preview
8. Report Generator
9. User Management
10. Settings

### 8.3 Client Portal Screens
1. Login
2. My Facilities
3. Inspection History
4. Report Viewer
5. Download Reports

---

## 9. Reporting Requirements

### 9.1 Report Sections

**Section 1: Header**
- CYFT Logo
- Facility name and address
- Inspection date and inspector name
- Report reference number

**Section 2: Executive Summary**
- Overall Facility Health Score (large, color-coded)
- Status indicator (Excellent/Good/Fair/Critical)
- Category performance overview table
- Critical issues box (top 3)
- Total costs summary

**Section 3: Detailed Findings (per category)**
- Category score and status
- Issues found (bulleted list)
- Detailed notes
- Recommendations with costs
- Photo thumbnails (if available)

**Section 4: Financial Summary**
- Category-by-category cost breakdown
- Critical repairs total
- All recommendations total
- Priority breakdown (Urgent/High/Medium/Low)

**Section 5: Action Plan**
- This Week (Days 1-7) checklist
- This Month (Weeks 2-4) checklist
- Next Quarter tasks

**Section 6: Next Steps**
- Follow-up schedule
- Recommended maintenance schedule
- CYFT contact information

---

## 10. Acceptance Criteria

### 10.1 Inspection Module
- [ ] All 11 categories display correctly with checkpoints
- [ ] Scores calculate accurately based on checkpoints
- [ ] Status auto-assigns based on score thresholds
- [ ] Photos upload and attach to correct categories
- [ ] Data saves and syncs without loss

### 10.2 Report Generation
- [ ] Standard report generates with all sections
- [ ] Detailed report includes financial analysis
- [ ] PDF renders correctly with formatting
- [ ] DOCX is editable and properly formatted
- [ ] Reports include correct facility and inspection data

### 10.3 User Experience
- [ ] Mobile app works offline
- [ ] Form progress saves automatically
- [ ] Interface is intuitive for new inspectors
- [ ] Dashboard loads quickly with large datasets

---

## 11. Appendix

### 11.1 Category Checklist Reference

**Generator Health (50 points)**
1. Load Testing Performance (15 pts) — 6 checkpoints
2. Oil Quality and Levels (10 pts) — 6 checkpoints
3. Battery Condition (10 pts) — 6 checkpoints
4. Fuel System Inspection (10 pts) — 6 checkpoints
5. Maintenance Records Review (5 pts) — 6 checkpoints

**HVAC Systems (60 points)**
1. Temperature Control — ICU/OR specific requirements
2. Air Filter Condition
3. Refrigerant Levels
4. Condenser Coil Cleanliness
5. Ductwork Inspection

**Electrical Systems (60 points)**
1. Main Panel Inspection
2. Circuit Capacity
3. Emergency Lighting
4. Wiring Condition
5. Grounding System
6. Backup Power

**Fire Safety (50 points)**
1. Fire Extinguisher Inspection (count, dates, accessibility)
2. Emergency Exits (clear, signage)
3. Fire Alarm System (zones, panel status)
4. Evacuation Drills (records)
5. Fire Equipment (hoses, hydrants)

*(Full checklist details available in Inspection_Checklists_Master_Guide.md)*

---

### 11.2 Sample Cost Reference (Naira)

| Item | Estimated Cost |
|------|---------------|
| Oil change (generator) | 15,000 |
| Battery replacement | 35,000 |
| Full generator service | 50,000 |
| AC filter cleaning (per unit) | 5,000 |
| AC gas refill (per unit) | 20,000 |
| Fire extinguisher refill | 15,000 |
| Electrical rewiring | 100,000+ |
| Tank cleaning | 80,000 |
| Fumigation | 50,000 |
| Deep cleaning | 100,000 |

---

## 12. Document Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | Jan 14, 2026 | Algolog Limited | Initial FRD |

---

**Prepared by:** Algolog Limited
**For:** CYFT Consulting Limited
**Contact:** support@algolog.co
