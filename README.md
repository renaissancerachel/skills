# renaissancerachel / skills

My personal Claude skills, out in the open.

These are small, reusable skills I lean on across projects. They run in Claude Code, and each `SKILL.md` can also be uploaded to the Claude apps (web and desktop) under Settings, Capabilities, Skills. This repo is a work in progress and I am building it in public, so expect it to grow.

## Install

```bash
/plugin marketplace add renaissancerachel/skills
/plugin install essentials@renaissancerachel
```

You can also skip the plugin system entirely and just copy any `SKILL.md` folder into `~/.claude/skills/`.

## Status

| Skill | What it does | Status |
| --- | --- | --- |
| simple | Summarize everything in plain terms with just enough context to decide, and spell out what's needed back | Stable |
| checkpoint | Get the session to a clean stopping point before the context window compacts | Stable |

### Coming soon

| Skill | What it does | Status |
| --- | --- | --- |
| workspace-cleanup family | Keep files and memory organized, enforce placement, prune bloat | In progress |
| uxr-synthesis | Turn raw user-research notes into structured findings | In progress |

## Layout

The repo follows the Claude Code marketplace format so it can be installed as a plugin:

- `.claude-plugin/marketplace.json` is the marketplace manifest. It names the marketplace (`renaissancerachel`) and lists the plugins it offers.
- `plugins/` holds each plugin. Right now there is one, `essentials`.
- `plugins/essentials/.claude-plugin/plugin.json` is that plugin's manifest.
- `plugins/essentials/skills/` holds the skills (each in its own folder with a `SKILL.md`).
- `plugins/essentials/commands/` holds the matching slash commands (`/simple`, `/checkpoint`).

A skill and its slash command do the same thing in two forms: the `SKILL.md` is model-invokable and uploadable to the Claude apps, and the command is the `/name` shortcut you type in Claude Code.

## Versioning

When I ship changes, I bump the `version` in both `.claude-plugin/marketplace.json` and `plugins/essentials/.claude-plugin/plugin.json`. To pull updates on your machine, run:

```bash
/plugin marketplace update renaissancerachel
```

That refresh step matters. Without it you can keep running a cached, stale copy and not realize a newer version exists.
