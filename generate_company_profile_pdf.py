"""
Generate Algolog Company Profile PDF — Black & White Design
"""

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib.colors import HexColor, white, black
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY, TA_RIGHT
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Image, Table, TableStyle,
    PageBreak, HRFlowable, KeepTogether, Frame, PageTemplate, BaseDocTemplate
)
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.graphics.shapes import Drawing, Rect, String, Line
from reportlab.platypus.flowables import Flowable
import os

BASE = "C:/Users/Femi Fayinminu/OneDrive/Documents/Algolog/Algolog_Projects"
FONT_DIR = os.path.join(BASE, "fonts/lexend-main/fonts/lexend/ttf")
BANNER_PATH = os.path.join(BASE, "claude.ai contex/Algolog_banner_cropped.png")
LOGO_PATH = os.path.join(BASE, "claude.ai contex/algolog_logo_watermark.png")
OUTPUT_PATH = os.path.join(BASE, "Proposals/Algolog-Company-Profile.pdf")

pdfmetrics.registerFont(TTFont("Lexend", os.path.join(FONT_DIR, "Lexend-Regular.ttf")))
pdfmetrics.registerFont(TTFont("Lexend-Bold", os.path.join(FONT_DIR, "Lexend-Bold.ttf")))
pdfmetrics.registerFont(TTFont("Lexend-SemiBold", os.path.join(FONT_DIR, "Lexend-SemiBold.ttf")))
pdfmetrics.registerFont(TTFont("Lexend-Light", os.path.join(FONT_DIR, "Lexend-Light.ttf")))
pdfmetrics.registerFont(TTFont("Lexend-Medium", os.path.join(FONT_DIR, "Lexend-Medium.ttf")))
pdfmetrics.registerFontFamily("Lexend", normal="Lexend", bold="Lexend-Bold", italic="Lexend", boldItalic="Lexend-Bold")

BLACK = HexColor("#111111")
DARK = HexColor("#1a1a1a")
MID_GREY = HexColor("#333333")
LIGHT_GREY = HexColor("#555555")
VERY_LIGHT = HexColor("#f0f0f0")
WHITE = HexColor("#ffffff")
ACCENT = HexColor("#0f3460")

PAGE_W, PAGE_H = A4
MARGIN = 20 * mm


class BlackPageBreak(Flowable):
    """A full-black page with centered white text"""
    def __init__(self, page_num, title, subtitle=None):
        Flowable.__init__(self)
        self.width = PAGE_W
        self.height = PAGE_H
        self.page_num = page_num
        self.title = title
        self.subtitle = subtitle

    def draw(self):
        c = self.canv
        c.saveState()
        c.setFillColor(BLACK)
        c.rect(-MARGIN, -MARGIN, PAGE_W, PAGE_H, fill=1, stroke=0)

        # Page number box
        c.setFillColor(WHITE)
        box_w, box_h = 22*mm, 8*mm
        box_x = (PAGE_W - 2*MARGIN - box_w) / 2
        box_y = PAGE_H - 2*MARGIN - 40*mm
        c.rect(box_x, box_y, box_w, box_h, fill=0, stroke=1)
        c.setStrokeColor(WHITE)
        c.rect(box_x, box_y, box_w, box_h, fill=0, stroke=1)
        c.setFont("Lexend-Light", 9)
        c.setFillColor(WHITE)
        c.drawCentredString(box_x + box_w/2, box_y + 2.5*mm, self.page_num)

        # Title
        c.setFont("Lexend-Bold", 28)
        c.setFillColor(WHITE)
        title_y = PAGE_H / 2
        c.drawCentredString((PAGE_W - 2*MARGIN)/2, title_y, self.title)

        # Horizontal lines around title
        line_y_top = title_y + 14*mm
        line_y_bot = title_y - 8*mm
        line_start = 20*mm
        line_end = PAGE_W - 4*MARGIN - 20*mm
        c.setStrokeColor(WHITE)
        c.setLineWidth(1.5)
        c.line(line_start, line_y_top, line_end, line_y_top)
        c.line(line_start, line_y_bot, line_end, line_y_bot)

        if self.subtitle:
            c.setFont("Lexend-Light", 10)
            c.drawCentredString((PAGE_W - 2*MARGIN)/2, title_y - 18*mm, self.subtitle)

        c.restoreState()


