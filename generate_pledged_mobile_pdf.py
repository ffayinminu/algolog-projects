"""
Generate Pledged — Mobile-Friendly Outreach PDF
Reformatted from the tall single-page design into a multi-page A4 PDF
that reads well on mobile phones without pinch-to-zoom.
Large fonts, generous spacing, single-column layout.
"""

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib.colors import HexColor
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    PageBreak, HRFlowable, KeepTogether
)
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import os

# --- Paths ---
BASE = "C:/Users/Femi Fayinminu/OneDrive/Documents/Algolog/Algolog_Projects"
FONT_DIR = os.path.join(BASE, "fonts/lexend-main/fonts/lexend/ttf")
OUTPUT_PATH = os.path.join(BASE, "Proposals/Pledged-Mobile-Outreach.pdf")

# --- Register Fonts ---
pdfmetrics.registerFont(TTFont("Lexend", os.path.join(FONT_DIR, "Lexend-Regular.ttf")))
pdfmetrics.registerFont(TTFont("Lexend-Bold", os.path.join(FONT_DIR, "Lexend-Bold.ttf")))
pdfmetrics.registerFont(TTFont("Lexend-SemiBold", os.path.join(FONT_DIR, "Lexend-SemiBold.ttf")))
pdfmetrics.registerFont(TTFont("Lexend-Light", os.path.join(FONT_DIR, "Lexend-Light.ttf")))
pdfmetrics.registerFont(TTFont("Lexend-Medium", os.path.join(FONT_DIR, "Lexend-Medium.ttf")))
pdfmetrics.registerFontFamily("Lexend", normal="Lexend", bold="Lexend-Bold", italic="Lexend", boldItalic="Lexend-Bold")

# --- Colors (matching Pledged brand — dark/purple tones from the PDF) ---
DARK_BG = HexColor("#1a1a2e")
PURPLE = HexColor("#6C3FC5")
PURPLE_LIGHT = HexColor("#8B5CF6")
DARK_TEXT = HexColor("#1a1a1a")
MEDIUM_TEXT = HexColor("#333333")
LIGHT_TEXT = HexColor("#555555")
WHITE = HexColor("#ffffff")
GREEN_CHECK = HexColor("#27ae60")
RED_X = HexColor("#e74c3c")
LIGHT_BG = HexColor("#f8f7ff")
BORDER = HexColor("#e0dce8")

# --- Page Setup ---
PAGE_W, PAGE_H = A4
LM = 18 * mm
RM = 18 * mm
TM = 16 * mm
BM = 16 * mm

# --- Styles (larger fonts for mobile readability) ---
def s(name, **kw):
    defaults = {"fontName": "Lexend", "fontSize": 11, "leading": 16, "textColor": DARK_TEXT, "alignment": TA_LEFT, "spaceAfter": 6}
    defaults.update(kw)
    return ParagraphStyle(name, **defaults)

TITLE = s("TITLE", fontName="Lexend-Bold", fontSize=28, leading=34, textColor=PURPLE, alignment=TA_CENTER, spaceAfter=8)
SUBTITLE = s("SUBTITLE", fontName="Lexend-Medium", fontSize=13, leading=18, textColor=MEDIUM_TEXT, alignment=TA_CENTER, spaceAfter=12)
H1 = s("H1", fontName="Lexend-Bold", fontSize=16, leading=22, textColor=PURPLE, spaceBefore=14, spaceAfter=8)
H2 = s("H2", fontName="Lexend-SemiBold", fontSize=13, leading=18, textColor=DARK_TEXT, spaceBefore=10, spaceAfter=6)
H3 = s("H3", fontName="Lexend-SemiBold", fontSize=12, leading=16, textColor=PURPLE, spaceBefore=8, spaceAfter=4)
BODY = s("BODY", fontSize=11, leading=17, textColor=MEDIUM_TEXT, spaceAfter=8)
BODY_B = s("BODY_B", fontName="Lexend-Bold", fontSize=11, leading=17, textColor=DARK_TEXT, spaceAfter=8)
BUL = s("BUL", fontSize=11, leading=17, textColor=MEDIUM_TEXT, leftIndent=16, bulletIndent=4, spaceAfter=6)
BUL_GREEN = s("BUL_GREEN", fontSize=11, leading=17, textColor=GREEN_CHECK, leftIndent=16, bulletIndent=4, spaceAfter=6)
SM = s("SM", fontSize=9, leading=13, textColor=LIGHT_TEXT, alignment=TA_CENTER)
TH = s("TH", fontName="Lexend-Bold", fontSize=10, leading=14, textColor=WHITE)
TC = s("TC", fontSize=10, leading=14, textColor=MEDIUM_TEXT)
TCB = s("TCB", fontName="Lexend-Bold", fontSize=10, leading=14, textColor=DARK_TEXT)
STEP_NUM = s("STEP_NUM", fontName="Lexend-Bold", fontSize=20, leading=24, textColor=PURPLE, alignment=TA_CENTER)
STEP_TEXT = s("STEP_TEXT", fontSize=11, leading=16, textColor=MEDIUM_TEXT)


