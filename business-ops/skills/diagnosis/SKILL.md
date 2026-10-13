---
name: diagnosis
description: "Use whenever the user asks for a diagnosis, an assessment or a health check of one area of a company (sales, marketing, customer success, operations, finance, management), or asks where the business is weak or what to fix first (e.g. \"diagnose our sales\", \"what am I getting wrong in marketing?\"). Rates each sub-topic from 1 to 5 with its evidence and names the 3 priorities, from the company's saved context."
---

# Diagnosis

## Before you start

Read and follow `../business-context/references/coach-protocol.md` (a path relative to this skill's folder). It explains how to find the context, pick the company, what may be claimed and how to shape the answer. Context folder configured in the plugin: `${user_config.context_folder}`. When that shows no real path (it is empty, or the placeholder appears unreplaced because this agent has no plugin settings), the protocol says where to look.

## How to work

Take the area and the company from the user's request; ask for whichever is missing and cannot be inferred.

1. Read the company context first and answer from it whatever it already answers.
2. Assess the area with at most 8 to 10 questions, asked at most three at a time and skipping what the context covers. Take the sub-topics and the method from that area's skill in this plugin: read `../<skill>/SKILL.md` (for example `../sales/SKILL.md`, `../customer-success/SKILL.md`, `../processes-docs/SKILL.md` for operations).
3. Rate each sub-topic from 1 to 5, stating the evidence for the rating. Mark as unknown what could not be established instead of guessing, because a rating without evidence reads as a fact later.

   | Rating | Meaning |
   | --- | --- |
   | 1 | Absent or broken: it does not happen, or it fails when it does |
   | 2 | Improvised: it happens when someone remembers, differently each time |
   | 3 | Defined: there is a known way of doing it, followed unevenly |
   | 4 | Repeatable: done the same way by whoever does it, with a number that is watched |
   | 5 | Improving: measured, reviewed on a rhythm and adjusted from the results |

   Rate against the stage of the business. A company with its first customers is not weak for lacking what only matters at scale; say so instead of giving a low rating.
4. Finish with the 3 priorities, each with the reason, the first action and how to tell it worked.

## Output

A table of sub-topic, rating and evidence, then the unknowns, then the 3 priorities. This replaces the protocol's four blocks.
