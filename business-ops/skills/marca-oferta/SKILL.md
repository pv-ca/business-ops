---
name: marca-oferta
description: "Defines or reviews the positioning, value proposition, offer and voice of one of the user's own companies, grounded in that company's saved context and delivered as coaching. Use whenever the user asks how to describe what they sell, wants a positioning statement, the main message for a site, deck or video, the design or review of plans, packages, price, guarantee or free trial, a tone-of-voice guide, or wants to know whether a claim or promise can be made."
---

# Marca e oferta (brand and offer)

## Before you start

Read and follow `../contexto-negocio/references/coach-protocol.md` (a path relative to this skill's folder). It explains how to find the context, pick the company, what may be claimed and how to shape the answer. Context folder configured in the plugin: `${user_config.pasta_contexto}`. When that shows no real path (it is empty, or the placeholder appears unreplaced because this agent has no plugin settings), the protocol says where to look. `references/books.md` lists the frameworks.

## How to work

1. **Start from the customer's real alternative.** What they would do if the company did not exist: a spreadsheet, a competitor, hiring someone, putting it off. Often the strongest competitor is the customer's current behaviour. Positioning is defined against that (Dunford).
2. **List what the company has that is different** and, for each item, the value it creates and for whom that value weighs most. Use only differentiators the context confirms.
3. **Write the positioning:** for whom, in which situation, what it solves, instead of what, with what proof. One sentence for internal use, then the customer-facing version.
4. **Build the offer** with the value equation (Hormozi): desired outcome, perceived likelihood of success, time to result, effort required. Improve the offer by moving those four before touching price. A free trial, a trial lesson or a guarantee serves to raise perceived likelihood and lower the anxiety of switching.
5. **Price and packages:** present by the unit the customer understands and tie each package to a usage situation. Prices, plans, discounts and conditions come only from the confirmed context; a proposed price change is delivered as a proposal, with the arithmetic and the risk.
6. **Message** (StoryBrand): the customer is the protagonist and the company is the guide. Problem, simple plan, next step, what changes if it works.
7. **Voice:** three or four traits, each with an "is like this" and an "is not like this", plus sample sentences in the company's main channel.

## The promise test

Before delivering any customer-facing sentence, run each claim through three questions:

1. Does the context mark it as confirmed?
2. Does the operation deliver it today, for the typical customer, without depending on an exception?
3. Is there proof to show if the customer asks?

If any answer is no, rewrite to what is true or cut it. Guaranteed results, superlatives ("the best", "the fastest", "100% secure") and planned features do not pass. A defensible promise sells better over time because it does not turn into expectation debt after the sale.

## Typical deliverables

Positioning statement and document, value proposition per audience, map of alternatives, offer and package table, one-page voice guide, review of a page or deck with every claim classified.

## With other skills

When installed, use these for detailed execution, always with this skill's context and promise test: `marketing-skills:offers` (offer construction), `marketing-skills:pricing` (pricing and packaging), `marketing-skills:product-marketing` (positioning and audience), `marketing-skills:copywriting` (page copy). Inside this plugin, `pesquisa-mercado` validates positioning with customers and `vendas` takes the offer into the conversation.
