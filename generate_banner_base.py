"""
Shared Banner Generator Module for Algolog Product Banners
Banner size: 40 x 87.3 inches (2880 x 6285.6 pts) — matches existing Spacer roll-up banner
All banners use Lexend font family, Algolog color palette, and consistent layout components.
"""

import os
from reportlab.lib.units import inch, mm
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

# --- Paths ---
BASE = "C:/Users/Femi Fayinminu/OneDrive/Documents/Algolog/Algolog_Projects"
FONT_DIR = os.path.join(BASE, "fonts/lexend-main/fonts/lexend/ttf")
BANNER_IMG_PATH = os.path.join(BASE, "claude.ai contex/banner_centered.png")
PROPOSALS_DIR = os.path.join(BASE, "Proposals")

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

# --- Banner Page Size ---
BANNER_W = 40 * inch    # 2880 pts
BANNER_H = 87.3 * inch  # 6285.6 pts
BANNER_SIZE = (BANNER_W, BANNER_H)

# Margins scaled for banner (approx 1.5 inches each side)
BANNER_LEFT = 1.5 * inch
BANNER_RIGHT = 1.5 * inch
BANNER_TOP = 1.5 * inch
BANNER_BOTTOM = 1.5 * inch
AVAIL_W = BANNER_W - BANNER_LEFT - BANNER_RIGHT  # ~2664 pts

# --- Colors ---
ACCENT_BLUE = HexColor("#0f3460")
DARK_TEXT = HexColor("#1a1a1a")
MEDIUM_TEXT = HexColor("#333333")
LIGHT_TEXT = HexColor("#555555")
WHITE = HexColor("#ffffff")
BORDER_COLOR = HexColor("#dcdde1")
GREEN = HexColor("#27ae60")
GREEN_LIGHT = HexColor("#eafaf1")
RED_ACCENT = HexColor("#c0392b")
RED_LIGHT = HexColor("#fdedec")
ORANGE_ACCENT = HexColor("#e67e22")
BLUE_LIGHT = HexColor("#eaf2f8")
YELLOW_LIGHT = HexColor("#fef9e7")
TABLE_HEADER_BG = HexColor("#1a1a2e")
TABLE_ALT_ROW = HexColor("#f5f6fa")
DARK_BG = HexColor("#1a1a2e")


# --- Style Factory ---
def make_style(name, **kwargs):
    defaults = {
        "fontName": "Lexend",
        "fontSize": 28,
        "leading": 38,
        "textColor": DARK_TEXT,
        "alignment": TA_LEFT,
        "spaceAfter": 12,
    }
    defaults.update(kwargs)
    return ParagraphStyle(name, **defaults)


# --- Banner-Scaled Styles ---
# Product name / big title (~80pt)
S_TITLE = make_style("S_TITLE", fontName="Lexend-Bold", fontSize=80, leading=96,
                      textColor=ACCENT_BLUE, alignment=TA_CENTER, spaceAfter=20)

# Tagline under product name (~42pt)
S_TAGLINE = make_style("S_TAGLINE", fontName="Lexend-Medium", fontSize=42, leading=54,
                        textColor=MEDIUM_TEXT, alignment=TA_CENTER, spaceAfter=30)

# Section headings (~48pt)
S_SECTION = make_style("S_SECTION", fontName="Lexend-SemiBold", fontSize=48, leading=60,
                        textColor=ACCENT_BLUE, alignment=TA_LEFT, spaceAfter=20, spaceBefore=30)
S_SECTION_CENTER = make_style("S_SECTION_CENTER", fontName="Lexend-SemiBold", fontSize=48, leading=60,
                               textColor=ACCENT_BLUE, alignment=TA_CENTER, spaceAfter=20, spaceBefore=30)

# Sub-headings (~36pt)
S_SUBHEAD = make_style("S_SUBHEAD", fontName="Lexend-SemiBold", fontSize=36, leading=46,
                        textColor=DARK_TEXT, alignment=TA_LEFT, spaceAfter=14)

# Body text (~28pt)
S_BODY = make_style("S_BODY", fontSize=28, leading=40, textColor=MEDIUM_TEXT,
                     alignment=TA_LEFT, spaceAfter=12)
S_BODY_CENTER = make_style("S_BODY_CENTER", fontSize=28, leading=40, textColor=MEDIUM_TEXT,
                            alignment=TA_CENTER, spaceAfter=12)
S_BODY_BOLD = make_style("S_BODY_BOLD", fontName="Lexend-Bold", fontSize=28, leading=40,
                          textColor=DARK_TEXT, spaceAfter=12)

# Stats / callout text (~36pt)
S_STAT = make_style("S_STAT", fontName="Lexend-Medium", fontSize=36, leading=46,
                     textColor=ACCENT_BLUE, alignment=TA_CENTER, spaceAfter=14)

