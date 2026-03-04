"""
Generate SkillPay Product Banner — Front + Back
40 x 87.3 inch roll-up banner
"""

import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from generate_banner_base import *

OUTPUT_PATH = os.path.join(PROPOSALS_DIR, "Banner-SkillPay.pdf")


def build_front(story):
    header_with_banner(story, "SkillPay",
                       "Payment Infrastructure\nThat Powers Your Platform",
                       "skillpay.link")

    problem_block(story,
        "Building payment infrastructure from scratch for each new product is expensive, "
        "slow, and error-prone. Nigerian businesses need reliable payment processing "
        "that handles Paystack integration, merchant accounts, custom links, and bank "
        "settlements \u2014 without rebuilding it every time.")

    value_prop_block(story, [
        ("Multi-Brand Support",
         "One backend powers unlimited frontend products. Build once, deploy many."),
        ("Battle-Tested",
         "Already serving 4 live product domains with real users and real transactions."),
        ("Full Payment Stack",
         "Payments, merchant accounts, custom links, bank settlements, and recurring billing \u2014 all included."),
        ("Nigerian-First",
         "Built for Paystack, Nigerian banks, and local compliance. Not a foreign tool adapted for Nigeria."),
    ])

    step_flow_block(story, [
        ("Connect Your Frontend", "Link your product\u2019s frontend to SkillPay\u2019s API."),
        ("SkillPay Handles Payments", "Payment processing, user accounts, custom links \u2014 all managed by SkillPay."),
        ("Branded Experience", "Customers see your brand, not ours. SkillPay powers the backend invisibly."),
        ("Automatic Settlement", "Funds settle to merchant bank accounts automatically. No manual reconciliation."),
    ])

    # Trust stat highlight
    story.append(Paragraph("ALREADY POWERING", S_SECTION_CENTER))
    story.append(banner_spacer(0.15))
    trust_elements_block(story, [
        ("4", "Live Product\nDomains"),
        ("skillpay.link", "Primary\nPlatform"),
        ("Paystack", "Payment\nIntegration"),
    ])

    cta_block(story, "Book a Free Consultation", "skillpay.link")


def build_back(story):
    header_with_banner(story, "SkillPay",
                       "Feature Breakdown & Details", "skillpay.link")

    story.append(banner_spacer(0.3))

    feature_grid(story, [
        ("Multi-Brand/Tenant Architecture",
         "One backend serves multiple product frontends. Each brand gets its own experience."),
        ("Paystack Integration",
         "Full payment processing layer with card payments, bank transfers, and recurring billing."),
        ("User/Merchant Accounts",
         "Unified account system across all connected platforms. One signup, multiple products."),
        ("Custom Link Generation",
         "Shareable payment links for every merchant. Easy to create, easy to share."),
        ("Transaction Logging",
         "Complete transaction history and tracking across all connected products."),
        ("Bank Payout",
         "Direct settlement to merchant bank accounts. Automated, reliable, transparent."),
        ("Recurring Subscriptions",
         "Paystack charge_authorization for recurring payments. Powers Pledged\u2019s giving automation."),
        ("Paystack Subaccounts",
         "Direct settlement splits for marketplace models. Funds go straight to the right account."),
    ])

    who_its_for_block(story, [
        "SaaS startups needing payment infrastructure without building from scratch",
        "Platform builders looking for a multi-tenant payment backend",
        "Marketplace operators needing split settlements",
        "Businesses launching multiple consumer-facing products",
    ])

    trust_elements_block(story, [
        ("4", "Live Domains\nPowered"),
        ("Multi-Tenant", "Architecture\nBuilt-In"),
        ("Recurring", "Billing\nSupport"),
    ])

    pricing_hint_block(story,
        "Custom pricing based on transaction volume and product count.\nContact us for a tailored proposal.")

    about_algolog_block(story)
    contact_block(story)


if __name__ == "__main__":
    build_banner_pdf(OUTPUT_PATH, build_front, build_back)
