---
name: llm-council
description: "Use whenever the user asks to council, pressure-test, stress-test, debate or war-room a business decision, wants several perspectives before deciding, or says they are torn between options with real stakes (e.g. \"council this\", \"run the council on this pricing change\", \"should I hire or automate first? I can't decide\", \"am I crazy to pivot?\"). Six advisors with opposed thinking styles answer independently from the company's saved context, a reviewer checks them when they conflict on something that matters, and a chairman gives one verdict. Not for factual questions, simple choices or creation tasks; those go to the area's skill."
---

# LLM council

One answer to a hard question shows one line of reasoning, and an agent tends to agree with the way the question was asked. The council answers the same question from six opposed angles, checks the answers against each other when they conflict on something that would change the choice, and ends with one verdict from a chairman who took no side. The method follows Andrej Karpathy's LLM Council, with thinking lenses in place of different models.

## Before you start

Read and follow `../business-context/references/coach-protocol.md` (a path relative to this skill's folder). It explains how to find the context, pick the company and what may be claimed. Context folder configured in the plugin: `${user_config.context_folder}`. When that shows no real path (it is empty, or the placeholder appears unreplaced because this agent has no plugin settings), the protocol says where to look.

`references/prompts.md` has the full description of each member and the prompt templates.

## Choose the smallest path

A full council costs seven or more model runs. Use the lightest of these that covers the request:

| Path | When |
| --- | --- |
| Direct answer | The question has one right answer, the task is to write or process something, or the choice is cheap to reverse. Answer with the area's skill and say in one line why no council was needed |
| Partial consultation | Two or three lenses are enough (for example Contrarian and Executor on a plan that is already chosen). Say which lenses ran and do not call it a council |
| Full council | The user asked for one, or a decision with real alternatives is expensive to get wrong: a price change, a pivot, a hire, a launch, a positioning choice, entering a channel, ending a product |

When the user only wants agreement, tell them the council will argue against the idea and ask whether that is what they want.

## The members

Seven members: six advisors and the Chairman. Each advisor is a thinking lens, not a character to act out.

| Member | Role |
| --- | --- |
| Contrarian | What is wrong, missing, fragile or likely to fail; the question the user is avoiding |
| First principles | What problem is really being solved; goals, mechanisms, constraints and proxy metrics; whether the question is the right one |
| Expansionist | The upside others miss: the larger version, the adjacent opportunity, the underused asset |
| Outsider | What an intelligent person with no inside knowledge would find confusing, doubtful or missing |
| Executor | What can be done with the people, time and cash available, where execution breaks, what can be tested now |
| Hacker | What the system is really made of under its labels; which constraints are real and which are convention; the shortest legitimate path, with its second-order costs |
| Chairman | Takes no lens. Reads the brief, the six opinions and any review, and decides |

The tensions that make the council useful: Contrarian against Expansionist (downside and upside), First principles against Executor (rethinking and doing), Outsider against Hacker (what is seen from outside and how it works inside), Hacker against Contrarian (unconventional leverage and its later risks), Executor against Expansionist (validating and enlarging).

The Hacker looks for lawful, ethical leverage only. It never recommends deception, misuse of access, invasion of privacy, evasion of an obligation or manipulation, and it names what a shortcut costs once others notice it.

## How to run it

You are the principal: you prepare the brief, call the members, and are the only one who reads files, searches or writes. Members receive text and return text.

1. **Write a neutral brief.** Read the company's `context.md`, its `catalog.md` when the decision touches what is sold, and `method-adaptation.md` when it exists. The brief holds:
   - the objective and the concrete question, with the options on the table;
   - the facts that bear on it, each with its source and truth status (confirmed, represented, planned, hypothesis, unknown), and the numbers the context holds;
   - constraints (cash, capacity, time), consequences and the stage of the business;
   - what is unknown;
   - what a finished answer looks like and by when the decision is needed.

   Leave out your own recommendation, earlier conclusions and the conversation history; a leading brief produces six versions of your answer. Ask the user only when a gap would make the assessment useless; otherwise mark the gap as unknown. Show the brief to the user in two or three lines before calling anyone, so a wrong premise is caught before the runs are spent.

2. **Collect six independent opinions.** Give each advisor the same brief and its own description, each in a fresh context. Run as many in parallel as the agent allows and the rest in a second wave; a later wave receives the brief only, never the earlier opinions. The Outsider receives the essential facts and constraints without the internal narrative, because its value is not knowing what the others know.

   Each opinion has a conclusion, the evidence it rests on, its limitations and a next step, normally up to 200 words. Advisors lean into their lens and separate fact from hypothesis; they do not hedge, and they do not manufacture certainty or disagreement for effect.

3. **Decide whether a review is needed.** Read the six opinions and look for a material conflict: incompatible claims about the evidence, an omission or a fragile premise that could change the choice, or a disagreement about risk or feasibility with a concrete consequence. A difference of emphasis that the same facts explain is not one. Agreement is not proof either; check whether the six agree for independent reasons or because they share one premise from the brief.

   - No material conflict: go to the Chairman and note the reason in one line.
   - Material conflict: call one or two reviewers who wrote none of the opinions. The first verifies the conflicting claims against the evidence. A second is called only for a different question, such as a material risk or a specific factual gap. Replace the advisor names with opaque IDs, shuffle the order, and send only the brief and the arguments in question, with no votes and no hint of the answer you expect. IDs hide labels; style may still reveal the author, so do not describe the review as fully blind.

   One review round. Open another check only when a new concrete question appears that could change the decision.

4. **Call the Chairman.** A separate member, in a fresh context, that receives the brief, the six opinions with their names restored and the reviews that were made. It uses no tools and calls no one. It decides from the evidence, keeps the disagreements visible, may side with one advisor against five, and sets a condition where information is missing instead of answering "it depends".

5. **Check and present.** Before showing the verdict, check every number and market fact in it against the brief. What is not there is an assumption: label it, or verify it on the web with source and date as the protocol requires. Then present the verdict in the user's language.

## When something is missing

- **No subagents:** write the opinions yourself, one lens at a time from the brief alone, and say in the verdict that this was a single-context analysis by lenses. Do not call it independent, do not claim a review was made, and do not report consensus between models. Do not reach for another model's API or CLI to make up for it.
- **An advisor did not answer:** give a partial synthesis that names which opinions exist. Do not invent the missing one and do not present the result as a full council. Do not replace a failed call with a clone.
- **No eligible reviewer:** verify the conflicting claim yourself and state the limitation.

## Output

This structure replaces the protocol's four blocks. Headings are written in the reply language.

```markdown
## Council verdict: <decision in a few words>

### Where the council agrees
Points several advisors reached for independent reasons.

### Where the council disagrees
The real conflicts, both sides, and what each side assumes.

### Blind spots
What the review or the tension between lenses surfaced, and what nobody could know from the context. Leave this out when there is none; do not invent one to fill the section.

### Recommendation
One answer, with its reasoning. When it depends on an unknown, state the condition and what follows on each side of it.

### First step
Exactly one action, with a suggested deadline and how to tell it worked. When the recommendation rests on a hypothesis, the first step is the cheapest test of it.

### Limits of this council
Which members ran, whether a review was made or waived and why, and anything that was not independent.
```

Show the verdict only. Do not write a report file or a transcript unless the user asks; when they do, save brief, opinions, reviews and verdict, in that order, in the company's `deliverables/YYYY-MM-DD-council-<topic>/` folder and state the path.

The council advises and the user decides. It evaluates a decision; it does not authorize any action, so everything in section 11 of the protocol still needs the user's go-ahead. If the user decides something that changes the company's direction, offer to record it in the "Updates" section of `context.md`.

## Mistakes this skill prevents

- Running a council on a question an area skill answers directly.
- A brief that already contains the answer.
- Listing six perspectives in one reply and calling it a council.
- A review round run by habit, with nothing material to resolve.
- Treating an advisor's invented number as a fact in the verdict.
- A verdict that averages the opinions and leaves the decision where it started.

## Neighbouring skills

`management-strategy` for setting priorities and choosing a strategy without a council, `finance` for the numbers a decision depends on, `diagnosis` for assessing an area, `material-review` for critique of a text.
