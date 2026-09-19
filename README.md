# renaissancerachel / skills

My personal Claude skills, out in the open.

These are small, reusable skills I lean on across projects. They run in Claude Code, and each `SKILL.md` can also be uploaded to the Claude apps (web and desktop) under Settings, Capabilities, Skills. This repo is a work in progress and I am building it in public, so expect it to grow.

## Install

There are two ways to run these, and which one you use depends on where you run Claude.

**1. Claude Code CLI (terminal).** Use the plugin system:

```bash
/plugin marketplace add renaissancerachel/skills
/plugin install essentials@renaissancerachel
/plugin install ux@renaissancerachel
```

Pull later updates with `/plugin marketplace update renaissancerachel`.

**2. Claude desktop app, or any machine where you want one editable source.** The desktop app loads skills from `~/.claude/skills/` and does not use the plugin system (`/plugin` is a CLI-only feature). So you link each skill folder from a local clone of this repo into `~/.claude/skills/`. See [Run from one source](#run-from-one-source) below. This keeps the repo as the single copy you ever edit.

You can always fall back to copying a `SKILL.md` folder into `~/.claude/skills/` by hand, but a copy drifts out of date. Linking does not.

## Run from one source

The goal: one clone of this repo is the single source of truth, and every machine points its `~/.claude/skills/` entries at that clone. Edit once, and every surface on that machine sees the change. Update with one `git pull`.

**One-time setup per machine:**

1. **Clone the repo to a local path** (not a cloud-synced folder like OneDrive, iCloud, or Dropbox, which can turn the files into placeholders and break the links):

   ```bash
   git clone https://github.com/renaissancerachel/skills.git
   ```

2. **Link each skill folder into `~/.claude/skills/`.** A skill must sit one level down (`~/.claude/skills/<name>/SKILL.md`), so link each skill individually rather than the whole repo.

   macOS / Linux (symlink):
   ```bash
   ln -s /path/to/skills/plugins/essentials/skills/simple     ~/.claude/skills/simple
   ln -s /path/to/skills/plugins/essentials/skills/checkpoint ~/.claude/skills/checkpoint
   ln -s /path/to/skills/plugins/ux/skills/rux                ~/.claude/skills/rux
   ```

   Windows (directory junction, no admin needed), in PowerShell:
   ```powershell
   New-Item -ItemType Junction -Path "$HOME\.claude\skills\simple"     -Target "C:\path\to\skills\plugins\essentials\skills\simple"
   New-Item -ItemType Junction -Path "$HOME\.claude\skills\checkpoint" -Target "C:\path\to\skills\plugins\essentials\skills\checkpoint"
   New-Item -ItemType Junction -Path "$HOME\.claude\skills\rux"        -Target "C:\path\to\skills\plugins\ux\skills\rux"
   ```

3. **Link any slash commands you want** the same way, into `~/.claude/commands/` (each is a single `.md` file):

   macOS / Linux:
   ```bash
   ln -s /path/to/skills/plugins/essentials/commands/simple.md     ~/.claude/commands/simple.md
   ln -s /path/to/skills/plugins/essentials/commands/checkpoint.md ~/.claude/commands/checkpoint.md
   ```

**Updating, any machine:** `git pull` in the clone. The links already point at it, so the update lands everywhere on that machine at once. Nothing to re-copy.

**Note on `~/.claude/skills` vs `~/.claude/commands`:** a skill is model-invokable (Claude reaches for it on its own) and lives in `skills/`. A command is the `/name` shortcut you type and lives in `commands/`. Many skills ship both forms; link whichever you want on a given machine.

## Status

| Skill | What it does | Status |
| --- | --- | --- |
| simple | Summarize everything in plain terms with just enough context to decide, and spell out what's needed back | Stable |
| checkpoint | Get the session to a clean stopping point before the context window compacts | Stable |
| rux | Rapid 30-criterion UX heuristic audit of a site or page | Stable |
| decks family | Build presentations from a real PowerPoint template (router + setup, build, check); design-system-agnostic via a per-project `DECK-SYSTEM.md` | Stable |
| deep-docs family | Author Layer-1 deep docs (concept substrate): a router over writing / reviewing / brainstorm files; author-agnostic via a local `personal.md` | Stable |

### Coming soon

| Skill | What it does | Status |
| --- | --- | --- |
| workspace-cleanup family | Keep files and memory organized, enforce placement, prune bloat | In progress |
| uxr-synthesis | Turn raw user-research notes into structured findings | In progress |

## Layout

The repo follows the Claude Code marketplace format so it can be installed as a plugin:

- `.claude-plugin/marketplace.json` is the marketplace manifest. It names the marketplace (`renaissancerachel`) and lists the plugins it offers.
- `plugins/` holds each plugin (`essentials`, `ux`, `workspace-cleanup`, `decks`, `deep-docs`, with more being added).
- `plugins/<plugin>/.claude-plugin/plugin.json` is that plugin's manifest.
- `plugins/<plugin>/skills/` holds the skills (each in its own folder with a `SKILL.md`).
- `plugins/<plugin>/commands/` holds the matching slash commands.

A skill and its slash command do the same thing in two forms: the `SKILL.md` is model-invokable and uploadable to the Claude apps, and the command is the `/name` shortcut you type in Claude Code.

## Versioning

When I ship changes, I bump the `version` of the affected plugin in both `.claude-plugin/marketplace.json` and that plugin's `plugins/<plugin>/.claude-plugin/plugin.json`. To pull updates on your machine, run:

```bash
/plugin marketplace update renaissancerachel
```

That refresh step matters. Without it you can keep running a cached, stale copy and not realize a newer version exists.
