"""
Generate Pledged Lead Magnet #1 PDF:
"Why Your Offering Drops Every Holiday: The Attendance-Revenue Trap Every Church Faces"
Format: Algolog brand styling (banner header, Lexend font, colored callout boxes, number badges)
"""

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import inch, mm
from reportlab.lib.colors import HexColor, white, black
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY, TA_RIGHT
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Image, Table, TableStyle,
    PageBreak, HRFlowable, KeepTogether, Flowable
)
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.graphics.shapes import Drawing, Circle, String
import os

# --- Paths ---
BASE = "C:/Users/Femi Fayinminu/OneDrive/Documents/Algolog/Algolog_Projects"
FONT_DIR = os.path.join(BASE, "fonts/lexend-main/fonts/lexend/ttf")
BANNER_PATH = os.path.join(BASE, "claude.ai contex/banner_centered.png")
OUTPUT_PATH = os.path.join(BASE, "Proposals/Lead-Magnet-Pledged-Holiday-Offering.pdf")

# --- Register Lexend Fonts ---
pdfmetrics.registerFont(TTFont("Lexend", os.path.join(FONT_DIR, "Lexend-Regular.ttf")))
pdfmetrics.registerFont(TTFont("Lexend-Bold", os.path.join(FONT_DIR, "Lexend-Bold.ttf")))
pdfmetrics.registerFont(TTFont("Lexend-SemiBold", os.path.join(FONT_DIR, "Lexend-SemiBold.ttf")))
pdfmetrics.registerFont(TTFont("Lexend-Light", os.path.join(FONT_DIR, "Lexend-Light.ttf")))
pdfmetrics.registerFont(TTFont("Lexend-Medium", os.path.join(FONT_DIR, "Lexend-Medium.ttf")))

pdfmetrics.registerFontFamily(
    "Lexend",
    normal="Lexend",
    bold="Lexend-Bold",
    italic="Lexend",
    boldItalic="Lexend-Bold",
)

# --- Colors ---
ACCENT_BLUE = HexColor("#0f3460")
DARK_TEXT = HexColor("#1a1a1a")
MEDIUM_TEXT = HexColor("#333333")
LIGHT_TEXT = HexColor("#555555")
GREEN = HexColor("#27ae60")
GREEN_LIGHT = HexColor("#eafaf1")
RED_ACCENT = HexColor("#c0392b")
RED_LIGHT = HexColor("#fdedec")
ORANGE_ACCENT = HexColor("#e67e22")
ORANGE_LIGHT = HexColor("#fef5e7")
BLUE_LIGHT = HexColor("#eaf2f8")
YELLOW_LIGHT = HexColor("#fef9e7")
YELLOW_ACCENT = HexColor("#f39c12")
BORDER_COLOR = HexColor("#dcdde1")
TABLE_HEADER_BG = HexColor("#1a1a2e")
TABLE_ALT_ROW = HexColor("#f5f6fa")
DARK_BG = HexColor("#1a1a2e")

# --- Page Setup ---
PAGE_W, PAGE_H = A4
LEFT_MARGIN = 22 * mm
RIGHT_MARGIN = 22 * mm
TOP_MARGIN = 20 * mm
BOTTOM_MARGIN = 18 * mm

# --- Styles ---
styles = getSampleStyleSheet()


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


