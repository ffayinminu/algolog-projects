"""
Generate WorkingForGod.org delivery documents as branded PDFs:
  1. WFG-Requirements-List.pdf      (rendered from WFG-Requirements-List.md)
  2. WFG-Scope-Lock.pdf             (rendered from WFG-Scope-Lock.md)
  3. Agreement-WorkingForGod-Updated.pdf  (hand-built; preserves the original signed file)
Matches Algolog standard: Algolog banner header, Lexend font, navy palette.
"""
import os, re
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib.colors import HexColor, white
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Image, Table, TableStyle,
    PageBreak, HRFlowable, KeepTogether,
)
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from PIL import Image as PILImage

BASE = "C:/Users/Femi Fayinminu/OneDrive/Documents/Algolog/Algolog_Projects"
FONT_DIR = os.path.join(BASE, "fonts/lexend-main/fonts/lexend/ttf")
BANNER = os.path.join(BASE, "claude.ai contex/Algolog_banner_cropped.png")
CTX = os.path.join(BASE, "claude.ai contex")
PROP = os.path.join(BASE, "Proposals")

pdfmetrics.registerFont(TTFont("Lexend", os.path.join(FONT_DIR, "Lexend-Regular.ttf")))
pdfmetrics.registerFont(TTFont("Lexend-Bold", os.path.join(FONT_DIR, "Lexend-Bold.ttf")))
pdfmetrics.registerFont(TTFont("Lexend-SemiBold", os.path.join(FONT_DIR, "Lexend-SemiBold.ttf")))
pdfmetrics.registerFont(TTFont("Lexend-Light", os.path.join(FONT_DIR, "Lexend-Light.ttf")))
pdfmetrics.registerFont(TTFont("Lexend-Medium", os.path.join(FONT_DIR, "Lexend-Medium.ttf")))
pdfmetrics.registerFontFamily("Lexend", normal="Lexend", bold="Lexend-Bold",
                              italic="Lexend", boldItalic="Lexend-Bold")

ACCENT = HexColor("#0f3460")
DARK = HexColor("#1a1a2e")
DARK_TEXT = HexColor("#1a1a1a")
MED = HexColor("#333333")
LIGHT = HexColor("#555555")
BORDER = HexColor("#dcdde1")
ALT = HexColor("#f5f6fa")

PAGE_W, PAGE_H = A4
LM = RM = 20 * mm
TM = BM = 18 * mm
AVAIL = PAGE_W - LM - RM


def st(name, **kw):
    d = dict(fontName="Lexend", fontSize=9.5, leading=13.5, textColor=MED,
             alignment=TA_LEFT, spaceAfter=4)
    d.update(kw)
    return ParagraphStyle(name, **d)

# keepWithNext on headings => a header is never stranded alone at the foot of a
# page; it moves to the next page only when its following content can't fit.
H1 = st("H1", fontName="Lexend-Bold", fontSize=14, leading=18, textColor=ACCENT, spaceBefore=10, spaceAfter=4, keepWithNext=1)
H2 = st("H2", fontName="Lexend-SemiBold", fontSize=11.5, leading=15, textColor=DARK_TEXT, spaceBefore=7, spaceAfter=3, keepWithNext=1)
H3 = st("H3", fontName="Lexend-SemiBold", fontSize=10.5, leading=13, textColor=MED, spaceBefore=5, spaceAfter=2, keepWithNext=1)
BODY = st("BODY", alignment=TA_JUSTIFY, spaceAfter=4)
BODYB = st("BODYB", fontName="Lexend-Bold", textColor=DARK_TEXT, spaceAfter=3)
BUL = st("BUL", leftIndent=15, bulletIndent=4, spaceAfter=2, alignment=TA_LEFT)
NOTE = st("NOTE", fontName="Lexend", fontSize=9, leading=12.5, textColor=LIGHT, leftIndent=8, rightIndent=8)
SMALL = st("SMALL", fontSize=8, leading=11, textColor=LIGHT, alignment=TA_CENTER)
CELL = st("CELL", fontSize=8.8, leading=12, spaceAfter=0)
CELLB = st("CELLB", fontName="Lexend-Bold", fontSize=8.8, leading=12, textColor=DARK_TEXT, spaceAfter=0)
CELLH = st("CELLH", fontName="Lexend-Bold", fontSize=9, leading=12, textColor=white, spaceAfter=0)


