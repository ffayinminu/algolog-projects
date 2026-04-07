"""
Generate WorkingForGod.org — Upfront Payment Invoice PDF
Client: AiMP Network (Apostles In The Market Place)
Format: Matches KayWi invoice style (Algolog standard)
"""

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib.colors import HexColor
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT, TA_JUSTIFY
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    HRFlowable, Image
)
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import os

# --- Paths ---
BASE = "C:/Users/Femi Fayinminu/OneDrive/Documents/Algolog/Algolog_Projects"
FONT_DIR = os.path.join(BASE, "fonts/lexend-main/fonts/lexend/ttf")
BANNER_PATH = os.path.join(BASE, "claude.ai contex/banner_centered.png")
LOGO_PATH = os.path.join(BASE, "claude.ai contex/Algolog_invoice_Logo_nobg.png")
OUTPUT_PATH = os.path.join(BASE, "Proposals/Invoice-AiMP-Network-WorkingForGod.pdf")

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
DARK_BG = HexColor("#1a1a2e")
ACCENT_BLUE = HexColor("#0f3460")
DARK_TEXT = HexColor("#1a1a1a")
MEDIUM_TEXT = HexColor("#333333")
LIGHT_TEXT = HexColor("#555555")
TABLE_HEADER_BG = HexColor("#1a1a2e")
TABLE_ALT_ROW = HexColor("#f5f6fa")
BORDER_COLOR = HexColor("#dcdde1")
WHITE = HexColor("#ffffff")

# --- Page Setup ---
PAGE_W, PAGE_H = A4
LEFT_MARGIN = 22 * mm
RIGHT_MARGIN = 22 * mm
TOP_MARGIN = 20 * mm
BOTTOM_MARGIN = 20 * mm

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

S_COMPANY = make_style("S_COMPANY", fontName="Lexend-Bold", fontSize=16, leading=20, textColor=ACCENT_BLUE)
S_COMPANY_INFO = make_style("S_COMPANY_INFO", fontSize=9, leading=13, textColor=LIGHT_TEXT)
S_INVOICE_TITLE = make_style("S_INVOICE_TITLE", fontName="Lexend-Bold", fontSize=24, leading=28, textColor=ACCENT_BLUE, alignment=TA_RIGHT)
S_LABEL = make_style("S_LABEL", fontName="Lexend-SemiBold", fontSize=9.5, leading=13, textColor=DARK_TEXT)
S_VALUE = make_style("S_VALUE", fontSize=9.5, leading=13, textColor=MEDIUM_TEXT)
S_VALUE_BOLD = make_style("S_VALUE_BOLD", fontName="Lexend-Bold", fontSize=9.5, leading=13, textColor=DARK_TEXT)
S_BODY = make_style("S_BODY", fontSize=9.5, leading=14, textColor=MEDIUM_TEXT, alignment=TA_JUSTIFY)
S_TABLE_HEADER = make_style("S_TABLE_HEADER", fontName="Lexend-Bold", fontSize=9, leading=12, textColor=WHITE)
S_TABLE_CELL = make_style("S_TABLE_CELL", fontSize=9, leading=12, textColor=MEDIUM_TEXT)
S_TABLE_CELL_BOLD = make_style("S_TABLE_CELL_BOLD", fontName="Lexend-Bold", fontSize=9, leading=12, textColor=DARK_TEXT)
S_TABLE_CELL_RIGHT = make_style("S_TABLE_CELL_RIGHT", fontSize=9, leading=12, textColor=MEDIUM_TEXT, alignment=TA_RIGHT)
S_TABLE_CELL_BOLD_RIGHT = make_style("S_TABLE_CELL_BOLD_RIGHT", fontName="Lexend-Bold", fontSize=9, leading=12, textColor=DARK_TEXT, alignment=TA_RIGHT)
S_TABLE_HEADER_RIGHT = make_style("S_TABLE_HEADER_RIGHT", fontName="Lexend-Bold", fontSize=9, leading=12, textColor=WHITE, alignment=TA_RIGHT)
S_TABLE_HEADER_CENTER = make_style("S_TABLE_HEADER_CENTER", fontName="Lexend-Bold", fontSize=9, leading=12, textColor=WHITE, alignment=TA_CENTER)
S_TABLE_CELL_CENTER = make_style("S_TABLE_CELL_CENTER", fontSize=9, leading=12, textColor=MEDIUM_TEXT, alignment=TA_CENTER)
S_NOTE = make_style("S_NOTE", fontSize=8.5, leading=12, textColor=LIGHT_TEXT, alignment=TA_JUSTIFY)
S_FOOTER = make_style("S_FOOTER", fontName="Lexend-Light", fontSize=7.5, leading=11, textColor=LIGHT_TEXT, alignment=TA_CENTER)
S_SMALL = make_style("S_SMALL", fontSize=8, leading=11, textColor=LIGHT_TEXT, alignment=TA_CENTER)


