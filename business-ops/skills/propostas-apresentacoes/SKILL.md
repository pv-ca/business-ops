---
name: propostas-apresentacoes
description: "Builds commercial proposals, sales presentations, one-pagers and plan sheets for one of the user's own companies from that company's templates, catalog and brand, and maintains those templates. Use whenever the user asks for a proposal, a quote or budget document, a deck or slides for a prospect or a demo, an institutional presentation, a one-page summary to send, a plan or price sheet, or wants to create or update a template for any of these (e.g. \"monta a proposta pra esse cliente\", \"preciso de uma apresentação\", \"cria um modelo de proposta\")."
---

# Propostas e apresentações (proposals and presentations)

## Before you start

Read and follow `../contexto-negocio/references/coach-protocol.md` (a path relative to this skill's folder). It explains how to find the context, pick the company, what may be claimed and how to shape the answer. Context folder configured in the plugin: `${user_config.pasta_contexto}`. When that shows no real path (it is empty, or the placeholder appears unreplaced because this agent has no plugin settings), the protocol says where to look.

Then read, for the company in question: `catalogo.md` (what may be offered, at what price), the brand identity in `marca/<company>/identidade.md` (colors, type, logo files, tone) and the `modelos/` folder with its README.

## Why templates

A proposal assembled from scratch each time drifts: prices get copied from an old file, a claim that was softened last month comes back, the layout changes. A template fixes the structure and the reviewed wording, leaves open only what belongs to this customer, and names the catalog entries it depends on, so a product change shows which templates to revise.

## Producing a document

1. **Pick the template** in the company's `modelos/` that matches the request. If none matches, say so and offer to create one (see below) rather than improvising a one-off.
2. **Gather the variable inputs** the template lists. Take them from what the user pasted, from the lead's record if the company keeps a lead register, and from meeting notes or transcripts in the document library when the user points to them. Ask for what is missing; a diagnosis fact is never invented.
3. **Check fit before writing.** A proposal needs a diagnosed situation and one plan to recommend. If the conversation did not get that far, tell the user what is missing and what to do first (the `vendas` skill covers discovery).
4. **Fill the blocks.** Fixed blocks keep the template wording. Catalog blocks copy price, capacity and inclusions from the catalog today. Variable blocks use the customer's own words and numbers.
5. **Run the claim check** below on the finished text.
6. **Build the file** in the format the template names, matching the look of the most recent reference original in the document library and the brand notes. Use the document skills available in the session for the format (`pptx` for decks, `docx` or `pdf` for proposals and one-pagers). Render and look at the result before presenting it: text that overflows or a missing logo is caught by looking, not by assuming.
7. **Save the draft** in the company's `entregas/YYYY-MM-DD-topic/` folder and show it. When the user approves it as final, offer to save it to the matching folder of the document library with that library's naming pattern, and write only after the user agrees to that write.

## Claim check

Go through every sentence a customer will read:

- Each plan, price, capacity, module and feature exists in the catalog with status available, and matches it. If the catalog says its table awaits the user's confirmation, stop and ask before quoting.
- Nothing planned, in development or unknown is presented as available. An open question from the meeting may appear as an open point, stated honestly with who will answer it.
- No guaranteed result, accuracy rate, processing time, superlative or legal-sufficiency claim unless the catalog explicitly allows the wording.
- Contract terms come from the current contract or the catalog's note on it, not from a legacy contract or an old proposal.
- Nothing from another company of the user appears.
- The customer's situation is described with facts they gave, not with assumptions.

List for the user anything you removed or softened and why, so they can correct the catalog if it is out of date.

## Creating or updating a template

1. Find what the company already sent: look in the document library for the most recent real proposal or deck of that kind and read it. Real documents show the structure and tone that already work, which is better than a generic outline.
2. Write the template as a Markdown file in `modelos/` with front matter `template`, `company`, `uses` (the catalog IDs it depends on), `reference` (the original it was based on) and, for an unvalidated audience, `status: hypothesis`.
3. Describe each block: its order, whether it is fixed, variable or filled from the catalog, and what goes in it. Put fixed customer-facing wording in the customer's language.
4. End with the rules specific to that document.
5. Add it to the `modelos/README.md` table.

`references/template-format.md` shows the format with an annotated example.

## After a catalog change

When the `novidade` skill reports that an entry changed, open each template whose `uses` list names it, update the affected block, and tell the user which already-sent documents in the document library quoted the old value, so they can decide whether to tell those customers.

## Neighbouring skills

`vendas` (the conversation and diagnosis that feed a proposal), `marca-oferta` (positioning and the promise test), `video-motion` (when the presentation should be a video).
