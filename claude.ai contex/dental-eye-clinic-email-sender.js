/**
 * Dental & Eye Clinic Cold Outreach — Google Apps Script
 *
 * SETUP:
 * 1. Open Google Sheets with the clinic contact list
 * 2. Go to Extensions > Apps Script
 * 3. Paste this code
 * 4. Update SENDER_NAME and SENDER_EMAIL
 * 5. Run sendFirstTouch() for Day 1 emails
 * 6. Run sendFollowUp() on Day 4
 * 7. Run sendFinalTouch() on Day 8
 *
 * SHEET FORMAT:
 * Column A: Company Name
 * Column B: Type (Dental/Eye)
 * Column C: Email
 * Column D: Phone
 * Column E: Location
 * Column F: Status (New/Sent Touch 1/Sent Touch 2/Sent Touch 3)
 * Column G: Notes
 */

const SENDER_NAME = "Fayinminu Femi";
const SENDER_EMAIL = "ffayinminu@algolog.co";
const SHEET_NAME = "Sheet1";

function getSheet() {
  return SpreadsheetApp.getActiveSpreadsheet().getSheetByName(SHEET_NAME);
}

function sendFirstTouch() {
  const sheet = getSheet();
  const data = sheet.getDataRange().getValues();
  let sent = 0;

  for (let i = 1; i < data.length; i++) {
    const clinicName = data[i][0];
    const email = data[i][2];
    const status = data[i][5];

    if (!email || email.trim() === "" || status === "Sent Touch 1" || status === "Sent Touch 2" || status === "Sent Touch 3") {
      continue;
    }

    const subject = `A question about ${clinicName}`;
    const body = `Hi,

Quick question — when a potential patient sends your clinic a WhatsApp message at 9pm on a Saturday, what happens?

For most practices in Abuja, the answer is: nothing until Monday morning. By then, the patient has already booked somewhere else.

We've built a system that responds to every enquiry instantly — WhatsApp, Instagram, Google Maps — 24 hours a day, 7 days a week. It answers patient questions, shares your services and pricing, and books appointments automatically. After the visit, it follows up, prompts rebooking, and requests Google reviews.

It's live within 7 days. No disruption to your current operations.

Would it be worth 10 minutes to show you how it works for a practice like ${clinicName}?

Best regards,
${SENDER_NAME}
Algolog Limited
hello@algolog.co | algolog.co`;

    try {
      GmailApp.sendEmail(email, subject, body, {
        name: SENDER_NAME,
        replyTo: SENDER_EMAIL
      });
      sheet.getRange(i + 1, 6).setValue("Sent Touch 1");
      sheet.getRange(i + 1, 7).setValue("Touch 1: " + new Date().toLocaleDateString());
      sent++;
      Utilities.sleep(3000); // 3 second delay between emails
    } catch (e) {
      sheet.getRange(i + 1, 7).setValue("ERROR: " + e.message);
    }
  }

  Logger.log(`First touch sent to ${sent} clinics`);
}

function sendFollowUp() {
  const sheet = getSheet();
  const data = sheet.getDataRange().getValues();
  let sent = 0;

  for (let i = 1; i < data.length; i++) {
    const clinicName = data[i][0];
    const email = data[i][2];
    const status = data[i][5];

    if (!email || email.trim() === "" || status !== "Sent Touch 1") {
      continue;
    }

    const subject = `Re: A question about ${clinicName}`;
    const body = `Hi,

Following up on my earlier note. I know you're busy — that's actually the point.

Every hour your team spends answering routine WhatsApp questions ("How much is a cleaning?", "Do you take walk-ins?", "What are your hours?") is an hour they're not spending with patients.

Our system handles those conversations automatically — in a natural, conversational way — so your team focuses on the patients who are already in your chairs.

Here's what it covers:
• Instant replies to WhatsApp and Instagram enquiries (24/7)
• Automated appointment booking and confirmation
• No-show reduction (24hr + morning-of reminders)
• Post-visit follow-up and Google review requests
• Recall reminders for routine visits

Live in 7 days. If it doesn't improve your bookings in 30 days, the first month is free.

Worth a quick look?

Best regards,
${SENDER_NAME}
Algolog Limited
hello@algolog.co | algolog.co`;

    try {
      GmailApp.sendEmail(email, subject, body, {
        name: SENDER_NAME,
        replyTo: SENDER_EMAIL
      });
      sheet.getRange(i + 1, 6).setValue("Sent Touch 2");
      sheet.getRange(i + 1, 7).setValue("Touch 2: " + new Date().toLocaleDateString());
      sent++;
      Utilities.sleep(3000);
    } catch (e) {
      sheet.getRange(i + 1, 7).setValue("ERROR: " + e.message);
    }
  }

  Logger.log(`Follow-up sent to ${sent} clinics`);
}

function sendFinalTouch() {
  const sheet = getSheet();
  const data = sheet.getDataRange().getValues();
  let sent = 0;

  for (let i = 1; i < data.length; i++) {
    const clinicName = data[i][0];
    const email = data[i][2];
    const status = data[i][5];

    if (!email || email.trim() === "" || status !== "Sent Touch 2") {
      continue;
    }

    const subject = `Last note from me — ${clinicName}`;
    const body = `Hi,

Last message from me on this — I don't want to be a nuisance.

The short version: we help dental and eye clinics in Abuja capture every patient enquiry (even at midnight), reduce no-shows with automated reminders, and bring patients back for routine visits with recall prompts.

One of the practices we work with told us: "We didn't realise how many enquiries we were losing until we saw the system catch them."

If you'd like to see a 10-minute demo using your own services and pricing, I'm happy to set that up. If not, no hard feelings at all.

Best regards,
${SENDER_NAME}
Algolog Limited
hello@algolog.co | algolog.co`;

    try {
      GmailApp.sendEmail(email, subject, body, {
        name: SENDER_NAME,
        replyTo: SENDER_EMAIL
      });
      sheet.getRange(i + 1, 6).setValue("Sent Touch 3");
      sheet.getRange(i + 1, 7).setValue("Touch 3: " + new Date().toLocaleDateString());
      sent++;
      Utilities.sleep(3000);
    } catch (e) {
      sheet.getRange(i + 1, 7).setValue("ERROR: " + e.message);
    }
  }

  Logger.log(`Final touch sent to ${sent} clinics`);
}
