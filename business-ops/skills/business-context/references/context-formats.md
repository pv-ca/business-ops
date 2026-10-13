# Context formats

Structure of the files the plugin keeps in the context folder. Other skills find facts by these section names, IDs and status words, so keep them as written here. Section names and keys stay in English; the content follows the language rule in section 7 of the coach protocol. A file may hold more than the sections below when the company needs it.

## Contents

- `business-ops-context.md`
- `<company>/context.md`
- `<company>/catalog.md`
- `<company>/changelog.md`
- `brand/<company>/identity.md`
- Lead record
- Files that grow

## `business-ops-context.md`

One per context folder. Profile of the user and index of companies.

```markdown
# business-ops context

## Person

Name, role in each company, what they decide alone and what depends on others.

## Companies

| Company | Model | Folder here | Document library | Lead register |
| --- | --- | --- | --- | --- |
| Acme | B2B software, monthly subscription | `acme/` | /absolute/path or "none" | /absolute/path or "none" |

## Current situation

Main difficulty today, goal for the next 90 days, what was already tried, tools, budget and time available.

## Level per area

| Area | Level |
| --- | --- |
| Sales | beginner, intermediate or advanced |

## Preferences

Reply language (only when the user stated one), tone, short or detailed, explanation with the plan or not.

## Last update

YYYY-MM-DD and what changed.
```

Write "not informed" where the user gave no answer.

## `<company>/context.md`

The stable picture of one company. Every statement carries a truth status, either as a label at the end of the line or by sitting under a heading that names the status.

```markdown
# Acme context

## Identity

What it is, what it sells, to whom, how it charges. [confirmed]

## Offer

One paragraph on what the customer gets and why it matters. Plans and prices are in `catalog.md`.

## Customer journey and main channel

How a customer arrives, decides and starts, and the channel most of it happens in.

## What must not be promised

## Unknowns that matter

## Legacy

Older brands or products whose terms no longer apply.

## Updates

### YYYY-MM-DD

Newest first. What the user said, in one or two lines.
```

Truth status values: `confirmed`, `represented`, `planned`, `hypothesis`, `unknown`. Their meaning is in section 3 of the coach protocol.

## `<company>/catalog.md`

The living register of what the company sells.

```markdown
# Acme catalog

## Plans

| ID | Plan | Price | Includes | Status | Notes |
| --- | --- | --- | --- | --- | --- |
| `basic-plan` | Basic | 99 per month | up to 10 users | available | what may and may not be said |

## Modules and features

| ID | Name | What it does | Status | Notes |
| --- | --- | --- | --- | --- |
| `free-trial` | Free trial | 14 days, no card | available | |
```

- **ID:** lowercase words joined by hyphens, unique in the file, never reused or renamed once a template references it. Templates name the entries they depend on in their `uses` list (`../../proposals-presentations/references/template-format.md`), and `product-update` finds affected templates by that ID, so a renamed ID silently disconnects them.
- **Status:** `planned`, `in_development`, `pilot`, `available`, `retired`, `unknown`. Only `available` entries appear in customer-facing material, and an entry becomes `available` only when the user says so.
- A retired entry stays in the file with status `retired`, so old documents that quote it can still be understood.
- Write the price with its currency and period exactly as it should be quoted.

## `<company>/changelog.md`

```markdown
# Acme changelog

## YYYY-MM-DD: short title

- What: what changed.
- Changed from: the previous value.
- Status: the entry's status after the change.
- Source: who said it or which document showed it.
- Materials reviewed: templates updated because of it.
```

Newest first. One entry per launch, price change, plan change or status change.

## `brand/<company>/identity.md`

```markdown
# Acme identity

## Colors

Name, hex value and where each is used.

## Type

Families, weights and where each is used.

## Logo

Files in `assets/`, which version goes on which background, minimum size and clear space.

## Voice

How the company sounds in customer-facing material: three or four traits, each with one sentence that fits and one that does not. Words it uses and words it avoids.
```

This file is the source for tone in every customer-facing piece. `<company>/social/voice.md` adds what is specific to social media.

## Lead record

Used when the index names a lead register. One Markdown file per lead in that folder, named in the pattern already used there, or `<lead-name>.md` when the folder is empty. The register holds personal data, so it lives in the company's document library and not in the context folder, and each write needs the user's approval for that write.

```markdown
# Lead name (company, when B2B)

- Source: where the lead came from, and when.
- Stage: first thought, passive looking, active looking, deciding, won, lost or paused.
- Interested in: catalog IDs.
- Reason for change: what made the current situation uncomfortable, as far as known.
- Objections: what holds them back.
- Next step: the agreed action and its date.

## History

### YYYY-MM-DD

Newest first. What was said and by which channel, in two or three lines.
```

Record what the lead said and what was agreed. Do not copy identity documents, payment data or anything the conversation did not need.

## Files that grow

Skills read these files on every request, so each has a ceiling. When a file passes it, move the oldest part to `<company>/archive/`, keep the file's headings, and tell the user what moved. Archived files are read only when a question is about the past.

| File | Keep in the file | Move to |
| --- | --- | --- |
| `context.md`, "Updates" | about twenty entries, none older than a year; fold what still holds into the section it belongs to first | `archive/context-updates-YYYY.md` |
| `changelog.md` | the last two years | `archive/changelog-YYYY.md` |
| `social/calendar.md` | the current quarter and the one before it | `archive/calendar-YYYY-QN.md` |
| Lead record, "History" | everything; a lead that is won, lost or paused for a year can be closed with a one-line summary on top | |

Never archive a catalog entry: mark it `retired`.
