"""
Generate Court 474 Ltd — Implementation Document PDF
AI-Powered Short-Let Management with Fair Distribution Algorithm
Built on Spacer
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
OUTPUT_PATH = os.path.join(BASE, "Proposals/Implementation-Court474.pdf")

# --- Register Fonts ---
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

PAGE_W, PAGE_H = A4
LM = 22 * mm
RM = 22 * mm
TM = 20 * mm
BM = 20 * mm

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

    story.append(Paragraph("Spacer",
        s("ct", fontName="Lexend-Bold", fontSize=28, leading=34, textColor=ACCENT_BLUE, alignment=TA_CENTER, spaceAfter=4)))
    story.append(Paragraph("Implementation Document",
        s("ct2", fontName="Lexend-SemiBold", fontSize=18, leading=24, textColor=DARK_TEXT, alignment=TA_CENTER, spaceAfter=4)))
    story.append(Paragraph("Smart Short-Let Management &amp; Fair Distribution System",
        s("cs2a", fontName="Lexend-Medium", fontSize=11, leading=16, textColor=LIGHT_TEXT, alignment=TA_CENTER, spaceAfter=2)))
    story.append(Paragraph("Prepared for Court 474 Ltd",
        s("cs2", fontName="Lexend-Medium", fontSize=12, leading=16, textColor=LIGHT_TEXT, alignment=TA_CENTER, spaceAfter=6)))

    story.append(Spacer(1, 12 * mm))
    story.append(hr())
    story.append(Spacer(1, 6 * mm))

    info = [
        [Paragraph("<b>Prepared for:</b>", TCB), Paragraph("<b>Prepared by:</b>", TCB)],
        [Paragraph("Court 474 Ltd", TC), Paragraph("Algolog Limited", TC)],
        [Paragraph("", TC), Paragraph("Plot 1387 Aminu Kano Crescent,<br/>Wuse, Abuja", TC)],
        [Paragraph("", TC), Paragraph("ffayinminu@algolog.co<br/>+234 705 301 6348", TC)],
        [Paragraph("", TC), Paragraph("Fayinminu Femi<br/>Senior Business Developer", TC)],
    ]
    t = Table(info, colWidths=[aw * 0.5, aw * 0.5])
    t.setStyle(TableStyle([("VALIGN", (0,0), (-1,-1), "TOP"), ("TOPPADDING", (0,0), (-1,-1), 4),
        ("BOTTOMPADDING", (0,0), (-1,-1), 4), ("LEFTPADDING", (0,0), (-1,-1), 8),
        ("LINEBELOW", (0,0), (-1,0), 0.5, BORDER_COLOR)]))
    story.append(t)

    story.append(Spacer(1, 12 * mm))
    story.append(Paragraph("April 2026", s("dt", fontName="Lexend-Medium", fontSize=11, textColor=LIGHT_TEXT, alignment=TA_CENTER)))
    story.append(PageBreak())

    # ========== 1. PROJECT OVERVIEW ==========
    story.append(Paragraph("1. PROJECT OVERVIEW", H1))
    story.append(hr())

    story.append(Paragraph(
        "Court 474 Ltd is developing a short-let apartment complex consisting of <b>25 one-bedroom apartments</b> "
        "and <b>4 two-bedroom apartments</b>, along with a <b>40-seater conference room</b>. These apartments will "
        "be constructed and sold to multiple individual owners (subscribers). Court 474 will then manage the "
        "short-let bookings, guest access, and revenue distribution on behalf of these owners.", BODY))

    story.append(Paragraph(
        "The central challenge is <b>fairness</b>. With 29 apartments owned by different people, the system must "
        "ensure that bookings and revenue are distributed equitably across all units. No owner should feel that "
        "their apartment is being overlooked while others receive preferential treatment.", BODY))

    story.append(Paragraph(
        "This document outlines how <b>Spacer</b> \u2014 Algolog\u2019s property management platform already live "
        "and processing bookings across multiple properties in Nigeria \u2014 will be deployed for Court 474, "
        "with its <b>Fair Distribution Algorithm</b> configured specifically for the multi-owner model.", BODY))

    story.append(Spacer(1, 4 * mm))
    story.append(Paragraph("What Spacer delivers for Court 474:", H3))
    story.append(Paragraph("\u2022  A branded booking link where guests browse, select dates, and pay online", BUL))
    story.append(Paragraph("\u2022  A fair distribution algorithm that automatically assigns apartments to bookings", BUL))
    story.append(Paragraph("\u2022  TTLock smart lock integration \u2014 access codes tied to the guest\u2019s period of stay", BUL))
    story.append(Paragraph("\u2022  Revenue splitting \u2014 agency charge to Court 474, remainder to the apartment owner", BUL))
    story.append(Paragraph("\u2022  Owner dashboard with full transparency into bookings, earnings, and fairness metrics", BUL))
    story.append(Paragraph("\u2022  Cart abandonment recovery \u2014 automatic reminders until the booking is completed", BUL))
    story.append(Paragraph("\u2022  Temporary space removal \u2014 owners can block their apartment from bookings", BUL))
    story.append(Paragraph("\u2022  Conference room booking as a separate revenue stream", BUL))
    story.append(Paragraph("\u2022  Smart home synchronisation advisory \u2014 TTLocks, smart lighting, and automated shutoff", BUL))

    story.append(PageBreak())

    # ========== 2. THE PROBLEMS WE ARE SOLVING ==========
    story.append(Paragraph("2. THE PROBLEMS WE ARE SOLVING", H1))
    story.append(hr())

    story.append(Paragraph("A. Fair Guest Distribution Across Multiple Owners", H2))
    story.append(Paragraph(
        "With 29 apartments owned by different subscribers, manual allocation of guests is inherently unfair. "
        "Without a system, some apartments will receive more bookings than others \u2014 whether by coincidence, "
        "convenience, or unconscious bias. Owners will inevitably question whether they are getting their fair "
        "share, and this erodes trust in Court 474\u2019s management.", BODY))
    story.append(Paragraph(
        "The solution requires an algorithm that distributes bookings across all apartments in a way that is "
        "transparent, auditable, and mathematically fair \u2014 while still being practical (considering availability, "
        "apartment type, and owner preferences).", BODY))

    story.append(Paragraph("B. Revenue Splitting and Transparency", H2))
    story.append(Paragraph(
        "Every booking generates revenue that must be split between Court 474 (agency/management fee) and "
        "the apartment owner. This needs to happen automatically with a clear audit trail. Owners need to see "
        "exactly how much their apartment earned, what fee was deducted, and what their net payout is \u2014 "
        "without having to ask or chase.", BODY))

    story.append(Paragraph("C. Incomplete Bookings", H2))
    story.append(Paragraph(
        "Prospective guests who start a booking but don\u2019t complete payment represent lost revenue. Without "
        "follow-up, these bookings are simply abandoned. The system needs to automatically remind these guests "
        "until they either complete the booking or the hold period expires.", BODY))

    story.append(Paragraph("D. Owner Control Over Their Space", H2))
    story.append(Paragraph(
        "Apartment owners may need to temporarily remove their unit from the booking pool \u2014 for personal "
        "use, maintenance, renovation, or any other reason. The system must allow owners to block specific "
        "dates without affecting other apartments or the overall booking flow.", BODY))

    story.append(Paragraph("E. Smart Access &amp; Key Management", H2))
    story.append(Paragraph(
        "Physical key handovers are impractical at scale with 29 apartments. Guests need self-service "
        "access that activates on arrival and deactivates on checkout \u2014 without a front desk or manual "
        "coordination.", BODY))

    story.append(Paragraph("F. Conference Room as a Separate Revenue Stream", H2))
    story.append(Paragraph(
        "The 40-seater conference room needs its own booking system (hourly and daily), separate from the "
        "apartment bookings, with its own availability calendar and payment processing.", BODY))

    story.append(PageBreak())

    # ========== 3. THE FAIR DISTRIBUTION ALGORITHM ==========
    story.append(Paragraph("3. THE FAIR DISTRIBUTION ALGORITHM", H1))
    story.append(hr())

    story.append(Paragraph(
        "This is the core intelligence of the Spacer deployment for Court 474. The algorithm ensures that every apartment "
        "gets a fair share of bookings and revenue over time, while still making practical allocation decisions "
        "based on real-time conditions.", BODY))

    story.append(Spacer(1, 3 * mm))
    story.append(Paragraph("How It Works", H2))

    story.append(Paragraph(
        "When a guest initiates a booking (e.g., \u201c1-bedroom apartment, April 10\u201315\u201d), the algorithm "
        "evaluates all eligible apartments and selects one based on the following criteria, applied in order:", BODY))

    story.append(Spacer(1, 2 * mm))
    story.append(Paragraph("<b>Step 1: Filter by Type</b>", BODY_B))
    story.append(Paragraph(
        "If the guest requests a 1-bedroom, only the 25 one-bedroom apartments are considered. If they "
        "request a 2-bedroom, only the 4 two-bedroom apartments are considered. This is a hard filter \u2014 "
        "no cross-type allocation.", BODY))

    story.append(Paragraph("<b>Step 2: Filter by Availability</b>", BODY_B))
    story.append(Paragraph(
        "Remove any apartments that are already booked for the requested dates, or that have been "
        "temporarily blocked by the owner. Only apartments that are genuinely available proceed to the "
        "next step.", BODY))

    story.append(Paragraph("<b>Step 3: Filter by Readiness</b>", BODY_B))
    story.append(Paragraph(
        "Remove any apartments that are not in a \u201cready\u201d state \u2014 e.g., under maintenance, "
        "or flagged for any operational reason. Only guest-ready apartments proceed.", BODY))

    story.append(Paragraph("<b>Step 4: Rank by Fairness Score</b>", BODY_B))
    story.append(Paragraph(
        "Each apartment maintains a <b>fairness score</b> that the algorithm updates after every booking. "
        "The score considers two factors:", BODY))

    story.append(Paragraph("\u2022  <b>Booking count</b> \u2014 How many bookings has this apartment received in the current period "
        "(month/quarter)? Apartments with fewer bookings score higher.", BUL))
    story.append(Paragraph("\u2022  <b>Revenue earned</b> \u2014 How much total revenue has this apartment generated? This matters "
        "because a 2-bedroom apartment earning \u20a6200,000 from 2 bookings shouldn\u2019t be treated the same as a "
        "1-bedroom earning \u20a660,000 from 2 bookings. The algorithm balances by revenue, not just count.", BUL))

    story.append(Spacer(1, 2 * mm))
    story.append(Paragraph(
        "The apartment with the <b>lowest fairness score</b> (fewest bookings + lowest revenue in the current "
        "period) gets priority for the next booking.", BODY))

    story.append(Paragraph("<b>Step 5: Randomised Tie-Breaking</b>", BODY_B))
    story.append(Paragraph(
        "If multiple apartments have the same fairness score (common at the start of a new period), the "
        "algorithm selects randomly among them. This prevents any predictable pattern that could feel unfair.", BODY))

    story.append(Spacer(1, 4 * mm))
    story.append(Paragraph("Distribution Modes", H2))

    story.append(Paragraph(
        "Court 474 management can choose between three distribution modes depending on their preference:", BODY))

    modes = [
        [Paragraph("<b>Mode</b>", TH), Paragraph("<b>How It Works</b>", TH), Paragraph("<b>Best For</b>", TH)],
        [Paragraph("Weighted Fair Share", TCB), Paragraph("Balances by both booking count and revenue earned. Default mode.", TC),
         Paragraph("Multi-owner properties where fairness is the top priority", TC)],
        [Paragraph("Round-Robin", TC), Paragraph("Strict rotation: Apt 1 \u2192 Apt 2 \u2192 Apt 3... regardless of revenue", TC),
         Paragraph("When owners want perfectly equal booking counts", TC)],
        [Paragraph("Manual Override", TC), Paragraph("Admin assigns a specific apartment. Logged in audit trail.", TC),
         Paragraph("Special requests, VIP guests, or operational reasons", TC)],
    ]
    mt = Table(modes, colWidths=[aw * 0.22, aw * 0.45, aw * 0.33])
    mt.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,0), TABLE_HEADER_BG),
        ("VALIGN", (0,0), (-1,-1), "TOP"),
        ("TOPPADDING", (0,0), (-1,-1), 6), ("BOTTOMPADDING", (0,0), (-1,-1), 6),
        ("LEFTPADDING", (0,0), (-1,-1), 6), ("RIGHTPADDING", (0,0), (-1,-1), 6),
        ("ROWBACKGROUNDS", (0,1), (-1,-1), [WHITE, TABLE_ALT_ROW]),
        ("BOX", (0,0), (-1,-1), 0.5, BORDER_COLOR),
        ("LINEBELOW", (0,0), (-1,-2), 0.25, BORDER_COLOR),
    ]))
    story.append(mt)

    story.append(Spacer(1, 4 * mm))
    story.append(Paragraph("Fairness Transparency", H2))
    story.append(Paragraph(
        "Every owner can see their fairness metrics from their dashboard:", BODY))
    story.append(Paragraph("\u2022  Total bookings received vs. property average", BUL))
    story.append(Paragraph("\u2022  Total revenue earned vs. property average", BUL))
    story.append(Paragraph("\u2022  Distribution history \u2014 which apartment was selected for each booking and why", BUL))
    story.append(Paragraph("\u2022  Period-over-period fairness trend (are things balancing out over time?)", BUL))

    story.append(Paragraph(
        "This transparency is what builds trust. Owners don\u2019t have to take Court 474\u2019s word for it \u2014 they "
        "can verify fairness themselves at any time.", CALLOUT))

    story.append(PageBreak())

    # ========== 4. BOOKING FLOW ==========
    story.append(Paragraph("4. THE BOOKING FLOW", H1))
    story.append(hr())

    story.append(Paragraph(
        "This is the end-to-end journey from a guest discovering Court 474 to checking out of their apartment.", BODY))

    story.append(Spacer(1, 3 * mm))
    steps = [
        ("Step 1: Guest Visits Booking Link",
         "Court 474 gets a branded booking page (e.g., court474.spacer.so or a custom domain). The guest "
         "browses available apartment types, views photos and descriptions, and selects their preferred dates."),
        ("Step 2: Algorithm Selects Apartment",
         "The guest does not choose a specific apartment \u2014 they choose a type (1-bed or 2-bed) and dates. "
         "The fair distribution algorithm automatically selects the most appropriate apartment based on the "
         "fairness score, availability, and readiness criteria described above."),
        ("Step 3: Payment",
         "The guest pays online via Paystack (card or bank transfer). Payment is confirmed instantly. The "
         "booking is locked and the apartment is marked as occupied for those dates."),
        ("Step 4: TTLock Access Code Generation",
         "A unique TTLock smart lock access code is generated and sent to the guest via email and SMS. "
         "This code is tied to the guest\u2019s period of stay \u2014 it activates on check-in day and automatically "
         "expires at checkout. No physical key handover required."),
        ("Step 5: Guest Stay",
         "The guest arrives, uses their TTLock access code, and stays in the apartment. If they need to "
         "extend, they can do so through the platform (subject to availability). Court 474 staff can monitor "
         "all active stays from the admin dashboard."),
        ("Step 6: Checkout",
         "On the checkout date, the TTLock access code expires automatically. The apartment is marked "
         "as available and re-enters the booking pool for the next guest."),
        ("Step 7: Revenue Settlement",
         "After each booking, the system automatically calculates the revenue split: Court 474\u2019s agency "
         "charge is deducted, and the remaining amount is credited to the apartment owner\u2019s account. "
         "Settlement reports are generated automatically."),
    ]

    for title, desc in steps:
        story.append(Paragraph(title, H3))
        story.append(Paragraph(desc, BODY))
        story.append(Spacer(1, 1 * mm))

    story.append(PageBreak())

    # ========== 5. CART ABANDONMENT RECOVERY ==========
    story.append(Paragraph("5. CART ABANDONMENT RECOVERY", H1))
    story.append(hr())

    story.append(Paragraph(
        "When a prospective guest starts a booking but does not complete payment, the system does not "
        "simply discard the booking. Instead, it enters the <b>cart abandonment recovery flow</b>:", BODY))

    story.append(Spacer(1, 2 * mm))
    story.append(Paragraph("1. <b>Immediate hold</b> \u2014 The selected apartment is temporarily held for a defined period "
        "(e.g., 30 minutes) to give the guest time to complete payment.", NUM))
    story.append(Paragraph("2. <b>First reminder</b> \u2014 If payment is not completed within the hold period, the guest "
        "receives an email and/or SMS reminder with a direct link to complete their booking.", NUM))
    story.append(Paragraph("3. <b>Follow-up reminders</b> \u2014 The system sends follow-up reminders at configured intervals "
        "(e.g., after 2 hours, after 24 hours, after 48 hours) until either the guest completes the booking "
        "or the maximum reminder count is reached.", NUM))
    story.append(Paragraph("4. <b>Release</b> \u2014 If the guest does not complete payment after all reminders, the apartment "
        "hold is released and the unit returns to the available pool for other guests.", NUM))

    story.append(Spacer(1, 3 * mm))
    story.append(Paragraph(
        "This recovery flow is critical because every abandoned booking is potential revenue. In our "
        "experience with other Spacer deployments, cart abandonment recovery can recapture 15\u201325% of "
        "bookings that would otherwise be lost.", BODY))

    story.append(Spacer(1, 6 * mm))

    # ========== 6. TEMPORARY SPACE REMOVAL ==========
    story.append(Paragraph("6. TEMPORARY SPACE REMOVAL", H1))
    story.append(hr())

    story.append(Paragraph(
        "Apartment owners may need to temporarily remove their unit from the booking pool. The platform "
        "provides this through a <b>calendar blocking</b> feature:", BODY))

    story.append(Spacer(1, 2 * mm))
    story.append(Paragraph("\u2022  <b>Owner-initiated blocking</b> \u2014 The owner logs into their dashboard and blocks specific "
        "dates. The apartment is removed from the booking pool for those dates. No bookings can be "
        "assigned to it during the blocked period.", BUL))
    story.append(Paragraph("\u2022  <b>Reason tracking</b> \u2014 The system records the reason for the block (personal use, "
        "maintenance, renovation, etc.) for management visibility.", BUL))
    story.append(Paragraph("\u2022  <b>Advance notice</b> \u2014 Blocking can only be done for future dates. Dates with existing "
        "confirmed bookings cannot be blocked (the owner would need to coordinate with Court 474 "
        "management to relocate an existing booking).", BUL))
    story.append(Paragraph("\u2022  <b>Fairness adjustment</b> \u2014 When an apartment is blocked by the owner, the fairness "
        "algorithm accounts for this. The blocked period is excluded from the fairness calculation so the "
        "owner is not penalised for voluntarily removing their unit.", BUL))
    story.append(Paragraph("\u2022  <b>Auto-return</b> \u2014 Once the blocked period ends, the apartment automatically returns "
        "to the booking pool. No manual action needed.", BUL))

    story.append(PageBreak())

    # ========== 7. REVENUE SPLITTING ==========
    story.append(Paragraph("7. REVENUE SPLITTING &amp; OWNER SETTLEMENTS", H1))
    story.append(hr())

    story.append(Paragraph(
        "Every booking generates revenue that is split between Court 474 and the apartment owner. The "
        "platform handles this automatically:", BODY))

    story.append(Spacer(1, 3 * mm))
    story.append(Paragraph("The Revenue Flow", H2))

    story.append(Paragraph("1. Guest pays for booking (e.g., \u20a650,000 for 3 nights)", NUM))
    story.append(Paragraph("2. Payment lands in Court 474\u2019s Paystack account", NUM))
    story.append(Paragraph("3. System calculates the split:", NUM))
    story.append(Paragraph("    \u2022  <b>Court 474 agency charge</b> \u2014 a percentage of the booking amount (e.g., 20%)", BUL))
    story.append(Paragraph("    \u2022  <b>Owner net amount</b> \u2014 the remainder (e.g., 80%)", BUL))
    story.append(Paragraph("4. The split is recorded and visible to both Court 474 management and the apartment owner", NUM))
    story.append(Paragraph("5. Court 474 disburses to the owner on an agreed schedule (weekly or monthly)", NUM))

    story.append(Spacer(1, 3 * mm))
    story.append(Paragraph("Example:", H3))

    ex_data = [
        [Paragraph("<b>Item</b>", TH), Paragraph("<b>Amount</b>", TH)],
        [Paragraph("Guest pays (3 nights \u00d7 \u20a615,000/night)", TC), Paragraph("\u20a645,000", TC)],
        [Paragraph("Paystack processing fee (1.5%)", TC), Paragraph("\u2212 \u20a6675", TC)],
        [Paragraph("Net received", TCB), Paragraph("\u20a644,325", TCB)],
        [Paragraph("Court 474 agency charge (20%)", TC), Paragraph("\u20a68,865", TC)],
        [Paragraph("Owner net payout", TCB), Paragraph("\u20a635,460", TCB)],
    ]
    et = Table(ex_data, colWidths=[aw * 0.6, aw * 0.4])
    et.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,0), TABLE_HEADER_BG),
        ("VALIGN", (0,0), (-1,-1), "TOP"),
        ("TOPPADDING", (0,0), (-1,-1), 6), ("BOTTOMPADDING", (0,0), (-1,-1), 6),
        ("LEFTPADDING", (0,0), (-1,-1), 8), ("RIGHTPADDING", (0,0), (-1,-1), 8),
        ("ROWBACKGROUNDS", (0,1), (-1,-2), [WHITE, TABLE_ALT_ROW]),
        ("LINEABOVE", (0,-1), (-1,-1), 1, ACCENT_BLUE),
        ("BOX", (0,0), (-1,-1), 0.5, BORDER_COLOR),
    ]))
    story.append(et)

    story.append(Spacer(1, 3 * mm))
    story.append(Paragraph(
        "<b>Note:</b> The agency charge percentage is configurable and agreed between Court 474 and its "
        "owners. It can be set globally or per apartment if different owners have different agreements.", BODY))

    story.append(Spacer(1, 3 * mm))
    story.append(Paragraph("Owner Settlement Reports", H2))
    story.append(Paragraph("Each owner receives automated settlement reports showing:", BODY))
    story.append(Paragraph("\u2022  Each booking on their apartment (dates, guest, amount)", BUL))
    story.append(Paragraph("\u2022  Gross amount received", BUL))
    story.append(Paragraph("\u2022  Agency charge deducted", BUL))
    story.append(Paragraph("\u2022  Net payout amount", BUL))
    story.append(Paragraph("\u2022  Running total for the period", BUL))
    story.append(Paragraph("\u2022  Comparison to property average (fairness metric)", BUL))

    story.append(PageBreak())

    # ========== 8. CONFERENCE ROOM ==========
    story.append(Paragraph("8. CONFERENCE ROOM BOOKING", H1))
    story.append(hr())

    story.append(Paragraph(
        "The 40-seater conference room operates as a separate revenue stream with its own booking flow:", BODY))
    story.append(Paragraph("\u2022  <b>Hourly and daily booking options</b> \u2014 clients can book by the hour or for a full day", BUL))
    story.append(Paragraph("\u2022  <b>Online availability calendar</b> \u2014 visible on the booking page, shows available slots in real time", BUL))
    story.append(Paragraph("\u2022  <b>Online payment</b> \u2014 same Paystack integration, instant confirmation", BUL))
    story.append(Paragraph("\u2022  <b>Add-ons</b> \u2014 projector, catering, and other services can be added as optional extras", BUL))
    story.append(Paragraph("\u2022  <b>Access instructions</b> \u2014 sent automatically upon booking confirmation", BUL))
    story.append(Paragraph("\u2022  <b>Separate marketing</b> \u2014 the conference room can be marketed independently from the apartments", BUL))

    story.append(Paragraph(
        "Conference room revenue goes entirely to Court 474 (unless a different arrangement is agreed "
        "with apartment owners).", BODY))

    story.append(Spacer(1, 6 * mm))

    # ========== 9. SPACER FEATURES FOR COURT 474 ==========
    story.append(Paragraph("9. SPACER FEATURES FOR COURT 474", H1))
    story.append(hr())

    story.append(Paragraph("All of the following are existing Spacer capabilities that will be deployed for Court 474:", BODY))
    story.append(Spacer(1, 2 * mm))

    features = [
        ("Branded Booking Portal", "Custom booking page with property photos, apartment types, date selection, and online payment"),
        ("Fair Distribution Algorithm", "Apartment selection ensuring equitable bookings and revenue across all owners"),
        ("TTLock Smart Lock Integration", "Unique access codes generated per booking, tied to stay period, auto-expire at checkout"),
        ("Cart Abandonment Recovery", "Automatic reminders to guests who start but don\u2019t complete bookings"),
        ("Owner Dashboard", "Each owner sees bookings, revenue, fairness metrics, and can block dates for personal use"),
        ("Revenue Splitting", "Automatic agency charge deduction and owner settlement with full audit trail"),
        ("Temporary Space Removal", "Owners block dates for personal use/maintenance; apartment auto-returns when period ends"),
        ("Conference Room Booking", "Separate hourly/daily booking flow with availability calendar and payment"),
        ("Admin Dashboard", "Management sees all bookings, occupancy, revenue, settlements, and fairness metrics"),
        ("Automated Notifications", "Booking confirmations, access codes, reminders, settlement reports via email and SMS"),
        ("Real-Time Occupancy", "Visual grid showing occupied, available, and blocked apartments at a glance"),
        ("Invoice &amp; Receipt Generation", "Automatic for all bookings \u2014 exportable as PDF"),
        ("Conflict Prevention", "Prevents double-bookings across the entire property"),
    ]

    feat_data = [[Paragraph("<b>Feature</b>", TH), Paragraph("<b>Description</b>", TH)]]
    for fname, fdesc in features:
        feat_data.append([Paragraph(fname, TCB), Paragraph(fdesc, TC)])

    ft = Table(feat_data, colWidths=[aw * 0.3, aw * 0.7])
    ft.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,0), TABLE_HEADER_BG),
        ("VALIGN", (0,0), (-1,-1), "TOP"),
        ("TOPPADDING", (0,0), (-1,-1), 5), ("BOTTOMPADDING", (0,0), (-1,-1), 5),
        ("LEFTPADDING", (0,0), (-1,-1), 6), ("RIGHTPADDING", (0,0), (-1,-1), 6),
        ("ROWBACKGROUNDS", (0,1), (-1,-1), [WHITE, TABLE_ALT_ROW]),
        ("BOX", (0,0), (-1,-1), 0.5, BORDER_COLOR),
        ("LINEBELOW", (0,0), (-1,-2), 0.25, BORDER_COLOR),
    ]))
    story.append(ft)

    story.append(PageBreak())

    # ========== 10. SMART ACCESS & SMART HOME ADVISORY ==========
    story.append(Paragraph("10. SMART ACCESS &amp; SMART HOME ADVISORY", H1))
    story.append(hr())

    story.append(Paragraph("TTLock Smart Door Locks", H2))
    story.append(Paragraph(
        "We recommend <b>TTLock</b> smart locks for all 29 apartments and the conference room. TTLock is the "
        "smart lock brand that Spacer integrates with natively. These locks support:", BODY))

    story.append(Paragraph("\u2022  <b>Temporary passcodes</b> \u2014 generated by Spacer per booking, valid only for the stay period", BUL))
    story.append(Paragraph("\u2022  <b>Auto-expiry</b> \u2014 codes deactivate automatically at checkout time", BUL))
    story.append(Paragraph("\u2022  <b>Remote management</b> \u2014 lock/unlock remotely from the admin dashboard", BUL))
    story.append(Paragraph("\u2022  <b>Audit trail</b> \u2014 every lock/unlock event is logged with timestamp", BUL))
    story.append(Paragraph("\u2022  <b>Battery powered</b> \u2014 no wiring required, easy to install on existing doors", BUL))
    story.append(Paragraph("\u2022  <b>Bluetooth + Wi-Fi gateway</b> \u2014 TTLock G2 gateway enables remote access over the internet", BUL))

    story.append(Spacer(1, 3 * mm))
    story.append(Paragraph(
        "<b>Procurement:</b> Court 474 procures the TTLock hardware directly. Algolog handles the software "
        "integration \u2014 connecting each lock to Spacer so access codes are generated and managed "
        "automatically with every booking.", BODY))

    story.append(Spacer(1, 6 * mm))
    story.append(Paragraph("Fully Smart Apartment System", H2))
    story.append(Paragraph(
        "Beyond door locks, Court 474 has expressed interest in a fully smart apartment setup where everything "
        "can be controlled and automated. We recommend the following smart home components:", BODY))

    story.append(Spacer(1, 2 * mm))
    smart_items = [
        ("Smart Lighting", "Wi-Fi or Zigbee smart bulbs/switches that can be scheduled, dimmed, or turned off remotely. "
         "Can be configured to turn off automatically when the guest\u2019s access code expires (checkout)."),
        ("Smart Switches &amp; Sockets", "Replace standard wall switches with smart switches. Allows remote control of "
         "all electrical outlets \u2014 lights, AC, water heater. Everything can be shut off centrally when the "
         "apartment is unoccupied."),
        ("Smart AC Control", "IR blasters or smart thermostats that control air conditioning units remotely. "
         "AC can be pre-cooled before guest arrival and shut off on checkout."),
        ("Automated Shutoff on Departure", "When a guest\u2019s TTLock code expires or they check out, the system "
         "can trigger a \u201cshutoff all\u201d command \u2014 turning off lights, AC, water heater, and non-essential "
         "sockets. This reduces electricity waste between guests."),
        ("Energy Monitoring", "Smart meters or energy monitoring plugs to track electricity consumption per "
         "apartment. Useful for billing owners or identifying wasteful usage patterns."),
    ]

    for item_name, item_desc in smart_items:
        story.append(Paragraph(item_name, H3))
        story.append(Paragraph(item_desc, BODY))

    story.append(Spacer(1, 3 * mm))
    story.append(Paragraph(
        "<b>Procurement:</b> Court 474 procures all smart home hardware (switches, bulbs, IR blasters, "
        "energy monitors) directly from suppliers. Algolog provides the advisory on which specific "
        "products are compatible and handles the software synchronisation \u2014 connecting the smart home "
        "devices to Spacer so they respond to booking events (check-in, checkout, code expiry).", BODY))

    story.append(PageBreak())

    # ========== 11. INVESTMENT ==========
    story.append(Paragraph("11. INVESTMENT", H1))
    story.append(hr())

    story.append(Paragraph("A. Spacer Platform Setup &amp; Deployment", H2))
    story.append(Paragraph(
        "This covers the full Spacer deployment for Court 474 \u2014 booking portal, fair distribution algorithm, "
        "payment processing, revenue splitting, owner dashboards, cart abandonment recovery, conference room "
        "booking, admin dashboard, TTLock integration, and all automated notifications.", BODY))

    story.append(Spacer(1, 3 * mm))

    price_a = [
        [Paragraph("<b>Item</b>", TH), Paragraph("<b>Cost (NGN)</b>", TH)],
        [Paragraph("Spacer Platform Setup &amp; Deployment (29 apartments + conference room)", TC),
         Paragraph("Included", TC)],
        [Paragraph("Fair Distribution Algorithm Configuration", TC),
         Paragraph("Included", TC)],
        [Paragraph("TTLock Software Integration (up to 30 locks)", TC),
         Paragraph("Included", TC)],
        [Paragraph("Revenue Splitting Configuration", TC),
         Paragraph("Included", TC)],
        [Paragraph("Cart Abandonment &amp; Notification System", TC),
         Paragraph("Included", TC)],
        [Paragraph("Training &amp; Handover", TC),
         Paragraph("Included", TC)],
        [Paragraph("<b>Total Spacer Deployment</b>", TCB),
         Paragraph("<b>\u20a610,000,000</b>", TCB)],
    ]
    pa = Table(price_a, colWidths=[aw * 0.65, aw * 0.35])
    pa.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,0), TABLE_HEADER_BG),
        ("VALIGN", (0,0), (-1,-1), "TOP"),
        ("TOPPADDING", (0,0), (-1,-1), 6), ("BOTTOMPADDING", (0,0), (-1,-1), 6),
        ("LEFTPADDING", (0,0), (-1,-1), 8), ("RIGHTPADDING", (0,0), (-1,-1), 8),
        ("ROWBACKGROUNDS", (0,1), (-1,-2), [WHITE, TABLE_ALT_ROW]),
        ("LINEABOVE", (0,-1), (-1,-1), 1, ACCENT_BLUE),
        ("BOX", (0,0), (-1,-1), 0.5, BORDER_COLOR),
    ]))
    story.append(pa)

    story.append(Spacer(1, 6 * mm))
    story.append(Paragraph("B. Smart Home Synchronisation Setup", H2))
    story.append(Paragraph(
        "This covers the software integration of smart home devices (lighting, switches, AC control, "
        "automated shutoff) with the Spacer platform \u2014 so they respond to booking events automatically. "
        "Hardware procurement is handled separately by Court 474.", BODY))

    story.append(Spacer(1, 3 * mm))

    price_b = [
        [Paragraph("<b>Item</b>", TH), Paragraph("<b>Cost (NGN)</b>", TH)],
        [Paragraph("Smart Home Device Integration with Spacer (up to 29 apartments)", TC),
         Paragraph("Included", TC)],
        [Paragraph("Automated Shutoff Logic (checkout triggers all-off)", TC),
         Paragraph("Included", TC)],
        [Paragraph("Energy Monitoring Dashboard Integration", TC),
         Paragraph("Included", TC)],
        [Paragraph("Device Advisory &amp; Compatibility Testing", TC),
         Paragraph("Included", TC)],
        [Paragraph("<b>Total Smart Home Synchronisation</b>", TCB),
         Paragraph("<b>\u20a62,000,000</b>", TCB)],
    ]
    pb = Table(price_b, colWidths=[aw * 0.65, aw * 0.35])
    pb.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,0), TABLE_HEADER_BG),
        ("VALIGN", (0,0), (-1,-1), "TOP"),
        ("TOPPADDING", (0,0), (-1,-1), 6), ("BOTTOMPADDING", (0,0), (-1,-1), 6),
        ("LEFTPADDING", (0,0), (-1,-1), 8), ("RIGHTPADDING", (0,0), (-1,-1), 8),
        ("ROWBACKGROUNDS", (0,1), (-1,-2), [WHITE, TABLE_ALT_ROW]),
        ("LINEABOVE", (0,-1), (-1,-1), 1, ACCENT_BLUE),
        ("BOX", (0,0), (-1,-1), 0.5, BORDER_COLOR),
    ]))
    story.append(pb)

    story.append(Spacer(1, 6 * mm))

    # Total
    total_data = [
        [Paragraph("<b>Component</b>", TH), Paragraph("<b>Cost (NGN)</b>", TH)],
        [Paragraph("Spacer Platform Setup &amp; Deployment", TC), Paragraph("\u20a610,000,000", TC)],
        [Paragraph("Smart Home Synchronisation Setup", TC), Paragraph("\u20a62,000,000", TC)],
        [Paragraph("<b>Total Investment</b>", TCB), Paragraph("<b>\u20a612,000,000</b>", TCB)],
    ]
    tt = Table(total_data, colWidths=[aw * 0.65, aw * 0.35])
    tt.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,0), TABLE_HEADER_BG),
        ("VALIGN", (0,0), (-1,-1), "TOP"),
        ("TOPPADDING", (0,0), (-1,-1), 6), ("BOTTOMPADDING", (0,0), (-1,-1), 6),
        ("LEFTPADDING", (0,0), (-1,-1), 8), ("RIGHTPADDING", (0,0), (-1,-1), 8),
        ("ROWBACKGROUNDS", (0,1), (-1,-2), [WHITE, TABLE_ALT_ROW]),
        ("LINEABOVE", (0,-1), (-1,-1), 1.5, ACCENT_BLUE),
        ("BOX", (0,0), (-1,-1), 0.5, BORDER_COLOR),
    ]))
    story.append(tt)

    story.append(Spacer(1, 4 * mm))
    story.append(Paragraph(
        "<b>Note:</b> The above covers all software setup, configuration, integration, and training. "
        "Hardware procurement (TTLock door locks, smart switches, smart bulbs, IR blasters, energy monitors, "
        "Wi-Fi gateways) is handled directly by Court 474. Algolog will provide a detailed hardware "
        "specification list with recommended models and quantities.", BODY))

    story.append(PageBreak())

    # ========== WHY ALGOLOG ==========
    story.append(Paragraph("WHY ALGOLOG", H1))
    story.append(hr())

    story.append(Paragraph(
        "Algolog Limited is a Nigerian technology company committed to ensuring businesses across Africa get "
        "the technology they need to build their future, improve their sales, and strengthen their operations.", BODY))

    story.append(Spacer(1, 3 * mm))
    story.append(Paragraph("Our work includes:", H3))
    story.append(Paragraph("\u2022  <b>Spacer</b> (spacer.so) \u2014 Smart hospitality and workspace management platform, "
        "deployed across multiple properties in Abuja, Kaduna, and Lagos", BUL))
    story.append(Paragraph("\u2022  <b>DeepThread</b> (deepthread.ai) \u2014 AI-powered cross-platform context engine", BUL))
    story.append(Paragraph("\u2022  <b>Visora</b> (visora-ai.com) \u2014 AI-powered data analytics and insights platform", BUL))
    story.append(Paragraph("\u2022  <b>PrivateTransfer</b> (privatetransfer.ng) \u2014 Secure transfer platform", BUL))

    story.append(Spacer(1, 4 * mm))
    story.append(Paragraph(
        "Spacer is already live and processing bookings at properties across Nigeria. Every feature described "
        "in this document is a production-ready Spacer capability. Court 474 is getting a proven, deployed "
        "platform \u2014 not a promise.", BODY))

    story.append(Spacer(1, 8 * mm))

    # ========== NEXT STEP ==========
    story.append(Paragraph("NEXT STEP", H1))
    story.append(hr())

    story.append(Paragraph(
        "<b>We\u2019d love to continue the conversation</b> \u2014 the owner agreements, the agency charge "
        "structure, the smart home hardware specifications, and the deployment timeline.", BODY_B))

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