def make_style(name, **kwargs):
    defaults = {"fontName": "Lexend", "fontSize": 9.5, "leading": 14, "textColor": MID_GREY, "alignment": TA_LEFT, "spaceAfter": 6}
    defaults.update(kwargs)
    return ParagraphStyle(name, **defaults)

S_BODY = make_style("S_BODY", alignment=TA_JUSTIFY)
S_BODY_WHITE = make_style("S_BODY_WHITE", textColor=WHITE, alignment=TA_JUSTIFY)
S_H1 = make_style("S_H1", fontName="Lexend-Bold", fontSize=18, leading=22, textColor=BLACK, spaceAfter=10, spaceBefore=4)
S_H2 = make_style("S_H2", fontName="Lexend-SemiBold", fontSize=12, leading=16, textColor=BLACK, spaceBefore=14, spaceAfter=6)
S_H3 = make_style("S_H3", fontName="Lexend-SemiBold", fontSize=10.5, leading=14, textColor=DARK, spaceBefore=10, spaceAfter=4)
S_BULLET = make_style("S_BULLET", fontSize=9, leading=13, textColor=MID_GREY, leftIndent=14, bulletIndent=4, spaceAfter=3)
S_SMALL = make_style("S_SMALL", fontName="Lexend-Light", fontSize=7.5, leading=10, textColor=LIGHT_GREY, alignment=TA_CENTER)
S_PAGE_NUM = make_style("S_PAGE_NUM", fontName="Lexend-Light", fontSize=8, leading=10, textColor=LIGHT_GREY, alignment=TA_LEFT, spaceBefore=0, spaceAfter=4)
S_PRODUCT_NAME = make_style("S_PRODUCT_NAME", fontName="Lexend-Bold", fontSize=11, leading=14, textColor=BLACK, spaceAfter=2, spaceBefore=10)
S_PRODUCT_URL = make_style("S_PRODUCT_URL", fontName="Lexend-Light", fontSize=8, leading=10, textColor=MID_GREY, spaceAfter=4)
S_PRODUCT_DESC = make_style("S_PRODUCT_DESC", fontSize=9, leading=13, textColor=MID_GREY, spaceAfter=3)
S_PRODUCT_FEATURES = make_style("S_PRODUCT_FEATURES", fontName="Lexend-Light", fontSize=8.5, leading=12, textColor=MID_GREY, spaceAfter=8)
S_SERVICE_NUM = make_style("S_SERVICE_NUM", fontName="Lexend-Bold", fontSize=24, leading=28, textColor=HexColor("#bbbbbb"), spaceAfter=0)


def page_num_box(num):
    return Paragraph(f"<font color='#888888'>{num}</font>", S_PAGE_NUM)

def hr_black():
    return HRFlowable(width="100%", thickness=1, color=BLACK, spaceAfter=6, spaceBefore=6)

def hr_light():
    return HRFlowable(width="100%", thickness=0.5, color=HexColor("#dddddd"), spaceAfter=6, spaceBefore=6)

def add_footer(canvas_obj, doc):
    canvas_obj.saveState()
    # Footer text
    canvas_obj.setFont("Lexend-Light", 7)
    canvas_obj.setFillColor(LIGHT_GREY)
    canvas_obj.drawCentredString(PAGE_W / 2, 10 * mm, "Algolog Limited  |  algolog.co  |  Confidential")
    # Watermark logo at bottom center
    if os.path.exists(LOGO_PATH):
        logo_w = 30 * mm
        logo_h = 24 * mm
        x = (PAGE_W - logo_w) / 2
        y = 14 * mm
        canvas_obj.drawImage(LOGO_PATH, x, y, width=logo_w, height=logo_h, mask='auto', preserveAspectRatio=True)
    canvas_obj.restoreState()


