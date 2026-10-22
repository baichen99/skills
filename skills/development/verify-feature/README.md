<p align="center">
  <img src="docs/hero.svg" alt="Verify Feature — Your AI says done. Ask for evidence." width="100%">
</p>

<h1 align="center">Verify Feature</h1>
<p align="center"><strong>Your AI says “done.” Ask for evidence.</strong></p>
<p align="center">A frontend verification skill for coding agents.<br>Midscene for interactions. Bifrost for mocks. Evidence for the verdict.</p>

<p align="center">
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-86efac?style=flat-square" alt="MIT license"></a>
  <a href="https://agentskills.io/specification"><img src="https://img.shields.io/badge/Agent_Skills-open_standard-93c5fd?style=flat-square" alt="Agent Skills format"></a>
  <a href="https://github.com/baichen99/skills/actions/workflows/verify-feature.yml"><img src="https://github.com/baichen99/skills/actions/workflows/verify-feature.yml/badge.svg" alt="Package checks"></a>
</p>

<p align="center">English · <a href="README.zh-CN.md">简体中文</a><br><a href="#install">Install</a> · <a href="#try-it">Try it</a> · <a href="#what-you-get">What you get</a> · <a href="docs/example-report.md">Report example</a></p>

---

## “The build passes” is where verification starts.

The form renders. The request returns 200. The toast says “Saved.”

But did the input survive a failed request? Did retry submit twice?
Does the value survive a reload?

**Verify Feature teaches your coding agent to answer those questions with actual execution and linked evidence.** It connects the requirement to a case, the case to a check, and the check to what really happened.

```text
Requirement  →  Case  →  Execute  →  Inspect  →  Report
                                              ├─ PASS
                                              ├─ FAIL
                                              ├─ BLOCKED
                                              └─ NOT RUN
```

## Install

