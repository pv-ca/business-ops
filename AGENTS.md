# business-ops

Instructions for an agent or a person changing this repository. The plugin is in `business-ops/`; the repository root is the marketplace it is installed from.

## Rules

- **Nothing from a particular business.** The plugin is used by anyone, so it holds no company, product, customer or person name, no price and no local path. Examples use a placeholder company. What is specific to a business belongs in that user's context folder.
- **English instructions, any reply language.** Skill, reference and command files are written in English, including examples and section names. The language of the reply is set by section 7 of the coach protocol, never by the language of these files.
- **Markdown first, scripts only where exactness matters.** The plugin has no hooks and no MCP servers, because Codex and Claude Code do not share them and nothing here should run without the agent choosing to. A skill may carry a script in `skills/<name>/scripts/` for a step that must give the same result every time (arithmetic, checking a file's structure). Such a script is Python with the standard library only, reads its inputs and prints its result without writing to the user's files or using the network, and holds no formula or rule that is not also written in the skill or its references, so the skill still works where no command can be run. The skill names the script and says what to do without it. Each script has tests in `tests/`. `scripts/` and `tests/` at the repository root are maintenance tools and are not part of the installed plugin.
- **Own words.** The plugin carries methods and insights, never the text of a book. Name the source and do not copy passages.
- **One source for both agents.** Claude Code and Codex install the same folder. Keep the portability rules in `business-ops/README.md`: paths relative to the skill folder, `${CLAUDE_PLUGIN_ROOT}` only in `commands/`, `name` and `description` only in frontmatter, description starting with the trigger wording.
- **The coach protocol is shared.** A rule that applies to every skill goes in `business-ops/skills/business-context/references/coach-protocol.md`, not in each skill.

## Changing a skill

1. Edit the files under `business-ops/skills/<name>/`.
2. When a skill is added, removed or renamed, update the tables in `README.md`, `docs/readme/README_pt-BR.md` and `business-ops/README.md`, and the skill count in the two READMEs.
3. Raise `version` in both `business-ops/.claude-plugin/plugin.json` and `business-ops/.codex-plugin/plugin.json`. Each agent caches the plugin by version, so a change without a new number is not picked up.
4. Add the entry at the top of `CHANGELOG.md`. `python3 scripts/bump_version.py <version> "<line>" "<line>"` does steps 3 and 4 together.
5. Run `python3 scripts/validate.py` and `python3 -m unittest discover tests`. The validator checks frontmatter, relative paths, skill scripts (standard library only, named by their skill), playbook numbering, manifests in sync, the changelog and the README tables; the tests run the skills' scripts. Both run on every push.
6. Tag the commit `v<version>` when it is pushed.

`scripts/forbidden-terms.txt`, when it exists, lists terms the validator must not find inside the plugin, one per line. It is ignored by Git so that each maintainer can list their own company names without publishing them.

## Writing

Explain why a rule exists instead of writing it in capitals. Keep `SKILL.md` under 500 lines and move detail to `references/`, with a table of contents in any reference longer than 300 lines.