S_H1 = make_style("S_H1", fontName="Lexend-Bold", fontSize=15, leading=20, textColor=ACCENT_BLUE, spaceBefore=18, spaceAfter=8)
S_H2 = make_style("S_H2", fontName="Lexend-SemiBold", fontSize=12, leading=16, textColor=DARK_TEXT, spaceBefore=12, spaceAfter=6)
S_H3 = make_style("S_H3", fontName="Lexend-SemiBold", fontSize=11, leading=14, textColor=MEDIUM_TEXT, spaceBefore=8, spaceAfter=4)
S_BODY = make_style("S_BODY", fontSize=9.5, leading=14, textColor=MEDIUM_TEXT, alignment=TA_JUSTIFY, spaceAfter=6)
S_BODY_BOLD = make_style("S_BODY_BOLD", fontName="Lexend-Bold", fontSize=9.5, leading=14, textColor=DARK_TEXT, spaceAfter=6)
S_BULLET = make_style("S_BULLET", fontSize=9.5, leading=14, textColor=MEDIUM_TEXT, leftIndent=18, bulletIndent=6, spaceAfter=4)
S_NUMBEREDITEM = make_style("S_NUMBEREDITEM", fontSize=9.5, leading=14, textColor=MEDIUM_TEXT, leftIndent=18, bulletIndent=6, spaceAfter=4)
S_SMALL = make_style("S_SMALL", fontSize=8, leading=11, textColor=LIGHT_TEXT, alignment=TA_CENTER)
S_HEADER_INFO = make_style("S_HEADER_INFO", fontName="Lexend-Light", fontSize=8.5, leading=12, textColor=LIGHT_TEXT, alignment=TA_CENTER)
S_TABLE_HEADER = make_style("S_TABLE_HEADER", fontName="Lexend-Bold", fontSize=9, leading=12, textColor=HexColor("#ffffff"))
S_TABLE_CELL = make_style("S_TABLE_CELL", fontSize=9, leading=12, textColor=MEDIUM_TEXT)
S_TABLE_CELL_BOLD = make_style("S_TABLE_CELL_BOLD", fontName="Lexend-Bold", fontSize=9, leading=12, textColor=DARK_TEXT)


# --- Custom Flowables ---

class CalloutBox(Flowable):
    """A colored callout box with optional title and body text."""

    def __init__(self, text, bg_color, border_color, width, title=None, title_color=None, padding=12):
        Flowable.__init__(self)
        self.text = text
        self.bg_color = bg_color
        self.border_color = border_color
        self.box_width = width
        self.title = title
        self.title_color = title_color or DARK_TEXT
        self.padding = padding
        self._fixed_height = None

    def wrap(self, availWidth, availHeight):
        self.box_width = min(self.box_width, availWidth)
        inner_width = self.box_width - 2 * self.padding

        total_h = self.padding  # top padding

        if self.title:
            title_style = ParagraphStyle(
                "callout_title_measure",
                fontName="Lexend-SemiBold",
                fontSize=10,
                leading=14,
                textColor=self.title_color,
            )
            title_para = Paragraph(self.title, title_style)
            tw, th = title_para.wrap(inner_width, 999)
            total_h += th + 6

        body_style = ParagraphStyle(
            "callout_body_measure",
            fontName="Lexend",
            fontSize=9.5,
            leading=14,
            textColor=MEDIUM_TEXT,
            alignment=TA_JUSTIFY,
        )
        body_para = Paragraph(self.text, body_style)
        bw, bh = body_para.wrap(inner_width, 999)
        total_h += bh + self.padding  # body + bottom padding

        self._fixed_height = total_h
        return self.box_width, total_h

    def draw(self):
        canvas = self.canv
        w = self.box_width
        h = self._fixed_height
        p = self.padding

        # Background
        canvas.setFillColor(self.bg_color)
        canvas.setStrokeColor(self.border_color)
        canvas.setLineWidth(1.5)
        canvas.roundRect(0, 0, w, h, radius=6, fill=1, stroke=1)

        # Left accent bar
        canvas.setFillColor(self.border_color)
        canvas.rect(0, 0, 4, h, fill=1, stroke=0)

        inner_width = w - 2 * p
        y_cursor = h - p

        if self.title:
            title_style = ParagraphStyle(
                "callout_title_draw",
                fontName="Lexend-SemiBold",
                fontSize=10,
                leading=14,
                textColor=self.title_color,
            )
            title_para = Paragraph(self.title, title_style)
            tw, th = title_para.wrap(inner_width, 999)
            title_para.drawOn(canvas, p, y_cursor - th)
            y_cursor -= th + 6

        body_style = ParagraphStyle(
            "callout_body_draw",
            fontName="Lexend",
            fontSize=9.5,
            leading=14,
            textColor=MEDIUM_TEXT,
            alignment=TA_JUSTIFY,
        )
        body_para = Paragraph(self.text, body_style)
        bw, bh = body_para.wrap(inner_width, 999)
        body_para.drawOn(canvas, p, y_cursor - bh)