def inline(t):
    t = t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    t = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", t)
    t = re.sub(r"(?<!\*)\*(?!\*)(.+?)(?<!\*)\*(?!\*)", r"<i>\1</i>", t)
    return t


def hr():
    return HRFlowable(width="100%", thickness=0.5, color=BORDER, spaceAfter=5, spaceBefore=2)


def hf(label):
    def _f(c, doc):
        c.saveState()
        c.setFont("Lexend-Light", 7)
        c.setFillColor(LIGHT)
        c.drawCentredString(PAGE_W / 2, 11 * mm,
                            f"Algolog Limited  |  Confidential  |  {label}  |  Page {doc.page}")
        c.restoreState()
    return _f


def banner_flow():
    img = PILImage.open(BANNER)
    w, h = img.size
    return Image(BANNER, width=AVAIL, height=AVAIL * (h / w))


def cover(title, sub1, sub2):
    s = [banner_flow(), Spacer(1, 10 * mm), hr(), Spacer(1, 5 * mm)]
    s.append(Paragraph(title, st("ct", fontName="Lexend-Bold", fontSize=24, leading=30,
                                 textColor=ACCENT, alignment=TA_CENTER, spaceAfter=6)))
    s.append(Paragraph(sub1, st("cs1", fontName="Lexend-SemiBold", fontSize=16, leading=22,
                                textColor=DARK_TEXT, alignment=TA_CENTER, spaceAfter=4)))
    s.append(Paragraph(sub2, st("cs2", fontName="Lexend-Medium", fontSize=12, leading=17,
                                textColor=LIGHT, alignment=TA_CENTER, spaceAfter=6)))
    s += [Spacer(1, 8 * mm), hr(), Spacer(1, 5 * mm)]
    info = [
        [Paragraph("Prepared for:", CELLB), Paragraph("Prepared by:", CELLB)],
        [Paragraph("AiMP (Apostles In The Marketplace) Network", CELL), Paragraph("Algolog Limited", CELL)],
        [Paragraph("Primary contact: Nwamaka Okoye", CELL),
         Paragraph("Plot 1387 Aminu Kano Crescent,<br/>Wuse, Abuja", CELL)],
        [Paragraph("", CELL), Paragraph("ffayinminu@algolog.co<br/>+234 813 857 1129", CELL)],
        [Paragraph("", CELL), Paragraph("Fayinminu Femi<br/>Senior Business Developer", CELL)],
    ]
    t = Table(info, colWidths=[AVAIL * 0.5, AVAIL * 0.5])
    t.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("TOPPADDING", (0, 0), (-1, -1), 4), ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
        ("LEFTPADDING", (0, 0), (-1, -1), 8),
        ("LINEBELOW", (0, 0), (-1, 0), 0.5, BORDER),
    ]))
    s.append(t)
    s += [Spacer(1, 8 * mm),
          Paragraph("June 2026", st("dt", fontName="Lexend-Medium", fontSize=11,
                                    textColor=LIGHT, alignment=TA_CENTER)),
          PageBreak()]
    return s


