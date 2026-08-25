/**
 * TOPSCHOOL - nurture drip (Google Apps Script, bound to the Sheet)
 *
 * Sends a DIFFERENT email every 4 days, up to 5 emails per lead, and tracks
 * each lead so nobody ever repeats a step. Step 1 is a re-introduction that
 * explains what TOPSCHOOL is, anchored on results compilation + report cards.
 *
 * Sheet tab must be named "Leads" with these headers on row 1:
 *   School | Contact Name | Email | WhatsApp | Stage | Pupils | Signed Up |
 *   Send? | Note | Email Status | Sent At | Error
 * The script adds these columns automatically the first time it runs:
 *   Step Sent | Next Send | Reintro Sent
 *
 * Menu (after you reload the sheet): TOPSCHOOL
 *   - Preview all 5 emails to myself
 *   - Send re-intro to EVERYONE now   (one-off blast of the Step 1 re-intro)
 *   - Send due emails now             (sends whatever step each lead is due for)
 *   - Turn ON 4-day automation        (auto-sends daily; each lead every 4 days)
 *   - Turn OFF automation
 *   - Reset selected rows             (clears a lead's progress)
 *
 * Typical use now: run "Send re-intro to EVERYONE now" once so every current
 * school gets the re-introduction, then leave the 4-day automation on so new
 * signups start at the re-intro and everyone flows through the series.
 */

// ---------- CONFIG ----------
var CFG = {
  SHEET_NAME: 'Leads',
  SENDER_NAME: 'Femi from TOPSCHOOL',
  REPLY_TO: 'ffayinminu@algolog.co',
  CC: '',
  BANNER_FILE_ID: '16AQDQWLZgq7H_EpSegwogw44JANsXCFm',
  START_URL: 'https://topschool.app/start',
  DAYS_BETWEEN: 4,
  DAILY_CAP: 250,        // max emails per run
  PAUSE_MS: 1200,        // gap between sends
  AUTOMATION_HOUR: 9,    // hour of day the automation runs
  TEST_EMAIL: 'ffayinminu@algolog.co'
};

// The 5 emails. subject + cta label + body paragraphs (plain sentences).
// Step 1 is the re-introduction (results compilation + report cards).
var STEPS = [
  {
    subject: 'COMPILE RESULTS AND PRINT REPORT CARDS IN MINUTES',
    cta: 'See how it works',
    paras: [
      "A little while ago you created a TOPSCHOOL account at topschool.app, so here is a quick reminder of what it does for your school, and why it is worth a first look before the term gets busy.",
      "TOPSCHOOL is a school management app built for Nigerian schools, and the part most proprietors love is how it handles end of term. You enter each pupil's scores once, and TOPSCHOOL works out the totals, averages, subject positions and class positions for you, with no manual adding or sorting.",
      "The moment the results are in, it also generates clean, branded report cards you can print or share, complete with teacher and head-teacher comments, in minutes instead of days.",
      "So the week you would normally lose to compiling results and writing report cards becomes an afternoon, with fewer mistakes and a smarter finish for parents. Your account is already set up, and we can import your pupil and class lists for you in about 10 minutes, at no cost."
    ]
  },
  {
    subject: 'YOU ARE DOING THE WORK OF FIVE PEOPLE',
    cta: 'Pick up where you left off',
    paras: [
      "Look at an ordinary day for you. You are marking the register, sorting out fees, answering parents, keeping records, checking what each class is doing, and somehow still running the school on top of it all. One person carrying the work of five. By evening you are drained, and tomorrow starts the same way.",
      "That load does not ease off. It grows every term as the school grows.",
      "TOPSCHOOL lifts a large part of it off your shoulders. Pupils, attendance and fees sit in one place you manage from your phone, and the system handles the counting, totalling and record-keeping you do by hand today. You spend less of your day buried in paperwork and more of it actually running the school.",
      "You already created your account, so the hard part is done. We can also import your pupil and class lists for you, in about 10 minutes, at no cost."
    ]
  },
  {
    subject: 'WHO OWES YOU FEES RIGHT NOW?',
    cta: 'Set up your fees',
    paras: [
      "A quick question. Without opening a single notebook, can you say exactly which parents are owing fees this term, and how much?",
      "For most schools the honest answer is no, and that gap is where money quietly leaks out all session long. A missed entry here, an unpaid balance nobody chased there, a parent who says they already paid.",
      "TOPSCHOOL records every fee and payment as it happens, and shows you who has paid and who is owing. When a parent says they paid, you see the truth in seconds, all from your phone.",
      "Your account is ready. Add your classes and fees and you will see your money clearly from day one."
    ]
  },
  {
    subject: 'YOUR PARENTS ARE COMPARING YOU',
    cta: 'See what parents would see',
    paras: [
      "Parents talk to each other, and more of them now expect to follow their child on their phone: attendance, results and fees, as they happen.",
      "When the school down the road offers that and you are still sending a paper slip at the end of term, you look behind, even when your teaching is better. To a parent, the other school simply looks more serious.",
      "TOPSCHOOL puts your school on every parent's phone. Each parent sees only their own child, their own results, their own fees, and nothing about anyone else's child. A small school starts to look sharp very quickly.",
      "You have already signed up. Add your pupils and parents and your school is on their phone this week."
    ]
  },
  {
    subject: 'ONE NOTEBOOK AWAY FROM A CRISIS',
    cta: 'Put your school in one place',
    paras: [
      "Ask yourself where your school's records really sit today. For a lot of schools it is one big notebook, one laptop, and what a few staff carry in their heads.",
      "So when you want a simple answer, how many pupils are owing, who was absent this week, you cannot get it quickly. And if that notebook goes missing or the laptop crashes, a frightening amount of your school goes with it.",
      "TOPSCHOOL keeps pupils, results, attendance and fees in one place you open from your phone, instead of trapped in one book or one machine that can be lost. The answers are already there, without chasing anyone.",
      "Your account is set up. Move your records in once and stop carrying that risk."
    ]
  }
];
// ----------------------------

