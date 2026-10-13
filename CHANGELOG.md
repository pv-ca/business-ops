# Changelog

The version number lives in `business-ops/.claude-plugin/plugin.json`. Each agent keeps one cached copy of the plugin per version, so every change to the skills raises the number.

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
