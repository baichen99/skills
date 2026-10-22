# Midscene and Bifrost setup

Both integrations are included in Verify Feature's workflow. Their runtimes are
not bundled. Discover project dependencies and installed skills before suggesting
changes. Give missing-tool installation instructions, then continue independent
checks. Do not automatically run installers or change machine configuration.

## Midscene: browser interaction and visual checks

Reuse the project's installed version, runner, fixture, and model setup. If
missing, direct the user to the [official Playwright integration guide](https://midscenejs.com/integrate-with-playwright).
For a new npm-based Playwright setup, its documented starting point is:

```sh
npm install --save-dev @midscene/web playwright @playwright/test tsx
npx playwright install chromium
```

Use the project's package manager; add only missing dependencies. Model access
must also be configured using [official model configuration](https://midscenejs.com/model-config).
Do not copy private gateways or keys; installing a package does not configure a
model. Report model readiness separately and disclose that model calls may cost
money. Keep credentials in the user's secret configuration.

Reminder example:

> Midscene is not ready for the requested interaction check. Install the missing
> dependencies using the official guide and configure model access. This run can
> still perform independent checks; Midscene-dependent cases remain blocked.

## Bifrost: API mocks and traffic evidence

This refers to [bifrost-proxy/bifrost](https://github.com/bifrost-proxy/bifrost),
the traffic proxy, not another product named Bifrost.

If the CLI is absent, point the user to [official installation](https://bifrost-proxy.github.io/en/getting-started/installation)
or [GitHub Releases](https://github.com/bifrost-proxy/bifrost/releases). Once the
CLI is installed, the documented project-local agent-skill installer is:

```sh
bifrost install-skill --cwd -y
```

See the [official skill installation guide](https://bifrost-proxy.github.io/en/reference/agent-skill)
for agent-specific options. Read the installed general `bifrost` skill before
operating rules or traffic. Remote access is outside this verification setup.

Check CLI availability/version, proxy readiness, intended browser/runner routing,
and a real matched request separately. Installing skill documents does not start
the proxy or authorize system-proxy, certificate, remote-shell, or global changes.
Use task-scoped routing and cleanup under the user's existing permissions.

Reminder example:

> Bifrost or its agent skill is missing. Install the official CLI, then run
> `bifrost install-skill --cwd -y`. API mock execution is blocked until routing
> and rule hits are verified; independent UI checks can continue.
