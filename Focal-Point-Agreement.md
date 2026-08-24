# SOFTWARE DEVELOPMENT & DEPLOYMENT AGREEMENT
### Focal Point Operational Digitization & Tracking System

Effective Date: 24th August 2026
## Parties
Algolog Limited ("Algolog"), of Plot 1387 Aminu Kano Crescent, Wuse, Abuja, Nigeria;
and
Focal Point Drycleaners ("the Client"), of 120 Pa Michael Imoudu Avenue, Gwarinpa, Abuja, FCT, represented by Hassan Rilwan.
Algolog and the Client are each a "Party" and together the "Parties".
## 1. Background & Purpose
The Client operates a laundry and garment-care business in Gwarinpa, Abuja, and requires a unified digital platform to replace its current system (DriveStream) and manage its operations from customer intake to final delivery, including tracking, payments, staff accountability, revenue assurance, and reporting. Algolog agrees to design, develop, deploy, and support the Focal Point Operational Digitization & Tracking System ("the System") on the terms set out in this Agreement.
## 2. Scope of Work (Consolidated)
The System is delivered as a single, fully integrated platform comprising the following functional modules and the supporting engineering and infrastructure beneath them. Nothing in this scope is delivered in isolation; all items below form one unified build. The scope of this Agreement is limited to the items expressly described in this Section 2; anything not expressly listed here is out of scope and is handled as a change request under Section 10.
**2.1 Functional Modules**
- A. Customer & Intake Management: customer registration (in-store + online); digital terms & conditions signing; customer portal for tracking, receipts and history; wallet system for prepaid credit & auto-deductions; automatic SMS/email status updates.
- B. Item Tracking & Lifecycle Monitoring: unique RFID tag/item code per garment; full lifecycle tracking (intake, sorting, washing, pressing, QC, delivery); multi-level notes for stains/damage/special care; return-history tracking; visibility across all branches; real-time shelf item-count.
- C. Sales, Invoicing & Payments: a sales system covering the Client's service types; bank transfer, POS, cash and Paystack integration; staff transfer-validation; automatic receipts; end-of-day/month balancing; corporate invoicing & bulk customer handling.
- D. Revenue Assurance & Fraud Prevention: automated matching of walk-in, payment and walk-out; alerts when an item leaves unpaid; staff permission controls; full audit logs; management reconciliation tools.
- E. Inventory Control (Walk-In vs Walk-Out): stock-on-hand tracking, instant discrepancy detection, shelf-vs-system reconciliation.
- F. Staff Productivity & Performance Tracking: per-item scan counts, automatic earnings calculation, duplicate-scan prevention, QC and returns penalty logic, daily staff performance reports.
- G. Returns & Penalty Management: daily per-staff return limits, automatic penalties beyond thresholds, full handling logs.
- H. High-Value Item Declaration: customer value declaration above a set threshold with applicable protection charges.
- I. Reporting & Analytics: revenue (daily/weekly/monthly), top customers, staff productivity, branch performance, top service categories, walk-in vs walk-out reconciliation, payment-channel performance, wallet usage, bottleneck identification.
- J. Website & Online Customer Interface: a modern Focal Point website; online item-tracking portal; customer login & wallet; T&C signing; order/receipt/invoice history; pickup/delivery requests.
- K. Mobile Usability: The System will be fully developed for mobile usability, responsive across phones, tablets and desktops, including customer dashboard access and a manager view for approvals, QC and reconciliation.
- L. SOP & Documentation: full operational SOPs (intake, washing & pressing, QC, returns, customer communication, cash/transfer/POS handling, branch reporting, staff accountability), plus an operational manual, hosting & infrastructure documentation, and a staff/user manual for day-to-day System use.
- M. Customer Rewards & Discounts: the ability to set up and apply customer discounts, and to reward the Client's top customers (for example, high-value or high-frequency customers) with configurable loyalty benefits.
**2.2 Engineering & Infrastructure**
- Scanning & workflow engineering: integration with commercial RFID readers; error handling for unreadable or damaged tags; offline scanning capability with background sync; custom packing / after-pack workflow (batch validation + final handover confirmation); API integration between readers and the cloud backend.
- Security & access: authentication, role-based access control (RBAC), and secure session management.
- Cloud infrastructure: AWS/Azure architecture; compute, storage and network configuration; database clustering and automated backups; file/tag metadata storage; logging and monitoring; scalable architecture designed to support a growing customer base.
- DevOps: Continuous Integration & Continuous Deployment (CI/CD) pipelines; Infrastructure as Code (IaC, Terraform/Pulumi); staging and production deployment workflows.
- Quality assurance: full manual and automated testing; test-script development; performance and load testing; security testing; beta testing with selected staff; final launch verification and sign-off.
## 3. Deliverables
- Full multi-tenant operational system (all modules and engineering in Section 2).
- Custom website with customer portal.
- Data migration from DriveStream (per Section 9).
- Staff accounts and permission setup.
- Dashboards, insights and analytics.
- Fraud-detection and reconciliation tools.
- Wallet system.
- Customer rewards and discounts module.
- SOP documentation.
- Operational manual, hosting & infrastructure documentation, and staff/user manual.
- Staff training.
- All UI/UX screens, delivered mobile-responsive.
- CI/CD pipelines and Infrastructure-as-Code configuration.
- Twelve (12) months technical support (per Section 6).
- One (1) year managed cloud hosting (per Section 6).
- Full codebase access (per Section 7).
## 4. Equipment (Client-Procured)
Hardware required to operate the System is procured directly by the Client and is not included in this Agreement's fee. Algolog will advise on specifications and integrate and configure the equipment with the System. The System uses a UHF RFID scanning setup, described below.
**UHF RFID Setup**
Garments carry washable UHF RFID tags, each holding a permanent ID the System reads on every scan. This approach scans a whole basket of garments at once, and in locate mode it beeps faster as staff move closer to a specific garment, so a single item can be found in a pile or on a rack by sound. One handheld unit at the front desk handles the bulk scanning and locating, while each department uses a lower-cost reader paired with an Android phone for everyday station scanning. The recommended set and indicative pricing is:
| Equipment | Suggested Spec | Qty | Indicative price (NGN) |
| --- | --- | --- | --- |
| UHF RFID Laundry Tags | Washable UHF tag, permanent ID, sewn into a seam or heat-sealed, survives hundreds of wash/press cycles | Batch of 2,000 | 500 per tag (1,000,000 / batch) |
| Handheld UHF Reader (front desk) | Rugged Android UHF handheld (Chainway C72 class); runs the System over WiFi, long-range and bulk read, single-read mode, tag-locate (beep-to-find) | 1 | 1,500,000 |
| Station UHF Reader | UHF reader with barcode support, paired with the station phone | 1 per station | ~256,000 |
| Station Phone | Android phone (Samsung Galaxy A06 class) running the System | 1 per station | ~120,900 |

