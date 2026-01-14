# CYFT FACILITY HEALTH REPORT - MANUAL DATA ENTRY SYSTEM
# Simple Excel/Google Sheets Template + Auto-Report Generator

## SYSTEM OVERVIEW

This system has 3 components:
1. **Paper Inspection Checklist** (Inspector uses on-site)
2. **Google Sheets Data Entry Form** (You enter data after inspection)
3. **Auto-Report Generator Script** (Generates PDF with 1 click)

---

## COMPONENT 1: PAPER INSPECTION CHECKLIST

### PRINTABLE INSPECTION FORM (Give to your FM technician)

```
┌────────────────────────────────────────────────────────────┐
│  CYFT FACILITY HEALTH INSPECTION CHECKLIST                 │
│  Inspector: ____________  Date: ______________             │
└────────────────────────────────────────────────────────────┘

FACILITY INFORMATION:
Hospital/Clinic Name: _______________________________________
Address: ____________________________________________________
Contact Person: _____________________________________________
Phone: ______________________________________________________

═══════════════════════════════════════════════════════════════

INSPECTION SCORING GUIDE:
Rate each category 0-10 (then mark status):
• 9-10 points = 🟢 EXCELLENT (Green)
• 6-8 points  = 🟡 GOOD (Yellow)  
• 4-5 points  = 🟠 FAIR (Orange)
• 0-3 points  = 🔴 CRITICAL (Red)

═══════════════════════════════════════════════════════════════

1. GENERATOR HEALTH                        Score: ___/10

☐ Oil level checked           Clean ☐  Dirty ☐
☐ Battery tested             Good ☐  Weak ☐  Dead ☐
☐ Fuel quality checked       Clean ☐  Contaminated ☐
☐ Load test performed        Passed ☐  Failed ☐
☐ Exhaust system checked     Normal ☐  Excessive smoke ☐

Issues Found (check all that apply):
☐ Low oil level              ☐ Fuel contamination
☐ Dirty/dark oil             ☐ Excessive smoke
☐ Low/dead battery           ☐ Unusual noises
☐ Fuel leaks                 ☐ Corroded connections
☐ Other: _________________________________________________

Detailed Notes:
_____________________________________________________________
_____________________________________________________________
_____________________________________________________________

Photos Taken: ☐ Yes (Photo #: _______)  ☐ No

Recommendations & Costs:
☐ Oil change - ₦15,000
☐ Battery replacement - ₦35,000
☐ Full service - ₦50,000
☐ Fuel system cleaning - ₦25,000
☐ Other: _________________ - ₦__________

Status: ☐ 🟢 Excellent  ☐ 🟡 Good  ☐ 🟠 Fair  ☐ 🔴 Critical

───────────────────────────────────────────────────────────────

2. HVAC/AC SYSTEMS                         Score: ___/10

☐ All units tested           Working: _____ of _____
☐ Temperature checked        Adequate ☐  Inadequate ☐
☐ Filters inspected          Clean ☐  Dirty ☐
☐ Noise level checked        Normal ☐  Unusual sounds ☐

Issues Found:
☐ Unit(s) not cooling        ☐ Low refrigerant suspected
☐ Unusual noises             ☐ Poor airflow
☐ Water leaking              ☐ Thermostat malfunction
☐ Dirty/clogged filters      
☐ Other: _________________________________________________

Detailed Notes:
_____________________________________________________________
_____________________________________________________________
_____________________________________________________________

Photos Taken: ☐ Yes (Photo #: _______)  ☐ No

Recommendations & Costs:
☐ Filter cleaning - ₦5,000 per unit
☐ Gas refill - ₦20,000 per unit
☐ Full service - ₦30,000 per unit
☐ Compressor repair - ₦80,000+
☐ Other: _________________ - ₦__________

Status: ☐ 🟢 Excellent  ☐ 🟡 Good  ☐ 🟠 Fair  ☐ 🔴 Critical

───────────────────────────────────────────────────────────────

3. MEDICAL EQUIPMENT ENVIRONMENT           Score: ___/10

☐ Temperature monitored      Normal ☐  Too high ☐
☐ Dust levels checked        Clean ☐  Dusty ☐
☐ Ventilation checked        Adequate ☐  Poor ☐
☐ Lighting checked           Adequate ☐  Inadequate ☐

Issues Found:
☐ Temperature too high       ☐ Power fluctuations
☐ Excessive dust             ☐ Inadequate lighting
☐ Poor ventilation           ☐ Moisture/humidity
☐ Other: _________________________________________________

Detailed Notes:
_____________________________________________________________
_____________________________________________________________

Photos Taken: ☐ Yes (Photo #: _______)  ☐ No

Recommendations & Costs:
☐ Temperature monitoring - ₦25,000
☐ Deep cleaning - ₦15,000
☐ Improve ventilation - ₦40,000
☐ UPS/stabilizer - ₦100,000+
☐ Other: _________________ - ₦__________

Status: ☐ 🟢 Excellent  ☐ 🟡 Good  ☐ 🟠 Fair  ☐ 🔴 Critical

───────────────────────────────────────────────────────────────

4. WATER SYSTEMS                           Score: ___/10

☐ Pressure tested            Good ☐  Low ☐
☐ Quality checked            Clear ☐  Discolored ☐
☐ Tank inspected (external)  Clean ☐  Dirty ☐
☐ Leaks checked              None ☐  Present ☐

Issues Found:
☐ Low water pressure         ☐ No hot water
☐ Water discoloration        ☐ Pump malfunction
☐ Tank dirty (external)      
☐ Leaking pipes/taps         
☐ Other: _________________________________________________

Detailed Notes:
_____________________________________________________________
_____________________________________________________________

Photos Taken: ☐ Yes (Photo #: _______)  ☐ No

Recommendations & Costs:
☐ Tank cleaning - ₦80,000
☐ Pump repair - ₦60,000
☐ Leak repairs - ₦25,000
☐ Water treatment - ₦150,000
☐ Other: _________________ - ₦__________

Status: ☐ 🟢 Excellent  ☐ 🟡 Good  ☐ 🟠 Fair  ☐ 🔴 Critical

───────────────────────────────────────────────────────────────

5. ELECTRICAL SYSTEMS                      Score: ___/10

☐ Wiring inspected           Good ☐  Issues found ☐
☐ Outlets tested             Working: _____ of _____
☐ Lighting checked           Bulbs out: _____
☐ Circuits checked           Normal ☐  Overloaded ☐

Issues Found:
☐ Exposed/frayed wiring      ☐ Broken switches
☐ Non-functional outlets     ☐ Burned-out bulbs (count: ___)
☐ Flickering lights          ☐ Overloaded circuits
☐ Other: _________________________________________________

Detailed Notes:
_____________________________________________________________
_____________________________________________________________

Photos Taken: ☐ Yes (Photo #: _______)  ☐ No

Recommendations & Costs:
☐ Rewiring - ₦100,000+
☐ Outlet repairs - ₦15,000
☐ Bulb replacements - ₦10,000
☐ Circuit inspection - ₦30,000
☐ Other: _________________ - ₦__________

Status: ☐ 🟢 Excellent  ☐ 🟡 Good  ☐ 🟠 Fair  ☐ 🔴 Critical

───────────────────────────────────────────────────────────────

6. PLUMBING & DRAINAGE                     Score: ___/10

☐ Toilets tested             Working: _____ of _____
☐ Drains checked             Clear ☐  Slow ☐  Clogged ☐
☐ Leaks inspected            None ☐  Present ☐
☐ Odors checked              None ☐  Present ☐

Issues Found:
☐ Clogged drains             ☐ Running toilets
☐ Slow drainage              ☐ Foul odors
☐ Toilets not flushing       ☐ Visible leaks
☐ Other: _________________________________________________

Detailed Notes:
_____________________________________________________________
_____________________________________________________________

Photos Taken: ☐ Yes (Photo #: _______)  ☐ No

Recommendations & Costs:
☐ Drain cleaning - ₦25,000
☐ Toilet repairs - ₦20,000
☐ Pipe repairs - ₦30,000
☐ Septic maintenance - ₦100,000
☐ Other: _________________ - ₦__________

Status: ☐ 🟢 Excellent  ☐ 🟡 Good  ☐ 🟠 Fair  ☐ 🔴 Critical

───────────────────────────────────────────────────────────────

7. MEDICAL WASTE MANAGEMENT                Score: ___/10

☐ Yellow bins checked        Available ☐  Insufficient ☐
☐ Sharp containers checked   OK ☐  Overfilled ☐
☐ Segregation observed       Proper ☐  Improper ☐
☐ Storage area inspected     Secure ☐  Not secure ☐

Issues Found:
☐ Yellow bins missing        ☐ No labeling
☐ Sharp containers overfilled ☐ Pickup delays
☐ Improper segregation       ☐ Storage not secure
☐ Other: _________________________________________________

Detailed Notes:
_____________________________________________________________
_____________________________________________________________

Photos Taken: ☐ Yes (Photo #: _______)  ☐ No

Recommendations & Costs:
☐ Additional bins - ₦30,000
☐ Sharp containers - ₦15,000
☐ Staff training - ₦50,000
☐ Improve storage - ₦40,000
☐ Other: _________________ - ₦__________

Status: ☐ 🟢 Excellent  ☐ 🟡 Good  ☐ 🟠 Fair  ☐ 🔴 Critical

───────────────────────────────────────────────────────────────

8. FIRE SAFETY                             Score: ___/10

☐ Extinguishers counted      Total: _____
☐ Expiry dates checked       Expired: _____
☐ Exit routes inspected      Clear ☐  Blocked ☐
☐ Smoke detectors checked    Working: _____ of _____

Issues Found:
☐ Extinguishers expired (count: ___)
☐ Extinguishers not accessible
☐ Missing extinguishers      
☐ Exit routes blocked        
☐ No/broken smoke detectors  
☐ No fire drill records
☐ Other: _________________________________________________

Detailed Notes:
_____________________________________________________________
_____________________________________________________________

Photos Taken: ☐ Yes (Photo #: _______)  ☐ No

Recommendations & Costs:
☐ Extinguisher refills - ₦15,000 each
☐ New extinguishers - ₦25,000 each
☐ Smoke detectors - ₦40,000
☐ Fire safety training - ₦100,000
☐ Fire drill - ₦50,000
☐ Other: _________________ - ₦__________

Status: ☐ 🟢 Excellent  ☐ 🟡 Good  ☐ 🟠 Fair  ☐ 🔴 Critical

───────────────────────────────────────────────────────────────

9. PEST CONTROL                            Score: ___/10

☐ Droppings checked          None ☐  Present ☐
☐ Insect activity checked    None ☐  Present ☐
☐ Food storage inspected     Proper ☐  Improper ☐
☐ Last fumigation date: _________________

Issues Found:
☐ Rodent droppings visible   ☐ Gaps in doors/windows
☐ Cockroach infestation      ☐ Food storage improper
☐ Ants present               ☐ Last fumigation >3 months
☐ Flies/mosquitoes           
☐ Other: _________________________________________________

Detailed Notes:
_____________________________________________________________
_____________________________________________________________

Photos Taken: ☐ Yes (Photo #: _______)  ☐ No

Recommendations & Costs:
☐ Fumigation - ₦50,000
☐ Rodent control - ₦40,000
☐ Door/window sealing - ₦30,000
☐ Monthly prevention - ₦25,000/month
☐ Other: _________________ - ₦__________

Status: ☐ 🟢 Excellent  ☐ 🟡 Good  ☐ 🟠 Fair  ☐ 🔴 Critical

───────────────────────────────────────────────────────────────

10. CLEANLINESS & HYGIENE                  Score: ___/10

☐ Floors inspected           Clean ☐  Dirty ☐
☐ Surfaces checked           Dust-free ☐  Dusty ☐
☐ Toilets inspected          Clean ☐  Dirty ☐
☐ Sanitizers checked         Available ☐  Missing ☐

Issues Found:
☐ Dirty floors               ☐ Unpleasant odors
☐ Dusty surfaces             ☐ No hand sanitizer/soap
☐ Unclean toilets            ☐ Dirty windows
☐ Trash overflow             
☐ Other: _________________________________________________

Detailed Notes:
_____________________________________________________________
_____________________________________________________________

Photos Taken: ☐ Yes (Photo #: _______)  ☐ No

Recommendations & Costs:
☐ Deep cleaning - ₦100,000
☐ Daily cleaning improvement
☐ Additional staff needed
☐ Sanitation supplies - ₦30,000
☐ Other: _________________ - ₦__________

Status: ☐ 🟢 Excellent  ☐ 🟡 Good  ☐ 🟠 Fair  ☐ 🔴 Critical

═══════════════════════════════════════════════════════════════

OVERALL SUMMARY

Top 3 CRITICAL Issues (Must Fix Within 7 Days):

1. ___________________________________________________________
   Cost: ₦____________

2. ___________________________________________________________
   Cost: ₦____________

3. ___________________________________________________________
   Cost: ₦____________

Total Critical Repairs Cost: ₦_________________

Total All Recommendations: ₦_________________

Overall Facility Condition:
☐ Excellent - minimal interventions needed
☐ Good - routine maintenance required
☐ Fair - several issues need attention
☐ Poor - major interventions required urgently

Additional Comments:
_____________________________________________________________
_____________________________________________________________
_____________________________________________________________
_____________________________________________________________

Inspector Signature: _______________________  Date: _________

Inspection Time: Start: ______  End: ______  Duration: ______

═══════════════════════════════════════════════════════════════

PHOTO DOCUMENTATION LOG

Photo 1: __________________ (e.g., "Generator - oil level")
Photo 2: __________________ (e.g., "AC Unit 3 - water leak")
Photo 3: __________________ (e.g., "Fire extinguisher - expired")
Photo 4: __________________
Photo 5: __________________
Photo 6: __________________
Photo 7: __________________
Photo 8: __________________
Photo 9: __________________
Photo 10: _________________

Photos stored in: ☐ Phone  ☐ Camera  ☐ Cloud Drive

Transfer photos to folder: CYFT_Inspections/[Hospital Name]/[Date]

```

---

## INSTRUCTIONS FOR USING THE PAPER CHECKLIST:

**BEFORE SITE VISIT:**
1. Print 2-3 copies of this checklist
2. Attach to clipboard
3. Bring pen, camera/phone
4. Review scoring guide

**DURING INSPECTION:**
1. Work through each category systematically
2. Check boxes as you go
3. Take photos of ALL issues found
4. Write detailed notes (these go in the report!)
5. Get actual cost quotes where possible

**AFTER INSPECTION:**
1. Review checklist for completeness
2. Calculate total costs
3. Transfer data to Google Sheet (next section)
4. Upload photos to Google Drive

**TIME:** 30-45 minutes on-site

---