# Big stat number (~60pt)
S_STAT_BIG = make_style("S_STAT_BIG", fontName="Lexend-Bold", fontSize=60, leading=72,
                          textColor=ACCENT_BLUE, alignment=TA_CENTER, spaceAfter=8)

# Small / footer text (~20pt)
S_SMALL = make_style("S_SMALL", fontName="Lexend-Light", fontSize=20, leading=28,
                      textColor=LIGHT_TEXT, alignment=TA_CENTER, spaceAfter=8)

# Value prop number badge
S_BADGE_NUM = make_style("S_BADGE_NUM", fontName="Lexend-Bold", fontSize=42, leading=50,
                          textColor=WHITE, alignment=TA_CENTER, spaceAfter=0)

# Feature title in grid
S_FEAT_TITLE = make_style("S_FEAT_TITLE", fontName="Lexend-SemiBold", fontSize=28, leading=36,
                            textColor=DARK_TEXT, alignment=TA_LEFT, spaceAfter=4)
S_FEAT_DESC = make_style("S_FEAT_DESC", fontSize=24, leading=34, textColor=MEDIUM_TEXT,
                           alignment=TA_LEFT, spaceAfter=8)

# Contact info
S_CONTACT = make_style("S_CONTACT", fontName="Lexend-Medium", fontSize=28, leading=40,
                         textColor=WHITE, alignment=TA_CENTER, spaceAfter=8)
S_CONTACT_BIG = make_style("S_CONTACT_BIG", fontName="Lexend-Bold", fontSize=36, leading=48,
                             textColor=WHITE, alignment=TA_CENTER, spaceAfter=12)

# Problem text (big, bold for front side)
S_PROBLEM = make_style("S_PROBLEM", fontName="Lexend-SemiBold", fontSize=34, leading=46,
                         textColor=DARK_TEXT, alignment=TA_CENTER, spaceAfter=20)

# Website URL style
S_URL = make_style("S_URL", fontName="Lexend-Medium", fontSize=36, leading=46,
                     textColor=ACCENT_BLUE, alignment=TA_CENTER, spaceAfter=14)

# Step number style
S_STEP_NUM = make_style("S_STEP_NUM", fontName="Lexend-Bold", fontSize=48, leading=56,
                          textColor=WHITE, alignment=TA_CENTER, spaceAfter=0)
S_STEP_TITLE = make_style("S_STEP_TITLE", fontName="Lexend-SemiBold", fontSize=30, leading=40,
                            textColor=DARK_TEXT, alignment=TA_LEFT, spaceAfter=4)
S_STEP_DESC = make_style("S_STEP_DESC", fontSize=24, leading=34, textColor=MEDIUM_TEXT,
                           alignment=TA_LEFT, spaceAfter=8)

# Audience text
S_AUDIENCE = make_style("S_AUDIENCE", fontName="Lexend-Medium", fontSize=28, leading=40,
                          textColor=MEDIUM_TEXT, alignment=TA_LEFT, spaceAfter=10)

# Master banner product grid
S_PRODUCT_NAME = make_style("S_PRODUCT_NAME", fontName="Lexend-Bold", fontSize=32, leading=42,
                              textColor=ACCENT_BLUE, alignment=TA_LEFT, spaceAfter=4)
S_PRODUCT_DESC = make_style("S_PRODUCT_DESC", fontSize=24, leading=34, textColor=MEDIUM_TEXT,
                              alignment=TA_LEFT, spaceAfter=4)
S_PRODUCT_URL = make_style("S_PRODUCT_URL", fontName="Lexend-Medium", fontSize=22, leading=30,
                             textColor=ACCENT_BLUE, alignment=TA_LEFT, spaceAfter=8)

# Category header for master banner
S_CATEGORY = make_style("S_CATEGORY", fontName="Lexend-Bold", fontSize=34, leading=44,
                          textColor=WHITE, alignment=TA_LEFT, spaceAfter=10)

# About Algolog paragraph
S_ABOUT = make_style("S_ABOUT", fontSize=26, leading=38, textColor=MEDIUM_TEXT,
                       alignment=TA_JUSTIFY, spaceAfter=14)

# Pricing hint
S_PRICE = make_style("S_PRICE", fontName="Lexend-SemiBold", fontSize=32, leading=42,
                       textColor=GREEN, alignment=TA_CENTER, spaceAfter=14)


# --- Reusable Components ---

def banner_spacer(height_inches=0.3):
    """Return a spacer sized for banner scale."""
    return Spacer(1, height_inches * inch)


def banner_hr():
    """Horizontal rule scaled for banner."""
    return HRFlowable(width="100%", thickness=3, color=BORDER_COLOR, spaceAfter=20, spaceBefore=20)