Indicative prices are shown for guidance only and may vary with supplier and exchange rate at the time of purchase. The number of station devices depends on the Client's branch and department layout.
Where the Client requests Algolog to procure any equipment on its behalf, this will be handled and invoiced separately from this Agreement.
**4.1 Equipment & Performance**
The quantities and specifications above are Algolog's recommendation for the System to perform at its best, and Algolog is glad to advise on the equipment. The Client may adjust them to suit its budget or preferences. Where the equipment provided is below the recommended standard, some aspects of performance (such as speed, scanning accuracy, or coverage) may be affected, and this would not be treated as a fault in the System. Algolog will confirm the equipment configuration tested and verified as part of user acceptance testing (UAT). Any additional work to resolve issues caused by the equipment can be carried out as a separately agreed item under Section 10.
RFID performance also depends on the working environment, for example metal racks and trolleys, dense piles of garments, moisture, and how each tag is placed on the garment. These are normal characteristics of RFID and are not a fault in the System. Algolog will set up the readers and tags to get the best practical result, and any further optimisation the Client asks for beyond that can be handled as a separately agreed item under Section 10.
## 5. Project Fee & Payment Terms
Total project fee: N14,000,000 (Fourteen Million Naira only). This is a fixed fee covering the full consolidated scope, deliverables, data migration, training, twelve (12) months technical support, and one (1) year of managed hosting as described in this Agreement.
**Payment schedule:**
| Installment | Trigger | Amount (N) |
| --- | --- | --- |
| 50% | On signing of this Agreement (mobilisation, before work begins) | 7,000,000 |
| 25% | On completion of core build / user acceptance testing (UAT) | 3,500,000 |
| 25% | On go-live / handover | 3,500,000 |

