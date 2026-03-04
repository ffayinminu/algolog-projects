"""
Generate BuyMeAShawarma Product Banner — Front + Back
40 x 87.3 inch roll-up banner
"""

import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from generate_banner_base import *

OUTPUT_PATH = os.path.join(PROPOSALS_DIR, "Banner-BuyMeAShawarma.pdf")


def build_front(story):
    header_with_banner(story, "BuyMeAShawarma",
                       "Support Your Favorites \u2014\nOne Shawarma at a Time",
                       "buymeshawarma.com")

    problem_block(story,
        "Content creators, freelancers, and professionals in Nigeria have no fun, "
        "culturally relevant way to accept tips from supporters. International tipping "
        "platforms don\u2019t work well with Nigerian banks, and generic payment links "
        "feel impersonal. Shawarma is Nigeria\u2019s favorite \u2014 make gifting fun.")

    value_prop_block(story, [
        ("Culturally Relevant",
         "Shawarma is Nigeria\u2019s most beloved street food. It makes gifting relatable, fun, and personal."),
        ("Custom Shareable Link",
         "Get your own buymeshawarma.com/[yourname] link. Share it everywhere."),
        ("Instant Bank Settlement",
         "Funds go directly to your Nigerian bank account via Paystack. Fast, reliable, transparent."),
    ])

    step_flow_block(story, [
        ("Create Your Profile", "Sign up for free on buymeshawarma.com. Quick, simple, no hassle."),
        ("Get Your Link", "Receive your custom link \u2014 buymeshawarma.com/[yourname]."),
        ("Share It Everywhere", "Social media, WhatsApp, bio links, email signatures \u2014 anywhere your audience is."),
        ("Get Shawarma'd", "Fans buy you shawarma, money hits your bank account. Simple."),
    ])

    cta_block(story, "Get Started for Free", "buymeshawarma.com")


def build_back(story):
    header_with_banner(story, "BuyMeAShawarma",
                       "Feature Breakdown & Details", "buymeshawarma.com")

    story.append(banner_spacer(0.3))

    feature_grid(story, [
        ("Custom Payment Links",
         "Your own branded shawarma-themed link that supporters use to send gifts."),
        ("Paystack-Powered Payments",
         "Secure, trusted payment processing through Nigeria\u2019s leading payment platform."),
        ("Direct Bank Settlement",
         "Funds settle directly to your bank account. No holding, no delays."),
        ("Transaction History",
         "Track every gift \u2014 who sent it, when, and how much. Full visibility."),
        ("Merchant Dashboard",
         "Manage your profile, track earnings, and monitor your growth from one place."),
        ("Mobile-Responsive",
         "Works beautifully on any device. Supporters can gift from their phone in seconds."),
        ("Social Sharing",
         "One-tap sharing to WhatsApp, Twitter, Instagram. Spread your link effortlessly."),
        ("Fun Food-Themed Experience",
         "A uniquely Nigerian gifting experience that makes both giving and receiving enjoyable."),
    ])

    who_its_for_block(story, [
        "Content creators looking for a fun monetization tool",
        "Freelancers accepting appreciation from happy clients",
        "Social media influencers connecting with their community",
        "Anyone in Nigeria who wants to accept casual tips and gifts",
    ])

    trust_elements_block(story, [
        ("Free", "To Create\nYour Profile"),
        ("SkillPay", "Proven Backend\nInfrastructure"),
        ("Nigerian", "Built for\nLocal Banks"),
    ])

    pricing_hint_block(story,
        "Free to use.\nPaystack transaction fees: 1.5% capped at NGN 2,000.")

    about_algolog_block(story)
    contact_block(story)


if __name__ == "__main__":
    build_banner_pdf(OUTPUT_PATH, build_front, build_back)
