<p align="center">
  <img src="docs/hero-imagegen.png" alt="Verify Feature: Your AI says done. Ask for evidence." width="100%">
</p>

# Verify Feature

A skill for checking frontend features from a coding agent. It uses Midscene for browser interactions, Bifrost for API mocks, and deterministic assertions for values such as request payloads and submission counts. Results go into a Markdown report with links to screenshots, traces, and logs.

Each requirement maps to a case, a check, a result, and its evidence. A successful build, HTTP 200, or success message alone cannot establish that the whole feature works.

Watch on Bilibili (Chinese): [Landscape](https://www.bilibili.com/video/BV1kLn16HEum/) · [Portrait](https://www.bilibili.com/video/BV1rJn16UE8c/). Both are workflow animations, not recordings of actual toolchain verification.

[简体中文](README.zh-CN.md) · [Setup](references/setup.md) · [Report example](docs/example-report.md)

[![Package checks](https://github.com/baichen99/skills/actions/workflows/verify-feature.yml/badge.svg)](https://github.com/baichen99/skills/actions/workflows/verify-feature.yml)
[![MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

## Install

Run from your project directory:

```sh
npx skills@latest add baichen99/skills --skill verify-feature
```

Select your agent when prompted. The [Skills CLI](https://github.com/vercel-labs/skills) requires Node.js 22.20+ and installs to the current project by default.

This command installs skill instructions, templates, and helper scripts. Browser interactions and API mocks also need Midscene, model access, and Bifrost; see [Setup](#setup) below.

For manual installation, copy the entire `skills/development/verify-feature/` directory from this repository to the appropriate location. Keep its references, scripts, and templates together.

| Agent | Project directory | Invocation |
| --- | --- | --- |
| [Codex](https://learn.chatgpt.com/docs/build-skills) | `.agents/skills/verify-feature/` | `$verify-feature` |
| [Claude Code](https://code.claude.com/docs/en/skills) | `.claude/skills/verify-feature/` | `/verify-feature` |
| [Cursor](https://cursor.com/docs/skills) | `.cursor/skills/verify-feature/` | `/verify-feature` |

Use an empty destination. Restart the agent if the skill does not appear. Other tools that load the [Agent Skills format](https://agentskills.io/specification) can read the same directory.

## Setup

| Tool | Used for |
| --- | --- |
| [Midscene](https://midscenejs.com/) | Browser interactions and visual checks. Requires model access. |
| [Bifrost](https://github.com/bifrost-proxy/bifrost) | API mocks and traffic capture. Requires the CLI and its agent skill. |
| Python 3.9+ (optional) | Checking local links in the report. No Python packages to install. |

The skill checks for missing tools and provides installation instructions. It leaves dependent cases blocked until setup is ready, while independent checks can continue. See the [setup guide](references/setup.md) for commands and model configuration. Model calls may incur costs.

## Usage

Start your app, open Codex in the project, replace the URL, and send this prompt. In Claude Code or Cursor, change the first line to `/verify-feature`:

```text
$verify-feature
Verify the profile form at http://localhost:3000/settings.

- A failed save must keep the entered values and show an error.
- Clicking retry once must send one request.
- After a successful save, reloading must show the new values.

Use Midscene for interactions and Bifrost for the API scenarios.
Keep the existing component and request code running.
Report the results with evidence. Do not modify product code.
```

You can also ask for a single screenshot comparison, a component check, or mock configuration only. A spec, issue, design reference, or clear expectation in your message supplies the acceptance criteria.

The workflow follows your project's framework and test setup. Existing Playwright, Cypress, component tests, and mocks can stay in place. New process checks use Midscene; new proxy mock tasks use Bifrost.

## Workflow

![Frontend verification with Midscene, Bifrost, assertions and evidence](docs/workflow.en.svg)

[Download the interactive diagram](docs/workflow.en.html) and open it locally to switch themes, zoom, or export. The [JSON source](docs/workflow.en.json) is included.

## Reports

A full acceptance report records each requirement, its case ID, the check performed, expected and observed behavior, and links to the generated evidence. Cases use four states:

| State | Meaning |
| --- | --- |
| PASS | The check ran and met the stated expectation. |
| FAIL | An expectation failed or a tool error invalidated the check. |
| BLOCKED | A missing prerequisite prevented execution. |
| NOT RUN | The case was not executed or has not been evaluated. |

Reports also record the application revision, entry URL, environment, and backend mode. Failed runs and retries remain separate. Frontend checks with a mocked backend do not verify the real backend.

See the [report template](assets/report.md), [case template](assets/case.md), and [annotated example](docs/example-report.md). The example is fictional and is labeled as such.

## Development

From this skill's directory:

```sh
python3 -m unittest discover -s tests -v
python3 scripts/check_package.py
```

The tests cover the report-link checker and package references. Installation has been smoke-tested with the Codex target; browser verification across framework and agent versions has not been completed. [Evaluation scenarios](docs/evaluation.md) describe the remaining behavior checks.

For bugs, include the expected behavior, the agent's actual actions, framework and runner versions, and a small redacted reproduction. Review screenshots and traces for private data before attaching them.

[MIT](LICENSE). Diagram assets include the [Archify runtime notice](docs/ARCHIFY-LICENSE.txt). [Visual sources and validation](docs/visuals.md).
