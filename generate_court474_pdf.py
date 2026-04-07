"""
Generate Court 474 Ltd — Solution Brief PDF
Client: Court 474 Ltd (Danjuma)
Format: Matches Algolog standard (banner header, Lexend font, professional layout)
"""

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib.colors import HexColor
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Image, Table, TableStyle,
    PageBreak, HRFlowable
)
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import os

# --- Paths ---
BASE = "C:/Users/Femi Fayinminu/OneDrive/Documents/Algolog/Algolog_Projects"
FONT_DIR = os.path.join(BASE, "fonts/lexend-main/fonts/lexend/ttf")
BANNER_PATH = os.path.join(BASE, "claude.ai contex/Algolog_banner_cropped.png")
OUTPUT_PATH = os.path.join(BASE, "Proposals/Court474-Solution-Brief.pdf")

# --- Register Lexend Fonts ---
pdfmetrics.registerFont(TTFont("Lexend", os.path.join(FONT_DIR, "Lexend-Regular.ttf")))
pdfmetrics.registerFont(TTFont("Lexend-Bold", os.path.join(FONT_DIR, "Lexend-Bold.ttf")))
pdfmetrics.registerFont(TTFont("Lexend-SemiBold", os.path.join(FONT_DIR, "Lexend-SemiBold.ttf")))
pdfmetrics.registerFont(TTFont("Lexend-Light", os.path.join(FONT_DIR, "Lexend-Light.ttf")))
pdfmetrics.registerFont(TTFont("Lexend-Medium", os.path.join(FONT_DIR, "Lexend-Medium.ttf")))
pdfmetrics.registerFontFamily("Lexend", normal="Lexend", bold="Lexend-Bold", italic="Lexend", boldItalic="Lexend-Bold")

# --- Colors ---
ACCENT_BLUE = HexColor("#0f3460")
DARK_TEXT = HexColor("#1a1a1a")
MEDIUM_TEXT = HexColor("#333333")
LIGHT_TEXT = HexColor("#555555")
TABLE_HEADER_BG = HexColor("#1a1a2e")
TABLE_ALT_ROW = HexColor("#f5f6fa")
BORDER_COLOR = HexColor("#dcdde1")
GREEN = HexColor("#27ae60")
WHITE = HexColor("#ffffff")

# --- Page Setup ---
PAGE_W, PAGE_H = A4
LM = 22 * mm
RM = 22 * mm
TM = 20 * mm
BM = 20 * mm

# --- Styles ---
def s(name, **kw):
    defaults = {"fontName": "Lexend", "fontSize": 10, "leading": 14, "textColor": DARK_TEXT, "alignment": TA_LEFT, "spaceAfter": 6}
    defaults.update(kw)
    return ParagraphStyle(name, **defaults)

H1 = s("H1", fontName="Lexend-Bold", fontSize=15, leading=20, textColor=ACCENT_BLUE, spaceBefore=18, spaceAfter=8)
H2 = s("H2", fontName="Lexend-SemiBold", fontSize=12, leading=16, textColor=DARK_TEXT, spaceBefore=12, spaceAfter=6)
H3 = s("H3", fontName="Lexend-SemiBold", fontSize=11, leading=14, textColor=MEDIUM_TEXT, spaceBefore=8, spaceAfter=4)
BODY = s("BODY", fontSize=9.5, leading=14, textColor=MEDIUM_TEXT, alignment=TA_JUSTIFY, spaceAfter=6)
BODY_B = s("BODY_B", fontName="Lexend-Bold", fontSize=9.5, leading=14, textColor=DARK_TEXT, spaceAfter=6)
BUL = s("BUL", fontSize=9.5, leading=14, textColor=MEDIUM_TEXT, leftIndent=18, bulletIndent=6, spaceAfter=4)
NUM = s("NUM", fontSize=9.5, leading=14, textColor=MEDIUM_TEXT, leftIndent=18, bulletIndent=6, spaceAfter=4)
SM = s("SM", fontSize=8, leading=11, textColor=LIGHT_TEXT, alignment=TA_CENTER)
HDR = s("HDR", fontName="Lexend-Light", fontSize=8.5, leading=12, textColor=LIGHT_TEXT, alignment=TA_CENTER)
TH = s("TH", fontName="Lexend-Bold", fontSize=9, leading=12, textColor=WHITE)
TC = s("TC", fontSize=9, leading=12, textColor=MEDIUM_TEXT)
TCB = s("TCB", fontName="Lexend-Bold", fontSize=9, leading=12, textColor=DARK_TEXT)
CALLOUT = s("CALLOUT", fontName="Lexend-SemiBold", fontSize=10, leading=14, textColor=GREEN, spaceAfter=8, spaceBefore=8)


