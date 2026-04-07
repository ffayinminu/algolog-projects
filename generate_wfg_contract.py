"""
Generate WorkingForGod.org — Project Agreement & Contract PDF
Client: Nwamaka Okoye / Nnaemeka Okoye
Format: Matches Algolog standard (banner header, Lexend font, professional layout)
"""

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import inch, mm
from reportlab.lib.colors import HexColor
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Image, Table, TableStyle,
    PageBreak, HRFlowable, KeepTogether
)
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import os

# --- Paths ---
BASE = "C:/Users/Femi Fayinminu/OneDrive/Documents/Algolog/Algolog_Projects"
FONT_DIR = os.path.join(BASE, "fonts/lexend-main/fonts/lexend/ttf")
BANNER_PATH = os.path.join(BASE, "claude.ai contex/Algolog_banner_cropped.png")
OUTPUT_PATH = os.path.join(BASE, "Proposals/Agreement-WorkingForGod.pdf")

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
GREEN = HexColor("#27ae60")
DARK_TEXT = HexColor("#1a1a1a")
MEDIUM_TEXT = HexColor("#333333")
LIGHT_TEXT = HexColor("#555555")
TABLE_HEADER_BG = HexColor("#1a1a2e")
TABLE_ALT_ROW = HexColor("#f5f6fa")
BORDER_COLOR = HexColor("#dcdde1")

# --- Page Setup ---
PAGE_W, PAGE_H = A4
LEFT_MARGIN = 22 * mm
RIGHT_MARGIN = 22 * mm
TOP_MARGIN = 20 * mm
BOTTOM_MARGIN = 20 * mm

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
S_CALLOUT_GREEN = make_style("S_CALLOUT_GREEN", fontName="Lexend-SemiBold", fontSize=10, leading=14, textColor=GREEN, spaceAfter=8, spaceBefore=8)
S_TABLE_HEADER = make_style("S_TABLE_HEADER", fontName="Lexend-Bold", fontSize=9, leading=12, textColor=HexColor("#ffffff"))
S_TABLE_CELL = make_style("S_TABLE_CELL", fontSize=9, leading=12, textColor=MEDIUM_TEXT)
S_TABLE_CELL_BOLD = make_style("S_TABLE_CELL_BOLD", fontName="Lexend-Bold", fontSize=9, leading=12, textColor=DARK_TEXT)

CLIENT_NAME = "AiMP Network"
PROJECT_NAME = "WorkingForGod.org"


def add_header_footer(canvas_obj, doc):
    canvas_obj.saveState()
    canvas_obj.setFont("Lexend-Light", 7)
    canvas_obj.setFillColor(LIGHT_TEXT)
    canvas_obj.drawCentredString(
        PAGE_W / 2, 12 * mm,
        f"Algolog Limited  |  Confidential  |  Project Agreement \u2014 {PROJECT_NAME}  |  Page {doc.page}"
    )
    canvas_obj.restoreState()