function esc_(t) {
  return String(t).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;');
}

function buildPlain_(name, step) {
  var out = ['Hello ' + name + ','];
  out.push('');
  for (var i = 0; i < step.paras.length; i++) { out.push(step.paras[i]); out.push(''); }
  out.push(step.cta + ': ' + CFG.START_URL);
  out.push('');
  out.push('If you would like us to set it up with you, just reply to this email');
  out.push('or call us on +2348103698758 and we will arrange a short time.');
  out.push('');
  out.push('Femi from TOPSCHOOL');
  return out.join('\n');
}

function buildHtml_(name, step) {
  var p = 'style="margin:0 0 15px;"';
  var body = [];
  for (var i = 0; i < step.paras.length; i++) {
    body.push('<p ' + p + '>' + esc_(step.paras[i]) + '</p>');
  }
  return [
    '<div style="background:#eef1f6;padding:26px 12px;font-family:Arial,Helvetica,sans-serif;">',
    '<div style="max-width:600px;margin:0 auto;background:#ffffff;border:1px solid #e3e7ef;',
    'border-radius:12px;overflow:hidden;">',
    '<img src="cid:banner" alt="TOPSCHOOL" style="width:100%;max-width:600px;height:auto;display:block;">',
    '<div style="padding:30px 32px 26px;color:#25324d;font-size:15px;line-height:1.62;">',
    '<p style="margin:0 0 18px;font-size:19px;font-weight:bold;color:#1B2A4A;">Hello ' + esc_(name) + ',</p>',
    body.join(''),
    '<div style="text-align:center;margin:28px 0 22px;">',
    '<a href="' + CFG.START_URL + '" style="background:#1B2A4A;color:#ffffff;text-decoration:none;',
    'padding:14px 30px;border-radius:8px;display:inline-block;font-weight:bold;font-size:15px;">',
    esc_(step.cta) + '</a>',
    '</div>',
    '<p ' + p + '>If you would like us to set it up with you, just reply to this email or call us',
    ' on <a href="tel:+2348103698758" style="color:#1B2A4A;font-weight:bold;text-decoration:none;">',
    '+234 810 369 8758</a> and we will arrange a short time.</p>',
    '<p style="margin:22px 0 0;">Femi from TOPSCHOOL</p>',
    '</div>',
    '<div style="background:#1B2A4A;color:#c7d0e2;font-size:12px;line-height:1.5;',
    'padding:16px 32px;text-align:center;">',
    'TOPSCHOOL &middot; Nigerian School Management App &middot; topschool.app<br>Call: +234 810 369 8758',
    '</div>',
    '</div>',
    '</div>'
  ].join('');
}

function getBanner_() {
  try { return DriveApp.getFileById(CFG.BANNER_FILE_ID).getBlob().setName('banner'); }
  catch (e) { return null; }
}

function sendStep_(to, name, stepIndex, banner) {
  var step = STEPS[stepIndex - 1];
  var opts = { name: CFG.SENDER_NAME, replyTo: CFG.REPLY_TO,
               htmlBody: buildHtml_(name, step) };
  if (CFG.CC) opts.cc = CFG.CC;
  if (banner) opts.inlineImages = { banner: banner };
  GmailApp.sendEmail(to, step.subject, buildPlain_(name, step), opts);
}