Payments are made to Algolog Limited per the details on Algolog's issued invoice(s). The fee excludes hardware/equipment (Section 4), ongoing hosting beyond the first year, third-party/subscription fees, and any work outside Section 2 (see Section 10).
Fees paid for delivered and accepted work are non-refundable. On the Client's acceptance of the System and handover of the codebase (Section 8.3), the project is complete and no refund or further liability arises. The Client's protection for value paid is provided through the licence in Section 7 and the support and warranty in Sections 6 and 14, not through refunds.
If any payment is overdue, Algolog may suspend work on the project until payment is received, and may charge interest on the overdue amount at 2% per month. A suspension for non-payment extends the affected timelines day-for-day, in line with Section 8.1.
## 6. Hosting & Support
- Managed hosting: Algolog provides secure, managed cloud infrastructure for one (1) year, commencing on go-live or on receipt of the final payment if later: application hosting, secure data/file storage, daily automated backups, and high-availability servers. Hosting beyond the first year is renewable under a separate arrangement.
- Technical support: Algolog provides twelve (12) months of technical support, commencing on go-live or on receipt of the final payment if later, strictly covering bug fixes, uptime monitoring, and correction of defects within the System's originally agreed scope (Section 2). It does not include new features, new modules, workflow redesigns, third-party integrations, or any expansion of scope, which are quoted and handled separately under Section 10. Support is provided as a service and creates no liability to refund fees or pay damages.
**6.1 Support Boundaries and Response**
Support is provided remotely during business hours (Monday to Friday, 9:00am to 6:00pm WAT, excluding public holidays). Reported issues are prioritised by severity, and Critical Issues are attended to as a priority. A Critical Issue means a defect that makes the System substantially unavailable to all users, or that prevents a core operational function (customer intake, payment processing, or garment tracking) from operating. On-site support, where needed, is arranged separately. Algolog may carry out scheduled maintenance with reasonable prior notice, during which brief downtime may occur.
**6.1.1 Severity Levels and Response Targets**
Reported issues are classified by severity. The response targets below are the times within which Algolog aims to acknowledge and begin work during the support hours in 6.1; they are good-faith targets, not guarantees of resolution time.
| Severity | Meaning | Response target |
| --- | --- | --- |
| Critical | System substantially unavailable to all users, or a core function (customer intake, payment processing, or garment tracking) cannot operate | Within 4 business hours |
| Major | A significant function is impaired or fails for some users, but a workaround exists or the System remains usable | Within 1 business day |
| Minor | A limited, cosmetic, or low-impact issue not affecting core operations | Within 3 business days |

