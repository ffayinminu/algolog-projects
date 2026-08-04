# The FEE Institute — Learning & Admissions Platform
## Functional Requirements Document (FRD)

**Prepared by:** Algolog Limited
**Prepared for:** The Fred Eze Enelamah (FEE) Institute
**Referred by:** Mrs Nwamaka Okoye (AiMP Network)
**Date:** 5 August 2026
**Version:** 1.0 (pre-meeting draft)

---

## 1. Introduction

### 1.1 Purpose
This document defines the functional and technical requirements for The FEE Institute's online **Admissions and Learning Management Platform** — the digital system through which the Institute will admit students, deliver its programmes, assess learners, and issue diplomas.

It is intended to give the Institute's leadership a clear, shared picture of what the platform will do ahead of scope agreement, and to serve as the build blueprint for Algolog's engineering team.

### 1.2 Background
The FEE Institute (The Fred Eze Eñelamah Institute) is a **character-development and Kingdom-leadership school** — a project of **Kingdom Apostolic Revival Ministries (KARM)**, promoted by **John and Ngozi Eñelamah**. Its mission is to *"form Africans who will fix Africa"* by training and deploying leaders of character across the seven spheres of society. The curriculum has been piloted in Uganda and launches in Nigeria for the **2026/2027 session** (beginning December 2026 / January 2027), headquartered in Umuahia, Abia State. The Institute is **diploma-awarding**.

Delivery is **hybrid** — a physical campus in Umuahia combined with **online learning** — and classes run on a **weekend timetable** (Friday–Sunday).

The marketing website already exists (feeinstitute.org). What is required now is the **operational platform** behind it: admissions/applications, enrolment and payments, course delivery, assessment, attendance, examinations, and diploma issuance. That platform is the focus of this document.

### 1.3 Institute Profile (from the Institute's documents)
- **Promoter:** Kingdom Apostolic Revival Ministries (KARM). **Promoters/Founders:** John Eñelamah (apostolic leader; US-based) and Dr Ngozi Eñelamah (academic; teaches at the University of New Hampshire). Institute contact: +1 (857) 234-7407 · info@feeinstitute.org.
- **Model:** discipleship-first — character, competence and spiritual formation; "priesthood of the believer," with every graduate deployed as a minister in their sphere.
- **Seven schools:** Arts, Sports & Entertainment; Business & Entrepreneurial Studies; **Pa S. G. Elton School of Pastoral & Missions Studies**; Digital Media; Education; Politics & Societal Transformation; Family & Human Development.
- **Phased academic rollout:** the **Pastoral & Missions school launches first** (Q4 2026 – Q1 2027), with the other tracks following — so the platform should support **one track at launch, then multi-track expansion**.
- **Curriculum:** ~49 courses across **9 categories**, using an **FEE course-code system** (e.g. FEE 510–550), delivered over **two semesters** on a weekend schedule; the full first-year course set and descriptions are defined.
- **Audience:** recent school-certificate graduates, university students & graduates, young professionals & entrepreneurs, and church leaders & pastors-in-training.

### 1.4 Scope of this document
In scope: applicant and student journeys, faculty and academic administration, learning delivery, assessment/attendance/examinations and certification, payments, communications, and the administrative and analytics layer.

Out of scope (this phase): redesign of the public marketing website (integrate or link), and physical-campus facilities/operations.

---

## 2. Product Vision

A single, secure platform where:
- A prospective student can **discover a programme, apply, be reviewed, accepted, enrol, and pay** — end to end, online.
- An admitted student can **learn** through structured courses, complete **assessments**, participate in **live sessions and cohorts**, track **progress**, and earn a **verifiable diploma/certificate**.
- Faculty and academic staff can **deliver content, manage classes, grade, and support students**.
- Leadership can **see the full picture** — admissions pipeline, enrolment, academic progress, and revenue — in real time.

The platform mirrors the proven architecture Algolog delivered for a comparable Christian professional-training platform, adapted for a **diploma-awarding institution** with a full admissions layer.

---

## 3. User Roles