function onOpen() {
  SpreadsheetApp.getUi()
    .createMenu('TOPSCHOOL')
    .addItem('Preview all 5 emails to myself', 'previewAll')
    .addSeparator()
    .addItem('Send re-intro to EVERYONE now', 'broadcastReintro')
    .addItem('Send due emails now', 'runCampaign')
    .addSeparator()
    .addItem('Turn ON 4-day automation', 'setupAutomation')
    .addItem('Turn OFF automation', 'removeAutomation')
    .addSeparator()
    .addItem('Reset selected rows', 'resetSelected')
    .addToUi();
}

function sheet_() {
  var ss = SpreadsheetApp.getActive();
  return ss.getSheetByName(CFG.SHEET_NAME) || ss.getActiveSheet();
}

// Returns a header->index map, adding any missing columns to row 1.
function cols_(sh) {
  var lastCol = sh.getLastColumn();
  var headers = sh.getRange(1, 1, 1, lastCol).getValues()[0];
  var m = {};
  for (var i = 0; i < headers.length; i++) m[String(headers[i]).trim()] = i;
  var core = ['Email', 'Contact Name', 'Send?'];
  for (var k = 0; k < core.length; k++) {
    if (m[core[k]] === undefined) throw new Error('Missing column: ' + core[k] +
      '. Make sure the tab is named "Leads" and has the header row.');
  }
  var ensure = ['Email Status', 'Sent At', 'Error', 'Step Sent', 'Next Send', 'Reintro Sent'];
  for (var e = 0; e < ensure.length; e++) {
    if (m[ensure[e]] === undefined) {
      lastCol += 1;
      sh.getRange(1, lastCol).setValue(ensure[e]);
      m[ensure[e]] = lastCol - 1;
    }
  }
  return m;
}

function validEmail_(email) {
  return /^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(email) && email.indexOf('.vom') === -1;
}

function previewAll() {
  var banner = getBanner_();
  for (var s = 1; s <= STEPS.length; s++) sendStep_(CFG.TEST_EMAIL, 'there', s, banner);
  SpreadsheetApp.getActive().toast('Sent all ' + STEPS.length + ' preview emails to ' + CFG.TEST_EMAIL);
}

// One-off blast of the Step 1 re-introduction to every Send?=YES lead that has
// not already received it. Idempotent: a "Reintro Sent" date guards repeats.
// Leads still at step 0 are advanced to step 1 so the normal drip does not
// resend the re-intro; leads already mid-series keep their place.
function broadcastReintro() {
  var sh = sheet_();
  var c = cols_(sh);
  var vals = sh.getDataRange().getValues();
  var now = new Date();
  var quota = MailApp.getRemainingDailyQuota();
  var banner = getBanner_();
  var sent = 0, skipped = 0, failed = 0, already = 0;

  for (var r = 1; r < vals.length; r++) {
    if (sent >= CFG.DAILY_CAP || sent >= quota) break;
    var row = vals[r];
    var send = String(row[c['Send?']]).trim().toUpperCase();
    if (send !== 'YES' && send !== 'TRUE') continue;
    if (String(row[c['Reintro Sent']]).trim() !== '') { already++; continue; }

    var email = String(row[c['Email']]).trim();
    if (!validEmail_(email)) {
      sh.getRange(r + 1, c['Email Status'] + 1).setValue('Skipped');
      sh.getRange(r + 1, c['Error'] + 1).setValue('Invalid email');
      skipped++; continue;
    }
    var name = String(row[c['Contact Name']] || '').trim() || 'there';
    try {
      sendStep_(email, name, 1, banner);            // STEPS[0] = re-intro
      sh.getRange(r + 1, c['Reintro Sent'] + 1).setValue(now);
      var step = parseInt(row[c['Step Sent']], 10) || 0;
      if (step < 1) {
        sh.getRange(r + 1, c['Step Sent'] + 1).setValue(1);
        sh.getRange(r + 1, c['Next Send'] + 1).setValue(
          new Date(now.getTime() + CFG.DAYS_BETWEEN * 86400000));
      }
      sh.getRange(r + 1, c['Email Status'] + 1).setValue('Re-intro sent');
      sh.getRange(r + 1, c['Sent At'] + 1).setValue(now);
      sh.getRange(r + 1, c['Error'] + 1).setValue('');
      sent++;
      Utilities.sleep(CFG.PAUSE_MS);
    } catch (err) {
      sh.getRange(r + 1, c['Email Status'] + 1).setValue('Failed re-intro');
      sh.getRange(r + 1, c['Error'] + 1).setValue(String(err));
      failed++;
    }
  }
  SpreadsheetApp.getActive().toast(
    'Re-intro: sent ' + sent + ' | skipped ' + skipped + ' | failed ' + failed +
    ' | already had it ' + already, 'TOPSCHOOL', 8);
}