Where Algolog does not meet a response target, its obligation is to prioritise and use reasonable efforts to remediate the issue. A missed response target does not entitle the Client to any refund, penalty, service credit, or liquidated damages, and creates no liability beyond correction of the defect (Sections 14 and 15).
**6.2 Defects and Change Requests**
For the purpose of support and warranty, a defect (or bug) means a failure of the System to perform substantially in accordance with the agreed scope in Section 2. Cosmetic or layout preferences, new features, new modules, redesigns, or additional workflows are change requests, which are quoted and handled separately under Section 10.
**6.3 Access**
Any access Algolog holds to the Client's System, data, or environment is temporary and limited to what is necessary to deliver the project and provide support under this Section 6. On acceptance and handover (Section 8.3), administrative control and credentials pass to the Client (Section 7), and Algolog will relinquish standing administrative access, retaining only such limited access as the Client authorises for the support period. On expiry of that period, or on the Client's earlier written request, Algolog will cease all access and return or securely delete any Client credentials in its possession (Section 13).
**6.4 Renewal and Running Costs**
Algolog provides technical support for the full twelve (12) months following delivery, as set out in this Section 6. After that period, Algolog can continue to provide support at a cost to be agreed between the Parties. Server, storage, and running costs cannot be calculated in advance, because they depend on the Client's actual customer traffic and System usage, which are not known at the time of signing. After approximately one (1) month of live usage, Algolog will assess the actual usage and send the Client an estimate of the ongoing server and running costs. Any renewal of support or hosting beyond the first year is not fixed by this Agreement and will be quoted separately, based on actual usage at that time.
## 7. Intellectual Property & Codebase Access
- As each instalment is received, the Client is granted a non-exclusive, irrevocable licence to use the portion of the System that has been delivered and paid for, effective from the date of that payment. This licence is a right to use the delivered functionality through the deployed, running System only; it does not include the source code, which is handed over separately on full and final payment (Section 8.3). This ensures the Client retains the benefit of work already funded, even if the engagement ends before completion.
- On full and final payment, full ownership of and access to the complete System codebase vests in the Client, providing full transparency, future extensibility, and long-term control over the solution.
- Following handover, the System and source code are accepted as delivered. Any future maintenance, enhancement, adaptation, optimisation, compatibility work, or regulatory updates are outside this Agreement unless separately agreed in writing (see Section 10).
- Algolog retains ownership of any pre-existing tools, libraries, frameworks and reusable components used to build the System, and grants the Client a perpetual licence to use them as part of the System.
- Third-party software and open-source components incorporated into the System remain subject to their own licence terms, which continue to apply despite any transfer of ownership under this Agreement.
## 8. Timeline & Delivery Milestones
The following milestone schedule sets target dates, measured in weeks from project commencement (commencement being the later of receipt of the upfront payment and receipt of the Client inputs required to begin). These dates are good-faith targets and estimates, and are subject to Section 8.1. Each milestone has a target completion and, where applicable, a linked payment trigger:
| Milestone | Target (from commencement) | Linked payment |
| --- | --- | --- |
| Requirements & data mapping | End of Week 1 | - |
| System architecture & UX sign-off | End of Week 3 | - |
| Core build complete (UAT start) | End of Week 8 | - |
| UAT sign-off | End of Week 10 | 25% (N3,500,000) |
| Website & customer portal complete | End of Week 11 | - |
| Testing & QA complete | End of Week 12 | - |
| Data migration & go-live | End of Week 13 | 25% (N3,500,000) |
| Staff training & handover | End of Week 13 | - |

