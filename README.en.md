# Skills

Agent Skills for frontend verification and technical writing. Each skill has its own directory with instructions, references, and any required scripts.

[简体中文](README.md)

## Verify Feature

[![Verify Feature: Your AI says done. Ask for evidence.](skills/development/verify-feature/docs/hero-imagegen.png)](skills/development/verify-feature/README.md)

Ask your coding agent to check a frontend feature against its requirements and show the evidence: requirement → case → check → result and evidence. Midscene handles browser interactions; [Bifrost](https://github.com/bifrost-proxy/bifrost) provides API mocks. Results and links to screenshots, traces, and logs go into a Markdown report.

```sh
npx skills@latest add baichen99/skills --skill verify-feature
```

The command installs the skill. Browser interactions and API mocks also need Midscene model access and Bifrost; follow the [setup guide](skills/development/verify-feature/references/setup.md). Missing tools produce installation instructions, and checks that could not run stay visible.

Start your app, open Codex in the project, replace the URL, and send this prompt. In Claude Code or Cursor, change the first line to `/verify-feature`:

```text
$verify-feature
Verify the profile form at http://localhost:3000/settings.
A failed save must preserve input. One retry click
must send one request. After success, reloading must show the new values.
Use a mocked backend. Report the results with evidence. Do not modify product code.
```

[Documentation](skills/development/verify-feature/README.md) · [Setup](skills/development/verify-feature/references/setup.md) · [Report example](skills/development/verify-feature/docs/example-report.md)

## Install

Use the [Skills CLI](https://github.com/vercel-labs/skills) to select skills and agents:

```sh
npx skills@latest add baichen99/skills
```

For manual installation, copy the entire skill directory to your agent's skills location. Keep its references and scripts together.

## Skills

| Skill | Category | Use |
| --- | --- | --- |
| [verify-feature](skills/development/verify-feature/README.md) | Development | Frontend screenshots, components, API mocks, and acceptance checks. |
| [plainspoken-tech-talk](skills/productivity/plainspoken-tech-talk/SKILL.md) | Productivity | Chinese technical talks, articles, retrospectives, and narration based on supplied material. |

## Maintenance

Skills live under `skills/<category>/<name>/`, with `SKILL.md` as the entry point. The directory layout follows [mattpocock/skills](https://github.com/mattpocock/skills). This repository distributes ordinary skill directories; it has no plugin marketplace or automatic update configuration.

Verify Feature has automated helper and package checks. Browser acceptance across framework and agent versions is still pending. Mocked frontend checks do not establish real backend behavior. Writing skills also depend on source material and must not invent experience or results.
