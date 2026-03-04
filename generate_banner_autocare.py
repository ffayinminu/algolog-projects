"""
Generate AutoCare Product Banner — Front + Back
40 x 87.3 inch roll-up banner
"""

import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from generate_banner_base import *

OUTPUT_PATH = os.path.join(PROPOSALS_DIR, "Banner-AutoCare.pdf")


def build_front(story):
    header_with_banner(story, "AutoCare",
                       "Never Lose a Customer\nto a Forgotten Service Date")

    problem_block(story,
        "Auto-mechanic workshops lose repeat customers because they have no system for follow-up. "
        "Customers forget when their next service is due, and mechanics have no organized way "
        "to track vehicles, service history, or send reminders. The result: lost revenue from "
        "customers who simply forgot to come back.")

    value_prop_block(story, [
        ("Automatic Reminders",
         "WhatsApp and email alerts sent automatically at 7 days and 3 days before service is due. No manual effort."),
        ("Customer Retention",
         "Customers come back on time, every time. Proactive reminders build loyalty and trust."),
        ("Zero App Download",
         "Runs on a clean Airtable interface \u2014 no installation, no training headaches, works on any device."),
        ("Complete Service History",
         "Every vehicle, every service, every date tracked. Full visibility into your customer base."),
    ])

    step_flow_block(story, [
        ("Get Your Dashboard", "Workshop receives a personalized AutoCare dashboard \u2014 clean, simple, ready to use."),
        ("Register Customers", "Add customers and their vehicles with service details and mileage."),
        ("Automatic Scheduling", "System calculates next service dates automatically based on service intervals."),
        ("Reminders Sent", "Automated WhatsApp and email reminders go out at 7 days and 3 days before service is due."),
    ])

    cta_block(story, "Book a Free Consultation")


def build_back(story):
    header_with_banner(story, "AutoCare",
                       "Feature Breakdown & Details")

    story.append(banner_spacer(0.3))

    feature_grid(story, [
        ("Customer Management",
         "Register and manage all customers per business. Contact details, preferences, and history in one place."),
        ("Vehicle Registry",
         "Track every vehicle \u2014 make, model, year, plate number, mileage, and full service history."),
        ("Automated Reminders",
         "WhatsApp + email reminders at 7 days and 3 days before service is due. Powered by Zapier + SyncMate."),
        ("Manual Messaging",
         "Send custom messages to individual customers or groups for promotions, seasonal offers, or updates."),
        ("Activity Logging",
         "Every automated action logged for transparency \u2014 see exactly when reminders were sent and to whom."),
        ("Multi-Tenant Architecture",
         "Each workshop sees only their own data. Fully isolated, secure, and private."),
        ("Personalized Dashboards",
         "Clean, intuitive interface customized for each business. No clutter, no confusion."),
        ("Auto Date Calculation",
         "System automatically calculates next service dates based on service type and interval."),
    ])

    who_its_for_block(story, [
        "Auto-mechanic workshops looking to retain more customers",
        "Car service centers wanting automated customer follow-up",
        "Fleet management companies tracking vehicle maintenance",
        "Dealership service departments needing organized scheduling",
    ])

    trust_elements_block(story, [
        ("2", "Reminder Types\n(7-day + 3-day)"),
        ("WhatsApp", "Native Integration\nvia SyncMate"),
        ("Zero", "App Downloads\nRequired"),
    ])

    pricing_hint_block(story,
        "Affordable monthly subscription.\nContact us for a personalized quote.")

    about_algolog_block(story)
    contact_block(story)


if __name__ == "__main__":
    build_banner_pdf(OUTPUT_PATH, build_front, build_back)