**8.1 Client-caused delay**
Where a delay is caused by the Client (for example, late inputs, approvals, content, data exports, or equipment procurement) or by any third party or event outside Algolog's reasonable control, the affected milestone dates extend day-for-day, and no liquidated damages accrue for that period.
**8.2 Delay**
If a milestone is delayed for reasons attributable to Algolog, Algolog will prioritise remediation and agree a revised date with the Client. A delay does not entitle the Client to a refund, penalty, or liquidated damages. However, if go-live has not occurred within twelve (12) weeks after the Week 13 target date in Section 8, for reasons solely attributable to Algolog (and not any delay under Section 8.1 or event under Section 15.3), the Client may terminate this Agreement by written notice, in which case the valuation, payment, and handover provisions of Section 16 apply. Persistent failure to deliver is addressed through the termination provisions in Section 16. Algolog's priority in any delay is to complete and hand over the System to the Client as quickly as reasonably practicable, rather than to prolong the engagement. This statement of intent does not vary the targets, remedies, or limits set out elsewhere in this Agreement.
**8.2.1 Delay credit**
If go-live is delayed past the Week 13 target in Section 8 for reasons solely attributable to Algolog, Algolog will credit the Client 0.5% of the total project fee for each full week of that delay, up to a maximum of 3% of the total project fee (N420,000). The credit is applied as a reduction of the final instalment due under Section 5. This delay credit is the Client's sole and exclusive remedy for late delivery. It is in addition to the Client's right to terminate under Section 8.2, and it does not give the Client any further refund, cash payment, or other damages. No credit accrues for any period of delay caused by the Client (Section 8.1) or by an event outside Algolog's reasonable control (Section 15.3), and this credit remains subject to the overall limit in Section 15.
**8.2.2 Meaning of "solely attributable to Algolog"**
In Sections 8.2 and 8.2.1, a delay is solely attributable to Algolog only where it is caused by Algolog's own act or omission and is not caused, wholly or in part, by any of the following: the Client's late or incomplete inputs, approvals, content, data, or payments; the Client's procurement, supply, or configuration of hardware, equipment, or connectivity; any third-party service, supplier, or platform; or any event under Section 15.3.
**8.3 Acceptance and Handover**
On completion of the build, Algolog will deploy the System and make it available to the Client for user acceptance testing (UAT). Algolog will give the Client written notice that the acceptance period has commenced. The Client will review the System and confirm acceptance in writing. Acceptance is deemed given if the Client puts the System into live use, or does not raise a material, documented defect within ten (10) business days of that written notice. On acceptance, the Parties will execute a Handover & Acceptance Certificate substantially in the form of Schedule 1 to this Agreement, recording acceptance, receipt of the final payment, and handover of the deliverables; a Party's failure or refusal to execute the Certificate does not delay or invalidate acceptance arising under this Section 8.3. On acceptance and receipt of the final payment, Algolog will hand over the codebase and access credentials, and ownership passes to the Client under Section 7. Acceptance and handover mark completion of the project, after which Algolog has no further liability under this Agreement (see Section 15).
On acceptance, all features described in Section 2 are treated as delivered, except any item the Client has identified in writing as an outstanding defect before acceptance.
**8.4 Milestone Completion Checklist**
At each milestone in the schedule above, Algolog will provide the Client with a short completion checklist confirming that the items due at that milestone have been completed, for the Client's review. A milestone checklist substantially in the form of Schedule 2 may be used. Sign-off of a milestone checklist confirms that stage is complete for progress-tracking purposes only; it is not the acceptance of the System, which occurs solely under Section 8.3.
**8.5 Milestone Visibility**
At each milestone, Algolog will give the Client access to review the functionality built up to that point, through a walkthrough or the deployed or staging System, so the Client can confirm progress against the milestone schedule. This is a right to view and assess the work delivered to date, for progress-tracking only. It does not release the source code, which is handed over on full and final payment under Sections 7 and 8.3, and it grants no licence or other right in the System or its code beyond what Section 7 provides on payment.
## 9. Data Migration
Algolog will migrate the Client's operational data from DriveStream into the System on the following basis:
- Pre-migration audit & backup: before any migration, Algolog will document the source data and take a complete backup of the DriveStream export provided by the Client.
- Integrity verification: after migration, Algolog and the Client will jointly verify the completeness and accuracy of the migrated data against the source before go-live.
- Rollback: a documented rollback procedure will be available so the prior state can be restored if a material migration issue is found.
- Liability: where data is lost or corrupted as a direct result of Algolog's migration process, Algolog will, at its cost, re-perform the migration and restore the affected data from the pre-migration backup. This restoration is the Client's sole and exclusive remedy for migration-caused data loss, and consequential losses are excluded (subject to Section 15). The Client is responsible for the accuracy and completeness of the source data and exports it provides.
## 10. Change Requests & Out-of-Scope Work
Any feature, integration or workflow not described in Section 2 is out of scope and will be quoted and agreed separately before development. Approved changes may affect timeline and fee.
## 11. Client Responsibilities
The Client will: procure the required hardware (Section 4); provide existing data for migration (including DriveStream exports); supply content, branding and operational details; grant timely access and approvals; nominate a primary contact for decisions; and make payments per Section 5.
## 12. Confidentiality
Each Party will keep the other's confidential, proprietary, client and operational information confidential during and after this Agreement, and use it only to perform this Agreement.
## 13. Data Protection (NDPA 2023)
In performing this Agreement, both Parties will comply with the Nigeria Data Protection Act 2023 (NDPA) and applicable data-protection regulations. In respect of personal data processed through the System (such as customer names, contacts, payment history and wallet balances), the Client is the data controller and Algolog acts as data processor. Algolog will: process personal data only as needed to deliver and support the System or on the Client's documented instructions; apply appropriate technical and organisational security measures; reasonably assist the Client with data-subject requests and security-incident notifications; and, on termination, return or securely delete personal data at the Client's instruction. The Parties will execute a Data Processing Addendum where required to give fuller effect to this clause.
**13.1 Security Responsibilities**
Algolog will apply commercially reasonable security measures within the delivered System. However, no software system can guarantee absolute security, and Algolog does not warrant that the System will be completely immune from cyberattacks, malware, or unauthorised access. The Client is responsible for the security of its own accounts and devices, including keeping passwords confidential, provisioning and promptly removing user access (particularly for departed staff), endpoint security, and any compromise arising from credential sharing, negligence, malware, or unauthorised access to Client-controlled systems or accounts. A loss or breach arising from these Client-side matters is not a defect in the System.
## 14. Warranty
Up to acceptance (Section 8.3), Algolog warrants that the System will materially perform the functions in Section 2. During the support period (Section 6), Algolog will, as a service, correct reported defects in the delivered scope at no additional cost. The sole remedy under this warranty is correction of the defect; it does not include any refund or damages, and it does not revive any liability after acceptance and handover. The warranty does not cover issues caused by client-side changes, misuse, or third-party/hardware failure.
## 15. Limitation of Liability
Algolog's total aggregate liability under this Agreement, for all claims however arising, will not exceed the total fees paid by the Client. Algolog is not liable for indirect, incidental, or consequential losses (including loss of revenue, profit, or business), or for losses arising from client-procured hardware, third-party services, or connectivity outside Algolog's control. The Client's remedies are limited to those expressly stated in this Agreement, and no refund of fees paid for delivered and accepted work will be due. The limitations and exclusions of liability in this Agreement apply regardless of the legal basis of the claim, whether in contract, tort (including negligence), statute, or otherwise, to the fullest extent permitted by applicable law. Nothing in this Agreement excludes or limits either Party's liability for fraud, fraudulent misrepresentation, or wilful misconduct, or any other liability that cannot lawfully be excluded or limited under applicable law.
**15.1 Release on Acceptance and Handover**
The Client's acceptance of the System and receipt of the codebase (Section 8.3) confirm the Client's satisfaction that the project has been delivered. Except for the correction-only support and warranty in Sections 6 and 14, from that point the Client releases Algolog from any further liability arising from the System, the codebase, or this Agreement, including any liability to refund fees or to pay damages, to the fullest extent permitted by law.
**15.2 Post-Handover Modifications**
After handover of the codebase (Section 8.3), Algolog is not responsible for defects, downtime, security issues, compatibility issues, data loss, or performance degradation arising from modifications to the System by the Client or anyone other than Algolog, or from changes to infrastructure, hosting environment, operating systems, databases, cloud services, third-party integrations, software dependencies, security configuration, or any other environment in which the Client chooses to host or operate the System.
For the avoidance of doubt, following handover the System and source code are accepted as delivered, and any future maintenance, enhancement, adaptation, optimisation, compatibility work, or regulatory updates fall outside this Agreement unless separately agreed in writing (Section 10).
**15.3 Force Majeure**
Neither Party is liable for any delay or failure to perform caused by events beyond its reasonable control, including power or internet failure, cloud-provider outage, fire, flood, strike, civil unrest, terrorism, or government action. Affected obligations are suspended for the duration of the event, and any linked timelines extend accordingly. If such an event continues for more than thirty (30) days, either Party may terminate under Section 16.
## 16. Termination
Either Party may terminate for material breach not remedied within fourteen (14) days of written notice. On termination:
- Valuation: the value of work completed to the termination date is measured by the milestones achieved under Section 8, together with a fair pro-rata (quantum meruit) valuation of any work substantially completed between milestones.
- Payment: the Client pays for all work completed to the termination date. Fees for completed or accepted work, and the mobilisation payment, are non-refundable. Reconciliation applies only to a later stage of work not yet commenced, and is the Client's sole remedy on termination.
- Handover: once amounts due for completed work are settled, Algolog will provide the Client with its own data and continued licensed use of the completed, paid-for portion of the System, in line with Section 7. The System source code is released only on full and final payment (Sections 7 and 8.3), and is not handed over on early termination.
These termination provisions apply before completion. After the Client's acceptance of the System and handover of the codebase (Section 8.3), the project is complete and no refund or liability arises under this Section.
**16.1 Survival**
Sections 7, 12, 13, 14, 15, and 17, together with any payment obligations that have accrued, survive the completion, expiry, or termination of this Agreement.
## 17. Governing Law & Dispute Resolution
This Agreement is governed by the laws of the Federal Republic of Nigeria. If a dispute arises, the Parties will first attempt to resolve it in good faith through mediation for a period of twenty-one (21) days from written notice of the dispute. If the dispute is not resolved within that period, it will be submitted to the exclusive jurisdiction of the High Court of the Federal Capital Territory, Abuja.
## 18. Entire Agreement
This Agreement, together with Schedules 1 and 2, which form part of this Agreement, constitutes the entire agreement between the Parties on its subject matter and supersedes all prior discussions, proposals, and understandings, whether written or oral, including the Version 1 Agreement dated 24th June 2026.
## 19. Acceptance & Signatures
By signing below, the Parties agree to the terms of this Agreement. Each signatory warrants that they are duly authorised to execute this Agreement on behalf of the Party for which they sign.

