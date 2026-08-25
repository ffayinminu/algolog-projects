# -*- coding: utf-8 -*-
"""TOPSCHOOL - daily leads export.

Pulls the admin leads page (https://schoolsapi.algolog.co/api/admin/leads),
parses every signup card, and writes a timestamped CSV of prospects with
email + WhatsApp/phone + follow-up status + plan tier.

Credentials are read from environment variables so nothing secret lives in
this file or in git:

    setx TOPSCHOOL_USER algolog
    setx TOPSCHOOL_PASS <the-password>      (run once in a normal terminal)

Then, any day:

    python topschool_export_leads.py

Output: Desktop\TOPSCHOOL-leads-YYYY-MM-DD.csv
"""
import os, re, csv, ssl, base64, datetime, collections, html as H
import urllib.request, urllib.error

URL = "https://schoolsapi.algolog.co/api/admin/leads"
USER = os.environ.get("TOPSCHOOL_USER", "algolog")
PW = os.environ.get("TOPSCHOOL_PASS")

COLS = ["school", "contact", "email", "phone_intl", "phone_local",
        "pupils", "signed_up_utc", "status", "plan", "lead_id"]


def fetch_html():
    if not PW:
        raise SystemExit("Set TOPSCHOOL_PASS (and optionally TOPSCHOOL_USER) "
                         "environment variables first.")
    tok = base64.b64encode(f"{USER}:{PW}".encode()).decode()
    req = urllib.request.Request(URL, headers={"Authorization": "Basic " + tok})
    with urllib.request.urlopen(req, context=ssl.create_default_context(),
                                timeout=60) as r:
        return r.read().decode("utf-8", "replace")


def g(pat, s):
    m = re.search(pat, s, re.S)
    return H.unescape(m.group(1).strip()) if m else ""


def parse(html):
    rows = []
    for c in re.split(r"<details", html)[1:]:
        intl = g(r"wa\.me/(\d+)", c)
        local = "0" + intl[3:] if intl.startswith("234") and len(intl) >= 13 else intl
        rows.append({
            "school": g(r'class="s-school">([^<]*)<', c),
            "contact": g(r'class="s-contact">([^<]*)<', c) or g(r"<b>Contact</b>\s*([^<]+)", c),
            "email": g(r"<b>Email</b>\s*([^<]+)", c),
            "phone_intl": intl,
            "phone_local": local,
            "pupils": g(r"<b>Pupils</b>\s*([^<]+)", c),
            "signed_up_utc": g(r"<b>Signed up</b>\s*([^<]+?)</div>", c),
            "status": g(r'<option value="([^"]+)" selected', c),
            "plan": g(r'<span class="badge" [^>]*>([^<]+)</span>', c),
            "lead_id": g(r'id="lead-([0-9a-f\-]+)"', c),
        })
    seen, uniq = set(), []
    for r in rows:
        if r["lead_id"] and r["lead_id"] in seen:
            continue
        seen.add(r["lead_id"])
        uniq.append(r)
    return uniq


def main():
    rows = parse(fetch_html())
    desk = os.path.join(os.path.expanduser("~"), "Desktop")
    today = datetime.date.today().isoformat()
    out = os.path.join(desk, f"TOPSCHOOL-leads-{today}.csv")
    with open(out, "w", newline="", encoding="utf-8-sig") as f:
        w = csv.DictWriter(f, fieldnames=COLS)
        w.writeheader()
        w.writerows(rows)
    print("TOTAL LEADS:", len(rows))
    print("with email:", sum(1 for r in rows if "@" in r["email"]))
    print("with phone:", sum(1 for r in rows if r["phone_intl"]))
    print("by status:", dict(collections.Counter(r["status"] or "(none)" for r in rows)))
    print("by plan:", dict(collections.Counter(r["plan"] or "(none)" for r in rows)))
    print("CSV:", out)


if __name__ == "__main__":
    main()
