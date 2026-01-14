# 🎯 CYFT FACILITY HEALTH REPORT - COMPLETE SETUP GUIDE
## Manual Data Entry → Auto-Generated Professional Report

---

## 📦 WHAT YOU'RE GETTING

This complete system allows you to:
1. **Inspect facilities** using a simple paper checklist (30-45 minutes on-site)
2. **Enter data** into Google Sheets or Excel (10 minutes in office)  
3. **Generate professional PDF reports** with 1 command (2 minutes)

**Total time: 45 minutes vs 3+ hours manually creating reports!**

---

## 📋 SYSTEM COMPONENTS

You now have **5 files** in your outputs folder:

### 1. **Manual_Inspection_Data_Entry_Template.md**
   - Printable paper checklist for your FM technician
   - Use this on-site during inspections
   - 10 categories with scoring guide

### 2. **CYFT_Facility_Health_Data_Entry_Template.csv**
   - Google Sheets/Excel template
   - Transfer paper checklist data here after inspection
   - Clear instructions for each field

### 3. **generate_report.js**
   - The "magic" script that creates the report
   - Reads your CSV data and generates beautiful DOCX
   - Requires Node.js (already installed on your computer)

### 4. **SAMPLE_Inspection_Data.csv**
   - Example of completed inspection data (Cedar Crest Hospital)
   - Use this to learn the format
   - Test the system before your first real inspection

### 5. **Cedar_Crest_Hospital_Report.docx**
   - Sample output report
   - Shows exactly what your reports will look like
   - 12-page professional document with:
     ✅ Cover page with overall score
     ✅ Executive summary
     ✅ Category breakdown with traffic lights
     ✅ Critical issues highlighted
     ✅ Cost summaries
     ✅ Detailed findings for each category
     ✅ Recommendations and next steps

---

## 🚀 STEP-BY-STEP SETUP (ONE-TIME, 30 MINUTES)

### STEP 1: SET UP GOOGLE SHEETS (15 minutes)