def thin_hr():
    """Thin horizontal rule."""
    return HRFlowable(width="100%", thickness=1.5, color=BORDER_COLOR, spaceAfter=12, spaceBefore=12)


def header_with_banner(story, product_name, tagline, website_url=None):
    """Add the standard header: Algolog banner image + product name + tagline."""
    if os.path.exists(BANNER_IMG_PATH):
        img = PILImage.open(BANNER_IMG_PATH)
        aspect = img.size[1] / img.size[0]
        display_w = AVAIL_W
        display_h = display_w * aspect
        banner = Image(BANNER_IMG_PATH, width=display_w, height=display_h)
        story.append(banner)

    story.append(banner_spacer(0.6))

    story.append(Paragraph(product_name, S_TITLE))
    story.append(Paragraph(tagline, S_TAGLINE))

    if website_url:
        story.append(Paragraph(website_url, S_URL))

    story.append(banner_spacer(0.3))
    story.append(banner_hr())


def problem_block(story, problem_text):
    """The Problem section — 2-3 sentence pain point in large text."""
    story.append(Paragraph("THE PROBLEM", S_SECTION_CENTER))
    story.append(banner_spacer(0.15))

    prob_para = Paragraph(problem_text, S_PROBLEM)
    prob_box = Table([[prob_para]], colWidths=[AVAIL_W * 0.9])
    prob_box.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), RED_LIGHT),
        ("TOPPADDING", (0, 0), (-1, -1), 30),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 30),
        ("LEFTPADDING", (0, 0), (-1, -1), 40),
        ("RIGHTPADDING", (0, 0), (-1, -1), 40),
        ("ROUNDEDCORNERS", [12, 12, 12, 12]),
    ]))
    prob_box.hAlign = "CENTER"
    story.append(prob_box)
    story.append(banner_spacer(0.3))


def value_prop_block(story, props):
    """
    Value propositions with numbered badges.
    props: list of (title, description) tuples
    """
    story.append(Paragraph("WHY IT MATTERS", S_SECTION_CENTER))
    story.append(banner_spacer(0.15))

    for i, (title, desc) in enumerate(props, 1):
        # Number badge + content in a row
        badge_para = Paragraph(str(i), S_BADGE_NUM)
        badge_box = Table([[badge_para]], colWidths=[60], rowHeights=[60])
        badge_box.setStyle(TableStyle([
            ("BACKGROUND", (0, 0), (-1, -1), ACCENT_BLUE),
            ("ALIGN", (0, 0), (-1, -1), "CENTER"),
            ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
            ("TOPPADDING", (0, 0), (-1, -1), 4),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
            ("ROUNDEDCORNERS", [8, 8, 8, 8]),
        ]))

        content_para = Paragraph(
            f'<font face="Lexend-SemiBold" color="#1a1a1a">{title}</font><br/>'
            f'<font face="Lexend" color="#333333">{desc}</font>',
            make_style(f"vp_{i}", fontSize=26, leading=36, textColor=MEDIUM_TEXT, spaceAfter=0))

        row = Table([[badge_box, content_para]], colWidths=[80, AVAIL_W * 0.88])
        row.setStyle(TableStyle([
            ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ("TOPPADDING", (0, 0), (-1, -1), 10),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 10),
            ("LEFTPADDING", (1, 0), (1, 0), 20),
            ("BACKGROUND", (0, 0), (-1, -1), TABLE_ALT_ROW if i % 2 == 0 else WHITE),
            ("ROUNDEDCORNERS", [8, 8, 8, 8]),
        ]))
        story.append(row)
        story.append(banner_spacer(0.1))

    story.append(banner_spacer(0.2))


