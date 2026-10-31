---
name: sales
description: "Use whenever the user wants to answer or approach a lead, prepare or review a sales conversation, discovery call, demo or follow-up, handle a price objection, qualify a lead or revive a stalled deal, in B2B or B2C, including chat and e-mail messages (e.g. \"reply to this lead\", \"write a discovery call script\", \"the customer said it is too expensive\"). Works from the company's saved context. The proposal or deck file belongs to `proposals-presentations`, and a neutral interview with no selling to `market-research`."
---

# Sales

## Before you start

Read and follow `../business-context/references/advisor-protocol.md` (a path relative to this skill's folder). It explains how to find the context, pick the company, what may be claimed and how to shape the answer. Context folder configured in the plugin: `${user_config.context_folder}`. When that shows no real path (it is empty, or the placeholder appears unreplaced because this agent has no plugin settings), the protocol says where to look.

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

A one-to-one message answers a person, not an audience, so it follows the conversation rather than a copy framework. Reason in this order: the person's real situation, what is already known about them, what they just said or asked, the problem or intent behind it, the impact or motivation and the anxiety or barrier when they are known, the decision stage, the smallest natural next step, and only then the message. Marketing frameworks (StoryBrand, awareness levels, the value equation) do not shape a reply; RRR shapes outreach once the situation is understood.

- Answer what the person asked first. When answering is enough, the message is the answer. A short question gets a short reply, not a pitch.
- Then ask at most one question, the one that defines the next step, and none that the conversation already answered. A string of questions reads as an interrogation and people stop replying.
- Keep it short and in the tone of the channel and the company (`brand/<company>/identity.md` records how the company sounds). No feature lists.
- Use what the person actually said, in their words, instead of a benefit they did not mention.
- Quote only plans and prices of catalog entries with status available, copied from `catalog.md`, alongside what the person wants to solve.
- When a next step follows naturally, end with one concrete request that is easy to accept (a time slot, a confirmation). Not every message needs a request; one in every reply reads as pressure.
- Match the commercial intensity to the readiness the person has shown. No urgency the situation does not have: a deadline or a limited offer appears only when the catalog records it.
- If the context folder has the company's own e-mail or message rules, follow them exactly.

**First message from a lead who arrived by chat** (a site button, an ad, a form that opens the chat). The lead usually wrote one line and has not yet said what hurts. Reply in this order: acknowledge the specific thing they asked; ask for the pain and the current volume or process (what they do today, how often, with how many people); mirror it back in their words; then offer a short call or demo with a concrete time slot. Plans and prices wait until after the demo, unless the person asks for them: a price given before the pain is heavy makes the answer "too expensive" and ends a conversation that diagnosis could have kept open. When they do ask, answer plainly from the catalog and return to the problem.

## Demo and follow-up

Small deals are usually lost here, and rarely because of the product: the person who decides was not in the room, the date slipped, or the contact went quiet with nothing new to react to.

**Booking a demo.**
- Ask for a sample of the real material the product will handle (a document, a spreadsheet, a screenshot of today's process), so the demo runs on their case instead of a generic one.
- Ask who else decides and whether they can join the call. A demo the decision maker never sees only postpones the real conversation.
- Confirm on the day with a short reminder that repeats the time and the link.
- After a no-show, reschedule once and leave a way to try the product alone (a sign-up or trial link). A second reschedule is a signal about interest, not a scheduling problem.
- The same day, send a summary: what was shown, what they said matters, the agreed next step and its date. A deal without a dated next step is only waiting.

**Following up.**
- Every touch brings something new: an answer to a doubt they raised, a result, an example close to their case, a relevant change in the product. "Just checking in" brings nothing and trains people to ignore you.
- At most three touches, spaced out. After that, stop chasing.
- The last touch asks for the reason in a form that is easy to answer: say you will not insist and ask whether it was timing, price, a missing feature, another option or something else. The answer is the most useful thing a lost deal gives, so record it in the lead file when there is one.

## Continuity between conversations

When the company index names a lead register, look for this lead's file before answering and build on it. After the work, offer to record the update: who the lead is, where they came from, what was said and when, the reason for change found so far, objections, the agreed next step and its date. Saving it writes to the company's document library, so show the entry and ask first. For a proposal or a deck, use the `proposals-presentations` skill.

## Objections

Treat an objection as information about anxiety or habit, not as an obstacle to defeat. A price objection usually signals an incomplete diagnosis: return to the problem and its impact before talking about discount (section 26 of the playbook). Do not invent a discount, condition or guarantee the catalog does not record. An objection is not a copywriting problem: when the cause is fit, price, product, timing or missing value, better wording only delays the answer, so say what the cause is.

## Mistakes this skill prevents

- Presenting before understanding.
- Promising what the context marks as hypothesis, plan or unknown.
- Using a complex sales technique on a simple purchase.
- A follow-up that only chases a reply and brings nothing new.
- Turning neutral research into selling. To learn without selling, use the `market-research` skill.

## Neighbouring skills

`recurring-revenue` covers the recurring-revenue system (lifecycle, metrics, roles, scale). `customer-success` takes over after the sale. `brand-offer` handles positioning and offer.