def footer(c, doc):
    c.saveState()
    c.setFont("Lexend-Light", 7)
    c.setFillColor(LIGHT_TEXT)
    c.drawCentredString(PAGE_W / 2, 12 * mm, f"Algolog Limited  |  Confidential  |  Prepared for Court 474 Ltd  |  Page {doc.page}")
    c.restoreState()


def hr():
    return HRFlowable(width="100%", thickness=0.5, color=BORDER_COLOR, spaceAfter=8, spaceBefore=8)


def build():
    doc = SimpleDocTemplate(OUTPUT_PATH, pagesize=A4, leftMargin=LM, rightMargin=RM, topMargin=TM, bottomMargin=BM)
    story = []
    aw = PAGE_W - LM - RM

    # ========== COVER ==========
    if os.path.exists(BANNER_PATH):
        from PIL import Image as PILImage
        img = PILImage.open(BANNER_PATH)
        iw, ih = img.size
        dw = aw
        dh = dw * (ih / iw)
        story.append(Image(BANNER_PATH, width=dw, height=dh))

    story.append(Spacer(1, 18 * mm))
    story.append(hr())
    story.append(Spacer(1, 8 * mm))

    story.append(Paragraph("Court474", s("ct", fontName="Lexend-Bold", fontSize=28, leading=34, textColor=ACCENT_BLUE, alignment=TA_CENTER, spaceAfter=4)))
    story.append(Paragraph("AI-Powered Short-Let Property Management<br/>&amp; Guest Distribution System", s("cs1", fontName="Lexend-SemiBold", fontSize=14, leading=20, textColor=DARK_TEXT, alignment=TA_CENTER, spaceAfter=4)))
    story.append(Paragraph("Solution Brief for Court 474 Ltd", s("cs2", fontName="Lexend-Medium", fontSize=12, leading=16, textColor=LIGHT_TEXT, alignment=TA_CENTER, spaceAfter=6)))

    story.append(Spacer(1, 12 * mm))
    story.append(hr())
    story.append(Spacer(1, 6 * mm))

    info = [
        [Paragraph("<b>Prepared for:</b>", TCB), Paragraph("<b>Prepared by:</b>", TCB)],
        [Paragraph("Court 474 Ltd", TC), Paragraph("Algolog Limited", TC)],
        [Paragraph("Danjuma", TC), Paragraph("Plot 1387 Aminu Kano Crescent,<br/>Wuse, Abuja", TC)],
        [Paragraph("", TC), Paragraph("ffayinminu@algolog.co<br/>+234 705 301 6348", TC)],
        [Paragraph("", TC), Paragraph("Fayinminu Femi<br/>Senior Business Developer", TC)],
    ]
    t = Table(info, colWidths=[aw * 0.5, aw * 0.5])
    t.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "TOP"), ("TOPPADDING", (0, 0), (-1, -1), 4), ("BOTTOMPADDING", (0, 0), (-1, -1), 4), ("LEFTPADDING", (0, 0), (-1, -1), 8), ("LINEBELOW", (0, 0), (-1, 0), 0.5, BORDER_COLOR)]))
    story.append(t)

    story.append(Spacer(1, 12 * mm))
    story.append(Paragraph("April 2026", s("dt", fontName="Lexend-Medium", fontSize=11, textColor=LIGHT_TEXT, alignment=TA_CENTER)))
    story.append(PageBreak())

    # ========== 1. THE BUSINESS ==========
    story.append(Paragraph("1. THE BUSINESS", H1))
    story.append(hr())

    story.append(Paragraph("Court 474 Ltd operates a short-let (Airbnb-style) property consisting of:", BODY))
    story.append(Paragraph("\u2022  <b>25 x 1-bedroom apartments</b> \u2014 owned by different subscribers/property owners", BUL))
    story.append(Paragraph("\u2022  <b>4 x 2-bedroom apartments</b> \u2014 owned by different subscribers/property owners", BUL))
    story.append(Paragraph("\u2022  <b>1 x 40-seater conference room</b> \u2014 meetings, seminars, retreats, trainings", BUL))

    story.append(Spacer(1, 3 * mm))
    story.append(Paragraph("Court 474 manages the facility on behalf of the individual apartment owners across two layers:", BODY))

    story.append(Paragraph("Layer 1 \u2014 General Facility Management (all units)", H3))
    story.append(Paragraph("\u2022  Security, water supply, cleaning of external premises and common areas", BUL))
    story.append(Paragraph("\u2022  Charged at a pre-agreed fixed service charge to all apartment owners", BUL))

    story.append(Paragraph("Layer 2 \u2014 Individual Apartment Management (opt-in)", H3))
    story.append(Paragraph("\u2022  Short-letting, guest management, cleaning of individual apartments", BUL))
    story.append(Paragraph("\u2022  Charged at an agreed fee per apartment", BUL))
    story.append(Paragraph("\u2022  This is the revenue-generating layer where technology has the most impact", BUL))

    story.append(PageBreak())

    # ========== 2. THE PROBLEMS ==========
    story.append(Paragraph("2. THE PROBLEMS TO SOLVE", H1))
    story.append(hr())

    story.append(Paragraph("A. Fair Guest Distribution", H2))
    story.append(Paragraph("With 29 apartments owned by different people, how do you ensure bookings are distributed evenly? Without a system:", BODY))
    story.append(Paragraph("\u2022  Some apartments get overbooked while others sit empty", BUL))
    story.append(Paragraph("\u2022  Owners complain about unequal treatment", BUL))
    story.append(Paragraph("\u2022  Manual allocation is time-consuming and biased (consciously or not)", BUL))
    story.append(Paragraph("\u2022  No transparency for owners to verify fair distribution", BUL))

    story.append(Paragraph("B. Revenue Splitting", H2))
    story.append(Paragraph("Each booking generates revenue that needs to be split between the apartment owner (their share) and Court 474 (management fee). This needs to happen automatically, transparently, and with a full audit trail.", BODY))

    story.append(Paragraph("C. Operations Cost", H2))
    story.append(Paragraph("Running 29 apartments + a conference room with traditional staffing is expensive:", BODY))
    story.append(Paragraph("\u2022  Receptionist/front desk for check-in/out", BUL))
    story.append(Paragraph("\u2022  Manual booking tracking (WhatsApp, spreadsheets, calls)", BUL))
    story.append(Paragraph("\u2022  Manual cleaning scheduling and procurement tracking", BUL))
    story.append(Paragraph("\u2022  Manual invoicing and payment reconciliation", BUL))

    story.append(Paragraph("D. Conference Room Management", H2))
    story.append(Paragraph("The 40-seater conference room is a separate revenue stream that needs its own booking system (hourly/daily), availability calendar, payment processing, and conflict prevention.", BODY))

    story.append(PageBreak())

    # ========== 3. THE SOLUTION ==========
    story.append(Paragraph("3. THE SOLUTION", H1))
    story.append(hr())

    story.append(Paragraph("A purpose-built platform for Court 474\u2019s multi-owner short-let model. It manages the entire operation: bookings, AI guest distribution, owner settlements, conference room, and facility operations \u2014 all from one system.", BODY_B))

    # --- Module 1 ---
    story.append(Spacer(1, 4 * mm))
    story.append(Paragraph("Module 1: AI Guest Queuing &amp; Distribution Engine", H2))

    story.append(Paragraph("The system maintains a <b>fairness score</b> for each apartment. When a new booking request comes in, the AI engine allocates it based on:", BODY))
    story.append(Paragraph("1. <b>Occupancy balance</b> \u2014 Which apartments have had the fewest bookings this period? Those get priority.", NUM))
    story.append(Paragraph("2. <b>Revenue balance</b> \u2014 Which owners have earned the least? The system balances revenue, not just bookings (since 2-beds earn more than 1-beds).", NUM))
    story.append(Paragraph("3. <b>Apartment type match</b> \u2014 Guest requests a 1-bed \u2192 only 1-bed apartments are considered. 2-bed \u2192 only 2-beds.", NUM))
    story.append(Paragraph("4. <b>Availability</b> \u2014 Only apartments that are actually available for the requested dates.", NUM))
    story.append(Paragraph("5. <b>Cleaning status</b> \u2014 Only apartments that are cleaned and ready.", NUM))
    story.append(Paragraph("6. <b>Owner preferences</b> \u2014 Some owners may block certain dates (personal use, maintenance).", NUM))

    story.append(Spacer(1, 2 * mm))
    story.append(Paragraph("Every owner gets a fair share of bookings. The system can show each owner exactly how many bookings they\u2019ve received vs. the average, and why a particular apartment was chosen for a particular guest.", BODY))

    story.append(Paragraph("Distribution modes:", H3))
    story.append(Paragraph("\u2022  <b>Round-robin</b> \u2014 Strict rotation (Apartment 1, then 2, then 3...)", BUL))
    story.append(Paragraph("\u2022  <b>Weighted fair share</b> \u2014 Balances by revenue earned, not just count", BUL))
    story.append(Paragraph("\u2022  <b>Priority override</b> \u2014 Admin can manually assign a specific apartment when needed (with audit log)", BUL))

    # --- Module 2 ---
    story.append(Spacer(1, 4 * mm))
    story.append(Paragraph("Module 2: Owner Dashboard &amp; Revenue Distribution", H2))

    story.append(Paragraph("Each property owner gets a portal showing:", BODY))
    story.append(Paragraph("\u2022  <b>Live occupancy status</b> of their apartment(s)", BUL))
    story.append(Paragraph("\u2022  <b>Booking history</b> \u2014 who stayed, when, how long, how much", BUL))
    story.append(Paragraph("\u2022  <b>Revenue earned</b> \u2014 gross booking amount, management fee deducted, net owner earnings", BUL))
    story.append(Paragraph("\u2022  <b>Automatic settlement reports</b> \u2014 weekly/monthly statements", BUL))
    story.append(Paragraph("\u2022  <b>Fairness transparency</b> \u2014 their booking count vs. property average, revenue vs. average", BUL))
    story.append(Paragraph("\u2022  <b>Calendar blocking</b> \u2014 owners can block dates for personal use", BUL))
    story.append(Paragraph("\u2022  <b>Maintenance requests</b> \u2014 flag issues in their apartment", BUL))

    story.append(Spacer(1, 2 * mm))
    story.append(Paragraph("Revenue split flow:", H3))
    story.append(Paragraph("1. Guest pays for booking \u2192 money lands in Court 474 account", NUM))
    story.append(Paragraph("2. System calculates: Gross amount \u2192 Management fee (%) \u2192 Owner net", NUM))
    story.append(Paragraph("3. Settlement report generated automatically", NUM))
    story.append(Paragraph("4. Court 474 disburses to owner on agreed schedule (weekly/monthly)", NUM))
    story.append(Paragraph("5. Full audit trail \u2014 every naira accounted for", NUM))

    story.append(PageBreak())

    # --- Module 3 ---
    story.append(Paragraph("Module 3: Guest Booking &amp; Management", H2))

    story.append(Paragraph("For guests:", H3))
    story.append(Paragraph("\u2022  Online booking portal \u2014 browse available apartments, see photos, select dates, pay online", BUL))
    story.append(Paragraph("\u2022  Instant booking confirmation via email/SMS", BUL))
    story.append(Paragraph("\u2022  Smart lock access code \u2014 generated automatically, sent to guest, expires at checkout", BUL))
    story.append(Paragraph("\u2022  QR check-in \u2014 scan on arrival, validated against active booking", BUL))
    story.append(Paragraph("\u2022  No front desk needed for standard check-ins", BUL))

    story.append(Paragraph("For Court 474 staff:", H3))
    story.append(Paragraph("\u2022  Dashboard showing all active bookings, upcoming arrivals, departures", BUL))
    story.append(Paragraph("\u2022  Guest communication tools and issue/complaint tracking", BUL))
    story.append(Paragraph("\u2022  Automated reminders (checkout time, extension offers)", BUL))

    # --- Module 4 ---
    story.append(Spacer(1, 4 * mm))
    story.append(Paragraph("Module 4: Conference Room Booking System", H2))

    story.append(Paragraph("\u2022  Separate booking flow for the 40-seater conference room", BUL))
    story.append(Paragraph("\u2022  Hourly and daily booking options", BUL))
    story.append(Paragraph("\u2022  Online calendar showing availability in real time", BUL))
    story.append(Paragraph("\u2022  Payment processing", BUL))
    story.append(Paragraph("\u2022  Add-ons: projector, catering, breakout rooms (if available)", BUL))
    story.append(Paragraph("\u2022  Automated confirmation and access instructions", BUL))
    story.append(Paragraph("\u2022  Can be marketed separately from the apartments", BUL))

    # --- Module 5 ---
    story.append(Spacer(1, 4 * mm))
    story.append(Paragraph("Module 5: AI Operations Manager", H2))

    story.append(Paragraph("Cleaning automation:", H3))
    story.append(Paragraph("\u2022  Guest checks out \u2192 system automatically flags apartment for cleaning", BUL))
    story.append(Paragraph("\u2022  Assigns cleaning staff based on availability", BUL))
    story.append(Paragraph("\u2022  Staff marks apartment as \u201cready\u201d \u2192 apartment becomes bookable again", BUL))
    story.append(Paragraph("\u2022  Track cleaning time, frequency, and cost per apartment", BUL))

    story.append(Paragraph("Procurement:", H3))
    story.append(Paragraph("\u2022  Track consumables per apartment (toiletries, linens, cleaning supplies)", BUL))
    story.append(Paragraph("\u2022  Auto-generate restock alerts when inventory drops below threshold", BUL))
    story.append(Paragraph("\u2022  Monthly procurement reports \u2014 cost per apartment, cost trends", BUL))

    story.append(Paragraph("Staff optimization:", H3))
    story.append(Paragraph("\u2022  AI suggests optimal staffing levels based on occupancy patterns", BUL))
    story.append(Paragraph("\u2022  Low occupancy week? Reduce cleaning staff schedule. High occupancy weekend? Alert for additional support.", BUL))
    story.append(Paragraph("\u2022  Track staff performance (cleaning time, guest ratings)", BUL))

    story.append(Paragraph("Cost analytics:", H3))
    story.append(Paragraph("\u2022  Utility costs per apartment (electricity, water \u2014 if metered)", BUL))
    story.append(Paragraph("\u2022  Revenue vs. cost per apartment \u2014 which units are most/least profitable", BUL))
    story.append(Paragraph("\u2022  Monthly P&amp;L per apartment and for the facility overall", BUL))

    story.append(PageBreak())

    # --- Module 6 ---
    story.append(Paragraph("Module 6: Facility Management Dashboard", H2))

    story.append(Paragraph("For Court 474 management:", H3))
    story.append(Paragraph("\u2022  Bird\u2019s eye view of the entire property \u2014 29 apartments + conference room", BUL))
    story.append(Paragraph("\u2022  Real-time occupancy map (visual grid: occupied, available, cleaning, blocked)", BUL))
    story.append(Paragraph("\u2022  Financial overview \u2014 total revenue, management fees earned, pending settlements", BUL))
    story.append(Paragraph("\u2022  Maintenance tracker \u2014 open issues, resolved issues, cost", BUL))
    story.append(Paragraph("\u2022  Service charge tracking \u2014 which owners have paid, who\u2019s overdue", BUL))

    story.append(PageBreak())

    # ========== 4. TECHNICAL APPROACH ==========
    story.append(Paragraph("4. TECHNICAL APPROACH", H1))
    story.append(hr())

    tech = [
        [Paragraph("<b>Component</b>", TH), Paragraph("<b>Technology</b>", TH)],
        [Paragraph("Frontend", TC), Paragraph("Next.js + React", TC)],
        [Paragraph("Backend", TC), Paragraph("Node.js (NestJS)", TC)],
        [Paragraph("Database", TC), Paragraph("PostgreSQL", TC)],
        [Paragraph("AI Engine", TC), Paragraph("Custom allocation algorithm (fairness scoring, occupancy balancing)", TC)],
        [Paragraph("Payments", TC), Paragraph("Paystack (guest payments, owner settlements)", TC)],
        [Paragraph("Smart Access", TC), Paragraph("IoT smart locks (auto-generated codes, auto-expiry)", TC)],
        [Paragraph("Cloud", TC), Paragraph("Microsoft Azure", TC)],
        [Paragraph("Infrastructure", TC), Paragraph("Terraform", TC)],
        [Paragraph("Notifications", TC), Paragraph("Email + SMS (bookings, owner reports, staff alerts)", TC)],
        [Paragraph("Security", TC), Paragraph("OWASP standard, role-based access control", TC)],
    ]
    tt = Table(tech, colWidths=[aw * 0.3, aw * 0.7])
    tt.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), TABLE_HEADER_BG),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("TOPPADDING", (0, 0), (-1, -1), 6), ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
        ("LEFTPADDING", (0, 0), (-1, -1), 8), ("RIGHTPADDING", (0, 0), (-1, -1), 8),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [WHITE, TABLE_ALT_ROW]),
        ("LINEBELOW", (0, 0), (-1, -2), 0.25, BORDER_COLOR),
        ("BOX", (0, 0), (-1, -1), 0.5, BORDER_COLOR),
    ]))
    story.append(tt)

    story.append(Spacer(1, 4 * mm))
    story.append(Paragraph(
        "Algolog has built and deployed property management systems for hospitality businesses across "
        "Nigeria \u2014 handling bookings, payments, smart lock automation, and operational dashboards. "
        "Court474 is a custom build designed specifically for the multi-owner short-let model, with "
        "AI-powered guest distribution as its core differentiator.", BODY))

    story.append(Spacer(1, 8 * mm))

    # ========== 5. WHAT COURT 474 GETS ==========
    story.append(Paragraph("5. WHAT COURT 474 GETS", H1))
    story.append(hr())

    comp = [
        [Paragraph("<b>Without the system</b>", TH), Paragraph("<b>With the system</b>", TH)],
        [Paragraph("Manual guest allocation (WhatsApp, calls, gut feel)", TC),
         Paragraph("AI distributes guests fairly across all apartments automatically", TC)],
        [Paragraph("Owners don\u2019t know if they\u2019re getting fair share", TC),
         Paragraph("Every owner sees their stats vs. average in real time", TC)],
        [Paragraph("Revenue splitting done manually in Excel", TC),
         Paragraph("Automatic calculation, settlement reports, audit trail", TC)],
        [Paragraph("Front desk needed for every check-in", TC),
         Paragraph("Smart lock codes sent to guests automatically", TC)],
        [Paragraph("Cleaning scheduled via phone calls", TC),
         Paragraph("Auto-triggered cleaning workflow on checkout", TC)],
        [Paragraph("No visibility into costs per apartment", TC),
         Paragraph("Full P&L per apartment, per month", TC)],
        [Paragraph("Conference room booked via calls/WhatsApp", TC),
         Paragraph("Online booking with real-time availability and payment", TC)],
        [Paragraph("Procurement tracked manually or not at all", TC),
         Paragraph("Auto restock alerts, usage tracking, cost reports", TC)],
        [Paragraph("High staff costs", TC),
         Paragraph("AI suggests optimal staffing based on occupancy", TC)],
    ]
    ct = Table(comp, colWidths=[aw * 0.5, aw * 0.5])
    ct.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), TABLE_HEADER_BG),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("TOPPADDING", (0, 0), (-1, -1), 6), ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
        ("LEFTPADDING", (0, 0), (-1, -1), 8), ("RIGHTPADDING", (0, 0), (-1, -1), 8),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [WHITE, TABLE_ALT_ROW]),
        ("LINEBELOW", (0, 0), (-1, -2), 0.25, BORDER_COLOR),
        ("BOX", (0, 0), (-1, -1), 0.5, BORDER_COLOR),
    ]))
    story.append(ct)

    story.append(PageBreak())

    # ========== 6. SUMMARY ==========
    story.append(Paragraph("6. SUMMARY", H1))
    story.append(hr())

    story.append(Paragraph(
        "Court 474\u2019s multi-owner model creates a unique challenge: <b>fairness</b>. Every owner needs to trust "
        "that their apartment is getting its fair share of bookings and revenue. At the same time, Court 474 "
        "needs to run operations as lean as possible.", BODY))

    story.append(Spacer(1, 3 * mm))
    story.append(Paragraph(
        "This solution uses AI to solve both problems simultaneously \u2014 fair distribution builds owner trust "
        "and retention, while automation reduces the staff and manual effort needed to manage 29 apartments "
        "and a conference room.", BODY))

    story.append(Spacer(1, 3 * mm))
    story.append(Paragraph(
        "The platform is purpose-built for Court 474\u2019s multi-owner model, developed by Algolog \u2014 a team "
        "with proven experience building and deploying property management systems in the Nigerian market.", BODY))

    story.append(Spacer(1, 10 * mm))

    # ========== WHY ALGOLOG ==========
    story.append(Paragraph("WHY ALGOLOG", H1))
    story.append(hr())

    story.append(Paragraph(
        "Algolog Limited is a Nigerian technology company committed to ensuring businesses across Africa get "
        "the technology they need to build their future, improve their sales, and strengthen their operations.", BODY))

    story.append(Spacer(1, 3 * mm))
    story.append(Paragraph("\u2022  <b>Spacer</b> (spacer.so) \u2014 Smart hospitality and workspace management platform", BUL))
    story.append(Paragraph("\u2022  <b>DeepThread</b> (deepthread.ai) \u2014 AI-powered cross-platform context engine", BUL))
    story.append(Paragraph("\u2022  <b>Visora</b> (visora-ai.com) \u2014 AI-powered data analytics and insights", BUL))
    story.append(Paragraph("\u2022  <b>PrivateTransfer</b> (privatetransfer.ng) \u2014 Secure transfer platform", BUL))

    story.append(Spacer(1, 6 * mm))

    # ========== NEXT STEP ==========
    story.append(Paragraph("NEXT STEP", H1))
    story.append(hr())

    story.append(Paragraph(
        "We\u2019d love to have a conversation about how Court474 can work for your specific operation \u2014 "
        "the apartment mix, the owner agreements, the conference room, and how AI distribution would "
        "integrate into your day-to-day workflow.", BODY))

    story.append(Spacer(1, 3 * mm))
    story.append(Paragraph("Whenever you\u2019re ready, reach out to:", H3))
    story.append(Paragraph("\u2022  <b>Call/WhatsApp:</b> Fayinminu Femi \u2014 +234 705 301 6348", BUL))
    story.append(Paragraph("\u2022  <b>Email:</b> ffayinminu@algolog.co", BUL))

    story.append(Spacer(1, 10 * mm))
    story.append(hr())
    story.append(Paragraph("Algolog Limited", s("fc", fontName="Lexend-Bold", fontSize=10, textColor=DARK_TEXT, alignment=TA_CENTER)))
    story.append(Paragraph("Plot 1387 Aminu Kano Crescent, Wuse, Abuja  |  algolog.co", HDR))
    story.append(Spacer(1, 3 * mm))
    story.append(Paragraph("Prepared with care for Court 474 Ltd \u2014 April 2026", SM))

    doc.build(story, onFirstPage=footer, onLaterPages=footer)
    print(f"PDF generated: {OUTPUT_PATH}")
    print(f"File size: {os.path.getsize(OUTPUT_PATH):,} bytes")


if __name__ == "__main__":
    build()
