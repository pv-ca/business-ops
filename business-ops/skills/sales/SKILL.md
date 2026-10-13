---
name: sales
description: "Use whenever the user wants to answer or approach a lead, prepare or review a sales conversation, discovery call, demo or follow-up, handle a price objection, qualify a lead or revive a stalled deal, in B2B or B2C, including chat and e-mail messages (e.g. \"reply to this lead\", \"write a discovery call script\", \"the customer said it is too expensive\"). Works from the company's saved context. The proposal or deck file belongs to `proposals-presentations`, and a neutral interview with no selling to `market-research`."
---

# Sales

## Before you start

Read and follow `../business-context/references/coach-protocol.md` (a path relative to this skill's folder). It explains how to find the context, pick the company, what may be claimed and how to shape the answer. Context folder configured in the plugin: `${user_config.context_folder}`. When that shows no real path (it is empty, or the placeholder appears unreplaced because this agent has no plugin settings), the protocol says where to look.

The method lives in `references/commercial-sales-playbook.md`. It is long: read only the part the task needs. `references/books.md` maps each method to its book.

## Choose the method by the decision

| The user needs to | Method | Playbook part |
| --- | --- | --- |
| Understand why customers start looking and what holds them back | Demand-Side Sales | II |
| Diagnose, qualify or unblock a live opportunity | Gap Selling | III |
| Build a thesis for a B2B sale with several stakeholders | Challenger, only with evidence | IV |
| Write outreach, run a meeting, follow up | Commercial communication (RRR, ACE) | V |
| Work a list of named accounts | ABM, after the readiness check | VI |

Sales to individuals or low-ticket sales use Demand-Side and commercial communication. Challenger and ABM assume several stakeholders and enough account value to justify the effort, so they misfire there.

## How to work

1. **Place the opportunity.** Who the lead is, where they came from, what has been said, and where they are in the decision (first thought, passive looking, active looking, deciding). If the user pasted the conversation, extract this from it before asking anything.
2. **Find the reason for change.** What made the current situation uncomfortable now, what the person hopes to gain, what scares them about switching and which habit holds them. Without a reason, the next step is to discover it, not to present.
3. **Define one next step** proportional to the decision stage: a question, a focused demo, a trial, a proposal. Someone who has not yet recognized the problem does not get a proposal.
4. **Write the artifact** to the standard in section 49 of the playbook (outreach message, discovery guide, demo plan, proposal, deal review).
5. **Disqualify when it applies.** An unimportant problem, weak impact, a customer who cannot implement, or an expectation the operation cannot meet: tell the user and propose deferring or closing politely. A bad-fit sale costs more after it closes than it earns.

## WhatsApp and e-mail conversations

- Answer what the person asked first. Then ask at most one question, the one that defines the next step. A string of questions reads as an interrogation and people stop replying.
- Keep it short and in the tone of the channel and the company (`brand/<company>/identity.md` records how the company sounds). No feature lists.
- Quote only plans and prices of catalog entries with status available, copied from `catalog.md`, alongside what the person wants to solve.
- End with a concrete request that is easy to accept (a time slot, a confirmation).
- If the context folder has the company's own e-mail or message rules, follow them exactly.

## Continuity between conversations

When the company index names a lead register, look for this lead's file before answering and build on it. After the work, offer to record the update: who the lead is, where they came from, what was said and when, the reason for change found so far, objections, the agreed next step and its date. Saving it writes to the company's document library, so show the entry and ask first. For a proposal or a deck, use the `proposals-presentations` skill.

## Objections

Treat an objection as information about anxiety or habit, not as an obstacle to defeat. A price objection usually signals an incomplete diagnosis: return to the problem and its impact before talking about discount (section 26 of the playbook). Do not invent a discount, condition or guarantee the catalog does not record.

## Mistakes this skill prevents

- Presenting before understanding.
- Promising what the context marks as hypothesis, plan or unknown.
- Using a complex sales technique on a simple purchase.
- A follow-up that only chases a reply and brings nothing new.
- Turning neutral research into selling. To learn without selling, use the `market-research` skill.

## Neighbouring skills

`recurring-revenue` covers the recurring-revenue system (lifecycle, metrics, roles, scale). `customer-success` takes over after the sale. `brand-offer` handles positioning and offer.
