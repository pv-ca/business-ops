---
name: llm-council
description: "Use whenever the user asks to council, pressure-test, stress-test, debate or war-room a business decision, wants several perspectives before deciding, or says they are torn between options with real stakes (e.g. \"council this\", \"run the council on this pricing change\", \"should I hire or automate first? I can't decide\", \"am I crazy to pivot?\"). Five advisors with opposed thinking styles answer independently from the company's saved context, review each other anonymously, and a chairman gives one verdict. Not for factual questions, simple choices or creation tasks; those go to the area's skill."
---

# LLM council

One answer to a hard question shows one line of reasoning, and an agent tends to agree with the way the question was asked. The council answers the same question from five opposed angles, has each answer reviewed without knowing who wrote it, and then gives one verdict that shows where the angles agree and where they do not. The method follows Andrej Karpathy's LLM Council, with thinking styles in place of different models.

## Before you start

Read and follow `../business-context/references/coach-protocol.md` (a path relative to this skill's folder). It explains how to find the context, pick the company and what may be claimed. Context folder configured in the plugin: `${user_config.context_folder}`. When that shows no real path (it is empty, or the placeholder appears unreplaced because this agent has no plugin settings), the protocol says where to look.

`references/prompts.md` has the advisor descriptions and the three prompt templates.

## When a council is worth it

A council costs up to ten extra model runs, so it is for decisions where being wrong is expensive and the answer is uncertain: a price change, a pivot, a hire, a launch, choosing between positioning angles, entering a channel, ending a product.

It is the wrong tool when the question has one right answer, when the task is to write or process something, or when the choice is cheap to reverse. In those cases say so in one line and answer with the area's skill. Do the same when the user only wants agreement: tell them the council will argue against the idea, and ask whether that is what they want.

## The five advisors

| Advisor | Looks for |
| --- | --- |
| Contrarian | What fails, what is missing, the flaw nobody wants to name |
| First principles | What the decision is really trying to solve, and whether the question is the right one |
| Expansionist | The upside being undervalued and what happens if it works better than expected |
| Outsider | What someone with none of the company's background would understand, doubt or miss |
| Executor | Whether it can be done with the people, time and cash available, and what the first week looks like |

They pull against each other on purpose: downside against upside, rethinking against doing, and the outsider checking what the insiders assume.

## How to run it

1. **Frame the question.** Read the company's `context.md`, its `catalog.md` when the decision touches what is sold, and `method-adaptation.md` when it exists. Write a brief that every advisor receives:
   - the decision, stated neutrally, with the options on the table;
   - the facts that bear on it, each with its truth status (confirmed, represented, planned, hypothesis, unknown), and the numbers the context holds;
   - the constraint (cash, capacity, time) and the stage of the business;
   - what is at stake and by when the decision is needed.

   Leave your own opinion out of the brief; a leading brief produces five versions of your answer. If the request is too vague to brief, ask one question and then proceed. Show the brief to the user in two or three lines before convening, so a wrong premise is caught before ten runs are spent on it.

2. **Convene the advisors.** Give each one the brief and its description, using the advisor template. The Outsider gets only the decision and what a customer or a stranger could see, without the internal context, because its value is not knowing what the others know. Each answer is 150 to 300 words, takes its angle fully and does not try to be balanced.

   Run the five as parallel subagents when the agent has them, so no answer is written after reading another. Without subagents, write the five answers one after another, each from the brief alone, and tell the user in the verdict that the answers shared one context and are less independent.

3. **Peer review.** Label the five answers A to E in a shuffled order and remove the advisor names. Give all five to five reviewers with the reviewer template: which answer is strongest, which has the biggest blind spot, and what all five missed. Anonymity matters because a reviewer who knows the author judges the style instead of the argument.

   The user can ask for a quick council, which skips this step. Say in the verdict that the review round was skipped.

4. **Chair the verdict.** You are the chairman. Read the five answers with their names restored and the reviews, then write the verdict below. Before writing:
   - check every factual claim the advisors made against the brief. An advisor's number or market fact that is not in the context is an assumption; label it or drop it. Facts that change quickly need a web search with source and date, as the protocol says;
   - side with the strongest reasoning, even when it is one advisor against four;
   - do not average the answers. A verdict that says "it depends" has failed.

## Output

This structure replaces the protocol's four blocks. Headings are written in the reply language.

```markdown
## Council verdict: <decision in a few words>

### Where the council agrees
Points several advisors reached independently.

### Where the council disagrees
The real disagreements, both sides, and what each side is assuming.

### Blind spots
What only the review round surfaced, and what no advisor could know from the context.

### Recommendation
One answer, with the reasoning and the advisor it draws on most.

### What would change this verdict
The assumption the recommendation rests on, and the fact that would reverse it.

### First step
One action, with a suggested deadline and how to tell it worked. When the recommendation rests on a hypothesis, the first step is the cheapest test of it.
```

Keep the verdict to what fits on one screen. Offer the five answers and the reviews after it instead of pasting them; when the user wants them, or the decision is one they will revisit, save brief, answers, reviews and verdict in the company's `deliverables/YYYY-MM-DD-council-<topic>/` folder and state the path.

The council advises and the user decides. If the user decides something that changes the company's direction, offer to record it in the "Updates" section of `context.md`.

## Mistakes this skill prevents

- Running a council on a question an area skill answers directly.
- A brief that already contains the answer.
- Advisors that hedge, which gives five balanced answers and no tension to learn from.
- Treating an advisor's invented number as a fact in the verdict.
- A verdict that lists considerations and leaves the decision where it started.

## Neighbouring skills

`management-strategy` for setting priorities and choosing a strategy without a council, `finance` for the numbers a decision depends on, `diagnosis` for assessing an area, `material-review` for critique of a text.