**For Algolog Limited**
Name: Yasmin Umar Dewu
Title: Chief Brand Strategist
Signature:
Date: 24th August 2026

**For Focal Point Drycleaners**
Name: Hassan Rilwan
Title: Director
Signature: ____________________
Date: ____________________

# SCHEDULE 1: HANDOVER & ACCEPTANCE CERTIFICATE
This Certificate is issued pursuant to Section 8.3 of the Software Development and Deployment Agreement dated 24th August 2026 ("the Agreement") between:
Algolog Limited ("Algolog"), of Plot 1387 Aminu Kano Crescent, Wuse, Abuja, Nigeria; and
Focal Point Drycleaners ("the Client"), of 120 Pa Michael Imoudu Avenue, Gwarinpa, Abuja, FCT.
Capitalised terms used in this Certificate have the meanings given in the Agreement.
### 1. Completion of User Acceptance Testing
The Client confirms that:
1.1. The System was deployed and made available to the Client for user acceptance testing (UAT), and written notice of the commencement of the acceptance period was given by Algolog on ____ / ____ / 20____.
1.2. The Client has reviewed and tested the System and confirms that it materially performs the functions described in Section 2 of the Agreement.
1.3. The equipment configuration tested and verified as part of UAT (per Section 4.1 of the Agreement) is recorded in the attached UAT record or as follows:
_____________________________________________
_____________________________________________
### 2. Acceptance
2.1. The Client hereby confirms its acceptance of the System in accordance with Section 8.3 of the Agreement.
2.2. Outstanding defects identified in writing before acceptance (Section 8.3), if any, are limited to those listed below, which Algolog will correct under the support and warranty provisions of Sections 6 and 14 of the Agreement:
| # | Defect description | Reference / date reported |
| --- | --- | --- |
| 1 |  |  |
| 2 |  |  |
| 3 |  |  |