class NumberBadge(Flowable):
    """A colored circle with a number, followed by text."""

    def __init__(self, number, text, circle_color, width, text_style=None):
        Flowable.__init__(self)
        self.number = str(number)
        self.text = text
        self.circle_color = circle_color
        self.box_width = width
        self.text_style = text_style or S_BODY
        self.circle_size = 22
        self._fixed_height = None

    def wrap(self, availWidth, availHeight):
        self.box_width = min(self.box_width, availWidth)
        text_width = self.box_width - self.circle_size - 14
        para = Paragraph(self.text, self.text_style)
        pw, ph = para.wrap(text_width, 999)
        self._fixed_height = max(ph, self.circle_size) + 4
        return self.box_width, self._fixed_height

    def draw(self):
        canvas = self.canv
        cs = self.circle_size
        h = self._fixed_height

        # Circle
        cx = cs / 2
        cy = h - cs / 2 - 2
        canvas.setFillColor(self.circle_color)
        canvas.circle(cx, cy, cs / 2, fill=1, stroke=0)

        # Number in circle
        canvas.setFillColor(white)
        canvas.setFont("Lexend-Bold", 10)
        canvas.drawCentredString(cx, cy - 3.5, self.number)

        # Text
        text_width = self.box_width - cs - 14
        para = Paragraph(self.text, self.text_style)
        pw, ph = para.wrap(text_width, 999)
        para.drawOn(canvas, cs + 12, h - ph - 2)


class ScoreBar(Flowable):
    """A colored score interpretation bar."""

    def __init__(self, label, description, bar_color, text_color, width):
        Flowable.__init__(self)
        self.label = label
        self.description = description
        self.bar_color = bar_color
        self.text_color = text_color
        self.box_width = width
        self._fixed_height = None

    def wrap(self, availWidth, availHeight):
        self.box_width = min(self.box_width, availWidth)
        desc_style = ParagraphStyle("sb_measure", fontName="Lexend", fontSize=9, leading=13, textColor=MEDIUM_TEXT)
        p = Paragraph(self.description, desc_style)
        pw, ph = p.wrap(self.box_width - 90, 999)
        self._fixed_height = max(ph, 24) + 10
        return self.box_width, self._fixed_height

    def draw(self):
        canvas = self.canv
        h = self._fixed_height
        w = self.box_width

        # Label badge
        canvas.setFillColor(self.bar_color)
        canvas.roundRect(0, h / 2 - 11, 72, 22, radius=4, fill=1, stroke=0)
        canvas.setFillColor(white)
        canvas.setFont("Lexend-Bold", 9)
        canvas.drawCentredString(36, h / 2 - 4, self.label)

        # Description
        desc_style = ParagraphStyle("sb_draw", fontName="Lexend", fontSize=9, leading=13, textColor=self.text_color)
        p = Paragraph(self.description, desc_style)
        pw, ph = p.wrap(w - 90, 999)
        p.drawOn(canvas, 82, (h - ph) / 2)


# --- Helper Functions ---

def hr():
    return HRFlowable(width="100%", thickness=0.5, color=BORDER_COLOR, spaceAfter=8, spaceBefore=8)


def add_footer(canvas_obj, doc):
    canvas_obj.saveState()
    canvas_obj.setFont("Lexend-Light", 7)
    canvas_obj.setFillColor(LIGHT_TEXT)
    canvas_obj.drawCentredString(
        PAGE_W / 2, 10 * mm,
        f"Algolog Limited  |  algolog.co  |  autogiving.ng  |  Page {doc.page}"
    )
    canvas_obj.restoreState()


