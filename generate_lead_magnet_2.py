"""
Generate Lead Magnet #2: "Kill the Key Handover: A Smart Lock Playbook for Serviced Apartments in Nigeria"
Format: Branded PDF — multi-page playbook with callout boxes, numbered steps, and self-assessment
Aligned with Alex Hormozi's lead magnet framework (give away the secret, sell the implementation)
"""

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib.colors import HexColor
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Image, Table, TableStyle,
    HRFlowable, KeepTogether, PageBreak, Flowable
)
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from PIL import Image as PILImage
import os

# --- Paths ---
BASE = "C:/Users/Femi Fayinminu/OneDrive/Documents/Algolog/Algolog_Projects"
FONT_DIR = os.path.join(BASE, "fonts/lexend-main/fonts/lexend/ttf")
BANNER_PATH = os.path.join(BASE, "claude.ai contex/banner_centered.png")
OUTPUT_PATH = os.path.join(BASE, "Proposals/Lead-Magnet-Kill-The-Key-Handover.pdf")

# --- Register Lexend Fonts ---
pdfmetrics.registerFont(TTFont("Lexend", os.path.join(FONT_DIR, "Lexend-Regular.ttf")))
pdfmetrics.registerFont(TTFont("Lexend-Bold", os.path.join(FONT_DIR, "Lexend-Bold.ttf")))
pdfmetrics.registerFont(TTFont("Lexend-SemiBold", os.path.join(FONT_DIR, "Lexend-SemiBold.ttf")))
pdfmetrics.registerFont(TTFont("Lexend-Light", os.path.join(FONT_DIR, "Lexend-Light.ttf")))
pdfmetrics.registerFont(TTFont("Lexend-Medium", os.path.join(FONT_DIR, "Lexend-Medium.ttf")))

# --- Colors ---
ACCENT_BLUE = HexColor("#0f3460")
DARK_TEXT = HexColor("#1a1a1a")
MEDIUM_TEXT = HexColor("#333333")
LIGHT_TEXT = HexColor("#555555")
BORDER_COLOR = HexColor("#dcdde1")
GREEN = HexColor("#27ae60")
GREEN_LIGHT = HexColor("#eafaf1")
RED_ACCENT = HexColor("#c0392b")
RED_LIGHT = HexColor("#fdedec")
ORANGE_ACCENT = HexColor("#e67e22")
ORANGE_LIGHT = HexColor("#fef5e7")
BLUE_LIGHT = HexColor("#eaf2f8")
YELLOW_LIGHT = HexColor("#fef9e7")
TABLE_HEADER_BG = HexColor("#1a1a2e")
TABLE_ALT_ROW = HexColor("#f5f6fa")
WHITE = HexColor("#ffffff")

# --- Page Setup ---
PAGE_W, PAGE_H = A4
LEFT_MARGIN = 22 * mm
RIGHT_MARGIN = 22 * mm
TOP_MARGIN = 20 * mm
BOTTOM_MARGIN = 18 * mm
AVAIL_W = PAGE_W - LEFT_MARGIN - RIGHT_MARGIN


# --- Styles ---
def make_style(name, **kwargs):
    defaults = {
        "fontName": "Lexend",
        "fontSize": 10,
        "leading": 14,
        "textColor": DARK_TEXT,
        "alignment": TA_LEFT,
        "spaceAfter": 6,
    }
    defaults.update(kwargs)
    return ParagraphStyle(name, **defaults)


S_BODY = make_style("S_BODY", fontSize=9.5, leading=14, textColor=MEDIUM_TEXT, alignment=TA_JUSTIFY, spaceAfter=6)
S_BODY_CENTER = make_style("S_BODY_CENTER", fontSize=9.5, leading=14, textColor=MEDIUM_TEXT, alignment=TA_CENTER, spaceAfter=6)
S_BODY_BOLD = make_style("S_BODY_BOLD", fontName="Lexend-Bold", fontSize=9.5, leading=14, textColor=DARK_TEXT, spaceAfter=6)
S_H1 = make_style("S_H1", fontName="Lexend-Bold", fontSize=15, leading=20, textColor=ACCENT_BLUE, spaceBefore=12, spaceAfter=6)
S_H2 = make_style("S_H2", fontName="Lexend-SemiBold", fontSize=12, leading=16, textColor=DARK_TEXT, spaceBefore=10, spaceAfter=5)
S_H3 = make_style("S_H3", fontName="Lexend-SemiBold", fontSize=11, leading=14, textColor=MEDIUM_TEXT, spaceBefore=8, spaceAfter=4)
S_BULLET = make_style("S_BULLET", fontSize=9, leading=13, textColor=MEDIUM_TEXT, leftIndent=14, bulletIndent=4, spaceAfter=3)
S_BULLET_BOLD = make_style("S_BULLET_BOLD", fontName="Lexend-SemiBold", fontSize=9, leading=13, textColor=DARK_TEXT, leftIndent=14, bulletIndent=4, spaceAfter=3)
S_SMALL = make_style("S_SMALL", fontName="Lexend-Light", fontSize=7.5, leading=10, textColor=LIGHT_TEXT, alignment=TA_CENTER)
S_TABLE_HEADER = make_style("S_TABLE_HEADER", fontName="Lexend-Bold", fontSize=8.5, leading=12, textColor=WHITE)
S_TABLE_CELL = make_style("S_TABLE_CELL", fontSize=8.5, leading=12, textColor=MEDIUM_TEXT)
S_TABLE_CELL_BOLD = make_style("S_TABLE_CELL_BOLD", fontName="Lexend-Bold", fontSize=8.5, leading=12, textColor=DARK_TEXT)
S_QUOTE = make_style("S_QUOTE", fontName="Lexend", fontSize=8.5, leading=12, textColor=MEDIUM_TEXT, leftIndent=20, rightIndent=20, spaceAfter=4)


