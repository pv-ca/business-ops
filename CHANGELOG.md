# Changelog

The version number lives in `business-ops/.claude-plugin/plugin.json`. Each agent keeps one cached copy of the plugin per version, so every change to the skills raises the number.

## 0.11.0 (2026-10-13)

- New skill `llm-council`: pressure-tests a costly, uncertain decision. Five advisors with opposed thinking styles answer from a brief built on the company's context, review each other anonymously, and the chairman gives one verdict with what would change it and a first step. It follows Andrej Karpathy's LLM Council method and works without subagents, with the loss of independence stated in the verdict.

## 0.10.0 (2026-10-13)

- Every skill description now starts with its trigger wording and ends by naming the neighbouring skill for look-alike requests. This separates `marketing` from `social-media` and `ads`, `management-strategy` from `quarterly-plan`, `sales` from `proposals-presentations` and `market-research`, and `material-review` from `proposals-presentations`.
- Coach protocol: an urgent request that already carries its facts is answered before the onboarding when no context is saved yet; company selection now lists `method-adaptation.md` and `brand/<company>/identity.md` among the files to read; a skill's own output structure replaces the four blocks.
- Prices live only in `catalog.md`. `business-context` no longer asks for them in `context.md`, and `sales` quotes from available catalog entries.
- Tone is read from `brand/<company>/identity.md`, with `social/voice.md` for social media. `sales`, `customer-success` and `material-review` point there.
- New `business-context/references/context-formats.md`: the structure of the profile, context, catalog, changelog, brand identity and lead record, plus a ceiling and an `archive/` folder for the files that grow. History sections are newest first everywhere.
- `diagnosis` defines each rating from 1 to 5. `material-review` checks tone, applies the promise test and flags represented claims and prices that differ from the catalog.
- The four playbooks have a table of contents. The numbering gaps are closed: customer success sections 44 to 46 are now 43 to 45, and recurring revenue 53 to 55 are now 52 to 54. The sales playbook gained a section on company-specific adaptation (50), so its last two sections are now 51 and 52.
- Leftover Portuguese in `commands/process.md`, `document-formats.md`, `template-format.md` and the `books.md` titles is now English.
- Optional companions (`ffmpeg-skill`, document skills, `humanizer`) are documented, and each skill says what to do without them.
- README: install command in the header includes the marketplace step, the five truth statuses are named, the Codex equivalent of each shortcut is listed, and an example shows the four-block answer.

## 0.9.0 (2026-10-13)

- Files and folders of the context folder are now named in English: `business-ops-context.md`, `context.md`, `catalog.md`, `changelog.md`, `method-adaptation.md`, `templates/`, `processes/`, `deliverables/`, `brand/<company>/identity.md` with `assets/`, and `social/strategy.md`, `voice.md`, `calendar.md`. An existing context folder needs its files renamed to match.

## 0.8.0 (2026-10-13)

- Skills, shortcuts and the plugin option are now named in English, since the plugin is meant for users anywhere. For example `vendas` became `sales`, `financas` became `finance`, and the option `pasta_contexto` became `context_folder`. Reinstall and set the option again after updating.
- Trigger examples in the skill descriptions are in English.
- Added the MIT license.
- The README is in English, with a Brazilian Portuguese version in `docs/readme/`.
- Book references now say what the plugin carries: insights in its own words, never the books' text.

## 0.7.1 (2026-10-13)

- Replies no longer default to Brazilian Portuguese. With no recorded preference, the plugin answers in the language the user writes in.
- Deliverable labels and reference examples moved to English, with the rule to render them in the reply language.

## 0.7.0 (2026-10-13)

- The install catalog is now named `pvca`, so the plugin installs as `business-ops@pvca`.
- First commit in its own repository, with a README and this changelog.

## 0.6.1 (2026-10-13)

- The plugin no longer names any company. Company-specific sections left three playbooks and moved to an `adaptacao-dos-metodos.md` file in each company's context folder.
- The protocol now tells skills to read that file before applying a method.

## 0.6.0 (2026-10-13)

- New `social-media` skill: strategy, voice, standing calendar, pieces and monthly review, with references for platforms, formats and the calendar.

## 0.5.0 (2026-10-13)

- The plugin now works in Codex from the same source.
- Five commands became skills, because Codex does not load plugin commands.
- Skills point to the shared protocol by relative path.
- The context folder can be found without Claude Code's plugin settings: project instructions, then `~/.config/business-ops/context-folder`, then the current directory.

## 0.4.0 (2026-10-13)

- Renamed from `negocio-coach` to `business-ops`.

## 0.3.1 and earlier

- First versions, named `negocio-coach`, for Claude Code only.
