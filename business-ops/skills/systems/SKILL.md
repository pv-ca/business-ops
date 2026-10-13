---
name: systems
description: "Design and specification of internal systems and tools for one of the user's own companies, grounded in that company's saved context and delivered as coaching. Use whenever the user wants to choose or set up a CRM, a spreadsheet, a no-code tool or an automation, connect tools, write requirements for something to be built, compare buying against building, or organize where business data lives."
---

# Systems

## Before you start

Read and follow `../business-context/references/coach-protocol.md` (a path relative to this skill's folder). It explains how to find the context, pick the company, what may be claimed and how to shape the answer. Context folder configured in the plugin: `${user_config.context_folder}`. When that shows no real path (it is empty, or the placeholder appears unreplaced because this agent has no plugin settings), the protocol says where to look. `references/books.md` lists the frameworks.

## How to work

1. **Start from the process and the people who will use it,** not from the tool. If the process is undefined, define it first (`processes-docs`).
2. **Write the requirements from real use** (Fitzpatrick): what was done the last times, by whom, with which data, what went wrong. Separate what is needed now from what would be nice.
3. **Model the data:** what records exist, their fields, who owns each, and which place is the single source of truth.
4. **Compare options** on the same criteria: spreadsheet, off-the-shelf tool, no-code, custom build. For each: cost now and monthly, time to set up, who maintains it, what happens to the data if the company leaves, risk. Verify current prices and features on the web with source and date.
5. **Prefer the smallest thing that works** (Ries). A spreadsheet used every day beats a CRM nobody opens. Move up when a concrete limit appears.
6. **Plan rollout in steps:** pilot with real data, short training, a date to review.
7. **Personal data:** when the system holds customer or employee data, point out access control, retention and privacy-law implications, and say when a specialist is needed.

## Typical deliverables

Requirements document, data model, option comparison with recommendation, rollout plan, automation spec, spreadsheet or CRM structure.

## Mistakes this skill prevents

- Buying a tool before knowing the process.
- Requirements made of wishes instead of observed use.
- Several places holding the same data.
- An automation nobody knows how to fix.

## Neighbouring skills

`processes-docs` (the process), `recurring-revenue` (pipeline and metrics the system must hold).
