#!/usr/bin/env python3
"""ED-03 Call-Funnel Financial Model (restated from ericdeeran.co/financial-model, S-06).

Defaults are Eric Deeran's stated "typical" values: assumptions, not measurements.
Run: python3 formulas/call_funnel.py [--spend 10000 --cpl 65 --cpc 200 --show .7 --close .25 --cash 10000 --contract 15000]
"""
import argparse


def model(spend, cpl, cpc, show, close, cash, contract):
    calls = spend / cpc
    leads = spend / cpl
    live = calls * show
    clients = live * close
    cash_in = clients * cash
    booked = clients * contract
    return {
        "leads": leads,
        "booking_rate": cpl / cpc,
        "booked_calls": calls,
        "live_calls": live,
        "clients": clients,
        "cash_collected": cash_in,
        "contract_value": booked,
        "cash_roas": cash_in / spend,
        "contract_roas": booked / spend,
        "cash_roi": (cash_in - spend) / spend,
        "cac": spend / clients if clients else float("inf"),
        "cash_per_booked_call": show * close * cash,
        "breakeven_close_rate": cpc / (show * cash),
        "cash_upfront_share": cash / contract,
    }


if __name__ == "__main__":
    a = argparse.ArgumentParser()
    for k, v in [("spend", 10000), ("cpl", 65), ("cpc", 200), ("show", .7),
                 ("close", .25), ("cash", 10000), ("contract", 15000)]:
        a.add_argument("--" + k, type=float, default=v)
    r = model(**vars(a.parse_args()))
    for k, v in r.items():
        print(f"{k:22} {v:,.4g}")
