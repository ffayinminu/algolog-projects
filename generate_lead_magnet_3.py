"""
Generate Lead Magnet #3: "The Rooms You're Paying For But Not Selling"
Subtitle: "How to See (and Fill) Every Empty Night Across Your Property"
Format: Branded PDF — multi-page visibility guide with callout boxes, formulas, sample tracker, and self-assessment
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
OUTPUT_PATH = os.path.join(BASE, "Proposals/Lead-Magnet-Rooms-Not-Selling.pdf")

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
S_QUOTE = make_style("S_QUOTE", fontName="Lexend-Medium", fontSize=9.5, leading=14, textColor=ACCENT_BLUE, leftIndent=20, rightIndent=20, spaceAfter=4, alignment=TA_CENTER)


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
        make_style(f"step_{number}_{id(title_text)}", fontSize=9, leading=13, textColor=MEDIUM_TEXT, spaceAfter=2)
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
        "The Rooms You\u2019re Paying For<br/>But Not Selling",
        make_style("cover_title", fontName="Lexend-Bold", fontSize=26, leading=32,
                    textColor=ACCENT_BLUE, alignment=TA_CENTER, spaceAfter=4)))

    story.append(Spacer(1, 2 * mm))

    story.append(Paragraph(
        "How to See (and Fill) Every Empty Night<br/>Across Your Property",
        make_style("cover_sub", fontName="Lexend-Medium", fontSize=13, leading=18,
                    textColor=MEDIUM_TEXT, alignment=TA_CENTER, spaceAfter=6)))

    story.append(Spacer(1, 10 * mm))
    story.append(hr())
    story.append(Spacer(1, 6 * mm))

    # Intro blurb
    story.append(Paragraph(
        "Most serviced apartment operators think their occupancy is higher than it actually is. "
        "They remember the sold-out weekends and forget the empty weeknights. This guide gives you "
        "the exact formula to calculate your real occupancy rate, shows you the three biggest causes "
        "of invisible vacancy, and walks you through a free fix you can start today.",
        make_style("cover_intro", fontSize=10.5, leading=15, textColor=MEDIUM_TEXT,
                    alignment=TA_CENTER, spaceAfter=8)))

    story.append(Spacer(1, 6 * mm))

    # What's inside
    story.append(Paragraph(
        "What\u2019s inside:",
        make_style("cover_inside_h", fontName="Lexend-SemiBold", fontSize=11, leading=15,
                    textColor=DARK_TEXT, alignment=TA_CENTER, spaceAfter=6)))

    inside_items = [
        "Why most operators overestimate their occupancy",
        "The occupancy and RevPAR formulas (with worked examples)",
        "The 3 biggest causes of invisible vacancy",
        "A free weekly occupancy tracker you can start using today",
        "What real-time occupancy visibility looks like at scale",
        "A self-assessment scorecard for your property",
    ]
    for item in inside_items:
        story.append(Paragraph(
            f'\u2022  {item}',
            make_style(f"ci_{id(item)}", fontSize=9.5, leading=14, textColor=MEDIUM_TEXT,
                        alignment=TA_CENTER, spaceAfter=3)))

    story.append(Spacer(1, 12 * mm))

    story.append(Paragraph(
        "A free visibility guide by Algolog Limited  |  spacer.so",
        make_style("cover_tag", fontName="Lexend-Light", fontSize=9, leading=12,
                    textColor=LIGHT_TEXT, alignment=TA_CENTER)))

    story.append(PageBreak())

    # =====================================================
    # PAGE 2: THE OCCUPANCY BLIND SPOT
    # =====================================================

    story.append(Paragraph("THE OCCUPANCY BLIND SPOT", S_H1))
    story.append(hr())

    story.append(Paragraph(
        "Most serviced apartment operators think their occupancy is higher than it actually is. "
        "And it\u2019s not because they\u2019re bad at their job \u2014 it\u2019s because of how human memory works.",
        S_BODY))

    story.append(Paragraph(
        "You remember the busy weekends. You remember the sold-out Friday night, the back-to-back "
        "Saturday bookings, the WhatsApp messages flying in with enquiries. What you don\u2019t remember "
        "\u2014 or don\u2019t track \u2014 is the empty Tuesday. The vacant Wednesday. The room that sat "
        "unbooked for four consecutive weeknights while you were focused on the weekend rush.",
        S_BODY))

    story.append(Paragraph(
        "The reality is this: <b>most 10-unit serviced apartment properties in Nigeria operate at "
        "50\u201365% occupancy.</b> That means 35\u201350% of their room-nights generate zero revenue.",
        S_BODY))

    story.append(Spacer(1, 2 * mm))

    story.append(Paragraph(
        "Here\u2019s the part that makes this painful:",
        make_style("painful_h", fontName="Lexend-SemiBold", fontSize=10, leading=14,
                    textColor=DARK_TEXT, spaceAfter=4)))

    story.append(Paragraph(
        "You\u2019re paying rent, electricity, DSTV, cleaning, and security on every room, every day "
        "\u2014 whether a guest is in it or not. An empty room doesn\u2019t cost nothing. It costs "
        "everything except the revenue it was supposed to generate.",
        S_BODY))

    story.append(Spacer(1, 4 * mm))

    # Yellow callout — cost calculator
    cost_title = Paragraph(
        '<font face="Lexend-SemiBold" color="#b7791f">What it\u2019s costing you:</font>',
        make_style("cost_h", fontSize=10, leading=14, textColor=DARK_TEXT, spaceAfter=4))

    cost_formula = Paragraph(
        '<font face="Lexend-SemiBold" color="#1a1a1a">[Total rooms] \u00d7 [Empty nights per month] '
        '\u00d7 [Your nightly rate] = Revenue left on the table</font>',
        make_style("cost_formula", fontSize=9.5, leading=14, textColor=DARK_TEXT, alignment=TA_CENTER, spaceAfter=6))

    cost_example = Paragraph(
        '<font face="Lexend" color="#333333">'
        '<b>For a 10-unit property with 35% vacancy at NGN 30,000/night:</b><br/>'
        '\u2022  10 rooms \u00d7 30 days = 300 total room-nights<br/>'
        '\u2022  35% vacancy = 105 empty room-nights<br/>'
        '\u2022  105 \u00d7 NGN 30,000 = <b>NGN 3.15 million</b> in potential revenue sitting on the table every month</font>',
        make_style("cost_ex", fontSize=9, leading=13, textColor=MEDIUM_TEXT, spaceAfter=4))

    cost_note = Paragraph(
        '<font face="Lexend" color="#555555">'
        'This isn\u2019t a theoretical number. It\u2019s the gap between what your property could earn '
        'and what it actually earns. And the first step to closing that gap is knowing the gap exists.</font>',
        make_style("cost_note", fontSize=8.5, leading=12, textColor=LIGHT_TEXT, spaceAfter=0))

    cost_box = callout_box([cost_title, cost_formula, cost_example, Spacer(1, 1 * mm), cost_note], YELLOW_LIGHT, ORANGE_ACCENT)
    story.append(cost_box)

    story.append(PageBreak())

    # =====================================================
    # PAGE 3: KNOW YOUR REAL NUMBER — THE OCCUPANCY FORMULA
    # =====================================================

    story.append(Paragraph("KNOW YOUR REAL NUMBER \u2014 THE OCCUPANCY FORMULA", S_H1))
    story.append(hr())

    story.append(Paragraph(
        "Before you can fix your occupancy, you need to know your occupancy. Not a guess. Not a feeling. "
        "An actual number. Here are the two formulas every property operator should know.",
        S_BODY))

    story.append(Spacer(1, 3 * mm))

    # Formula 1: Occupancy Rate — blue callout
    f1_title = Paragraph(
        '<font face="Lexend-Bold" color="#0f3460">Formula 1: Occupancy Rate</font>',
        make_style("f1_h", fontSize=11, leading=15, textColor=ACCENT_BLUE, spaceAfter=6))

    f1_formula = Paragraph(
        '<font face="Lexend-Bold" color="#1a1a1a" size="11">'
        '(Total Booked Room-Nights \u00f7 Total Available Room-Nights) \u00d7 100 = Occupancy Rate</font>',
        make_style("f1_form", fontSize=11, leading=16, textColor=DARK_TEXT, alignment=TA_CENTER, spaceAfter=8))

    f1_example_h = Paragraph(
        '<font face="Lexend-SemiBold" color="#333333">Worked example \u2014 10-unit property, 30-day month:</font>',
        make_style("f1_ex_h", fontSize=9.5, leading=13, textColor=MEDIUM_TEXT, spaceAfter=4))

    f1_example = Paragraph(
        '<font face="Lexend" color="#333333">'
        '\u2022  Total available room-nights: 10 \u00d7 30 = <b>300</b><br/>'
        '\u2022  If 195 were booked: 195 \u00f7 300 = <b>65% occupancy</b><br/>'
        '\u2022  That means <b>105 room-nights earned nothing</b></font>',
        make_style("f1_ex", fontSize=9, leading=13, textColor=MEDIUM_TEXT, spaceAfter=0))

    f1_box = callout_box([f1_title, f1_formula, f1_example_h, f1_example], BLUE_LIGHT)
    story.append(f1_box)

    story.append(Spacer(1, 5 * mm))

    # Formula 2: RevPAR — green callout
    f2_title = Paragraph(
        '<font face="Lexend-Bold" color="#27ae60">Formula 2: RevPAR (Revenue Per Available Room)</font>',
        make_style("f2_h", fontSize=11, leading=15, textColor=GREEN, spaceAfter=6))

    f2_formula = Paragraph(
        '<font face="Lexend-Bold" color="#1a1a1a" size="11">'
        'Total Room Revenue \u00f7 Total Available Room-Nights = RevPAR</font>',
        make_style("f2_form", fontSize=11, leading=16, textColor=DARK_TEXT, alignment=TA_CENTER, spaceAfter=8))

    f2_example_h = Paragraph(
        '<font face="Lexend-SemiBold" color="#333333">Using the same example:</font>',
        make_style("f2_ex_h", fontSize=9.5, leading=13, textColor=MEDIUM_TEXT, spaceAfter=4))

    f2_example = Paragraph(
        '<font face="Lexend" color="#333333">'
        '\u2022  You earned NGN 5.85M from 195 booked nights<br/>'
        '\u2022  RevPAR = NGN 5,850,000 \u00f7 300 = <b>NGN 19,500</b><br/>'
        '\u2022  Your nightly rate is NGN 30,000 \u2014 but you\u2019re only making <b>NGN 19,500</b> per room per night '
        'when you account for the empty ones</font>',
        make_style("f2_ex", fontSize=9, leading=13, textColor=MEDIUM_TEXT, spaceAfter=0))

    f2_box = callout_box([f2_title, f2_formula, f2_example_h, f2_example], GREEN_LIGHT)
    story.append(f2_box)

    story.append(Spacer(1, 5 * mm))

    # Key insight quote
    insight_para = Paragraph(
        '\u201CRevPAR is the number that tells you the truth. Your nightly rate is what you charge. '
        'RevPAR is what you actually earn.\u201D',
        S_QUOTE)
    insight_box = Table([[insight_para]], colWidths=[AVAIL_W - 30])
    insight_box.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), HexColor("#f8f9fa")),
        ("TOPPADDING", (0, 0), (-1, -1), 10),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 10),
        ("LEFTPADDING", (0, 0), (-1, -1), 16),
        ("RIGHTPADDING", (0, 0), (-1, -1), 16),
        ("BOX", (0, 0), (-1, -1), 1.5, ACCENT_BLUE),
    ]))
    insight_box.hAlign = "CENTER"
    story.append(insight_box)

    story.append(Spacer(1, 4 * mm))

    story.append(Paragraph(
        "Most operators focus on their nightly rate and ignore RevPAR. But RevPAR is the number that "
        "determines whether your property is profitable or just busy on weekends.",
        S_BODY))

    story.append(PageBreak())

    # =====================================================
    # PAGE 4: THE 3 BIGGEST CAUSES OF INVISIBLE VACANCY
    # =====================================================

    story.append(Paragraph("THE 3 BIGGEST CAUSES OF INVISIBLE VACANCY", S_H1))
    story.append(hr())

    story.append(Paragraph(
        "If your occupancy is below 75%, it\u2019s not random bad luck. There are usually three "
        "structural causes \u2014 and most operators are dealing with at least two of them.",
        S_BODY))

    story.append(Spacer(1, 4 * mm))

    # Cause 1
    cause1_elements = [
        Paragraph(
            '<font face="Lexend-Bold" color="#c0392b" size="11">Cause 1: No Midweek Strategy</font>',
            make_style("c1_h", fontSize=11, leading=15, textColor=RED_ACCENT, spaceAfter=4)),
        Paragraph(
            "Weekends tend to fill themselves \u2014 especially in cities like Abuja and Kaduna where "
            "short-stay demand spikes Friday through Sunday. But Tuesday, Wednesday, and Thursday? "
            "Those nights consistently underperform.",
            make_style("c1_b1", fontSize=9, leading=13, textColor=MEDIUM_TEXT, spaceAfter=4)),
        Paragraph(
            "Most operators don\u2019t even track which days of the week are weakest. They accept that "
            "\u201Cmidweek is always slow\u201D without doing anything targeted about it. But \u201Cslow\u201D "
            "and \u201Cempty\u201D are different problems. Slow means low demand. Empty means no strategy "
            "to capture the demand that does exist.",
            make_style("c1_b2", fontSize=9, leading=13, textColor=MEDIUM_TEXT, spaceAfter=0)),
    ]
    story.append(callout_box(cause1_elements, RED_LIGHT, RED_ACCENT))

    story.append(Spacer(1, 4 * mm))

    # Cause 2
    cause2_elements = [
        Paragraph(
            '<font face="Lexend-Bold" color="#e67e22" size="11">Cause 2: No Gap-Fill Pricing</font>',
            make_style("c2_h", fontSize=11, leading=15, textColor=ORANGE_ACCENT, spaceAfter=4)),
        Paragraph(
            "A room sitting empty tonight at NGN 30,000 will earn NGN 0 tomorrow. A room sold tonight "
            "at NGN 20,000 earns NGN 20,000. The maths is straightforward.",
            make_style("c2_b1", fontSize=9, leading=13, textColor=MEDIUM_TEXT, spaceAfter=4)),
        Paragraph(
            "But many operators would rather leave a room empty than \u201Cdiscount\u201D it. There\u2019s "
            "a psychological resistance to lowering prices \u2014 it feels like devaluing the property. "
            "Here\u2019s the reality: <b>an empty room costs money</b> (rent, electricity, cleaning, security). "
            "<b>A discounted room makes money.</b> The real devaluation is leaving revenue on the table.",
            make_style("c2_b2", fontSize=9, leading=13, textColor=MEDIUM_TEXT, spaceAfter=0)),
    ]
    story.append(callout_box(cause2_elements, ORANGE_LIGHT, ORANGE_ACCENT))

    story.append(Spacer(1, 4 * mm))

    # Cause 3
    cause3_elements = [
        Paragraph(
            '<font face="Lexend-Bold" color="#0f3460" size="11">Cause 3: No Visibility Into Patterns</font>',
            make_style("c3_h", fontSize=11, leading=15, textColor=ACCENT_BLUE, spaceAfter=4)),
        Paragraph(
            "Without data, you can\u2019t see that Room 7 has been empty every Monday through Wednesday "
            "for the last 3 months. You can\u2019t see that your occupancy drops 40% the week after salary "
            "week. You can\u2019t see that your best-performing unit is carried by repeat guests while your "
            "worst-performing unit hasn\u2019t had a booking in 12 days.",
            make_style("c3_b1", fontSize=9, leading=13, textColor=MEDIUM_TEXT, spaceAfter=4)),
        Paragraph(
            "<b>You can\u2019t act on patterns you can\u2019t see.</b> And without a tracking system \u2014 "
            "even a simple one \u2014 these patterns remain invisible.",
            make_style("c3_b2", fontSize=9, leading=13, textColor=MEDIUM_TEXT, spaceAfter=0)),
    ]
    story.append(callout_box(cause3_elements, BLUE_LIGHT, ACCENT_BLUE))

    story.append(PageBreak())

    # =====================================================
    # PAGE 5: THE FREE FIX — DO THIS TODAY
    # =====================================================

    story.append(Paragraph("THE FREE FIX \u2014 DO THIS TODAY", S_H1))
    story.append(hr())

    story.append(Paragraph(
        "You don\u2019t need software to start understanding your occupancy. Here\u2019s a simple, "
        "manual tracking system you can set up today in a notebook, Google Sheet, or Excel spreadsheet.",
        S_BODY))

    story.append(Spacer(1, 3 * mm))

    # Blue callout — step-by-step tracker setup
    tracker_steps = [
        ("Create a simple weekly tracker.",
         "Columns: Week | Room 1 | Room 2 | ... | Room 10 | Total Booked | Total Available | Occupancy %. "
         "Mark each cell as booked or empty for each night of the week."),
        ("Fill it in every Friday afternoon.",
         "It takes 10 minutes. Look at your bookings for the week, mark which rooms were occupied each night, "
         "and calculate the totals."),
        ("After 4 weeks, calculate your real monthly occupancy.",
         "Not a guess, not a feeling \u2014 an actual number. Add up all booked nights, divide by total "
         "available nights, multiply by 100."),
        ("After 8 weeks, look for patterns.",
         "Which rooms consistently underperform? Which days of the week are weakest? Which weeks of the "
         "month dip? The patterns will be obvious once you have the data."),
    ]

    step_elements = [
        Paragraph(
            '<font face="Lexend-SemiBold" color="#0f3460">Your free step-by-step fix:</font>',
            make_style("free_h", fontSize=10, leading=14, textColor=ACCENT_BLUE, spaceAfter=6)),
    ]
    for i, (title, body) in enumerate(tracker_steps, 1):
        step_elements.append(step_row(i, ACCENT_BLUE, title, body))
        step_elements.append(Spacer(1, 2 * mm))

    free_box = callout_box(step_elements, BLUE_LIGHT)
    story.append(free_box)

    story.append(Spacer(1, 4 * mm))

    # Sample tracker table
    story.append(Paragraph("Sample weekly occupancy tracker:", S_H3))
    story.append(Spacer(1, 1 * mm))

    # Table header
    tracker_header_style = make_style("th_s", fontName="Lexend-Bold", fontSize=7, leading=10, textColor=WHITE)
    tracker_cell_style = make_style("tc_s", fontSize=7.5, leading=10, textColor=MEDIUM_TEXT, alignment=TA_CENTER)
    tracker_cell_bold = make_style("tcb_s", fontName="Lexend-Bold", fontSize=7.5, leading=10, textColor=DARK_TEXT, alignment=TA_CENTER)
    tracker_cell_left = make_style("tcl_s", fontName="Lexend-SemiBold", fontSize=7.5, leading=10, textColor=DARK_TEXT)

    col_w = AVAIL_W
    c0 = col_w * 0.14  # Room label
    cd = col_w * 0.08  # Day cols (7)
    cn = col_w * 0.09  # Booked
    ca = col_w * 0.09  # Available
    co = col_w * 0.12  # Occ%

    tracker_data = [
        [Paragraph("<b>Week of:</b>", tracker_header_style),
         Paragraph("<b>Mon</b>", tracker_header_style),
         Paragraph("<b>Tue</b>", tracker_header_style),
         Paragraph("<b>Wed</b>", tracker_header_style),
         Paragraph("<b>Thu</b>", tracker_header_style),
         Paragraph("<b>Fri</b>", tracker_header_style),
         Paragraph("<b>Sat</b>", tracker_header_style),
         Paragraph("<b>Sun</b>", tracker_header_style),
         Paragraph("<b>Booked</b>", tracker_header_style),
         Paragraph("<b>Avail</b>", tracker_header_style),
         Paragraph("<b>Occ %</b>", tracker_header_style)],
        [Paragraph("Room 1", tracker_cell_left),
         Paragraph("\u2014", tracker_cell_style),
         Paragraph("\u2014", tracker_cell_style),
         Paragraph("\u2014", tracker_cell_style),
         Paragraph("\u2713", tracker_cell_bold),
         Paragraph("\u2713", tracker_cell_bold),
         Paragraph("\u2713", tracker_cell_bold),
         Paragraph("\u2713", tracker_cell_bold),
         Paragraph("4", tracker_cell_bold),
         Paragraph("7", tracker_cell_style),
         Paragraph("57%", tracker_cell_bold)],
        [Paragraph("Room 2", tracker_cell_left),
         Paragraph("\u2713", tracker_cell_bold),
         Paragraph("\u2713", tracker_cell_bold),
         Paragraph("\u2014", tracker_cell_style),
         Paragraph("\u2014", tracker_cell_style),
         Paragraph("\u2713", tracker_cell_bold),
         Paragraph("\u2713", tracker_cell_bold),
         Paragraph("\u2713", tracker_cell_bold),
         Paragraph("5", tracker_cell_bold),
         Paragraph("7", tracker_cell_style),
         Paragraph("71%", tracker_cell_bold)],
        [Paragraph("Room 3", tracker_cell_left),
         Paragraph("\u2014", tracker_cell_style),
         Paragraph("\u2014", tracker_cell_style),
         Paragraph("\u2014", tracker_cell_style),
         Paragraph("\u2014", tracker_cell_style),
         Paragraph("\u2713", tracker_cell_bold),
         Paragraph("\u2713", tracker_cell_bold),
         Paragraph("\u2014", tracker_cell_style),
         Paragraph("2", tracker_cell_bold),
         Paragraph("7", tracker_cell_style),
         Paragraph("29%", tracker_cell_bold)],
        [Paragraph("TOTAL", tracker_cell_left),
         Paragraph("", tracker_cell_style),
         Paragraph("", tracker_cell_style),
         Paragraph("", tracker_cell_style),
         Paragraph("", tracker_cell_style),
         Paragraph("", tracker_cell_style),
         Paragraph("", tracker_cell_style),
         Paragraph("", tracker_cell_style),
         Paragraph("11", tracker_cell_bold),
         Paragraph("21", tracker_cell_style),
         Paragraph("52%", tracker_cell_bold)],
    ]
    tracker_table = Table(tracker_data,
                          colWidths=[c0, cd, cd, cd, cd, cd, cd, cd, cn, ca, co])
    tracker_table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), TABLE_HEADER_BG),
        ("TEXTCOLOR", (0, 0), (-1, 0), WHITE),
        ("BACKGROUND", (0, 2), (-1, 2), TABLE_ALT_ROW),
        ("BACKGROUND", (0, 4), (-1, 4), TABLE_ALT_ROW),
        ("BACKGROUND", (0, -1), (-1, -1), HexColor("#e8f0fe")),
        ("FONTNAME", (0, 0), (-1, -1), "Lexend"),
        ("FONTSIZE", (0, 0), (-1, -1), 7.5),
        ("ALIGN", (1, 0), (-1, -1), "CENTER"),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("TOPPADDING", (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
        ("LEFTPADDING", (0, 0), (-1, -1), 4),
        ("RIGHTPADDING", (0, 0), (-1, -1), 4),
        ("GRID", (0, 0), (-1, -1), 0.5, BORDER_COLOR),
    ]))
    story.append(tracker_table)

    story.append(Spacer(1, 4 * mm))

    # Action steps once you see the data
    story.append(Paragraph("Once you have 4\u20138 weeks of data, act on what you see:", S_H3))

    actions = [
        ("<b>Midweek occupancy below 40%?</b> \u2192 Create a midweek promo (e.g., 3-night stay, pay for 2)",
        ),
        ("<b>Same rooms always empty?</b> \u2192 Check pricing, check listing quality, consider different marketing for those units",
        ),
        ("<b>Post-salary-week dip?</b> \u2192 Pre-book loyal customers with a standing reservation offer",
        ),
    ]
    for a in actions:
        story.append(Paragraph(f"\u2022  {a[0]}", S_BULLET))

    story.append(Spacer(1, 4 * mm))

    # Honest note (orange callout)
    honest_para = Paragraph(
        '<font face="Lexend-SemiBold" color="#b7791f">An honest note:</font><br/><br/>'
        '<font face="Lexend" color="#333333">'
        'Tracking by hand gives you the data. But it\u2019s backward-looking \u2014 you see what happened, '
        'not what\u2019s happening now. And it can\u2019t alert you to opportunities in real time. '
        'By the time you notice Room 3 has been empty all week, the week is already over.<br/><br/>'
        'A manual tracker tells you where the problem <i>was</i>. Automation tells you where the '
        'opportunity <i>is</i> \u2014 right now.</font>',
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
    # PAGE 6: THE AUTOMATED FIX
    # =====================================================

    story.append(Paragraph("THE AUTOMATED FIX \u2014 WHAT REAL-TIME VISIBILITY LOOKS LIKE", S_H1))
    story.append(hr())

    story.append(Paragraph(
        "Here\u2019s what changes when occupancy tracking happens automatically, in real time, "
        "across every room in your property:",
        S_BODY))

    story.append(Spacer(1, 3 * mm))

    # Green callout box — automated features
    auto_items = [
        ("Live occupancy dashboard.",
         "Updated in real time, not at the end of the week. You open the dashboard and see exactly "
         "which rooms are occupied, which are empty, and which have upcoming bookings. Right now, not last Friday."),
        ("Automatic gap detection.",
         "The system flags rooms that have been empty for 3 or more consecutive days. Instead of "
         "discovering this on Friday afternoon, you know on Tuesday morning \u2014 while you can still do something about it."),
        ("Occupancy trends by day, week, and season.",
         "See that your Tuesdays consistently run at 35% occupancy. See that the second week of every month dips. "
         "See that December outperforms every other month by 40%. Patterns become visible and actionable."),
        ("RevPAR tracking.",
         "Know your actual earning power per room, not just your listed nightly rate. This single number "
         "tells you more about your property\u2019s health than any other metric."),
        ("Dynamic pricing suggestions.",
         "\u201CRoom 4 is empty Tuesday through Thursday. Similar rooms in your area are selling at "
         "NGN 22,000. Consider a midweek rate.\u201D Actionable pricing intelligence, not just data."),
        ("Automated promotion triggers.",
         "When occupancy drops below a threshold you set, the system can send targeted offers to past guests. "
         "\u201CStay midweek this month and get 30% off.\u201D No manual effort required."),
        ("Booking trend forecasting.",
         "See next week\u2019s expected occupancy before it happens, based on current bookings and historical "
         "patterns. Act proactively instead of reactively."),
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

    # Spacer product callout (dark blue box)
    spacer_para_white = Paragraph(
        '<font face="Lexend-SemiBold" color="#ffffff" size="10">'
        'This is what Spacer gives property operators \u2014 not just a booking tool, '
        'but a revenue visibility engine.</font><br/><br/>'
        '<font face="Lexend" color="#e0e0e0" size="9">'
        'Currently managing 500+ bookings monthly across properties in Abuja and Kaduna. '
        'Live dashboards. Occupancy analytics. Gap detection. Dynamic pricing tools. '
        'Everything you need to see and fill every empty night across your property.</font>',
        make_style("spacer_cta", fontSize=9, leading=13, textColor=WHITE, spaceAfter=0))
    spacer_box = Table([[spacer_para_white]], colWidths=[AVAIL_W - 20])
    spacer_box.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), ACCENT_BLUE),
        ("TOPPADDING", (0, 0), (-1, -1), 12),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 12),
        ("LEFTPADDING", (0, 0), (-1, -1), 14),
        ("RIGHTPADDING", (0, 0), (-1, -1), 14),
    ]))
    story.append(spacer_box)

    story.append(PageBreak())

    # =====================================================
    # PAGE 7: SELF-ASSESSMENT + CTA
    # =====================================================

    story.append(Paragraph(
        "YOUR OCCUPANCY HEALTH CHECK",
        S_H1))
    story.append(hr())

    story.append(Paragraph(
        "Answer these five statements honestly. Count how many are true for your property.",
        S_BODY))

    story.append(Spacer(1, 3 * mm))

    # Scorecard table
    score_data = [
        [Paragraph("<b>#</b>", S_TABLE_HEADER),
         Paragraph("<b>Statement</b>", S_TABLE_HEADER),
         Paragraph("<b>Yes / No</b>", S_TABLE_HEADER)],
        [Paragraph("1", S_TABLE_CELL_BOLD),
         Paragraph("I don\u2019t know my exact occupancy rate for last month", S_TABLE_CELL),
         Paragraph("", S_TABLE_CELL)],
        [Paragraph("2", S_TABLE_CELL_BOLD),
         Paragraph("I can\u2019t tell you which day of the week has the lowest bookings", S_TABLE_CELL),
         Paragraph("", S_TABLE_CELL)],
        [Paragraph("3", S_TABLE_CELL_BOLD),
         Paragraph("I\u2019ve had rooms sit empty for 5+ consecutive days without taking action", S_TABLE_CELL),
         Paragraph("", S_TABLE_CELL)],
        [Paragraph("4", S_TABLE_CELL_BOLD),
         Paragraph("I don\u2019t have a different strategy for midweek vs weekends", S_TABLE_CELL),
         Paragraph("", S_TABLE_CELL)],
        [Paragraph("5", S_TABLE_CELL_BOLD),
         Paragraph("I\u2019ve never calculated my RevPAR", S_TABLE_CELL),
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
         "Your visibility is better than most. You likely have systems in place \u2014 or a very small "
         "property where you can track things manually. Smart automation would still save you time "
         "and reveal patterns you can\u2019t see by hand."),
        ("2\u20133", "#e67e22", ORANGE_LIGHT,
         "You have blind spots that are costing you real money. You\u2019re making decisions based on "
         "intuition rather than data, and some of those decisions are leaving revenue on the table. "
         "Start with the free tracker on Page 5 \u2014 it will change how you think about your property "
         "within a month."),
        ("4\u20135", "#c0392b", RED_LIGHT,
         "You\u2019re operating in the dark. Rooms are sitting empty, revenue is being left on the table, "
         "and you don\u2019t have the visibility to know where or why. This is the single biggest thing you "
         "can fix to increase your property\u2019s revenue \u2014 and it starts with knowing your numbers."),
    ]
    for score_range, color, bg, interpretation in scores:
        score_para = Paragraph(
            f'<font face="Lexend-Bold" color="{color}">{score_range}:</font>  {interpretation}',
            make_style(f"si_{score_range[0]}_{id(score_range)}", fontSize=9, leading=13,
                        textColor=MEDIUM_TEXT, spaceAfter=0))
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
        "In 15 minutes, we\u2019ll review your current occupancy tracking, identify where revenue is "
        "being left on the table, and show you what real-time visibility looks like for your specific property.",
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
        "This guide was prepared by <b>Algolog Limited</b>, a Nigerian technology company that "
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
