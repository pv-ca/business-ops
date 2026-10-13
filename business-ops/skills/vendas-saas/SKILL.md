---
name: vendas-saas
description: "Designs and assesses the recurring-revenue system of one of the user's own companies (SaaS or subscription service), grounded in that company's saved context and delivered as coaching. Use whenever the user asks whether they are ready to scale, how to organize the funnel and customer lifecycle, which metrics to track (MRR, churn, CAC, payback), how to split sales and post-sale roles, how to set up pipeline, forecast or CRM, whether to hire for sales, or how to run an ABM pilot."
---

# Vendas SaaS (recurring revenue)

## Before you start

Read and follow `../contexto-negocio/references/coach-protocol.md` (a path relative to this skill's folder). It explains how to find the context, pick the company, what may be claimed and how to shape the answer. Context folder configured in the plugin: `${user_config.pasta_contexto}`. When that shows no real path (it is empty, or the placeholder appears unreplaced because this agent has no plugin settings), the protocol says where to look.

The method lives in `references/revenue-operations-and-scale-playbook.md`. Read only the part the task needs. `references/books.md` maps the books.

The sales conversation itself (outreach, discovery, demo, proposal) belongs to the `vendas` skill. This skill covers the system around it.

## First: which stage is the business in

Scaling validates nothing; it multiplies whatever is already there, including the flaws. Before recommending a team, a tool, ABM or a growth target, assess readiness (section 3 of the playbook) across seven areas, rating each as unknown, weak evidence, emerging, repeatable or scalable:

market and customer, offer, commercial motion, delivery, retention, economics, data and management.

| Stage | Do | Avoid |
| --- | --- | --- |
| Discovery or validation | Research, founder-led selling, pilots, a simple record of every conversation | Hiring a team, automating, setting volume targets |
| Emerging repeatability | Document what worked, qualification criteria, a first dashboard | Specializing roles too early |
| Scale | Roles, capacity, forecast, data governance | Growing without knowing margin per segment |

If the company context marks ideal customer, price or channel as a hypothesis or unknown, the stage is discovery or validation and the recommendation starts by reducing that uncertainty.

## How to work

1. **Map the whole lifecycle**, not only the funnel up to the close: awareness, education, selection, commit, onboarding, use and expansion (Part II). In recurring revenue most of the value arrives after the signature, so retention and expansion are part of the sale (the Bowtie model).
2. **Find the moment that matters most** in each phase: where the customer decides to continue or drop, and who owns it.
3. **Build the economics from numbers that exist** (Part IV): revenue, cash and profit are different things; acquisition cost, retention cost, time to profitability. A number the context lacks is listed as "to be collected", with how to collect it. Do not estimate a company metric and present it as data.
4. **Define roles from the work that exists**, not from a large-company org chart (Part VI). While the founder sells, the priority is to learn and record, not to delegate.
5. **Instrument the minimum** (Part VII): one system of record, few mandatory fields, each metric tied to a decision, an owner and an action.
6. **ABM only after the readiness check** (Part VIII), as a pilot with a bounded list, an owner and a measurement period. It does not apply to consumer sales.

## Typical deliverables

Scale-readiness assessment, lifecycle map with owners, minimum metrics dashboard, role and handoff design, ABM pilot plan, scale plan (section 53 of the playbook).

## Mistakes this skill prevents

- Copying a large SaaS structure (SDR, AE, CS, RevOps) into a business still validating its offer.
- Treating MRR as cash, or growth as proof of the model.
- A dashboard with many metrics and no decision.
- Automating a process that has not been standardized.

## Neighbouring skills

`vendas` (the conversation), `sucesso-cliente` (onboarding, retention, expansion), `financas` (cash, margin, pricing), `pesquisa-mercado` (validating segment and ideal customer).