def md_to_flowables(path, skip_first_h1=True):
    with open(path, encoding="utf-8") as f:
        lines = f.read().split("\n")
    flow, i, n, dropped = [], 0, len(lines), False
    while i < n:
        line = lines[i].rstrip()
        if not line.strip():
            i += 1; continue
        if re.match(r"^---+$", line.strip()):
            flow.append(hr()); i += 1; continue
        if line.startswith("### "):
            flow.append(Paragraph(inline(line[4:]), H3)); i += 1; continue
        if line.startswith("## "):
            flow.append(Paragraph(inline(line[3:]), H2)); i += 1; continue
        if line.startswith("# "):
            if skip_first_h1 and not dropped:
                dropped = True
                i += 1
                if i < n and lines[i].strip().startswith("**"):
                    i += 1
                continue
            flow.append(Paragraph(inline(line[2:]), H1)); i += 1; continue
        if line.lstrip().startswith(">"):
            buf = []
            while i < n and lines[i].lstrip().startswith(">"):
                buf.append(lines[i].lstrip()[1:].strip()); i += 1
            flow += [Spacer(1, 2), Paragraph(inline(" ".join(buf)), NOTE), Spacer(1, 2)]
            continue
        if line.lstrip().startswith("|"):
            rows = []
            while i < n and lines[i].lstrip().startswith("|"):
                rows.append([c.strip() for c in lines[i].strip().strip("|").split("|")]); i += 1
            rows = [r for r in rows if not all(re.match(r"^:?-{2,}:?$", c) for c in r if c != "")]
            ncols = len(rows[0])
            data = [[Paragraph(inline(c), CELLH) for c in rows[0]]]
            for r in rows[1:]:
                r = (r + [""] * ncols)[:ncols]
                data.append([Paragraph(inline(c), CELL) for c in r])
            t = Table(data, colWidths=[AVAIL / ncols] * ncols, repeatRows=1)
            t.setStyle(TableStyle([
                ("BACKGROUND", (0, 0), (-1, 0), DARK),
                ("ROWBACKGROUNDS", (0, 1), (-1, -1), [white, ALT]),
                ("GRID", (0, 0), (-1, -1), 0.4, BORDER),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 5), ("RIGHTPADDING", (0, 0), (-1, -1), 5),
                ("TOPPADDING", (0, 0), (-1, -1), 4), ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
            ]))
            flow += [Spacer(1, 2), t, Spacer(1, 4)]
            continue
        m = re.match(r"^\s*-\s+(.*)$", line)
        if m:
            flow.append(Paragraph(inline(m.group(1)), BUL, bulletText="•")); i += 1; continue
        m = re.match(r"^\s*(\d+)\.\s+(.*)$", line)
        if m:
            flow.append(Paragraph(f"{m.group(1)}.  " + inline(m.group(2)), BUL)); i += 1; continue
        flow.append(Paragraph(inline(line), BODY)); i += 1
    return flow


def build(path, label, story):
    doc = SimpleDocTemplate(path, pagesize=A4, leftMargin=LM, rightMargin=RM,
                            topMargin=TM, bottomMargin=BM, title=label, author="Algolog Limited")
    doc.build(story, onFirstPage=hf(label), onLaterPages=hf(label))
    print(f"  {os.path.basename(path)} -> {os.path.getsize(path):,} bytes")


# ---------- 1. Requirements List ----------
def requirements():
    s = cover("Project Requirements", "WorkingForGod.org",
              "What We Need From You to Begin")
    s += md_to_flowables(os.path.join(CTX, "WFG-Requirements-List.md"))
    build(os.path.join(PROP, "WFG-Requirements-List.pdf"),
          "WorkingForGod.org — Requirements", s)


# ---------- 2. Scope Lock ----------
def scope_lock():
    s = cover("Scope Lock", "ELI / WorkingForGod.org",
              "Complete Delivery Scope")
    s += md_to_flowables(os.path.join(CTX, "WFG-Scope-Lock.md"))
    build(os.path.join(PROP, "WFG-Scope-Lock.pdf"),
          "WorkingForGod.org — Scope Lock", s)


# ---------- shared agreement helpers ----------
def bullets(items):
    return [Paragraph("•  " + inline(x), BUL) for x in items]


def kv_table(rows, w=(0.6, 0.4), total_row=True):
    data = [[Paragraph(rows[0][0], CELLH), Paragraph(rows[0][1], CELLH)]]
    for r in rows[1:]:
        data.append([Paragraph(inline(r[0]), CELL), Paragraph(inline(r[1]), CELL)])
    t = Table(data, colWidths=[AVAIL * w[0], AVAIL * w[1]])
    style = [
        ("BACKGROUND", (0, 0), (-1, 0), DARK),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("TOPPADDING", (0, 0), (-1, -1), 5), ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
        ("LEFTPADDING", (0, 0), (-1, -1), 8), ("RIGHTPADDING", (0, 0), (-1, -1), 8),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [white, ALT]),
        ("LINEBELOW", (0, 0), (-1, -2), 0.25, BORDER),
        ("BOX", (0, 0), (-1, -1), 0.5, BORDER),
    ]
    if total_row:
        style.append(("LINEABOVE", (0, -1), (-1, -1), 1, ACCENT))
    t.setStyle(TableStyle(style))
    return t


