# Formulas

The definitions `scripts/finance_calc.py` uses. Financial terms have more than one definition in use, so say which one a number follows whenever you report it, and use these when the user has not named another. Without the script, compute by hand with the same formulas and show the working.

Percentages are entered as percentages: 80 means 80%.

## Break-even

```
python3 scripts/finance_calc.py break-even --fixed-costs 12000 --price 99 --variable-cost 22
```

- Contribution margin per unit = price − variable cost per unit.
- Contribution margin percent = contribution margin per unit ÷ price.
- Break-even units = fixed costs ÷ contribution margin per unit, rounded up, because a fraction of a sale does not exist.
- Break-even revenue = fixed costs ÷ contribution margin percent.

Fixed costs and the result refer to the same period: monthly costs give the units needed per month. With several products, run it per product only when fixed costs can be split honestly; otherwise use the average price and variable cost of the real sales mix and say so.

## Unit economics for recurring revenue

```
python3 scripts/finance_calc.py unit-economics --cac 450 --revenue-per-customer 99 --gross-margin 80 --monthly-churn 3
```

- Gross margin per customer per month = revenue per customer per month × gross margin.
- Average lifetime in months = 1 ÷ monthly churn.
- LTV = gross margin per customer per month × average lifetime. It is margin, not revenue: revenue-based LTV overstates what a customer is worth.
- LTV to CAC = LTV ÷ CAC.
- CAC payback in months = CAC ÷ gross margin per customer per month.

This assumes churn and revenue per customer stay constant, which is rarely true in a young company: early churn is usually higher than later churn. With fewer than a few dozen customers or a few months of history, report the result as a hypothesis. CAC includes the sales and marketing cost of the period, salaries and tools included, divided by the customers won in it.

## Cash-flow projection

```
python3 scripts/finance_calc.py cash-flow plan.json
```

The plan is a JSON file. Write it in the request's deliverables folder, so the user can see and correct the inputs:

```json
{
  "opening_balance": 20000,
  "months": [
    {"label": "2026-01", "inflows": 30000, "outflows": 34000},
    {"label": "2026-02", "inflows": 32000, "outflows": 34000}
  ],
  "scenarios": {
    "base": {},
    "worst": {"inflows": 80, "outflows": 105},
    "best": {"inflows": 110}
  }
}
```

- Inflows are money received in that month and outflows money paid in it, not sales made or bills issued.
- Closing balance = previous balance + inflows − outflows.
- A scenario multiplies every month's inflows and outflows by the given percentage of the plan (80 means 80% of the planned inflows). Left out, a value stays at 100.
- For each scenario the result gives the month with the lowest balance and the first month that closes below zero, which is the answer to "can we afford it" and "when do we need the money".