class NumberBadge(Flowable):
    """A colored circle with a number inside."""
    def __init__(self, number, color, size=22):
        Flowable.__init__(self)
        self.number = str(number)
        self.color = color
        self.size = size
        self.width = size + 4
        self.height = size + 4

    def draw(self):
        r = self.size / 2
        self.canv.setFillColor(self.color)
        self.canv.circle(r + 2, r + 2, r, fill=1, stroke=0)
        self.canv.setFillColor(WHITE)
        self.canv.setFont("Lexend-Bold", 11)
        self.canv.drawCentredString(r + 2, r - 2, self.number)


def add_footer(canvas_obj, doc):
    canvas_obj.saveState()
    canvas_obj.setFont("Lexend-Light", 7)
    canvas_obj.setFillColor(LIGHT_TEXT)
    canvas_obj.drawCentredString(
        PAGE_W / 2, 10 * mm,
        f"Algolog Limited  |  algolog.co  |  spacer.so  |  Page {doc.page}"
    )
    canvas_obj.restoreState()


def hr():
    return HRFlowable(width="100%", thickness=0.5, color=BORDER_COLOR, spaceAfter=6, spaceBefore=6)


def callout_box(content_elements, bg_color, border_color=None):
    """Create a colored callout box containing a list of flowable elements."""
    inner_w = AVAIL_W - 20
    rows = [[el] for el in content_elements]
    tbl = Table(rows, colWidths=[inner_w])
    style_cmds = [
        ("BACKGROUND", (0, 0), (-1, -1), bg_color),
        ("TOPPADDING", (0, 0), (0, 0), 10),
        ("BOTTOMPADDING", (0, -1), (-1, -1), 10),
        ("LEFTPADDING", (0, 0), (-1, -1), 12),
        ("RIGHTPADDING", (0, 0), (-1, -1), 12),
        ("TOPPADDING", (0, 1), (-1, -1), 1),
        ("BOTTOMPADDING", (0, 0), (-1, -2), 1),
    ]
    if border_color:
        style_cmds.append(("LINEBELOW", (0, 0), (-1, -1), 0, bg_color))
        style_cmds.append(("BOX", (0, 0), (-1, -1), 1, border_color))
    tbl.setStyle(TableStyle(style_cmds))
    return tbl


def step_row(number, color, title_text, body_text):
    """Build a numbered step with a badge and description."""
    badge = NumberBadge(number, color)
    inner_w = AVAIL_W - 50
    combined = Paragraph(
        f'<font face="Lexend-SemiBold" color="#1a1a1a">{title_text}</font><br/>'
        f'<font face="Lexend" color="#333333">{body_text}</font>',
        make_style(f"step_{number}", fontSize=9, leading=13, textColor=MEDIUM_TEXT, spaceAfter=2)
    )
    tbl = Table([[badge, combined]], colWidths=[32, inner_w])
    tbl.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (0, 0), 0),
        ("LEFTPADDING", (1, 0), (1, 0), 6),
        ("TOPPADDING", (0, 0), (-1, -1), 2),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 2),
    ]))
    return tbl