def step_flow_block(story, steps, title="HOW IT WORKS"):
    """
    How-it-works step flow.
    steps: list of (step_title, step_description) tuples
    """
    story.append(Paragraph(title, S_SECTION_CENTER))
    story.append(banner_spacer(0.15))

    for i, (step_title, step_desc) in enumerate(steps, 1):
        num_para = Paragraph(str(i), S_STEP_NUM)
        num_box = Table([[num_para]], colWidths=[70], rowHeights=[70])
        num_box.setStyle(TableStyle([
            ("BACKGROUND", (0, 0), (-1, -1), GREEN),
            ("ALIGN", (0, 0), (-1, -1), "CENTER"),
            ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
            ("TOPPADDING", (0, 0), (-1, -1), 4),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
            ("ROUNDEDCORNERS", [35, 35, 35, 35]),
        ]))

        step_content = Paragraph(
            f'<font face="Lexend-SemiBold" size="30" color="#1a1a1a">{step_title}</font><br/>'
            f'<font face="Lexend" size="24" color="#333333">{step_desc}</font>',
            make_style(f"step_{i}", fontSize=26, leading=36, textColor=MEDIUM_TEXT, spaceAfter=0))

        # Arrow between steps (except last)
        row = Table([[num_box, step_content]], colWidths=[90, AVAIL_W * 0.88])
        row.setStyle(TableStyle([
            ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ("TOPPADDING", (0, 0), (-1, -1), 14),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 14),
            ("LEFTPADDING", (1, 0), (1, 0), 20),
        ]))
        story.append(row)

        if i < len(steps):
            # Vertical connector line
            arrow = Paragraph("|", make_style(f"arrow_{i}", fontName="Lexend-Light",
                              fontSize=36, leading=40, textColor=GREEN, alignment=TA_CENTER, spaceAfter=0))
            arrow_box = Table([[arrow]], colWidths=[90])
            arrow_box.setStyle(TableStyle([
                ("ALIGN", (0, 0), (-1, -1), "CENTER"),
                ("TOPPADDING", (0, 0), (-1, -1), 0),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
            ]))
            story.append(arrow_box)

    story.append(banner_spacer(0.3))


def case_study_box(story, client_name, before_text, after_text, quote=None):
    """Case study section with before/after or client quote."""
    story.append(Paragraph("PROVEN RESULTS", S_SECTION_CENTER))
    story.append(banner_spacer(0.15))

    # Client name
    story.append(Paragraph(client_name, make_style("cs_client", fontName="Lexend-Bold",
                 fontSize=34, leading=44, textColor=ACCENT_BLUE, alignment=TA_CENTER, spaceAfter=14)))

    # Before / After columns
    before_para = Paragraph(
        f'<font face="Lexend-SemiBold" color="#c0392b">BEFORE</font><br/><br/>'
        f'<font face="Lexend" color="#333333">{before_text}</font>',
        make_style("cs_before", fontSize=24, leading=34, textColor=MEDIUM_TEXT, spaceAfter=0))
    after_para = Paragraph(
        f'<font face="Lexend-SemiBold" color="#27ae60">AFTER</font><br/><br/>'
        f'<font face="Lexend" color="#333333">{after_text}</font>',
        make_style("cs_after", fontSize=24, leading=34, textColor=MEDIUM_TEXT, spaceAfter=0))

    col_w = (AVAIL_W * 0.9 - 30) / 2
    case_table = Table([[before_para, after_para]], colWidths=[col_w, col_w])
    case_table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (0, 0), RED_LIGHT),
        ("BACKGROUND", (1, 0), (1, 0), GREEN_LIGHT),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("TOPPADDING", (0, 0), (-1, -1), 24),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 24),
        ("LEFTPADDING", (0, 0), (-1, -1), 24),
        ("RIGHTPADDING", (0, 0), (-1, -1), 24),
        ("ROUNDEDCORNERS", [10, 10, 10, 10]),
    ]))
    case_table.hAlign = "CENTER"
    story.append(case_table)

    if quote:
        story.append(banner_spacer(0.2))
        quote_para = Paragraph(
            f'<i>"{quote}"</i>',
            make_style("cs_quote", fontName="Lexend-Light", fontSize=26, leading=36,
                        textColor=LIGHT_TEXT, alignment=TA_CENTER, spaceAfter=0))
        quote_box = Table([[quote_para]], colWidths=[AVAIL_W * 0.8])
        quote_box.setStyle(TableStyle([
            ("BACKGROUND", (0, 0), (-1, -1), BLUE_LIGHT),
            ("TOPPADDING", (0, 0), (-1, -1), 20),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 20),
            ("LEFTPADDING", (0, 0), (-1, -1), 30),
            ("RIGHTPADDING", (0, 0), (-1, -1), 30),
            ("ROUNDEDCORNERS", [10, 10, 10, 10]),
        ]))
        quote_box.hAlign = "CENTER"
        story.append(quote_box)

    story.append(banner_spacer(0.3))


