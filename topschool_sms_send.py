# -*- coding: utf-8 -*-
"""TOPSCHOOL - bulk SMS sender (Termii).

Reads a leads CSV (from topschool_export_leads.py) and sends one personalised
SMS per school through Termii's API. Defaults to a DRY RUN that prints what
would be sent and the projected cost; add --send to actually deliver.

Setup (run once in a normal terminal, values from your Termii dashboard):
    setx TERMII_API_KEY   <your-api-key>
    setx TERMII_SENDER_ID TOPSCHOOL         (must be an APPROVED sender id)

Usage:
    python topschool_sms_send.py --csv "C:\\path\\TOPSCHOOL-leads-YYYY-MM-DD.csv"
    python topschool_sms_send.py --csv ... --segment offer          # only "offer page - not paid"
    python topschool_sms_send.py --csv ... --limit 5 --send          # live send, capped at 5
    python topschool_sms_send.py --csv ... --send                    # live send to all

Notes:
  * Nigerian promotional SMS mostly hits DND numbers; Termii routes these on
    its DND/generic channel. Keep messages <=160 GSM-7 chars = 1 unit.
  * Sender id "TOPSCHOOL" must be registered & approved in Termii first.
"""
import os, csv, json, time, argparse, ssl, urllib.request, urllib.error

API_KEY = os.environ.get("TERMII_API_KEY")
SENDER = os.environ.get("TERMII_SENDER_ID", "TOPSCHOOL")
ENDPOINT = "https://api.ng.termii.com/api/sms/send"
CHANNEL = "generic"        # "generic" carries DND traffic on Termii
UNIT_COST_NGN = 4.0        # conservative per-unit estimate for cost projection

# 155 chars -> stays within one 160-char GSM-7 unit after {school} fill.
TEMPLATE = ("Hi {school}, this is TOPSCHOOL (topschool.app). Compile results & "
            "print report cards in minutes. Free demo: call 08103698758 -Algolog")


def seg_match(plan, seg):
    p = (plan or "").lower()
    if seg == "all":
        return True
    if seg == "offer":
        return "offer" in p
    if seg == "free":
        return "free" in p
    if seg == "paying":
        return "pay" in p
    return True


def load(csv_path, seg):
    out = []
    with open(csv_path, newline="", encoding="utf-8-sig") as f:
        for r in csv.DictReader(f):
            if not r.get("phone_intl"):
                continue
            if not seg_match(r.get("plan"), seg):
                continue
            out.append(r)
    return out


def build(msg_school):
    m = TEMPLATE.format(school=(msg_school or "there").strip())
    return m[:160]


def send_one(to, text):
    payload = {
        "to": to, "from": SENDER, "sms": text,
        "type": "plain", "channel": CHANNEL, "api_key": API_KEY,
    }
    data = json.dumps(payload).encode()
    req = urllib.request.Request(ENDPOINT, data=data,
                                 headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, context=ssl.create_default_context(),
                                timeout=45) as r:
        return r.status, r.read().decode("utf-8", "replace")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--csv", required=True)
    ap.add_argument("--segment", default="all",
                    choices=["all", "offer", "free", "paying"])
    ap.add_argument("--limit", type=int, default=0, help="cap recipients (0 = no cap)")
    ap.add_argument("--send", action="store_true", help="actually send (default is dry run)")
    a = ap.parse_args()

    rows = load(a.csv, a.segment)
    if a.limit:
        rows = rows[: a.limit]
    units = len(rows)  # 1 unit each while template stays <=160 chars
    print(f"recipients: {units}  segment: {a.segment}")
    print(f"projected cost @ NGN{UNIT_COST_NGN:.1f}/unit: NGN{units*UNIT_COST_NGN:,.0f}")
    print("sample:", build(rows[0]["school"]) if rows else "(none)")

    if not a.send:
        print("\nDRY RUN - nothing sent. Re-run with --send to deliver.")
        return
    if not API_KEY:
        raise SystemExit("Set TERMII_API_KEY first.")

    ok = fail = 0
    for r in rows:
        to = r["phone_intl"]
        try:
            st, body = send_one(to, build(r["school"]))
            good = st == 200 and '"code":"ok"' in body.replace(" ", "")
            ok += good
            fail += (not good)
            if not good:
                print("FAIL", to, st, body[:160])
        except urllib.error.HTTPError as e:
            fail += 1
            print("HTTP", to, e.code, e.read().decode("utf-8", "replace")[:160])
        except Exception as e:
            fail += 1
            print("ERR", to, type(e).__name__, e)
        time.sleep(0.4)  # gentle pacing
    print(f"\nsent ok: {ok}  failed: {fail}")


if __name__ == "__main__":
    main()
