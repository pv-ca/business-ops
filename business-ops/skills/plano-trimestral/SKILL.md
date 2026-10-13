---
name: plano-trimestral
description: "Builds a 90-day plan for one of the user's own companies: 3 to 5 measurable goals, tasks by week, owners, metrics and review rituals, sized to the stage of the business. Use whenever the user asks for a quarterly plan, a 90-day plan, goals for the next quarter or months, or a plan to reach a target by a date (e.g. \"monta o plano do trimestre\", \"quero um plano de 90 dias\")."
---

# Plano trimestral (90-day plan)

## Before you start

Read and follow `../contexto-negocio/references/coach-protocol.md` (a path relative to this skill's folder). It explains how to find the context, pick the company, what may be claimed and how to shape the answer. Context folder configured in the plugin: `${user_config.pasta_contexto}`. When that shows no real path (it is empty, or the placeholder appears unreplaced because this agent has no plugin settings), the protocol says where to look.

## How to work

Take the company from the user's request or the context index; ask if it is ambiguous.

1. Read the context and establish the stage of the business and its main constraint before setting goals. A business still validating its offer gets learning goals, not growth targets.
2. Define 3 to 5 measurable goals, tasks by week, owners, metrics the company can actually observe, and the review rhythm.
3. Say what is deliberately left out of the quarter, so the plan reads as a choice and not a wish list.

Use the `gestao-estrategia` skill for the method.