def cta_block(story, cta_text="Book a Free Consultation", website=None):
    """Call to action block with contact details."""
    story.append(banner_spacer(0.2))

    # CTA heading
    cta_head = Paragraph(cta_text,
        make_style("cta_h", fontName="Lexend-Bold", fontSize=44, leading=54,
                    textColor=WHITE, alignment=TA_CENTER, spaceAfter=20))

    contact_lines = (
        '<font face="Lexend" size="30" color="#ffffff">'
        'Yasmin Umar  |  Chief Brand Strategist<br/>'
        'Call/WhatsApp: +234 706 905 7925<br/>'
        'Email: yasmin@algolog.co</font>'
    )
    contact_para = Paragraph(contact_lines,
        make_style("cta_contact", fontSize=30, leading=42, textColor=WHITE, alignment=TA_CENTER, spaceAfter=0))

    cta_content = [[cta_head], [contact_para]]
    if website:
        web_para = Paragraph(
            f'<font face="Lexend-Bold" size="34" color="#ffffff">{website}</font>',
            make_style("cta_web", fontSize=34, leading=44, textColor=WHITE, alignment=TA_CENTER, spaceAfter=0))
        cta_content.append([web_para])

    cta_table = Table(cta_content, colWidths=[AVAIL_W * 0.85])
    cta_table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), ACCENT_BLUE),
        ("ALIGN", (0, 0), (-1, -1), "CENTER"),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("TOPPADDING", (0, 0), (0, 0), 40),
        ("BOTTOMPADDING", (0, -1), (-1, -1), 40),
        ("LEFTPADDING", (0, 0), (-1, -1), 40),
        ("RIGHTPADDING", (0, 0), (-1, -1), 40),
        ("ROUNDEDCORNERS", [16, 16, 16, 16]),
    ]))
    cta_table.hAlign = "CENTER"
    story.append(cta_table)
    story.append(banner_spacer(0.3))


def feature_grid(story, features, title="FEATURES"):
    """
    Feature breakdown grid for back side.
    features: list of (feature_name, description) tuples (6-8 items)
    """
    story.append(Paragraph(title, S_SECTION_CENTER))
    story.append(banner_spacer(0.15))

    # Two-column layout
    rows = []
    col_w = (AVAIL_W - 40) / 2

    for i in range(0, len(features), 2):
        left_name, left_desc = features[i]
        left_para = Paragraph(
            f'<font face="Lexend-SemiBold" size="28" color="#0f3460">{left_name}</font><br/>'
            f'<font face="Lexend" size="22" color="#333333">{left_desc}</font>',
            make_style(f"fg_l_{i}", fontSize=24, leading=34, textColor=MEDIUM_TEXT, spaceAfter=0))

        if i + 1 < len(features):
            right_name, right_desc = features[i + 1]
            right_para = Paragraph(
                f'<font face="Lexend-SemiBold" size="28" color="#0f3460">{right_name}</font><br/>'
                f'<font face="Lexend" size="22" color="#333333">{right_desc}</font>',
                make_style(f"fg_r_{i}", fontSize=24, leading=34, textColor=MEDIUM_TEXT, spaceAfter=0))
        else:
            right_para = Paragraph("", make_style(f"fg_r_{i}", fontSize=24, spaceAfter=0))

        rows.append([left_para, right_para])

    feat_table = Table(rows, colWidths=[col_w, col_w])
    feat_table.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("TOPPADDING", (0, 0), (-1, -1), 18),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 18),
        ("LEFTPADDING", (0, 0), (-1, -1), 20),
        ("RIGHTPADDING", (0, 0), (-1, -1), 20),
        ("LINEBELOW", (0, 0), (-1, -2), 1, BORDER_COLOR),
    ]))
    feat_table.hAlign = "CENTER"
    story.append(feat_table)
    story.append(banner_spacer(0.3))


def who_its_for_block(story, audiences):
    """
    Target audience section.
    audiences: list of audience description strings
    """
    story.append(Paragraph("WHO IT'S FOR", S_SECTION_CENTER))
    story.append(banner_spacer(0.15))

    for aud in audiences:
        aud_para = Paragraph(
            f'<font face="Lexend-Medium" color="#0f3460">&#x2713;</font>  {aud}',
            make_style(f"aud_{id(aud)}", fontName="Lexend-Medium", fontSize=28, leading=40,
                        textColor=MEDIUM_TEXT, alignment=TA_LEFT, spaceAfter=8))
        box = Table([[aud_para]], colWidths=[AVAIL_W * 0.9])
        box.setStyle(TableStyle([
            ("BACKGROUND", (0, 0), (-1, -1), BLUE_LIGHT),
            ("TOPPADDING", (0, 0), (-1, -1), 14),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 14),
            ("LEFTPADDING", (0, 0), (-1, -1), 24),
            ("RIGHTPADDING", (0, 0), (-1, -1), 24),
            ("ROUNDEDCORNERS", [8, 8, 8, 8]),
        ]))
        box.hAlign = "CENTER"
        story.append(box)
        story.append(banner_spacer(0.08))

    story.append(banner_spacer(0.2))


