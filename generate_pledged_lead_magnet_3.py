"""
Generate Lead Magnet #3 for Pledged: "The Predictable Church"
Subtitle: "How to Know What You'll Receive Next Month (Before It Arrives)"
Format: Branded PDF — multi-page planning guide with callout boxes, numbered steps,
        tables, calculator worksheet, and self-assessment
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
OUTPUT_PATH = os.path.join(BASE, "Proposals/Lead-Magnet-Pledged-Predictable-Church.pdf")

# Ensure output directory exists
os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)

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
S_NUMBEREDITEM = make_style("S_NUMBEREDITEM", fontSize=9.5, leading=14, textColor=MEDIUM_TEXT, leftIndent=18, bulletIndent=6, spaceAfter=4)


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
        "The Predictable Church",
        make_style("cover_title", fontName="Lexend-Bold", fontSize=28, leading=34,
                    textColor=ACCENT_BLUE, alignment=TA_CENTER, spaceAfter=4)))

    story.append(Spacer(1, 2 * mm))

    story.append(Paragraph(
        "How to Know What You\u2019ll Receive<br/>Next Month (Before It Arrives)",
        make_style("cover_sub", fontName="Lexend-Medium", fontSize=13, leading=18,
                    textColor=MEDIUM_TEXT, alignment=TA_CENTER, spaceAfter=6)))

    story.append(Spacer(1, 10 * mm))
    story.append(hr())
    story.append(Spacer(1, 6 * mm))

    # Hook
    story.append(Paragraph(
        "What if you knew exactly how much was coming in next month?",
        make_style("cover_hook", fontName="Lexend-SemiBold", fontSize=12, leading=16,
                    textColor=ACCENT_BLUE, alignment=TA_CENTER, spaceAfter=8)))

    story.append(Spacer(1, 4 * mm))

    # What's inside
    story.append(Paragraph(
        "What\u2019s inside:",
        make_style("cover_inside_h", fontName="Lexend-SemiBold", fontSize=11, leading=15,
                    textColor=DARK_TEXT, alignment=TA_CENTER, spaceAfter=6)))

    inside_items = [
        "Why unpredictable income keeps churches in survival mode",
        "The 3 types of church income (and which one matters most)",
        "Why pledge drives fail \u2014 and what to do instead",
        "A free 6-step method to build predictable income today",
        "What automated recurring giving looks like in practice",
        "A self-assessment calculator for your church",
    ]
    for item in inside_items:
        story.append(Paragraph(
            f'\u2022  {item}',
            make_style(f"ci_{id(item)}", fontSize=9.5, leading=14, textColor=MEDIUM_TEXT,
                        alignment=TA_CENTER, spaceAfter=3)))

    story.append(Spacer(1, 12 * mm))

    story.append(Paragraph(
        "A free planning guide for church leaders by Algolog Limited  |  autogiving.ng",
        make_style("cover_tag", fontName="Lexend-Light", fontSize=9, leading=12,
                    textColor=LIGHT_TEXT, alignment=TA_CENTER)))

    story.append(PageBreak())

    # =====================================================
    # PAGE 2: THE COST OF UNPREDICTABLE INCOME
    # =====================================================

    story.append(Paragraph("THE COST OF UNPREDICTABLE INCOME", S_H1))
    story.append(hr())

    story.append(Paragraph(
        "Every church has ambitions. Hire more staff. Start a building project. Fund missions. "
        "Expand the children\u2019s ministry. Support community outreach. These are not luxuries "
        "\u2014 they are the work of the church.",
        S_BODY))

    story.append(Paragraph(
        "But most churches cannot commit to any of these because they do not know what next month\u2019s "
        "income will be. When the offering varies by 30\u201340% from one Sunday to the next, every plan "
        "becomes a gamble, and every budget becomes a guess.",
        S_BODY))

    story.append(Paragraph(
        "The result: churches operate in survival mode \u2014 paying bills month to month, never truly "
        "investing in growth. Leaders spend their energy managing cash flow instead of fulfilling vision.",
        S_BODY))

    story.append(Spacer(1, 2 * mm))
    story.append(Paragraph(
        "Here are the conversations happening in church offices across Nigeria right now:",
        make_style("conv_h", fontName="Lexend-SemiBold", fontSize=10, leading=14,
                    textColor=DARK_TEXT, spaceAfter=4)))

    conversations = [
        "\u201CWe want to hire a youth pastor, but we are not sure we can sustain the salary.\u201D",
        "\u201CWe started the building project, but had to pause because giving dropped for two months.\u201D",
        "\u201CWe promised the missionaries monthly support, but some months we can barely cover our own rent.\u201D",
        "\u201CWe approved the outreach programme in January, but by March we had to scale it back.\u201D",
    ]
    for c in conversations:
        story.append(Paragraph(f"\u2022  {c}", S_BULLET))

    story.append(Spacer(1, 3 * mm))

    story.append(Paragraph(
        "These are not failures of faith or generosity. They are the natural consequence of a structural "
        "problem: <b>when 80% or more of your income comes from spontaneous, weekly offerings, every "
        "budget is a prayer.</b>",
        S_BODY))

    story.append(Spacer(1, 4 * mm))

    # Yellow callout — cost calculation
    cost_title = Paragraph(
        '<font face="Lexend-SemiBold" color="#b7791f">What it looks like in numbers:</font>',
        make_style("cost_h", fontSize=10, leading=14, textColor=DARK_TEXT, spaceAfter=4))

    cost_body = Paragraph(
        '<font face="Lexend" color="#333333">'
        'A church averaging <b>NGN 4M/month</b> in offerings with 80% coming from unpredictable '
        'sources has only <b>NGN 800K</b> it can actually count on. The other <b>NGN 3.2M</b> might '
        'come... or it might not.</font>',
        make_style("cost_b", fontSize=9.5, leading=14, textColor=MEDIUM_TEXT, spaceAfter=6))

    cost_punchline = Paragraph(
        '<font face="Lexend-Bold" color="#1a1a1a">'
        'That is not a budget \u2014 it is a hope.</font>',
        make_style("cost_p", fontSize=10, leading=14, textColor=DARK_TEXT, alignment=TA_CENTER, spaceAfter=0))

    cost_box = callout_box([cost_title, cost_body, cost_punchline], YELLOW_LIGHT, ORANGE_ACCENT)
    story.append(cost_box)

    story.append(PageBreak())

    # =====================================================
    # PAGE 3: THE 3 TYPES OF CHURCH INCOME
    # =====================================================

    story.append(Paragraph("THE 3 TYPES OF CHURCH INCOME", S_H1))
    story.append(hr())

    story.append(Paragraph(
        "Understanding your income mix is the first step toward financial stability. Not all church "
        "income is equal \u2014 and the difference matters enormously for planning.",
        S_BODY))

    story.append(Spacer(1, 4 * mm))

    # Type 1 — Red callout
    t1_elements = [
        Paragraph(
            '<font face="Lexend-Bold" color="#c0392b" size="11">Type 1: Spontaneous Giving</font>',
            make_style("t1_h", fontSize=11, leading=15, textColor=RED_ACCENT, spaceAfter=4)),
        Paragraph(
            "One-time offerings, visitor gifts, special Sunday appeals. This income is <b>completely "
            "unpredictable.</b> It depends on attendance, mood, personal circumstances, and whether "
            "it rained on Sunday morning.",
            make_style("t1_b1", fontSize=9, leading=13, textColor=MEDIUM_TEXT, spaceAfter=4)),
        Paragraph(
            "Important for engagement, but <b>dangerous as a primary income source.</b>",
            make_style("t1_b2", fontSize=9, leading=13, textColor=MEDIUM_TEXT, spaceAfter=0)),
    ]
    story.append(callout_box(t1_elements, RED_LIGHT, RED_ACCENT))

    story.append(Spacer(1, 4 * mm))

    # Type 2 — Orange callout
    t2_elements = [
        Paragraph(
            '<font face="Lexend-Bold" color="#e67e22" size="11">Type 2: Seasonal Giving</font>',
            make_style("t2_h", fontSize=11, leading=15, textColor=ORANGE_ACCENT, spaceAfter=4)),
        Paragraph(
            "Harvest thanksgiving, Christmas, Easter, special project fundraisers. The timing is "
            "predictable, but the amounts are not.",
            make_style("t2_b1", fontSize=9, leading=13, textColor=MEDIUM_TEXT, spaceAfter=4)),
        Paragraph(
            "This often creates a <b>\u201Cfeast and famine\u201D cycle</b> \u2014 a huge December "
            "followed by a dry January and February. Churches that depend heavily on seasonal giving "
            "live on a financial rollercoaster.",
            make_style("t2_b2", fontSize=9, leading=13, textColor=MEDIUM_TEXT, spaceAfter=0)),
    ]
    story.append(callout_box(t2_elements, ORANGE_LIGHT, ORANGE_ACCENT))

    story.append(Spacer(1, 4 * mm))

    # Type 3 — Green callout
    t3_elements = [
        Paragraph(
            '<font face="Lexend-Bold" color="#27ae60" size="11">Type 3: Committed Recurring Giving</font>',
            make_style("t3_h", fontSize=11, leading=15, textColor=GREEN, spaceAfter=4)),
        Paragraph(
            "The same amount, the same frequency, every week or every month, automatically. Rain or "
            "shine. Travel or not. <b>This is the floor</b> \u2014 the income you KNOW will arrive "
            "regardless of attendance, weather, or holidays.",
            make_style("t3_b1", fontSize=9, leading=13, textColor=MEDIUM_TEXT, spaceAfter=4)),
        Paragraph(
            "<b>The healthiest churches worldwide have 50\u201370% of income from Type 3.</b> Most Nigerian "
            "churches have less than 10% from committed recurring giving.",
            make_style("t3_b2", fontSize=9, leading=13, textColor=MEDIUM_TEXT, spaceAfter=0)),
    ]
    story.append(callout_box(t3_elements, GREEN_LIGHT, GREEN))

    story.append(Spacer(1, 5 * mm))

    # Ideal mix table
    story.append(Paragraph("The ideal income mix:", S_H3))
    story.append(Spacer(1, 1 * mm))

    mix_header_s = make_style("mix_th", fontName="Lexend-Bold", fontSize=8.5, leading=12, textColor=WHITE)
    mix_cell_s = make_style("mix_tc", fontSize=9, leading=12, textColor=MEDIUM_TEXT)
    mix_cell_b = make_style("mix_tcb", fontName="Lexend-Bold", fontSize=9, leading=12, textColor=DARK_TEXT)

    mix_data = [
        [Paragraph("<b>Income Type</b>", mix_header_s),
         Paragraph("<b>Ideal %</b>", mix_header_s),
         Paragraph("<b>What It Provides</b>", mix_header_s)],
        [Paragraph("Committed Recurring", mix_cell_b),
         Paragraph("50\u201360%", mix_cell_b),
         Paragraph("Your predictable floor \u2014 budget with confidence", mix_cell_s)],
        [Paragraph("Spontaneous", mix_cell_s),
         Paragraph("20\u201330%", mix_cell_s),
         Paragraph("Engagement and growth \u2014 visitors, special moments", mix_cell_s)],
        [Paragraph("Seasonal", mix_cell_s),
         Paragraph("10\u201320%", mix_cell_s),
         Paragraph("Special projects and celebrations", mix_cell_s)],
    ]
    mix_table = Table(mix_data, colWidths=[AVAIL_W * 0.28, AVAIL_W * 0.15, AVAIL_W * 0.57])
    mix_table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), TABLE_HEADER_BG),
        ("TEXTCOLOR", (0, 0), (-1, 0), WHITE),
        ("BACKGROUND", (0, 2), (-1, 2), TABLE_ALT_ROW),
        ("FONTNAME", (0, 0), (-1, -1), "Lexend"),
        ("FONTSIZE", (0, 0), (-1, -1), 9),
        ("ALIGN", (1, 0), (1, -1), "CENTER"),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("TOPPADDING", (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
        ("LEFTPADDING", (0, 0), (-1, -1), 8),
        ("RIGHTPADDING", (0, 0), (-1, -1), 8),
        ("GRID", (0, 0), (-1, -1), 0.5, BORDER_COLOR),
    ]))
    story.append(mix_table)

    story.append(Spacer(1, 4 * mm))

    # Key insight quote
    insight_para = Paragraph(
        '\u201CThe goal is not to eliminate spontaneous or seasonal giving. It is to build a '
        'predictable floor so your church can plan with confidence.\u201D',
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

    story.append(PageBreak())

    # =====================================================
    # PAGE 4: THE PLEDGE GAP
    # =====================================================

    story.append(Paragraph("THE PLEDGE GAP \u2014 WHY GOOD INTENTIONS DON\u2019T PAY BILLS", S_H1))
    story.append(hr())

    story.append(Paragraph(
        "Many churches have tried \u201Cpledge drives\u201D or \u201Cfaith promises\u201D \u2014 asking "
        "members to commit to a monthly amount. The intention is right. The execution breaks down.",
        S_BODY))

    story.append(Spacer(1, 2 * mm))

    # Red callout — the stat
    stat_para = Paragraph(
        '<font face="Lexend-Bold" color="#c0392b" size="12">The reality: 40\u201360% of verbal '
        'pledges go unfulfilled.</font>',
        make_style("stat_p", fontSize=12, leading=16, textColor=RED_ACCENT, alignment=TA_CENTER, spaceAfter=0))
    stat_box = callout_box([stat_para], RED_LIGHT, RED_ACCENT)
    story.append(stat_box)

    story.append(Spacer(1, 4 * mm))
    story.append(Paragraph("Why pledges fail:", S_H2))

    # 5 reasons with numbered badges
    pledge_reasons = [
        ("Life gets busy.",
         "The intention was real when the pledge card was filled out. But there is no system to "
         "execute it. Monday comes, the week gets hectic, and the pledge is forgotten by Wednesday."),
        ("No reminder mechanism.",
         "The pledge card sits in a drawer or gets lost. There is nothing prompting the member to "
         "act on their commitment when the time comes."),
        ("Giving is still manual.",
         "Even committed members forget some weeks. Manual giving requires a conscious decision "
         "every single time \u2014 and that is a lot of decisions over a year."),
        ("No accountability loop.",
         "The church does not know who is behind until months later when the finance team "
         "reconciles. By then, the moment to follow up has passed."),
        ("Embarrassment.",
         "Members who fall behind on their pledges feel ashamed. Instead of catching up, they "
         "disengage further. The pledge that was meant to increase giving actually reduces it."),
    ]

    for i, (title, body) in enumerate(pledge_reasons, 1):
        story.append(step_row(i, RED_ACCENT, title, body))
        story.append(Spacer(1, 2 * mm))

    story.append(Spacer(1, 4 * mm))

    # Key insight quote
    gap_quote = Paragraph(
        '\u201CThe problem is not the commitment. The problem is the gap between intention and '
        'execution. Good systems close that gap.\u201D',
        S_QUOTE)
    gap_box = Table([[gap_quote]], colWidths=[AVAIL_W - 30])
    gap_box.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), HexColor("#f8f9fa")),
        ("TOPPADDING", (0, 0), (-1, -1), 10),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 10),
        ("LEFTPADDING", (0, 0), (-1, -1), 16),
        ("RIGHTPADDING", (0, 0), (-1, -1), 16),
        ("BOX", (0, 0), (-1, -1), 1.5, ACCENT_BLUE),
    ]))
    gap_box.hAlign = "CENTER"
    story.append(gap_box)

    story.append(PageBreak())

    # =====================================================
    # PAGE 5: THE FREE FIX
    # =====================================================

    story.append(Paragraph("THE FREE FIX \u2014 BUILDING PREDICTABLE INCOME WITHOUT SOFTWARE", S_H1))
    story.append(hr())

    story.append(Paragraph(
        "You do not need to buy any software to start solving this. Here are six steps you can "
        "implement this month:",
        S_BODY))

    story.append(Spacer(1, 3 * mm))

    # Blue callout — step-by-step
    free_steps = [
        ("Identify your committed core.",
         "Look at your giving records for the past 6 months. Find your top 20\u201330 consistent "
         "givers \u2014 the people who give every Sunday regardless. They have already proven their "
         "faithfulness. They just need a better system."),
        ("Have personal conversations.",
         "This is NOT a public announcement. It is a personal, one-on-one conversation. Say: "
         "\u201CWe are trying to build a more predictable foundation for the church. Would you be "
         "open to setting up a monthly standing order with your bank for your tithe? It is "
         "completely voluntary.\u201D"),
        ("Help them set it up.",
         "Most Nigerian banks offer free standing orders. Provide the church account details and "
         "walk them through the process. Remove every friction point. If possible, have someone "
         "available after service to help."),
        ("Track commitments in a simple spreadsheet.",
         "Columns: Member Name | Monthly Amount | Bank | Standing Order Set Up? | Jan | Feb | Mar... "
         "Track who committed and who has actually started."),
        ("Review monthly.",
         "Check which standing orders actually came through. Follow up gently with anyone who "
         "committed but has not started. A simple WhatsApp message is enough: \u201CJust checking "
         "in \u2014 is everything okay with the standing order?\u201D"),
        ("Calculate your predictable floor.",
         "Total of all active, confirmed standing orders. This is the amount you can actually "
         "budget against with confidence."),
    ]

    step_elements = [
        Paragraph(
            '<font face="Lexend-SemiBold" color="#0f3460">Your free 6-step method:</font>',
            make_style("free_h", fontSize=10, leading=14, textColor=ACCENT_BLUE, spaceAfter=6)),
    ]
    for i, (title, body) in enumerate(free_steps, 1):
        step_elements.append(step_row(i, ACCENT_BLUE, title, body))
        step_elements.append(Spacer(1, 1 * mm))

    free_box = callout_box(step_elements, BLUE_LIGHT)
    story.append(free_box)

    story.append(Spacer(1, 3 * mm))

    # Impact calculation — green callout
    impact_para = Paragraph(
        '<font face="Lexend-SemiBold" color="#27ae60">The impact:</font>  '
        '<font face="Lexend" color="#333333">'
        'If <b>25 members</b> commit to an average of <b>NGN 50,000/month</b>, that is '
        '<b>NGN 1.25 million</b> in predictable monthly income. That is enough to hire a staff '
        'member, fund a mission, or start a building savings plan \u2014 with confidence.</font>',
        make_style("impact_p", fontSize=9, leading=13, textColor=MEDIUM_TEXT, spaceAfter=0))
    impact_box = callout_box([impact_para], GREEN_LIGHT, GREEN)
    story.append(impact_box)

    story.append(Spacer(1, 3 * mm))

    # Honest note — orange callout
    honest_para = Paragraph(
        '<font face="Lexend-SemiBold" color="#b7791f">An honest note:</font>  '
        '<font face="Lexend" color="#333333">'
        'Standing orders are a good start, but they have real limitations in Nigeria. Banks '
        'sometimes miss payments without explanation. Members cannot easily adjust amounts if their '
        'circumstances change \u2014 they have to visit the bank or call. There is no receipt or '
        'category tracking (the church cannot tell tithes from offerings from building fund). And '
        'you are still manually following up every month. '
        'It works for your first 20\u201330 committed givers \u2014 but it does not scale, and it '
        'breaks when banks fail.</font>',
        make_style("honest_p", fontSize=8.5, leading=12, textColor=MEDIUM_TEXT, spaceAfter=0))
    honest_box = Table([[honest_para]], colWidths=[AVAIL_W - 20])
    honest_box.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), ORANGE_LIGHT),
        ("TOPPADDING", (0, 0), (-1, -1), 8),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
        ("LEFTPADDING", (0, 0), (-1, -1), 12),
        ("RIGHTPADDING", (0, 0), (-1, -1), 12),
        ("BOX", (0, 0), (-1, -1), 1, ORANGE_ACCENT),
    ]))
    story.append(honest_box)

    story.append(PageBreak())

    # =====================================================
    # PAGE 6: THE AUTOMATED FIX
    # =====================================================

    story.append(Paragraph("THE AUTOMATED FIX \u2014 WHAT TRULY PREDICTABLE GIVING LOOKS LIKE", S_H1))
    story.append(hr())

    story.append(Paragraph(
        "Here is what giving looks like when there is a proper system behind it:",
        S_BODY))

    story.append(Spacer(1, 3 * mm))

    # Green callout — automated steps
    auto_items = [
        ("Your church gets a branded giving link.",
         "autogiving.ng/yourchurch \u2014 with your church name, logo, and colours. Share it once "
         "from the pulpit, in the WhatsApp group, on your church website."),
        ("Members choose a category and set their giving.",
         "Tithes, Offerings, Building Fund, Missions \u2014 whatever categories your church has set "
         "up. They choose an amount and frequency (weekly or monthly)."),
        ("First payment goes through, card is securely saved.",
         "From then on, giving is automatic. Every week or every month. Whether they attend or not. "
         "Whether it rains or not. Whether they are in Abuja or Lagos or London."),
        ("Your dashboard shows your predictable floor.",
         "\u201C42 members have active recurring subscriptions totaling NGN 2.8M/month.\u201D That is "
         "your predictable floor. Budget against it with confidence."),
        ("Members control their own giving.",
         "If a member needs to pause (travel, financial hardship), they do it themselves online \u2014 "
         "no awkward conversation needed. They can resume whenever they are ready."),
        ("Automatic receipts and full visibility.",
         "Members get email and SMS receipts after every transaction. The church sees total recurring "
         "vs one-time giving, giving by category, trends over time. Export to CSV anytime."),
        ("Funds go directly to your church bank account.",
         "Never touches Algolog or any other account. Paystack subaccount technology ensures direct "
         "settlement to your church\u2019s own bank account."),
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

    # Pledged product callout (dark blue box)
    pledged_para = Paragraph(
        '<font face="Lexend-SemiBold" color="#ffffff" size="10">'
        'This is Pledged \u2014 your members set it up once, and giving continues rain or shine, '
        'holiday or not.</font><br/><br/>'
        '<font face="Lexend" color="#e0e0e0" size="9">'
        'No forgotten standing orders. No manual tracking. No awkward follow-ups. No bank failures '
        'to chase. Just predictable income your church can plan around.</font>',
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
    # PAGE 7: CALCULATOR + SELF-ASSESSMENT + CTA
    # =====================================================

    story.append(Paragraph("THE PREDICTABLE CHURCH CALCULATOR", S_H1))
    story.append(hr())

    story.append(Paragraph(
        "Use this worksheet to see where your church stands today \u2014 and what changes with "
        "recurring giving:",
        S_BODY))

    story.append(Spacer(1, 2 * mm))

    # Calculator table
    calc_th = make_style("calc_th", fontName="Lexend-Bold", fontSize=8, leading=11, textColor=WHITE)
    calc_tc = make_style("calc_tc", fontSize=8, leading=11, textColor=MEDIUM_TEXT, alignment=TA_CENTER)
    calc_tcb = make_style("calc_tcb", fontName="Lexend-Bold", fontSize=8, leading=11, textColor=DARK_TEXT, alignment=TA_CENTER)
    calc_tl = make_style("calc_tl", fontName="Lexend-SemiBold", fontSize=8, leading=11, textColor=DARK_TEXT)

    calc_data = [
        [Paragraph("", calc_th),
         Paragraph("<b>Current</b>", calc_th),
         Paragraph("<b>With 25 Recurring</b>", calc_th),
         Paragraph("<b>With 50 Recurring</b>", calc_th)],
        [Paragraph("Avg Monthly Offering", calc_tl),
         Paragraph("NGN _______", calc_tc),
         Paragraph("NGN _______", calc_tc),
         Paragraph("NGN _______", calc_tc)],
        [Paragraph("Predictable (Recurring)", calc_tl),
         Paragraph("NGN _______ (____%)", calc_tc),
         Paragraph("NGN _______ (____%)", calc_tc),
         Paragraph("NGN _______ (____%)", calc_tc)],
        [Paragraph("Unpredictable", calc_tl),
         Paragraph("NGN _______ (____%)", calc_tc),
         Paragraph("NGN _______ (____%)", calc_tc),
         Paragraph("NGN _______ (____%)", calc_tc)],
        [Paragraph("Budget Confidently?", calc_tl),
         Paragraph("?", calc_tcb),
         Paragraph("Getting there", calc_tcb),
         Paragraph("Yes", calc_tcb)],
    ]
    calc_table = Table(calc_data, colWidths=[AVAIL_W * 0.28, AVAIL_W * 0.24, AVAIL_W * 0.24, AVAIL_W * 0.24])
    calc_table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), TABLE_HEADER_BG),
        ("TEXTCOLOR", (0, 0), (-1, 0), WHITE),
        ("BACKGROUND", (0, 2), (-1, 2), TABLE_ALT_ROW),
        ("BACKGROUND", (0, 4), (-1, 4), TABLE_ALT_ROW),
        ("FONTNAME", (0, 0), (-1, -1), "Lexend"),
        ("FONTSIZE", (0, 0), (-1, -1), 8),
        ("ALIGN", (1, 0), (-1, -1), "CENTER"),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("TOPPADDING", (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
        ("LEFTPADDING", (0, 0), (-1, -1), 6),
        ("RIGHTPADDING", (0, 0), (-1, -1), 6),
        ("GRID", (0, 0), (-1, -1), 0.5, BORDER_COLOR),
    ]))
    story.append(calc_table)

    story.append(Spacer(1, 5 * mm))

    # Self-assessment
    story.append(Paragraph("SELF-ASSESSMENT: IS YOUR CHURCH INCOME PREDICTABLE?", S_H2))
    story.append(Paragraph(
        "Answer these five statements honestly. Count how many are true for your church.",
        S_BODY))

    story.append(Spacer(1, 2 * mm))

    # Scorecard table
    score_data = [
        [Paragraph("<b>#</b>", S_TABLE_HEADER),
         Paragraph("<b>Statement</b>", S_TABLE_HEADER),
         Paragraph("<b>Yes / No</b>", S_TABLE_HEADER)],
        [Paragraph("1", S_TABLE_CELL_BOLD),
         Paragraph("Our church budget is based on estimates, not committed income", S_TABLE_CELL),
         Paragraph("", S_TABLE_CELL)],
        [Paragraph("2", S_TABLE_CELL_BOLD),
         Paragraph("We have had to delay or cancel a project because giving was lower than expected", S_TABLE_CELL),
         Paragraph("", S_TABLE_CELL)],
        [Paragraph("3", S_TABLE_CELL_BOLD),
         Paragraph("We do not know what percentage of our income is recurring vs one-time", S_TABLE_CELL),
         Paragraph("", S_TABLE_CELL)],
        [Paragraph("4", S_TABLE_CELL_BOLD),
         Paragraph("We have tried pledge drives but most pledges went unfulfilled", S_TABLE_CELL),
         Paragraph("", S_TABLE_CELL)],
        [Paragraph("5", S_TABLE_CELL_BOLD),
         Paragraph("We cannot tell members exactly how much they gave last year if they ask", S_TABLE_CELL),
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

    story.append(Spacer(1, 4 * mm))
    story.append(Paragraph("Your score:", S_H3))

    # Score interpretation boxes
    scores = [
        ("0\u20131", "#27ae60", GREEN_LIGHT,
         "Your church is in good shape. You likely already have systems supporting predictable "
         "income. Automation would save your team time and give members a better experience."),
        ("2\u20133", "#e67e22", ORANGE_LIGHT,
         "There are gaps in your giving infrastructure. The free fix on the previous page will make "
         "an immediate difference. Automation would transform your financial planning."),
        ("4\u20135", "#c0392b", RED_LIGHT,
         "Your church is operating without a predictable income floor. Every budget is a guess. "
         "This is the single most impactful thing you can address \u2014 and it starts with helping "
         "your members give consistently."),
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

    story.append(PageBreak())

    # --- CTA PAGE ---
    story.append(Spacer(1, 8 * mm))
    story.append(Paragraph(
        "FREE 15-MINUTE CHURCH GIVING AUDIT",
        make_style("cta_h", fontName="Lexend-Bold", fontSize=14, leading=18,
                    textColor=ACCENT_BLUE, alignment=TA_CENTER, spaceAfter=6)))

    # Scarcity
    scarcity_para = Paragraph(
        'We only do <b>10 of these per month</b>, so we can give each church our full attention.',
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
        "In 15 minutes, we\u2019ll look at your current giving patterns, identify the biggest gaps "
        "between intention and execution, and show you exactly what a recurring giving system would "
        "look like for your church \u2014 branded with your name, logo, and colours.",
        S_BODY_CENTER))

    story.append(Paragraph(
        "No obligation. No pressure. Just a conversation about what is possible for your church.",
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
        "This guide was prepared by <b>Algolog Limited</b>, a Nigerian technology company that "
        "builds tools to help churches and organisations operate more effectively. Our platform, "
        "<b>Pledged</b> (autogiving.ng), enables churches to set up branded recurring giving "
        "in minutes \u2014 no app download needed, funds go directly to the church\u2019s bank account.",
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