# ---------- 3. Updated Agreement ----------
def agreement():
    s = cover("Project Agreement", "WorkingForGod.org",
              "Christian Professional Training Platform")

    s.append(Paragraph("1. PROJECT OVERVIEW", H1)); s.append(hr())
    s.append(Paragraph(inline(
        "This agreement outlines the scope of work, deliverables, technical specifications, payment terms, "
        "support commitments, and ownership for the design, development, and deployment of the "
        "**Ethical Leadership Institute (ELI)** platform (ethicalleadershipinstitute.org) and its associated "
        "Christian-facing brand, **WorkingForGod.org**, sharing one backend and database. It incorporates the "
        "full set of requirements set out in the ELI Scope Document and the BRD Additions sheet."), BODY))
    s.append(Paragraph(inline(
        "This version reflects the scope agreed at the SLC Inaugural Meeting of 13 April 2026 together with the "
        "requirements subsequently provided by the Client. **All specified requirements have been incorporated "
        "into the delivery scope below at the agreed fixed price.** This signed agreement constitutes the agreed "
        "and locked scope for the project."), BODY))
    s.append(Paragraph("Parties to this Agreement:", BODYB))
    s += bullets([
        "**The Client:** AiMP (Apostles In The Marketplace) Network, represented by Nwamaka Okoye",
        "**The Developer:** Algolog Limited, a technology company registered in Nigeria",
    ])

    s.append(Paragraph("2. SCOPE OF WORK & DELIVERABLES", H1)); s.append(hr())
    s.append(Paragraph("A. UI/UX Prototype", H2))
    s.append(Paragraph(
        "A high-fidelity interactive Figma prototype has been designed and delivered, covering all core screens "
        "and user flows. It has been reviewed and approved as the foundation for development.", BODY))
    s.append(Paragraph("B. Full Platform Development", H2))
    s.append(Paragraph("The following features and modules will be built as part of the platform:", BODY))
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
            "5–10 minute microlearning video modules with chapter/section navigation",
            "Two-tier content: neutral core ethics modules + optional Christian deep-dive via a “Learn More” prompt",
            "Progress bar tracking per course",
            "“Continue Watching” functionality for returning users",
            "Reflection and discussion questions after each video segment",
            "Downloadable resources per course (PDF guides, scripture references)",
            "Bookmarking and related courses feature",
            "Free-tier access for teaser content",
        ]),
        ("Live Sessions (Occasional)", [
            "Support for occasional live (real-time) sessions alongside the standard pre-recorded courses",
            "An integrated live-session tool that handles scheduling, participant access, and live delivery",
            "Enrolled learners and cohorts can join scheduled live sessions from within the platform",
        ]),
        ("Learning Programs & Assessments", [
            "Group individual courses into structured learning programs / journeys",
            "Pre-, during-, and post-module assessments",
            "Pass / benchmark logic to track understanding and learning milestones",
        ]),
        ("Cohorts & Group Learning", [
            "Both individual learner profiles and group (cohort) profiles",
            "Assign learners to cohorts that take courses or programs together",
            "Group progress tracking and reporting",
        ]),
        ("Article & Resource Library", [
            "Categorized articles by theme",
            "Search and filter functionality",
            "Grid/list view with thumbnails, titles, and summaries",
            "Multi-format resources — PDF, Excel, Word, video, and audio",
            "Embedded content support (YouTube sermons, teaching clips)",
        ]),
        ("Community Forum", [
            "“Post a Dilemma” feature — users anonymously submit real ethical or workplace issues",
            "Moderated forum with biblical feedback from trusted contributors",
            "AI-assisted first-line moderation with human review and approval",
            "Categorized discussions",
        ]),
        ("Speakers, Leaders & Events", [
            "Speaker & leader profiles highlighting marketplace credibility and faith journeys",
            "Upcoming conferences and speaker lineup",
            "Faith-based workplace event promotions and announcements",
        ]),
        ("Certificates & Credentials", [
            "Certificate of completion for each learning journey",
        ]),
        ("Subscription & Payment System", [
            "Individual plans: Monthly and Yearly subscription options",
            "Organization plans: Tiered pricing based on number of seats",
            "Payment gateway integration",
            "Admin dashboard for organizations to monitor staff participation",
        ]),
        ("User Profile & Dashboard", [
            "Track completed courses, progress, and completion rates",
            "Personalised recommendations (“others who learned this also learned…”)",
            "Save/bookmark articles and favourite lessons",
            "Subscription management",
            "Course history",
        ]),
        ("About Us & Mission Page", [
            "Vision and mission statement",
            "Core scriptures that guide the platform",
            "Platform goals, narrative, and connection to AiMP and WFG",
        ]),
        ("Content Management System & Analytics", [
            "Admin panel for easy upload of videos, articles, and resources",
            "User management and subscription monitoring",
            "Content tagging for dual-brand (ELI + WFG) distribution",
            "Analytics & benchmarking — engagement, completion, and cohort performance",
            "Forum moderation tools",
        ]),
        ("Scalable Data Architecture", [
            "Database structured to hold 500,000+ profiles",
            "Cleanly sectioned for reporting, analysis, and benchmarking",
            "Built to scale for rapid expansion",
        ]),
    ]
    for title, bl in modules:
        s.append(Paragraph(title, H3)); s += bullets(bl)

    s.append(Paragraph("C. Dual Front-End Architecture", H2))
    s.append(Paragraph(inline(
        "The platform ships with **two front-ends sharing one backend and database**: the **Ethical Leadership "
        "Institute (ELI)** corporate-facing brand and the **WorkingForGod.org** Christian-facing brand. Both are "
        "delivered within the agreed fixed price."), BODY))
    s += bullets(["Two branded front-ends, one shared content backend and database",
                  "Consistent content library serving both audiences"])
    s.append(Paragraph("D. Network Integration & Cross-Linking", H2))
    s += bullets(["“AiMP initiative / join the network” calls-to-action woven through the content",
                  "Cross-linking between ELI and WorkingForGod.org (funnel both directions)",
                  "SEO setup under the new domain"])

    s.append(Paragraph("3. TECHNICAL SPECIFICATIONS", H1)); s.append(hr())
    s.append(Paragraph("The platform will be built using the following technologies:", BODY))
    s.append(kv_table([
        ("Component", "Technology"),
        ("Server Runtime", "Node.js (JavaScript)"),
        ("Backend Framework", "NestJS"),
        ("Frontend Framework", "Next.js + React.js"),
        ("Cloud Hosting", "Microsoft Azure"),
        ("Infrastructure", "Terraform (Infrastructure as Code)"),
        ("Database", "PostgreSQL"),
        ("Security Standard", "OWASP Top 10 compliance"),
        ("Video Delivery", "HLS streaming + YouTube embeds"),
        ("Payment Integration", "Paystack (or equivalent)"),
    ], w=(0.38, 0.62), total_row=False))
    s.append(Paragraph("Key technical commitments:", H3))
    s += bullets([
        "Fully responsive design (desktop, tablet, and mobile)",
        "OWASP security standard compliance — the widely accepted standard for web application security",
        "Scalable cloud infrastructure on Azure",
        "Regular backups and security services",
        "CDN for optimized video streaming",
        "Rate limiting and DDoS protection",
    ])

    s.append(Paragraph("4. PROJECT INVESTMENT", H1)); s.append(hr())
    s.append(Paragraph(
        "The total project cost covers full platform development (both front-ends), deployment, quality testing, "
        "CMS setup, payment integration, and staff training.", BODY))
    s.append(kv_table([
        ("Milestone", "Amount (NGN)"),
        ("Upfront Payment (Commencement) — RECEIVED", "₦5,000,000"),
        ("Balance on Completion (Deployment & Handover)", "₦3,900,000"),
        ("**Total Project Cost**", "**₦8,900,000**"),
    ]))
    s.append(Paragraph(inline(
        "**Note:** The upfront payment of ₦5,000,000 has been received; this agreement is therefore effective and "
        "development commences upon the signing of this agreement. The total cost is for development and delivery only. "
        "**The Client is responsible for all ongoing hosting and data costs** — cloud servers, storage, bandwidth/"
        "data transfer, and video streaming (CDN) — billed directly by the cloud provider based on usage. These "
        "are not part of the ₦8,900,000."), BODY))

    s.append(Paragraph("5. PROJECT TIMELINE", H1)); s.append(hr())
    s.append(Paragraph(inline(
        "The full project will be delivered within **6 weeks** of commencement — four weeks of core development, "
        "then two weeks for testing/QA, deployment, staff training, and handover."), BODY))
    s.append(Paragraph(inline(
        "**Commencement is the point at which this agreement is signed** — development begins immediately on "
        "signing. Content (videos, articles, speaker bios, images) is provided by the Client during the build and "
        "is not required upfront to begin; significant delays in content delivery may affect the delivery date."), BODY))

    s.append(Paragraph("6. TRAINING & HANDOVER", H1)); s.append(hr())
    s.append(Paragraph("Upon completion of development and deployment, the following will be provided:", BODY))
    s += bullets([
        "**Staff Training:** all designated staff trained on the platform and CMS — content uploads, user management, and subscription monitoring",
        "**Comprehensive Manual:** a written user manual covering all platform features and administrative functions",
        "**Admin Access:** full administrative access to the platform, CMS, and hosting dashboard",
    ])

    s.append(Paragraph("7. SUPPORT & MAINTENANCE", H1)); s.append(hr())
    s.append(Paragraph("Algolog Limited is committed to providing ongoing support under the following terms:", BODY))
    s.append(Paragraph("What is included:", H3))
    s += bullets([
        "Free life-long technical support for any issues, bugs, or questions related to the features and functionality delivered under this agreement",
        "Bug fixes and troubleshooting within the originally agreed scope",
        "Guidance on platform usage, content management, and administrative functions",
        "Security patches and critical updates to maintain platform stability",
    ])
    s.append(Paragraph("What requires separate discussion:", H3))
    s += bullets([
        "New features, modules, or functionality not included in the original scope",
        "Significant redesigns or UI overhauls beyond the approved prototype",
        "Integration with third-party systems not specified in this agreement",
        "Native mobile app development (Android/iOS)",
    ])
    s.append(Paragraph(
        "Any request that falls outside the originally agreed and delivered scope will require a separate "
        "discussion to determine scope, timeline, and cost.", BODY))

    s.append(Paragraph("8. OWNERSHIP & INTELLECTUAL PROPERTY", H1)); s.append(hr())
    s.append(Paragraph(inline(
        "Upon full payment of the total project cost (**₦8,900,000**), the following ownership rights transfer to "
        "the Client:"), BODY))
    s += bullets([
        "Full ownership of the platform, including all source code, design assets, and documentation",
        "The platform is the Client’s property — the Client is free to manage, modify, or extend it independently",
        "No recurring licensing fees or ownership restrictions from Algolog Limited",
        "All login credentials, API keys, hosting access, and administrative controls handed over to the Client",
    ])
    s.append(Paragraph(
        "Algolog Limited retains the right to reference WorkingForGod.org in its portfolio as a completed project, "
        "unless otherwise requested by the Client.", BODY))

    s.append(Paragraph("9. HOSTING, INFRASTRUCTURE & DATA COSTS", H1)); s.append(hr())
    s.append(Paragraph(inline(
        "The platform will be hosted on **Microsoft Azure** (or equivalent cloud provider). **All hosting and data "
        "costs are the responsibility of the Client** and are separate from the ₦8,900,000 development fee — they "
        "are billed directly by the cloud provider based on usage."), BODY))
    s += bullets([
        "Algolog will set up and configure the cloud infrastructure as part of the project",
        "Client-borne costs include: secure servers/compute, scalable storage, **data transfer / bandwidth**, "
        "**video streaming (CDN) data**, backups, and security services",
        "These costs scale with the user base, content volume, and video/data usage",
        "The Client owns and is billed on the cloud account, with full access to the hosting dashboard and billing",
        "Algolog can advise on cost optimisation, but does not bear or mark up hosting or data charges",
    ])

    s.append(Paragraph("10. TERMS & CONDITIONS", H1)); s.append(hr())
    terms = [
        "This agreement is effective from receipt of the upfront payment (₦5,000,000), which has been received.",
        "Commencement is the signing of this agreement, and the project timeline begins from that point. This signed "
        "agreement constitutes the locked scope for the project.",
        "Content (videos, articles, images, speaker information) is provided by the Client during the build and is "
        "not required upfront to begin. Significant delays in content delivery may affect the delivery date.",
        "All requirements specified by the Client are included in the delivery scope at the agreed fixed price of "
        "₦8,900,000. Any new requirement raised after commencement (beyond the agreed scope) will be documented as "
        "a written addendum with adjusted cost and timeline, consistent with this agreement.",
        "Hosting and data costs (servers, storage, bandwidth/data transfer, and video streaming/CDN) are the "
        "Client's responsibility and are billed directly by the cloud provider, separate from the fixed price.",
        "Either party may terminate this agreement with 14 days’ written notice. On termination, the Client is "
        "billed for work completed up to that date.",
    ]
    for i, t in enumerate(terms, 1):
        s.append(Paragraph(f"{i}.  " + inline(t), BUL))

    s.append(Paragraph("11. ACCEPTANCE", H1)); s.append(hr())
    s.append(Paragraph(
        "By signing below, both parties acknowledge and agree to the terms, scope, deliverables, payment schedule, "
        "and conditions outlined in this agreement.", BODY))
    sig = [
        [Paragraph("For the Client:", CELLB), Paragraph("For Algolog Limited:", CELLB)],
        [Paragraph("", CELL), Paragraph("", CELL)],
        [Paragraph("____________________________", CELL), Paragraph("____________________________", CELL)],
        [Paragraph("Nwamaka Okoye", CELLB), Paragraph("Fayinminu Femi", CELLB)],
        [Paragraph("AiMP (Apostles In The Marketplace) Network", CELL),
         Paragraph("Senior Business Developer, Algolog Limited", CELL)],
        [Paragraph("", CELL), Paragraph("", CELL)],
        [Paragraph("Date: ____________________", CELL), Paragraph("Date: ____________________", CELL)],
    ]
    st_tbl = Table(sig, colWidths=[AVAIL * 0.5, AVAIL * 0.5])
    st_tbl.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "TOP"),
                                ("TOPPADDING", (0, 0), (-1, -1), 4), ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
                                ("LEFTPADDING", (0, 0), (-1, -1), 8)]))
    s.append(KeepTogether([
        Spacer(1, 8 * mm), st_tbl, Spacer(1, 10 * mm), hr(), Spacer(1, 2 * mm),
        Paragraph("We look forward to partnering with you to bring WorkingForGod.org to life.",
                  st("cl", fontName="Lexend-Medium", fontSize=9.5, leading=14, textColor=MED, alignment=TA_CENTER)),
        Spacer(1, 6 * mm), hr(),
        Paragraph("Algolog Limited", st("fc", fontName="Lexend-Bold", fontSize=10, textColor=DARK_TEXT, alignment=TA_CENTER)),
        Paragraph("Plot 1387 Aminu Kano Crescent, Wuse, Abuja  |  algolog.co", SMALL),
    ]))
    build(os.path.join(PROP, "Agreement-WorkingForGod-Updated.pdf"),
          "Project Agreement — WorkingForGod.org", s)


if __name__ == "__main__":
    print("Generating WFG delivery documents:")
    requirements()
    agreement()
    print("Done.")
