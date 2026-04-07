"""
Generate Court 474 Ltd — Facility Management System Implementation Document PDF
SDS custom build — separate from the Spacer deployment
"""

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib.colors import HexColor
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer as Sp, Image, Table, TableStyle,
    PageBreak, HRFlowable
)
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import os

BASE = "C:/Users/Femi Fayinminu/OneDrive/Documents/Algolog/Algolog_Projects"
FONT_DIR = os.path.join(BASE, "fonts/lexend-main/fonts/lexend/ttf")
BANNER_PATH = os.path.join(BASE, "claude.ai contex/Algolog_banner_cropped.png")
OUTPUT_PATH = os.path.join(BASE, "Proposals/Implementation-Court474-FacilityMgmt.pdf")

pdfmetrics.registerFont(TTFont("Lexend", os.path.join(FONT_DIR, "Lexend-Regular.ttf")))
pdfmetrics.registerFont(TTFont("Lexend-Bold", os.path.join(FONT_DIR, "Lexend-Bold.ttf")))
pdfmetrics.registerFont(TTFont("Lexend-SemiBold", os.path.join(FONT_DIR, "Lexend-SemiBold.ttf")))
pdfmetrics.registerFont(TTFont("Lexend-Light", os.path.join(FONT_DIR, "Lexend-Light.ttf")))
pdfmetrics.registerFont(TTFont("Lexend-Medium", os.path.join(FONT_DIR, "Lexend-Medium.ttf")))
pdfmetrics.registerFontFamily("Lexend", normal="Lexend", bold="Lexend-Bold", italic="Lexend", boldItalic="Lexend-Bold")

ACCENT_BLUE = HexColor("#0f3460")
DARK_TEXT = HexColor("#1a1a1a")
MEDIUM_TEXT = HexColor("#333333")
LIGHT_TEXT = HexColor("#555555")
TABLE_HEADER_BG = HexColor("#1a1a2e")
TABLE_ALT_ROW = HexColor("#f5f6fa")
BORDER_COLOR = HexColor("#dcdde1")
GREEN = HexColor("#27ae60")
WHITE = HexColor("#ffffff")

PAGE_W, PAGE_H = A4
LM = 22 * mm; RM = 22 * mm; TM = 20 * mm; BM = 20 * mm

def s(name, **kw):
    defaults = {"fontName": "Lexend", "fontSize": 10, "leading": 14, "textColor": DARK_TEXT, "alignment": TA_LEFT, "spaceAfter": 6}
    defaults.update(kw)
    return ParagraphStyle(name, **defaults)

H1 = s("H1", fontName="Lexend-Bold", fontSize=15, leading=20, textColor=ACCENT_BLUE, spaceBefore=18, spaceAfter=8)
H2 = s("H2", fontName="Lexend-SemiBold", fontSize=12, leading=16, textColor=DARK_TEXT, spaceBefore=12, spaceAfter=6)
H3 = s("H3", fontName="Lexend-SemiBold", fontSize=11, leading=14, textColor=MEDIUM_TEXT, spaceBefore=8, spaceAfter=4)
BODY = s("BODY", fontSize=9.5, leading=14, textColor=MEDIUM_TEXT, alignment=TA_JUSTIFY, spaceAfter=6)
BODY_B = s("BODY_B", fontName="Lexend-Bold", fontSize=9.5, leading=14, textColor=DARK_TEXT, spaceAfter=6)
BUL = s("BUL", fontSize=9.5, leading=14, textColor=MEDIUM_TEXT, leftIndent=18, bulletIndent=6, spaceAfter=4)
NUM = s("NUM", fontSize=9.5, leading=14, textColor=MEDIUM_TEXT, leftIndent=18, bulletIndent=6, spaceAfter=4)
SM = s("SM", fontSize=8, leading=11, textColor=LIGHT_TEXT, alignment=TA_CENTER)
HDR = s("HDR", fontName="Lexend-Light", fontSize=8.5, leading=12, textColor=LIGHT_TEXT, alignment=TA_CENTER)
TH = s("TH", fontName="Lexend-Bold", fontSize=9, leading=12, textColor=WHITE)
TC = s("TC", fontSize=9, leading=12, textColor=MEDIUM_TEXT)
TCB = s("TCB", fontName="Lexend-Bold", fontSize=9, leading=12, textColor=DARK_TEXT)
CALLOUT = s("CALLOUT", fontName="Lexend-SemiBold", fontSize=10, leading=14, textColor=GREEN, spaceAfter=8, spaceBefore=8)

