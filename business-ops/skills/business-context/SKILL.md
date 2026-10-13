---
name: business-context
description: "Use on first use of the plugin, when `business-ops-context.md` is missing, when the user wants to set up or update their profile or a company's identity, role, stage, audience or goals, when they add a new company, or when another skill finds the context outdated or too thin for the task. Creates and maintains the saved context every other business-ops skill reads. A launch or a change to a product, plan, price or feature goes to `product-update`."
---

# Business context

Every other skill in this plugin reads this context before acting, so its quality sets the ceiling for everything else. The protocol all skills follow is `references/coach-protocol.md` in this skill's folder; read it before the first onboarding.

When another skill sent the user here in the middle of an urgent request, that request comes first (section 1 of the protocol). Run the onboarding after it is answered.

Context folder configured in the plugin: `${user_config.context_folder}`. When that shows no real path (it is empty, or the placeholder appears unreplaced because this agent has no plugin settings), find the folder in the order given in section 1 of the protocol. Confirm the folder with the user before creating files in a directory that holds unrelated work, and when you create the context for the first time, write the folder's absolute path to `~/.config/business-ops/context-folder` so every agent finds it from any directory.

## Layout

```
<context folder>/
  business-ops-context.md         profile and index of companies
  <company>/context.md            identity, positioning, what is confirmed
  <company>/catalog.md            plans, prices and features, each with a status
  <company>/changelog.md          dated record of launches and changes
  <company>/method-adaptation.md  how the general methods apply to this company
  <company>/templates/            templates for proposals, presentations and messages
  <company>/processes/            procedures, policies and manuals, with an index
  <company>/social/               social media strategy, voice and calendar
  <company>/deliverables/         drafts, one folder per request
  <company>/archive/              older entries moved out of the files that grow
  brand/<company>/identity.md     colors, type, logo use and tone
  brand/<company>/assets/         local copy of logo and brand files
```

The index also records, per company, the path of its document library (the real archive, often a shared drive) and of its lead register when there is one. Create the catalog, changelog, brand and template files when the company first needs them, not all upfront.

`references/context-formats.md` has the structure of each of these files and of a lead record. Read it before creating one, so IDs, statuses and section names match what the other skills look for.

The brand folder sits beside the company folders instead of inside them because it holds binary files (logos, fonts, images) that are usually synced or excluded from version control as one unit, and because design tools point at a single brand root.

One file per company, because a user may run businesses with different models and audiences, and a single file invites carrying a price or a practice from one to the other.

## When it already exists

Read what is there and change only what the user brought. Add each new fact at the top of that company's "Updates" section with the date (newest first), instead of rewriting older sections, so it stays clear what changed and when. Do not create parallel versions.

Every skill reads these files on every request, so they have to stay short. When "Updates" passes about twenty entries, or holds entries older than a year, fold what still holds into the section it belongs to, move the folded entries to `<company>/archive/context-updates-YYYY.md`, and tell the user what was merged. The same rule applies to the other files that grow: see `references/context-formats.md`.

## Onboarding conversation

Talk in short blocks, not a form. Ask at most three questions at a time, skip what was already answered, and take from any document the user shares before asking.

1. **Person:** name, role and function in each company, what they decide alone and what depends on others.
2. **Companies:** for each one, what it sells, to whom, revenue model, team size, stage (idea, traction, growth, maturity), current channels.
3. **Situation:** main pain today, goal for the next 90 days, what was already tried, tools in use, budget and time available.
4. **Level:** familiarity with each area (sales, marketing, operations, finance, management). This sets the depth of the coaching.
5. **Preferences:** reply language (record it only when the user states one; otherwise replies follow the language they write in), tone, short or detailed format, whether they want the explanation along with the plan.

## What a company file holds

- Identity: what it is, what it sells, to whom, how it charges.
- The offer in one paragraph: what the customer gets and why it matters to them. No prices or plan details.
- Customer journey and main channel. How the company sounds is recorded in `brand/<company>/identity.md`, and for social media in `social/voice.md`.
- **Truth status.** Mark each statement as confirmed, represented (shown in material but not confirmed as available), planned, hypothesis or unknown. This is what lets the other skills write customer-facing material without overpromising.
- What must not be promised.
- Unknowns that matter (metrics, policies, capacity).
- Legacy brands or products whose terms no longer apply.
- Updates, dated, newest first.

Plans, prices, modules and features do not go here: they go in `catalog.md`, because they change more often than the rest and other files reference them by ID. Product changes are recorded through the `product-update` skill.

## Output

Write or update the files, then show a five-line summary and ask for confirmation or correction.

## Rules

- Do not invent data. Write "not informed" for what is missing; a gap is more useful than a guess that later reads as fact.
- Do not ask for or store secrets (passwords, document numbers, card numbers) or customers' personal data.
- Reply to the user in their language; keep the files in the language they already use.
