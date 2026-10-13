---
name: diagnosis
description: "Diagnoses one area of one of the user's own companies (sales, marketing, customer success, operations, finance, management) from its saved context and names the 3 priorities. Use whenever the user asks for a diagnosis, an assessment or a health check of an area, or asks where the business is weak or what to fix first (e.g. \"diagnose our sales\", \"what am I getting wrong in marketing?\")."
---

# Diagnosis

## Before you start

Read and follow `../business-context/references/coach-protocol.md` (a path relative to this skill's folder). It explains how to find the context, pick the company, what may be claimed and how to shape the answer. Context folder configured in the plugin: `${user_config.context_folder}`. When that shows no real path (it is empty, or the placeholder appears unreplaced because this agent has no plugin settings), the protocol says where to look.

## How to work

Take the area and the company from the user's request; ask for whichever is missing and cannot be inferred.

1. Read the company context first and answer from it whatever it already answers.
2. Assess the area with at most 8 to 10 questions, asked a few at a time and skipping what the context covers. Use this plugin's skill for that area for the method.
3. Rate each sub-topic from 1 to 5, stating the evidence for the rating. Mark as unknown what could not be established instead of guessing, because a rating without evidence reads as a fact later.
4. Finish with the 3 priorities, each with the reason, the first action and how to tell it worked.
