---
name: ads
description: "Paid advertising and direct-response copy for one of the user's own companies, grounded in that company's saved context and delivered as coaching. Use whenever the user wants to create, structure or review ad campaigns on Meta, Google, TikTok, YouTube or LinkedIn, write ad copy or creative briefs, plan creative tests, set a budget, or read campaign results (CPM, CTR, CPC, CPA, ROAS) and decide what to do next."
---

# Ads

## Before you start

Read and follow `../business-context/references/coach-protocol.md` (a path relative to this skill's folder). It explains how to find the context, pick the company, what may be claimed and how to shape the answer. Context folder configured in the plugin: `${user_config.context_folder}`. When that shows no real path (it is empty, or the placeholder appears unreplaced because this agent has no plugin settings), the protocol says where to look. `references/books.md` lists the frameworks.

## How to work

1. **Objective, audience, offer and landing destination come before the creative.** An ad cannot fix an unclear offer or a destination that does not convert; check both first (`brand-offer`).
2. **Check readiness.** Is there a way to measure a lead or sale from the ad? Is there capacity to answer the leads quickly? Paid traffic into a slow reply wastes the budget.
3. **Write variations** of hook, body and call to action. The hook speaks to the customer's situation; the claim is something the context confirms.
4. **Plan tests one variable at a time**, with the minimum budget and period needed to decide, and the decision criterion written before launch (Hopkins).
5. **Read the metrics as a chain:** CPM (cost of attention), CTR (creative fit), CPC, conversion rate on the destination, CPA, and return. Locate the weak link before changing anything.
6. **Verify current platform facts** (formats, policies, minimum budgets, targeting options, benchmarks) on the web and cite source and date. These change often and stale advice costs money.

Spending money is the user's action: deliver the campaign structure, copy and budget recommendation, and let the user publish.

## Typical deliverables

Campaign structure, ad copy variations, creative brief, test plan with budget, results reading with next action.

## Mistakes this skill prevents

- Testing many things at once and learning nothing.
- Judging a campaign before it has enough data.
- Ad claims that the product or service cannot back (also a platform-policy risk).
- Optimizing clicks when the problem is the offer.

## With other skills

When installed: `marketing-skills:ads` (campaign setup and optimization), `marketing-skills:ad-creative` (creative variations), `marketing-skills:cro` (landing page conversion), `marketing-skills:analytics` (tracking). Inside this plugin: `marketing` for channel choice, `motion-video` for video creatives.
