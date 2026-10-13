---
name: market-research
description: "Plans and analyzes market and customer research for one of the user's own companies, grounded in that company's saved context and delivered as coaching. Use whenever the user wants to interview customers or leads, understand why people buy, stay or cancel, validate an ideal customer profile, segment, offer or price, write an interview script or survey, analyze interview notes, study competitors and alternatives, or size a market, before launching or repositioning."
---

# Market research

## Before you start

Read and follow `../business-context/references/coach-protocol.md` (a path relative to this skill's folder). It explains how to find the context, pick the company, what may be claimed and how to shape the answer. Context folder configured in the plugin: `${user_config.context_folder}`. When that shows no real path (it is empty, or the placeholder appears unreplaced because this agent has no plugin settings), the protocol says where to look. The method lives in `references/customer-research-playbook.md` (interview guides in Part I, analysis in Part II). Read only the part the task needs. `references/books.md` lists the books.

## Research is not selling

Research seeks reliable learning; a sales conversation seeks a decision. Mixing them ruins both: the participant stops being candid and the evidence becomes worthless. In a research interview do not pitch, defend, challenge or negotiate. If the user wants to diagnose a live opportunity, that is the `sales` skill.

## How to work

1. **Start from the decision.** Name the decision the research must inform and what would change depending on the answer (section 3). Research with no decision attached produces interesting notes and no action.
2. **Choose the method** (section 4): interviews for why and how, quantitative data for how many, competitor and public-data analysis for the landscape. For market size and competitor facts, search the web and cite sources with dates.
3. **Choose participants** by behaviour, not demographics (sections 8 and 9): people who recently bought, switched, stayed long, reduced use or cancelled each answer a different question.
4. **Write the guide** from the matching template: problem discovery (14), switching or new customer (15), long-term customer (16), cancellation (17), prioritization (19), willingness to pay (20), feature request (21). Ask about past and current behaviour, not hypothetical preference, and avoid leading questions (sections 12 and 13).
5. **Analyze** (Part II): capture evidence verbatim, debrief each interview, map the journey, plot pain against frequency, look for patterns across participants, and control for bias.
6. **Deliver a decision**, not a transcript summary: patterns, the evidence behind each, what remains uncertain, and the recommended decision with its reversal condition.

When the company context lists an ideal customer, segment or channel as a hypothesis, treat validating it as a research question and say what evidence would confirm or kill it.

## Typical deliverables

Research brief, recruitment message, interview guide, note-taking template, debrief, pain and frequency matrix, findings report with a recommended decision, competitor and alternatives map.

## Mistakes this skill prevents

- Asking "would you use/pay for this?" and treating the answer as evidence.
- Interviewing only happy customers.
- Turning a cancellation interview into a save attempt.
- Reporting opinions of the researcher as findings.

## Neighbouring skills

`brand-offer` uses the findings for positioning, `sales` for discovery in live deals, `customer-success` for churn follow-up. When installed, `marketing-skills:customer-research` and `marketing-skills:competitors` help with online review mining and competitor profiling.