def hr():
    return HRFlowable(width="100%", thickness=0.5, color=BORDER_COLOR, spaceAfter=8, spaceBefore=8)


def add_footer(canvas_obj, doc):
    canvas_obj.saveState()
    canvas_obj.setFont("Lexend-Light", 7)
    canvas_obj.setFillColor(LIGHT_TEXT)
    canvas_obj.drawCentredString(
        PAGE_W / 2, 12 * mm,
        f"Algolog Limited \u2014 Plot 1387 Aminu Kano Crescent, Wuse, Abuja | algolog.co"
    )
    canvas_obj.restoreState()


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
    # HEADER: Logo + Company info + INVOICE title
    # =====================================================
    # Logo — square, height matches the company info block beside it
    logo_h = 30 * mm
    logo_w = logo_h  # square
    logo_img = Image(LOGO_PATH, width=logo_w, height=logo_h) if os.path.exists(LOGO_PATH) else Paragraph("", S_COMPANY)

    logo_col_w = logo_w + 4 * mm
    header_data = [
        [logo_img,
         [Paragraph("Algolog Limited", S_COMPANY),
          Paragraph("Plot 1387 Aminu Kano Crescent, Wuse, Abuja", S_COMPANY_INFO),
          Paragraph("info@algolog.co | algolog.co", S_COMPANY_INFO)],
         Paragraph("INVOICE", S_INVOICE_TITLE)],
    ]
    header_table = Table(header_data, colWidths=[logo_col_w, avail_w - logo_col_w - avail_w * 0.3, avail_w * 0.3])
    header_table.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("LEFTPADDING", (0, 0), (-1, -1), 0),
        ("RIGHTPADDING", (0, 0), (-1, -1), 0),
    ]))
    story.append(header_table)
    story.append(Spacer(1, 8 * mm))
    story.append(hr())

    # =====================================================
    # BILL TO / INVOICE DETAILS
    # =====================================================
    bill_to = [
        Paragraph("<b>Bill To:</b>", S_LABEL),
        Spacer(1, 2 * mm),
        Paragraph("AiMP Network", S_VALUE_BOLD),
        Paragraph("(Apostles In The Market Place)", S_VALUE),
        Paragraph("Attn: Nwamaka Okoye", S_VALUE),
    ]

    invoice_details = [
        Paragraph("<b>Invoice Details:</b>", S_LABEL),
        Spacer(1, 2 * mm),
        Paragraph("WorkingForGod.org Project", S_VALUE_BOLD),
        Paragraph("<b>Invoice No:</b> ALG-2026-0402", S_VALUE),
        Paragraph("<b>Date:</b> April 2, 2026", S_VALUE),
        Paragraph("<b>Due Date:</b> Upon Receipt", S_VALUE),
        Paragraph("<b>Payment Terms:</b> Upfront Payment", S_VALUE),
    ]

    details_data = [[bill_to, invoice_details]]
    details_table = Table(details_data, colWidths=[avail_w * 0.5, avail_w * 0.5])
    details_table.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 0),
        ("RIGHTPADDING", (0, 0), (-1, -1), 0),
    ]))
    story.append(details_table)

    story.append(Spacer(1, 4 * mm))
    story.append(Paragraph(
        "<b>Reference:</b> Upfront Payment \u2014 WorkingForGod.org Christian Professional Training Platform "
        "(Full Design, Development, Deployment & Training)",
        make_style("ref", fontSize=9, leading=13, textColor=MEDIUM_TEXT)))

    story.append(Spacer(1, 6 * mm))

    # =====================================================
    # LINE ITEMS TABLE
    # =====================================================
    col_widths = [avail_w * 0.06, avail_w * 0.74, avail_w * 0.2]

    items_header = [
        Paragraph("<b>#</b>", S_TABLE_HEADER_CENTER),
        Paragraph("<b>Description</b>", S_TABLE_HEADER),
        Paragraph("<b>Total (\u20a6)</b>", S_TABLE_HEADER_RIGHT),
    ]

    items = [
        items_header,
        [
            Paragraph("", S_TABLE_CELL),
            Paragraph("<b>WorkingForGod.org \u2014 Full Platform Development</b>", S_TABLE_CELL_BOLD),
            Paragraph("<b>8,900,000</b>", S_TABLE_CELL_BOLD_RIGHT),
        ],
        [
            Paragraph("1", S_TABLE_CELL_CENTER),
            Paragraph("Frontend Development \u2014 Next.js + React.js implementation, responsive design, all user-facing screens", S_TABLE_CELL),
            Paragraph("", S_TABLE_CELL),
        ],
        [
            Paragraph("2", S_TABLE_CELL_CENTER),
            Paragraph("Backend Development \u2014 Node.js server, PostgreSQL database, API layer, user management, Azure cloud deployment", S_TABLE_CELL),
            Paragraph("", S_TABLE_CELL),
        ],
        [
            Paragraph("3", S_TABLE_CELL_CENTER),
            Paragraph("Subscription & Payment Gateway Integration \u2014 Individual and organizational subscription tiers, payment processing", S_TABLE_CELL),
            Paragraph("", S_TABLE_CELL),
        ],
        [
            Paragraph("4", S_TABLE_CELL_CENTER),
            Paragraph("Content Management System (CMS) Setup \u2014 Admin panel for courses, articles, user management, analytics", S_TABLE_CELL),
            Paragraph("", S_TABLE_CELL),
        ],
        [
            Paragraph("5", S_TABLE_CELL_CENTER),
            Paragraph("Deployment, Quality Testing & Training \u2014 QA, production deployment, staff training, user manual", S_TABLE_CELL),
            Paragraph("", S_TABLE_CELL),
        ],
    ]

    items_table = Table(items, colWidths=col_widths)
    items_table.setStyle(TableStyle([
        # Header row
        ("BACKGROUND", (0, 0), (-1, 0), TABLE_HEADER_BG),
        ("TEXTCOLOR", (0, 0), (-1, 0), WHITE),
        # Section header row
        ("BACKGROUND", (0, 1), (-1, 1), HexColor("#e8e8e8")),
        # Alternating rows for items
        ("ROWBACKGROUNDS", (0, 2), (-1, -1), [WHITE, TABLE_ALT_ROW]),
        # General
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("TOPPADDING", (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
        ("LEFTPADDING", (0, 0), (-1, -1), 6),
        ("RIGHTPADDING", (0, 0), (-1, -1), 6),
        ("LINEBELOW", (0, 0), (-1, -2), 0.25, BORDER_COLOR),
        ("BOX", (0, 0), (-1, -1), 0.5, BORDER_COLOR),
    ]))
    story.append(items_table)

    story.append(Spacer(1, 6 * mm))

    # =====================================================
    # TOTALS
    # =====================================================
    totals_data = [
        [Paragraph("", S_TABLE_CELL), Paragraph("<b>Subtotal:</b>", S_TABLE_CELL_BOLD),
         Paragraph("<b>\u20a68,900,000</b>", S_TABLE_CELL_BOLD_RIGHT)],
        [Paragraph("", S_TABLE_CELL), Paragraph("<b>Upfront Payment Due:</b>", S_TABLE_CELL_BOLD),
         Paragraph("<b>\u20a65,000,000</b>",
                    make_style("amt_due", fontName="Lexend-Bold", fontSize=11, leading=14, textColor=ACCENT_BLUE, alignment=TA_RIGHT))],
        [Paragraph("", S_TABLE_CELL), Paragraph("Balance (on Completion):", S_TABLE_CELL),
         Paragraph("\u20a63,900,000", S_TABLE_CELL_RIGHT)],
    ]
    totals_table = Table(totals_data, colWidths=[avail_w * 0.4, avail_w * 0.35, avail_w * 0.25])
    totals_table.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("TOPPADDING", (0, 0), (-1, -1), 4),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
        ("LEFTPADDING", (0, 0), (-1, -1), 6),
        ("RIGHTPADDING", (0, 0), (-1, -1), 6),
        ("LINEABOVE", (1, 0), (-1, 0), 1, BORDER_COLOR),
        ("LINEBELOW", (1, 1), (-1, 1), 1.5, ACCENT_BLUE),
    ]))
    story.append(totals_table)

    story.append(Spacer(1, 10 * mm))
    story.append(hr())

    # =====================================================
    # PAYMENT DETAILS
    # =====================================================
    story.append(Paragraph("<b>Payment Details</b>",
                           make_style("pay_title", fontName="Lexend-Bold", fontSize=12, leading=16, textColor=ACCENT_BLUE, spaceAfter=6)))

    bank_data = [
        [Paragraph("<b>Account Name:</b>", S_LABEL), Paragraph("Algolog Limited", S_VALUE)],
        [Paragraph("<b>Bank:</b>", S_LABEL), Paragraph("United Bank for Africa (UBA)", S_VALUE)],
        [Paragraph("<b>Account Number:</b>", S_LABEL), Paragraph("1027225122", S_VALUE_BOLD)],
        [Paragraph("<b>Amount Due:</b>", S_LABEL),
         Paragraph("<b>\u20a65,000,000</b>",
                    make_style("amt_bank", fontName="Lexend-Bold", fontSize=10, leading=14, textColor=ACCENT_BLUE))],
    ]
    bank_table = Table(bank_data, colWidths=[avail_w * 0.25, avail_w * 0.75])
    bank_table.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("TOPPADDING", (0, 0), (-1, -1), 4),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
        ("LEFTPADDING", (0, 0), (-1, -1), 6),
        ("RIGHTPADDING", (0, 0), (-1, -1), 6),
        ("LINEBELOW", (0, 0), (-1, -2), 0.25, BORDER_COLOR),
    ]))
    story.append(bank_table)

    story.append(Spacer(1, 8 * mm))

    # =====================================================
    # NOTE
    # =====================================================
    story.append(Paragraph(
        "<b>Note:</b> Upfront payment of \u20a65,000,000 is required prior to project commencement as per the "
        "agreed terms. Upon receipt, Algolog will mobilize the development team and activate project "
        "timelines. The balance of \u20a63,900,000 is due upon completion, deployment, and handover of the platform.",
        S_NOTE))

    story.append(Spacer(1, 8 * mm))
    story.append(hr())

    story.append(Paragraph(
        "Contact: Fayinminu Femi | ffayinminu@algolog.co | +234 705 301 6348", S_FOOTER))
    story.append(Spacer(1, 2 * mm))
    story.append(Paragraph(
        "Algolog Limited \u2014 Plot 1387 Aminu Kano Crescent, Wuse, Abuja | algolog.co", S_FOOTER))

    # Build
    doc.build(story, onFirstPage=add_footer, onLaterPages=add_footer)
    print(f"PDF generated: {OUTPUT_PATH}")
    print(f"File size: {os.path.getsize(OUTPUT_PATH):,} bytes")


if __name__ == "__main__":
    build_pdf()
