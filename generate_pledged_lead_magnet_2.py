"""
Generate Pledged Lead Magnet #2: "Where Did the Offering Go?"
Subtitle: "A Cash Transparency Checklist for Church Finance Teams"
Format: Branded PDF -- multi-page checklist with callout boxes, numbered steps, and self-assessment
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
OUTPUT_PATH = os.path.join(BASE, "Proposals/Lead-Magnet-Pledged-Cash-Transparency.pdf")

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
        f"Algolog Limited  |  algolog.co  |  autogiving.ng  |  Page {doc.page}"
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


def point_row(number, color, title_text, body_text):
    """Build a numbered leak point with a badge and description."""
    badge = NumberBadge(number, color)
    inner_w = AVAIL_W - 50
    combined = Paragraph(
        f'<font face="Lexend-SemiBold" color="#1a1a1a">{title_text}</font><br/>'
        f'<font face="Lexend" color="#333333">{body_text}</font>',
        make_style(f"point_{number}", fontSize=9, leading=13, textColor=MEDIUM_TEXT, spaceAfter=2)
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
        "Where Did the Offering Go?",
        make_style("cover_title", fontName="Lexend-Bold", fontSize=28, leading=34,
                    textColor=ACCENT_BLUE, alignment=TA_CENTER, spaceAfter=4)))

    story.append(Spacer(1, 2 * mm))

    story.append(Paragraph(
        "A Cash Transparency Checklist for<br/>Church Finance Teams",
        make_style("cover_sub", fontName="Lexend-Medium", fontSize=14, leading=19,
                    textColor=MEDIUM_TEXT, alignment=TA_CENTER, spaceAfter=6)))

    story.append(Spacer(1, 10 * mm))
    story.append(hr())
    story.append(Spacer(1, 6 * mm))

    # Hook
    story.append(Paragraph(
        "Your offering was counted by 3 people. Can you verify the total?",
        make_style("cover_hook", fontName="Lexend-SemiBold", fontSize=11, leading=15,
                    textColor=DARK_TEXT, alignment=TA_CENTER, spaceAfter=8)))

    story.append(Spacer(1, 6 * mm))

    # What's inside
    story.append(Paragraph(
        "What\u2019s inside:",
        make_style("cover_inside_h", fontName="Lexend-SemiBold", fontSize=11, leading=15,
                    textColor=DARK_TEXT, alignment=TA_CENTER, spaceAfter=6)))

    inside_items = [
        "The 5 points where cash offerings are most vulnerable to error",
        "Why transparency protects volunteers and builds trust",
        "A free, step-by-step cash handling process you can implement this week",
        "A printable count sheet template for your finance team",
        "What digital giving solves that cash fundamentally cannot",
        "A self-assessment checklist for your church",
    ]
    for item in inside_items:
        story.append(Paragraph(
            f'\u2022  {item}',
            make_style(f"ci_{item[:6]}", fontSize=9.5, leading=14, textColor=MEDIUM_TEXT,
                        alignment=TA_CENTER, spaceAfter=3)))

    story.append(Spacer(1, 12 * mm))

    story.append(Paragraph(
        "A free checklist for church leaders by Algolog Limited  |  autogiving.ng",
        make_style("cover_tag", fontName="Lexend-Light", fontSize=9, leading=12,
                    textColor=LIGHT_TEXT, alignment=TA_CENTER)))

    story.append(PageBreak())

    # =====================================================
    # PAGE 2: THE 5 POINTS WHERE CASH OFFERINGS CAN LEAK
    # =====================================================

    story.append(Paragraph("THE 5 POINTS WHERE CASH OFFERINGS CAN LEAK", S_H1))
    story.append(hr())

    story.append(Paragraph(
        "This is not about accusing anyone. The vast majority of church volunteers who handle "
        "offering are faithful, trustworthy people who serve with integrity. But good people make "
        "mistakes when there are no systems. And without proper processes, those mistakes are "
        "invisible \u2014 which means honest volunteers are exposed to suspicion they do not deserve.",
        S_BODY))

    story.append(Spacer(1, 3 * mm))

    # Five leak points with numbered badges
    leak_points = [
        ("Counting errors.",
         "Volunteers counting quickly after a long service. Fatigue, distraction, loose change "
         "that gets missed, notes that stick together. Even a 2% error rate on a NGN 500,000 "
         "offering = NGN 10,000 per Sunday = NGN 520,000 per year in undetected counting errors."),
        ("Recording mistakes.",
         "The counted total is written on paper, sometimes transcribed to another sheet, sometimes "
         "entered into a phone. Each handoff from one format to another is a chance for error. "
         "A 5 becomes a 3. A zero gets dropped. And because the original cash has already been "
         "bundled, there is no easy way to go back and verify."),
        ("Delayed deposits.",
         "Cash sits in the church safe or someone\u2019s car for 1\u20133 days before deposit. No "
         "chain of custody. No way to verify the deposited amount matches the counted amount. "
         "Not because anyone took anything \u2014 but because there is no system to prove they did not."),
        ("No member receipts.",
         "Members give cash and have no record. They cannot track their own giving for personal "
         "accountability, tax purposes, or annual reviews. If a member asks \u201CHow much have I "
         "given this year?\u201D, the finance team has to dig through paper records \u2014 if those "
         "records even exist."),
        ("No category tracking.",
         "A member puts NGN 50,000 in the offering basket. Was it tithe? Offering? Building fund? "
         "With cash, it is all one lump sum. The church cannot report on giving by category. The "
         "member cannot confirm their giving was allocated where they intended."),
    ]

    for i, (title, body) in enumerate(leak_points, 1):
        story.append(point_row(i, ORANGE_ACCENT, title, body))
        story.append(Spacer(1, 2 * mm))

    story.append(Spacer(1, 4 * mm))

    # Yellow callout box
    callout_para = Paragraph(
        '<font face="Lexend-SemiBold" color="#b7791f">A note on framing:</font><br/><br/>'
        '<font face="Lexend" color="#333333">'
        'We are not suggesting anyone is stealing. We are saying: without systems, honest mistakes '
        'are invisible, good volunteers are exposed to suspicion, and the church has no way to '
        'verify what happened. Good systems protect everyone.</font>',
        make_style("callout_framing", fontSize=9, leading=13, textColor=MEDIUM_TEXT, spaceAfter=0))
    framing_box = Table([[callout_para]], colWidths=[AVAIL_W - 20])
    framing_box.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), YELLOW_LIGHT),
        ("TOPPADDING", (0, 0), (-1, -1), 10),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 10),
        ("LEFTPADDING", (0, 0), (-1, -1), 12),
        ("RIGHTPADDING", (0, 0), (-1, -1), 12),
        ("BOX", (0, 0), (-1, -1), 1, ORANGE_ACCENT),
    ]))
    story.append(framing_box)

    story.append(PageBreak())

    # =====================================================
    # PAGE 3: WHY THIS MATTERS MORE THAN YOU THINK
    # =====================================================

    story.append(Paragraph("WHY THIS MATTERS MORE THAN YOU THINK", S_H1))
    story.append(hr())

    # Trust points
    trust_points = [
        ("<b>Trust is the currency of ministry.</b>",
         "When a church member hears even a whisper of financial impropriety \u2014 whether founded "
         "or not \u2014 it damages everything. It affects attendance, giving, volunteer morale, and "
         "the pastor\u2019s authority. Financial trust takes years to build and moments to destroy."),
        ("<b>Transparency protects volunteers.</b>",
         "Counting teams should want a system that proves they handled every naira correctly. "
         "Without clear processes, the very people who serve faithfully are the ones most vulnerable "
         "to accusation. Good systems do not imply distrust \u2014 they provide protection."),
        ("<b>Accountability enables generosity.</b>",
         "When members know their giving is tracked, receipted, and properly allocated, they give "
         "with more confidence. Transparency does not reduce giving \u2014 it increases it, because "
         "people trust the process."),
        ("<b>Planning requires accuracy.</b>",
         "If your recorded totals are off by even 5%, your annual budget is built on wrong numbers. "
         "You are making staffing decisions, building plans, and outreach commitments based on "
         "figures that may not reflect reality."),
    ]

    for title, body in trust_points:
        story.append(Paragraph(title, S_H3))
        story.append(Paragraph(body, S_BODY))
        story.append(Spacer(1, 2 * mm))

    story.append(Spacer(1, 3 * mm))

    # The uncomfortable truth callout
    truth_para = Paragraph(
        '<font face="Lexend-SemiBold" color="#c0392b">The uncomfortable truth:</font><br/><br/>'
        '<font face="Lexend" color="#333333">'
        'Most churches have no way to answer the question \u201CIs the amount deposited exactly '
        'what was collected?\u201D with certainty. Not because of wrongdoing, but because the '
        'process was never designed to provide that answer.</font>',
        make_style("truth_callout", fontSize=9, leading=13, textColor=MEDIUM_TEXT, spaceAfter=0))
    truth_box = Table([[truth_para]], colWidths=[AVAIL_W - 20])
    truth_box.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), RED_LIGHT),
        ("TOPPADDING", (0, 0), (-1, -1), 10),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 10),
        ("LEFTPADDING", (0, 0), (-1, -1), 12),
        ("RIGHTPADDING", (0, 0), (-1, -1), 12),
        ("BOX", (0, 0), (-1, -1), 1, RED_ACCENT),
    ]))
    story.append(truth_box)

    story.append(PageBreak())

    # =====================================================
    # PAGE 4: THE FREE FIX -- A BETTER CASH HANDLING PROCESS
    # =====================================================

    story.append(Paragraph("THE FREE FIX \u2014 A BETTER CASH HANDLING PROCESS", S_H1))
    story.append(hr())

    story.append(Paragraph(
        "You do not need software to dramatically improve your cash handling transparency. "
        "Here is a step-by-step process you can implement this week:",
        S_BODY))

    story.append(Spacer(1, 3 * mm))

    # Steps in blue callout
    free_steps = [
        ("Always have at least 2 people count, independently.",
         "Two volunteers count the same offering separately. They do not communicate during "
         "counting. When both are done, they compare totals. If the totals do not match, they "
         "recount until they agree. This single step eliminates most counting errors."),
        ("Use a standardized count sheet.",
         "Every counting session should produce a completed form with: Date, Service, Counter 1 "
         "Name and Total, Counter 2 Name and Total, Final Agreed Total, Deposited By, Deposit "
         "Date, and Bank Confirmation. Print several copies and keep them in the counting room."),
        ("Photograph the completed count sheet after every service.",
         "Take a clear photo and store it in a dedicated WhatsApp group (Finance Committee only). "
         "This creates a timestamped digital backup that cannot be altered after the fact."),
        ("Deposit within 24 hours \u2014 no exceptions.",
         "Cash should reach the bank within 24 hours of being collected. Critical detail: the "
         "person who deposits should NOT be one of the counters. This is separation of duties "
         "\u2014 a basic financial control that protects everyone involved."),
        ("Bank confirmation same day.",
         "The person who deposits sends a photo of the deposit slip or mobile banking confirmation "
         "to the Finance Committee WhatsApp group on the same day. This creates a verifiable "
         "chain: count sheet total matches deposit confirmation."),
        ("Monthly reconciliation.",
         "At the end of every month, compare total count sheet amounts versus total bank deposits. "
         "They should match exactly. If they do not, investigate the discrepancy immediately."),
    ]

    step_elements = [
        Paragraph(
            '<font face="Lexend-SemiBold" color="#0f3460">Your free step-by-step fix:</font>',
            make_style("free_h", fontSize=10, leading=14, textColor=ACCENT_BLUE, spaceAfter=6)),
    ]
    for i, (title, body) in enumerate(free_steps, 1):
        step_elements.append(step_row(i, ACCENT_BLUE, title, body))
        step_elements.append(Spacer(1, 2 * mm))

    free_box = callout_box(step_elements, BLUE_LIGHT)
    story.append(free_box)

    story.append(Spacer(1, 4 * mm))

    # Count sheet template
    story.append(Paragraph("Printable Count Sheet Template:", S_H3))
    story.append(Spacer(1, 2 * mm))

    count_sheet_data = [
        [Paragraph("<b>Date</b>", S_TABLE_HEADER),
         Paragraph("<b>Service</b>", S_TABLE_HEADER),
         Paragraph("<b>Counter 1</b>", S_TABLE_HEADER),
         Paragraph("<b>C1 Total</b>", S_TABLE_HEADER),
         Paragraph("<b>Counter 2</b>", S_TABLE_HEADER),
         Paragraph("<b>C2 Total</b>", S_TABLE_HEADER),
         Paragraph("<b>Final Total</b>", S_TABLE_HEADER),
         Paragraph("<b>Deposited By</b>", S_TABLE_HEADER),
         Paragraph("<b>Deposit Date</b>", S_TABLE_HEADER),
         Paragraph("<b>Bank Confirm</b>", S_TABLE_HEADER)],
    ]
    # Add 4 blank rows
    for _ in range(4):
        count_sheet_data.append([Paragraph("", S_TABLE_CELL)] * 10)

    col_w = AVAIL_W / 10
    count_table = Table(count_sheet_data, colWidths=[col_w] * 10)
    count_table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), TABLE_HEADER_BG),
        ("TEXTCOLOR", (0, 0), (-1, 0), WHITE),
        ("BACKGROUND", (0, 2), (-1, 2), TABLE_ALT_ROW),
        ("BACKGROUND", (0, 4), (-1, 4), TABLE_ALT_ROW),
        ("FONTNAME", (0, 0), (-1, -1), "Lexend"),
        ("FONTSIZE", (0, 0), (-1, -1), 6.5),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("TOPPADDING", (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
        ("LEFTPADDING", (0, 0), (-1, -1), 3),
        ("RIGHTPADDING", (0, 0), (-1, -1), 3),
        ("GRID", (0, 0), (-1, -1), 0.5, BORDER_COLOR),
    ]))
    story.append(count_table)

    story.append(Spacer(1, 4 * mm))

    # Honest note callout (orange)
    honest_para = Paragraph(
        '<font face="Lexend-SemiBold" color="#e67e22">An honest note:</font><br/><br/>'
        '<font face="Lexend" color="#333333">'
        'This process dramatically improves cash transparency. But it still cannot solve: '
        'no member receipts, no category tracking, no digital audit trail, and it still depends '
        'on human consistency every single week. One missed step, one busy Sunday, and gaps appear.'
        '</font>',
        make_style("honest", fontSize=9, leading=13, textColor=MEDIUM_TEXT, spaceAfter=0))
    honest_box = Table([[honest_para]], colWidths=[AVAIL_W - 20])
    honest_box.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), ORANGE_LIGHT),
        ("TOPPADDING", (0, 0), (-1, -1), 10),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 10),
        ("LEFTPADDING", (0, 0), (-1, -1), 12),
        ("RIGHTPADDING", (0, 0), (-1, -1), 12),
        ("BOX", (0, 0), (-1, -1), 1, ORANGE_ACCENT),
    ]))
    story.append(honest_box)

    story.append(PageBreak())

    # =====================================================
    # PAGE 5: WHAT DIGITAL GIVING SOLVES THAT CASH CAN'T
    # =====================================================

    story.append(Paragraph("WHAT DIGITAL GIVING SOLVES THAT CASH CANNOT", S_H1))
    story.append(hr())

    story.append(Paragraph(
        "Even with perfect cash handling \u2014 two counters, standardized sheets, same-day "
        "deposits, monthly reconciliation \u2014 cash fundamentally cannot provide:",
        S_BODY))

    story.append(Spacer(1, 3 * mm))

    digital_solves = [
        ("Individual giving receipts for every member, automatically.",
         "No manual work, no paper trails to manage. Every giver gets a confirmation the moment "
         "their gift is processed. Members always know their giving was received and recorded."),
        ("Category-level tracking.",
         "How much went to tithes versus building fund versus missions? With digital giving, every "
         "naira is tagged to a specific category at the moment of giving. No guessing, no "
         "lumping everything together."),
        ("A searchable transaction history going back months or years.",
         "Need to know how much a member gave to the building fund between March and September? "
         "It takes 10 seconds, not 3 hours of digging through paper records."),
        ("The ability for members to give when they are not physically present.",
         "Travelling, sick, caring for family, working abroad \u2014 none of these stop a member "
         "from giving when the system is digital. Giving is no longer tied to attendance."),
        ("Recurring giving that happens without the member remembering each week.",
         "Set it once, it runs automatically. Weekly or monthly. Rain or shine. Present or absent. "
         "No forgotten intentions, no missed Sundays."),
        ("A dashboard where leadership can see giving trends and patterns.",
         "Real data for real planning. Total giving by week and month, category breakdowns, "
         "member giving history \u2014 not estimates based on memory."),
    ]

    for i, (title, body) in enumerate(digital_solves, 1):
        story.append(step_row(i, ACCENT_BLUE, title, body))
        story.append(Spacer(1, 2 * mm))

    story.append(Spacer(1, 5 * mm))

    # Bridge quote
    bridge_para = Paragraph(
        '<font face="Lexend-Medium" color="#0f3460" size="10">'
        'Cash served the church well for generations. But as churches grow and members '
        'expect transparency, the limitations of cash become the ceiling of trust.</font>',
        make_style("bridge", fontSize=10, leading=14, textColor=ACCENT_BLUE,
                    alignment=TA_CENTER, spaceAfter=0))
    bridge_box = Table([[bridge_para]], colWidths=[AVAIL_W - 30])
    bridge_box.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), BLUE_LIGHT),
        ("TOPPADDING", (0, 0), (-1, -1), 12),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 12),
        ("LEFTPADDING", (0, 0), (-1, -1), 16),
        ("RIGHTPADDING", (0, 0), (-1, -1), 16),
    ]))
    bridge_box.hAlign = "CENTER"
    story.append(bridge_box)

    story.append(PageBreak())

    # =====================================================
    # PAGE 6: THE AUTOMATED FIX -- WHAT FULL TRANSPARENCY LOOKS LIKE
    # =====================================================

    story.append(Paragraph("THE AUTOMATED FIX \u2014 WHAT FULL TRANSPARENCY LOOKS LIKE", S_H1))
    story.append(hr())

    story.append(Paragraph(
        "Here is what giving looks like when there is a proper system behind it:",
        S_BODY))

    story.append(Spacer(1, 3 * mm))

    # Green callout box for automated steps
    auto_items = [
        ("Your church gets a branded giving link: autogiving.ng/yourchurch",
         "No app to download. No complicated setup. Just a clean, branded page with your "
         "church name, logo, and colours. Members visit the link on their phone and give "
         "in under 60 seconds."),
        ("Every transaction is logged automatically.",
         "Amount, giver name, category, date, time \u2014 all recorded the moment a gift is "
         "processed. No manual entry, no paper records, no transcription errors."),
        ("Members choose their giving category.",
         "Tithes, Offerings, Building Fund, Missions, or any custom category your church creates. "
         "Every naira goes exactly where the giver intends. No more guessing at allocation."),
        ("Automatic receipts sent to every giver.",
         "Email and SMS after every transaction. No manual work for your finance team. Members "
         "have a complete record of their giving at all times."),
        ("Church admin dashboard shows everything.",
         "Total giving by week and month, giving by category, member giving history, exportable "
         "CSV reports. Everything your finance committee needs, in one place."),
        ("Funds settle directly into your church bank account.",
         "Never touches Algolog or any intermediary. Your money goes straight to your account, "
         "every time. Full separation \u2014 your funds are always yours."),
        ("Members set up recurring giving.",
         "It runs weekly or monthly, automatically. Whether they attend or not. Whether it rains "
         "or not. Whether they are in Abuja, Lagos, or London."),
        ("Full audit trail.",
         "Every naira is tracked from the moment it is given to the moment it lands in the church "
         "account. Every transaction has a timestamp, a giver name, a category, and a status."),
    ]

    auto_elements = [
        Paragraph(
            '<font face="Lexend-SemiBold" color="#27ae60">The automated workflow:</font>',
            make_style("auto_h", fontSize=10, leading=14, textColor=GREEN, spaceAfter=6)),
    ]
    for i, (title, body) in enumerate(auto_items, 1):
        auto_elements.append(step_row(i, GREEN, title, body))
        auto_elements.append(Spacer(1, 2 * mm))

    auto_box = callout_box(auto_elements, GREEN_LIGHT)
    story.append(auto_box)

    story.append(Spacer(1, 5 * mm))

    # Pledged summary callout (dark blue)
    pledged_para = Paragraph(
        '<font face="Lexend-SemiBold" color="#ffffff" size="10">'
        'No counting errors. No recording mistakes. No delayed deposits. No missing receipts. '
        'Just complete transparency, automatically.</font><br/><br/>'
        '<font face="Lexend" color="#e0e0e0" size="9">'
        'This is Pledged \u2014 autogiving.ng. Your members set it up once. Giving continues '
        'rain or shine, holiday or not. Every naira tracked, every giver receipted, every '
        'category accounted for.</font>',
        make_style("pledged_cta", fontSize=9, leading=13, textColor=WHITE, spaceAfter=0))
    pledged_box = Table([[pledged_para]], colWidths=[AVAIL_W - 20])
    pledged_box.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), ACCENT_BLUE),
        ("TOPPADDING", (0, 0), (-1, -1), 12),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 12),
        ("LEFTPADDING", (0, 0), (-1, -1), 14),
        ("RIGHTPADDING", (0, 0), (-1, -1), 14),
    ]))
    story.append(pledged_box)

    story.append(PageBreak())

    # =====================================================
    # PAGE 7: SELF-ASSESSMENT + CTA
    # =====================================================

    story.append(Paragraph(
        "SELF-ASSESSMENT: HOW TRANSPARENT IS YOUR CASH HANDLING?",
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
         Paragraph("Our offering is counted by volunteers without a standardized process", S_TABLE_CELL),
         Paragraph("", S_TABLE_CELL)],
        [Paragraph("2", S_TABLE_CELL_BOLD),
         Paragraph("Cash sometimes sits for more than 24 hours before being deposited", S_TABLE_CELL),
         Paragraph("", S_TABLE_CELL)],
        [Paragraph("3", S_TABLE_CELL_BOLD),
         Paragraph("We cannot provide individual giving receipts to members who ask", S_TABLE_CELL),
         Paragraph("", S_TABLE_CELL)],
        [Paragraph("4", S_TABLE_CELL_BOLD),
         Paragraph("We do not track giving by category (tithes vs offerings vs building fund)", S_TABLE_CELL),
         Paragraph("", S_TABLE_CELL)],
        [Paragraph("5", S_TABLE_CELL_BOLD),
         Paragraph("We have had at least one instance where count totals and bank deposits did not match", S_TABLE_CELL),
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
         "Your cash handling process is solid. You have good systems in place. Digital giving "
         "would still add convenience and transparency, but your foundation is strong."),
        ("2\u20133", "#e67e22", ORANGE_LIGHT,
         "There are meaningful gaps in your cash transparency. These gaps are not about trust "
         "\u2014 they are about systems. Addressing them now will protect your volunteers and "
         "build member confidence."),
        ("4\u20135", "#c0392b", RED_LIGHT,
         "Your cash handling process has significant vulnerabilities. Every week without a proper "
         "system is a week where errors can go undetected and good volunteers remain unprotected. "
         "This deserves your attention."),
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
        "FREE 15-MINUTE CHURCH GIVING AUDIT",
        make_style("cta_h", fontName="Lexend-Bold", fontSize=14, leading=18,
                    textColor=ACCENT_BLUE, alignment=TA_CENTER, spaceAfter=6)))

    # Scarcity
    scarcity_para = Paragraph(
        'We only do <b>10 of these per month</b> so we can give each church our full attention.',
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
        "In 15 minutes, we will look at your current giving process, identify the biggest "
        "transparency gaps, and show you exactly what a receipted, categorised, auditable "
        "giving system could look like for your church \u2014 branded with your name, logo, "
        "and colours.",
        S_BODY_CENTER))

    story.append(Paragraph(
        "No obligation. No pressure. Just a conversation about protecting your church "
        "and empowering your members to give with confidence.",
        make_style("cta_sub", fontName="Lexend-Medium", fontSize=9.5, leading=13,
                    textColor=LIGHT_TEXT, alignment=TA_CENTER, spaceAfter=6)))

    story.append(Spacer(1, 3 * mm))

    # Contact box
    cta_inner = Paragraph(
        '<font face="Lexend-Bold" size="10" color="#ffffff">Book your free audit:</font><br/><br/>'
        '<font face="Lexend" size="9.5" color="#ffffff">'
        'Call/WhatsApp: Yasmin Umar \u2014 +234 706 905 7925<br/>'
        'Email: yasmin@algolog.co<br/>'
        'Website: autogiving.ng</font>',
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
        "This checklist was prepared by <b>Algolog Limited</b>, a Nigerian technology company "
        "that builds platforms to help churches and organisations operate with transparency "
        "and efficiency. Our platform, <b>Pledged</b> (autogiving.ng), provides church-branded "
        "recurring giving with automatic receipting, category tracking, and full audit trails.",
        make_style("fblurb", fontName="Lexend", fontSize=8.5, leading=12,
                    textColor=LIGHT_TEXT, alignment=TA_CENTER, spaceAfter=4)))

    story.append(Paragraph(
        "5, Kwaji Close, Maitama, Abuja, Nigeria  |  algolog.co  |  autogiving.ng",
        S_SMALL))

    # Build
    doc.build(story, onFirstPage=add_footer, onLaterPages=add_footer)
    print(f"PDF generated: {OUTPUT_PATH}")
    print(f"File size: {os.path.getsize(OUTPUT_PATH):,} bytes")


if __name__ == "__main__":
    build_pdf()