def hr():
    return HRFlowable(width="100%", thickness=0.5, color=BORDER, spaceAfter=8, spaceBefore=8)


def purple_hr():
    return HRFlowable(width="30%", thickness=2, color=PURPLE, spaceAfter=10, spaceBefore=6)


def build():
    doc = SimpleDocTemplate(OUTPUT_PATH, pagesize=A4, leftMargin=LM, rightMargin=RM, topMargin=TM, bottomMargin=BM)
    story = []
    aw = PAGE_W - LM - RM

    # ========== PAGE 1: HERO ==========
    story.append(Spacer(1, 30 * mm))
    story.append(Paragraph("Pledged", s("logo", fontName="Lexend-Bold", fontSize=36, leading=42, textColor=PURPLE, alignment=TA_CENTER, spaceAfter=4)))
    story.append(purple_hr())
    story.append(Spacer(1, 6 * mm))

    story.append(Paragraph("Zero Cash Handling", s("hero1", fontName="Lexend-Bold", fontSize=22, leading=28, textColor=DARK_TEXT, alignment=TA_CENTER, spaceAfter=4)))
    story.append(Paragraph("Recurring Giving That Runs<br/>Automatically \u2014 Even When<br/>Members Travel", s("hero2", fontName="Lexend-SemiBold", fontSize=16, leading=22, textColor=PURPLE, alignment=TA_CENTER, spaceAfter=12)))

    story.append(Paragraph(
        "Pledged replaces cash-dependent Sunday collections with automated digital giving. "
        "Churches get a branded giving page, and members can set up their own recurring "
        "contributions independently in under 2 minutes \u2014 no church admin needs to do it for them. "
        "Funds settle directly to the church\u2019s bank account. No third party ever holds the money.",
        s("hero_body", fontSize=12, leading=18, textColor=MEDIUM_TEXT, alignment=TA_CENTER, spaceAfter=8)))

    story.append(PageBreak())

    # ========== PAGE 2: THE PROBLEM ==========
    story.append(Paragraph("The Problem", H1))
    story.append(purple_hr())

    problems = [
        "Giving drops during holidays and travel when members are absent",
        "Cash offerings counted manually every Sunday \u2014 errors and time wasted",
        "No visibility into who gave what without manual ledgers",
        "Finance team spends hours reconciling weekly collections",
    ]
    for p in problems:
        story.append(Paragraph(f"\u2718  {p}", s("prob", fontSize=11, leading=17, textColor=RED_X, leftIndent=16, bulletIndent=4, spaceAfter=8)))

    story.append(Spacer(1, 8 * mm))

    # ========== THE SOLUTION ==========
    story.append(Paragraph("The Pledged Solution", H1))
    story.append(purple_hr())

    solutions = [
        "Every transaction recorded digitally with instant receipts",
        "Recurring giving continues automatically \u2014 zero holiday drop",
        "Full member giving history accessible from admin dashboard",
        "One-click CSV export for reconciliation in minutes",
    ]
    for sol in solutions:
        story.append(Paragraph(f"\u2714  {sol}", s("sol", fontSize=11, leading=17, textColor=GREEN_CHECK, leftIndent=16, bulletIndent=4, spaceAfter=8)))

    story.append(PageBreak())

    # ========== PAGE 3: KEY CAPABILITIES ==========
    story.append(Paragraph("Key Capabilities", H1))
    story.append(purple_hr())

    caps = [
        "Branded giving page at <b>pledged.app/[churchname]</b> with church logo and colours",
        "Members set up their own giving independently \u2014 no church admin involvement needed",
        "Weekly or monthly recurring giving \u2014 pause, adjust, or cancel anytime",
        "Direct settlement to church bank account via Paystack subaccounts",
        "Automated email and SMS receipts for every transaction",
        "Admin dashboard with full giving analytics and member management",
        "Category-based giving (tithes, offerings, building fund, missions, etc.)",
    ]
    for cap in caps:
        story.append(Paragraph(f"\u2022  {cap}", BUL))
        story.append(Spacer(1, 2 * mm))

    story.append(Spacer(1, 6 * mm))
    story.append(Paragraph(
        "Pledged automates church giving, protects revenue during holidays, and gives "
        "members full control over their contributions.",
        s("cap_summary", fontName="Lexend-SemiBold", fontSize=11, leading=17, textColor=PURPLE, alignment=TA_CENTER, spaceAfter=8)))

    story.append(PageBreak())

    # ========== PAGE 4: USE CASES ==========
    story.append(Paragraph("Who Is Pledged For?", H1))
    story.append(purple_hr())

    # Use Case 1
    story.append(Paragraph("Use Case 1: Mid-Size Church (200\u2013500 members)", H2))
    story.append(Paragraph(
        "A church with 300 members currently collects cash offerings every Sunday. Only about 80 "
        "members give consistently \u2014 the rest give when they remember or when they\u2019re physically "
        "present. With Pledged, members set up recurring giving once. Contributions continue "
        "automatically even during holidays, travel, or when members attend other branches. The "
        "finance team stops counting cash and starts managing from a dashboard.", BODY))

    story.append(Spacer(1, 4 * mm))

    # Use Case 2
    story.append(Paragraph("Use Case 2: Multi-Branch Church", H2))
    story.append(Paragraph(
        "A church with 3 branches currently has no unified view of giving across locations. Each "
        "branch counts independently and reports manually. Pledged gives leadership a single "
        "dashboard showing giving across all branches in real time \u2014 with category breakdowns, "
        "member activity, and automatic reconciliation.", BODY))

    story.append(Spacer(1, 4 * mm))

    # Use Case 3
    story.append(Paragraph("Use Case 3: New Church Plant", H2))
    story.append(Paragraph(
        "A new church with 50 members can\u2019t afford a full finance team. Pledged handles giving "
        "infrastructure from day one \u2014 branded page, automated receipts, bank settlement, member "
        "management \u2014 so leadership can focus on ministry instead of administration.", BODY))

    story.append(PageBreak())

    # ========== PAGE 5: WHAT PLEDGED ENABLES ==========
    story.append(Paragraph("What Pledged Enables", H1))
    story.append(purple_hr())

    enables = [
        "Predictable monthly income from recurring subscriptions",
        "Giving that doesn\u2019t stop when members travel or miss service",
        "Complete transparency \u2014 members see their own giving history",
        "Zero cash handling risk \u2014 no counting, no discrepancies",
        "Monday reconciliation reduced from hours to minutes",
    ]
    for e in enables:
        story.append(Paragraph(f"\u2714  {e}", s("en", fontSize=12, leading=18, textColor=GREEN_CHECK, leftIndent=16, bulletIndent=4, spaceAfter=10)))

    story.append(Spacer(1, 10 * mm))

    # ========== HOW IT WORKS ==========
    story.append(Paragraph("How It Works", H1))
    story.append(Paragraph("From Signup to First Giving in Under 5 Minutes", s("hw_sub", fontName="Lexend-Medium", fontSize=12, leading=16, textColor=LIGHT_TEXT, spaceAfter=10)))
    story.append(purple_hr())

    steps = [
        ("1", "Church signs up and connects their bank account"),
        ("2", "Church gets a branded giving page (pledged.app/[churchname])"),
        ("3", "Members visit the page and set up their giving (amount + frequency)"),
        ("4", "Giving runs automatically \u2014 funds settle directly to church bank"),
    ]

    for num, text in steps:
        step_data = [[
            Paragraph(num, STEP_NUM),
            Paragraph(text, s(f"st{num}", fontSize=11, leading=16, textColor=MEDIUM_TEXT)),
        ]]
        step_table = Table(step_data, colWidths=[14 * mm, aw - 14 * mm])
        step_table.setStyle(TableStyle([
            ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
            ("LEFTPADDING", (0, 0), (-1, -1), 4),
            ("RIGHTPADDING", (0, 0), (-1, -1), 4),
            ("TOPPADDING", (0, 0), (-1, -1), 6),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
        ]))
        story.append(step_table)
        story.append(Spacer(1, 2 * mm))

    story.append(PageBreak())

    # ========== PAGE 6: COMPARISON TABLE ==========
    story.append(Paragraph("Before &amp; After Pledged", H1))
    story.append(purple_hr())

    comp = [
        [Paragraph("<b>Without Pledged</b>", TH), Paragraph("<b>With Pledged</b>", TH)],
        [Paragraph("Cash offerings handled by multiple volunteers \u2014 risk of errors", TC),
         Paragraph("Zero cash handling \u2014 all giving is digital and auditable", TC)],
        [Paragraph("Members forget to give when absent from service", TC),
         Paragraph("Automated recurring giving runs whether members are present or not", TC)],
        [Paragraph("No way to track individual member giving patterns", TC),
         Paragraph("Complete member giving history with category breakdown", TC)],
        [Paragraph("Budget planning based on rough estimates", TC),
         Paragraph("Predictable monthly income from recurring subscriptions", TC)],
    ]
    ct = Table(comp, colWidths=[aw * 0.5, aw * 0.5])
    ct.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), PURPLE),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("TOPPADDING", (0, 0), (-1, -1), 8),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
        ("LEFTPADDING", (0, 0), (-1, -1), 8),
        ("RIGHTPADDING", (0, 0), (-1, -1), 8),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [WHITE, LIGHT_BG]),
        ("LINEBELOW", (0, 0), (-1, -2), 0.25, BORDER),
        ("BOX", (0, 0), (-1, -1), 0.5, BORDER),
    ]))
    story.append(ct)

    story.append(Spacer(1, 6 * mm))
    story.append(Paragraph(
        "Pledged delivers transparent, automated giving that members trust and leadership can plan around.",
        s("comp_close", fontName="Lexend-SemiBold", fontSize=11, leading=17, textColor=PURPLE, alignment=TA_CENTER)))

    story.append(Spacer(1, 10 * mm))

    # ========== CONTACT ==========
    story.append(hr())
    story.append(Spacer(1, 4 * mm))

    story.append(Paragraph("Algolog Limited", s("fc", fontName="Lexend-Bold", fontSize=12, textColor=DARK_TEXT, alignment=TA_CENTER, spaceAfter=4)))
    story.append(Paragraph("Plot 1387 Aminu Kano Crescent, Wuse, Abuja  |  algolog.co", SM))

    story.append(Spacer(1, 4 * mm))

    contact_data = [
        [Paragraph("<b>Mike</b> (CEO/CTO)", TCB), Paragraph("<b>Yasmin</b> (Brand Strategy)", TCB)],
        [Paragraph("+234 808 396 5912", TC), Paragraph("+234 706 905 7925", TC)],
        [Paragraph("info@algolog.co", TC), Paragraph("yasmin@algolog.co", TC)],
    ]
    contact_table = Table(contact_data, colWidths=[aw * 0.5, aw * 0.5])
    contact_table.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("TOPPADDING", (0, 0), (-1, -1), 4),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
        ("LEFTPADDING", (0, 0), (-1, -1), 8),
        ("ALIGN", (0, 0), (-1, -1), "CENTER"),
    ]))
    story.append(contact_table)

    doc.build(story)
    print(f"PDF generated: {OUTPUT_PATH}")
    print(f"File size: {os.path.getsize(OUTPUT_PATH):,} bytes")


if __name__ == "__main__":
    build()
