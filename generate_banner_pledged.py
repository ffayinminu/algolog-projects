"""
Generate Pledged (AutoGiving) Product Banner — Front + Back
40 x 87.3 inch roll-up banner
"""

import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from generate_banner_base import *

OUTPUT_PATH = os.path.join(PROPOSALS_DIR, "Banner-Pledged.pdf")


def build_front(story):
    # 1. Header
    header_with_banner(story, "Pledged",
                       "Church-Branded Recurring Giving,\nSet Up by Churchgoers Themselves",
                       "autogiving.ng")

    # 2. The Problem
    problem_block(story,
        "Churches lose significant giving income when members travel, relocate, "
        "or simply forget. Manual cash collection lacks transparency and creates "
        "reconciliation headaches. Sporadic giving makes it nearly impossible "
        "to plan budgets with confidence.")

    # 3. Key Value Props
    value_prop_block(story, [
        ("Giver-Initiated Adoption",
         "Members start using Pledged independently \u2014 no church-wide rollout or committee approval needed."),
        ("Direct Settlement",
         "Funds go straight to the church\u2019s bank account via Paystack subaccounts. Money never touches Algolog."),
        ("Zero Lock-In",
         "Members can pause, adjust, or cancel their giving anytime. Complete control stays with the giver."),
        ("Predictable Income",
         "Converts sporadic, cash-based giving into reliable recurring revenue the church can plan around."),
        ("Full Transparency",
         "Every transaction is tracked, auditable, and accompanied by digital receipts \u2014 no more cash counting."),
    ])

    # 4. How It Works
    step_flow_block(story, [
        ("Church Signs Up", "Church admin creates an account and adds bank details for direct settlement via Paystack subaccounts."),
        ("Customize Your Page", "Upload church logo, set brand colors, and create giving categories (Tithes, Offerings, Building Fund, etc.)."),
        ("Members Give", "Members visit autogiving.ng/[church-name], select a category, choose one-time or recurring, and pay securely."),
        ("Automatic Processing", "System charges on schedule, sends receipts, and settles funds directly to the church \u2014 all automated."),
    ])

    # 5. CTA
    cta_block(story, "Book a Free Consultation", "autogiving.ng")


def build_back(story):
    # Header
    header_with_banner(story, "Pledged",
                       "Feature Breakdown & Details", "autogiving.ng")

    story.append(banner_spacer(0.3))

    # 1. Feature Breakdown
    feature_grid(story, [
        ("Church-Branded Giving Links",
         "Each church gets autogiving.ng/[church-slug] with custom logo, brand colors, and giving categories."),
        ("Recurring Giving Automation",
         "Members set amount + frequency (weekly/monthly). Card tokenized, charges run automatically."),
        ("One-Time Giving",
         "No account required. Name, email, amount, pay \u2014 perfect for first-time givers and visitors."),
        ("Direct Paystack Settlement",
         "Funds settle directly to church bank via Paystack subaccounts. Zero intermediary handling."),
        ("Member Self-Service Dashboard",
         "View giving history, pause/adjust/cancel subscriptions anytime. Complete member control."),
        ("Church Admin Dashboard",
         "Real-time transaction totals, member lists, CSV export, and category management."),
        ("Multi-Church Accounts",
         "A single member account can give to multiple churches \u2014 perfect for members attending multiple services."),
        ("Automated Receipts",
         "Email + SMS receipts on payment, failed payment alerts, and weekly summaries to church admin."),
    ])

    # 2. Who It's For
    who_its_for_block(story, [
        "Church administrators looking to modernize giving operations",
        "Church finance teams needing transparent, auditable records",
        "Individual churchgoers who want to give consistently, even when absent",
        "Church leadership seeking predictable income for better budget planning",
    ])

    # 3. Trust Elements
    trust_elements_block(story, [
        ("181+", "Churches in\nCampaign Pipeline"),
        ("84", "Nationwide\nTargets"),
        ("Direct", "Settlement to\nChurch Bank"),
    ])

    # 4. Pricing
    pricing_hint_block(story,
        "Small percentage on transactions \u2014 church keeps the vast majority.\n"
        "No setup fees. No monthly fees. You only pay when giving happens.")

    # 5. About Algolog
    about_algolog_block(story)

    # 6. Contact Block
    contact_block(story)


if __name__ == "__main__":
    build_banner_pdf(OUTPUT_PATH, build_front, build_back)
