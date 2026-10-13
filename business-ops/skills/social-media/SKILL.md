---
name: social-media
description: "Plans and writes organic social media for one of the user's own companies: content strategy, pillars, a standing calendar, and ready-to-post pieces (posts, carousels, short-video scripts, captions), grounded in that company's saved context. Use whenever the user asks what to post, wants content ideas, a content calendar or a month of posts, a social media strategy, a caption, a carousel, a Reels, TikTok or Shorts script, wants to repurpose something into posts, or to review what performed on Instagram, LinkedIn, TikTok, YouTube or Facebook (e.g. \"what should I post this week?\", \"build a content calendar\", \"make a carousel about this\", \"our Instagram has gone quiet\")."
---

# Social media

## Before you start

Read and follow `../business-context/references/coach-protocol.md` (a path relative to this skill's folder). It explains how to find the context, pick the company, what may be claimed and how to shape the answer. Context folder configured in the plugin: `${user_config.context_folder}`. When that shows no real path (it is empty, or the placeholder appears unreplaced because this agent has no plugin settings), the protocol says where to look.

A post is customer-facing material. Everything in it follows section 3 of the protocol: prices, plans and features come from catalog entries with status available, and nothing is promised that the context does not confirm.

## What this skill keeps

Social media fails less from a lack of ideas than from stopping: posting falls off the list in a busy week and the profile goes quiet. So the work lives in three files that persist between sessions, in the company's folder under `social/`. Create each one when it is first needed.

| File | Holds |
| --- | --- |
| `social/strategy.md` | Objective, audience, channels, pillars, cadence, metrics. One page. |
| `social/voice.md` | How the company sounds in posts, with real examples. |
| `social/calendar.md` | The standing calendar: what is planned, drafted, approved and published. |

Finished pieces for a period go in `deliverables/YYYY-MM-DD-topic/`, as the protocol says.

## How to work

Find where the request sits and start there. A request for one caption does not need a strategy session; it needs the voice file and the context.

### 1. Strategy (when `social/strategy.md` is missing or the user asks for one)

1. **Objective first.** What should social media do for this business in the next 90 days: bring leads, build trust before a sale, keep current customers, recruit? One primary objective. It decides the content mix and the metric.
2. **Audience and decision.** From the company context: who decides, what they already believe, and what would make them trust this company. Content answers their questions, not the company's wish to talk about itself.
3. **One or two channels.** Choose by where that audience already pays attention and by what the team can keep up. `references/platforms.md` says what each platform rewards and how B2C services and B2B software differ.
4. **Three to five pillars.** Each pillar is a recurring theme tied to the objective, with its share of the calendar. Build them with the matrix in `references/calendar.md`. Keep direct selling to a small share; a feed of offers teaches people to scroll past.
5. **Cadence the team will keep.** Ask who produces, how many hours a week and whether anyone appears on camera. Two posts a week for a year beat a daily month followed by silence.
6. **One metric per objective**, and the review rhythm.

Write the page, show it, and adjust before planning the calendar.

### 2. Voice (before writing any piece)

Read `social/voice.md`, plus the tone section of `brand/<company>/identity.md`. If there is no voice file, build it from real material: ask for five to ten posts or messages the user considers "sounds like us", read them, and record the patterns (sentence length, formality, words used and avoided, how they open, how they close) with two or three short examples. Confirm with the user. Do not guess a personality; a guessed voice produces the generic copy the user came here to avoid, and it is the main reason people reject AI-written posts.

When the user corrects a draft's tone, record the correction in `social/voice.md` so it holds next time.

### 3. Calendar

Read `social/calendar.md` first. Extend it; never rebuild it. Report what is scheduled, what was published, and where the gaps are, then plan forward so the next two to four weeks always exist. Format, status values and the repurposing rules are in `references/calendar.md`.

Each row names the date, channel, format, pillar, the single idea of the piece and its source (a customer question, a catalog entry, a process, a result). A row with no source is a guess; go find one.

**Get the calendar approved before producing the pieces.** A wrong theme is free to fix in a table and costly after ten captions are written.

### 4. Pieces

Write each approved row using `references/formats.md` (hooks, post, carousel, short video, caption, and the list of machine-sounding patterns to avoid). For every piece deliver:

- the text ready to copy, in the company's voice;
- the visual brief: what the image, each slide or each shot shows, in the brand's colors and type;
- the call to action, one per piece;
- hashtags or keywords only where the platform still rewards them (check, see below).

Videos that need animation or rendering go to `motion-video`. Paid distribution goes to `ads`.

### 5. Review (monthly, or when the user brings numbers)

Ask for the platform's own export or screenshots; do not estimate numbers. Compare pieces by pillar and format against the metric of the objective, not by likes. Decide three things: what to repeat, what to stop, and one experiment for next month with its success criterion written before it runs. Record the decisions at the top of `social/strategy.md` with the date.

## What changes quickly

Algorithms, character and duration limits, best posting times, hashtag conventions and feature names change within months. Before stating any of them, search the web and cite the source and its date. The references here hold the method, which lasts; they deliberately leave out the numbers that expire.

## People and permissions

- A customer's or student's name, face, message or result appears only with that person's authorization for that use, and for a minor, the guardian's. Ask the user whether it exists; "they would not mind" is not authorization. Without it, describe the situation without identifying the person.
- Testimonials and results are real and quoted as given. Never write a sample testimonial as if a customer had said it.
- Posting, scheduling, replying to comments or messages on the company's behalf needs the user's go-ahead for that specific action. Deliver drafts ready to post; the user publishes.

## Mistakes this skill prevents

- A month of posts with no objective, measured by likes.
- Content about the company's news when the audience has unanswered questions.
- The same caption pasted on every platform.
- A calendar the team cannot keep, abandoned in week three.
- Copy that sounds generated, which readers notice and skip.
- A price, feature or result in a post that the catalog does not confirm.

## With other skills

`marketing` decides whether social media is the right channel at all and how it fits the funnel. `brand-offer` owns positioning and the promise test. `market-research` supplies the customer questions that become content. `creators-partners` covers creators and partners, `ads` paid media, `motion-video` produced video. When the `marketing-skills` plugin is installed, its `social` and `content-strategy` skills carry more platform detail; use them for execution depth while keeping this skill's files, voice and truth-status rule.

`references/books.md` maps the method to its books.