def trust_elements_block(story, stats):
    """
    Trust elements / stats section.
    stats: list of (number_or_stat, label) tuples
    """
    story.append(Paragraph("BY THE NUMBERS", S_SECTION_CENTER))
    story.append(banner_spacer(0.15))

    # Create stat boxes in a row (up to 3 per row)
    col_w = (AVAIL_W - 60) / min(len(stats), 3)
    rows = []
    current_row = []

    for stat_val, stat_label in stats:
        stat_para = Paragraph(
            f'<font face="Lexend-Bold" size="48" color="#0f3460">{stat_val}</font><br/>'
            f'<font face="Lexend" size="22" color="#555555">{stat_label}</font>',
            make_style(f"stat_{id(stat_val)}", fontSize=36, leading=50,
                        textColor=ACCENT_BLUE, alignment=TA_CENTER, spaceAfter=0))
        current_row.append(stat_para)

        if len(current_row) == 3:
            rows.append(current_row)
            current_row = []

    if current_row:
        while len(current_row) < 3:
            current_row.append(Paragraph("", make_style(f"stat_empty_{len(current_row)}", spaceAfter=0)))
        rows.append(current_row)

    for row_data in rows:
        stat_table = Table([row_data], colWidths=[col_w] * 3)
        stat_table.setStyle(TableStyle([
            ("BACKGROUND", (0, 0), (-1, -1), TABLE_ALT_ROW),
            ("ALIGN", (0, 0), (-1, -1), "CENTER"),
            ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
            ("TOPPADDING", (0, 0), (-1, -1), 30),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 30),
            ("LEFTPADDING", (0, 0), (-1, -1), 16),
            ("RIGHTPADDING", (0, 0), (-1, -1), 16),
            ("ROUNDEDCORNERS", [10, 10, 10, 10]),
        ]))
        stat_table.hAlign = "CENTER"
        story.append(stat_table)
        story.append(banner_spacer(0.1))

    story.append(banner_spacer(0.2))


def pricing_hint_block(story, pricing_text):
    """Optional pricing hint."""
    story.append(Paragraph("PRICING", S_SECTION_CENTER))
    story.append(banner_spacer(0.1))

    price_para = Paragraph(pricing_text, S_PRICE)
    price_box = Table([[price_para]], colWidths=[AVAIL_W * 0.8])
    price_box.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), GREEN_LIGHT),
        ("TOPPADDING", (0, 0), (-1, -1), 24),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 24),
        ("LEFTPADDING", (0, 0), (-1, -1), 30),
        ("RIGHTPADDING", (0, 0), (-1, -1), 30),
        ("ROUNDEDCORNERS", [12, 12, 12, 12]),
    ]))
    price_box.hAlign = "CENTER"
    story.append(price_box)
    story.append(banner_spacer(0.3))


def about_algolog_block(story):
    """Standard About Algolog section for back side."""
    story.append(Paragraph("ABOUT ALGOLOG", S_SECTION_CENTER))
    story.append(banner_spacer(0.15))

    story.append(Paragraph(
        "Algolog Limited is a Nigerian technology company committed to ensuring businesses "
        "across Africa get the technology they need to build their future, improve their sales, "
        "and strengthen their operations.",
        S_ABOUT))

    story.append(Paragraph(
        "We build software solutions tailored to how African businesses actually operate "
        "\u2014 from hospitality management to AI analytics, from payment infrastructure to "
        "automated compliance systems.",
        S_ABOUT))

    # Products showcase
    products_text = (
        '<font face="Lexend-SemiBold" color="#0f3460">Our Products:</font><br/>'
        '<font face="Lexend" color="#333333">'
        'Spacer (spacer.so) \u2022 DeepThread (deepthread.ai) \u2022 Visora (visora.ai) \u2022 '
        'PrivateTransfer (privatetransfer.ng) \u2022 Pledged (autogiving.ng) \u2022 '
        'SkillPay (skillpay.link) \u2022 AutoCare \u2022 BDC System \u2022 '
        'BuyMeABeverage \u2022 BuyMeAShawarma</font>'
    )
    story.append(Paragraph(products_text,
        make_style("about_products", fontSize=24, leading=34, textColor=MEDIUM_TEXT, spaceAfter=14)))

    story.append(banner_spacer(0.2))


