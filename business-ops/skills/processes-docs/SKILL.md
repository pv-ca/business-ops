---
name: processes-docs
description: "Use whenever the user wants to document, standardize, review, audit or improve a process or routine: write or update an SOP, checklist, policy, manual, onboarding or training guide, find or fix a bottleneck, rework or delay, delegate or hand over a task, decide what to automate, or asks which processes exist, which are outdated or who owns them (e.g. \"document this process\", \"write a step-by-step\", \"I need a cancellation policy\", \"organize our documentation\"). Keeps the company's process library in its saved context."
---

# Processes and documentation

## Before you start

Read and follow `../business-context/references/coach-protocol.md` (a path relative to this skill's folder). It explains how to find the context, pick the company, what may be claimed and how to shape the answer. Context folder configured in the plugin: `${user_config.context_folder}`. When that shows no real path (it is empty, or the placeholder appears unreplaced because this agent has no plugin settings), the protocol says where to look.

Then open the company's process library: `processes/README.md` in its folder. It is the index of every process and internal document, with owner, status and last review. `references/document-formats.md` has the format for each kind of document and `references/books.md` the frameworks.

## What this skill is for

A company runs on what its people repeatedly do. When that lives only in someone's head, the work stops when the person is away, new people learn by trial, and every improvement is lost with the next change. This skill turns how the work is done into documents short enough to be used, and keeps them true as the business changes.

A document nobody follows is worse than none, because it looks like control. So the test of everything written here is whether a person doing the task would open it and find it useful.

## The process library

Each company has a `processes/` folder:

```
processes/
  README.md            index: every process and document, owner, status, last review, where the file is
  <area>/<name>.md     one document per process, policy or guide
```

- **Source and final copy.** The Markdown file in `processes/` is the working source: easy to edit, compare and review. When the user approves a version for use by the team, offer to export it (PDF or DOCX) to the matching folder of the company's document library. Writing there needs the user's approval for that write.
- **Statuses:** `draft` (being written), `in review` (waiting for the user or the process owner), `approved` (in use, with the approval date), `outdated` (known not to match practice), `retired`.
- **Existing documents.** The index also lists documents that already exist in the document library and were not written here. Their status is `existing, approval not established` until the user says which version is in force. Before writing something new, check whether such a document exists and build on it; several versions of the same manual is exactly the problem this library solves.
- Only the user moves a document to `approved`. Record who approved and when.

## Documenting a process

1. **Capture it as it happens today,** not as it should. Ask the user to walk through the last real case: what triggered it, each step, who did it, with which tool, how long, where it waited, what went wrong. If a recording transcript, a message thread or an older document shows it, read that first and ask only for what is missing.
2. **Name the essentials** before writing steps: purpose (why the process exists), trigger (what starts it), outcome (what "done" looks like), owner (one person or role accountable), and how often it runs.
3. **Find the constraint** (Goldratt). One step limits the whole flow. Look for where work piles up or waits. Improving any other step changes nothing, so say which step it is.
4. **Remove before improving.** Drop steps that serve neither the customer nor control, then simplify what remains. Record what was removed and why.
5. **Write the document** in the format for its kind (`references/document-formats.md`): SOP, checklist, policy, manual, onboarding or training guide, process map. Write for the person who will do the task on a busy day: imperative steps, one action each, the standard for "done", and what to do when the usual case does not apply.
6. **Mark what is decided and what is proposed.** A step the company already follows is fact. An improvement you suggest is a proposal until the user accepts it; keep the two visibly apart so a draft never reads as policy.
7. **Add it to the index** with owner, status, date and a review date.

## Policies need extra care

A policy (cancellation, rescheduling, refunds, absences, discounts, data handling) is a promise to customers or staff. Write only what the user has decided; where the company context lists a policy as unknown, present options with their consequences and let the user choose instead of filling the gap. Policies that touch labor, consumer, tax or privacy law need a specialist's review; say so in the document's notes and keep it as `in review` until that happens. A policy that customers will read uses the company's tone and only confirmed facts.

## Keeping documentation alive

- **Review dates.** Every approved document has one. When asked what is outdated, or during a review, list documents past their date and those whose process changed.
- **Change triggers.** A new product, plan, price or feature (recorded through the `product-update` skill), a new tool, a new role or a recurring problem all mean some document is now wrong. Find which, using the index, and update it or flag it as `outdated`.
- **Versions.** Change the document in place, add a dated line to its change history, and export a new final copy on approval. Do not keep parallel "v2", "final", "corrigido" files in the library; when you find them among existing documents, ask the user which is in force and record the answer in the index.
- **Audit on request:** which processes exist, which have no owner, which are undocumented though the work happens weekly, which documents contradict each other.

## Improving and delegating

- **Bottleneck analysis:** the constraint, the evidence for it, one recommended change and how to tell it worked.
- **Delegation:** hand over a task with a definition of done, an owner, a check point and the document to follow, not just a task name (Gerber: the business should not depend on one person's memory).
- **Automation comes last.** Automating an unstandardized process fixes its flaws in place. Standardize, run it by hand a few times, then automate the stable part. For choosing or specifying the tool, use the `systems` skill.

## Typical deliverables

Process map, SOP, checklist, policy, operations manual, onboarding or training guide, delegation brief, bottleneck analysis, documentation audit, updated library index.

## Mistakes this skill prevents

- Documenting the ideal process nobody follows.
- A manual so long that nobody opens it.
- Inventing a policy the company never decided.
- Several versions of the same document with no one knowing which is valid.
- Optimizing a step that is not the bottleneck.
- Documentation written once and never reviewed.

## Neighbouring skills

`systems` (tools and automation), `management-strategy` (priorities, roles and meeting rhythm), `customer-success` (the customer-facing side of onboarding and delivery), `sales` (sales scripts and conversations), `proposals-presentations` (documents sent to customers).
