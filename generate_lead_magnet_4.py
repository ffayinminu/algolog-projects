"""
Generate Lead Magnet #4: "Is Your Serviced Apartment Actually Profitable?
The 10-Minute Financial Health Check for Hospitality Operators"
Format: Branded PDF — multi-page financial health check with callout boxes, numbered metrics, and self-assessment
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
OUTPUT_DIR = os.path.join(BASE, "Proposals")
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "Lead-Magnet-Actually-Profitable.pdf")

# Ensure output directory exists
os.makedirs(OUTPUT_DIR, exist_ok=True)

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
S_QUOTE = make_style("S_QUOTE", fontName="Lexend-Medium", fontSize=9, leading=13, textColor=ACCENT_BLUE,
                      leftIndent=16, rightIndent=16, spaceBefore=4, spaceAfter=4, alignment=TA_CENTER)
S_FORMULA = make_style("S_FORMULA", fontName="Lexend-SemiBold", fontSize=9, leading=13, textColor=DARK_TEXT,
                        leftIndent=20, spaceAfter=4)


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


def metric_row(number, color, title_text, body_text):
    """Build a numbered metric with a badge and description."""
    badge = NumberBadge(number, color)
    inner_w = AVAIL_W - 50
    combined = Paragraph(
        f'<font face="Lexend-SemiBold" color="#1a1a1a">{title_text}</font><br/>'
        f'<font face="Lexend" color="#333333">{body_text}</font>',
        make_style(f"metric_{number}", fontSize=9, leading=13, textColor=MEDIUM_TEXT, spaceAfter=2)
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


def quote_box(text):
    """Styled quote box."""
    para = Paragraph(
        f'<font face="Lexend-Medium" color="#0f3460">\u201C{text}\u201D</font>',
        make_style(f"q_{text[:8]}", fontName="Lexend-Medium", fontSize=9.5, leading=14,
                   textColor=ACCENT_BLUE, alignment=TA_CENTER, spaceAfter=0)
    )
    box = Table([[para]], colWidths=[AVAIL_W - 40])
    box.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), BLUE_LIGHT),
        ("TOPPADDING", (0, 0), (-1, -1), 8),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
        ("LEFTPADDING", (0, 0), (-1, -1), 14),
        ("RIGHTPADDING", (0, 0), (-1, -1), 14),
    ]))
    box.hAlign = "CENTER"
    return box


def formula_box(formula_text):
    """Styled formula display box."""
    para = Paragraph(
        f'<font face="Lexend-SemiBold" color="#1a1a1a">{formula_text}</font>',
        make_style(f"f_{formula_text[:8]}", fontName="Lexend-SemiBold", fontSize=9.5, leading=14,
                   textColor=DARK_TEXT, alignment=TA_CENTER, spaceAfter=0)
    )
    box = Table([[para]], colWidths=[AVAIL_W - 50])
    box.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), HexColor("#f8f9fa")),
        ("TOPPADDING", (0, 0), (-1, -1), 7),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
        ("LEFTPADDING", (0, 0), (-1, -1), 12),
        ("RIGHTPADDING", (0, 0), (-1, -1), 12),
        ("BOX", (0, 0), (-1, -1), 0.5, BORDER_COLOR),
    ]))
    box.hAlign = "CENTER"
    return box


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

    story.append(Spacer(1, 12 * mm))
    story.append(hr())
    story.append(Spacer(1, 6 * mm))

    # Title
    story.append(Paragraph(
        "Is Your Serviced Apartment<br/>Actually Profitable?",
        make_style("cover_title", fontName="Lexend-Bold", fontSize=26, leading=32,
                    textColor=ACCENT_BLUE, alignment=TA_CENTER, spaceAfter=4)))

    story.append(Spacer(1, 3 * mm))

    story.append(Paragraph(
        "The 10-Minute Financial Health Check<br/>for Hospitality Operators",
        make_style("cover_sub", fontName="Lexend-Medium", fontSize=13, leading=18,
                    textColor=MEDIUM_TEXT, alignment=TA_CENTER, spaceAfter=6)))

    story.append(Spacer(1, 8 * mm))
    story.append(hr())
    story.append(Spacer(1, 6 * mm))

    # Hook line
    story.append(Paragraph(
        "Revenue is not profit. Occupancy is not success.<br/>"
        "Here are the <b>5 numbers</b> that tell you the truth.",
        make_style("cover_hook", fontName="Lexend-Medium", fontSize=11, leading=16,
                    textColor=DARK_TEXT, alignment=TA_CENTER, spaceAfter=8)))

    story.append(Spacer(1, 6 * mm))

    # What's inside
    story.append(Paragraph(
        "What\u2019s inside:",
        make_style("cover_inside_h", fontName="Lexend-SemiBold", fontSize=11, leading=15,
                    textColor=DARK_TEXT, alignment=TA_CENTER, spaceAfter=6)))

    inside_items = [
        "Why high occupancy doesn\u2019t always mean high profit",
        "The 5 financial metrics every operator should track",
        "How to calculate each one (with Nigerian benchmarks)",
        "How these numbers interact \u2014 the profitability matrix",
        "A free monthly health check worksheet you can use today",
        "What automated financial tracking looks like at scale",
        "A self-assessment to score your property\u2019s financial visibility",
    ]
    for item in inside_items:
        story.append(Paragraph(
            f'\u2022  {item}',
            make_style(f"ci_{item[:10]}", fontSize=9.5, leading=14, textColor=MEDIUM_TEXT,
                        alignment=TA_CENTER, spaceAfter=3)))

    story.append(Spacer(1, 10 * mm))

    story.append(Paragraph(
        "A free diagnostic tool by Algolog Limited  |  spacer.so",
        make_style("cover_tag", fontName="Lexend-Light", fontSize=9, leading=12,
                    textColor=LIGHT_TEXT, alignment=TA_CENTER)))

    story.append(PageBreak())

    # =====================================================
    # PAGE 2: REVENUE IS NOT PROFIT
    # =====================================================

    story.append(Paragraph("REVENUE IS NOT PROFIT", S_H1))
    story.append(Paragraph(
        "Why Busy Doesn\u2019t Mean Profitable",
        make_style("p2_sub", fontName="Lexend-SemiBold", fontSize=11, leading=14,
                    textColor=MEDIUM_TEXT, spaceAfter=4)))
    story.append(hr())

    story.append(Paragraph(
        "The most common thing we hear from serviced apartment operators is: "
        "\u201CWe had a great month \u2014 we were almost fully booked!\u201D "
        "But the question that matters is different: <b>were you actually profitable?</b>",
        S_BODY))

    story.append(Spacer(1, 2 * mm))

    story.append(Paragraph(
        "High occupancy does not equal high profit. You can be 80% occupied and still losing money if:",
        S_BODY))

    leakage_items = [
        "<b>Payments aren\u2019t being collected properly.</b> Guests confirm bookings, "
        "say they\u2019ll transfer, and the payment never arrives \u2014 or arrives partially "
        "and no one follows up.",
        "<b>Staff costs eat into margins during peak periods.</b> When you\u2019re fully booked, "
        "you need more cleaning, more reception coverage, more maintenance responses. Those costs "
        "scale with occupancy, but revenue only scales if rates hold.",
        "<b>You\u2019re discounting too aggressively without tracking the impact.</b> Running a 30% "
        "discount to fill rooms feels like a win until you realise the rooms would have filled at "
        "15% off \u2014 or even at full rate with better visibility.",
        "<b>Utility and maintenance costs aren\u2019t allocated per room.</b> You know your total "
        "electricity bill, but do you know what each room costs you to operate per night? "
        "Without that number, you can\u2019t price accurately.",
        "<b>Guest acquisition cost is higher than you think.</b> Every new guest costs marketing "
        "spend, staff time, platform fees, and onboarding effort. If you\u2019re spending NGN 15,000 "
        "to acquire a guest who books one night at NGN 25,000, the math doesn\u2019t work.",
    ]
    for item in leakage_items:
        story.append(Paragraph(f"\u2022  {item}", S_BULLET))

    story.append(Spacer(1, 3 * mm))

    # Flip side callout (blue)
    flip_para = Paragraph(
        '<font face="Lexend-SemiBold" color="#0f3460">The flip side is equally important:</font> '
        'Low occupancy does not equal failure. A property at 55% occupancy with premium rates, '
        'strong payment collection, and a 40% guest return rate can outperform one at 85% occupancy '
        'with low rates and payment gaps.',
        make_style("flip", fontSize=9, leading=13, textColor=MEDIUM_TEXT, spaceAfter=0))
    flip_box = Table([[flip_para]], colWidths=[AVAIL_W - 20])
    flip_box.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), BLUE_LIGHT),
        ("TOPPADDING", (0, 0), (-1, -1), 9),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 9),
        ("LEFTPADDING", (0, 0), (-1, -1), 12),
        ("RIGHTPADDING", (0, 0), (-1, -1), 12),
    ]))
    story.append(flip_box)

    story.append(Spacer(1, 4 * mm))

    story.append(quote_box(
        "The question isn\u2019t \u2018how busy are we?\u2019 "
        "It\u2019s \u2018how much of what we earn do we actually keep?\u2019"))

    story.append(PageBreak())

    # =====================================================
    # PAGE 3: THE 5 NUMBERS (Numbers 1-3)
    # =====================================================

    story.append(Paragraph("THE 5 NUMBERS EVERY OPERATOR SHOULD KNOW", S_H1))
    story.append(hr())

    story.append(Paragraph(
        "These are the five metrics that separate operators who are truly profitable from those "
        "who are just busy. Each one takes less than 2 minutes to calculate.",
        S_BODY))

    story.append(Spacer(1, 3 * mm))

    # --- NUMBER 1: Occupancy Rate ---
    story.append(metric_row(1, ACCENT_BLUE,
        "OCCUPANCY RATE",
        "The percentage of your available room-nights that are actually booked and occupied."))

    story.append(Spacer(1, 2 * mm))
    story.append(formula_box("Occupancy Rate = (Booked Room-Nights \u00f7 Total Available Room-Nights) \u00d7 100"))
    story.append(Spacer(1, 2 * mm))

    story.append(Paragraph(
        "<b>Example:</b> 10 rooms \u00d7 30 days = 300 available room-nights. "
        "If 195 were booked, occupancy = 65%.",
        make_style("ex1", fontSize=8.5, leading=12, textColor=MEDIUM_TEXT, leftIndent=10, spaceAfter=3)))

    # Benchmark callout
    bench1_para = Paragraph(
        '<font face="Lexend-SemiBold" color="#0f3460">Benchmark:</font>  '
        '<b>60\u201375%</b> is healthy.  '
        'Below 50%: pricing or visibility problem.  '
        'Above 80%: you may be undercharging.',
        make_style("b1", fontSize=8.5, leading=12, textColor=MEDIUM_TEXT, spaceAfter=0))
    bench1_box = Table([[bench1_para]], colWidths=[AVAIL_W - 20])
    bench1_box.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), YELLOW_LIGHT),
        ("TOPPADDING", (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
        ("LEFTPADDING", (0, 0), (-1, -1), 10),
        ("RIGHTPADDING", (0, 0), (-1, -1), 10),
    ]))
    story.append(bench1_box)

    story.append(Spacer(1, 5 * mm))

    # --- NUMBER 2: RevPAR ---
    story.append(metric_row(2, ACCENT_BLUE,
        "RevPAR (Revenue Per Available Room-Night)",
        "The single most important metric in hospitality. It combines how full you are with how "
        "much you charge, giving you one number that tells you how well your rooms are performing."))

    story.append(Spacer(1, 2 * mm))
    story.append(formula_box("RevPAR = Total Room Revenue \u00f7 Total Available Room-Nights"))
    story.append(Paragraph(
        "Or simply: <b>RevPAR = Occupancy Rate \u00d7 Average Nightly Rate</b>",
        make_style("revpar_alt", fontSize=8.5, leading=12, textColor=MEDIUM_TEXT,
                    alignment=TA_CENTER, spaceAfter=3)))

    story.append(Paragraph(
        "<b>Example:</b> Average rate NGN 30,000 \u00d7 65% occupancy = <b>RevPAR of NGN 19,500</b>. "
        "This means each room \u2014 booked or not \u2014 generates NGN 19,500/night on average.",
        make_style("ex2", fontSize=8.5, leading=12, textColor=MEDIUM_TEXT, leftIndent=10, spaceAfter=3)))

    bench2_para = Paragraph(
        '<font face="Lexend-SemiBold" color="#0f3460">Benchmark:</font>  '
        'For mid-range Abuja serviced apartments (NGN 25K\u201335K/night), '
        'a RevPAR of <b>NGN 16,000\u201322,000</b> indicates healthy performance.',
        make_style("b2", fontSize=8.5, leading=12, textColor=MEDIUM_TEXT, spaceAfter=0))
    bench2_box = Table([[bench2_para]], colWidths=[AVAIL_W - 20])
    bench2_box.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), YELLOW_LIGHT),
        ("TOPPADDING", (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
        ("LEFTPADDING", (0, 0), (-1, -1), 10),
        ("RIGHTPADDING", (0, 0), (-1, -1), 10),
    ]))
    story.append(bench2_box)

    story.append(Spacer(1, 3 * mm))

    story.append(quote_box(
        "This is the one number that tells you more than any other. "
        "It combines how full you are with how much you charge."))

    story.append(Spacer(1, 5 * mm))

    # --- NUMBER 3: Payment Collection Rate ---
    story.append(metric_row(3, ACCENT_BLUE,
        "PAYMENT COLLECTION RATE",
        "The percentage of money you invoiced that you actually received. "
        "This is where many Nigerian serviced apartments lose money without realising it."))

    story.append(Spacer(1, 2 * mm))
    story.append(formula_box("Collection Rate = (Total Payments Received \u00f7 Total Payments Invoiced) \u00d7 100"))
    story.append(Spacer(1, 2 * mm))

    bench3_para = Paragraph(
        '<font face="Lexend-SemiBold" color="#0f3460">Benchmark:</font>  '
        '<b>95%+</b> is where you should be. '
        'Below 90% means you have a serious collection problem directly reducing your profit.',
        make_style("b3", fontSize=8.5, leading=12, textColor=MEDIUM_TEXT, spaceAfter=0))
    bench3_box = Table([[bench3_para]], colWidths=[AVAIL_W - 20])
    bench3_box.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), YELLOW_LIGHT),
        ("TOPPADDING", (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
        ("LEFTPADDING", (0, 0), (-1, -1), 10),
        ("RIGHTPADDING", (0, 0), (-1, -1), 10),
    ]))
    story.append(bench3_box)

    story.append(Spacer(1, 2 * mm))

    # Common causes callout
    causes_title = Paragraph(
        '<font face="Lexend-SemiBold" color="#b7791f">Common causes of leakage:</font>',
        make_style("causes_h", fontSize=9, leading=13, textColor=DARK_TEXT, spaceAfter=3))
    causes = [
        "Unconfirmed bank transfers (\u201CI\u2019ll send it now\u201D \u2014 and then silence)",
        "Cash payments not recorded by staff",
        "Partial payments not followed up to completion",
        "Deposits collected but balance never converted to full payment",
    ]
    cause_elements = [causes_title]
    for c in causes:
        cause_elements.append(Paragraph(
            f"\u2022  {c}",
            make_style(f"c_{c[:8]}", fontSize=8.5, leading=12, textColor=MEDIUM_TEXT,
                        leftIndent=10, spaceAfter=2)))
    causes_box = callout_box(cause_elements, ORANGE_LIGHT, ORANGE_ACCENT)
    story.append(causes_box)

    story.append(PageBreak())

    # =====================================================
    # PAGE 4: THE 5 NUMBERS (Numbers 4-5)
    # =====================================================

    story.append(Paragraph("THE 5 NUMBERS (CONTINUED)", S_H1))
    story.append(hr())

    # --- NUMBER 4: Guest Return Rate ---
    story.append(metric_row(4, ACCENT_BLUE,
        "GUEST RETURN RATE",
        "The percentage of your guests who have stayed with you before. "
        "This is your most powerful profitability indicator because returning guests "
        "cost almost nothing to acquire."))

    story.append(Spacer(1, 2 * mm))
    story.append(formula_box("Guest Return Rate = (Returning Guests \u00f7 Total Guests in Period) \u00d7 100"))
    story.append(Spacer(1, 2 * mm))

    bench4_para = Paragraph(
        '<font face="Lexend-SemiBold" color="#0f3460">Benchmark:</font>  '
        '<b>25\u201340%</b> is good. Above 40% is excellent. '
        'Below 20%: your guest experience needs attention.',
        make_style("b4", fontSize=8.5, leading=12, textColor=MEDIUM_TEXT, spaceAfter=0))
    bench4_box = Table([[bench4_para]], colWidths=[AVAIL_W - 20])
    bench4_box.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), YELLOW_LIGHT),
        ("TOPPADDING", (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
        ("LEFTPADDING", (0, 0), (-1, -1), 10),
        ("RIGHTPADDING", (0, 0), (-1, -1), 10),
    ]))
    story.append(bench4_box)

    story.append(Spacer(1, 2 * mm))

    # Why it matters callout (green)
    return_para = Paragraph(
        '<font face="Lexend-SemiBold" color="#27ae60">Why this matters:</font>  '
        'A returning guest costs you almost nothing to acquire. They already know your property, '
        'they\u2019ve had a good experience, and they book directly \u2014 no marketing spend, no platform fees, '
        'no onboarding time. Every percentage point increase in your return rate directly increases '
        'your profit margin.',
        make_style("return_why", fontSize=8.5, leading=12, textColor=MEDIUM_TEXT, spaceAfter=0))
    return_box = Table([[return_para]], colWidths=[AVAIL_W - 20])
    return_box.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), GREEN_LIGHT),
        ("TOPPADDING", (0, 0), (-1, -1), 8),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
        ("LEFTPADDING", (0, 0), (-1, -1), 10),
        ("RIGHTPADDING", (0, 0), (-1, -1), 10),
    ]))
    story.append(return_box)

    story.append(Spacer(1, 6 * mm))

    # --- NUMBER 5: Cost Per Booking ---
    story.append(metric_row(5, ACCENT_BLUE,
        "COST PER BOOKING",
        "How much it costs you to service a single booking, including all operating costs. "
        "This is the number most operators have never calculated \u2014 and it\u2019s often the reason "
        "properties that look busy aren\u2019t actually profitable."))

    story.append(Spacer(1, 2 * mm))
    story.append(formula_box("Cost Per Booking = Total Operating Costs \u00f7 Total Bookings in Period"))
    story.append(Spacer(1, 2 * mm))

    story.append(Paragraph(
        "<b>Operating costs include:</b> staff salaries (proportional), marketing spend, utilities, "
        "maintenance, cleaning, platform/payment fees, and consumables.",
        make_style("costs_inc", fontSize=8.5, leading=12, textColor=MEDIUM_TEXT, leftIndent=10, spaceAfter=3)))

    bench5_para = Paragraph(
        '<font face="Lexend-SemiBold" color="#0f3460">Benchmark:</font>  '
        'Should be <b>less than 30%</b> of your average booking value. '
        'If your average booking is NGN 90,000 (3 nights at NGN 30,000), '
        'your cost per booking should be under NGN 27,000.',
        make_style("b5", fontSize=8.5, leading=12, textColor=MEDIUM_TEXT, spaceAfter=0))
    bench5_box = Table([[bench5_para]], colWidths=[AVAIL_W - 20])
    bench5_box.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), YELLOW_LIGHT),
        ("TOPPADDING", (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
        ("LEFTPADDING", (0, 0), (-1, -1), 10),
        ("RIGHTPADDING", (0, 0), (-1, -1), 10),
    ]))
    story.append(bench5_box)

    story.append(Spacer(1, 4 * mm))

    story.append(quote_box(
        "If it costs you more to service a booking than you\u2019re making from it, "
        "you\u2019re running a charity, not a business."))

    story.append(PageBreak())

    # =====================================================
    # PAGE 5: THE PROFITABILITY MATRIX
    # =====================================================

    story.append(Paragraph("HOW THESE NUMBERS CONNECT", S_H1))
    story.append(Paragraph(
        "The Profitability Matrix",
        make_style("p5_sub", fontName="Lexend-SemiBold", fontSize=11, leading=14,
                    textColor=MEDIUM_TEXT, spaceAfter=4)))
    story.append(hr())

    story.append(Paragraph(
        "These five numbers don\u2019t exist in isolation. They interact, and the combination "
        "tells you more than any single metric. Here are the four most common patterns we see:",
        S_BODY))

    story.append(Spacer(1, 3 * mm))

    # Matrix combinations as styled boxes
    matrix_items = [
        ("High occupancy + Low collection rate",
         "\u201CYou\u2019re busy but broke.\u201D",
         "You\u2019re filling rooms, but the money isn\u2019t making it to your bank account. "
         "This is one of the most common traps for Nigerian serviced apartments \u2014 the property "
         "looks successful, but the actual cash collected tells a different story.",
         RED_LIGHT, "#c0392b"),
        ("Low occupancy + High rate + High return rate",
         "\u201CPremium and sustainable.\u201D",
         "You don\u2019t need to be fully booked to be profitable. If you\u2019re charging premium rates, "
         "collecting efficiently, and guests keep coming back, you have a strong, sustainable business.",
         GREEN_LIGHT, "#27ae60"),
        ("High occupancy + High cost per booking",
         "\u201CWorking hard, keeping little.\u201D",
         "You\u2019re always busy, your staff is stretched, but at the end of the month there\u2019s "
         "not much left. Your costs are scaling faster than your revenue.",
         ORANGE_LIGHT, "#e67e22"),
        ("Low occupancy + Low return rate",
         "\u201CLeaking from both ends.\u201D",
         "Not enough guests are coming in, and the ones who do come aren\u2019t coming back. "
         "This requires attention on both acquisition and experience.",
         YELLOW_LIGHT, "#b7791f"),
    ]

    for combo, label, desc, bg, color in matrix_items:
        combo_para = Paragraph(
            f'<font face="Lexend-Bold" color="{color}">{combo}</font><br/>'
            f'<font face="Lexend-SemiBold" color="{color}" size="10">{label}</font><br/><br/>'
            f'<font face="Lexend" color="#333333" size="9">{desc}</font>',
            make_style(f"mx_{combo[:10]}", fontSize=9, leading=13, textColor=MEDIUM_TEXT, spaceAfter=0))
        combo_box = Table([[combo_para]], colWidths=[AVAIL_W - 20])
        combo_box.setStyle(TableStyle([
            ("BACKGROUND", (0, 0), (-1, -1), bg),
            ("TOPPADDING", (0, 0), (-1, -1), 9),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 9),
            ("LEFTPADDING", (0, 0), (-1, -1), 12),
            ("RIGHTPADDING", (0, 0), (-1, -1), 12),
        ]))
        story.append(combo_box)
        story.append(Spacer(1, 3 * mm))

    story.append(Spacer(1, 3 * mm))

    story.append(quote_box(
        "Most operators only look at occupancy. That\u2019s like judging a restaurant "
        "by how full it is without checking if customers actually paid."))

    story.append(PageBreak())

    # =====================================================
    # PAGE 6: THE FREE FIX -- MONTHLY HEALTH CHECK WORKSHEET
    # =====================================================

    story.append(Paragraph("THE FREE FIX \u2014 YOUR MONTHLY HEALTH CHECK", S_H1))
    story.append(hr())

    story.append(Paragraph(
        "This is the tool. Print it out or copy it into a spreadsheet. Fill it in on the "
        "1st of every month. It takes 10 minutes.",
        S_BODY))

    story.append(Spacer(1, 3 * mm))

    # Worksheet table (blue callout)
    ws_title = Paragraph(
        '<font face="Lexend-SemiBold" color="#0f3460">Monthly Financial Health Check Worksheet</font>',
        make_style("ws_h", fontSize=10, leading=14, textColor=ACCENT_BLUE, spaceAfter=6))

    ws_data = [
        [Paragraph("<b>Metric</b>", S_TABLE_HEADER),
         Paragraph("<b>Your Number</b>", S_TABLE_HEADER),
         Paragraph("<b>Benchmark</b>", S_TABLE_HEADER),
         Paragraph("<b>Status</b>", S_TABLE_HEADER)],
        [Paragraph("Occupancy Rate", S_TABLE_CELL_BOLD),
         Paragraph("___%", S_TABLE_CELL),
         Paragraph("60\u201375%", S_TABLE_CELL),
         Paragraph("", S_TABLE_CELL)],
        [Paragraph("RevPAR", S_TABLE_CELL_BOLD),
         Paragraph("NGN ___", S_TABLE_CELL),
         Paragraph("NGN 19,500+", S_TABLE_CELL),
         Paragraph("", S_TABLE_CELL)],
        [Paragraph("Collection Rate", S_TABLE_CELL_BOLD),
         Paragraph("___%", S_TABLE_CELL),
         Paragraph("95%+", S_TABLE_CELL),
         Paragraph("", S_TABLE_CELL)],
        [Paragraph("Guest Return Rate", S_TABLE_CELL_BOLD),
         Paragraph("___%", S_TABLE_CELL),
         Paragraph("25\u201340%", S_TABLE_CELL),
         Paragraph("", S_TABLE_CELL)],
        [Paragraph("Cost Per Booking", S_TABLE_CELL_BOLD),
         Paragraph("NGN ___", S_TABLE_CELL),
         Paragraph("<30% of avg booking", S_TABLE_CELL),
         Paragraph("", S_TABLE_CELL)],
    ]
    inner_ws_w = AVAIL_W - 44
    ws_table = Table(ws_data,
                     colWidths=[inner_ws_w * 0.30, inner_ws_w * 0.22, inner_ws_w * 0.30, inner_ws_w * 0.18])
    ws_table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), TABLE_HEADER_BG),
        ("TEXTCOLOR", (0, 0), (-1, 0), WHITE),
        ("BACKGROUND", (0, 2), (-1, 2), TABLE_ALT_ROW),
        ("BACKGROUND", (0, 4), (-1, 4), TABLE_ALT_ROW),
        ("FONTNAME", (0, 0), (-1, -1), "Lexend"),
        ("FONTSIZE", (0, 0), (-1, -1), 8.5),
        ("ALIGN", (1, 0), (-1, -1), "CENTER"),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("TOPPADDING", (0, 0), (-1, -1), 7),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
        ("LEFTPADDING", (0, 0), (-1, -1), 6),
        ("GRID", (0, 0), (-1, -1), 0.5, BORDER_COLOR),
    ]))

    ws_note = Paragraph(
        '<font face="Lexend" size="8" color="#555555">'
        'Fill this in on the 1st of every month. After 3 months, you\u2019ll see trends '
        'that would have taken years to notice otherwise.</font>',
        make_style("ws_note", fontSize=8, leading=11, textColor=LIGHT_TEXT, spaceAfter=0))

    ws_box = callout_box([ws_title, Spacer(1, 2 * mm), ws_table, Spacer(1, 3 * mm), ws_note], BLUE_LIGHT)
    story.append(ws_box)

    story.append(Spacer(1, 5 * mm))

    # Action items
    story.append(Paragraph("What to do with your results:", S_H2))

    actions = [
        ("<b>Occupancy below 60%?</b> Focus on visibility and pricing. Are you listed on enough "
         "platforms? Is your pricing competitive? Could you run midweek or off-peak promotions?"),
        ("<b>Collection below 90%?</b> Tighten payment rules immediately. No check-in without "
         "confirmed payment. Assign one person to reconcile daily."),
        ("<b>Return rate below 20%?</b> Your guest experience needs work. Look at reviews, "
         "survey past guests, and identify friction points in the stay."),
        ("<b>Cost per booking above 35%?</b> Look for automation opportunities. Where are you "
         "spending staff time on things a system could handle?"),
    ]
    for a in actions:
        story.append(Paragraph(f"\u2022  {a}", S_BULLET))

    story.append(Spacer(1, 4 * mm))

    # Honest note callout (orange)
    honest_para = Paragraph(
        '<font face="Lexend-SemiBold" color="#b7791f">An honest note:</font><br/><br/>'
        '<font face="Lexend" color="#333333">'
        'This worksheet gives you monthly snapshots. That\u2019s genuinely valuable \u2014 '
        'most operators don\u2019t even have this. But the real power comes from tracking these '
        'numbers <b>daily</b>, seeing trends in real time, and getting alerts before problems '
        'become losses.<br/><br/>'
        'A monthly snapshot tells you what happened. Daily tracking helps you change '
        'what\u2019s happening.</font>',
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
    # PAGE 7: THE AUTOMATED FIX -- SPACER
    # =====================================================

    story.append(Paragraph("THE AUTOMATED FIX \u2014 RUNNING ON DATA", S_H1))
    story.append(hr())

    story.append(Paragraph(
        "This is what the same five metrics look like when they\u2019re tracked automatically, "
        "updated in real time, and connected to your bookings, payments, and operations.",
        S_BODY))

    story.append(Spacer(1, 3 * mm))

    # Green callout box with Spacer features
    auto_items = [
        ("Live dashboard with all 5 metrics updated in real time.",
         "Open your laptop or phone, and your occupancy rate, RevPAR, collection rate, return rate, "
         "and cost metrics are right there \u2014 current as of this moment."),
        ("Automatic occupancy and RevPAR tracking.",
         "No manual counting of room-nights. The system calculates it from your live bookings."),
        ("Payment collection tied to bookings.",
         "The system flags unpaid bookings automatically. No transfer goes untracked. "
         "Every invoice has a status: paid, pending, overdue."),
        ("Guest profiles that track return visits and lifetime value.",
         "You know which guests have been 3 times, which ones prefer specific rooms, "
         "and what each guest is worth to your business over time."),
        ("Cost tracking per room, per booking, per month.",
         "You know exactly what each room costs to operate and what each booking costs to service."),
        ("Automated alerts when metrics dip.",
         "Occupancy dropping below threshold? Collection rate falling? A room empty for 3+ days? "
         "The system flags it before it becomes a trend."),
        ("Monthly performance reports generated automatically.",
         "No spreadsheet work. No manual calculations. A complete financial health report "
         "for your property, every month, without lifting a finger."),
    ]

    auto_elements = [
        Paragraph(
            '<font face="Lexend-SemiBold" color="#27ae60">What automation delivers:</font>',
            make_style("auto_h", fontSize=10, leading=14, textColor=GREEN, spaceAfter=6)),
    ]
    for i, (title, body) in enumerate(auto_items, 1):
        auto_elements.append(metric_row(i, GREEN, title, body))
        auto_elements.append(Spacer(1, 2 * mm))

    auto_box = callout_box(auto_elements, GREEN_LIGHT)
    story.append(auto_box)

    story.append(Spacer(1, 5 * mm))

    # Spacer blue banner
    spacer_para = Paragraph(
        '<font face="Lexend-SemiBold" color="#ffffff" size="10">'
        'This is what Spacer delivers. Not just a booking system \u2014 '
        'a profitability engine for your property.</font><br/><br/>'
        '<font face="Lexend" color="#e0e0e0" size="9">'
        'Managing 500+ bookings monthly across properties in Abuja and Kaduna. '
        'Real-time dashboards, automated payments, guest profiles, smart lock access, '
        'occupancy analytics, and financial reporting \u2014 all in one platform.</font>',
        make_style("spacer_cta", fontSize=9, leading=13, textColor=WHITE, spaceAfter=0))
    spacer_box = Table([[spacer_para]], colWidths=[AVAIL_W - 20])
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
    # PAGE 8: SELF-ASSESSMENT + CTA
    # =====================================================

    story.append(Paragraph(
        "YOUR FINANCIAL HEALTH SCORE",
        S_H1))
    story.append(hr())

    story.append(Paragraph(
        "Answer these five statements honestly. Count how many are true for you.",
        S_BODY))

    story.append(Spacer(1, 3 * mm))

    # Scorecard table
    score_data = [
        [Paragraph("<b>#</b>", S_TABLE_HEADER),
         Paragraph("<b>Statement</b>", S_TABLE_HEADER),
         Paragraph("<b>Yes / No</b>", S_TABLE_HEADER)],
        [Paragraph("1", S_TABLE_CELL_BOLD),
         Paragraph("I can\u2019t tell you my exact occupancy rate for last month", S_TABLE_CELL),
         Paragraph("", S_TABLE_CELL)],
        [Paragraph("2", S_TABLE_CELL_BOLD),
         Paragraph("I don\u2019t know what percentage of invoiced payments were actually collected", S_TABLE_CELL),
         Paragraph("", S_TABLE_CELL)],
        [Paragraph("3", S_TABLE_CELL_BOLD),
         Paragraph("I have no idea what percentage of my guests are returning guests", S_TABLE_CELL),
         Paragraph("", S_TABLE_CELL)],
        [Paragraph("4", S_TABLE_CELL_BOLD),
         Paragraph("I\u2019ve never calculated my cost per booking", S_TABLE_CELL),
         Paragraph("", S_TABLE_CELL)],
        [Paragraph("5", S_TABLE_CELL_BOLD),
         Paragraph("I don\u2019t know my RevPAR \u2014 or I\u2019d never heard the term before today", S_TABLE_CELL),
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
         "You\u2019re tracking the right numbers. Fine-tuning will unlock more. "
         "A system like Spacer would help you automate what you\u2019re already doing well "
         "and surface insights you can\u2019t see manually."),
        ("2\u20133", "#e67e22", ORANGE_LIGHT,
         "You\u2019re flying partially blind. These gaps are likely costing you "
         "NGN 500K\u20131.5M monthly in missed opportunities \u2014 not because you\u2019re doing "
         "something wrong, but because you don\u2019t have the visibility to do it better."),
        ("4\u20135", "#c0392b", RED_LIGHT,
         "You\u2019re running your property without a dashboard. The numbers you don\u2019t track "
         "are the ones that cost you the most. The good news is that every one of these metrics "
         "can be tracked automatically once the right system is in place."),
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
        "In 15 minutes, we\u2019ll review how your property currently tracks these five metrics, "
        "identify the biggest gaps, and show you what the fix looks like \u2014 "
        "whether you use Spacer or not.",
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
        "This diagnostic tool was prepared by <b>Algolog Limited</b>, a Nigerian technology company that "
        "builds management systems for hospitality and workspace businesses. Our platform, "
        "<b>Spacer</b> (spacer.so), manages 500+ bookings monthly across properties "
        "in Abuja and Kaduna.",
        make_style("fblurb", fontName="Lexend", fontSize=8.5, leading=12,
                    textColor=LIGHT_TEXT, alignment=TA_CENTER, spaceAfter=4)))

    story.append(Paragraph(
        "Algolog Limited  |  5, Kwaji Close, Maitama, Abuja, Nigeria  |  algolog.co  |  spacer.so",
        S_SMALL))

    # Build
    doc.build(story, onFirstPage=add_footer, onLaterPages=add_footer)
    print(f"PDF generated: {OUTPUT_PATH}")
    print(f"File size: {os.path.getsize(OUTPUT_PATH):,} bytes")


if __name__ == "__main__":
    build_pdf()
