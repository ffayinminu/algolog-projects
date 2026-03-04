"""
Generate Visora Product Banner — Front + Back
40 x 87.3 inch roll-up banner
"""

import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from generate_banner_base import *

OUTPUT_PATH = os.path.join(PROPOSALS_DIR, "Banner-Visora.pdf")


def build_front(story):
    header_with_banner(story, "Visora",
                       "AI-Powered Data Analytics\nThat Drives Decisions",
                       "visora.ai")

    problem_block(story,
        "Most businesses have data scattered across disconnected systems. "
        "Decisions are made on gut feeling instead of evidence. Manual reporting "
        "takes days and still misses the insights that actually matter. "
        "Your data should be working for you, not sitting in silos.")

    value_prop_block(story, [
        ("Unified Data View",
         "Connect all your business data sources in one place \u2014 finance, CRM, operations, and more."),
        ("AI-Driven Insights",
         "Patterns and trends identified automatically. No data science degree required."),
        ("Custom Dashboards",
         "Tailored views for executives, managers, and teams. Everyone sees what matters to their role."),
        ("Actionable Recommendations",
         "AI highlights profit opportunities and inefficiencies so you know exactly where to act."),
    ])

    step_flow_block(story, [
        ("Connect Your Data", "Link your business data sources \u2014 finance systems, CRMs, operational tools."),
        ("AI Analyzes", "Visora\u2019s AI identifies patterns, anomalies, and forecasts trends from your data."),
        ("View Insights", "Access role-based custom dashboards with real-time KPIs and visualizations."),
        ("Act on Recommendations", "Implement AI-generated recommendations to capture opportunities and fix inefficiencies."),
    ])

    cta_block(story, "Book a Free Consultation", "visora.ai")


def build_back(story):
    header_with_banner(story, "Visora",
                       "Feature Breakdown & Details", "visora.ai")

    story.append(banner_spacer(0.3))

    feature_grid(story, [
        ("Unified Data Visualization",
         "Connect multiple data sources and see everything in one unified view. No more switching between systems."),
        ("AI Pattern Recognition",
         "Machine learning identifies trends, anomalies, and correlations humans would miss."),
        ("Custom Dashboards",
         "Role-based views for executives, managers, and teams. Each person sees what matters most."),
        ("Real-Time KPI Monitoring",
         "Track performance metrics across departments in real time. No waiting for weekly reports."),
        ("Decision Support Engine",
         "AI-generated recommendations highlight profit opportunities and operational inefficiencies."),
        ("Document Search & Q&A",
         "Upload documents and ask questions in natural language. AI finds answers instantly."),
        ("Collaboration Tools",
         "Share dashboards, annotate insights, and collaborate with team members directly in the platform."),
        ("Automated Reporting",
         "Schedule reports to generate and distribute automatically. No more manual spreadsheet exports."),
    ])

    who_its_for_block(story, [
        "Enterprise executives making strategic decisions",
        "Operations managers needing real-time visibility",
        "Government agencies tracking program performance",
        "Data teams looking to democratize insights across the organization",
        "Any business making decisions from data",
    ])

    trust_elements_block(story, [
        ("AI", "Powered\nAnalytics"),
        ("Real-Time", "Dashboard\nUpdates"),
        ("Multi-Source", "Data\nIntegration"),
    ])

    pricing_hint_block(story,
        "Custom packages based on data volume and user count.\nContact us for a tailored proposal.")

    about_algolog_block(story)
    contact_block(story)


if __name__ == "__main__":
    build_banner_pdf(OUTPUT_PATH, build_front, build_back)
