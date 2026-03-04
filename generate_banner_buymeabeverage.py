"""
Generate BuyMeABeverage Product Banner — Front + Back
40 x 87.3 inch roll-up banner
"""

import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from generate_banner_base import *

OUTPUT_PATH = os.path.join(PROPOSALS_DIR, "Banner-BuyMeABeverage.pdf")


def build_front(story):
    header_with_banner(story, "BuyMeABeverage",
                       "The Simplest Way to Accept\nTips & Gifts in Nigeria",
                       "buymeabeverage.com")

    problem_block(story,
        "Content creators, freelancers, and professionals in Nigeria have no easy way "
        "to accept casual tips and gifts from supporters. Setting up payment collection "
        "is complex, and international platforms don\u2019t support Nigerian banks well. "
        "Your supporters want to show appreciation \u2014 make it effortless.")

    value_prop_block(story, [
        ("Custom Shareable Link",
         "Get your own buymeabeverage.com/[yourname] link. Share it anywhere \u2014 bio, WhatsApp, Instagram."),
        ("Instant Payouts",
         "Funds settle directly to your Nigerian bank account via Paystack. No waiting, no hassle."),
        ("Zero Complexity",
         "No app download, no complex setup. Create your profile and start receiving in minutes."),
    ])

    step_flow_block(story, [
        ("Create Your Profile", "Sign up for free on buymeabeverage.com. Takes less than 2 minutes."),
        ("Get Your Link", "Receive your custom shareable link \u2014 buymeabeverage.com/[yourname]."),
        ("Share Everywhere", "Put it on social media, WhatsApp status, email signatures, business cards."),
        ("Receive Gifts", "Supporters buy you a beverage. Funds go straight to your bank account."),
    ])

    cta_block(story, "Get Started for Free", "buymeabeverage.com")


def build_back(story):
    header_with_banner(story, "BuyMeABeverage",
                       "Feature Breakdown & Details", "buymeabeverage.com")

    story.append(banner_spacer(0.3))

    feature_grid(story, [
        ("Custom Payment Links",
         "Your own branded link that supporters can use to send gifts anytime."),
        ("Paystack-Powered Payments",
         "Secure payment processing through Nigeria\u2019s most trusted payment platform."),
        ("Direct Bank Settlement",
         "Funds settle directly to your Nigerian bank account. No intermediary holding your money."),
        ("Transaction History",
         "See every gift received, when it came in, and from whom. Full transparency."),
        ("Merchant Dashboard",
         "Manage your profile, track earnings, and view analytics from one clean dashboard."),
        ("Mobile-Responsive",
         "Works perfectly on any device \u2014 your supporters can gift from their phone in seconds."),
        ("Social Sharing",
         "Easy sharing to WhatsApp, Twitter, Instagram, and more. One tap to spread your link."),
        ("No App Download",
         "Everything works in the browser. Supporters don\u2019t need to install anything."),
    ])

    who_its_for_block(story, [
        "Content creators looking for a simple way to monetize",
        "Freelancers accepting tips for great work",
        "Social media influencers connecting with supporters",
        "Musicians, writers, and artists accepting gifts from fans",
        "Professionals building a personal brand",
    ])

    trust_elements_block(story, [
        ("Free", "To Create\nYour Profile"),
        ("Paystack", "Trusted Payment\nProcessing"),
        ("Instant", "Bank\nSettlement"),
    ])

    pricing_hint_block(story,
        "Free to use.\nPaystack transaction fees: 1.5% capped at NGN 2,000.")

    about_algolog_block(story)
    contact_block(story)


if __name__ == "__main__":
    build_banner_pdf(OUTPUT_PATH, build_front, build_back)