def hr():
    return HRFlowable(width="100%", thickness=0.5, color=BORDER_COLOR, spaceAfter=8, spaceBefore=8)


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

    story.append(Paragraph(
        "Project Agreement",
        make_style("cover_title", fontName="Lexend-Bold", fontSize=26, leading=32, textColor=ACCENT_BLUE, alignment=TA_CENTER, spaceAfter=6)
    ))
    story.append(Paragraph(
        "WorkingForGod.org",
        make_style("cover_sub1", fontName="Lexend-SemiBold", fontSize=18, leading=24, textColor=DARK_TEXT, alignment=TA_CENTER, spaceAfter=4)
    ))
    story.append(Paragraph(
        "Christian Professional Training Platform",
        make_style("cover_sub2", fontName="Lexend-Medium", fontSize=13, leading=18, textColor=LIGHT_TEXT, alignment=TA_CENTER, spaceAfter=6)
    ))

    story.append(Spacer(1, 12 * mm))
    story.append(hr())
    story.append(Spacer(1, 6 * mm))

    info_data = [
        [Paragraph("<b>Prepared for:</b>", S_TABLE_CELL_BOLD), Paragraph("<b>Prepared by:</b>", S_TABLE_CELL_BOLD)],
        [Paragraph("AiMP (Apostles In The Market Place)", S_TABLE_CELL), Paragraph("Algolog Limited", S_TABLE_CELL)],
        [Paragraph("Network", S_TABLE_CELL),
         Paragraph("Plot 1387 Aminu Kano Crescent,<br/>Wuse, Abuja", S_TABLE_CELL)],
        [Paragraph("", S_TABLE_CELL), Paragraph("ffayinminu@algolog.co<br/>+234 705 301 6348", S_TABLE_CELL)],
        [Paragraph("", S_TABLE_CELL), Paragraph("Fayinminu Femi<br/>Senior Business Developer", S_TABLE_CELL)],
    ]
    info_table = Table(info_data, colWidths=[avail_w * 0.5, avail_w * 0.5])
    info_table.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("TOPPADDING", (0, 0), (-1, -1), 4),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
        ("LEFTPADDING", (0, 0), (-1, -1), 8),
        ("LINEBELOW", (0, 0), (-1, 0), 0.5, BORDER_COLOR),
    ]))
    story.append(info_table)

    story.append(Spacer(1, 12 * mm))
    story.append(Paragraph("April 2026", make_style("date", fontName="Lexend-Medium", fontSize=11, textColor=LIGHT_TEXT, alignment=TA_CENTER)))

    story.append(PageBreak())

    # =====================================================
    # SECTION 1: PROJECT OVERVIEW
    # =====================================================
    story.append(Paragraph("1. PROJECT OVERVIEW", S_H1))
    story.append(hr())

    story.append(Paragraph(
        "This agreement outlines the scope of work, deliverables, technical specifications, payment terms, "
        "support commitments, and ownership details for the design, development, and deployment of "
        "<b>WorkingForGod.org</b> \u2014 a Christian-based professional development and discipleship platform.", S_BODY))

    story.append(Paragraph(
        "WorkingForGod.org is envisioned as a comprehensive platform that equips individuals and organizations "
        "with faith-centered educational resources. The platform will provide structured video-based courses, "
        "articles, community features, and learning materials inspired by Masterclass.com and LinkedIn Learning, "
        "tailored to Christian professionals seeking to integrate faith and excellence in their career pursuits.", S_BODY))

    story.append(Spacer(1, 3 * mm))
    story.append(Paragraph("<b>Parties to this Agreement:</b>", S_BODY_BOLD))
    story.append(Paragraph(
        "\u2022  <b>The Client:</b> AiMP (Apostles In The Market Place) Network, represented by Nwamaka Okoye", S_BULLET))
    story.append(Paragraph(
        "\u2022  <b>The Developer:</b> Algolog Limited, a technology company registered in Nigeria", S_BULLET))

    story.append(PageBreak())

    # =====================================================
    # SECTION 2: SCOPE OF WORK
    # =====================================================
    story.append(Paragraph("2. SCOPE OF WORK & DELIVERABLES", S_H1))
    story.append(hr())

    story.append(Paragraph("The following components are included in this project:", S_BODY))

    story.append(Spacer(1, 3 * mm))
    story.append(Paragraph("A. UI/UX Prototype (Completed)", S_H2))
    story.append(Paragraph(
        "A high-fidelity interactive Figma prototype has been designed and delivered, covering all core screens "
        "and user flows. This prototype has been reviewed and approved as the foundation for development.", S_BODY))

    story.append(Spacer(1, 3 * mm))
    story.append(Paragraph("B. Full Platform Development", S_H2))
    story.append(Paragraph(
        "The following features and modules will be built as part of the platform:", S_BODY))

    modules = [
        ("Landing / Home Page", [
            "Professional, faith-aligned hero section with mission tagline",
            "Featured trainers section with photos and bios",
            "Featured courses section with thumbnails",
            "Testimonials slider",
            "Dual CTA for individuals and organizations",
            "Dynamic course counters and trainer highlights",
        ]),
        ("Course Library & Training Modules", [
            "Curated courses segmented by themes (Leadership, Career Growth, Integrity, Business Ethics)",
            "Video player with chapter/section navigation",
            "Progress bar tracking per course",
            "\u201cContinue Watching\u201d functionality for returning users",
            "Reflection and discussion questions after each video segment",
            "Downloadable resources per course (PDF guides, scripture references)",
            "Bookmarking and related courses feature",
            "Free-tier access for teaser content",
        ]),
        ("Article & Resources Library", [
            "Categorized articles by theme",
            "Search and filter functionality",
            "Grid/list view with thumbnails, titles, and summaries",
            "Embedded content support (YouTube sermons, teaching clips)",
        ]),
        ("Community Forum", [
            "\u201cPost a Dilemma\u201d feature \u2014 users anonymously submit real ethical or workplace issues",
            "Moderated forum with biblical feedback from trusted contributors",
            "Categorized discussions",
        ]),
        ("Events & Speakers Section", [
            "Future conferences and speaker lineup",
            "Faith-based workplace event promotions and announcements",
        ]),
        ("Subscription & Payment System", [
            "Individual plans: Monthly and Yearly subscription options",
            "Organization plans: Tiered pricing based on number of seats",
            "Payment gateway integration",
            "Admin dashboard for organizations to monitor staff participation",
        ]),
        ("User Profile & Dashboard", [
            "Track completed courses and progress",
            "Save/bookmark articles and favourite lessons",
            "Subscription management",
            "Course history",
        ]),
        ("About Us & Mission Page", [
            "Vision and mission statement",
            "Core scriptures that guide the platform",
            "Platform goals and narrative",
        ]),
        ("Content Management System (CMS)", [
            "Admin panel for easy upload of videos, articles, and resources",
            "User management and subscription monitoring",
            "Analytics \u2014 track user engagement, content performance, and growth metrics",
            "Forum moderation tools",
        ]),
    ]

    for title, bullets in modules:
        story.append(Paragraph(title, S_H3))
        for b in bullets:
            story.append(Paragraph(f"\u2022  {b}", S_BULLET))
        story.append(Spacer(1, 1 * mm))

    story.append(PageBreak())

    # =====================================================
    # SECTION 3: TECHNICAL SPECIFICATIONS
    # =====================================================
    story.append(Paragraph("3. TECHNICAL SPECIFICATIONS", S_H1))
    story.append(hr())

    story.append(Paragraph("The platform will be built using the following technologies:", S_BODY))
    story.append(Spacer(1, 3 * mm))

    tech_data = [
        [Paragraph("<b>Component</b>", S_TABLE_HEADER), Paragraph("<b>Technology</b>", S_TABLE_HEADER)],
        [Paragraph("Server Runtime", S_TABLE_CELL), Paragraph("Node.js (JavaScript)", S_TABLE_CELL)],
        [Paragraph("Frontend Framework", S_TABLE_CELL), Paragraph("Next.js + React.js", S_TABLE_CELL)],
        [Paragraph("Cloud Hosting", S_TABLE_CELL), Paragraph("Microsoft Azure", S_TABLE_CELL)],
        [Paragraph("Infrastructure", S_TABLE_CELL), Paragraph("Terraform (Infrastructure as Code)", S_TABLE_CELL)],
        [Paragraph("Database", S_TABLE_CELL), Paragraph("PostgreSQL", S_TABLE_CELL)],
        [Paragraph("Security Standard", S_TABLE_CELL), Paragraph("OWASP (industry standard for web application security)", S_TABLE_CELL)],
        [Paragraph("Video Delivery", S_TABLE_CELL), Paragraph("HLS streaming + YouTube embeds", S_TABLE_CELL)],
        [Paragraph("Payment Integration", S_TABLE_CELL), Paragraph("Paystack (or equivalent)", S_TABLE_CELL)],
    ]
    tech_table = Table(tech_data, colWidths=[avail_w * 0.35, avail_w * 0.65])
    tech_table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), TABLE_HEADER_BG),
        ("TEXTCOLOR", (0, 0), (-1, 0), HexColor("#ffffff")),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("TOPPADDING", (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
        ("LEFTPADDING", (0, 0), (-1, -1), 8),
        ("RIGHTPADDING", (0, 0), (-1, -1), 8),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [HexColor("#ffffff"), TABLE_ALT_ROW]),
        ("LINEBELOW", (0, 0), (-1, -2), 0.25, BORDER_COLOR),
        ("BOX", (0, 0), (-1, -1), 0.5, BORDER_COLOR),
    ]))
    story.append(tech_table)

    story.append(Spacer(1, 6 * mm))
    story.append(Paragraph("Key Technical Commitments:", S_H3))
    story.append(Paragraph("\u2022  Fully responsive design (desktop, tablet, and mobile)", S_BULLET))
    story.append(Paragraph("\u2022  OWASP security standard compliance \u2014 the widely accepted security standard for software applications", S_BULLET))
    story.append(Paragraph("\u2022  Scalable cloud infrastructure on Azure", S_BULLET))
    story.append(Paragraph("\u2022  Regular backups and security services", S_BULLET))
    story.append(Paragraph("\u2022  CDN for optimized video streaming", S_BULLET))

    story.append(PageBreak())

    # =====================================================
    # SECTION 4: PROJECT INVESTMENT
    # =====================================================
    story.append(Paragraph("4. PROJECT INVESTMENT", S_H1))
    story.append(hr())

    story.append(Paragraph(
        "The total project cost covers full platform development, deployment, quality testing, "
        "CMS setup, payment integration, and staff training.", S_BODY))

    story.append(Spacer(1, 4 * mm))

    cost_data = [
        [Paragraph("<b>Phase</b>", S_TABLE_HEADER), Paragraph("<b>Cost (NGN)</b>", S_TABLE_HEADER)],
        [Paragraph("Frontend Development", S_TABLE_CELL), Paragraph("Included", S_TABLE_CELL)],
        [Paragraph("Backend Development", S_TABLE_CELL), Paragraph("Included", S_TABLE_CELL)],
        [Paragraph("Subscription & Payment Integration", S_TABLE_CELL), Paragraph("Included", S_TABLE_CELL)],
        [Paragraph("Content Management System Setup", S_TABLE_CELL), Paragraph("Included", S_TABLE_CELL)],
        [Paragraph("Deployment & Quality Testing", S_TABLE_CELL), Paragraph("Included", S_TABLE_CELL)],
        [Paragraph("Staff Training & Manual", S_TABLE_CELL), Paragraph("Included", S_TABLE_CELL)],
        [Paragraph("<b>Total Project Cost</b>", S_TABLE_CELL_BOLD),
         Paragraph("<b>\u20a68,900,000</b>", S_TABLE_CELL_BOLD)],
    ]
    cost_table = Table(cost_data, colWidths=[avail_w * 0.6, avail_w * 0.4])
    cost_table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), TABLE_HEADER_BG),
        ("TEXTCOLOR", (0, 0), (-1, 0), HexColor("#ffffff")),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("TOPPADDING", (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
        ("LEFTPADDING", (0, 0), (-1, -1), 8),
        ("RIGHTPADDING", (0, 0), (-1, -1), 8),
        ("ROWBACKGROUNDS", (0, 1), (-1, -2), [HexColor("#ffffff"), TABLE_ALT_ROW]),
        ("LINEBELOW", (0, 0), (-1, -2), 0.25, BORDER_COLOR),
        ("LINEABOVE", (0, -1), (-1, -1), 1, ACCENT_BLUE),
        ("BOX", (0, 0), (-1, -1), 0.5, BORDER_COLOR),
    ]))
    story.append(cost_table)

    story.append(Spacer(1, 6 * mm))
    story.append(Paragraph("Payment Schedule:", S_H2))

    payment_data = [
        [Paragraph("<b>Milestone</b>", S_TABLE_HEADER),
         Paragraph("<b>Amount (NGN)</b>", S_TABLE_HEADER)],
        [Paragraph("Upfront Payment (Project Commencement)", S_TABLE_CELL),
         Paragraph("\u20a65,000,000", S_TABLE_CELL)],
        [Paragraph("Balance on Completion (Deployment & Handover)", S_TABLE_CELL),
         Paragraph("\u20a63,900,000", S_TABLE_CELL)],
        [Paragraph("<b>Total</b>", S_TABLE_CELL_BOLD),
         Paragraph("<b>\u20a68,900,000</b>", S_TABLE_CELL_BOLD)],
    ]
    payment_table = Table(payment_data, colWidths=[avail_w * 0.6, avail_w * 0.4])
    payment_table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), TABLE_HEADER_BG),
        ("TEXTCOLOR", (0, 0), (-1, 0), HexColor("#ffffff")),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("TOPPADDING", (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
        ("LEFTPADDING", (0, 0), (-1, -1), 8),
        ("RIGHTPADDING", (0, 0), (-1, -1), 8),
        ("ROWBACKGROUNDS", (0, 1), (-1, -2), [HexColor("#ffffff"), TABLE_ALT_ROW]),
        ("LINEBELOW", (0, 0), (-1, -2), 0.25, BORDER_COLOR),
        ("LINEABOVE", (0, -1), (-1, -1), 1, ACCENT_BLUE),
        ("BOX", (0, 0), (-1, -1), 0.5, BORDER_COLOR),
    ]))
    story.append(payment_table)

    story.append(Spacer(1, 4 * mm))
    story.append(Paragraph(
        "<b>Note:</b> The total project cost excludes cloud hosting fees, which are billed directly by the "
        "cloud provider (Microsoft Azure) based on usage. Algolog will assist with setup and configuration.", S_BODY))

    story.append(PageBreak())

    # =====================================================
    # SECTION 5: PROJECT TIMELINE
    # =====================================================
    story.append(Paragraph("5. PROJECT TIMELINE", S_H1))
    story.append(hr())

    story.append(Paragraph(
        "The full project will be delivered within <b>6 weeks</b> from the date of project commencement.", S_BODY))

    story.append(Spacer(1, 4 * mm))
    story.append(Paragraph(
        "Development begins upon receipt of the upfront payment (\u20a65,000,000). This timeline "
        "assumes timely provision of content (course videos, articles, trainer bios, and images) by the client.", S_BODY))

    story.append(Spacer(1, 8 * mm))

    # =====================================================
    # SECTION 6: TRAINING & HANDOVER
    # =====================================================
    story.append(Paragraph("6. TRAINING & HANDOVER", S_H1))
    story.append(hr())

    story.append(Paragraph(
        "Upon completion of development and deployment, the following will be provided:", S_BODY))
    story.append(Spacer(1, 2 * mm))

    story.append(Paragraph("\u2022  <b>Staff Training:</b> All designated staff will be trained on how to use and manage the platform, "
                           "including the CMS, user management, content uploads, and subscription monitoring", S_BULLET))
    story.append(Paragraph("\u2022  <b>Comprehensive Manual:</b> A written user manual/guide will be delivered covering all platform "
                           "features and administrative functions", S_BULLET))
    story.append(Paragraph("\u2022  <b>Admin Access:</b> Full administrative access to the platform, CMS, and hosting dashboard", S_BULLET))

    story.append(Spacer(1, 8 * mm))

    # =====================================================
    # SECTION 7: SUPPORT & MAINTENANCE
    # =====================================================
    story.append(Paragraph("7. SUPPORT & MAINTENANCE", S_H1))
    story.append(hr())

    story.append(Paragraph(
        "Algolog Limited is committed to providing ongoing support for the WorkingForGod.org platform "
        "under the following terms:", S_BODY))
    story.append(Spacer(1, 3 * mm))

    story.append(Paragraph("What is Included (at no additional cost):", S_H3))
    story.append(Paragraph("\u2022  Free life-long technical support for any issues, bugs, or questions related to the "
                           "features and functionality delivered as part of this agreement", S_BULLET))
    story.append(Paragraph("\u2022  Bug fixes and troubleshooting within the originally agreed scope", S_BULLET))
    story.append(Paragraph("\u2022  Guidance on platform usage, content management, and administrative functions", S_BULLET))
    story.append(Paragraph("\u2022  Security patches and critical updates to maintain platform stability", S_BULLET))

    story.append(Spacer(1, 3 * mm))
    story.append(Paragraph("What Requires Separate Discussion:", S_H3))
    story.append(Paragraph("\u2022  New features, modules, or functionality not included in the original scope of this agreement", S_BULLET))
    story.append(Paragraph("\u2022  Significant redesigns or UI overhauls beyond the approved prototype", S_BULLET))
    story.append(Paragraph("\u2022  Integration with third-party systems not specified in this agreement", S_BULLET))
    story.append(Paragraph("\u2022  Mobile app development (Android/iOS)", S_BULLET))

    story.append(Spacer(1, 3 * mm))
    story.append(Paragraph(
        "Any requests that fall outside the scope of what was originally agreed and delivered will require "
        "a separate discussion to determine scope, timeline, and cost.", S_BODY))

    story.append(PageBreak())

    # =====================================================
    # SECTION 8: OWNERSHIP & INTELLECTUAL PROPERTY
    # =====================================================
    story.append(Paragraph("8. OWNERSHIP & INTELLECTUAL PROPERTY", S_H1))
    story.append(hr())

    story.append(Paragraph(
        "Upon full payment of the total project cost (\u20a68,900,000), the following ownership rights transfer "
        "to the Client:", S_BODY))
    story.append(Spacer(1, 2 * mm))

    story.append(Paragraph("\u2022  Full ownership of the WorkingForGod.org platform, including all source code, "
                           "design assets, and documentation", S_BULLET))
    story.append(Paragraph("\u2022  The platform is the Client\u2019s property \u2014 the Client is free to manage, modify, "
                           "or extend it independently", S_BULLET))
    story.append(Paragraph("\u2022  No recurring licensing fees or ownership restrictions from Algolog Limited", S_BULLET))
    story.append(Paragraph("\u2022  All login credentials, API keys, hosting access, and administrative controls "
                           "will be handed over to the Client", S_BULLET))

    story.append(Spacer(1, 4 * mm))
    story.append(Paragraph(
        "Algolog Limited retains the right to reference WorkingForGod.org in its portfolio as a completed project, "
        "unless otherwise requested by the Client.", S_BODY))

    story.append(Spacer(1, 8 * mm))

    # =====================================================
    # SECTION 9: CLOUD HOSTING
    # =====================================================
    story.append(Paragraph("9. CLOUD HOSTING & INFRASTRUCTURE", S_H1))
    story.append(hr())

    story.append(Paragraph(
        "The platform will be hosted on <b>Microsoft Azure</b> (or equivalent cloud provider). "
        "Hosting is a separate, ongoing cost paid directly to the cloud provider.", S_BODY))
    story.append(Spacer(1, 2 * mm))

    story.append(Paragraph("\u2022  Algolog will set up and configure the cloud infrastructure as part of the project", S_BULLET))
    story.append(Paragraph("\u2022  Hosting includes secure servers, scalable storage, CDN for video streaming, regular backups, and security services", S_BULLET))
    story.append(Paragraph("\u2022  Hosting costs scale with the user base and data volume", S_BULLET))
    story.append(Paragraph("\u2022  The Client will have full access to the hosting dashboard and billing", S_BULLET))

    story.append(Spacer(1, 8 * mm))

    # =====================================================
    # SECTION 10: TERMS & CONDITIONS
    # =====================================================
    story.append(Paragraph("10. TERMS & CONDITIONS", S_H1))
    story.append(hr())

    terms = [
        "This agreement becomes effective upon receipt of the upfront payment (\u20a65,000,000).",
        "The project timeline begins from the date of upfront payment receipt.",
        "Timely provision of content (videos, articles, images, trainer information) by the Client is essential "
        "to meeting the stated timeline. Delays in content delivery may extend the project duration.",
        "This agreement and the quoted costs are valid for 30 days from the date of issuance.",
        "Any modifications to the scope of work after commencement will be documented as an addendum "
        "to this agreement with adjusted costs and timelines as applicable.",
        "Either party may terminate this agreement with 14 days\u2019 written notice. In the event of termination, "
        "the Client will be billed for work completed up to the date of termination.",
    ]
    for i, term in enumerate(terms, 1):
        story.append(Paragraph(f"{i}. {term}", S_NUMBEREDITEM))
        story.append(Spacer(1, 1 * mm))

    story.append(PageBreak())

    # =====================================================
    # SECTION 11: ACCEPTANCE & SIGNATURES
    # =====================================================
    story.append(Paragraph("11. ACCEPTANCE", S_H1))
    story.append(hr())

    story.append(Paragraph(
        "By signing below, both parties acknowledge and agree to the terms, scope, deliverables, "
        "payment schedule, and conditions outlined in this agreement.", S_BODY))

    story.append(Spacer(1, 12 * mm))

    # Signature block
    sig_data = [
        [Paragraph("<b>For the Client:</b>", S_TABLE_CELL_BOLD),
         Paragraph("<b>For Algolog Limited:</b>", S_TABLE_CELL_BOLD)],
        [Paragraph("", S_TABLE_CELL), Paragraph("", S_TABLE_CELL)],
        [Paragraph("", S_TABLE_CELL), Paragraph("", S_TABLE_CELL)],
        [Paragraph("____________________________", S_TABLE_CELL),
         Paragraph("____________________________", S_TABLE_CELL)],
        [Paragraph("Nwamaka Okoye", S_TABLE_CELL_BOLD),
         Paragraph("Fayinminu Femi", S_TABLE_CELL_BOLD)],
        [Paragraph("AiMP (Apostles In The Market Place)", S_TABLE_CELL),
         Paragraph("Senior Business Developer", S_TABLE_CELL)],
        [Paragraph("Network", S_TABLE_CELL),
         Paragraph("Algolog Limited", S_TABLE_CELL)],
        [Paragraph("", S_TABLE_CELL), Paragraph("", S_TABLE_CELL)],
        [Paragraph("Date: ____________________", S_TABLE_CELL),
         Paragraph("Date: ____________________", S_TABLE_CELL)],
    ]
    sig_table = Table(sig_data, colWidths=[avail_w * 0.5, avail_w * 0.5])
    sig_table.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("TOPPADDING", (0, 0), (-1, -1), 4),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
        ("LEFTPADDING", (0, 0), (-1, -1), 8),
    ]))
    story.append(sig_table)

    story.append(Spacer(1, 16 * mm))
    story.append(hr())
    story.append(Spacer(1, 4 * mm))

    story.append(Paragraph(
        "We look forward to partnering with you to bring WorkingForGod.org to life, creating a lasting "
        "impact on Christian professionals globally.",
        make_style("closing1", fontName="Lexend-Medium", fontSize=9.5, leading=14, textColor=MEDIUM_TEXT, alignment=TA_CENTER)))

    story.append(Spacer(1, 10 * mm))
    story.append(hr())
    story.append(Paragraph("Algolog Limited", make_style("footer_co", fontName="Lexend-Bold", fontSize=10, textColor=DARK_TEXT, alignment=TA_CENTER)))
    story.append(Paragraph("Plot 1387 Aminu Kano Crescent, Wuse, Abuja  |  algolog.co", S_HEADER_INFO))
    story.append(Spacer(1, 3 * mm))
    story.append(Paragraph("Prepared with care for WorkingForGod.org \u2014 April 2026", S_SMALL))

    # Build
    doc.build(story, onFirstPage=add_header_footer, onLaterPages=add_header_footer)
    print(f"PDF generated: {OUTPUT_PATH}")
    print(f"File size: {os.path.getsize(OUTPUT_PATH):,} bytes")


if __name__ == "__main__":
    build_pdf()
