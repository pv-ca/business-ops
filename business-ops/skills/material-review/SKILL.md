---
name: material-review
description: "Use whenever the user shares an existing text or file (message, e-mail, proposal, deck, landing page, script, ad, plan) and asks for a review, feedback, critique or improvement (e.g. \"review this proposal\", \"what do you think of this email?\", \"improve this copy\"). Critiques it, rewrites the weak passages and checks every customer-facing claim against the company's saved context and catalog. Building a new proposal or deck belongs to `proposals-presentations`."
---

# Material review

## Before you start

Read and follow `../business-context/references/coach-protocol.md` (a path relative to this skill's folder). It explains how to find the context, pick the company, what may be claimed and how to shape the answer. Context folder configured in the plugin: `${user_config.context_folder}`. When that shows no real path (it is empty, or the placeholder appears unreplaced because this agent has no plugin settings), the protocol says where to look.

## How to work

The material comes in the user's request, as a file path or pasted text; ask for it if absent.

1. Point out strengths, weaknesses and risks.
2. Check the tone against `brand/<company>/identity.md`, and against `social/voice.md` for social media copy, when those files exist. Material that is correct and sounds like another company still needs rewriting.
3. Rewrite the weak passages and explain each change by the principle behind it.
4. Check every customer-facing claim against `context.md` and `catalog.md`, using the three questions of "The promise test" in `../brand-offer/SKILL.md`. Flag anything stated as fact that they mark as represented, planned, hypothesis or unknown, any plan or price that differs from the catalog or belongs to an entry that is not available, and anything that guarantees a result.

To build a new proposal or deck instead of reviewing one, use the `proposals-presentations` skill.