1. **Open Google Sheets** (https://sheets.google.com)

2. **Create New Spreadsheet**
   - Click "+ Blank"
   - Name it: "CYFT Facility Inspections Database"

3. **Import the Template**
   - Open the file: `CYFT_Facility_Health_Data_Entry_Template.csv`
   - In Google Sheets: File → Import → Upload → Select the CSV file
   - Import location: "Replace current sheet"
   - Click "Import data"

4. **Format for Easy Data Entry**
   
   **Make it look like this:**
   
   | Column A (FIELD) | Column B (VALUE) | Column C (INSTRUCTIONS) |
   |------------------|------------------|-------------------------|
   | Hospital/Clinic Name | *[Enter here]* | Enter full official name |
   | Address | *[Enter here]* | Complete address |
   | Generator Score (0-10) | *[Enter here]* | Rate 0-10 based on condition |
   
   - **Freeze Row 1**: View → Freeze → 1 row (so headers stay visible)
   - **Color-code sections**: 
     - Blue background for FACILITY INFO rows
     - Green background for each CATEGORY header
     - Yellow background for SUMMARY rows
   - **Widen Column B**: Make it wide enough for long notes
   - **Add Data Validation** (optional but helpful):
     - For "Status" cells: Data → Data validation → List of items: "Excellent, Good, Fair, Critical"
     - For "Score" cells: Number between 0 and 10

5. **Create Template for Each Inspection**
   - Make a copy of this sheet for each new inspection
   - Name format: "Hospital_Name_Date" (e.g., "Cedar_Crest_12Jan2026")
   - Keep the original template blank

6. **Save Your Spreadsheet**
   - It auto-saves to Google Drive
   - Share with your data entry staff if needed

---

### STEP 2: PRINT PAPER CHECKLISTS (5 minutes)

1. **Open**: `Manual_Inspection_Data_Entry_Template.md`

2. **Print Multiple Copies**
   - Print 10-20 copies
   - Use clipboard for on-site inspections
   - Keep extras in your vehicle

3. **Optional: Create Laminated Master**
   - Print one copy
   - Laminate it
   - Use dry-erase markers for quick checks
   - Photo the completed checklist instead of paper

---

### STEP 3: SET UP REPORT GENERATOR (10 minutes)

1. **Check Node.js is Installed**
   Open Terminal/Command Prompt and type:
   ```bash
   node --version
   ```
   Should show: `v18.x.x` or similar
   
   If not installed:
   - Windows: Download from https://nodejs.org
   - Mac: `brew install node`
   - Linux: `sudo apt install nodejs npm`

2. **Install the docx Library**
   ```bash
   npm install -g docx
   ```
   This installs the report generation library.

3. **Test the System**
   Navigate to your outputs folder and run:
   ```bash
   node generate_report.js SAMPLE_Inspection_Data.csv Test_Report.docx
   ```
   
   You should see:
   ```
   ✅ Report generated successfully: Test_Report.docx
   
   Report Summary:
   - Hospital: Cedar Crest Hospital
   - Overall Score: 76/100 (GOOD)
   - Critical Repairs Cost: ₦115,000
   - Total Recommendations: ₦605,000
   ```

4. **Open Test_Report.docx**
   - Should be a beautiful 12-page report
   - If it looks good, you're ready!

---

## 📝 DAILY WORKFLOW (PER INSPECTION)

### PHASE 1: ON-SITE INSPECTION (30-45 minutes)

1. **Your FM Technician Goes to Hospital**
   - Brings: Paper checklist, pen, camera/phone, basic tools
   - Duration: 30-45 minutes

2. **Walks Through 10 Categories**
   - Scores each 0-10
   - Checks boxes for issues found
   - Takes photos of every problem
   - Writes detailed notes
   - Lists recommendations with costs

3. **Returns to Office**
   - Has completed paper checklist
   - Has 10-20 photos on phone
   - Ready for data entry

---

### PHASE 2: DATA ENTRY (10 minutes)

**You or admin staff at computer:**

1. **Open Google Sheets**
   - Go to: "CYFT Facility Inspections Database"
   - Make a copy of the blank template
   - Name it: "Hospital_Name_Date"

2. **Enter Data from Paper Checklist**
   - Work through Column B, top to bottom
   - Copy exactly what's on the paper
   - For "Issues Found": Type them separated by semicolons
   - For "Recommendations": Include costs like "Oil change - ₦15000; Battery - ₦35000"
   - Takes 10 minutes if checklist is clear

3. **Upload Photos to Google Drive** (optional for now)
   - Create folder: "CYFT_Inspections/Hospital_Name/Date"
   - Upload all photos
   - Note filenames in the "Photo Filename" fields

4. **Download as CSV**
   - File → Download → Comma Separated Values (.csv)
   - Save as: "HospitalName_Date.csv"
   - Save to your outputs folder (where generate_report.js is)

---

### PHASE 3: GENERATE REPORT (2 minutes)

1. **Open Terminal/Command Prompt**
   - Navigate to your outputs folder:
   ```bash
   cd /path/to/outputs/folder
   ```

2. **Run the Generator**
   ```bash
   node generate_report.js HospitalName_Date.csv HospitalName_Report.docx
   ```
   
   Example:
   ```bash
   node generate_report.js CedarCrest_12Jan2026.csv CedarCrest_Report.docx
   ```

3. **Wait 2 Seconds**
   ```
   Reading inspection data...
   Calculating overall score...
   Building document...
   Generating DOCX file...
   ✅ Report generated successfully: CedarCrest_Report.docx
   ```

4. **Open the Report**
   - Double-click the DOCX file
   - Preview in Word/Google Docs
   - Looks professional? ✅
   - Ready to send to client!

5. **Convert to PDF** (if needed)
   - Open DOCX in Word/Google Docs
   - File → Download/Save As → PDF
   - Or just send the DOCX (most clients prefer editable format)

---

## 💡 PRO TIPS FOR EFFICIENT WORKFLOW

### FOR YOUR FM TECHNICIAN (Field Work)

1. **Use Voice-to-Text**
   - For "Detailed Notes" sections on paper
   - Record voice memo on phone
   - Transcribe later (or have admin do it)
   - Saves 10 minutes on-site

2. **Photo Naming Convention**
   - Immediately rename photos: "Generator_Issue", "AC_Unit3", "FireExtinguisher"
   - Makes data entry easier
   - Example: Don't leave as "IMG_2543.jpg"

3. **Bring Printed Cost List**
   - Standard costs for common repairs
   - Oil change: ₦15K, Battery: ₦35K, AC gas: ₦20K, etc.
   - No guessing, just check the list

4. **Fill Critical Issues ON-SITE**
   - Don't wait till you return to office
   - Identify top 3 issues while inspecting
   - Write costs immediately

### FOR DATA ENTRY PERSON (Office Work)

1. **Use Copy-Paste**
   - Technician's handwriting unclear?
   - Have them WhatsApp you a voice note
   - Type while listening (faster than deciphering handwriting)

2. **Standard Phrases Library**
   - Keep a document of common descriptions:
     - "Generator oil dark, needs change"
     - "AC unit not cooling adequately"
     - "Fire extinguisher expired"
   - Copy-paste instead of retyping
   - Ensures consistency

3. **Double-Check Numbers**
   - Scores (0-10)
   - Costs (no commas in CSV: use 15000 not 15,000)
   - Phone numbers
   - Dates (format: DD/MM/YYYY)

4. **Save Multiple Versions**
   - Google Sheets auto-saves
   - But also download CSV after completion
   - Keep local backup

---

## 🎨 CUSTOMIZING THE REPORT

### EASY CUSTOMIZATIONS (No Coding Required)

**Change Contact Info:**
1. Open `generate_report.js` in any text editor
2. Find line ~970: `'Email: info@cyftconsulting.com'`
3. Change to your actual email
4. Find line ~980: `'Website: www.cyftconsulting.com'`
5. Change to your actual website
6. Save file

**Change Company Name in Header:**
1. Find line ~190: `'CYFT CONSULTING LIMITED - Facility Health Report'`
2. Change to your preferred header text
3. Save

**Change Report Title Color:**
1. Find line ~335: `color: '1976D2'` (this is blue)
2. Change to:
   - Red: `'D32F2F'`
   - Green: `'388E3C'`
   - Orange: `'F57C00'`
   - Purple: `'7B1FA2'`
3. Save

### ADVANCED CUSTOMIZATIONS (Requires Basic JavaScript)

**Add Your Company Logo:**
1. Put your logo file (PNG/JPG) in outputs folder
2. In generate_report.js, add after line 330:
```javascript
new Paragraph({
    alignment: AlignmentType.CENTER,
    children: [new ImageRun({
        type: "png",
        data: fs.readFileSync("your_logo.png"),
        transformation: { width: 200, height: 100 }
    })]
}),
```

**Change Scoring Thresholds:**
Currently: 90+=Excellent, 70-89=Good, 50-69=Fair, <50=Critical

Find line ~20 in generate_report.js:
```javascript
function getStatus(score) {
    if (score >= 90) return { emoji: '🟢', text: 'EXCELLENT', color: '4CAF50' };
    if (score >= 70) return { emoji: '🟡', text: 'GOOD', color: 'FFC107' };
    if (score >= 50) return { emoji: '🟠', text: 'FAIR', color: 'FF9800' };
    return { emoji: '🔴', text: 'CRITICAL', color: 'F44336' };
}
```
Change the numbers to your preference.

---

## 🐛 TROUBLESHOOTING

### Problem: "node: command not found"
**Solution:** Node.js not installed
```bash
# Windows: Download from https://nodejs.org
# Mac:
brew install node
# Linux:
sudo apt install nodejs npm
```

### Problem: "Cannot find module 'docx'"
**Solution:** docx library not installed
```bash
npm install -g docx
```

### Problem: "File not found" error
**Solution:** CSV file not in same folder as generate_report.js
- Make sure both files are in the same directory
- Or provide full path:
```bash
node generate_report.js "/full/path/to/file.csv" output.docx
```

### Problem: Report shows "[Hospital Name]" instead of actual name
**Solution:** CSV field name doesn't match
- Open CSV in text editor
- First column must be exactly: `Hospital/Clinic Name`
- Not "Hospital Name" or "Clinic Name"
- Match the template exactly

### Problem: Scores showing as 0/100
**Solution:** Score entered incorrectly in CSV
- Scores must be numbers: `8.5` not "8.5/10" or "85%"
- Range: 0 to 10 (converts to 0-100 automatically)
- Check: `Generator Score (0-10)` field has just a number

### Problem: Report looks weird in Word
**Solution:** Font or compatibility issue
- Open in Google Docs instead (upload to Google Drive)
- Or update Microsoft Word to latest version
- Or convert to PDF first

---

## 📊 SCALING UP YOUR OPERATION

### MONTH 1-3: Manual Process (1-3 inspections/week)
- Print paper checklists
- Manual data entry to Google Sheets
- Run script locally
- **Time per report: 45 minutes**
- **Capacity: 12 reports/month**

### MONTH 4-6: Semi-Automated (5-10 inspections/week)
- Train admin staff on data entry
- Create standard phrase library
- Batch generate reports (do 5 on Friday afternoon)
- **Time per report: 30 minutes**
- **Capacity: 40 reports/month**

### MONTH 7+: Fully Automated (20+ inspections/week)
**Option A: Google Forms (Recommended)**
- Use the form setup guide I provided earlier
- Technician fills form on phone during inspection
- Auto-populates Google Sheets
- You just click "Generate Report"
- **Time per report: 5 minutes**
- **Capacity: Unlimited**

**Option B: Hire Data Entry VA**
- Hire part-time Virtual Assistant
- They do ALL data entry
- You just review and generate
- **Cost: ₦30K-50K/month**
- **Your time per report: 5 minutes**

---

## 💰 PRICING YOUR SERVICE

### STANDARD PRICING (Based on Report Value)

**Tier 1: Basic Health Check** - ₦50,000/month
- Monthly inspection using this system
- 12-page professional report
- Email delivery
- Perfect for: Small clinics, diagnostic centers

**Tier 2: Standard Package** - ₦80,000/month
- Everything in Basic
- 30-minute review meeting with management
- WhatsApp support between inspections
- Perfect for: Medium hospitals, nursing homes

**Tier 3: Premium Package** - ₦120,000/month
- Everything in Standard
- Bi-weekly quick checks (brief inspections)
- Priority emergency consultation
- Quarterly trend analysis (compare 3 months of scores)
- Perfect for: Large hospitals, medical centers

**UPSELLS:**
- Photo documentation: +₦10,000 (include actual photos in report)
- Same-day report delivery: +₦15,000
- Additional inspection mid-month: +₦25,000
- Annual comprehensive audit: ₦500,000 (one-time)

### VALUE PROPOSITION TO CLIENTS:

**ROI Pitch:**
```
"Our ₦50,000/month Facility Health Check saves you:
✅ ₦200,000+ in prevented emergency repairs
✅ ₦150,000 in energy savings (we identify waste)
✅ ZERO downtime during HEFAMAA inspections
✅ Peace of mind knowing facility is monitored

That's ₦350,000 savings for ₦50,000 investment = 7X ROI

Plus: Insurance companies love this documentation 
(may reduce your premium by 10-15%)

First month FREE - see the value yourself!"
```

---

## 📅 QUICK REFERENCE CARD (PRINT THIS!)

```
┌────────────────────────────────────────────────┐
│  CYFT FACILITY HEALTH REPORT - QUICK GUIDE    │
└────────────────────────────────────────────────┘

STEP 1: ON-SITE INSPECTION
[ ] Print paper checklist
[ ] Bring: pen, camera, tools, clipboard
[ ] Score 10 categories (0-10 each)
[ ] Take photos of all issues
[ ] Write detailed notes
[ ] List recommendations with costs
[ ] Duration: 30-45 minutes

STEP 2: DATA ENTRY
[ ] Open Google Sheets template
[ ] Make copy: "HospitalName_Date"
[ ] Transfer paper data to Column B
[ ] Double-check all numbers
[ ] Download as CSV
[ ] Save to outputs folder
[ ] Duration: 10 minutes

STEP 3: GENERATE REPORT
[ ] Open Terminal
[ ] cd to outputs folder
[ ] Run: node generate_report.js file.csv output.docx
[ ] Wait 2 seconds
[ ] Open generated DOCX
[ ] Review for accuracy
[ ] Send to client!
[ ] Duration: 2 minutes

TOTAL TIME: 45 MINUTES PER REPORT

TROUBLESHOOTING:
• "Command not found" → Install Node.js
• "Module not found" → npm install -g docx
• Zeros in report → Check score format (0-10)
• Wrong hospital name → Check CSV field names

CONTACT: [Your Phone] | [Your Email]
```

---

## 🎯 YOUR NEXT STEPS (DO THIS NOW!)

### ✅ TODAY (30 minutes):
1. [ ] Print 10 paper checklists
2. [ ] Test the system with sample data
3. [ ] Generate the Cedar Crest sample report
4. [ ] Review the report quality
5. [ ] Customize contact info in script

### ✅ THIS WEEK (2 hours):
1. [ ] Set up Google Sheets properly
2. [ ] Train your FM technician on paper checklist
3. [ ] Do your first real inspection (practice on your own office!)
4. [ ] Enter data and generate first real report
5. [ ] Show report to 3 potential clients

### ✅ THIS MONTH (Launch):
1. [ ] Book 3 FREE first inspections with hospitals
2. [ ] Generate 3 professional reports
3. [ ] Get testimonials
4. [ ] Sign first 2 paying clients
5. [ ] Start monthly recurring revenue!

---

## 📞 NEED HELP?

**Common Questions:**

Q: Can I use Excel instead of Google Sheets?
A: Yes! Excel works perfectly. Just save as CSV when done.

Q: Do I need internet to generate reports?
A: No! Once Node.js and docx are installed, it works offline.

Q: Can I brand the report with my logo?
A: Yes! See "Advanced Customizations" section above.

Q: What if I have more than 10 categories?
A: Easy to add! Duplicate one category's code in the script.

Q: Can I automate photo insertion?
A: Yes, but requires coding. Start with manual for now.

Q: How do I backup my data?
A: Google Sheets auto-saves. Download CSVs weekly as backup.

---

## 🚀 SUCCESS METRICS (Track These!)

**OPERATIONAL:**
- Reports generated per week: Target 5+
- Time per report: Target <45 minutes
- Data entry accuracy: Target 95%+
- Client satisfaction: Target 4.5/5+

**FINANCIAL:**
- Monthly recurring revenue: Target ₦500K+ (10 clients)
- Report generation cost: ₦0 (system is free!)
- Gross profit margin: 95%+
- ROI on system setup time: Infinite!

---

**FINAL REMINDER:**

You now have a COMPLETE, PROFESSIONAL facility health reporting system that:
✅ Costs ₦0 to operate
✅ Generates unlimited reports
✅ Produces 12-page professional documents
✅ Saves 2+ hours per report
✅ Impresses clients immediately
✅ Scales infinitely

**GO SELL THIS SERVICE!** 💰

The hardest part (building the system) is DONE.
Now you just need to DO INSPECTIONS and GENERATE REPORTS.

Your first ₦500K/month in recurring revenue is 10 hospital clients away.
At ₦50K each, that's ONE new client every 3 days this month.

You got this! 🎯
```
