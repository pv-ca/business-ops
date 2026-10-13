---
name: contexto-negocio
description: "Creates and maintains the saved context the business-ops plugin works from: the user's profile and one context file per company. Use on first use of the plugin, when `business-ops-contexto.md` is missing, when the user says their company, role, offer, price or goal changed, when they add a new company, or when another skill finds the context outdated or too thin for the task."
---

# Contexto do negócio (business context)

Every other skill in this plugin reads this context before acting, so its quality sets the ceiling for everything else. The protocol all skills follow is `references/coach-protocol.md` in this skill's folder; read it before the first onboarding.

Context folder configured in the plugin: `${user_config.pasta_contexto}`. When that shows no real path (it is empty, or the placeholder appears unreplaced because this agent has no plugin settings), find the folder in the order given in section 1 of the protocol. Confirm the folder with the user before creating files in a directory that holds unrelated work, and when you create the context for the first time, write the folder's absolute path to `~/.config/business-ops/context-folder` so every agent finds it from any directory.

## Layout

```
<context folder>/
  business-ops-contexto.md      profile + index of companies
  <company>/contexto.md          stable facts about that company
  <company>/catalogo.md          plans, prices, modules and features, each with a status
  <company>/novidades.md         dated changelog of launches and changes
  <company>/modelos/             templates for proposals, presentations, messages
  <company>/processos/           process library: SOPs, policies, manuals, with an index
  <company>/adaptacao-dos-metodos.md  how the plugin's general methods apply to this company
  <company>/social/              social media: strategy, voice and the standing calendar
  <company>/entregas/            drafts, one YYYY-MM-DD-topic/ subfolder per request
  marca/<company>/identidade.md  colors, type, logo use, tone
  marca/<company>/arquivos/      local copy of logo and brand files
```

The index also records, per company, the path of its document library (the real archive, often a shared drive) and of its lead register when there is one. Create the catalog, changelog, brand and template files when the company first needs them, not all upfront.

One file per company, because a user may run businesses with different models and audiences, and a single file invites carrying a price or a practice from one to the other.

## When it already exists

Read what is there and change only what the user brought. Add each new fact to that company's file under an "Updates" section with the date, instead of rewriting older sections, so it stays clear what changed and when. Do not create parallel versions.

## Onboarding conversation

Talk in short blocks, not a form. Ask at most three questions at a time, skip what was already answered, and take from any document the user shares before asking.

1. **Person:** name, role and function in each company, what they decide alone and what depends on others.
2. **Companies:** for each one, what it sells, to whom, revenue model, team size, stage (idea, traction, growth, maturity), current channels.
3. **Situation:** main pain today, goal for the next 90 days, what was already tried, tools in use, budget and time available.
4. **Level:** familiarity with each area (sales, marketing, operations, finance, management). This sets the depth of the coaching.
5. **Preferences:** reply language (record it only when the user states one; otherwise replies follow the language they write in), tone, short or detailed format, whether they want the explanation along with the plan.

## What a company file holds

- Identity: what it is, what it sells, to whom, how it charges.
- Current offer and confirmed prices.
- Customer journey and main channel, with the tone used in it.
- **Truth status.** Mark each statement as confirmed, represented (shown in material but not confirmed as available), planned, hypothesis or unknown. This is what lets the other skills write customer-facing material without overpromising.
- What must not be promised.
- Unknowns that matter (metrics, policies, capacity).
- Legacy brands or products whose terms no longer apply.
- Updates, dated.

Plans, prices, modules and features do not go here: they go in `catalogo.md`, because they change more often than the rest and other files reference them by ID. Product changes are recorded through the `novidade` skill.

## Output

Write or update the files, then show a five-line summary and ask for confirmation or correction.

## Rules

- Do not invent data. Write "not informed" for what is missing; a gap is more useful than a guess that later reads as fact.
- Do not ask for or store secrets (passwords, document numbers, card numbers) or customers' personal data.
- Reply to the user in their language; keep the files in the language they already use.