def build_pdf():
    doc = SimpleDocTemplate(
        OUTPUT_PATH,
        pagesize=A4,
        leftMargin=LEFT_MARGIN,
        rightMargin=RIGHT_MARGIN,
        topMargin=TOP_MARGIN,
        bottomMargin=BOTTOM_MARGIN,
    )

    story = []

    # =====================================================
    # PAGE 1: COVER
    # =====================================================

    # Banner
    if os.path.exists(BANNER_PATH):
        img = PILImage.open(BANNER_PATH)
        aspect = img.size[1] / img.size[0]
        display_w = AVAIL_W
        display_h = display_w * aspect
        banner = Image(BANNER_PATH, width=display_w, height=display_h)
        story.append(banner)

    story.append(Spacer(1, 14 * mm))
    story.append(hr())
    story.append(Spacer(1, 8 * mm))

    # Title
    story.append(Paragraph(
        "Kill the Key Handover",
        make_style("cover_title", fontName="Lexend-Bold", fontSize=28, leading=34,
                    textColor=ACCENT_BLUE, alignment=TA_CENTER, spaceAfter=4)))

    story.append(Spacer(1, 2 * mm))

    story.append(Paragraph(
        "A Smart Lock Playbook for<br/>Serviced Apartments in Nigeria",
        make_style("cover_sub", fontName="Lexend-Medium", fontSize=14, leading=19,
                    textColor=MEDIUM_TEXT, alignment=TA_CENTER, spaceAfter=6)))

    story.append(Spacer(1, 10 * mm))
    story.append(hr())
    story.append(Spacer(1, 6 * mm))

    # Intro blurb
    story.append(Paragraph(
        "Physical keys are costing you more than you think. Late-night arrivals, lost keys, "
        "staff overtime, bad reviews. This playbook shows you exactly how to fix it "
        "\u2014 starting today, for free \u2014 and what full automation looks like when you're ready to scale.",
        make_style("cover_intro", fontSize=10.5, leading=15, textColor=MEDIUM_TEXT,
                    alignment=TA_CENTER, spaceAfter=8)))

    story.append(Spacer(1, 6 * mm))

    # What's inside
    story.append(Paragraph(
        "What\u2019s inside:",
        make_style("cover_inside_h", fontName="Lexend-SemiBold", fontSize=11, leading=15,
                    textColor=DARK_TEXT, alignment=TA_CENTER, spaceAfter=6)))

    inside_items = [
        "The real annual cost of physical key management",
        "Smart locks that work in Nigeria (with price ranges)",
        "How time-bound access codes work",
        "A free, step-by-step fix you can implement this week",
        "What full automation looks like at scale",
        "A self-assessment scorecard for your property",
    ]
    for item in inside_items:
        story.append(Paragraph(
            f'\u2022  {item}',
            make_style(f"ci_{item[:6]}", fontSize=9.5, leading=14, textColor=MEDIUM_TEXT,
                        alignment=TA_CENTER, spaceAfter=3)))

    story.append(Spacer(1, 12 * mm))

    story.append(Paragraph(
        "A free guide by Algolog Limited  |  spacer.so",
        make_style("cover_tag", fontName="Lexend-Light", fontSize=9, leading=12,
                    textColor=LIGHT_TEXT, alignment=TA_CENTER)))

    story.append(PageBreak())

    # =====================================================
    # PAGE 2: THE REAL COST OF PHYSICAL KEYS
    # =====================================================

    story.append(Paragraph("THE REAL COST OF PHYSICAL KEYS", S_H1))
    story.append(hr())

    story.append(Paragraph(
        "Every serviced apartment operator in Nigeria knows the drill. A guest\u2019s flight lands at 11 PM. "
        "Your receptionist finished their shift two hours ago. Now someone has to drive to the property, "
        "hand over a key, and drive back home. Or the guest waits. Neither option is good.",
        S_BODY))

    story.append(Paragraph(
        "Physical keys create problems that most operators have accepted as \u201Cjust how it works.\u201D "
        "But they don\u2019t have to be.",
        S_BODY))

    story.append(Spacer(1, 2 * mm))

    # Problem bullets
    problems = [
        ("<b>Late-night arrivals with no one at reception.</b> Abuja and Lagos airports have flights "
         "landing past 10 PM regularly. If your guest can\u2019t get into their room without a human "
         "being physically present, you\u2019re either paying staff overtime or making guests wait. Both cost you."),
        ("<b>Lost or unreturned keys.</b> Guests forget to return keys. Each replacement costs "
         "NGN 5,000\u201315,000 depending on the lock type. And while the key is out there, your "
         "security is compromised \u2014 someone has physical access to your property."),
        ("<b>Staff overtime for late check-ins.</b> If a guest is arriving at midnight, someone has "
         "to be there. That\u2019s either overtime pay (NGN 3,000\u20135,000 per late-night handover) or "
         "a full night-shift salary. For a property that gets 8\u201310 late arrivals per month, this adds up."),
        ("<b>Bad first impressions kill reviews.</b> A guest who waits 30 minutes in a car park "
         "at 11 PM for a key handover is not leaving a 5-star review. That one bad review sits "
         "on your listing and quietly deters the next 10 potential bookings."),
        ("<b>Unreturned keys are a security risk.</b> When a guest checks out and keeps the key, "
         "that key still opens your door. The only fix is to change the entire lock or accept the risk."),
    ]
    for p in problems:
        story.append(Paragraph(f"\u2022  {p}", S_BULLET))

    story.append(Spacer(1, 4 * mm))

    # Cost calculator callout box (yellow)
    cost_title = Paragraph(
        '\U0001F4B0  <font face="Lexend-SemiBold" color="#b7791f">What it\u2019s costing you (annual estimate):</font>',
        make_style("cost_h", fontSize=9.5, leading=13, textColor=DARK_TEXT, spaceAfter=4))

    cost_data = [
        [Paragraph("<b>Cost Item</b>", S_TABLE_HEADER),
         Paragraph("<b>Monthly</b>", S_TABLE_HEADER),
         Paragraph("<b>Annual</b>", S_TABLE_HEADER)],
        [Paragraph("Late arrivals requiring staff\n(8/month \u00d7 NGN 4,000)", S_TABLE_CELL),
         Paragraph("NGN 32,000", S_TABLE_CELL),
         Paragraph("NGN 384,000", S_TABLE_CELL)],
        [Paragraph("Lost/unreturned keys\n(3/month \u00d7 NGN 10,000)", S_TABLE_CELL),
         Paragraph("NGN 30,000", S_TABLE_CELL),
         Paragraph("NGN 360,000", S_TABLE_CELL)],
        [Paragraph("Bad reviews \u2192 lost referrals\n(2 lost bookings \u00d7 NGN 50,000)", S_TABLE_CELL),
         Paragraph("NGN 100,000", S_TABLE_CELL),
         Paragraph("NGN 1,200,000", S_TABLE_CELL)],
        [Paragraph("Lock changes for security\n(1/quarter \u00d7 NGN 25,000)", S_TABLE_CELL),
         Paragraph("NGN 6,250", S_TABLE_CELL),
         Paragraph("NGN 75,000", S_TABLE_CELL)],
        [Paragraph("<b>Total estimated cost</b>", S_TABLE_CELL_BOLD),
         Paragraph("<b>NGN 168,250</b>", S_TABLE_CELL_BOLD),
         Paragraph("<b>NGN 2,019,000</b>", S_TABLE_CELL_BOLD)],
    ]
    inner_w = AVAIL_W - 28
    cost_table = Table(cost_data, colWidths=[inner_w * 0.50, inner_w * 0.25, inner_w * 0.25])
    cost_table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), TABLE_HEADER_BG),
        ("TEXTCOLOR", (0, 0), (-1, 0), WHITE),
        ("BACKGROUND", (0, 2), (-1, 2), TABLE_ALT_ROW),
        ("BACKGROUND", (0, 4), (-1, 4), TABLE_ALT_ROW),
        ("BACKGROUND", (0, -1), (-1, -1), HexColor("#fff3cd")),
        ("FONTNAME", (0, 0), (-1, -1), "Lexend"),
        ("FONTSIZE", (0, 0), (-1, -1), 8),
        ("ALIGN", (1, 0), (-1, -1), "CENTER"),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("TOPPADDING", (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
        ("LEFTPADDING", (0, 0), (-1, -1), 6),
        ("GRID", (0, 0), (-1, -1), 0.5, BORDER_COLOR),
    ]))

    cost_note = Paragraph(
        '<font face="Lexend" size="8" color="#555555">'
        'Plug in your own numbers. Even if your costs are half of this, you\u2019re looking at over '
        'NGN 1 million per year spent on managing physical keys.</font>',
        make_style("cost_note", fontSize=8, leading=11, textColor=LIGHT_TEXT, spaceAfter=0))

    cost_box = callout_box([cost_title, Spacer(1, 2 * mm), cost_table, Spacer(1, 2 * mm), cost_note], YELLOW_LIGHT)
    story.append(cost_box)

    story.append(PageBreak())

    # =====================================================
    # PAGE 3: SMART LOCKS THAT WORK IN NIGERIA
    # =====================================================

    story.append(Paragraph("SMART LOCKS THAT WORK IN NIGERIA", S_H1))
    story.append(hr())

    story.append(Paragraph(
        "Not all smart locks are created equal \u2014 and not all of them work well in Nigeria\u2019s "
        "operating environment. Here\u2019s what you need to know.",
        S_BODY))

    story.append(Spacer(1, 2 * mm))
    story.append(Paragraph("Types of smart locks:", S_H2))

    lock_types = [
        ("<b>Keypad locks (recommended for Nigeria).</b> The guest punches in a numeric code to "
         "unlock the door. No phone required, no internet required, no Bluetooth pairing. These are "
         "the most reliable option for the Nigerian market because they work during power outages, "
         "don\u2019t depend on Wi-Fi, and don\u2019t require guests to download any app."),
        ("<b>Bluetooth locks.</b> The guest uses their phone (via an app) to unlock the door. Requires "
         "the guest to download an app and pair their phone. Works without internet but adds friction "
         "\u2014 especially for older guests or those unfamiliar with Bluetooth pairing."),
        ("<b>Wi-Fi locks.</b> Connected to the internet, can be managed remotely. But they depend on "
         "stable Wi-Fi \u2014 and in many Nigerian properties, Wi-Fi reliability varies. If the power is "
         "out and the router is down, the guest can\u2019t get in."),
    ]
    for lt in lock_types:
        story.append(Paragraph(f"\u2022  {lt}", S_BULLET))
        story.append(Spacer(1, 1 * mm))

    story.append(Spacer(1, 2 * mm))
    story.append(Paragraph("What to look for:", S_H2))

    criteria = [
        "<b>Offline capability</b> \u2014 Non-negotiable in Nigeria. Keypad locks run on AA batteries and work completely offline.",
        "<b>Durability</b> \u2014 Built for harmattan dust, humidity, and heavy daily use.",
        "<b>Battery life</b> \u2014 Most keypad locks run on 4\u00d7 AA batteries, lasting 6\u201312 months. Some alert you when low.",
        "<b>Multiple code capacity</b> \u2014 At least 50\u2013100 unique codes for different guests.",
        "<b>Easy code management</b> \u2014 Add and delete codes quickly via the lock\u2019s keypad or a connected app.",
    ]
    for c in criteria:
        story.append(Paragraph(f"\u2022  {c}", S_BULLET))

    story.append(Spacer(1, 4 * mm))
    story.append(Paragraph("Price ranges (Nigeria market):", S_H2))

    price_data = [
        [Paragraph("<b>Tier</b>", S_TABLE_HEADER),
         Paragraph("<b>Price Range (NGN)</b>", S_TABLE_HEADER),
         Paragraph("<b>What You Get</b>", S_TABLE_HEADER)],
        [Paragraph("Budget", S_TABLE_CELL_BOLD),
         Paragraph("50,000 \u2013 80,000", S_TABLE_CELL),
         Paragraph("Basic keypad lock, manual code setting, 20\u201350 codes, battery-powered", S_TABLE_CELL)],
        [Paragraph("Mid-range", S_TABLE_CELL_BOLD),
         Paragraph("100,000 \u2013 200,000", S_TABLE_CELL),
         Paragraph("Keypad + Bluetooth/Wi-Fi, app management, 100+ codes, auto-lock feature", S_TABLE_CELL)],
        [Paragraph("Premium", S_TABLE_CELL_BOLD),
         Paragraph("250,000+", S_TABLE_CELL),
         Paragraph("Full smart lock with remote management, audit trails, Tuya/SmartLife API integration, time-bound codes", S_TABLE_CELL)],
    ]
    price_table = Table(price_data, colWidths=[AVAIL_W * 0.15, AVAIL_W * 0.22, AVAIL_W * 0.63])
    price_table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), TABLE_HEADER_BG),
        ("TEXTCOLOR", (0, 0), (-1, 0), WHITE),
        ("BACKGROUND", (0, 2), (-1, 2), TABLE_ALT_ROW),
        ("FONTNAME", (0, 0), (-1, -1), "Lexend"),
        ("FONTSIZE", (0, 0), (-1, -1), 8.5),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("TOPPADDING", (0, 0), (-1, -1), 7),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
        ("LEFTPADDING", (0, 0), (-1, -1), 6),
        ("GRID", (0, 0), (-1, -1), 0.5, BORDER_COLOR),
    ]))
    story.append(price_table)

    story.append(Spacer(1, 4 * mm))

    # Recommendation callout
    rec_para = Paragraph(
        '<font face="Lexend-SemiBold" color="#0f3460">Our recommendation for starting out:</font> '
        'A mid-range keypad lock (NGN 100,000\u2013150,000) gives you the best balance of reliability, '
        'features, and price. If you want full automation with time-bound codes and remote management, '
        'look at premium locks with Tuya/SmartLife compatibility.',
        make_style("rec", fontSize=9, leading=13, textColor=MEDIUM_TEXT, spaceAfter=0))
    rec_box = Table([[rec_para]], colWidths=[AVAIL_W - 20])
    rec_box.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), BLUE_LIGHT),
        ("TOPPADDING", (0, 0), (-1, -1), 8),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
        ("LEFTPADDING", (0, 0), (-1, -1), 10),
        ("RIGHTPADDING", (0, 0), (-1, -1), 10),
    ]))
    story.append(rec_box)

    story.append(PageBreak())

    # =====================================================
    # PAGE 4: HOW TIME-BOUND ACCESS CODES WORK
    # =====================================================

    story.append(Paragraph("HOW TIME-BOUND ACCESS CODES WORK", S_H1))
    story.append(hr())

    story.append(Paragraph(
        "This is the concept that changes everything. Instead of a physical key or a permanent code, "
        "each guest gets a unique, temporary access code that only works during their stay.",
        S_BODY))

    story.append(Spacer(1, 3 * mm))
    story.append(Paragraph("Here\u2019s how it works:", S_H2))
    story.append(Spacer(1, 2 * mm))

    code_steps = [
        ("One unique code per guest, per stay.",
         "Guest A gets code 482916. Guest B (arriving the same week in a different room) gets code "
         "739241. No shared codes, no master keys floating around."),
        ("Code activates at check-in time.",
         "If check-in is 2 PM on Monday, the code starts working at 2 PM on Monday. Not before. "
         "The guest can\u2019t show up early while your cleaning team is still working."),
        ("Code expires at checkout.",
         "If checkout is 12 PM on Wednesday, the code stops working at 12 PM on Wednesday. "
         "The guest can\u2019t come back a week later with the same code."),
        ("Guest receives code before arrival.",
         "The code is sent via WhatsApp or SMS 24 hours before check-in, along with: the exact "
         "address, a Google Maps pin, room number, entry instructions, and an emergency contact."),
        ("They arrive at any hour and walk in.",
         "No waiting for staff. No phone calls. No key handover. They could arrive at 3 AM and "
         "the experience is exactly the same as arriving at 3 PM."),
        ("Codes cannot be reused after checkout.",
         "Once the stay ends, that code is dead. Even if the guest wrote it down or shared it "
         "with someone, it won\u2019t open the door."),
    ]
    for i, (title, body) in enumerate(code_steps, 1):
        story.append(step_row(i, ACCENT_BLUE, title, body))
        story.append(Spacer(1, 2 * mm))

    story.append(Spacer(1, 4 * mm))

    # Why this matters callout
    why_items = [
        "<b>Eliminates late-night check-in problems entirely.</b> There\u2019s no such thing as a \u201Clate arrival\u201D anymore.",
        "<b>Eliminates key loss and replacement costs.</b> There is no physical object to lose.",
        "<b>Eliminates security risks from unreturned keys.</b> Codes expire automatically.",
        "<b>Creates a premium guest experience.</b> Guests feel like they\u2019re staying somewhere modern and well-managed.",
    ]
    why_title = Paragraph(
        '<font face="Lexend-SemiBold" color="#27ae60">Why this matters:</font>',
        make_style("why_h", fontSize=10, leading=14, textColor=GREEN, spaceAfter=4))
    why_bullets = []
    for item in why_items:
        why_bullets.append(Paragraph(
            f"\u2022  {item}",
            make_style(f"why_{item[:8]}", fontSize=9, leading=13, textColor=MEDIUM_TEXT, leftIndent=10, spaceAfter=2)))

    why_box = callout_box([why_title] + why_bullets, GREEN_LIGHT)
    story.append(why_box)

    story.append(PageBreak())

    # =====================================================
    # PAGE 5: THE FREE FIX -- DO THIS TODAY
    # =====================================================

    story.append(Paragraph("THE FREE FIX \u2014 DO THIS TODAY", S_H1))
    story.append(hr())

    story.append(Paragraph(
        "You don\u2019t need software or a big budget to start solving the key handover problem. "
        "Here\u2019s a step-by-step process you can implement this week for a single unit.",
        S_BODY))

    story.append(Spacer(1, 3 * mm))

    # Step 1
    free_steps = [
        ("Buy a keypad smart lock for your busiest unit.",
         "Budget: NGN 60,000\u2013100,000. Look for a battery-powered keypad lock from a reputable brand. "
         "Install it on the unit that gets the most late arrivals or the most key-related complaints. "
         "This is your test unit."),
        ("For each booking, generate a random 6-digit code.",
         "Before the guest arrives, programme a new code on the lock (or via the app). "
         "Use random 6-digit numbers \u2014 don\u2019t use easy patterns like 123456 or 000000."),
        ("WhatsApp the code to the guest 24 hours before check-in.",
         "Send: the access code, room number, full address, Google Maps pin, check-in/checkout times, "
         "and a contact number for emergencies. One message. Everything the guest needs."),
        ("After checkout, change the code immediately.",
         "Don\u2019t wait. As soon as the guest checks out, delete their code and either set a new temporary "
         "code or leave it blank until the next booking."),
        ("Keep a simple log.",
         "Track every code you issue: Guest Name | Room | Code | Check-in Date | Checkout Date | "
         "Code Changed. A notebook or spreadsheet is fine."),
    ]

    # Blue callout box for free fix steps
    step_elements = [
        Paragraph(
            '\U0001F527  <font face="Lexend-SemiBold" color="#0f3460">Your free step-by-step fix:</font>',
            make_style("free_h", fontSize=10, leading=14, textColor=ACCENT_BLUE, spaceAfter=6)),
    ]
    for i, (title, body) in enumerate(free_steps, 1):
        step_elements.append(step_row(i, ACCENT_BLUE, title, body))
        step_elements.append(Spacer(1, 2 * mm))

    free_box = callout_box(step_elements, BLUE_LIGHT)
    story.append(free_box)

    story.append(Spacer(1, 4 * mm))

    # Sample WhatsApp message
    story.append(Paragraph("Sample WhatsApp message to send:", S_H3))
    msg_text = (
        '<font face="Lexend" size="8" color="#333333">'
        '<i>Hi [Guest Name], welcome to [Property Name]! Your room is ready for you.</i><br/><br/>'
        '<i><b>Your access code:</b> 482916</i><br/>'
        '<i><b>Room:</b> [Room Number]</i><br/>'
        '<i><b>Address:</b> [Full address]</i><br/>'
        '<i><b>Google Maps:</b> [Pin link]</i><br/>'
        '<i><b>Check-in from:</b> [Time]  |  <b>Checkout by:</b> [Time]</i><br/><br/>'
        '<i>When you arrive, enter the code on the keypad and turn the handle. That\u2019s it!</i><br/>'
        '<i>If you need anything, call/WhatsApp [Contact Number].</i></font>'
    )
    msg_para = Paragraph(msg_text,
        make_style("msg", fontSize=8, leading=11.5, textColor=MEDIUM_TEXT, spaceAfter=0))
    msg_box = Table([[msg_para]], colWidths=[AVAIL_W - 30])
    msg_box.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), HexColor("#f0f0f0")),
        ("TOPPADDING", (0, 0), (-1, -1), 8),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
        ("LEFTPADDING", (0, 0), (-1, -1), 12),
        ("RIGHTPADDING", (0, 0), (-1, -1), 12),
        ("BOX", (0, 0), (-1, -1), 0.5, BORDER_COLOR),
    ]))
    msg_box.hAlign = "CENTER"
    story.append(msg_box)

    story.append(Spacer(1, 5 * mm))

    # Honest note callout (yellow/orange)
    honest_para = Paragraph(
        '<font face="Lexend-SemiBold" color="#b7791f">An honest note:</font><br/><br/>'
        '<font face="Lexend" color="#333333">'
        '<b>This works great for 1\u20133 rooms.</b> You can manage codes manually, send WhatsApp '
        'messages personally, and change codes after each checkout without too much hassle.<br/><br/>'
        '<b>Beyond 3 rooms, it gets messy fast.</b> When you have 5, 10, or 20 rooms with overlapping '
        'stays, back-to-back bookings, and guests arriving at different times, manually generating, '
        'sending, tracking, and changing codes across all rooms becomes a full-time job. You\u2019ll '
        'forget to change a code. You\u2019ll send the wrong code to the wrong guest.<br/><br/>'
        'That\u2019s not a failure of effort \u2014 it\u2019s a limitation of manual processes. '
        'And it\u2019s exactly where automation becomes necessary.</font>',
        make_style("honest", fontSize=9, leading=13, textColor=MEDIUM_TEXT, spaceAfter=0))
    honest_box = Table([[honest_para]], colWidths=[AVAIL_W - 20])
    honest_box.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), YELLOW_LIGHT),
        ("TOPPADDING", (0, 0), (-1, -1), 10),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 10),
        ("LEFTPADDING", (0, 0), (-1, -1), 12),
        ("RIGHTPADDING", (0, 0), (-1, -1), 12),
        ("BOX", (0, 0), (-1, -1), 1, ORANGE_ACCENT),
    ]))
    story.append(honest_box)

    story.append(PageBreak())

    # =====================================================
    # PAGE 6: THE AUTOMATED FIX
    # =====================================================

    story.append(Paragraph("THE AUTOMATED FIX \u2014 WHAT FULL AUTOMATION LOOKS LIKE", S_H1))
    story.append(hr())

    story.append(Paragraph(
        "Here\u2019s what happens when the entire process is handled by a system instead of a person:",
        S_BODY))

    story.append(Spacer(1, 3 * mm))

    # Green callout box for automated steps
    auto_items_data = [
        ("Booking confirmed \u2192 code generated automatically.",
         "The system generates a unique time-bound access code for that specific guest, room, and "
         "date range. No human action required."),
        ("Code sent to guest automatically.",
         "The guest receives their access code via WhatsApp/SMS with complete check-in instructions "
         "\u2014 address, Google Maps pin, room details, entry instructions. This happens the moment "
         "payment is confirmed."),
        ("Code only works during the stay.",
         "The code activates at check-in time and deactivates at checkout time. No early access, "
         "no lingering access after departure."),
        ("Code auto-expires at checkout.",
         "No manual reset needed. The code simply stops working. The next guest gets a completely "
         "different code."),
        ("Works across all rooms simultaneously.",
         "Whether you have 3 rooms or 30, the system manages every code for every room for every "
         "overlapping stay. No spreadsheets. No forgetting. No conflicts."),
        ("Full audit trail.",
         "The system logs who accessed which room and when. If there\u2019s ever a dispute or a security "
         "question, you have a complete digital record."),
        ("Tied to payment.",
         "The access code is only generated and sent after payment is confirmed. No payment, no code, "
         "no access. This eliminates the \u201Cthey said they\u2019d transfer\u201D problem entirely."),
    ]

    auto_elements = [
        Paragraph(
            '\u2705  <font face="Lexend-SemiBold" color="#27ae60">The automated workflow:</font>',
            make_style("auto_h", fontSize=10, leading=14, textColor=GREEN, spaceAfter=6)),
    ]
    for i, (title, body) in enumerate(auto_items_data, 1):
        auto_elements.append(step_row(i, GREEN, title, body))
        auto_elements.append(Spacer(1, 2 * mm))

    auto_box = callout_box(auto_elements, GREEN_LIGHT)
    story.append(auto_box)

    story.append(Spacer(1, 5 * mm))

    # Spacer callout
    spacer_para = Paragraph(
        '<font face="Lexend-SemiBold" color="#0f3460" size="10">'
        'This is what Spacer does for properties across Abuja and Kaduna.</font><br/><br/>'
        '<font face="Lexend" color="#333333" size="9">'
        'Managing 500+ bookings monthly. Smart lock automation built directly into the booking and '
        'payment flow, using Tuya/SmartLife-compatible smart locks. Codes are generated, sent, '
        'activated, and expired automatically. Property operators log in to a dashboard and see '
        'everything: bookings, payments, access logs, occupancy \u2014 without touching a single '
        'WhatsApp message.</font>',
        make_style("spacer_cta", fontSize=9, leading=13, textColor=MEDIUM_TEXT, spaceAfter=0))
    spacer_box = Table([[spacer_para]], colWidths=[AVAIL_W - 20])
    spacer_box.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), ACCENT_BLUE),
        ("TOPPADDING", (0, 0), (-1, -1), 12),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 12),
        ("LEFTPADDING", (0, 0), (-1, -1), 14),
        ("RIGHTPADDING", (0, 0), (-1, -1), 14),
    ]))

    # Override the colors for the box text to white
    spacer_para_white = Paragraph(
        '<font face="Lexend-SemiBold" color="#ffffff" size="10">'
        'This is what Spacer does for properties across Abuja and Kaduna.</font><br/><br/>'
        '<font face="Lexend" color="#e0e0e0" size="9">'
        'Managing 500+ bookings monthly. Smart lock automation built directly into the booking and '
        'payment flow, using Tuya/SmartLife-compatible smart locks. Codes are generated, sent, '
        'activated, and expired automatically. Property operators log in to a dashboard and see '
        'everything: bookings, payments, access logs, occupancy \u2014 without touching a single '
        'WhatsApp message.</font>',
        make_style("spacer_cta2", fontSize=9, leading=13, textColor=WHITE, spaceAfter=0))
    spacer_box2 = Table([[spacer_para_white]], colWidths=[AVAIL_W - 20])
    spacer_box2.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), ACCENT_BLUE),
        ("TOPPADDING", (0, 0), (-1, -1), 12),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 12),
        ("LEFTPADDING", (0, 0), (-1, -1), 14),
        ("RIGHTPADDING", (0, 0), (-1, -1), 14),
    ]))
    story.append(spacer_box2)

    story.append(PageBreak())

    # =====================================================
    # PAGE 7: SELF-ASSESSMENT + CTA
    # =====================================================

    story.append(Paragraph(
        "SELF-ASSESSMENT: HOW BAD IS YOUR KEY PROBLEM?",
        S_H1))
    story.append(hr())

    story.append(Paragraph(
        "Answer these five questions honestly. Count how many you answer \u201CYes\u201D to.",
        S_BODY))

    story.append(Spacer(1, 3 * mm))

    # Scorecard table
    score_data = [
        [Paragraph("<b>#</b>", S_TABLE_HEADER),
         Paragraph("<b>Statement</b>", S_TABLE_HEADER),
         Paragraph("<b>Yes / No</b>", S_TABLE_HEADER)],
        [Paragraph("1", S_TABLE_CELL_BOLD),
         Paragraph("A guest has had to wait more than 15 minutes at arrival in the last month", S_TABLE_CELL),
         Paragraph("", S_TABLE_CELL)],
        [Paragraph("2", S_TABLE_CELL_BOLD),
         Paragraph("We\u2019ve had a lost or unreturned key in the last 3 months", S_TABLE_CELL),
         Paragraph("", S_TABLE_CELL)],
        [Paragraph("3", S_TABLE_CELL_BOLD),
         Paragraph("We pay staff overtime or night shifts specifically for late check-ins", S_TABLE_CELL),
         Paragraph("", S_TABLE_CELL)],
        [Paragraph("4", S_TABLE_CELL_BOLD),
         Paragraph("A guest has mentioned check-in problems in a review", S_TABLE_CELL),
         Paragraph("", S_TABLE_CELL)],
        [Paragraph("5", S_TABLE_CELL_BOLD),
         Paragraph("I worry when a guest\u2019s flight lands after 10 PM", S_TABLE_CELL),
         Paragraph("", S_TABLE_CELL)],
    ]
    score_table = Table(score_data, colWidths=[AVAIL_W * 0.08, AVAIL_W * 0.74, AVAIL_W * 0.18])
    score_table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), TABLE_HEADER_BG),
        ("TEXTCOLOR", (0, 0), (-1, 0), WHITE),
        ("BACKGROUND", (0, 2), (-1, 2), TABLE_ALT_ROW),
        ("BACKGROUND", (0, 4), (-1, 4), TABLE_ALT_ROW),
        ("FONTNAME", (0, 0), (-1, -1), "Lexend"),
        ("FONTSIZE", (0, 0), (-1, -1), 8.5),
        ("ALIGN", (0, 0), (0, -1), "CENTER"),
        ("ALIGN", (2, 0), (2, -1), "CENTER"),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("TOPPADDING", (0, 0), (-1, -1), 7),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
        ("LEFTPADDING", (0, 0), (-1, -1), 8),
        ("GRID", (0, 0), (-1, -1), 0.5, BORDER_COLOR),
    ]))
    story.append(score_table)

    story.append(Spacer(1, 5 * mm))
    story.append(Paragraph("Your score:", S_H2))

    # Score interpretation boxes
    scores = [
        ("0\u20131", "#27ae60", GREEN_LIGHT,
         "Your check-in process is working reasonably well. Smart locks would still save you time "
         "and create a more premium guest experience, but you\u2019re not bleeding money from this area."),
        ("2\u20133", "#e67e22", ORANGE_LIGHT,
         "The key handover is actively costing you money and affecting guest satisfaction. "
         "A smart lock on your busiest unit would pay for itself within 1\u20132 months. "
         "Start with the free fix on Page 5."),
        ("4\u20135", "#c0392b", RED_LIGHT,
         "Physical keys are one of your biggest operational pain points. You\u2019re spending money "
         "on overtime, replacements, and losing revenue from bad reviews. This needs to be fixed "
         "\u2014 and the manual approach won\u2019t scale. You need automation."),
    ]
    for score_range, color, bg, interpretation in scores:
        score_para = Paragraph(
            f'<font face="Lexend-Bold" color="{color}">{score_range}:</font>  {interpretation}',
            make_style(f"si_{score_range[0]}", fontSize=9, leading=13, textColor=MEDIUM_TEXT, spaceAfter=0))
        score_box = Table([[score_para]], colWidths=[AVAIL_W - 16])
        score_box.setStyle(TableStyle([
            ("BACKGROUND", (0, 0), (-1, -1), bg),
            ("TOPPADDING", (0, 0), (-1, -1), 7),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
            ("LEFTPADDING", (0, 0), (-1, -1), 10),
            ("RIGHTPADDING", (0, 0), (-1, -1), 10),
        ]))
        story.append(score_box)
        story.append(Spacer(1, 2.5 * mm))

    story.append(Spacer(1, 5 * mm))
    story.append(hr())
    story.append(Spacer(1, 3 * mm))

    # --- CTA ---
    story.append(Paragraph(
        "FREE 15-MINUTE PROPERTY TECH AUDIT",
        make_style("cta_h", fontName="Lexend-Bold", fontSize=14, leading=18,
                    textColor=ACCENT_BLUE, alignment=TA_CENTER, spaceAfter=6)))

    # Scarcity
    scarcity_para = Paragraph(
        'We only do <b>10 of these per month</b> so we can give each property our full attention.',
        make_style("scarcity", fontName="Lexend-Medium", fontSize=9.5, leading=13,
                    textColor=DARK_TEXT, alignment=TA_CENTER, spaceAfter=4))
    scarcity_box = Table([[scarcity_para]], colWidths=[AVAIL_W * 0.7])
    scarcity_box.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), YELLOW_LIGHT),
        ("TOPPADDING", (0, 0), (-1, -1), 7),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
        ("LEFTPADDING", (0, 0), (-1, -1), 12),
        ("RIGHTPADDING", (0, 0), (-1, -1), 12),
    ]))
    scarcity_box.hAlign = "CENTER"
    story.append(scarcity_box)

    story.append(Spacer(1, 3 * mm))

    story.append(Paragraph(
        "In 15 minutes, we\u2019ll review your current check-in process, identify exactly where it\u2019s "
        "costing you, and show you what the fix looks like \u2014 whether you use Spacer or not.",
        S_BODY_CENTER))

    story.append(Paragraph(
        "No obligation. No pressure. Just a useful conversation.",
        make_style("cta_sub", fontName="Lexend-Medium", fontSize=9.5, leading=13,
                    textColor=LIGHT_TEXT, alignment=TA_CENTER, spaceAfter=6)))

    story.append(Spacer(1, 3 * mm))

    # Contact box
    cta_inner = Paragraph(
        '<font face="Lexend-Bold" size="10" color="#ffffff">Book your free audit:</font><br/><br/>'
        '<font face="Lexend" size="9.5" color="#ffffff">'
        'Call/WhatsApp: Yasmin Umar \u2014 +234 706 905 7925<br/>'
        'Email: yasmin@algolog.co</font>',
        make_style("cta_box", fontName="Lexend", fontSize=9.5, leading=14,
                    textColor=WHITE, alignment=TA_CENTER))
    cta_table = Table([[cta_inner]], colWidths=[AVAIL_W * 0.65])
    cta_table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), ACCENT_BLUE),
        ("ALIGN", (0, 0), (-1, -1), "CENTER"),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("TOPPADDING", (0, 0), (-1, -1), 14),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 14),
        ("LEFTPADDING", (0, 0), (-1, -1), 20),
        ("RIGHTPADDING", (0, 0), (-1, -1), 20),
    ]))
    cta_table.hAlign = "CENTER"
    story.append(cta_table)

    story.append(Spacer(1, 6 * mm))
    story.append(hr())
    story.append(Spacer(1, 2 * mm))

    # Footer blurb
    story.append(Paragraph(
        "This playbook was prepared by <b>Algolog Limited</b>, a Nigerian technology company that "
        "builds management systems for hospitality and workspace businesses. Our platform, "
        "<b>Spacer</b> (spacer.so), manages 500+ bookings monthly across properties "
        "in Abuja and Kaduna.",
        make_style("fblurb", fontName="Lexend", fontSize=8.5, leading=12,
                    textColor=LIGHT_TEXT, alignment=TA_CENTER, spaceAfter=4)))

    story.append(Paragraph(
        "5, Kwaji Close, Maitama, Abuja, Nigeria  |  algolog.co  |  spacer.so",
        S_SMALL))

    # Build
    doc.build(story, onFirstPage=add_footer, onLaterPages=add_footer)
    print(f"PDF generated: {OUTPUT_PATH}")
    print(f"File size: {os.path.getsize(OUTPUT_PATH):,} bytes")


if __name__ == "__main__":
    build_pdf()