If there are no outstanding defects at handover, state "NONE" in row 1 above.
2.3. Except for the items listed in 2.2 (if any), all features described in Section 2 of the Agreement are confirmed as delivered.
### 3. Payment
3.1. Algolog confirms receipt of the full and final payment under Section 5 of the Agreement, being the total project fee of N14,000,000 (Fourteen Million Naira only), receipt of the final instalment having been confirmed on ____ / ____ / 20____.
### 4. Handover of Deliverables
4.1. The Client confirms receipt of the following, each ticked on delivery:
| Received | Deliverable (per Section 3 of the Agreement) |
| --- | --- |
| ☐ | Complete System codebase (Section 7) |
| ☐ | Access credentials (administrative and deployment) |
| ☐ | Custom website with customer portal |
| ☐ | Migrated data from DriveStream, verified per Section 9 |
| ☐ | Staff accounts and permission setup |
| ☐ | Dashboards, insights and analytics |
| ☐ | Fraud-detection and reconciliation tools |
| ☐ | Wallet system |
| ☐ | Customer rewards and discounts module |
| ☐ | SOP documentation |
| ☐ | Staff training (completed on: ____ / ____ / 20____) |
| ☐ | All UI/UX screens, mobile-responsive |
| ☐ | CI/CD pipelines and Infrastructure-as-Code configuration |

