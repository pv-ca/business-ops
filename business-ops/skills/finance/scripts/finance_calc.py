#!/usr/bin/env python3
"""Exact arithmetic for the three models the finance skill builds most.

Standard library only, Python 3.9 or newer. Reads numbers from the command
line or a JSON file, writes JSON to standard output, touches nothing else.
Every number comes from the user: the script never fills in a missing one.

    python3 finance_calc.py break-even --fixed-costs 12000 --price 99 --variable-cost 22
    python3 finance_calc.py unit-economics --cac 450 --revenue-per-customer 99 \
        --gross-margin 80 --monthly-churn 3
    python3 finance_calc.py cash-flow plan.json

Percentages are written as percentages (80 means 80%). The formulas are in
references/formulas.md, beside this folder.
"""
import argparse
import json
import math
import sys
from decimal import ROUND_HALF_UP, Decimal, InvalidOperation
from pathlib import Path

CENT = Decimal("0.01")


def money(value):
    return float(value.quantize(CENT, rounding=ROUND_HALF_UP))


def number(text):
    try:
        value = Decimal(str(text))
    except InvalidOperation:
        raise argparse.ArgumentTypeError(f"not a number: {text}")
    if not value.is_finite():
        raise argparse.ArgumentTypeError(f"not a number: {text}")
    return value


class InputError(Exception):
    pass


def break_even(fixed_costs, price, variable_cost):
    margin = price - variable_cost
    if price <= 0:
        raise InputError("price must be above zero")
    if margin <= 0:
        raise InputError("price does not cover the variable cost, so no volume breaks even")
    units = fixed_costs / margin
    ratio = margin / price
    return {
        "contribution_margin_per_unit": money(margin),
        "contribution_margin_percent": money(ratio * 100),
        "break_even_units": math.ceil(units),
        "break_even_units_exact": money(units),
        "break_even_revenue": money(fixed_costs / ratio),
    }


def unit_economics(cac, revenue_per_customer, gross_margin, monthly_churn):
    if not 0 < gross_margin <= 100:
        raise InputError("gross margin must be above 0 and at most 100 percent")
    if not 0 < monthly_churn <= 100:
        raise InputError("monthly churn must be above 0 and at most 100 percent; with no churn the lifetime has no end and LTV cannot be computed")
    if revenue_per_customer <= 0:
        raise InputError("revenue per customer must be above zero")
    margin_per_month = revenue_per_customer * gross_margin / 100
    lifetime = 100 / monthly_churn
    ltv = margin_per_month * lifetime
    result = {
        "gross_margin_per_customer_per_month": money(margin_per_month),
        "average_lifetime_months": money(lifetime),
        "ltv": money(ltv),
    }
    if cac > 0:
        result["ltv_to_cac"] = money(ltv / cac)
        result["cac_payback_months"] = money(cac / margin_per_month)
    else:
        result["note"] = "CAC is zero, so the LTV to CAC ratio and the payback are not computed"
    return result


def project(opening, months, inflow_factor, outflow_factor):
    balance = opening
    rows = []
    for index, month in enumerate(months, 1):
        try:
            inflows = number(month["inflows"]) * inflow_factor
            outflows = number(month["outflows"]) * outflow_factor
        except (KeyError, TypeError, argparse.ArgumentTypeError):
            raise InputError(f"month {index} needs numeric \"inflows\" and \"outflows\"")
        balance += inflows - outflows
        rows.append({
            "month": month.get("label", str(index)),
            "inflows": money(inflows),
            "outflows": money(outflows),
            "net": money(inflows - outflows),
            "closing_balance": money(balance),
        })
    lowest = min(rows, key=lambda row: row["closing_balance"])
    negative = next((row["month"] for row in rows if row["closing_balance"] < 0), None)
    return {
        "months": rows,
        "closing_balance": rows[-1]["closing_balance"],
        "lowest_balance": lowest["closing_balance"],
        "lowest_balance_month": lowest["month"],
        "first_negative_month": negative,
    }


def cash_flow(plan):
    """plan: {"opening_balance", "months": [{"label", "inflows", "outflows"}], "scenarios": {name: {"inflows": %, "outflows": %}}}"""
    try:
        opening = number(plan["opening_balance"])
        months = plan["months"]
    except (KeyError, TypeError, argparse.ArgumentTypeError):
        raise InputError("the plan needs a numeric \"opening_balance\" and a \"months\" list")
    if not isinstance(months, list) or not months:
        raise InputError("\"months\" must list at least one month")
    scenarios = plan.get("scenarios") or {"base": {}}
    result = {"opening_balance": money(opening), "scenarios": {}}
    for name, change in scenarios.items():
        try:
            inflow_factor = number(change.get("inflows", 100)) / 100
            outflow_factor = number(change.get("outflows", 100)) / 100
        except (AttributeError, argparse.ArgumentTypeError):
            raise InputError(f"scenario {name} must give \"inflows\" and \"outflows\" as percentages of the plan")
        result["scenarios"][name] = project(opening, months, inflow_factor, outflow_factor)
    return result


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    commands = parser.add_subparsers(dest="command", required=True)

    be = commands.add_parser("break-even", help="units and revenue needed to cover fixed costs")
    be.add_argument("--fixed-costs", type=number, required=True, help="fixed costs of the period")
    be.add_argument("--price", type=number, required=True, help="price per unit")
    be.add_argument("--variable-cost", type=number, required=True, help="variable cost per unit")

    ue = commands.add_parser("unit-economics", help="LTV, LTV to CAC and payback for recurring revenue")
    ue.add_argument("--cac", type=number, required=True, help="cost to acquire one customer")
    ue.add_argument("--revenue-per-customer", type=number, required=True, help="average revenue per customer per month")
    ue.add_argument("--gross-margin", type=number, required=True, help="gross margin, in percent")
    ue.add_argument("--monthly-churn", type=number, required=True, help="customers lost per month, in percent")

    cf = commands.add_parser("cash-flow", help="month-by-month balance from a JSON plan, per scenario")
    cf.add_argument("plan", help="path to the JSON plan, or - for standard input")

    args = parser.parse_args(argv)
    try:
        if args.command == "break-even":
            result = break_even(args.fixed_costs, args.price, args.variable_cost)
        elif args.command == "unit-economics":
            result = unit_economics(args.cac, args.revenue_per_customer, args.gross_margin, args.monthly_churn)
        else:
            text = sys.stdin.read() if args.plan == "-" else Path(args.plan).read_text(encoding="utf-8")
            result = cash_flow(json.loads(text))
    except InputError as problem:
        print(json.dumps({"error": str(problem)}))
        return 1
    except (OSError, json.JSONDecodeError) as problem:
        print(json.dumps({"error": f"could not read the plan: {problem}"}))
        return 1
    print(json.dumps(result, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
