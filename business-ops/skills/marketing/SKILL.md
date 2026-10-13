---
name: marketing
description: "Marketing strategy and planning for one of the user's own companies, grounded in that company's saved context and delivered as coaching. Use whenever the user asks how to get more leads or customers, which channels to use, for a marketing plan, content calendar, social media or content ideas, a referral program, a growth experiment, or wants to know why marketing is not bringing results."
---

# Marketing

## Before you start

Read and follow `../contexto-negocio/references/coach-protocol.md` (a path relative to this skill's folder). It explains how to find the context, pick the company, what may be claimed and how to shape the answer. Context folder configured in the plugin: `${user_config.pasta_contexto}`. When that shows no real path (it is empty, or the placeholder appears unreplaced because this agent has no plugin settings), the protocol says where to look. `references/books.md` lists the frameworks.

## How to work

1. **Audience, promise and positioning come before channel.** Read them from the company context; if positioning is weak or unconfirmed, fix that first with `marca-oferta`. A channel amplifies the message it is given.
2. **Find where demand already is.** How current customers found the company, what they were doing before, what they searched or asked. If the context does not say, that is the first thing to learn (`pesquisa-mercado`).
3. **Match the message to awareness** (Schwartz): someone who does not yet see the problem needs a different message from someone comparing options.
4. **Pick one or two main channels** and justify them by audience fit, the company's capacity to sustain them and cost. A small team that spreads across five channels does none well.
5. **Plan by funnel stage**, with one metric per stage and a calendar the team can actually keep.
6. **Run experiments** (Ellis and Brown): hypothesis, test, minimum sample or period, decision criterion written before the test.
7. **Check the numbers that exist.** Budgets, benchmarks and platform rules change; search the web and cite source and date. Do not present an estimated company metric as data.

## Typical deliverables

One-page marketing plan, channel choice with rationale, content calendar, experiment backlog, referral program outline, monthly review template.

## Mistakes this skill prevents

- Choosing a channel because it is fashionable.
- Content about the company instead of the customer's problem.
- Measuring reach when the goal is leads.
- Promising in a post what the context does not confirm.

## With other skills

When installed, hand detailed execution to the specialist, keeping this skill's context and truth-status rule: `marketing-skills:marketing-plan`, `marketing-skills:content-strategy`, `marketing-skills:social`, `marketing-skills:emails`, `marketing-skills:referrals`, `marketing-skills:copywriting`, `marketing-skills:seo-audit`. Inside this plugin: `social-media` for the organic social strategy, calendar and pieces, `anuncios` for paid media, `influencia` for creators and partners, `video-motion` for video.