def build_pdf():
    doc = SimpleDocTemplate(
        OUTPUT_PATH, pagesize=A4,
        leftMargin=MARGIN, rightMargin=MARGIN,
        topMargin=MARGIN, bottomMargin=MARGIN,
    )

    story = []
    avail_w = PAGE_W - 2 * MARGIN

    # =====================================================
    # PAGE 1: COVER (Black page)
    # =====================================================
    story.append(BlackPageBreak("01/10", "COMPANY", ""))
    story.append(PageBreak())

    # We need a white page after the black flowable — add cover subtitle content
    # Actually, let's build the cover differently

    # Remove the BlackPageBreak approach — use canvas drawing instead
    story.clear()

    # ----- PAGE 1: COVER -----
    if os.path.exists(BANNER_PATH):
        from PIL import Image as PILImage
        img = PILImage.open(BANNER_PATH)
        img_w, img_h = img.size
        aspect = img_h / img_w
        display_w = avail_w
        display_h = display_w * aspect
        banner = Image(BANNER_PATH, width=display_w, height=display_h)
        story.append(banner)
    story.append(Spacer(1, 20*mm))
    story.append(Paragraph("ALGOLOG LIMITED", make_style("cover_company", fontName="Lexend-Bold", fontSize=14, leading=18, textColor=LIGHT_GREY, alignment=TA_LEFT)))
    story.append(Spacer(1, 40*mm))
    story.append(Paragraph("COMPANY", make_style("cover_title", fontName="Lexend-Bold", fontSize=42, leading=48, textColor=BLACK, alignment=TA_LEFT)))
    story.append(Paragraph("PROFILE", make_style("cover_title2", fontName="Lexend-Light", fontSize=42, leading=48, textColor=LIGHT_GREY, alignment=TA_LEFT)))
    story.append(Spacer(1, 20*mm))
    story.append(hr_black())
    story.append(Paragraph("Software Engineering  \u00b7  AI &amp; Automation  \u00b7  Cloud &amp; Security  \u00b7  Enterprise Systems",
        make_style("cover_sub", fontName="Lexend-Light", fontSize=9, leading=12, textColor=LIGHT_GREY, alignment=TA_LEFT)))
    story.append(Spacer(1, 30*mm))
    story.append(Paragraph("www.algolog.co", make_style("cover_url", fontName="Lexend-Medium", fontSize=10, textColor=MID_GREY, alignment=TA_LEFT)))

    story.append(PageBreak())

    # ----- PAGE 2: ABOUT US -----
    story.append(page_num_box("02/10"))
    story.append(Spacer(1, 4*mm))
    story.append(Paragraph("ABOUT US", S_H1))
    story.append(hr_black())
    story.append(Spacer(1, 4*mm))

    story.append(Paragraph(
        "Algolog Limited is a Nigerian technology company headquartered in Abuja, Nigeria. Founded in 2022, "
        "we design, build, and deploy software systems that help businesses operate more efficiently, reduce "
        "costs, and scale with confidence.", S_BODY))
    story.append(Paragraph(
        "Our strength lies in execution. We combine deep technical expertise with a practical understanding of "
        "how Nigerian businesses actually operate \u2014 from hospitality operators managing bookings on WhatsApp, "
        "to oil and gas dealers tracking depositor balances in Excel, to churches collecting offerings in cash. "
        "We build systems that replace manual processes with reliable, automated solutions.", S_BODY))
    story.append(Paragraph(
        "We are led by a technical team with hands-on experience across cloud infrastructure, DevOps engineering, "
        "and enterprise software. Every project receives direct technical leadership from our core engineering team.", S_BODY))
    story.append(Paragraph(
        "Our team includes full-stack developers, backend engineers, DevOps specialists, QA engineers, AI/ML "
        "practitioners, and business analysts. We ship working software, not slide decks.", S_BODY))

    story.append(Spacer(1, 10*mm))

    # Key facts table
    facts = [
        [Paragraph("<b>Founded</b>", make_style("ft1", fontName="Lexend-Bold", fontSize=9, textColor=BLACK)),
         Paragraph("2022", make_style("ft2", fontSize=9, textColor=MID_GREY))],
        [Paragraph("<b>Headquarters</b>", make_style("ft3", fontName="Lexend-Bold", fontSize=9, textColor=BLACK)),
         Paragraph("Plot 1387 Aminu Kano Crescent, Wuse, Abuja", make_style("ft4", fontSize=9, textColor=MID_GREY))],
        [Paragraph("<b>Leadership</b>", make_style("ft5", fontName="Lexend-Bold", fontSize=9, textColor=BLACK)),
         Paragraph("Michael Akin-Ademola \u2014 CEO/CTO", make_style("ft6", fontSize=9, textColor=MID_GREY))],
        [Paragraph("<b>Website</b>", make_style("ft7", fontName="Lexend-Bold", fontSize=9, textColor=BLACK)),
         Paragraph("algolog.co", make_style("ft8", fontSize=9, textColor=MID_GREY))],
    ]
    ft = Table(facts, colWidths=[avail_w*0.25, avail_w*0.75])
    ft.setStyle(TableStyle([
        ("VALIGN", (0,0), (-1,-1), "TOP"),
        ("TOPPADDING", (0,0), (-1,-1), 4),
        ("BOTTOMPADDING", (0,0), (-1,-1), 4),
        ("LINEBELOW", (0,0), (-1,-1), 0.5, HexColor("#eeeeee")),
    ]))
    story.append(ft)

    story.append(PageBreak())

    # ----- PAGE 3: OUR SERVICES -----
    story.append(page_num_box("03/10"))
    story.append(Spacer(1, 4*mm))
    story.append(Paragraph("OUR SERVICES", S_H1))
    story.append(hr_black())

    services = [
        ("01", "Custom Software Development",
         "We build tailored software systems for businesses across industries \u2014 from depositor management "
         "platforms for oil and gas operators, to automated outreach systems for sales teams, to church giving "
         "platforms. Every system is designed around the client\u2019s actual workflow.",
         ["Full-stack web and mobile application development",
          "Enterprise resource planning (ERP) and workflow automation",
          "Payment processing and financial system integration (Paystack, Monnify)",
          "Real-time reporting and executive dashboard systems",
          "API design, development, and third-party integration"]),

        ("02", "AI &amp; Intelligent Automation",
         "We integrate artificial intelligence into business tools as a practical layer that makes systems smarter. "
         "Our AI work spans context engines, data analytics, automated outreach, and intelligent process automation.",
         ["AI-powered data analytics and business insights",
          "Natural language processing for document summarisation and search",
          "Automated outreach and lead qualification systems",
          "Multi-model AI integration (Claude, Gemini)",
          "No-code/low-code automation (Airtable, Make, Zapier)"]),

        ("03", "Cloud Architecture &amp; DevOps",
         "We design, provision, and manage cloud infrastructure that scales with your business. Our DevOps practice "
         "ensures deployments are fast, reliable, and repeatable.",
         ["Cloud provisioning (AWS, Azure, GCP)",
          "CI/CD pipelines and automated deployment",
          "Containerisation (Docker) and orchestration (Kubernetes)",
          "Infrastructure as Code (Terraform, Ansible)",
          "Monitoring, alerting, and uptime management"]),
    ]

    for num, title, desc, bullets in services:
        story.append(Spacer(1, 2*mm))
        story.append(Paragraph(num, S_SERVICE_NUM))
        story.append(Paragraph(title, S_H2))
        story.append(Paragraph(desc, S_BODY))
        for b in bullets:
            story.append(Paragraph(f"\u2022  {b}", S_BULLET))

    story.append(PageBreak())

    # ----- PAGE 4: SERVICES CONTINUED -----
    story.append(page_num_box("04/10"))
    story.append(Spacer(1, 4*mm))
    story.append(Paragraph("OUR SERVICES", S_H1))
    story.append(hr_black())

    services2 = [
        ("04", "Cybersecurity &amp; Data Protection",
         "We protect business systems and customer data from threats \u2014 both external and internal. "
         "Our security practice covers everything from architecture review to compliance alignment.",
         ["Security audits and vulnerability assessments",
          "Firewall configuration and intrusion detection/prevention",
          "Data encryption \u2014 at rest and in transit",
          "Secure API design and integration",
          "Regulatory compliance support (NDPR, ISO 27001 alignment)"]),

        ("05", "Code Audit, QA &amp; Testing",
         "For businesses with existing software, we provide independent code review, quality assurance, and testing. "
         "We identify gaps, write integration tests, flag vulnerabilities, and deliver a clear report.",
         ["Codebase audit and architecture review",
          "Integration testing and unit test coverage",
          "Performance testing and load analysis",
          "Security vulnerability scanning",
          "Post-audit discovery report with prioritised recommendations"]),
    ]

    for num, title, desc, bullets in services2:
        story.append(Spacer(1, 2*mm))
        story.append(Paragraph(num, S_SERVICE_NUM))
        story.append(Paragraph(title, S_H2))
        story.append(Paragraph(desc, S_BODY))
        for b in bullets:
            story.append(Paragraph(f"\u2022  {b}", S_BULLET))

    story.append(PageBreak())

    # ----- PRODUCTS WE HAVE BUILT -----
    story.append(page_num_box("05/10"))
    story.append(Spacer(1, 4*mm))
    story.append(Paragraph("PRODUCTS WE HAVE BUILT", S_H1))
    story.append(hr_black())
    story.append(Paragraph(
        "Algolog has designed, built, and deployed the following platforms:", S_BODY))
    story.append(Paragraph(
        "<i>* Products without URLs were custom-built and deployed directly for the client\u2019s business.</i>",
        make_style("products_note", fontName="Lexend-Light", fontSize=8, leading=11, textColor=LIGHT_GREY, spaceAfter=8)))

    all_products = [
        ("Spacer", "spacer.so",
         "Algolog\u2019s flagship product \u2014 a platform that enables organisations to manage and monetise "
         "physical spaces through automated booking, payment processing, and smart access control. Deployed across "
         "serviced apartments, hotels, co-working spaces, and resorts.",
         "Multi-tenant architecture \u2022 Auto-generated property websites \u2022 Multi-tier booking engine \u2022 "
         "Paystack payment integration \u2022 Smart lock automation (Tuya) \u2022 QR check-in \u2022 "
         "Cart abandonment notifications \u2022 Staff role management \u2022 Automated renewals"),

        ("DeepThread", "deepthread.ai",
         "An AI-powered tool that connects GitHub, Slack, Jira, Linear, Notion, and Google Docs \u2014 "
         "generating instant standups, handoff documents, and issue summaries. Turns scattered team activity "
         "into actionable context using multi-model AI analysis (Claude, GPT, Gemini, Cohere).",
         "Cross-platform context engine \u2022 Multi-model AI \u2022 Instant standups \u2022 "
         "Handoff document generation \u2022 Issue summaries \u2022 Predictive automation"),

        ("Visora", "visora-ai.com",
         "An AI-powered platform designed for seamless document querying, project collaboration, and knowledge "
         "management. Upload your business documents \u2014 contracts, reports, policies, financial records \u2014 "
         "and ask questions in plain language. Visora uses Retrieval-Augmented Generation (RAG) technology to find "
         "answers from your data, generate reports with visual insights, and enable team-based collaboration "
         "across projects. Supports both cloud and on-premises deployment for full data sovereignty.",
         "Natural language document queries \u2022 AI answers with source references \u2022 "
         "Project-based collaboration \u2022 Report generation \u2022 "
         "Multi-format upload (PDF, DOCX, CSV, XLSX) \u2022 Cloud &amp; on-premises deployment"),

        ("SkillPay", "skillpay.link",
         "Handles payment processing, user accounts, transaction tracking, and multi-brand support. Includes "
         "digital product sales, private gifting, payment links, and a funnel display mode for conversion-optimised "
         "sales pages.",
         "Digital product sales \u2022 Private gifting \u2022 Payment links \u2022 Fraud detection engine \u2022 "
         "Powers: BuyMeAShawarma (buymeshawarma.com) \u2022 BuyMeABeverage (buymeabeverage.com)"),

        ("PrivateTransfer", "privatetransfer.ng",
         "Secure transfer platform for safe, private financial transactions. Gift money to any Nigerian bank account "
         "\u2014 the recipient sees only the payment, not who sent it.",
         "Encrypted channels \u2022 Anonymous transfers \u2022 Bank account delivery"),

        ("AutoCare", "",
         "A platform helping automotive businesses automatically notify customers when vehicles are due for servicing. "
         "Multi-tenant architecture with personalised dashboards per business. Automated reminders via email and WhatsApp.",
         "Customer &amp; vehicle registry \u2022 Automated reminders (7-day, 3-day) \u2022 Service history \u2022 "
         "Multi-tenant dashboards \u2022 WhatsApp integration"),

        ("CYFT", "",
         "A digital platform for comprehensive facility health assessments of hospitals and clinics. 11 inspection "
         "categories, 316 checkpoints, colour-coded scoring, and professional inspection reports with repair cost estimates.",
         "480-point scoring system \u2022 11 inspection categories \u2022 Colour-coded reports \u2022 "
         "Repair cost estimates \u2022 Priority classification"),

        ("BDC System", "",
         "An MVP platform for Bureau De Change operators to manage FX rates, customer transactions, and back-office "
         "settlement workflows. Public rate display, receipt processing, and full audit trail.",
         "Live FX rates \u2022 Customer accounts \u2022 Receipt processing \u2022 Settlement workflows \u2022 Analytics"),
    ]

    for name, url, desc, features in all_products:
        story.append(Paragraph(name, S_PRODUCT_NAME))
        if url:
            story.append(Paragraph(url, S_PRODUCT_URL))
        story.append(Paragraph(desc, S_PRODUCT_DESC))
        story.append(Paragraph(features, S_PRODUCT_FEATURES))

    story.append(PageBreak())

    # ----- PAGE 7: SECTOR EXPERIENCE -----
    story.append(page_num_box("07/10"))
    story.append(Spacer(1, 4*mm))
    story.append(Paragraph("SECTOR EXPERIENCE", S_H1))
    story.append(hr_black())
    story.append(Spacer(1, 4*mm))

    sectors = [
        ("Hospitality &amp; Real Estate",
         "Property management, booking systems, guest communication, smart lock automation, auto-generated websites"),
        ("Oil &amp; Gas",
         "Depositor ledger management, digital voucher systems, AP remittance tracking, operational dashboards"),
        ("Financial Services",
         "Fintech applications, secure payment APIs, transaction processing, escrow and guarantee systems"),
        ("Healthcare",
         "Centralised health management systems, facility inspection, patient data security, compliance"),
        ("Religious Organisations",
         "Recurring giving platforms, member management, financial transparency"),
        ("Technology &amp; Startups",
         "Code audit, QA testing, AI integration, DevOps, team productivity tools"),
        ("FMCG &amp; Retail",
         "Supermarket revenue systems, checkout optimisation, customer retention platforms"),
    ]

    for title, desc in sectors:
        story.append(Paragraph(f"<b>{title}</b>", make_style(f"sec_{title[:4]}", fontName="Lexend-SemiBold", fontSize=10, leading=14, textColor=BLACK, spaceAfter=2, spaceBefore=8)))
        story.append(Paragraph(desc, S_BODY))
        story.append(hr_light())

    story.append(PageBreak())

    # ----- PAGE 8: OUR JOURNEY -----
    story.append(page_num_box("08/10"))
    story.append(Spacer(1, 4*mm))
    story.append(Paragraph("OUR JOURNEY", S_H1))
    story.append(hr_black())
    story.append(Spacer(1, 4*mm))

    story.append(Paragraph(
        "Founded in 2022 with a passion for solving complex problems using intelligent systems, Algolog Limited "
        "has evolved from a startup into a trusted partner for organisations across multiple industries.", S_BODY))
    story.append(Paragraph(
        "Our growth reflects a strong track record of innovation. From building Spacer \u2014 now managing bookings "
        "across properties in three Nigerian cities \u2014 to deploying DeepThread for developer teams, to creating "
        "Visora for enterprise analytics, every product we build is designed to solve a real "
        "problem we\u2019ve observed in the market.", S_BODY))
    story.append(Paragraph(
        "We operate from Abuja, but our work spans Lagos, Kaduna, and beyond. Our clients range from single-property "
        "hospitality operators to multi-station oil and gas dealers to nationwide church organisations.", S_BODY))
    story.append(Paragraph(
        "What sets us apart is not just what we build, but how we deliver. We move fast, we stay hands-on, and we "
        "don\u2019t stop until the system works as promised.", S_BODY))

    story.append(Spacer(1, 10*mm))

    # Why Algolog
    story.append(Paragraph("WHY ALGOLOG", S_H2))
    story.append(hr_light())

    why_items = [
        "We don\u2019t just consult and recommend \u2014 we build and ship. Every system we propose, we deliver.",
        "Deep technical team with international experience across cloud, security, and enterprise systems.",
        "Strong understanding of Nigerian regulatory, infrastructure, and business environments.",
        "Hands-on technical leadership on every engagement from our core engineering team.",
        "Commitment to security, compliance, and operational reliability.",
    ]
    for item in why_items:
        story.append(Paragraph(f"\u2022  {item}", S_BULLET))

    story.append(PageBreak())

    # ----- PAGE 9: IMPACT + CONTACT -----
    story.append(page_num_box("09/10"))
    story.append(Spacer(1, 4*mm))
    story.append(Paragraph("IMPACT", S_H1))
    story.append(hr_black())
    story.append(Spacer(1, 4*mm))

    story.append(Paragraph(
        "At Algolog Limited, our vision is to empower businesses by building technology that streamlines operations, "
        "reduces manual overhead, and ultimately increases profitability.", S_BODY))

    impacts = [
        "<b>Spacer</b> is actively managing bookings, payments, and access across properties in Abuja, Lagos, "
        "and Kaduna \u2014 replacing WhatsApp-based operations with a professional, automated platform.",
        "<b>DeepThread</b> is helping development teams cut standup and context-sharing time significantly \u2014 "
        "allowing engineers to focus on building, not searching for information.",
        "<b>AutoCare</b> is helping automotive businesses retain customers through automated service reminders "
        "\u2014 ensuring vehicles are maintained on schedule without manual follow-up.",
        "Our <b>custom enterprise builds</b> \u2014 from oil and gas depositor management systems to automated "
        "outreach platforms \u2014 are solving operational problems that businesses have struggled with for years.",
    ]
    for item in impacts:
        story.append(Paragraph(f"\u2022  {item}", S_BULLET))

    story.append(Spacer(1, 16*mm))

    # Contact section on same page
    story.append(Paragraph("CONTACT US", S_H1))
    story.append(hr_black())
    story.append(Spacer(1, 4*mm))

    story.append(Spacer(1, 4*mm))
    story.append(Paragraph("<b>Phone</b>          +234 808 396 5912", make_style("ci1", fontName="Lexend", fontSize=10, leading=16, textColor=MID_GREY, spaceAfter=10)))
    story.append(Paragraph("<b>Email</b>           info@algolog.co", make_style("ci2", fontName="Lexend", fontSize=10, leading=16, textColor=MID_GREY, spaceAfter=10)))
    story.append(Paragraph("<b>Website</b>       www.algolog.co", make_style("ci3", fontName="Lexend", fontSize=10, leading=16, textColor=MID_GREY, spaceAfter=10)))
    story.append(Paragraph("<b>Address</b>       Plot 1387 Aminu Kano Crescent, Wuse, Abuja", make_style("ci4", fontName="Lexend", fontSize=10, leading=16, textColor=MID_GREY, spaceAfter=10)))
    story.append(Spacer(1, 4*mm))
    story.append(Paragraph('<b>LinkedIn</b>      <a href="https://www.linkedin.com/company/algolog/" color="#0f3460">linkedin.com/company/algolog</a>', make_style("ci5", fontName="Lexend", fontSize=10, leading=16, textColor=MID_GREY, spaceAfter=10)))
    story.append(Paragraph('<b>Instagram</b>    <a href="https://www.instagram.com/algolog.co/" color="#0f3460">instagram.com/algolog.co</a>', make_style("ci6", fontName="Lexend", fontSize=10, leading=16, textColor=MID_GREY, spaceAfter=10)))
    story.append(Paragraph('<b>X (Twitter)</b>   <a href="https://x.com/algolog_co" color="#0f3460">x.com/algolog_co</a>', make_style("ci7", fontName="Lexend", fontSize=10, leading=16, textColor=MID_GREY, spaceAfter=10)))

    story.append(Spacer(1, 6*mm))
    story.append(Paragraph(
        "For enquiries, partnerships, or support, please reach out to us using the contact information provided \u2014 "
        "we\u2019re here to help.", S_BODY))

    story.append(PageBreak())

    # ----- PAGE 10: THANK YOU -----
    story.append(Spacer(1, 60*mm))
    story.append(Paragraph("ALGOLOG LIMITED", make_style("ty_co", fontName="Lexend-Light", fontSize=11, textColor=LIGHT_GREY, alignment=TA_CENTER)))
    story.append(Spacer(1, 30*mm))
    story.append(hr_black())
    story.append(Spacer(1, 6*mm))
    story.append(Paragraph("THANK YOU", make_style("ty_title", fontName="Lexend-Bold", fontSize=36, leading=42, textColor=BLACK, alignment=TA_CENTER)))
    story.append(Spacer(1, 6*mm))
    story.append(hr_black())
    story.append(Spacer(1, 10*mm))
    story.append(Paragraph(
        "Thank you for taking the time to learn about Algolog Limited \u2014 we look forward to the opportunity "
        "to work with you and deliver solutions that drive real results.",
        make_style("ty_sub", fontName="Lexend-Light", fontSize=10, leading=14, textColor=LIGHT_GREY, alignment=TA_CENTER)))
    story.append(Spacer(1, 16*mm))
    story.append(Paragraph("www.algolog.co", make_style("ty_url", fontName="Lexend-Medium", fontSize=11, textColor=MID_GREY, alignment=TA_CENTER)))

    doc.build(story, onFirstPage=add_footer, onLaterPages=add_footer)
    print(f"PDF generated: {OUTPUT_PATH}")
    print(f"File size: {os.path.getsize(OUTPUT_PATH):,} bytes")

if __name__ == "__main__":
    build_pdf()