From your frontend project, use the [Skills CLI](https://github.com/vercel-labs/skills):

```sh
npx skills add baichen99/skills --skill verify-feature
```

Choose your agent when prompted. The CLI currently requires Node.js 22.20+;
installation is project-scoped by default. Review third-party CLI code as you would
any installer. For manual installation, clone or download this repository and copy
the **entire** `skills/development/verify-feature/` folder to one of these locations:

| Agent | Destination relative to your project root | Invoke |
| --- | --- | --- |
| Codex | `.agents/skills/verify-feature/` | `$verify-feature` |
| Claude Code | `.claude/skills/verify-feature/` | `/verify-feature` |
| Cursor | `.cursor/skills/verify-feature/` | `/verify-feature` |

Use an empty destination; do not overwrite an existing skill. Reload/restart your
agent if the skill does not appear. These paths follow the official
[Codex](https://learn.chatgpt.com/docs/build-skills),
[Claude Code](https://code.claude.com/docs/en/skills), and
[Cursor](https://cursor.com/docs/skills) documentation. Other agents can use the
[Agent Skills format](https://agentskills.io/specification) or read [SKILL.md](SKILL.md)
and its linked references directly.

## Set up Midscene and Bifrost

Both are part of the workflow and installed separately:

| Tool | Role | If missing |
| --- | --- | --- |
| [Midscene](https://midscenejs.com/) | Browser interactions and visual/semantic checks | The agent points you to dependency and model setup |
| [Bifrost](https://github.com/bifrost-proxy/bifrost) | API mocking, scoped proxy rules, traffic evidence | The agent points you to CLI and agent-skill installation |

Follow the [setup guide](references/setup.md). The skill checks readiness and
prompts you to install what is missing. It does not silently run installers or
change your machine's proxy settings. Independent checks can continue while
cases requiring a missing tool stay blocked. Existing deterministic tests remain
useful and keep their actual tool labels.

## Try it

Paste a task after invoking the skill. Be specific about the outcome you expect.

**Check one interaction**

```text
Verify the profile form at http://localhost:3000/settings.
When saving fails, keep my input and show an error. Retrying should submit
once and update the page. Use the project's existing test tools and mocks.
Give me the result with evidence.
```

**Compare one screenshot**

```text
Check the checkout page at 390 × 844 against the attached design.
Focus on spacing, button visibility, and overflow. Capture and inspect
the screenshot, then explain each mismatch.
```

**Accept a feature**

```text
Verify the cart against acceptance criteria AC-1 through AC-6 in the issue.
Use the actual application with a mocked backend. Include empty state,
failed update, retry, and reload. Report every required case, including
anything blocked or not run. Do not modify product code.
```

No spec document? A clear expectation in your message is enough for a bounded
check. No browser or runner? You get the missing prerequisite and unexecuted
cases; the agent must not turn a plan into a pass.

## What you get

An inspectable Markdown result, scaled to the task. For full acceptance:

| In the report | Why it matters |
| --- | --- |
| Requirement → case → test mapping | You can see what was covered and what was missed |
| Expected vs. observed behavior | The verdict has an explicit basis |
| Screenshot, trace, video, or log links | Another person can inspect the evidence |
| Revision, environment, backend mode | A pass belongs to a particular run |
| Failed, blocked, and not-run cases | Gaps remain visible |
| Failed run and retry kept separately | A rerun does not erase the failure |

Example excerpt below is **illustrative, not a recorded test run**:

| Requirement | Case | Result | Observation |
| --- | --- | --- | --- |
| Failed save preserves input | VF-01 | FAIL | The typed name disappeared after a 500 response |
| Retry submits once | VF-02 | PASS | One request after one retry click |
| Value survives reload | VF-03 | BLOCKED | Persistent mock state was not available |

See the [annotated report example](docs/example-report.md),
[report template](assets/report.md), and [case template](assets/case.md).
Real reports link actual artifacts; the example invents no screenshots or logs.

## Your stack stays your stack

**React. Vue. Svelte. Angular. Web Components. Plain HTML.**

The workflow discovers your project; it does not prescribe a framework.
Component checks use your real components, providers, router, and styles.
Integration checks enter through your actual application. SSR and server-side
requests are treated at their real boundaries.

| Already using… | The skill's approach |
| --- | --- |
| Playwright / Cypress / WebdriverIO | Reuse runners, fixtures, and assertions |
| Testing Library / Storybook / TestBed | Reuse component setup; use a browser for layout claims |
| MSW / request interception / a mock server | Reuse contracts, state transitions, and reset behavior |
| Midscene | Reuse fixtures/models for new interaction checks; assert exact values separately |
| Bifrost | Use scoped mock rules and verify actual traffic hits |
| A project-specific platform or proxy | Follow documented local conventions; no internal platform is built in |

These are supported workflow choices, **not a claim of tested integration with
every version**. Execution depends on your agent's tools and project environment.

## What makes the verdict useful

- **Expectations come first.** The current implementation cannot define its own passing criteria.
- **Screenshots get inspected.** Capturing an image is a separate step from judging it.
- **Process claims require a process.** A final screenshot cannot prove retry or persistence.
- **Mock boundaries stay explicit.** Frontend success with mocks does not establish backend correctness.
- **Small tasks stay small.** One screenshot does not require a spec rewrite, a test platform migration, or a dashboard.
- **No fictional execution.** Missing prerequisites and unexecuted cases stay visible.

## Requirements and limits

This is an instruction-based skill with references and templates. It does not
bundle a browser, test runner, model API, or backend. Use an agent with repository
access and the execution/inspection tools needed for your task. Midscene requires configured model access, which may incur model costs. Bifrost
requires its CLI and agent skill. See the [setup guide](references/setup.md);
credentials are configured by the user and never bundled.

The included report-link checker uses Python 3.9+ and the standard library:

```sh
python3 <skill-directory>/scripts/check_report_links.py path/to/report.md
```

It checks supported local links and Markdown anchors. It does not validate test
results or remote access; parser limits are documented in [reporting guidance](references/reporting.md).
If Python is unavailable, the agent can inspect links with its available tools.

The skill asks agents to preserve evidence and report honestly; **it cannot
guarantee agent compliance, detect every bug, or certify release readiness**.
Use normal engineering review. Review traces, screenshots, and payloads for
private data before sharing them. Verification does not itself authorize
production writes or deployment.

## Contribute

Bring a real verification failure: the expected behavior, what the agent actually
did, its runner/framework, and a minimal redacted reproduction. An issue showing
a missed case is more useful than another generic checklist.

To check this package locally:

```sh
python3 -m unittest discover -s tests -v
python3 scripts/check_package.py
```

These check the helper and package integrity; they are not cross-agent or
cross-framework acceptance tests. See [evaluation scenarios](docs/evaluation.md)
for behavior checks that still require actual agent runs.

Licensed under [MIT](LICENSE). If the workflow catches a bug your agent called
“done,” share a redacted example in an issue.
