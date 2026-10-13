---
name: customer-success
description: "Post-sale work for one of the user's own companies, grounded in that company's saved context and delivered as coaching. Use whenever the user asks for an onboarding or implementation plan, a sales-to-post-sale handoff, a definition of activation, a way to follow up customers or students, risk signals, a reply to a cancellation request, churn analysis, renewal, expansion, a referral request, or welcome, check-in and retention messages (e.g. \"the customer wants to cancel\", \"how do I onboard a new customer\", \"this client went quiet\")."
---

# Customer success

## Before you start

Read and follow `../business-context/references/coach-protocol.md` (a path relative to this skill's folder). It explains how to find the context, pick the company, what may be claimed and how to shape the answer. Context folder configured in the plugin: `${user_config.context_folder}`. When that shows no real path (it is empty, or the placeholder appears unreplaced because this agent has no plugin settings), the protocol says where to look.

The method lives in `references/customer-success-lifecycle-playbook.md`. Read only the part the task needs. `references/books.md` maps the books.

## Principle

Customer success means helping suitable customers reach the outcome that justifies staying. It is not reactive support, frequent contact without a purpose, or preventing every cancellation. A problem born in the product, in delivery or in a badly fitted sale is not solved by more follow-up, so name the real cause even when it lies outside post-sale.

## Calibrate to the kind of business

| | B2B, software or service for companies | B2C, service for individuals |
| --- | --- | --- |
| Who the customer is | Several roles: who pays, who decides, who uses | One person |
| Onboarding | Data, configuration, enablement, first workflow running | Agree routine, schedule, material and one clear goal |
| Follow-up | Milestones and owners on both sides | Close conversation in the channel the person uses |
| Avoid | Meetings with no value agenda | Enterprise rituals (QBRs, formal success plans, complex health scores) |

The company context says which column applies and carries the company-specific adaptation when there is one.

## How to work

1. **Start from the reason for buying.** What the customer wanted to solve, what was promised, what was left out. A promise made in the sale that the operation does not keep is the first cause of churn (section 6, expectation debt).
2. **Separate the milestones** (section 12): contract, preparation, implementation, enablement, activation, first value, habitual use. Payment or signature is not activation.
3. **Define activation as an observable event** that indicates the customer will continue. Until there is data it is a hypothesis; say how to validate it (section 15).
4. **Shorten time to first value.** Remove from onboarding whatever does not lead to it (section 13).
5. **Make value visible.** A customer can be gaining and not notice. Show the starting point, what changed and the next milestone, without guaranteeing results (section 20).
6. **Read the health signals** the business can already observe (use, attendance, pending items, replies, payments). Build a score only when data predicts something.
7. **For risk or a request to leave**, investigate the cause before offering anything: fit, expectation, activation, adoption, value, price, the customer's circumstances (sections 24, 31, 33). Not every cancellation should be reversed, and a discount does not repair missing value.
8. **Expansion and referral** come after recognized value, never before (sections 28 and 29).

## Typical deliverables

Templates in section 44 of the playbook: sales-to-post-sale handoff, onboarding plan, risk playbook, renewal plan, churn analysis. Also welcome, check-in, win-back and referral-request messages in the tone the company context defines.

## Mistakes this skill prevents

- Measuring activation by payment or login.
- Following up everyone the same way, regardless of risk and value.
- Offering a discount before understanding why the customer wants to leave.
- Pushing a bigger plan, module or frequency on someone who has not yet seen value in what they have.
- Assigning to post-sale a problem that started in the sale or the product.

## Neighbouring skills

`sales` (before the close), `recurring-revenue` (lifecycle metrics and roles), `market-research` (neutral interviews with customers who stayed or left).
