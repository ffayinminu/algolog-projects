"""
Generate Lead Magnet #1: "5 Revenue Leaks Every Serviced Apartment Has (And How to Plug Them Today)"
Format: Branded PDF — one leak per page with cost calculator, free fix, and automated fix
Aligned with Alex Hormozi's 7-step lead magnet framework
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
OUTPUT_PATH = os.path.join(BASE, "Proposals/Lead-Magnet-5-Revenue-Leaks.pdf")

LEAK_IMAGES = {
    1: os.path.join(BASE, "claude.ai contex/leak1_double_booking.png"),
    2: os.path.join(BASE, "claude.ai contex/leak2_payments.png"),
    3: os.path.join(BASE, "claude.ai contex/leak3_empty_rooms.png"),
    4: os.path.join(BASE, "claude.ai contex/leak4_staff_time.png"),
    5: os.path.join(BASE, "claude.ai contex/leak5_checkin.png"),
}

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

# --- Page Setup ---
PAGE_W, PAGE_H = A4
LEFT_MARGIN = 22 * mm
RIGHT_MARGIN = 22 * mm
TOP_MARGIN = 20 * mm
BOTTOM_MARGIN = 18 * mm

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
S_SMALL = make_style("S_SMALL", fontName="Lexend-Light", fontSize=7.5, leading=10, textColor=LIGHT_TEXT, alignment=TA_CENTER)
S_BULLET = make_style("S_BULLET", fontSize=9, leading=13, textColor=MEDIUM_TEXT, leftIndent=14, bulletIndent=4, spaceAfter=3)
S_TABLE_HEADER = make_style("S_TABLE_HEADER", fontName="Lexend-Bold", fontSize=8.5, leading=12, textColor=HexColor("#ffffff"))
S_TABLE_CELL = make_style("S_TABLE_CELL", fontSize=8.5, leading=12, textColor=MEDIUM_TEXT)
S_TABLE_CELL_BOLD = make_style("S_TABLE_CELL_BOLD", fontName="Lexend-Bold", fontSize=8.5, leading=12, textColor=DARK_TEXT)


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
        self.canv.setFillColor(HexColor("#ffffff"))
        self.canv.setFont("Lexend-Bold", 12)
        self.canv.drawCentredString(r + 2, r - 2, self.number)


def make_leak_image(img_path, target_h=35 * mm):
    """Create a centered image flowable scaled to a target height."""
    if not os.path.exists(img_path):
        return Spacer(1, 1)
    pil_img = PILImage.open(img_path)
    aspect = pil_img.size[0] / pil_img.size[1]
    img_h = target_h
    img_w = img_h * aspect
    img = Image(img_path, width=img_w, height=img_h)
    img.hAlign = "CENTER"
    return img


def make_callout_box(icon, label, text, bg_color, label_color):
    """Build a colored callout box with icon, bold label, and body text."""
    avail_w = PAGE_W - LEFT_MARGIN - RIGHT_MARGIN
    inner_w = avail_w - 24  # padding from outer container

    para = Paragraph(
        f'{icon}  <font face="Lexend-SemiBold" color="{label_color}">{label}</font>  {text}',
        make_style(f"cb_{label[:4]}", fontSize=8.5, leading=12.5, textColor=MEDIUM_TEXT, spaceAfter=0))
    box = Table([[para]], colWidths=[inner_w])
    box.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), bg_color),
        ("TOPPADDING", (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
        ("LEFTPADDING", (0, 0), (-1, -1), 9),
        ("RIGHTPADDING", (0, 0), (-1, -1), 9),
    ]))
    return box


def make_leak_page(story, number, title, description, cost_text, free_fix_text, auto_fix_text,
                   bg_color, badge_color, img_path):
    """Build a full leak page: image + title + description + 3 callout boxes."""
    avail_w = PAGE_W - LEFT_MARGIN - RIGHT_MARGIN
    inner_w = avail_w - 20

    # --- Image ---
    img_flowable = make_leak_image(img_path, target_h=35 * mm)

    # --- Title row: badge + title ---
    badge = NumberBadge(number, badge_color)
    title_para = Paragraph(
        f'<font face="Lexend-Bold" size="11" color="#1a1a1a">{title}</font>',
        make_style(f"lt_{number}", fontName="Lexend-Bold", fontSize=11, leading=15, textColor=DARK_TEXT)
    )
    title_table = Table(
        [[badge, title_para]],
        colWidths=[28, inner_w - 28]
    )
    title_table.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("LEFTPADDING", (0, 0), (0, 0), 0),
        ("LEFTPADDING", (1, 0), (1, 0), 6),
        ("TOPPADDING", (0, 0), (-1, -1), 0),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
    ]))

    # --- Description ---
    desc_para = Paragraph(description,
        make_style(f"ld_{number}", fontSize=9.5, leading=14, textColor=MEDIUM_TEXT, alignment=TA_JUSTIFY, spaceAfter=4))

    # --- Three callout boxes ---
    cost_box = make_callout_box("\U0001F4B0", "What it\u2019s costing you:", cost_text, YELLOW_LIGHT, "#b7791f")
    free_box = make_callout_box("\U0001F527", "Free fix \u2014 do this today:", free_fix_text, BLUE_LIGHT, "#0f3460")
    auto_box = make_callout_box("\u2705", "The automated fix:", auto_fix_text, GREEN_LIGHT, "#27ae60")

    # --- Assemble into shaded container ---
    rows = [
        [img_flowable],
        [Spacer(1, 2 * mm)],
        [title_table],
        [Spacer(1, 1.5 * mm)],
        [desc_para],
        [Spacer(1, 1 * mm)],
        [cost_box],
        [Spacer(1, 1.5 * mm)],
        [free_box],
        [Spacer(1, 1.5 * mm)],
        [auto_box],
    ]
    container = Table([[r[0]] for r in rows], colWidths=[inner_w])
    container.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), bg_color),
        ("TOPPADDING", (0, 0), (0, 0), 10),
        ("BOTTOMPADDING", (0, -1), (-1, -1), 10),
        ("LEFTPADDING", (0, 0), (-1, -1), 10),
        ("RIGHTPADDING", (0, 0), (-1, -1), 10),
        ("TOPPADDING", (0, 1), (-1, -2), 0),
        ("BOTTOMPADDING", (0, 0), (-1, -2), 0),
    ]))

    story.append(container)


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
    avail_w = PAGE_W - LEFT_MARGIN - RIGHT_MARGIN

    # =====================================================
    # PAGE 1: COVER
    # =====================================================

    # Banner
    if os.path.exists(BANNER_PATH):
        img = PILImage.open(BANNER_PATH)
        aspect = img.size[1] / img.size[0]
        display_w = avail_w
        display_h = display_w * aspect
        banner = Image(BANNER_PATH, width=display_w, height=display_h)
        story.append(banner)

    story.append(Spacer(1, 10 * mm))

    # Title
    story.append(Paragraph(
        "5 Revenue Leaks Every<br/>Serviced Apartment Has",
        make_style("title", fontName="Lexend-Bold", fontSize=24, leading=30, textColor=ACCENT_BLUE, alignment=TA_CENTER, spaceAfter=4)))
    story.append(Paragraph(
        "(And How to Plug Them Today)",
        make_style("sub", fontName="Lexend-Medium", fontSize=15, leading=20, textColor=ACCENT_BLUE, alignment=TA_CENTER, spaceAfter=4)))

    story.append(Spacer(1, 2 * mm))
    story.append(Paragraph(
        "A Self-Diagnostic Checklist for Hospitality Operators in Nigeria",
        make_style("sub2", fontName="Lexend-Light", fontSize=10, leading=14, textColor=LIGHT_TEXT, alignment=TA_CENTER, spaceAfter=6)))

    story.append(Spacer(1, 3 * mm))
    story.append(hr())
    story.append(Spacer(1, 4 * mm))

    story.append(Paragraph(
        "Most serviced apartment operators are losing money every month without realising it. "
        "Not to theft or bad luck \u2014 but to small, invisible inefficiencies that add up over time.",
        make_style("intro1", fontSize=10.5, leading=15, textColor=MEDIUM_TEXT, alignment=TA_CENTER, spaceAfter=8)))

    story.append(Paragraph(
        "For each leak below, we\u2019ve included:",
        make_style("intro2", fontName="Lexend-Medium", fontSize=10, leading=14, textColor=DARK_TEXT, alignment=TA_CENTER, spaceAfter=4)))

    how_to_items = [
        ("\U0001F4B0", "What it\u2019s costing you", "so you can calculate your own losses"),
        ("\U0001F527", "A free fix you can do today", "something you can implement right now"),
        ("\u2705", "The automated fix", "how to eliminate the leak permanently"),
    ]
    for emoji, bold_text, desc in how_to_items:
        story.append(Paragraph(
            f'{emoji}  <font face="Lexend-SemiBold">{bold_text}</font> \u2014 {desc}',
            make_style(f"how_{bold_text[:4]}", fontSize=9.5, leading=14, textColor=MEDIUM_TEXT, alignment=TA_CENTER, spaceAfter=4)))

    story.append(Spacer(1, 8 * mm))
    story.append(hr())
    story.append(Spacer(1, 3 * mm))

    # Quick summary list
    summary_items = [
        ("\U0001F6D1", "Double-bookings that cost you twice"),
        ("\U0001F4B8", "Payments that fall through the cracks"),
        ("\U0001F3E0", "Empty rooms you don\u2019t know about"),
        ("\u23F0", "Staff time wasted on manual tasks"),
        ("\U0001F511", "Check-in friction that kills reviews"),
    ]
    for i, (emoji, text) in enumerate(summary_items, 1):
        story.append(Paragraph(
            f'<font face="Lexend-Bold" color="#c0392b">{i}.</font>  {emoji}  {text}',
            make_style(f"sum_{i}", fontName="Lexend-Medium", fontSize=11, leading=16, textColor=DARK_TEXT, alignment=TA_CENTER, spaceAfter=5)))

    story.append(Spacer(1, 10 * mm))
    story.append(Paragraph(
        "A free checklist by Algolog Limited  |  spacer.so",
        make_style("tag", fontName="Lexend-Light", fontSize=9, leading=12, textColor=LIGHT_TEXT, alignment=TA_CENTER)))

    story.append(PageBreak())

    # =====================================================
    # PAGE 2: LEAK #1
    # =====================================================
    make_leak_page(story,
        number=1,
        title="Double-Bookings That Cost You Twice",
        description=(
            "When bookings are managed on WhatsApp, phone calls, or spreadsheets, it\u2019s only a "
            "matter of time before two guests are confirmed for the same room on the same dates. "
            "The result: one guest has to be relocated or refunded, and your reputation takes a hit."
        ),
        cost_text=(
            "[Your double-bookings per month] \u00d7 NGN 100,000 average cost per incident. "
            "Even one per month = <b>NGN 1.2 million per year.</b>"
        ),
        free_fix_text=(
            "Create a shared Google Sheet with one column per room and one row per date. "
            "Before confirming ANY booking \u2014 WhatsApp, phone, or walk-in \u2014 check the sheet first. "
            "Make it a rule: no confirmation goes out without checking. It\u2019s not perfect, but it catches "
            "80% of conflicts."
        ),
        auto_fix_text=(
            "A centralized booking system that blocks conflicting reservations automatically. "
            "No manual checking, no human error, no forgotten updates. Every booking is validated in real time."
        ),
        bg_color=RED_LIGHT,
        badge_color=RED_ACCENT,
        img_path=LEAK_IMAGES[1],
    )
    story.append(PageBreak())

    # =====================================================
    # PAGE 3: LEAK #2
    # =====================================================
    make_leak_page(story,
        number=2,
        title="Payments That Fall Through the Cracks",
        description=(
            "A guest confirms on WhatsApp. They say they\u2019ll transfer. Your staff forgets to follow up. "
            "The payment never arrives, but the room was held. Or worse \u2014 the guest pays cash, but the "
            "amount isn\u2019t recorded properly and gets lost in the daily shuffle."
        ),
        cost_text=(
            "[Unpaid or unreconciled bookings per month] \u00d7 average booking value. "
            "If just 3 bookings go unreconciled at NGN 40,000 each = <b>NGN 1.44 million per year.</b>"
        ),
        free_fix_text=(
            "New rule: no check-in without a payment confirmation screenshot sent to the team group chat. "
            "Assign one person to reconcile bank statements against bookings every morning. "
            "Track it: Booking | Guest | Expected Amount | Received | Status."
        ),
        auto_fix_text=(
            "Automated invoicing tied to every booking. Payment confirmation required before "
            "check-in is granted. Digital receipts for every transaction. Every naira accounted for automatically."
        ),
        bg_color=ORANGE_LIGHT,
        badge_color=ORANGE_ACCENT,
        img_path=LEAK_IMAGES[2],
    )
    story.append(PageBreak())

    # =====================================================
    # PAGE 4: LEAK #3
    # =====================================================
    make_leak_page(story,
        number=3,
        title="Empty Rooms You Don\u2019t Know About",
        description=(
            "If you don\u2019t have real-time occupancy data, you can\u2019t see which rooms are sitting empty "
            "and for how long. You can\u2019t fix what you can\u2019t see."
        ),
        cost_text=(
            "[Empty room-nights per month] \u00d7 your nightly rate. A room unbooked for just "
            "5 extra days at NGN 30,000/night = NGN 150,000 lost \u2014 per room. "
            "Across 10 rooms, that\u2019s <b>NGN 1.5 million per month.</b>"
        ),
        free_fix_text=(
            "At the end of every week, count how many room-nights went unbooked. Write it down. "
            "Just tracking this number will change how you think about availability. "
            "Then ask: could I have filled any of these with a weekend promo or a reduced midweek rate?"
        ),
        auto_fix_text=(
            "A live dashboard showing occupancy rates, availability gaps, and booking trends "
            "in real time \u2014 so you can adjust pricing or run targeted promotions to fill rooms "
            "before they sit empty."
        ),
        bg_color=BLUE_LIGHT,
        badge_color=ACCENT_BLUE,
        img_path=LEAK_IMAGES[3],
    )
    story.append(PageBreak())

    # =====================================================
    # PAGE 5: LEAK #4
    # =====================================================
    make_leak_page(story,
        number=4,
        title="Staff Time Wasted on Manual Tasks",
        description=(
            "Your receptionist spends hours every day answering WhatsApp messages about availability, "
            "sending payment details manually, coordinating check-in times, and handing over physical "
            "keys. That\u2019s hours that could be spent on guest experience, upselling, or operations."
        ),
        cost_text=(
            "If your staff spends 3 hours daily on tasks a system could handle, that\u2019s "
            "over <b>90 hours a month</b> of paid labour. At NGN 2,000/hour, that\u2019s "
            "NGN 180,000/month \u2014 not counting the revenue those hours could have generated."
        ),
        free_fix_text=(
            "Create a WhatsApp Broadcast List with a standard check-in message template. "
            "Include: bank account details, check-in time, address, and directions. "
            "Copy-paste instead of retyping every time. It saves 30 minutes a day minimum."
        ),
        auto_fix_text=(
            "Automated booking confirmations, payment links, and access codes sent directly "
            "to guests the moment they book. Staff checks a dashboard instead of managing "
            "15 WhatsApp conversations."
        ),
        bg_color=ORANGE_LIGHT,
        badge_color=ORANGE_ACCENT,
        img_path=LEAK_IMAGES[4],
    )
    story.append(PageBreak())

    # =====================================================
    # PAGE 6: LEAK #5
    # =====================================================
    make_leak_page(story,
        number=5,
        title="Check-In Friction That Kills Reviews and Referrals",
        description=(
            "A guest arrives at 11 PM after a long flight. No one is at reception. Or someone is there, "
            "but they can\u2019t find the right key. Or the guest has to wait 30 minutes while staff "
            "\u201Cconfirms\u201D the booking on WhatsApp. That first impression shapes everything \u2014 "
            "the review they leave, whether they come back, and whether they recommend you."
        ),
        cost_text=(
            "A bad check-in doesn\u2019t just lose one guest \u2014 it loses everyone that guest "
            "would have referred. One negative review can deter 10+ potential bookings. "
            "At NGN 50,000/booking, that\u2019s <b>NGN 500,000+ in invisible losses</b> from a single bad experience."
        ),
        free_fix_text=(
            "Send every confirmed guest a WhatsApp message 24 hours before check-in with: "
            "the exact address, a Google Maps pin, their room number, and the name/phone of "
            "whoever will hand them the key. Remove every point of confusion before they arrive."
        ),
        auto_fix_text=(
            "Smart lock access codes sent automatically after booking. The guest arrives, "
            "enters their code, and walks in. No keys, no waiting, no friction \u2014 even at 2 AM."
        ),
        bg_color=RED_LIGHT,
        badge_color=RED_ACCENT,
        img_path=LEAK_IMAGES[5],
    )

    story.append(PageBreak())

    # =====================================================
    # PAGE 7: SCORECARD + CTA
    # =====================================================

    # --- Self-Diagnostic Scorecard ---
    story.append(Paragraph(
        "\U0001F4CA  SCORE YOURSELF: HOW MANY LEAKS DO YOU HAVE?",
        make_style("score_h", fontName="Lexend-Bold", fontSize=13, leading=17, textColor=ACCENT_BLUE, alignment=TA_CENTER, spaceAfter=4)))

    story.append(Spacer(1, 2 * mm))
    story.append(Paragraph(
        "Count how many of these are true for your property:",
        make_style("score_sub", fontName="Lexend-Medium", fontSize=10, leading=14, textColor=MEDIUM_TEXT, alignment=TA_CENTER, spaceAfter=6)))

    story.append(Spacer(1, 3 * mm))

    # Scorecard table
    TABLE_HEADER_BG = HexColor("#1a1a2e")
    TABLE_ALT_ROW = HexColor("#f5f6fa")

    score_data = [
        [Paragraph("<b>#</b>", S_TABLE_HEADER),
         Paragraph("<b>Statement</b>", S_TABLE_HEADER),
         Paragraph("<b>\u2713 or \u2717</b>", S_TABLE_HEADER)],
        [Paragraph("1", S_TABLE_CELL_BOLD),
         Paragraph("We\u2019ve had at least one double-booking in the last 3 months", S_TABLE_CELL),
         Paragraph("", S_TABLE_CELL)],
        [Paragraph("2", S_TABLE_CELL_BOLD),
         Paragraph("We\u2019ve had payments go missing or unreconciled in the last month", S_TABLE_CELL),
         Paragraph("", S_TABLE_CELL)],
        [Paragraph("3", S_TABLE_CELL_BOLD),
         Paragraph("I don\u2019t know my exact occupancy rate for last month", S_TABLE_CELL),
         Paragraph("", S_TABLE_CELL)],
        [Paragraph("4", S_TABLE_CELL_BOLD),
         Paragraph("Staff spend more than 2 hours daily on WhatsApp for bookings", S_TABLE_CELL),
         Paragraph("", S_TABLE_CELL)],
        [Paragraph("5", S_TABLE_CELL_BOLD),
         Paragraph("A guest has complained about check-in in the last 3 months", S_TABLE_CELL),
         Paragraph("", S_TABLE_CELL)],
    ]
    score_table = Table(score_data, colWidths=[avail_w * 0.08, avail_w * 0.74, avail_w * 0.18])
    score_table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), TABLE_HEADER_BG),
        ("TEXTCOLOR", (0, 0), (-1, 0), HexColor("#ffffff")),
        ("FONTNAME", (0, 0), (-1, 0), "Lexend-Bold"),
        ("BACKGROUND", (0, 2), (-1, 2), TABLE_ALT_ROW),
        ("BACKGROUND", (0, 4), (-1, 4), TABLE_ALT_ROW),
        ("FONTNAME", (0, 1), (-1, -1), "Lexend"),
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

    # Score interpretation boxes
    scores = [
        ("0\u20131", "#27ae60", "You\u2019re in good shape. Small optimizations can still unlock significant revenue."),
        ("2\u20133", "#e67e22", "You\u2019re leaving serious money on the table. A few targeted fixes could recover NGN 500K\u20131M monthly."),
        ("4\u20135", "#c0392b", "These leaks are likely costing you NGN 1\u20133 million per month. The sooner you act, the more you recover."),
    ]
    for score_range, color, interpretation in scores:
        score_para = Paragraph(
            f'<font face="Lexend-Bold" color="{color}">{score_range}:</font>  {interpretation}',
            make_style(f"si_{score_range[0]}", fontSize=9, leading=13, textColor=MEDIUM_TEXT, spaceAfter=0))
        score_box = Table([[score_para]], colWidths=[avail_w - 16])
        score_box.setStyle(TableStyle([
            ("BACKGROUND", (0, 0), (-1, -1), HexColor("#fafafa")),
            ("TOPPADDING", (0, 0), (-1, -1), 6),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
            ("LEFTPADDING", (0, 0), (-1, -1), 10),
            ("RIGHTPADDING", (0, 0), (-1, -1), 10),
        ]))
        story.append(score_box)
        story.append(Spacer(1, 2 * mm))

    story.append(Spacer(1, 4 * mm))
    story.append(hr())
    story.append(Spacer(1, 3 * mm))

    # --- CTA ---
    story.append(Paragraph(
        "\U0001F4DE  WANT HELP PLUGGING THESE LEAKS?",
        make_style("cta_h", fontName="Lexend-Bold", fontSize=13, leading=17, textColor=ACCENT_BLUE, alignment=TA_CENTER, spaceAfter=6)))

    story.append(Paragraph(
        "We offer a <b>free 15-minute Property Tech Audit</b> \u2014 a quick, focused conversation where "
        "we review how your property currently operates and identify exactly which leaks are "
        "costing you the most.",
        S_BODY_CENTER))

    # Scarcity line
    scarcity_para = Paragraph(
        "We only do <b>10 of these per month</b>, so we can give each property our full attention.",
        make_style("scarcity", fontName="Lexend-Medium", fontSize=9.5, leading=13, textColor=DARK_TEXT, alignment=TA_CENTER, spaceAfter=4))
    scarcity_box = Table([[scarcity_para]], colWidths=[avail_w * 0.7])
    scarcity_box.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), YELLOW_LIGHT),
        ("TOPPADDING", (0, 0), (-1, -1), 7),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
        ("LEFTPADDING", (0, 0), (-1, -1), 12),
        ("RIGHTPADDING", (0, 0), (-1, -1), 12),
    ]))
    scarcity_box.hAlign = "CENTER"
    story.append(scarcity_box)

    story.append(Spacer(1, 2 * mm))
    story.append(Paragraph(
        "No obligation. No pressure. Just a useful conversation.",
        make_style("cta_sub", fontName="Lexend-Medium", fontSize=9.5, leading=13, textColor=LIGHT_TEXT, alignment=TA_CENTER, spaceAfter=6)))

    story.append(Spacer(1, 3 * mm))

    # Contact box
    cta_inner = Paragraph(
        '<font face="Lexend-Bold" size="10" color="#ffffff">Book your free audit:</font><br/><br/>'
        '<font face="Lexend" size="9.5" color="#ffffff">'
        'Call/WhatsApp: Yasmin Umar \u2014 +234 706 905 7925<br/>'
        'Email: yasmin@algolog.co</font>',
        make_style("cta_box", fontName="Lexend", fontSize=9.5, leading=14, textColor=HexColor("#ffffff"), alignment=TA_CENTER))
    cta_table = Table([[cta_inner]], colWidths=[avail_w * 0.65])
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
        "This checklist was prepared by <b>Algolog Limited</b>, a Nigerian technology company that "
        "builds management systems for hospitality and workspace businesses. Our platform, "
        "<b>Spacer</b> (spacer.so), is currently managing 500+ bookings monthly across properties "
        "in Abuja and Kaduna.",
        make_style("fblurb", fontName="Lexend", fontSize=8.5, leading=12, textColor=LIGHT_TEXT, alignment=TA_CENTER, spaceAfter=4)))

    story.append(Paragraph(
        "5, Kwaji Close, Maitama, Abuja, Nigeria  |  algolog.co  |  spacer.so",
        S_SMALL))

    # Build
    doc.build(story, onFirstPage=add_footer, onLaterPages=add_footer)
    print(f"PDF generated: {OUTPUT_PATH}")
    print(f"File size: {os.path.getsize(OUTPUT_PATH):,} bytes")


if __name__ == "__main__":
    build_pdf()
