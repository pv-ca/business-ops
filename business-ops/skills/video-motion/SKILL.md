---
name: video-motion
description: "Plans and produces motion-graphics videos for one of the user's own companies, from script to rendered MP4, grounded in that company's saved context. Use whenever the user wants a product presentation or demo video, an explainer, an institutional or sales video, a short for social media, an animated piece with AI narration and no one on camera, or motion graphics synced to a recording (e.g. \"quero um vídeo de apresentação do software\", \"faz um vídeo de motion\", \"anima essa explicação\")."
---

# Video motion

## Before you start

Read and follow `../contexto-negocio/references/coach-protocol.md` (a path relative to this skill's folder). It explains how to find the context, pick the company and what may be claimed. Context folder configured in the plugin: `${user_config.pasta_contexto}`. When that shows no real path (it is empty, or the placeholder appears unreplaced because this agent has no plugin settings), the protocol says where to look.

A video is customer-facing material, so every sentence of narration and every on-screen claim passes the protocol's truth-status rule: confirmed facts only, no planned feature shown as available, no guaranteed result. For the message itself, use the `marca-oferta` skill's promise test.

## How the video gets made

The model does not output video. It writes the animation as code (HTML, CSS and GSAP), and a renderer opens that code in a headless browser, captures it frame by frame and encodes an MP4. The renderer here is **HyperFrames** (the `hyperframes` plugin by HeyGen, Apache 2.0). It needs Node 22+, FFmpeg and a Chrome it can drive.

Check the tooling once per machine with `npx hyperframes doctor`. If the `hyperframes` plugin is not installed, tell the user and give the commands:

```
# Claude Code
claude plugin marketplace add heygen-com/hyperframes
claude plugin install hyperframes@hyperframes
# Codex
codex plugin marketplace add heygen-com/hyperframes
codex plugin add hyperframes@hyperframes
```

Route the build through the HyperFrames skills instead of writing compositions from memory, because they carry the current composition format and CLI. The table names them as Claude Code shows them; agents that list skills without the plugin prefix show the part after the colon:

| Video | HyperFrames skill |
| --- | --- |
| Product presentation, demo, launch, site tour | `hyperframes:product-launch-video` |
| Concept or topic explainer with invented visuals | `hyperframes:faceless-explainer` |
| Short animated piece, titles, overlays | `hyperframes:motion-graphics` |
| Anything unclear | `hyperframes:hyperframes` (router) |
| Voice, music, sound effects, captions | `hyperframes:media-use`, `hyperframes:hyperframes-audio` |

For cuts, reframing to another aspect ratio, loudness and subtitles after the render, use the `ffmpeg-skill` skill when available.

## Workflow

The order matters: narration drives timing, and timing drives animation. Animating before the voice exists means redoing the animation.

1. **Brief.** Objective, audience, where it will be shown, duration, aspect ratio. Defaults when the user gives none: 16:9, 1080p, 30 fps, 60 to 90 seconds for a site or a sales e-mail; 9:16 and under 60 seconds for social feeds.
2. **Script.** Write the narration scene by scene. Open on the viewer's problem, not on the company. One idea per scene. About 140 to 160 spoken words per minute in Portuguese. End on one next step.
3. **Voice.** Generate the narration per scene and get word-level timestamps (from the TTS provider, or by transcribing the audio). Ask which voice provider the user has before generating; a paid voice sounds more natural in Brazilian Portuguese than the local fallback. With a recording of the user instead of AI voice, transcribe it with word timings and read a few frames to see what is on screen.
4. **Scene plan.** A table: scene, time range, narration, what appears on screen, on-screen text, motion, transition, assets needed. To show software working, choose per scene between recreating the interface as animation (cleaner, allows zoom and emphasis) and real screen recordings with highlights on top (faithful, needs footage from the user).
5. **Approval gate.** Show the scene plan and wait for the user's approval or corrections. Do not write animation code before this. A weak idea is cheap to fix in a table and expensive to fix after rendering.
6. **Build and render.** Hand the approved plan to the HyperFrames skill for the video type. Preview first, render when the preview is right.
7. **Review and deliver.** Extract a contact sheet of frames and check it against the plan (text readable, nothing clipped, timing matches the voice). Mix voice and optional music, add captions when the destination plays muted. State the output path.

## Motion principles

- Each movement has a job: direct the eye, show cause and effect, or mark a change of subject. Decoration that moves competes with the narration.
- Ease in and out; nothing starts or stops instantly. Stagger related elements by a few frames so the eye can follow.
- Anticipation before a big move and a small settle after it make interface animation feel physical.
- On-screen text is a few words that reinforce the narration, never the full sentence being spoken. Leave it on screen long enough to be read twice.
- Use the company's colors, type and logo from its brand identity file (`marca/<company>/identidade.md` in the context folder, with the logo files beside it). If something is not documented there, ask rather than invent it.

## Where files go

Project files and the rendered video go in the company's deliverables folder, in a `YYYY-MM-DD-topic/` subfolder. Keep the script and the approved scene plan next to the render so a later revision starts from them.

## Mistakes this skill prevents

- Rendering before the scene plan was approved.
- Narration that lists features instead of showing one problem being solved.
- Showing a screen or capability the context does not confirm as available.
- Text too small or too fast for a phone screen.
