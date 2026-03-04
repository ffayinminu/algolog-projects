"""
Generate Algolog Master Banner — Company Overview (Front + Back)
40 x 87.3 inch roll-up banner showcasing all 10 products
"""

import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from generate_banner_base import *

OUTPUT_PATH = os.path.join(PROPOSALS_DIR, "Banner-Algolog-Master.pdf")


def build_front(story):
    """FRONT SIDE: Company overview with all 10 products."""

    # 1. Header
    header_with_banner(story, "ALGOLOG LIMITED",
                       "We Build Technology for African Businesses",
                       "algolog.co")

    story.append(banner_spacer(0.3))

    # 2. Product Showcase by Category

    # --- HOSPITALITY & OPERATIONS ---
    category_header_block(story, "HOSPITALITY & OPERATIONS")
    product_grid_row(story, [
        ("Spacer", "Smart hospitality and workspace management \u2014 bookings, payments, smart locks, dashboards", "spacer.so"),
        ("AutoCare", "Automated service reminders for auto-mechanic workshops \u2014 WhatsApp + email alerts", "\u2014"),
    ])
    story.append(banner_spacer(0.2))

    # --- AI & DATA ---
    category_header_block(story, "AI & DATA")
    product_grid_row(story, [
        ("DeepThread", "AI cross-platform context engine \u2014 instant standups and handoffs from GitHub, Slack, Jira", "deepthread.ai"),
        ("Visora", "AI-powered data analytics and insights \u2014 custom dashboards, pattern recognition, recommendations", "visora.ai"),
    ])
    story.append(banner_spacer(0.2))

    # --- FINANCE & PAYMENTS ---
    category_header_block(story, "FINANCE & PAYMENTS")
    product_grid_row(story, [
        ("PrivateTransfer", "Secure transfer platform for private financial transactions", "privatetransfer.ng"),
        ("SkillPay", "Shared payment infrastructure powering multiple consumer products", "skillpay.link"),
        ("BDC System", "FX rate display and remote settlement for Bureau De Change operators", "\u2014"),
        ("Pledged", "Church-branded recurring giving \u2014 set up by churchgoers themselves", "autogiving.ng"),
    ])
    story.append(banner_spacer(0.2))

    # --- CONSUMER ---
    category_header_block(story, "CONSUMER")
    product_grid_row(story, [
        ("BuyMeABeverage", "Beverage gifting and tipping platform for creators and professionals", "buymeabeverage.com"),
        ("BuyMeAShawarma", "Food gifting platform with a fun Nigerian twist", "buymeshawarma.com"),
    ])

    story.append(banner_spacer(0.5))

    # 3. Company Stats
    trust_elements_block(story, [
        ("19", "Products Across\n4 Divisions"),
        ("500+", "Bookings Managed\nMonthly"),
        ("4", "Live Deployments\nand Counting"),
        ("NGN 21M+", "In Active\nDeals"),
    ])

    # 4. CTA
    cta_block(story, "Let's Build Your Future Together", "algolog.co")


def build_back(story):
    """BACK SIDE: Product deep-dives, client references, team."""

    # Header
    header_with_banner(story, "ALGOLOG LIMITED",
                       "Our Product Portfolio", "algolog.co")

    story.append(banner_spacer(0.3))

    # 1. Product Deep-Dives
    story.append(Paragraph("OUR PRODUCTS", S_SECTION_CENTER))
    story.append(banner_spacer(0.15))

    mini_product_section(story, "Spacer",
        "Smart hospitality and workspace management platform. Automates bookings, payments, "
        "smart lock access codes, and real-time occupancy dashboards. Deployed at multiple "
        "properties managing 500+ bookings monthly.",
        "Eliminates revenue leaks and booking chaos with one centralized system",
        "spacer.so")

    mini_product_section(story, "Pledged",
        "Church-branded recurring giving platform where churchgoers set it up themselves. "
        "Funds settle directly to church bank accounts via Paystack subaccounts. "
        "Members can pause, adjust, or cancel anytime.",
        "Converts sporadic giving into predictable recurring church income",
        "autogiving.ng")

    mini_product_section(story, "DeepThread",
        "AI-powered cross-platform context engine. Generates instant standups and handoff "
        "documents from GitHub, Slack, Jira, and 7 other platforms. No more manual reporting.",
        "Standups in 10 seconds, not 10 minutes",
        "deepthread.ai")

    mini_product_section(story, "Visora",
        "AI-powered data analytics and insights platform. Connects business data sources, "
        "identifies patterns, and delivers actionable recommendations through custom dashboards.",
        "Makes businesses truly data-driven with AI doing the analysis",
        "visora.ai")

    mini_product_section(story, "PrivateTransfer",
        "Secure transfer platform for safe, private financial transactions. "
        "Security-first architecture for businesses and individuals.",
        "Encrypted, private transfers you can trust",
        "privatetransfer.ng")

    mini_product_section(story, "SkillPay",
        "Shared payment and commerce backend powering multiple consumer products. "
        "Handles payments, merchant accounts, custom links, and bank settlements.",
        "One backend powering 4 live product domains",
        "skillpay.link")

    mini_product_section(story, "AutoCare",
        "Automated service reminder system for auto-mechanic workshops. Tracks customers, "
        "vehicles, and service history. Sends automated WhatsApp and email reminders "
        "before service is due.",
        "Mechanics never lose repeat customers to forgotten follow-ups",
        "\u2014")

    mini_product_section(story, "BDC System",
        "FX rate and remote settlement platform for Bureau De Change operators. "
        "Public rate display, receipt upload, transaction pipeline, and owner analytics.",
        "Digitizes the manual BDC workflow with full transparency",
        "\u2014")

    mini_product_section(story, "BuyMeABeverage",
        "Beverage gifting platform. Get a custom link, share it, and receive "
        "beverage gifts from supporters. Payments processed via Paystack.",
        "The simplest way to accept tips and gifts in Nigeria",
        "buymeabeverage.com")

    mini_product_section(story, "BuyMeAShawarma",
        "Food gifting platform with a fun Nigerian twist. Same proven mechanics, "
        "powered by SkillPay.",
        "A culturally relevant way to support your favorite creators",
        "buymeshawarma.com")

    story.append(banner_spacer(0.3))

    # 2. Client References
    client_references_block(story, [
        ("Saadatu\u2019s Apartment, Kaduna", "Spacer HMIS + Smart Lock automation deployed and operational"),
        ("Kay-Wi Limited, Abuja", "Real estate facility management \u2014 NGN 16M agreement"),
        ("Alegre Farms, Bwari", "Resort booking platform proposal"),
        ("Yanna Apartments, Abuja", "Migration from Yanolja Cloud to Spacer"),
    ])

    # 3. Core Competencies
    competencies_block(story, [
        "Software Engineering",
        "DevOps Engineering",
        "AI/ML Development",
        "Business Development",
    ])

    # 4. Team
    team_block(story, [
        ("Michael Akin-Ademola", "CEO / CTO"),
        ("Femi Fayinminu", "Senior Business Developer"),
        ("Yasmin Umar", "Chief Brand Strategist"),
    ])

    # 5. Contact Block
    contact_block(story)


if __name__ == "__main__":
    build_banner_pdf(OUTPUT_PATH, build_front, build_back)
