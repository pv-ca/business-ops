---
name: novidade
description: "Records a launch or change in what one of the user's own companies sells (a new product, plan, price, module or feature, or a change to one) in that company's catalog and changelog, then lists the templates and materials that now need updating. Use whenever the user reports that something was launched, repriced, renamed, retired or changed status (e.g. \"lançamos o módulo X\", \"o plano Y subiu para R$ 99\", \"isso já está disponível\"), even if they do not ask to record it."
---

# Novidade (product change)

## Before you start

Read and follow `../contexto-negocio/references/coach-protocol.md` (a path relative to this skill's folder). It explains how to find the context, pick the company, what may be claimed and how to shape the answer. Context folder configured in the plugin: `${user_config.pasta_contexto}`. When that shows no real path (it is empty, or the placeholder appears unreplaced because this agent has no plugin settings), the protocol says where to look.

## Inputs

Take the change from the user's request. Ask for the company if it cannot be inferred, and for whatever is missing among: what it is, who it is for, its status (planned, in development, pilot, available), the date, the price if any, and what may and may not be said to customers. If the user points to a document, read it for the details and treat the user's own statement as the confirmation.

## Steps

1. Update the company's `catalogo.md`: add the entry with a stable ID or change the existing one. Set status to available only when the user says it is being sold now. Keep the old value visible in the changelog, not in the catalog.
2. Add a dated entry at the top of `novidades.md`: what changed, from what to what, status, source.
3. Find what the change affects: templates in `modelos/` whose `uses` list names the entry, the company's message or e-mail rule files, and drafts in `entregas/` that quote it. If the index names a document library, also search it for recent sent proposals or decks that quote the old value. List them; update the templates now and leave sent documents untouched, because they record what was said on their date.
4. If the change contradicts the company's `contexto.md` (for example something listed there as planned is now available), add a dated note in its "Updates" section.
5. Offer, without doing it unasked: a short announcement for customers or leads, written only from the new catalog entry.

## Output

Report what was recorded, what was updated and what still needs the user's decision.