def contact_block(story):
    """Full contact details block for back side."""
    story.append(banner_spacer(0.2))

    contact_content = [
        [Paragraph(
            '<font face="Lexend-Bold" size="38" color="#ffffff">ALGOLOG LIMITED</font>',
            make_style("cb_name", fontSize=38, leading=48, textColor=WHITE, alignment=TA_CENTER, spaceAfter=0))],
        [Paragraph(
            '<font face="Lexend" size="28" color="#ffffff">'
            '5, Kwaji Close, Maitama, Abuja, Nigeria</font>',
            make_style("cb_addr", fontSize=28, leading=38, textColor=WHITE, alignment=TA_CENTER, spaceAfter=0))],
        [Paragraph(
            '<font face="Lexend-Medium" size="28" color="#ffffff">'
            'algolog.co  |  +234 808 396 5912</font>',
            make_style("cb_web", fontSize=28, leading=38, textColor=WHITE, alignment=TA_CENTER, spaceAfter=0))],
        [Paragraph(
            '<font face="Lexend" size="26" color="#ffffff">'
            'Yasmin Umar  |  yasmin@algolog.co  |  +234 706 905 7925</font>',
            make_style("cb_yasmin", fontSize=26, leading=36, textColor=WHITE, alignment=TA_CENTER, spaceAfter=0))],
    ]

    contact_table = Table(contact_content, colWidths=[AVAIL_W * 0.9])
    contact_table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), DARK_BG),
        ("ALIGN", (0, 0), (-1, -1), "CENTER"),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("TOPPADDING", (0, 0), (0, 0), 36),
        ("BOTTOMPADDING", (0, -1), (-1, -1), 36),
        ("TOPPADDING", (0, 1), (-1, -1), 8),
        ("BOTTOMPADDING", (0, 0), (-1, -2), 8),
        ("LEFTPADDING", (0, 0), (-1, -1), 40),
        ("RIGHTPADDING", (0, 0), (-1, -1), 40),
        ("ROUNDEDCORNERS", [16, 16, 16, 16]),
    ]))
    contact_table.hAlign = "CENTER"
    story.append(contact_table)
    story.append(banner_spacer(0.3))


def banner_footer(canvas_obj, doc):
    """Footer for banner pages."""
    canvas_obj.saveState()
    canvas_obj.setFont("Lexend-Light", 16)
    canvas_obj.setFillColor(LIGHT_TEXT)
    canvas_obj.drawCentredString(
        BANNER_W / 2, 0.5 * inch,
        "Algolog Limited  |  algolog.co  |  We build technology for African businesses"
    )
    canvas_obj.restoreState()


def build_banner_pdf(output_path, front_builder, back_builder):
    """
    Build a two-page banner PDF (front + back).
    front_builder: function(story) that adds front side content
    back_builder: function(story) that adds back side content
    """
    doc = SimpleDocTemplate(
        output_path,
        pagesize=BANNER_SIZE,
        leftMargin=BANNER_LEFT,
        rightMargin=BANNER_RIGHT,
        topMargin=BANNER_TOP,
        bottomMargin=BANNER_BOTTOM,
    )

    story = []

    # Front side
    front_builder(story)

    # Page break between front and back
    story.append(PageBreak())

    # Back side
    back_builder(story)

    doc.build(story, onFirstPage=banner_footer, onLaterPages=banner_footer)
    print(f"Banner PDF generated: {output_path}")
    print(f"File size: {os.path.getsize(output_path):,} bytes")
    return output_path


# --- Master Banner Specific Components ---

def product_showcase_item(name, one_liner, url):
    """Single product in the master banner grid."""
    return Paragraph(
        f'<font face="Lexend-Bold" size="30" color="#0f3460">{name}</font><br/>'
        f'<font face="Lexend" size="22" color="#333333">{one_liner}</font><br/>'
        f'<font face="Lexend-Medium" size="20" color="#0f3460">{url}</font>',
        make_style(f"ps_{id(name)}", fontSize=26, leading=34, textColor=MEDIUM_TEXT, spaceAfter=0))


def category_header_block(story, category_name):
    """Category divider for master banner product groups."""
    cat_para = Paragraph(category_name, S_CATEGORY)
    cat_box = Table([[cat_para]], colWidths=[AVAIL_W])
    cat_box.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), ACCENT_BLUE),
        ("TOPPADDING", (0, 0), (-1, -1), 14),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 14),
        ("LEFTPADDING", (0, 0), (-1, -1), 24),
        ("ROUNDEDCORNERS", [8, 8, 8, 8]),
    ]))
    story.append(cat_box)
    story.append(banner_spacer(0.1))


def product_grid_row(story, products):
    """
    Add products in a 2-column grid.
    products: list of (name, one_liner, url) tuples
    """
    col_w = (AVAIL_W - 30) / 2
    for i in range(0, len(products), 2):
        left = product_showcase_item(*products[i])
        if i + 1 < len(products):
            right = product_showcase_item(*products[i + 1])
        else:
            right = Paragraph("", make_style(f"pgr_empty_{i}", spaceAfter=0))

        row = Table([[left, right]], colWidths=[col_w, col_w])
        row.setStyle(TableStyle([
            ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ("TOPPADDING", (0, 0), (-1, -1), 16),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 16),
            ("LEFTPADDING", (0, 0), (-1, -1), 16),
            ("RIGHTPADDING", (0, 0), (-1, -1), 16),
            ("LINEBELOW", (0, 0), (-1, -1), 0.5, BORDER_COLOR),
        ]))
        story.append(row)