| Role | Description |
|------|-------------|
| **Applicant (Prospective Student)** | Browses programmes, submits an application, uploads documents, tracks status, accepts an offer, and pays. |
| **Student (Admitted)** | Enrols, accesses courses, takes assessments, joins live sessions and cohorts, tracks progress, earns diplomas. |
| **Faculty / Instructor** | Creates and delivers course content, sets and grades assessments, manages class rosters, runs live sessions. |
| **Academic Administrator / Provost** | Oversees programmes, curriculum, faculty, grading policy, and diploma approval. |
| **Admissions Officer** | Reviews applications, requests documents, issues offers, manages the admissions pipeline. |
| **Finance / Bursary** | Manages tuition and fees, tracks payments, applies scholarships/discounts, reconciles revenue. |
| **Super Administrator** | Full platform control: users, roles, schools/programmes, pricing, settings, audit. |
| **Teaching Assistant (TA) / Support** | Assists with scheduling, communications, and student support (permission-scoped). |

---

## 4. Platform Modules (Overview)

1. Admissions & Applications
2. Enrolment & Student Onboarding
3. Academic Structure (Schools → Programmes → Courses)
4. Learning Experience (Course Player)
5. Assessments & Grading
6. Diplomas & Certificates
7. Cohorts, Classes & Scheduling
8. Live Sessions / Virtual Classroom
9. Faculty & Academic Administration Tools
10. Payments & Fees
11. Communications & Notifications
12. Dashboards & Analytics
13. Roles, Permissions & Security

---

## 5. Functional Requirements

### 5.0 The Student Academic Journey (End to End)
The platform models the complete lifecycle of a student, so every stage below is a first-class part of the system:

1. **Apply** — prospective student discovers a programme and submits an application with documents.
2. **Admission** — admissions team reviews, requests any missing information, and issues an offer.
3. **Accept & Pay** — applicant accepts the offer and pays the application/acceptance/tuition fee.
4. **Enrol** — applicant becomes a student, is placed in the correct programme and cohort/intake, and registers for the session's courses.
5. **Learn** — student works through course content (video, written material, resources) with progress tracking, WFG-style.
6. **Continuous Assessment (CA)** — quizzes, assignments and participation are graded through the course/semester.
7. **Attendance** — attendance at live sessions/classes is tracked and counts toward eligibility and/or grade.
8. **Examinations** — the student sits the required exam(s); CA + attendance + exam combine into a final grade.
9. **Results & Progression** — results are computed and published; the student progresses to the next semester/year on meeting requirements.
10. **Diploma** — on completing all programme requirements, the student earns a verifiable, Institute-branded diploma.

Everything else in Section 5 supports this journey.

### 5.1 Admissions & Applications
This is the primary current gap and the platform's front door.

- **Programme discovery** — applicants can view the seven schools and their programmes, entry requirements, duration, and fees.
- **Online application form** — a structured application per programme, capturing personal details, background (recent school-cert graduate, undergraduate, graduate, young professional, church leader/pastor-in-training), and programme choice.
- **Document upload** — certificates, references, ID, testimony/statement of purpose, as required.
- **Application fee** (if applicable) — collected online at submission.
- **Application status tracking** — applicant can log in and see: Submitted → Under Review → Additional Info Requested → Offer → Accepted → Enrolled.
- **Admissions review workflow** — admissions officers/provost can review, request more information, and approve or decline; every action logged.
- **Offer & acceptance** — system issues an offer; applicant accepts and proceeds to enrolment and payment.
- **Automated communications** at each stage (see 5.11).

### 5.2 Enrolment & Student Onboarding
- On acceptance and payment, the applicant becomes an enrolled **Student** with a student profile/ID.
- Automatic enrolment into the correct programme, cohort/intake, and first-year courses.
- Onboarding sequence: welcome, orientation content, how-to guide, and access credentials.

