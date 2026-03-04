"""
Generate BDC System Product Banner — Front + Back
40 x 87.3 inch roll-up banner
"""

import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from generate_banner_base import *

OUTPUT_PATH = os.path.join(PROPOSALS_DIR, "Banner-BDC-System.pdf")


def build_front(story):
    header_with_banner(story, "BDC System",
                       "Digitize Your BDC Operations \u2014\nRates, Receipts, Settlements")

    problem_block(story,
        "Bureau De Change operators run their businesses through WhatsApp messages "
        "and phone calls. There\u2019s no structured workflow, no audit trail, and "
        "customers can\u2019t check rates without calling. This leads to settlement "
        "delays, errors, and a lack of operational visibility for owners.")

    value_prop_block(story, [
        ("Public Rate Display",
         "Customers check live USD/GBP rates online without calling. Saves time for both parties."),
        ("Digital Receipt Upload",
         "Customers submit transfer receipts directly through the platform. No more WhatsApp photo chaos."),
        ("Structured Workflow",
         "Every transaction follows a clear pipeline from receipt upload to final settlement."),
        ("Owner Analytics",
         "Full dashboard showing operations, volumes, staff performance, and transaction history."),
    ])

    step_flow_block(story, [
        ("Set Rates & Accounts", "BDC owner sets live FX rates and manages domiciliary account listings on the platform."),
        ("Customer Self-Service", "Customer views current rates online (no login needed), picks a dom account, uploads transfer receipt."),
        ("Staff Processes", "Back-office staff receives the receipt, processes through structured workflow pipeline, sends status updates."),
        ("Owner Monitors", "BDC owner monitors everything from an analytics dashboard \u2014 volumes, performance, settlements."),
    ])

    cta_block(story, "Book a Free Consultation")


def build_back(story):
    header_with_banner(story, "BDC System",
                       "Feature Breakdown & Details")

    story.append(banner_spacer(0.3))

    feature_grid(story, [
        ("Public FX Rate Display",
         "Customers view current USD and GBP rates without login. Always up to date, always accessible."),
        ("Receipt Upload System",
         "Customers upload transfer receipts (image or PDF) with amount, bank, and phone number."),
        ("Domiciliary Account Listing",
         "Shows BDC\u2019s dom accounts for customer reference \u2014 organized and easy to navigate."),
        ("Transaction Workflow Pipeline",
         "Structured pipeline from receipt upload through processing to settlement. Every step tracked."),
        ("Staff Assignment & Management",
         "Back-office staff assigned to transactions. Escalation paths and workload management built in."),
        ("Status Notifications",
         "Customers receive automatic updates on transaction progress. No more \u201Cwhat\u2019s the status?\u201D calls."),
        ("Analytics Dashboard",
         "Owner dashboard showing real-time operations, transaction volumes, and performance metrics."),
        ("Customer Self-Service",
         "Rate checking and receipt submission without needing to call or WhatsApp. Friction-free."),
    ])

    who_its_for_block(story, [
        "Bureau De Change operators looking to digitize operations",
        "BDC back-office staff needing structured transaction processing",
        "FX customers wanting self-service rate checking and submissions",
        "BDC owners seeking full operational visibility and analytics",
    ])

    trust_elements_block(story, [
        ("Full", "Transaction\nAudit Trail"),
        ("Real-Time", "Rate\nDisplay"),
        ("Structured", "Settlement\nWorkflow"),
    ])

    pricing_hint_block(story,
        "Custom pricing based on transaction volume.\nContact us for a tailored proposal.")

    about_algolog_block(story)
    contact_block(story)


if __name__ == "__main__":
    build_banner_pdf(OUTPUT_PATH, build_front, build_back)