# --- Build PDF ---

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
    if os.path.exists(BANNER_PATH):
        from PIL import Image as PILImage
        img = PILImage.open(BANNER_PATH)
        img_w, img_h = img.size
        aspect = img_h / img_w
        display_w = avail_w
        display_h = display_w * aspect
        banner = Image(BANNER_PATH, width=display_w, height=display_h)
        story.append(banner)

    story.append(Spacer(1, 18 * mm))
    story.append(hr())
    story.append(Spacer(1, 8 * mm))

    # Title
    story.append(Paragraph(
        "Why Your Offering Drops<br/>Every Holiday",
        make_style("cover_title", fontName="Lexend-Bold", fontSize=26, leading=32, textColor=ACCENT_BLUE, alignment=TA_CENTER, spaceAfter=6)
    ))
    story.append(Spacer(1, 3 * mm))

    # Subtitle
    story.append(Paragraph(
        "The Attendance-Revenue Trap Every Church Faces",
        make_style("cover_sub", fontName="Lexend-Medium", fontSize=13, leading=17, textColor=LIGHT_TEXT, alignment=TA_CENTER, spaceAfter=6)
    ))

    story.append(Spacer(1, 10 * mm))

    # Hook callout
    hook_box = CalloutBox(
        text="30% of your members missed last Sunday. So did 30% of your offering.",
        bg_color=BLUE_LIGHT,
        border_color=ACCENT_BLUE,
        width=avail_w * 0.85,
        title=None,
    )
    # Center the hook box using a table
    hook_table = Table([[hook_box]], colWidths=[avail_w])
    hook_table.setStyle(TableStyle([
        ("ALIGN", (0, 0), (0, 0), "CENTER"),
        ("VALIGN", (0, 0), (0, 0), "MIDDLE"),
        ("LEFTPADDING", (0, 0), (0, 0), avail_w * 0.075),
        ("RIGHTPADDING", (0, 0), (0, 0), avail_w * 0.075),
    ]))
    story.append(hook_table)

    story.append(Spacer(1, 14 * mm))
    story.append(hr())
    story.append(Spacer(1, 6 * mm))

    # Tag line
    story.append(Paragraph(
        "A free guide for church leaders by Algolog Limited  |  autogiving.ng",
        make_style("cover_tag", fontName="Lexend-Light", fontSize=9.5, leading=13, textColor=LIGHT_TEXT, alignment=TA_CENTER, spaceAfter=4)
    ))

    story.append(Spacer(1, 8 * mm))
    story.append(Paragraph(
        "March 2026",
        make_style("cover_date", fontName="Lexend-Medium", fontSize=10, textColor=LIGHT_TEXT, alignment=TA_CENTER)
    ))

    story.append(PageBreak())

    # =====================================================
    # PAGE 2: THE ATTENDANCE-REVENUE TRAP
    # =====================================================
    story.append(Paragraph("THE ATTENDANCE-REVENUE TRAP", S_H1))
    story.append(hr())

    story.append(Paragraph(
        "Every pastor knows the pattern. Holiday Sunday, rainy Sunday, long weekend \u2014 attendance drops, "
        "and so does the offering. It happens like clockwork: fewer people in the seats means less money in the basket.",
        S_BODY))

    story.append(Spacer(1, 2 * mm))
    story.append(Paragraph("The Math", S_H2))

    story.append(Paragraph(
        "If your church has <b>500 regular attendees</b> giving an average of <b>NGN 2,000 per Sunday</b>, "
        "a full Sunday brings in <b>NGN 1,000,000</b>.",
        S_BODY))

    story.append(Paragraph(
        "When <b>30% of your congregation misses</b> a single Sunday, you lose <b>NGN 300,000</b> that week. "
        "Not because people stopped caring \u2014 but because they were not physically present.",
        S_BODY))

    story.append(Spacer(1, 3 * mm))
    story.append(Paragraph(
        "And it is not just public holidays. Think about all the Sundays affected by:",
        S_BODY))

    reduced_reasons = [
        "<b>Travel season</b> (December/January) \u2014 families travel, attendance thins out for weeks",
        "<b>Rainy season Sundays</b> \u2014 heavy downpours keep members at home",
        "<b>Public holidays</b> \u2014 Independence Day, Democracy Day, Eid periods",
        "<b>Traffic and heat</b> \u2014 a hot Saturday night keeping people home Sunday morning",
        "<b>Personal travel</b> \u2014 work trips, family visits, weddings out of town",
    ]
    for item in reduced_reasons:
        story.append(Paragraph(f"\u2022  {item}", S_BULLET))

    story.append(Spacer(1, 3 * mm))
    story.append(Paragraph(
        "Count the reduced Sundays honestly: most churches experience <b>at least 10\u201315 Sundays per year</b> "
        "where attendance drops by 20\u201340%.",
        S_BODY))

    story.append(Spacer(1, 4 * mm))

    # Yellow callout box
    cost_callout = CalloutBox(
        title="What it\u2019s costing your church:",
        title_color=ORANGE_ACCENT,
        text="[Average Sunday offering] \u00d7 [% attendance drop] \u00d7 [Number of reduced Sundays per year]"
             "<br/><br/>"
             "For a church averaging NGN 1M per Sunday with 12 reduced Sundays at 30% drop: "
             "<br/><b>That is NGN 3.6 million per year that simply does not arrive.</b>",
        bg_color=YELLOW_LIGHT,
        border_color=YELLOW_ACCENT,
        width=avail_w,
    )
    story.append(cost_callout)

    story.append(PageBreak())

    # =====================================================
    # PAGE 3: WHY "JUST TRANSFER IT" DOESN'T WORK
    # =====================================================
    story.append(Paragraph("WHY \u201cJUST TRANSFER IT\u201d DOESN\u2019T WORK", S_H1))
    story.append(hr())

    story.append(Paragraph(
        "Most churches have tried the obvious solution: announce from the pulpit, \u201cIf you cannot attend "
        "next Sunday, please transfer your offering.\u201d",
        S_BODY))

    story.append(Spacer(1, 2 * mm))
    story.append(Paragraph("Why it consistently fails:", S_H2))
    story.append(Spacer(1, 2 * mm))

    transfer_failures = [
        (1, "<b>People forget.</b> Life happens. The intention is real on Sunday morning, but by Monday "
            "it has faded. By Tuesday, it is forgotten entirely."),
        (2, "<b>No dedicated church account publicized.</b> Members do not have the bank details handy "
            "when the moment of giving comes. They would have to search for it, ask someone, or wait \u2014 "
            "and waiting usually means it never happens."),
        (3, "<b>No categorization.</b> A bank transfer is just a lump sum. The church cannot tell tithes "
            "from offerings from building fund contributions. Your finance team has to guess or follow up manually."),
        (4, "<b>No receipt.</b> Members have no record of their giving for personal accountability, "
            "tax purposes, or simply the peace of mind that their contribution was received and recorded."),
        (5, "<b>No follow-up mechanism.</b> The church has no way to know who intended to give but did not. "
            "There is no system to gently remind or track consistency."),
    ]

    nb_style = make_style("nb_text", fontSize=9.5, leading=14, textColor=MEDIUM_TEXT, alignment=TA_JUSTIFY, spaceAfter=2)
    for num, text in transfer_failures:
        badge = NumberBadge(num, text, RED_ACCENT, avail_w, text_style=nb_style)
        story.append(badge)
        story.append(Spacer(1, 4 * mm))

    story.append(Spacer(1, 4 * mm))

    # Orange callout - the underlying issue
    issue_callout = CalloutBox(
        title="The underlying issue:",
        title_color=ORANGE_ACCENT,
        text="You are asking people to do something manually, repeatedly, with no system to support them. "
             "That is a <b>system design problem</b>, not a faithfulness problem."
             "<br/><br/>"
             "It is not that your members do not want to give. It is that there is no system making it easy "
             "for them to give consistently.",
        bg_color=ORANGE_LIGHT,
        border_color=ORANGE_ACCENT,
        width=avail_w,
    )
    story.append(issue_callout)

    story.append(PageBreak())

    # =====================================================
    # PAGE 4: THE 3 TYPES OF CHURCH INCOME
    # =====================================================
    story.append(Paragraph("THE 3 TYPES OF CHURCH INCOME", S_H1))
    story.append(hr())

    story.append(Paragraph(
        "Understanding your income mix is the first step to financial stability.",
        S_BODY))

    story.append(Spacer(1, 3 * mm))

    # Type 1
    type1_box = CalloutBox(
        title="Type 1: Spontaneous Giving",
        title_color=ACCENT_BLUE,
        text="One-time offerings, visitor gifts, special appeals. This income is <b>unpredictable by nature</b> "
             "\u2014 it depends entirely on who is present and how they feel in the moment.",
        bg_color=BLUE_LIGHT,
        border_color=ACCENT_BLUE,
        width=avail_w,
    )
    story.append(type1_box)
    story.append(Spacer(1, 4 * mm))

    # Type 2
    type2_box = CalloutBox(
        title="Type 2: Seasonal Giving",
        title_color=ORANGE_ACCENT,
        text="Harvest thanksgiving, Christmas, Easter, special projects. The timing is predictable, "
             "but the amounts <b>vary widely</b> year to year.",
        bg_color=ORANGE_LIGHT,
        border_color=ORANGE_ACCENT,
        width=avail_w,
    )
    story.append(type2_box)
    story.append(Spacer(1, 4 * mm))

    # Type 3
    type3_box = CalloutBox(
        title="Type 3: Committed Recurring Giving",
        title_color=GREEN,
        text="The backbone of financially healthy churches. Same amount, same frequency, <b>rain or shine, "
             "travel or not</b>. This is the income you can plan around \u2014 the income that lets you budget "
             "for staff salaries, building maintenance, outreach programmes, and growth.",
        bg_color=GREEN_LIGHT,
        border_color=GREEN,
        width=avail_w,
    )
    story.append(type3_box)

    story.append(Spacer(1, 6 * mm))

    story.append(Paragraph(
        "The healthiest churches worldwide have <b>50\u201370% of their income from Type 3</b>. "
        "Most Nigerian churches are <b>80% or more dependent on Type 1</b> \u2014 entirely reliant on who "
        "physically shows up on Sunday.",
        S_BODY))

    story.append(Spacer(1, 4 * mm))

    # Key insight callout
    insight_callout = CalloutBox(
        title=None,
        text="The goal is not to eliminate spontaneous giving. It is to build a <b>predictable floor of "
             "recurring income</b> so your church can plan, budget, and grow with confidence.",
        bg_color=GREEN_LIGHT,
        border_color=GREEN,
        width=avail_w,
    )
    story.append(insight_callout)

    story.append(PageBreak())

    # =====================================================
    # PAGE 5: THE FREE FIX - DO THIS TODAY
    # =====================================================
    story.append(Paragraph("THE FREE FIX \u2014 DO THIS TODAY", S_H1))
    story.append(hr())

    story.append(Paragraph(
        "You do not need to buy any software to start solving this problem. Here are five steps you can "
        "implement this week:",
        S_BODY))

    story.append(Spacer(1, 3 * mm))

    free_steps = [
        (1, "<b>Open a Dedicated Offering Account</b><br/>"
            "If you do not already have one, open a separate church offering account (distinct from your "
            "operations account). This makes giving by transfer clean and trackable."),
        (2, "<b>Print the Account Details on a Card</b><br/>"
            "Create a simple card with your bank name, account number, and church name. Hand one to every "
            "member. Make it wallet-sized so they keep it with them."),
        (3, "<b>Announce It Every Sunday</b><br/>"
            "Every single Sunday, verbally remind the congregation: \u201cIf you are travelling next week "
            "or cannot attend for any reason, you can still give \u2014 here are the bank details.\u201d "
            "Repetition is key. Say it until people can recite it."),
        (4, "<b>Have Personal Conversations with Key Givers</b><br/>"
            "For your most committed givers (your top 20\u201330 members), have a personal conversation: "
            "\u201cWould you be willing to set up a standing order with your bank for your monthly tithe?\u201d "
            "Standing orders are free at most Nigerian banks."),
        (5, "<b>Create a Simple Tracking Sheet</b><br/>"
            "Set up a basic spreadsheet: Member Name | Pledged Amount | Frequency | Jan | Feb | Mar | "
            "and so on. Track who is consistent and who might need a gentle follow-up."),
    ]

    free_nb_style = make_style("free_nb_text", fontSize=9.5, leading=14, textColor=MEDIUM_TEXT, alignment=TA_JUSTIFY, spaceAfter=2)
    for num, text in free_steps:
        badge = NumberBadge(num, text, ACCENT_BLUE, avail_w, text_style=free_nb_style)
        story.append(badge)
        story.append(Spacer(1, 5 * mm))

    story.append(Spacer(1, 4 * mm))

    # Orange honest note callout
    honest_callout = CalloutBox(
        title="An honest note:",
        title_color=ORANGE_ACCENT,
        text="This approach works \u2014 but it depends on members remembering, banks processing standing orders "
             "reliably (they often do not), and manual tracking by your finance team. It is a good start, but "
             "it <b>breaks down at scale</b>.",
        bg_color=ORANGE_LIGHT,
        border_color=ORANGE_ACCENT,
        width=avail_w,
    )
    story.append(honest_callout)

    story.append(PageBreak())

    # =====================================================
    # PAGE 6: THE AUTOMATED FIX
    # =====================================================
    story.append(Paragraph("THE AUTOMATED FIX", S_H1))
    story.append(Paragraph("What Effortless Giving Looks Like", S_H2))
    story.append(hr())

    story.append(Paragraph(
        "Here is what giving looks like when there is a proper system behind it:",
        S_BODY))

    story.append(Spacer(1, 3 * mm))

    auto_steps = [
        (1, "<b>Your church gets a branded giving link:</b> autogiving.ng/yourchurch"),
        (2, "<b>A member visits the link on their phone</b> \u2014 no app to download, no registration "
            "hassle, just a clean page with your church name, logo, and colours."),
        (3, "<b>They choose a category</b> \u2014 Tithes, Offerings, Building Fund, Missions, or whatever "
            "categories you have set up."),
        (4, "<b>They set an amount and frequency</b> \u2014 weekly or monthly, whatever they choose."),
        (5, "<b>First payment goes through</b> \u2014 their card is securely saved (tokenized, not stored "
            "as raw card data)."),
        (6, "<b>From then on, giving happens automatically.</b> Every week or every month. Whether they "
            "attend or not. Whether it rains or not. Whether they are in Abuja or Lagos or London."),
        (7, "<b>Members can pause, adjust, or cancel anytime</b> \u2014 no lock-in, no pressure, "
            "no awkward conversations."),
        (8, "<b>Church admin sees everything on a dashboard</b> \u2014 who gave, how much, which category, "
            "when. Export to CSV anytime."),
        (9, "<b>Receipts sent automatically</b> to every giver (email and SMS) after each transaction."),
        (10, "<b>Funds go directly to your church bank account</b> \u2014 never touches anyone else\u2019s account."),
    ]

    auto_nb_style = make_style("auto_nb_text", fontSize=9.5, leading=14, textColor=MEDIUM_TEXT, alignment=TA_JUSTIFY, spaceAfter=2)
    for num, text in auto_steps:
        badge = NumberBadge(num, text, GREEN, avail_w, text_style=auto_nb_style)
        story.append(badge)
        story.append(Spacer(1, 3 * mm))

    story.append(Spacer(1, 4 * mm))

    # Green callout
    pledged_callout = CalloutBox(
        title="This is Pledged.",
        title_color=GREEN,
        text="Your members set it up once. Giving continues <b>rain or shine, holiday or not</b>.",
        bg_color=GREEN_LIGHT,
        border_color=GREEN,
        width=avail_w,
    )
    story.append(pledged_callout)

    story.append(PageBreak())

    # =====================================================
    # PAGE 7: SELF-ASSESSMENT + CTA
    # =====================================================
    story.append(Paragraph("IS YOUR CHURCH IN THE ATTENDANCE-REVENUE TRAP?", S_H1))
    story.append(hr())

    story.append(Paragraph(
        "Answer honestly \u2014 yes or no:",
        S_BODY))

    story.append(Spacer(1, 3 * mm))

    # Assessment table
    assessment_data = [
        [Paragraph("#", S_TABLE_HEADER), Paragraph("Statement", S_TABLE_HEADER), Paragraph("Yes / No", S_TABLE_HEADER)],
        [Paragraph("1", S_TABLE_CELL), Paragraph("Our offering noticeably drops on holiday weekends or rainy Sundays", S_TABLE_CELL), Paragraph("", S_TABLE_CELL)],
        [Paragraph("2", S_TABLE_CELL), Paragraph("We have asked members to transfer when they cannot attend, but few actually do", S_TABLE_CELL), Paragraph("", S_TABLE_CELL)],
        [Paragraph("3", S_TABLE_CELL), Paragraph("We do not know what percentage of our income comes from recurring vs one-time giving", S_TABLE_CELL), Paragraph("", S_TABLE_CELL)],
        [Paragraph("4", S_TABLE_CELL), Paragraph("We cannot accurately predict next month\u2019s total income", S_TABLE_CELL), Paragraph("", S_TABLE_CELL)],
        [Paragraph("5", S_TABLE_CELL), Paragraph("Our church budget is based on hope rather than committed pledges", S_TABLE_CELL), Paragraph("", S_TABLE_CELL)],
    ]

    assessment_table = Table(assessment_data, colWidths=[30, avail_w - 100, 70])
    assessment_table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), TABLE_HEADER_BG),
        ("TEXTCOLOR", (0, 0), (-1, 0), white),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("TOPPADDING", (0, 0), (-1, -1), 8),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
        ("LEFTPADDING", (0, 0), (-1, -1), 8),
        ("RIGHTPADDING", (0, 0), (-1, -1), 8),
        ("BACKGROUND", (0, 1), (-1, 1), white),
        ("BACKGROUND", (0, 2), (-1, 2), TABLE_ALT_ROW),
        ("BACKGROUND", (0, 3), (-1, 3), white),
        ("BACKGROUND", (0, 4), (-1, 4), TABLE_ALT_ROW),
        ("BACKGROUND", (0, 5), (-1, 5), white),
        ("GRID", (0, 0), (-1, -1), 0.5, BORDER_COLOR),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [white, TABLE_ALT_ROW]),
    ]))
    story.append(assessment_table)

    story.append(Spacer(1, 6 * mm))
    story.append(Paragraph("Your Score:", S_H2))
    story.append(Spacer(1, 3 * mm))

    # Score bars
    score_green = ScoreBar(
        "0-1 Yes", "Your church is in good shape. You likely already have systems supporting consistent giving.",
        GREEN, MEDIUM_TEXT, avail_w)
    story.append(score_green)
    story.append(Spacer(1, 4 * mm))

    score_orange = ScoreBar(
        "2-3 Yes", "There are gaps in your giving infrastructure. Addressing them now will make a meaningful difference.",
        ORANGE_ACCENT, MEDIUM_TEXT, avail_w)
    story.append(score_orange)
    story.append(Spacer(1, 4 * mm))

    score_red = ScoreBar(
        "4-5 Yes", "Your church is heavily exposed to the attendance-revenue trap. Every missed Sunday is costing you significantly.",
        RED_ACCENT, MEDIUM_TEXT, avail_w)
    story.append(score_red)

    story.append(Spacer(1, 8 * mm))
    story.append(hr())
    story.append(Spacer(1, 4 * mm))

    # CTA Section
    story.append(Paragraph("FREE 15-MINUTE CHURCH GIVING AUDIT", S_H1))
    story.append(Spacer(1, 2 * mm))

    story.append(Paragraph(
        "<b>We only do 10 per month.</b>",
        make_style("cta_limit", fontName="Lexend-Bold", fontSize=10, leading=14, textColor=RED_ACCENT, alignment=TA_CENTER, spaceAfter=6)
    ))

    story.append(Spacer(1, 2 * mm))

    story.append(Paragraph(
        "In 15 minutes, we will look at your current giving patterns, identify the biggest gaps, and show you "
        "exactly what a recurring giving system could look like for your church \u2014 branded with your name, "
        "logo, and colours.",
        make_style("cta_body", fontSize=9.5, leading=14, textColor=MEDIUM_TEXT, alignment=TA_CENTER, spaceAfter=6)
    ))

    story.append(Spacer(1, 4 * mm))

    # Contact box
    contact_callout = CalloutBox(
        title="Reach out to:",
        title_color=ACCENT_BLUE,
        text="<b>Yasmin Umar</b> \u2014 Chief Brand Strategist"
             "<br/>Phone/WhatsApp: <b>+234 706 905 7925</b>"
             "<br/>Email: <b>yasmin@algolog.co</b>"
             "<br/>Website: <b>autogiving.ng</b>",
        bg_color=BLUE_LIGHT,
        border_color=ACCENT_BLUE,
        width=avail_w,
    )
    story.append(contact_callout)

    story.append(Spacer(1, 6 * mm))

    story.append(Paragraph(
        "No obligation. No pressure. Just a conversation about what is possible for your church.",
        make_style("cta_closing", fontName="Lexend-Medium", fontSize=10, leading=14, textColor=MEDIUM_TEXT, alignment=TA_CENTER, spaceAfter=6)
    ))

    story.append(Spacer(1, 8 * mm))
    story.append(hr())
    story.append(Paragraph(
        "Algolog Limited",
        make_style("footer_co", fontName="Lexend-Bold", fontSize=10, textColor=DARK_TEXT, alignment=TA_CENTER)
    ))
    story.append(Paragraph(
        "5, Kwaji Close, Maitama, Abuja, Nigeria  |  algolog.co  |  autogiving.ng",
        S_HEADER_INFO
    ))
    story.append(Spacer(1, 3 * mm))
    story.append(Paragraph(
        "A free guide prepared with care for church leaders across Nigeria \u2014 March 2026",
        S_SMALL
    ))

    # Build
    doc.build(story, onFirstPage=add_footer, onLaterPages=add_footer)
    print(f"PDF generated: {OUTPUT_PATH}")
    print(f"File size: {os.path.getsize(OUTPUT_PATH):,} bytes")


if __name__ == "__main__":
    build_pdf()
