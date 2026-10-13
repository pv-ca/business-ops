---
name: finance
description: "Use whenever a business decision depends on numbers: cash flow, margin, pricing math, break-even, unit economics (CAC, LTV, payback), budget, whether the company can afford a hire or an investment, or when the user wants a financial number explained in plain language. Works from the company's saved context."
---

# Finance

## Before you start

Read and follow `../business-context/references/coach-protocol.md` (a path relative to this skill's folder). It explains how to find the context, pick the company, what may be claimed and how to shape the answer. Context folder configured in the plugin: `${user_config.context_folder}`. When that shows no real path (it is empty, or the placeholder appears unreplaced because this agent has no plugin settings), the protocol says where to look. `references/books.md` lists the frameworks.

## How to work

1. **Use the user's real numbers.** Ask for them or read them from files the user provides. A number the context marks as unknown stays unknown: show the formula, say which inputs are missing and how to get them. An invented figure in a financial analysis leads to a real decision on false ground.
2. **Keep revenue, cash and profit apart.** A sale is not cash until it is received; a profitable month can still run out of cash.
3. **Build the simplest model that answers the question:** projected cash flow for "can we afford it", contribution margin per product or plan for "what should we push", break-even for "how much do we need to sell".
4. **State every assumption** and show how the answer changes if the main one is wrong (a best, base and worst case is usually enough).
5. **Explain each number in plain language** and what decision it supports.
6. **Know the limit.** Tax, accounting and payroll rules need an accountant; explain the business consequence and say when to consult one. Verify current rates and rules on the web with source and date.

## Typical deliverables

Cash-flow projection, margin by product or plan, break-even calculation, unit-economics sheet, pricing scenario comparison, simple budget.

## Mistakes this skill prevents

- Treating revenue as money in the bank.
- Pricing from cost alone, ignoring value and capacity.
- A precise-looking spreadsheet built on guessed inputs.
- Ignoring the owner's own time as a cost.

## Neighbouring skills

`brand-offer` (price presentation and packages), `recurring-revenue` (recurring-revenue economics), `management-strategy` (what the numbers should decide).
