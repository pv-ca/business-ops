# Document formats

Formats for the internal documents this skill writes. Each is a Markdown file in the company's `processos/` folder. Headings and body are in the language the team reads (Brazilian Portuguese unless the context says otherwise); the front matter keys stay in English so tools can read them.

## Front matter (every document)

```yaml
---
title: Atendimento de novo lead no WhatsApp
kind: sop            # sop | checklist | policy | manual | guide | map
area: comercial
owner: "role or person accountable"
status: draft        # draft | in review | approved | outdated | retired
approved: null       # date and who, when approved
review_by: 2027-01-15
sources: ["what this was based on: a walkthrough with the owner on a date, a transcript, an older document"]
---
```

End every document with a short **Histórico de alterações**: date, what changed, who asked.

## SOP (standard operating procedure)

For a task done repeatedly the same way.

1. **Objetivo:** one or two lines on why this exists.
2. **Quando usar:** the trigger, and when not to use it.
3. **Responsável:** who does it, who is accountable.
4. **Antes de começar:** access, tools and information needed.
5. **Passo a passo:** numbered, one action per step, imperative, with the standard for "done" where it is not obvious. Add the tool or screen where it happens.
6. **Exceções:** the cases that break the usual path and who decides each.
7. **Resultado esperado:** how to tell it was done right.
8. **Indicador** (optional): the one number worth watching.

Keep an SOP to what fits on two pages. If it is longer, it is probably two procedures.

## Checklist

For a task where forgetting a step is the risk. Short items to tick, in the order they are done, each verifiable. No explanations inside the list; link to the SOP for those.

## Policy

For a rule the company commits to.

1. **O que esta política define.**
2. **A quem se aplica.**
3. **A regra,** in plain statements, each one decided by the company.
4. **Exceções** and who may grant them.
5. **Como comunicar** to customers or staff, with the wording to use.
6. **Observações:** legal or specialist review needed, open questions.

Write only decided rules. An undecided point is listed under open questions with the options, not written as a rule.

## Manual

For the full picture of an area (for example the operations manual of a service). A manual is a table of contents over SOPs and policies plus the context that connects them: roles, tools, the journey from start to end. Do not copy the SOPs into it; link to them, so there is one place to update.

## Onboarding or training guide

For a new person in a role. Week by week: what to learn, which documents to read, what to practise, who to shadow, and what they should be able to do alone at the end of each stage.

## Process map

For seeing a flow end to end. A table works better than a diagram for most small processes:

| # | Etapa | Quem | Ferramenta | Entrada | Saída | Tempo | Onde espera |
| --- | --- | --- | --- | --- | --- | --- | --- |

Mark the constraint (the step that limits the flow) and note the evidence for it.

## Library index (`processos/README.md`)

| Documento | Tipo | Área | Responsável | Status | Última revisão | Rever até | Arquivo |
| --- | --- | --- | --- | --- | --- | --- | --- |

One row per document, including documents that exist only in the document library. For those, the status is "existing, approval not established" until the user says which version is in force.
