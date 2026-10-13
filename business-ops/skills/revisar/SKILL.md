---
name: revisar
description: "Critiques a piece of business material of one of the user's own companies (message, e-mail, proposal, deck, landing page, script, ad, plan) and rewrites its weak passages, checking every customer-facing claim against the company's saved context. Use whenever the user shares a text or a file and asks for a review, feedback, critique or improvement (e.g. \"revisa essa proposta\", \"o que acha deste e-mail?\", \"melhora esse texto\")."
---

# Revisar (material review)

## Before you start

Read and follow `../contexto-negocio/references/coach-protocol.md` (a path relative to this skill's folder). It explains how to find the context, pick the company, what may be claimed and how to shape the answer. Context folder configured in the plugin: `${user_config.pasta_contexto}`. When that shows no real path (it is empty, or the placeholder appears unreplaced because this agent has no plugin settings), the protocol says where to look.

## How to work

The material comes in the user's request, as a file path or pasted text; ask for it if absent.

1. Point out strengths, weaknesses and risks.
2. Rewrite the weak passages and explain each change by the principle behind it.
3. Check every customer-facing claim against the company context and catalog: flag anything stated as fact that they mark as planned, hypothesis or unknown, and anything that guarantees a result.