4.2. On execution of this Certificate, ownership of and access to the complete System codebase vests in the Client in accordance with Section 7 of the Agreement, subject to Algolog's retained ownership of pre-existing tools, libraries, frameworks and reusable components (licensed to the Client perpetually as part of the System) and to applicable third-party and open-source licence terms.
### 5. Effect of Acceptance and Handover
5.1. The Parties confirm that acceptance and handover under this Certificate mark completion of the project under Section 8.3 of the Agreement.
5.2. In accordance with Section 15.1 of the Agreement, and except for the correction-only support and warranty in Sections 6 and 14, the Client releases Algolog from any further liability arising from the System, the codebase, or the Agreement, including any liability to refund fees or to pay damages, to the fullest extent permitted by law.
5.3. For the avoidance of doubt, the Client retains:
- twelve (12) months of technical support (Section 6), commencing on ____ / ____ / 20____;
- one (1) year of managed cloud hosting (Section 6), commencing on ____ / ____ / 20____;
- the warranty and defect-correction service (Section 14);
- full ownership of the System codebase (Section 7); and
- the benefit of the surviving provisions listed in Section 16.1 of the Agreement.
5.4. Nothing in this Certificate excludes or limits any liability that cannot lawfully be excluded or limited under applicable law (Section 15 of the Agreement).
### 6. General
6.1. This Certificate is governed by the laws of the Federal Republic of Nigeria and is subject to the dispute-resolution provisions of Section 17 of the Agreement.
6.2. Each signatory warrants that they are duly authorised to execute this Certificate on behalf of the Party for which they sign.

**For Focal Point Drycleaners (the Client)**
Name: Hassan Rilwan
Title: Director
Signature: ____________________
Date: ____________________

**For Algolog Limited**
Name: ____________________
Title: ____________________
Signature: ____________________
Date: ____________________
End of Schedule 1

# SCHEDULE 2: MILESTONE COMPLETION CHECKLIST
This Schedule is issued pursuant to Section 8.4 of the Software Development and Deployment Agreement dated 24th August 2026 ("the Agreement"). It is used at each milestone to confirm, for progress-tracking purposes, that the items due at that milestone have been completed. It does not constitute acceptance of the System, which occurs solely under Section 8.3 of the Agreement.
| Milestone (per Section 8) | Completed | Date | Client initials |
| --- | --- | --- | --- |
| Requirements & data mapping | ☐ |  |  |
| System architecture & UX sign-off | ☐ |  |  |
| Core build complete (UAT start) | ☐ |  |  |
| UAT sign-off | ☐ |  |  |
| Website & customer portal complete | ☐ |  |  |
| Testing & QA complete | ☐ |  |  |
| Data migration & go-live | ☐ |  |  |
| Staff training & handover | ☐ |  |  |

Signed for progress-tracking at the milestone(s) marked above:

**For Focal Point Drycleaners**
Name: ____________________    Signature: ____________________    Date: ____________________

**For Algolog Limited**
Name: ____________________    Signature: ____________________    Date: ____________________
End of Schedule 2