def footer(c, doc):
    c.saveState()
    c.setFont("Lexend-Light", 7)
    c.setFillColor(LIGHT_TEXT)
    c.drawCentredString(PAGE_W / 2, 12 * mm, f"Algolog Limited  |  Confidential  |  Prepared for Court 474 Ltd  |  Page {doc.page}")
    c.restoreState()

def hr():
    return HRFlowable(width="100%", thickness=0.5, color=BORDER_COLOR, spaceAfter=8, spaceBefore=8)

def build():
    doc = SimpleDocTemplate(OUTPUT_PATH, pagesize=A4, leftMargin=LM, rightMargin=RM, topMargin=TM, bottomMargin=BM)
    story = []
    aw = PAGE_W - LM - RM

    # ========== COVER ==========
    if os.path.exists(BANNER_PATH):
        from PIL import Image as PILImage
        img = PILImage.open(BANNER_PATH)
        iw, ih = img.size
        dw = aw; dh = dw * (ih / iw)
        story.append(Image(BANNER_PATH, width=dw, height=dh))

    story.append(Sp(1, 18 * mm))
    story.append(hr())
    story.append(Sp(1, 8 * mm))

    story.append(Paragraph("Facility Management System",
        s("ct", fontName="Lexend-Bold", fontSize=24, leading=30, textColor=ACCENT_BLUE, alignment=TA_CENTER, spaceAfter=4)))
    story.append(Paragraph("Implementation Document",
        s("ct2", fontName="Lexend-SemiBold", fontSize=16, leading=22, textColor=DARK_TEXT, alignment=TA_CENTER, spaceAfter=4)))
    story.append(Paragraph("Cleaning, Procurement, Staff Management &amp; Cost Analytics",
        s("cs2a", fontName="Lexend-Medium", fontSize=11, leading=16, textColor=LIGHT_TEXT, alignment=TA_CENTER, spaceAfter=2)))
    story.append(Paragraph("Prepared for Court 474 Ltd",
        s("cs2", fontName="Lexend-Medium", fontSize=12, leading=16, textColor=LIGHT_TEXT, alignment=TA_CENTER, spaceAfter=6)))

    story.append(Sp(1, 12 * mm))
    story.append(hr())
    story.append(Sp(1, 6 * mm))

    info = [
        [Paragraph("<b>Prepared for:</b>", TCB), Paragraph("<b>Prepared by:</b>", TCB)],
        [Paragraph("Court 474 Ltd", TC), Paragraph("Algolog Limited", TC)],
        [Paragraph("", TC), Paragraph("Plot 1387 Aminu Kano Crescent,<br/>Wuse, Abuja", TC)],
        [Paragraph("", TC), Paragraph("ffayinminu@algolog.co<br/>+234 705 301 6348", TC)],
        [Paragraph("", TC), Paragraph("Fayinminu Femi<br/>Senior Business Developer", TC)],
    ]
    t = Table(info, colWidths=[aw * 0.5, aw * 0.5])
    t.setStyle(TableStyle([("VALIGN", (0,0), (-1,-1), "TOP"), ("TOPPADDING", (0,0), (-1,-1), 4),
        ("BOTTOMPADDING", (0,0), (-1,-1), 4), ("LEFTPADDING", (0,0), (-1,-1), 8),
        ("LINEBELOW", (0,0), (-1,0), 0.5, BORDER_COLOR)]))
    story.append(t)

    story.append(Sp(1, 12 * mm))
    story.append(Paragraph("April 2026", s("dt", fontName="Lexend-Medium", fontSize=11, textColor=LIGHT_TEXT, alignment=TA_CENTER)))
    story.append(PageBreak())

    # ========== 1. PROJECT OVERVIEW ==========
    story.append(Paragraph("1. PROJECT OVERVIEW", H1))
    story.append(hr())

    story.append(Paragraph(
        "Court 474 Ltd manages a short-let property with <b>29 apartments</b> (25 one-bedroom + 4 two-bedroom) "
        "and a <b>40-seater conference room</b>, all owned by multiple subscribers. Beyond the booking and "
        "guest management handled by Spacer, the day-to-day facility operations \u2014 cleaning, procurement, "
        "staff coordination, maintenance, and cost tracking \u2014 require their own dedicated system.", BODY))

    story.append(Paragraph(
        "This document outlines the <b>Facility Management System</b> we will build for Court 474 \u2014 a custom "
        "solution that integrates with Spacer to automate the operational side of managing 29 apartments "
        "and a conference room. It covers cleaning workflows, procurement, staff management, maintenance "
        "tracking, cost analytics, and service charge administration.", BODY))

    story.append(Sp(1, 4 * mm))
    story.append(Paragraph("What this system delivers:", H3))
    story.append(Paragraph("\u2022  Automated cleaning workflows triggered by guest checkout from Spacer", BUL))
    story.append(Paragraph("\u2022  Procurement tracking with auto-restock alerts for apartment consumables", BUL))
    story.append(Paragraph("\u2022  Staff scheduling and performance tracking tied to occupancy levels", BUL))
    story.append(Paragraph("\u2022  Maintenance request and resolution tracking per apartment", BUL))
    story.append(Paragraph("\u2022  Cost analytics \u2014 P&L per apartment, utility tracking, cost trends", BUL))
    story.append(Paragraph("\u2022  Service charge tracking \u2014 which owners have paid, who\u2019s overdue", BUL))
    story.append(Paragraph("\u2022  Facility management dashboard \u2014 bird\u2019s eye view of the entire operation", BUL))

    story.append(PageBreak())

    # ========== 2. THE PROBLEMS WE ARE SOLVING ==========
    story.append(Paragraph("2. THE PROBLEMS WE ARE SOLVING", H1))
    story.append(hr())

    story.append(Paragraph("A. Cleaning Coordination", H2))
    story.append(Paragraph(
        "With 29 apartments turning over guests on different schedules, cleaning coordination becomes a "
        "daily logistics challenge. Without a system, cleaning assignments happen via WhatsApp and phone "
        "calls. There\u2019s no visibility into which apartments need cleaning, which are ready, or how long "
        "cleaning takes. Apartments may sit unbooked simply because no one flagged them as ready.", BODY))

    story.append(Paragraph("B. Procurement Waste", H2))
    story.append(Paragraph(
        "Each apartment needs toiletries, linens, cleaning supplies, and other consumables. Without tracking, "
        "procurement is either reactive (run out and scramble) or wasteful (over-order and stockpile). There\u2019s "
        "no visibility into actual consumption per apartment or cost trends over time.", BODY))

    story.append(Paragraph("C. Staff Management", H2))
    story.append(Paragraph(
        "Cleaning staff, security, and maintenance personnel need to be scheduled based on actual occupancy, "
        "not guesswork. During low-occupancy periods, staff costs should scale down. During peak periods, "
        "additional support should be flagged in advance.", BODY))

    story.append(Paragraph("D. Maintenance Tracking", H2))
    story.append(Paragraph(
        "When something breaks in an apartment \u2014 a leaking tap, a faulty AC, a damaged fixture \u2014 it needs "
        "to be reported, tracked, assigned, and resolved. Without a system, maintenance requests get lost in "
        "WhatsApp threads and repairs are delayed.", BODY))

    story.append(Paragraph("E. Cost Visibility", H2))
    story.append(Paragraph(
        "Court 474 needs to know the actual cost of managing each apartment \u2014 cleaning costs, consumables, "
        "utilities, maintenance, and staff time. Without this, it\u2019s impossible to set accurate agency charges, "
        "identify unprofitable units, or make informed operational decisions.", BODY))

    story.append(Paragraph("F. Service Charge Administration", H2))
    story.append(Paragraph(
        "All apartment owners pay a fixed service charge for general facility management (security, water, "
        "common area cleaning). Tracking who has paid, who\u2019s overdue, and sending reminders needs to be "
        "automated \u2014 not managed in a spreadsheet.", BODY))

    story.append(PageBreak())

    # ========== 3. CLEANING AUTOMATION ==========
    story.append(Paragraph("3. CLEANING AUTOMATION", H1))
    story.append(hr())

    story.append(Paragraph(
        "The cleaning module integrates directly with Spacer. When a guest checks out, the facility "
        "management system automatically picks it up and triggers the cleaning workflow.", BODY))

    story.append(Sp(1, 2 * mm))
    story.append(Paragraph("How it works:", H3))
    story.append(Paragraph("1. <b>Guest checks out via Spacer</b> \u2014 the facility management system receives the event automatically", NUM))
    story.append(Paragraph("2. <b>Apartment flagged for cleaning</b> \u2014 status changes to \u201cNeeds Cleaning\u201d on the dashboard", NUM))
    story.append(Paragraph("3. <b>Cleaning staff assigned</b> \u2014 system assigns based on availability and current workload", NUM))
    story.append(Paragraph("4. <b>Staff notified</b> \u2014 cleaning staff receives a notification (SMS/app) with the apartment number", NUM))
    story.append(Paragraph("5. <b>Cleaning completed</b> \u2014 staff marks the apartment as \u201cReady\u201d in the system", NUM))
    story.append(Paragraph("6. <b>Spacer updated</b> \u2014 the apartment is automatically returned to the booking pool in Spacer", NUM))

    story.append(Sp(1, 3 * mm))
    story.append(Paragraph("What the system tracks:", H3))
    story.append(Paragraph("\u2022  Cleaning time per apartment (start to finish)", BUL))
    story.append(Paragraph("\u2022  Cleaning frequency per apartment per month", BUL))
    story.append(Paragraph("\u2022  Cost per cleaning (if cleaning staff are paid per job)", BUL))
    story.append(Paragraph("\u2022  Average turnaround time (checkout to ready)", BUL))
    story.append(Paragraph("\u2022  Staff workload distribution \u2014 who\u2019s handling the most/fewest apartments", BUL))

    story.append(Sp(1, 3 * mm))
    story.append(Paragraph(
        "The key benefit: no apartment sits idle because someone forgot to flag it as clean. The system "
        "ensures every checkout triggers a cleaning assignment, and every cleaned apartment returns to "
        "Spacer\u2019s booking pool automatically.", CALLOUT))

    story.append(PageBreak())

    # ========== 4. PROCUREMENT ==========
    story.append(Paragraph("4. PROCUREMENT &amp; INVENTORY MANAGEMENT", H1))
    story.append(hr())

    story.append(Paragraph(
        "Every apartment needs consumables \u2014 toiletries, linens, towels, cleaning products, light bulbs, "
        "and other supplies. The procurement module tracks what\u2019s being used and ensures restocking "
        "happens before anything runs out.", BODY))

    story.append(Sp(1, 2 * mm))
    story.append(Paragraph("Inventory Tracking", H2))
    story.append(Paragraph("\u2022  Each apartment has an inventory profile listing all consumables and their quantities", BUL))
    story.append(Paragraph("\u2022  After each cleaning, staff logs what was restocked (e.g., 2 soap bars, 1 set of towels)", BUL))
    story.append(Paragraph("\u2022  System deducts from central inventory and tracks usage per apartment", BUL))
    story.append(Paragraph("\u2022  Dashboard shows current stock levels for all items across the property", BUL))

    story.append(Sp(1, 3 * mm))
    story.append(Paragraph("Auto-Restock Alerts", H2))
    story.append(Paragraph("\u2022  Each item has a minimum threshold (e.g., when soap drops below 50 units, alert)", BUL))
    story.append(Paragraph("\u2022  System sends alerts to the procurement manager when thresholds are reached", BUL))
    story.append(Paragraph("\u2022  Alerts include the item, current quantity, and suggested reorder quantity based on usage history", BUL))

    story.append(Sp(1, 3 * mm))
    story.append(Paragraph("Procurement Reports", H2))
    story.append(Paragraph("\u2022  Monthly procurement cost per apartment", BUL))
    story.append(Paragraph("\u2022  Cost trends over time (is procurement spending going up or down?)", BUL))
    story.append(Paragraph("\u2022  Actual usage vs. purchase \u2014 identifies waste or theft", BUL))
    story.append(Paragraph("\u2022  Top items by cost and by frequency", BUL))

    story.append(PageBreak())

    # ========== 5. STAFF MANAGEMENT ==========
    story.append(Paragraph("5. STAFF SCHEDULING &amp; PERFORMANCE", H1))
    story.append(hr())

    story.append(Paragraph(
        "The system uses occupancy data from Spacer to help Court 474 manage staffing levels intelligently.", BODY))

    story.append(Sp(1, 2 * mm))
    story.append(Paragraph("Occupancy-Based Scheduling", H2))
    story.append(Paragraph("\u2022  System knows upcoming check-ins and check-outs from Spacer", BUL))
    story.append(Paragraph("\u2022  Suggests optimal cleaning staff schedule for the week based on expected turnovers", BUL))
    story.append(Paragraph("\u2022  Low occupancy week \u2192 reduce cleaning shifts, save on staff costs", BUL))
    story.append(Paragraph("\u2022  High occupancy weekend \u2192 alert for additional support in advance", BUL))

    story.append(Sp(1, 3 * mm))
    story.append(Paragraph("Performance Tracking", H2))
    story.append(Paragraph("\u2022  Cleaning time per staff member \u2014 who\u2019s fast, who\u2019s slow", BUL))
    story.append(Paragraph("\u2022  Number of apartments cleaned per day/week", BUL))
    story.append(Paragraph("\u2022  Guest ratings per apartment (if feedback is collected) \u2014 correlate with cleaning staff", BUL))
    story.append(Paragraph("\u2022  Attendance and shift tracking", BUL))

    story.append(Sp(1, 3 * mm))
    story.append(Paragraph("Staff Roles", H2))
    story.append(Paragraph("\u2022  <b>Cleaning staff</b> \u2014 receive cleaning assignments, mark apartments ready", BUL))
    story.append(Paragraph("\u2022  <b>Maintenance staff</b> \u2014 receive and resolve maintenance requests", BUL))
    story.append(Paragraph("\u2022  <b>Facility manager</b> \u2014 oversees all operations from the dashboard", BUL))
    story.append(Paragraph("\u2022  <b>Procurement manager</b> \u2014 manages inventory and restocking", BUL))

    story.append(PageBreak())

    # ========== 6. MAINTENANCE TRACKING ==========
    story.append(Paragraph("6. MAINTENANCE TRACKING", H1))
    story.append(hr())

    story.append(Paragraph(
        "When something needs fixing in an apartment or a common area, the maintenance module ensures "
        "it\u2019s logged, assigned, tracked, and resolved.", BODY))

    story.append(Sp(1, 2 * mm))
    story.append(Paragraph("How it works:", H3))
    story.append(Paragraph("1. <b>Issue reported</b> \u2014 by cleaning staff (during cleaning), facility manager, or apartment owner", NUM))
    story.append(Paragraph("2. <b>Categorised</b> \u2014 plumbing, electrical, AC, fixtures, structural, etc.", NUM))
    story.append(Paragraph("3. <b>Priority assigned</b> \u2014 urgent, normal, low", NUM))
    story.append(Paragraph("4. <b>Assigned to maintenance staff</b> \u2014 or flagged for external contractor", NUM))
    story.append(Paragraph("5. <b>Resolution logged</b> \u2014 what was done, cost, time taken", NUM))
    story.append(Paragraph("6. <b>Apartment status updated</b> \u2014 if the apartment was taken offline for repair, it\u2019s returned to ready", NUM))

    story.append(Sp(1, 3 * mm))
    story.append(Paragraph("Maintenance Reports:", H3))
    story.append(Paragraph("\u2022  Open issues by apartment and by category", BUL))
    story.append(Paragraph("\u2022  Resolution time (average and per issue)", BUL))
    story.append(Paragraph("\u2022  Maintenance cost per apartment per month", BUL))
    story.append(Paragraph("\u2022  Recurring issues \u2014 which apartments or categories have the most problems", BUL))

    story.append(PageBreak())

    # ========== 7. COST ANALYTICS ==========
    story.append(Paragraph("7. COST ANALYTICS &amp; P&amp;L PER APARTMENT", H1))
    story.append(hr())

    story.append(Paragraph(
        "The system pulls revenue data from Spacer and cost data from its own modules (cleaning, "
        "procurement, maintenance, utilities) to produce a complete financial picture per apartment.", BODY))

    story.append(Sp(1, 2 * mm))
    story.append(Paragraph("Per Apartment:", H3))
    story.append(Paragraph("\u2022  <b>Revenue</b> \u2014 total booking revenue (from Spacer)", BUL))
    story.append(Paragraph("\u2022  <b>Agency charge earned</b> \u2014 Court 474\u2019s share", BUL))
    story.append(Paragraph("\u2022  <b>Cleaning cost</b> \u2014 total cleaning spend for the apartment", BUL))
    story.append(Paragraph("\u2022  <b>Consumables cost</b> \u2014 toiletries, linens, supplies", BUL))
    story.append(Paragraph("\u2022  <b>Maintenance cost</b> \u2014 repairs and fixes", BUL))
    story.append(Paragraph("\u2022  <b>Utility cost</b> \u2014 electricity, water (if metered per apartment)", BUL))
    story.append(Paragraph("\u2022  <b>Net profit/loss</b> \u2014 revenue minus all costs", BUL))

    story.append(Sp(1, 3 * mm))
    story.append(Paragraph("For the Facility Overall:", H3))
    story.append(Paragraph("\u2022  Total revenue across all apartments + conference room", BUL))
    story.append(Paragraph("\u2022  Total agency charges earned", BUL))
    story.append(Paragraph("\u2022  Total operational costs (cleaning + procurement + maintenance + utilities + staff)", BUL))
    story.append(Paragraph("\u2022  Net facility P&L", BUL))
    story.append(Paragraph("\u2022  Monthly and quarterly trend reports", BUL))
    story.append(Paragraph("\u2022  Most profitable and least profitable apartments", BUL))

    story.append(Sp(1, 6 * mm))

    # ========== 8. SERVICE CHARGE ==========
    story.append(Paragraph("8. SERVICE CHARGE ADMINISTRATION", H1))
    story.append(hr())

    story.append(Paragraph(
        "All apartment owners pay a fixed service charge to Court 474 for general facility management "
        "(security, water supply, common area maintenance). The system tracks this:", BODY))

    story.append(Sp(1, 2 * mm))
    story.append(Paragraph("\u2022  <b>Charge schedule</b> \u2014 monthly or quarterly billing per apartment owner", BUL))
    story.append(Paragraph("\u2022  <b>Payment tracking</b> \u2014 who has paid, who\u2019s overdue, outstanding amounts", BUL))
    story.append(Paragraph("\u2022  <b>Automated reminders</b> \u2014 email/SMS reminders for upcoming and overdue payments", BUL))
    story.append(Paragraph("\u2022  <b>Payment history</b> \u2014 full record per owner", BUL))
    story.append(Paragraph("\u2022  <b>Reports</b> \u2014 total service charges collected vs. expected, delinquency rate", BUL))

    story.append(PageBreak())

    # ========== 9. FACILITY MANAGEMENT DASHBOARD ==========
    story.append(Paragraph("9. FACILITY MANAGEMENT DASHBOARD", H1))
    story.append(hr())

    story.append(Paragraph(
        "The central hub for Court 474\u2019s operations team \u2014 a single screen that shows the state of the "
        "entire property at a glance.", BODY))

    story.append(Sp(1, 2 * mm))
    story.append(Paragraph("\u2022  <b>Real-time apartment status map</b> \u2014 visual grid: occupied, available, needs cleaning, "
        "under maintenance, blocked by owner", BUL))
    story.append(Paragraph("\u2022  <b>Today\u2019s activity</b> \u2014 check-ins, check-outs, cleaning assignments, maintenance tasks", BUL))
    story.append(Paragraph("\u2022  <b>Financial overview</b> \u2014 total revenue, agency charges, operational costs, net position", BUL))
    story.append(Paragraph("\u2022  <b>Staff view</b> \u2014 who\u2019s on shift, current assignments, workload", BUL))
    story.append(Paragraph("\u2022  <b>Maintenance queue</b> \u2014 open issues by priority", BUL))
    story.append(Paragraph("\u2022  <b>Inventory alerts</b> \u2014 items below restock threshold", BUL))
    story.append(Paragraph("\u2022  <b>Service charge status</b> \u2014 paid, pending, overdue per owner", BUL))
    story.append(Paragraph("\u2022  <b>Security log</b> \u2014 integration with security systems if applicable", BUL))

    story.append(PageBreak())

    # ========== 10. TECHNICAL APPROACH ==========
    story.append(Paragraph("10. TECHNICAL APPROACH", H1))
    story.append(hr())

    tech = [
        [Paragraph("<b>Component</b>", TH), Paragraph("<b>Technology</b>", TH)],
        [Paragraph("Frontend", TC), Paragraph("Next.js + React", TC)],
        [Paragraph("Backend", TC), Paragraph("Node.js (NestJS)", TC)],
        [Paragraph("Database", TC), Paragraph("PostgreSQL", TC)],
        [Paragraph("Spacer Integration", TC), Paragraph("API integration for checkout events, occupancy data, and revenue data", TC)],
        [Paragraph("Cloud", TC), Paragraph("Microsoft Azure", TC)],
        [Paragraph("Infrastructure", TC), Paragraph("Terraform", TC)],
        [Paragraph("Notifications", TC), Paragraph("Email + SMS (cleaning assignments, restock alerts, service charge reminders)", TC)],
        [Paragraph("Security", TC), Paragraph("OWASP standard, role-based access control", TC)],
    ]
    tt = Table(tech, colWidths=[aw * 0.3, aw * 0.7])
    tt.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,0), TABLE_HEADER_BG),
        ("VALIGN", (0,0), (-1,-1), "TOP"),
        ("TOPPADDING", (0,0), (-1,-1), 6), ("BOTTOMPADDING", (0,0), (-1,-1), 6),
        ("LEFTPADDING", (0,0), (-1,-1), 8), ("RIGHTPADDING", (0,0), (-1,-1), 8),
        ("ROWBACKGROUNDS", (0,1), (-1,-1), [WHITE, TABLE_ALT_ROW]),
        ("LINEBELOW", (0,0), (-1,-2), 0.25, BORDER_COLOR),
        ("BOX", (0,0), (-1,-1), 0.5, BORDER_COLOR),
    ]))
    story.append(tt)

    story.append(Sp(1, 4 * mm))
    story.append(Paragraph(
        "The Facility Management System is built as a standalone application that communicates with "
        "Spacer via API. Checkout events, occupancy data, and revenue figures flow from Spacer into this "
        "system automatically \u2014 no manual data entry needed.", BODY))

    story.append(Sp(1, 8 * mm))

    # ========== 11. INVESTMENT ==========
    story.append(Paragraph("11. INVESTMENT", H1))
    story.append(hr())

    price = [
        [Paragraph("<b>Item</b>", TH), Paragraph("<b>Cost (NGN)</b>", TH)],
        [Paragraph("Cleaning Automation Module", TC), Paragraph("Included", TC)],
        [Paragraph("Procurement &amp; Inventory Management Module", TC), Paragraph("Included", TC)],
        [Paragraph("Staff Scheduling &amp; Performance Module", TC), Paragraph("Included", TC)],
        [Paragraph("Maintenance Tracking Module", TC), Paragraph("Included", TC)],
        [Paragraph("Cost Analytics &amp; P&amp;L Module", TC), Paragraph("Included", TC)],
        [Paragraph("Service Charge Administration", TC), Paragraph("Included", TC)],
        [Paragraph("Facility Management Dashboard", TC), Paragraph("Included", TC)],
        [Paragraph("Spacer API Integration", TC), Paragraph("Included", TC)],
        [Paragraph("Training &amp; Handover", TC), Paragraph("Included", TC)],
        [Paragraph("<b>Total Facility Management System</b>", TCB),
         Paragraph("<b>\u20a68,000,000</b>", TCB)],
    ]
    pt = Table(price, colWidths=[aw * 0.65, aw * 0.35])
    pt.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,0), TABLE_HEADER_BG),
        ("VALIGN", (0,0), (-1,-1), "TOP"),
        ("TOPPADDING", (0,0), (-1,-1), 6), ("BOTTOMPADDING", (0,0), (-1,-1), 6),
        ("LEFTPADDING", (0,0), (-1,-1), 8), ("RIGHTPADDING", (0,0), (-1,-1), 8),
        ("ROWBACKGROUNDS", (0,1), (-1,-2), [WHITE, TABLE_ALT_ROW]),
        ("LINEABOVE", (0,-1), (-1,-1), 1, ACCENT_BLUE),
        ("BOX", (0,0), (-1,-1), 0.5, BORDER_COLOR),
    ]))
    story.append(pt)

    story.append(Sp(1, 6 * mm))

    # Combined investment summary
    story.append(Paragraph("Combined Investment (Spacer + Facility Management)", H2))

    combined = [
        [Paragraph("<b>Component</b>", TH), Paragraph("<b>Cost (NGN)</b>", TH)],
        [Paragraph("Spacer Platform Setup &amp; Deployment", TC), Paragraph("\u20a610,000,000", TC)],
        [Paragraph("Smart Home Synchronisation", TC), Paragraph("\u20a62,000,000", TC)],
        [Paragraph("Facility Management System", TC), Paragraph("\u20a68,000,000", TC)],
        [Paragraph("<b>Total Investment</b>", TCB), Paragraph("<b>\u20a620,000,000</b>", TCB)],
    ]
    ct = Table(combined, colWidths=[aw * 0.65, aw * 0.35])
    ct.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,0), TABLE_HEADER_BG),
        ("VALIGN", (0,0), (-1,-1), "TOP"),
        ("TOPPADDING", (0,0), (-1,-1), 6), ("BOTTOMPADDING", (0,0), (-1,-1), 6),
        ("LEFTPADDING", (0,0), (-1,-1), 8), ("RIGHTPADDING", (0,0), (-1,-1), 8),
        ("ROWBACKGROUNDS", (0,1), (-1,-2), [WHITE, TABLE_ALT_ROW]),
        ("LINEABOVE", (0,-1), (-1,-1), 1.5, ACCENT_BLUE),
        ("BOX", (0,0), (-1,-1), 0.5, BORDER_COLOR),
    ]))
    story.append(ct)

    story.append(PageBreak())

    # ========== WHY ALGOLOG ==========
    story.append(Paragraph("WHY ALGOLOG", H1))
    story.append(hr())

    story.append(Paragraph(
        "Algolog Limited is a Nigerian technology company committed to ensuring businesses across Africa get "
        "the technology they need to build their future, improve their sales, and strengthen their operations.", BODY))

    story.append(Sp(1, 3 * mm))
    story.append(Paragraph("Our work includes:", H3))
    story.append(Paragraph("\u2022  <b>Spacer</b> (spacer.so) \u2014 Smart hospitality and workspace management platform, "
        "deployed across multiple properties in Abuja, Kaduna, and Lagos", BUL))
    story.append(Paragraph("\u2022  <b>DeepThread</b> (deepthread.ai) \u2014 AI-powered cross-platform context engine", BUL))
    story.append(Paragraph("\u2022  <b>Visora</b> (visora-ai.com) \u2014 AI-powered data analytics and insights platform", BUL))
    story.append(Paragraph("\u2022  <b>PrivateTransfer</b> (privatetransfer.ng) \u2014 Secure transfer platform", BUL))

    story.append(Sp(1, 8 * mm))

    # ========== NEXT STEP ==========
    story.append(Paragraph("NEXT STEP", H1))
    story.append(hr())

    story.append(Paragraph(
        "<b>We\u2019d love to discuss the facility management requirements in more detail</b> \u2014 the staffing "
        "structure, the service charge arrangements, procurement workflows, and how the system should "
        "integrate with Spacer for Court 474\u2019s specific operation.", BODY_B))

    story.append(Sp(1, 3 * mm))
    story.append(Paragraph("Whenever you\u2019re ready, reach out to:", H3))
    story.append(Paragraph("\u2022  <b>Call/WhatsApp:</b> Fayinminu Femi \u2014 +234 705 301 6348", BUL))
    story.append(Paragraph("\u2022  <b>Email:</b> ffayinminu@algolog.co", BUL))

    story.append(Sp(1, 10 * mm))
    story.append(hr())
    story.append(Paragraph("Algolog Limited", s("fc", fontName="Lexend-Bold", fontSize=10, textColor=DARK_TEXT, alignment=TA_CENTER)))
    story.append(Paragraph("Plot 1387 Aminu Kano Crescent, Wuse, Abuja  |  algolog.co", HDR))
    story.append(Sp(1, 3 * mm))
    story.append(Paragraph("Prepared with care for Court 474 Ltd \u2014 April 2026", SM))

    doc.build(story, onFirstPage=footer, onLaterPages=footer)
    print(f"PDF generated: {OUTPUT_PATH}")
    print(f"File size: {os.path.getsize(OUTPUT_PATH):,} bytes")


if __name__ == "__main__":
    build()
