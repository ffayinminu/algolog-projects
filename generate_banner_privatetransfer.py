"""
Generate PrivateTransfer Product Banner — Front + Back
40 x 87.3 inch roll-up banner
"""

import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from generate_banner_base import *

OUTPUT_PATH = os.path.join(PROPOSALS_DIR, "Banner-PrivateTransfer.pdf")


def build_front(story):
    header_with_banner(story, "PrivateTransfer",
                       "Secure Transfers You Can Trust",
                       "privatetransfer.ng")

    problem_block(story,
        "Businesses and individuals need to transfer sensitive files and financial data, "
        "but standard channels lack encryption and privacy guarantees. Data breaches "
        "and interception risks are growing across Africa. Your most important transfers "
        "deserve purpose-built security.")

    value_prop_block(story, [
        ("End-to-End Encryption",
         "Every transfer is protected from sender to receiver. No intermediary can access your data in transit."),
        ("Privacy by Design",
         "No data stored longer than necessary. Your transfers are yours \u2014 we don\u2019t keep copies."),
        ("Built for African Businesses",
         "Designed for local compliance requirements and infrastructure. Optimized for Nigerian networks."),
    ])

    step_flow_block(story, [
        ("Sign Up & Verify", "Create your account and complete identity verification for secure access."),
        ("Initiate Transfer", "Upload your file or initiate your financial transfer through the secure platform."),
        ("Secure Delivery", "Recipient receives a secure, encrypted access link with controlled permissions."),
        ("Complete & Clear", "Transfer completes with full encryption. Data cleared after delivery."),
    ])

    cta_block(story, "Book a Free Consultation", "privatetransfer.ng")


def build_back(story):
    header_with_banner(story, "PrivateTransfer",
                       "Feature Breakdown & Details", "privatetransfer.ng")

    story.append(banner_spacer(0.3))

    feature_grid(story, [
        ("End-to-End Encryption",
         "Military-grade encryption protects every transfer from initiation to delivery."),
        ("Secure File Sharing",
         "Share sensitive documents with confidence. Controlled access, no unauthorized viewing."),
        ("Private Financial Transactions",
         "Transfer funds with privacy guarantees that standard banking channels don\u2019t provide."),
        ("Identity Verification",
         "Know who you\u2019re transacting with. Built-in verification for both parties."),
        ("Full Audit Trail",
         "Complete record of every transfer for compliance and accountability."),
        ("Access Controls",
         "Set permissions, time limits, and access restrictions on every transfer."),
        ("Expiring Links",
         "Transfer links auto-expire after delivery or after a set time period. No lingering access."),
        ("Mobile-Responsive",
         "Works seamlessly on any device \u2014 desktop, tablet, or phone."),
    ])

    who_its_for_block(story, [
        "Businesses handling sensitive financial or legal data",
        "Financial institutions requiring secure inter-party transfers",
        "Legal firms sharing confidential client documents",
        "Healthcare organizations transferring patient information",
        "Government agencies needing secure communication channels",
    ])

    trust_elements_block(story, [
        ("E2E", "End-to-End\nEncryption"),
        ("Zero", "Data Retention\nAfter Delivery"),
        ("Built", "For African\nBusinesses"),
    ])

    about_algolog_block(story)
    contact_block(story)


if __name__ == "__main__":
    build_banner_pdf(OUTPUT_PATH, build_front, build_back)