function runCampaign() {
  var sh = sheet_();
  var c = cols_(sh);
  var vals = sh.getDataRange().getValues();
  var now = new Date();
  var quota = MailApp.getRemainingDailyQuota();
  var banner = getBanner_();
  var sent = 0, skipped = 0, failed = 0, done = 0;

  for (var r = 1; r < vals.length; r++) {
    if (sent >= CFG.DAILY_CAP || sent >= quota) break;
    var row = vals[r];
    var send = String(row[c['Send?']]).trim().toUpperCase();
    if (send !== 'YES' && send !== 'TRUE') continue;

    var step = parseInt(row[c['Step Sent']], 10) || 0;
    if (step >= STEPS.length) { done++; continue; }         // finished all 5

    var nextAt = row[c['Next Send']];
    var due = (nextAt === '' || nextAt === null) ||
              (nextAt instanceof Date && nextAt.getTime() <= now.getTime());
    if (!due) continue;

    var email = String(row[c['Email']]).trim();
    if (!validEmail_(email)) {
      sh.getRange(r + 1, c['Email Status'] + 1).setValue('Skipped');
      sh.getRange(r + 1, c['Error'] + 1).setValue('Invalid email');
      skipped++; continue;
    }

    var n = step + 1;
    var name = String(row[c['Contact Name']] || '').trim() || 'there';
    try {
      sendStep_(email, name, n, banner);
      sh.getRange(r + 1, c['Step Sent'] + 1).setValue(n);
      if (n < STEPS.length) {
        var next = new Date(now.getTime() + CFG.DAYS_BETWEEN * 86400000);
        sh.getRange(r + 1, c['Next Send'] + 1).setValue(next);
      } else {
        sh.getRange(r + 1, c['Next Send'] + 1).setValue('');   // series complete
      }
      sh.getRange(r + 1, c['Email Status'] + 1).setValue('Step ' + n + ' sent');
      sh.getRange(r + 1, c['Sent At'] + 1).setValue(now);
      sh.getRange(r + 1, c['Error'] + 1).setValue('');
      sent++;
      Utilities.sleep(CFG.PAUSE_MS);
    } catch (err) {
      sh.getRange(r + 1, c['Email Status'] + 1).setValue('Failed step ' + n);
      sh.getRange(r + 1, c['Error'] + 1).setValue(String(err));
      failed++;
    }
  }
  SpreadsheetApp.getActive().toast(
    'Sent ' + sent + ' | skipped ' + skipped + ' | failed ' + failed +
    ' | already finished ' + done, 'TOPSCHOOL', 8);
}

function setupAutomation() {
  removeAutomation();
  ScriptApp.newTrigger('runCampaign').timeBased()
    .everyDays(1).atHour(CFG.AUTOMATION_HOUR).create();
  SpreadsheetApp.getActive().toast(
    'Automation ON. It runs daily around ' + CFG.AUTOMATION_HOUR +
    ':00 and emails each lead the next step when their ' + CFG.DAYS_BETWEEN +
    ' days are up.', 'TOPSCHOOL', 8);
}

function removeAutomation() {
  var trigs = ScriptApp.getProjectTriggers();
  for (var i = 0; i < trigs.length; i++) {
    if (trigs[i].getHandlerFunction() === 'runCampaign') ScriptApp.deleteTrigger(trigs[i]);
  }
  SpreadsheetApp.getActive().toast('Automation OFF.');
}

function resetSelected() {
  var sh = SpreadsheetApp.getActiveSheet();
  var c = cols_(sh);
  var sel = sh.getActiveRange();
  for (var i = 0; i < sel.getNumRows(); i++) {
    var r = sel.getRow() + i;
    if (r === 1) continue;
    sh.getRange(r, c['Email Status'] + 1).setValue('');
    sh.getRange(r, c['Sent At'] + 1).setValue('');
    sh.getRange(r, c['Error'] + 1).setValue('');
    sh.getRange(r, c['Step Sent'] + 1).setValue('');
    sh.getRange(r, c['Next Send'] + 1).setValue('');
    sh.getRange(r, c['Reintro Sent'] + 1).setValue('');
  }
  SpreadsheetApp.getActive().toast('Selected rows reset to step 0.');
}