### 5.3 Academic Structure (Schools → Programmes → Courses)
- Represent the **seven schools**: Arts & Entertainment; Business & Entrepreneurial Studies; Pastoral & Missions Studies; Digital Media; Education; Politics & Societal Transformation; Family & Human Development.
- Each **school** contains **programmes**; each **programme** is organised by **academic year and semester** and contains **courses** (e.g. First-Year Courses for the 2026/2027 session).
- Each **course** carries: a title, description, assigned **faculty**, **credit/unit weight** (if the Institute uses units), whether it is **core or elective**, any **prerequisites**, and its **content, CA items, and exam**.
- **Course registration** — at the start of each semester a student registers for (or is auto-registered into) the courses required for their programme and year; registration can be reviewed/approved by academic staff.
- **Diploma / graduation requirements** per programme — the set of required courses, minimum grades, attendance thresholds, and total units/credits (if used) that must be satisfied to graduate.
- **Progression rules** — the conditions to move from one semester/year to the next (e.g. pass all core courses, meet the attendance minimum).
- Course catalogue is fully admin-manageable: add/edit courses, sequence them, assign faculty, set core/elective and prerequisites.
- **Course catalogue (confirmed from the Institute's curriculum):** ~49 courses organised into **9 categories** — History & Historical Analysis; Leadership & Leadership Formation; Management & Organizational Dynamics; Ethics & Human Values; Relationships, Marriage & Family Enrichment; Transformation of Mindset & Vision; Spirituality / Spiritual Formation; Economics & the Economy; and General Courses. Courses use an **FEE code system** (e.g. FEE 510 Personal Transformation, FEE 519 Leadership Development, FEE 522 Money Matters I).
- **Semester & weekend timetable:** each semester runs across weekends (Friday–Sunday), split into an early block (~6 weekends) and a later block (~7 weekends) with fixed class time-slots. The platform must model this **academic calendar and class timetable** per cohort.
  > *The full course list, first-year courses, and timetable from the Institute's Curriculum and First-Year Courses documents will be imported directly.*

### 5.4 Learning Experience (Course Player)
- Structured course view: sections and segments, video and written content, downloadable resources.
- **Curriculum outline** under the player showing all sections/segments, current position, what's left, and where assessments sit.
- **Progress tracking** that saves automatically and restores the student to where they left off on next login.
- Auto-advance across segments and module boundaries.
- Reflection/discussion prompts where relevant.
- Bookmark/save; mobile-responsive playback.

### 5.5 Assessment, Continuous Assessment, Attendance & Examinations
The Institute awards diplomas, so grading is not a single quiz — it combines **continuous assessment, attendance, and a final examination** into a course grade. The platform supports all three, with a configurable weighting per programme/course.

**5.5.1 Continuous Assessment (CA)**
- CA items throughout a course/semester: **quizzes, assignments, and participation**.
- Question types: multiple-choice, multi-select, true/false, and short-text; **assignments** are graded manually by faculty (with file upload where needed).
- Each CA item carries a mark; CA contributes a configurable percentage of the final course grade (e.g. CA 40%).
- Automated grading for objective questions; faculty grading interface for assignments, with feedback to the student.

**5.5.2 Attendance**
- Attendance is **tracked for live sessions/classes** (see 5.8) and can be recorded by faculty or captured automatically on session join.
- Attendance can be configured to:
  - **count toward the grade** (a percentage of the final mark), and/or
  - **gate exam eligibility** (a student must meet a minimum attendance threshold to be allowed to sit the exam).
- Attendance records are visible to the student, faculty, and academic administration.

**5.5.3 Examinations**
- Each course can have a **final examination** (timed where required), built from the same question engine plus, where needed, manually graded sections.
- **Exam eligibility** can require completion of course content, minimum CA, and minimum attendance.
- The exam contributes a configurable percentage of the final grade (e.g. Exam 60%).

**5.5.4 Grading model & results**
- **Final course grade = CA + Attendance (if weighted) + Exam**, per the programme's configured weighting; pass marks are configurable.
- A course cannot be completed or certified on content-viewing alone — the required CA and exam must be satisfied.
- Support for **grade classifications** (e.g. pass/merit/distinction) if the Institute uses them.
- **Results publication** — results are computed and released to the student; academic staff can review before release.
- **Resit/retake** handling where a student fails a course (configurable policy).

**5.5.5 Transcripts & academic records**
- A per-student **transcript** aggregates course grades across semesters/years.
- Academic records feed **progression** (5.3) and **diploma issuance** (5.6).
- Records are auditable and exportable for the student and academic administration.

> *Note: The Institute's documents confirm diploma-awarding status and weekend live classes (so attendance carries real weight), but do not yet specify the CA / attendance / exam weighting or pass marks. The model above is Algolog's proposed, fully configurable default — to be confirmed with the Provost.*

### 5.6 Diplomas & Certificates
- On satisfying all diploma requirements for a programme, the student earns a **diploma/certificate**.
- Certificates are **platform/Institute-branded**, issued in the Institute's name, and carry the graduate's details and programme.
- **Verification** — each certificate carries a unique code / verification page so third parties can confirm authenticity.
- Downloadable as PDF; print-quality output.
- A lapsed or withdrawn student retains diplomas already earned.

### 5.7 Cohorts, Classes & Scheduling
- Students are grouped into **cohorts/intakes** (e.g. the 2026/2027 session).
- Cohort-scoped communication and content where required.
- Academic calendar / schedule of classes and sessions per cohort.
- Per-cohort moderator/TA support.

### 5.8 Live Sessions / Virtual Classroom
- Schedule and host **live sessions** (lectures, seminars) targeted to eligible students, specific cohorts, or all.
- Support the Institute's **weekend class timetable** (Friday–Sunday) as recurring scheduled sessions per cohort, mapped to the academic calendar.
- **Hybrid delivery:** a session may be **in-person** (Umuahia campus), **online**, or both; the platform captures **attendance** in either mode and feeds it into grading/eligibility (see 5.5.2).
- Only genuinely upcoming sessions appear under "Upcoming"; past sessions drop off automatically.
- **Automated reminders/notifications** to participants ahead of each session.
- Option to link/embed a video conferencing tool and to post session recordings afterward.

### 5.9 Faculty & Academic Administration Tools
- Faculty: create/edit courses and content, set assessments, grade, view their class roster, run live sessions.
- Provost/Academic admin: manage curriculum, assign faculty to courses, set grading policy, approve diplomas.
- Admissions officer: manage the admissions pipeline (5.1).
- All content and academic actions are permission-scoped and auditable.

### 5.10 Payments & Fees
- Collect **application fees, tuition, and programme fees** online.
- Support **local and international payments** — important given a diaspora founder and potential international students (cards, transfers; USD/NGN as configured).
- **Fee structures** per programme; support for instalments where the Institute allows.
- **Scholarships/discounts and fundraising tiers** (the Institute already promotes donation tiers) — apply discounts, track sponsored students.
- Automated receipts and invoices; finance dashboard and reconciliation.
- Pricing is controlled by the Super Admin, scoped per programme, logged, and never retroactively re-charges existing students.

### 5.11 Communications & Notifications
- Automated, branded emails across the lifecycle: application received, info requested, offer, acceptance, enrolment, payment receipt, course/cohort updates, live-session reminders, certificate earned.
- Cohort messaging and broadcast email to a cohort or the whole student body (with moderator control).
- Emails clearly branded to The FEE Institute; content states the programme/cohort/reason with a short description.

### 5.12 Dashboards & Analytics
- **Leadership dashboard:** admissions pipeline (applications by stage), enrolment numbers, revenue, and academic progress at a glance, filterable by school/programme/cohort and date.
- **Academic dashboard:** course completion, assessment performance, at-risk students.
- **Finance dashboard:** fees collected, outstanding, scholarships, reconciliation.
- Exportable reports (CSV/PDF).

### 5.13 Roles, Permissions & Security
- Role-based access control across all modules (Section 3).
- Full audit logging of admissions decisions, grading, diploma issuance, pricing changes, and administrative actions.
- Secure authentication; password reset that properly invalidates the old password.

---

## 6. Non-Functional Requirements

- **Performance:** responsive under concurrent student load, including intake and exam peaks.
- **Availability:** high uptime target; automated backups and recovery.
- **Security:** encrypted data at rest and in transit; role-based access; secure document/credential storage; audit trails.
- **Scalability:** supports growth across cohorts, programmes, and future sessions.
- **Data privacy:** applicant and student data handled confidentially; access on a need-to-know basis.
- **Accessibility & devices:** fully mobile-responsive; usable on low-to-mid-range devices and varying connectivity.
- **Maintainability:** modular architecture allowing phased rollout without disrupting live operations.

---

## 7. Integrations

- **Payment gateway** — for local and international collections (cards, transfers; USD/NGN).
- **Email / SMTP** — transactional and cohort emails from the Institute's domain.
- **Video hosting/streaming** — secure delivery of course videos.
- **Video conferencing** — for live sessions (embed/link).
- **Domain** — deployment on the Institute's domain (feeinstitute.org and/or a subdomain such as portal.feeinstitute.org).
- Optional future: integration or migration path for any existing "GClassroom"/portal references on the current site.

---

## 8. Technical Architecture (Indicative)

- **Frontend:** modern responsive web application (Next.js / React).
- **Backend:** Node.js services with a PostgreSQL database and an API layer.
- **Cloud:** deployed on secure cloud infrastructure with monitoring, logging, and automated backups.
- **Access:** web-based; installable/mobile-friendly progressive experience.

*(This mirrors the stack Algolog used for a comparable training platform, which shortens delivery time and de-risks the build.)*

---

## 9. High-Level Data Entities

Applicant · Application · Student · School · Programme · Semester/Year · Course · Course Registration · Module/Segment · CA Item (Quiz/Assignment) · Attendance Record · Examination · Grade/Result · Transcript · Cohort/Intake · Live Session · Faculty · Enrolment · Payment/Fee · Scholarship · Diploma/Certificate · User/Role · Audit Log.

---

## 10. Assumptions & Dependencies

- The Institute will provide the **course curriculum, first-year course list, and programme structure** (referenced in their documents) for import.
- The Institute will provide **course content** (videos, materials), **faculty details**, **fee structures**, and **admission requirements** per programme.
- The Institute will provide **domain access** and an **email/SMTP** sending address.
- Branding assets (logo, colours) provided for certificate and email styling.

---

## 11. Out of Scope (Phase 1)

- Redesign of the public marketing website (link/integrate instead).
- Physical campus / facilities management.
- Advanced features that may follow later: mobile app store apps, alumni network, advanced analytics/AI, third-party SIS integrations.

**Optional module (can be added on request):** a **Partnerships / Donations module** — the Institute runs partner tiers (Pioneer, Founding, Major Donor, Principal, Institute, Supporting Partners) and online giving in USD and NGN. This can be built into the platform or kept on the marketing website.

---

## 12. Indicative Delivery Phases

1. **Discovery & Setup** — confirm programmes, admissions flow, fees; configure schools/programmes; branding.
2. **Admissions & Payments** — application forms, review workflow, offers, enrolment, fee collection (priority, given the open session).
3. **Learning & Assessment** — course delivery, assessments, progress, cohorts.
4. **Live Sessions & Certificates** — live classes, reminders, diploma issuance and verification.
5. **Dashboards, Testing & Training** — analytics, QA, staff training, go-live.

Because the 2026/2027 session opens in December 2026 / January 2027, the **admissions and payments layer is the priority for early delivery** so the Institute can begin admitting and enrolling immediately. In line with the Institute's own rollout, the platform can **launch first for the Pa S. G. Elton School of Pastoral & Missions Studies** (the first track), then extend to the remaining six schools.

---

## 13. Open Questions for the Meeting (to finalise scope)

1. **Admissions flow** — what exactly should the application capture, and what is the review/approval process (who approves)?
2. **Programme structure** — how is a diploma earned (courses, units, duration)? Semesters or continuous?
2b. **Grading model** — how should CA, attendance, and exams be weighted (e.g. CA 40% / Exam 60%)? Is there an attendance minimum to sit exams? Any grade classifications (pass/merit/distinction) or resit policy?
3. **Delivery mode** — confirmed hybrid (weekend classes, Umuahia campus + online). Which courses/sessions are in-person vs online, and how should attendance be captured for each?
4. **Fees** — application fee, tuition per programme, instalments, scholarships/sponsorship; currency (USD, NGN, or both)?
5. **Students** — expected first-intake size; local vs diaspora split (affects payments)?
6. **Existing portal** — what is the "GClassroom"/portal on the current site today; replace or integrate?
7. **Faculty** — number and roles (provost, faculty, TA); what tools do they need first?
8. **Timeline** — target date for admissions to be live, and for the first cohort to begin learning?
9. **Decision & sign-off** — who approves scope and budget (founder, provost, Ms Precious Ugboja)?

---

*This document is built from The FEE Institute's own materials — the Course Curriculum/Category, First-Year Courses, Concept Paper, flyer, and website — the referral briefing, and the founder's call, mapped onto Algolog's proven training-platform architecture. Remaining items to confirm at the scope meeting: the grading/attendance/exam weighting and pass marks, tuition/fee structure, and detailed admission requirements per programme.*

**Algolog Limited** — Plot 1387 Aminu Kano Crescent, Wuse, Abuja · info@algolog.co · algolog.co
