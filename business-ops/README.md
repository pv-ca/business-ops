# business-ops

Plugin for business work, for Claude Code and Codex from the same source. It structures the task and teaches while doing it, always from the saved context of the user's own companies.

## How it works

1. The `contexto-negocio` skill keeps a context folder: `business-ops-contexto.md` (profile and index of companies) plus, per company, `contexto.md` (stable facts), `catalogo.md` (plans, prices and features with status), `novidades.md` (changelog), `modelos/` (templates), `processos/` (process library), `social/` (social media strategy, voice and calendar), and a brand folder `marca/<company>/`. In Claude Code, set the folder with `claude plugin configure business-ops@pvca` (option `pasta_contexto`). Codex has no plugin settings, so there, and wherever the option is unset, the folder comes from the project instructions, then from the path written in `~/.config/business-ops/context-folder`, then from the working directory.
2. Every skill reads the context of the company in question before acting and keeps companies separate.
3. Every answer follows the coach protocol in `skills/contexto-negocio/references/coach-protocol.md`: confirmed facts only in customer-facing material, diagnosis before prescription, and the four-block deliverable (what to do, why, common mistake, next step).

The plugin holds no fact about any particular company. Everything specific to a business (context, catalog, brand, processes, how a method applies to it) lives in the user's context folder, so the plugin can be shared as it is.

Instruction files are in English. Replies follow the language the user writes in, unless their saved preferences name another.

## Skills

| Skill | Covers | Method source |
| --- | --- | --- |
| `contexto-negocio` | Onboarding and context upkeep | coach protocol |
| `vendas` | Leads, discovery, demo, proposal, objections, follow-up | commercial sales playbook |
| `vendas-saas` | Recurring-revenue system, metrics, roles, scale readiness, ABM | RevOps and scale playbook |
| `sucesso-cliente` | Onboarding, activation, health, retention, churn, expansion | customer success lifecycle playbook |
| `pesquisa-mercado` | Customer interviews, validation, competitors | customer research playbook |
| `marca-oferta` | Positioning, offer, pricing presentation, voice | books |
| `propostas-apresentacoes` | Proposals, decks, one-pagers and their templates | company templates, catalog and brand |
| `marketing`, `anuncios`, `influencia` | Channels and plan, paid media, creators and partners | books; hand off to `marketing-skills` when installed |
| `social-media` | Organic social media: strategy, pillars, standing calendar, posts, carousels and short-video scripts | platform, format and calendar references, books; `marketing-skills` for depth when installed |
| `video-motion` | Script-to-MP4 motion videos | HyperFrames plugin |
| `processos-documentacao` | Process library: SOPs, checklists, policies, manuals, guides; bottlenecks, delegation | document formats, books |
| `sistemas` | Tools and automation | books |
| `gestao-estrategia`, `financas` | Priorities and plans, numbers for decisions | books |
| `novidade` | Records a product, plan, price or feature change and lists what it affects | catalog and changelog |
| `diagnostico`, `plano-trimestral` | Area diagnosis with 3 priorities; 90-day plan | the area's skill, `gestao-estrategia` |
| `ensinar`, `revisar` | Mini-lesson from the user's own company; critique and rewrite of a material | coach protocol |

## Calling it

Every skill triggers from the request itself and can also be called by name: `/business-ops:<skill>` in Claude Code, `$<skill>` or `/skills` in Codex.

`commands/` holds four Claude Code shortcuts that only route to a skill: `/business-ops:contexto`, `/business-ops:proposta`, `/business-ops:apresentacao`, `/business-ops:processo`. Codex does not load plugin commands, so anything that must work in both agents is written as a skill.

## Keeping it portable

Codex reads this folder as it is, through the same `.claude-plugin/` manifests, so there is no build step and no second copy. Three rules keep it that way:

- Skills name files by paths relative to the skill's folder. `${CLAUDE_PLUGIN_ROOT}` is replaced only by Claude Code and may appear only in `commands/`.
- `${user_config.pasta_contexto}` is replaced only by Claude Code. A skill that shows it must also say what to do when it is not replaced; the lookup order is in section 1 of the coach protocol.
- Frontmatter uses `name` and `description` only, with the trigger wording at the start of the description, because Codex shortens long descriptions.

## Books

Each skill has `references/books.md`. The book knowledge base is still to be added by the owner; the files currently map books to uses and hold short summaries in the plugin's own words, never copied passages. The four playbooks under `references/` are the owner's own syntheses.

## Optional companions

- `hyperframes` plugin (HeyGen, Apache 2.0): required by `video-motion` to render.
- `marketing-skills` plugin: detailed execution for marketing, ads and offers.
