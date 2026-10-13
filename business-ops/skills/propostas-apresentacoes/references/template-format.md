# Template format

A template is a Markdown file in the company's `modelos/` folder. It describes a document; it is not the document. The skill reads it, gathers the inputs and builds the real file.

## Front matter

```yaml
---
template: proposta-comercial          # file name without extension
company: acme                         # company folder name
uses: [plano-basico, teste-gratis]    # catalog IDs this template depends on
reference: "Document library: Propostas/Acme — Proposta comercial — 2026-08.pdf"
status: hypothesis                    # optional: the audience or offer is not validated yet
---
```

`uses` is what connects a product change to the documents it affects. Keep it complete: every plan, price or feature the template mentions should be listed.

## Body

1. **Title and purpose:** when this document is the right one, and when it is not.
2. **Inputs needed:** what must be known about the customer before writing.
3. **Blocks table:**

| # | Block | Kind | Content |
| --- | --- | --- | --- |
| 1 | Cover | Variable | Title, customer name, date |
| 2 | Their situation | Variable | What they told us, with their numbers |
| 3 | Recommendation | Catalog | One plan, price and inclusions copied from the catalog |
| 4 | How it works | Fixed | The standard explanation, already reviewed |
| 5 | Next step | Variable | One action, with an owner |

   Kinds: **Fixed** (same wording every time), **Variable** (written for this customer), **Catalog** (copied from the catalog at the time of writing), **Conditional** (included only when something is true, stated in the content column).

4. **Rules:** the claims and wording limits specific to this document.

## Good practice

- One recommendation per proposal.
- Fixed wording is written once, checked against the catalog, then reused.
- A template for an unvalidated segment says so and is built to learn, not to scale.
- Keep the template short enough to read in a minute; detail that only matters to one block goes in that block's content cell.
