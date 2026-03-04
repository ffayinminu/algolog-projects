"""
Generate DeepThread Product Banner — Front + Back
40 x 87.3 inch roll-up banner
"""

import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from generate_banner_base import *

OUTPUT_PATH = os.path.join(PROPOSALS_DIR, "Banner-DeepThread.pdf")


def build_front(story):
    header_with_banner(story, "DeepThread",
                       "Instant Standups & Handoffs\nfrom GitHub, Slack, Jira",
                       "deepthread.ai")

    problem_block(story,
        "Software teams waste hours every week writing standup reports, "
        "searching for context across 5\u20137 tools, and creating handoff documents. "
        "Information gets lost between Slack threads, Jira tickets, and GitHub PRs. "
        "Remote work is harder than it needs to be.")

    value_prop_block(story, [
        ("10-Second Standups",
         "Generated automatically from your connected tools. No more writing reports manually."),
        ("Full Context, No Digging",
         "AI follows links between platforms and builds complete context automatically."),
        ("Seamless Handoffs",
         "Transition documents generated with one click. Nothing falls through the cracks."),
        ("Zero Manual Reporting",
         "AI does the summarizing so your team can focus on building."),
        ("7 Platform Integrations",
         "GitHub, Slack, Jira, Linear, Confluence, Notion, Google Docs \u2014 all connected."),
    ])

    step_flow_block(story, [
        ("Connect Your Tools", "Link GitHub, Slack, Jira, Linear, Confluence, Notion, and Google Docs."),
        ("AI Builds Context", "DeepThread\u2019s AI follows cross-platform links and assembles full context automatically."),
        ("Generate Reports", "Create instant standups, handoff documents, or issue summaries with one click."),
        ("Work Async Better", "Your team stays aligned with zero manual reporting effort."),
    ])

    cta_block(story, "Book a Free Consultation", "deepthread.ai")


def build_back(story):
    header_with_banner(story, "DeepThread",
                       "Feature Breakdown & Details", "deepthread.ai")

    story.append(banner_spacer(0.3))

    feature_grid(story, [
        ("Cross-Platform Context Engine",
         "Follows links between platforms to provide full context, not fragments. One connected view."),
        ("Instant Standup Generation",
         "AI generates standup reports from your tools in seconds. What used to take 10 minutes takes 10 seconds."),
        ("Handoff Document Creation",
         "Seamless transition docs for team changes, project handoffs, and knowledge transfer."),
        ("Issue Summaries",
         "AI-summarized context for any issue, ticket, or PR \u2014 pulled from across all connected platforms."),
        ("Workflow Automation",
         "Integrate CRMs, ERPs, and productivity tools with custom automated workflows."),
        ("No-Code Integrations",
         "Uses Make, Airtable, and Zapier for rapid deployment and customization."),
        ("Predictive Automation",
         "Anticipates needs based on patterns in your team\u2019s activity across platforms."),
        ("Multi-Platform Search",
         "Search across all connected tools from one interface. Find anything, anywhere, instantly."),
    ])

    who_its_for_block(story, [
        "Software development teams tired of manual reporting",
        "Product managers juggling context across multiple tools",
        "Engineering leads who need visibility without micromanaging",
        "Remote teams losing alignment due to fragmented communication",
        "CTOs looking to improve developer productivity",
    ])

    trust_elements_block(story, [
        ("7", "Platform\nIntegrations"),
        ("10s", "Standup\nGeneration"),
        ("Zero", "Manual\nReporting"),
    ])

    pricing_hint_block(story,
        "Contact us for pricing.\nDeveloper Tools \u2022 Productivity \u2022 AI")

    about_algolog_block(story)
    contact_block(story)


if __name__ == "__main__":
    build_banner_pdf(OUTPUT_PATH, build_front, build_back)