def mini_product_section(story, name, description, key_feature, url):
    """Mini product section for master banner back side."""
    content = Paragraph(
        f'<font face="Lexend-Bold" size="28" color="#0f3460">{name}</font><br/>'
        f'<font face="Lexend" size="22" color="#333333">{description}</font><br/>'
        f'<font face="Lexend-SemiBold" size="22" color="#27ae60">Key: {key_feature}</font><br/>'
        f'<font face="Lexend-Medium" size="20" color="#0f3460">{url}</font>',
        make_style(f"mps_{id(name)}", fontSize=24, leading=34, textColor=MEDIUM_TEXT, spaceAfter=0))
    box = Table([[content]], colWidths=[AVAIL_W * 0.95])
    box.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), TABLE_ALT_ROW),
        ("TOPPADDING", (0, 0), (-1, -1), 16),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 16),
        ("LEFTPADDING", (0, 0), (-1, -1), 20),
        ("RIGHTPADDING", (0, 0), (-1, -1), 20),
        ("ROUNDEDCORNERS", [8, 8, 8, 8]),
    ]))
    box.hAlign = "CENTER"
    story.append(box)
    story.append(banner_spacer(0.1))


def competencies_block(story, competencies):
    """Core competencies grid."""
    story.append(Paragraph("CORE COMPETENCIES", S_SECTION_CENTER))
    story.append(banner_spacer(0.15))

    col_w = (AVAIL_W - 40) / 2
    rows = []
    current_row = []

    for comp in competencies:
        comp_para = Paragraph(
            f'<font face="Lexend-SemiBold" size="28" color="#0f3460">{comp}</font>',
            make_style(f"comp_{id(comp)}", fontSize=28, leading=36,
                        textColor=ACCENT_BLUE, alignment=TA_CENTER, spaceAfter=0))
        current_row.append(comp_para)
        if len(current_row) == 2:
            rows.append(current_row)
            current_row = []

    if current_row:
        current_row.append(Paragraph("", make_style("comp_empty", spaceAfter=0)))
        rows.append(current_row)

    for row_data in rows:
        comp_table = Table([row_data], colWidths=[col_w, col_w])
        comp_table.setStyle(TableStyle([
            ("BACKGROUND", (0, 0), (-1, -1), BLUE_LIGHT),
            ("ALIGN", (0, 0), (-1, -1), "CENTER"),
            ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
            ("TOPPADDING", (0, 0), (-1, -1), 20),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 20),
            ("LEFTPADDING", (0, 0), (-1, -1), 16),
            ("RIGHTPADDING", (0, 0), (-1, -1), 16),
            ("ROUNDEDCORNERS", [10, 10, 10, 10]),
        ]))
        story.append(comp_table)
        story.append(banner_spacer(0.08))

    story.append(banner_spacer(0.2))


def team_block(story, members):
    """
    Team section.
    members: list of (name, role) tuples
    """
    story.append(Paragraph("LEADERSHIP", S_SECTION_CENTER))
    story.append(banner_spacer(0.15))

    for name, role in members:
        story.append(Paragraph(
            f'<font face="Lexend-Bold" color="#1a1a1a">{name}</font>  '
            f'<font face="Lexend" color="#555555">\u2014  {role}</font>',
            make_style(f"team_{id(name)}", fontSize=26, leading=36,
                        textColor=DARK_TEXT, alignment=TA_CENTER, spaceAfter=8)))

    story.append(banner_spacer(0.2))


def client_references_block(story, clients):
    """
    Client references.
    clients: list of (client_name, brief_description) tuples
    """
    story.append(Paragraph("CLIENT REFERENCES", S_SECTION_CENTER))
    story.append(banner_spacer(0.15))

    for client, desc in clients:
        ref_para = Paragraph(
            f'<font face="Lexend-SemiBold" color="#1a1a1a">{client}</font><br/>'
            f'<font face="Lexend" color="#333333">{desc}</font>',
            make_style(f"ref_{id(client)}", fontSize=24, leading=34, textColor=MEDIUM_TEXT, spaceAfter=0))
        box = Table([[ref_para]], colWidths=[AVAIL_W * 0.9])
        box.setStyle(TableStyle([
            ("BACKGROUND", (0, 0), (-1, -1), GREEN_LIGHT),
            ("TOPPADDING", (0, 0), (-1, -1), 14),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 14),
            ("LEFTPADDING", (0, 0), (-1, -1), 20),
            ("RIGHTPADDING", (0, 0), (-1, -1), 20),
            ("ROUNDEDCORNERS", [8, 8, 8, 8]),
        ]))
        box.hAlign = "CENTER"
        story.append(box)
        story.append(banner_spacer(0.08))

    story.append(banner_spacer(0.2))
