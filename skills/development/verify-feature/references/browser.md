# Browser checks

## Choose by the claim

| Claim | Adequate method |
| --- | --- |
| A specified visible state matches a reference | Prepare state, screenshot, inspect concrete comparison points |
| A control changes another visible state | Interact, wait for the expected condition, assert the result |
| Submission, retry, refresh, or re-entry works | Execute the sequence; inspect requests and final state |
| An exact ID, amount, payload, or count is correct | Deterministic DOM/network assertion at the relevant step |

Use the installed runner, fixtures, and APIs. Discover routes, accessible names,
selectors, and commands from real code or the live page. Prefer accessible roles
and stable test IDs where the project supports them. Do not guess selectors and
report an unexecuted script as successful.

For visual comparisons, record the reference version, viewport, device scale,
theme, locale, and relevant state. Stabilize animations/fonts/data when needed.
A screenshot can support a narrow visual judgment; it does not establish all
responsive sizes, keyboard behavior, screen-reader access, or pixel equivalence.
For accessibility requirements use relevant keyboard/semantic checks or the
project's accessibility tooling and report the exact coverage.

## Example: failed save, then retry

1. Seed a known record and identify its initial values.
2. Open the actual form and change a field.
3. Arrange a failing response; register request capture before clicking Save.
4. Assert the request payload, error message, and retained input.
5. Arrange success, retry once, and assert request count and updated UI.
6. Reload and read the record again if persistence is part of the requirement.
7. Preserve screenshots at the failure and successful result, plus available trace/logs.

Use observable waits; avoid fixed sleeps. Preserve the failure before investigating
or retrying. If navigation, authentication, or a locator fails, report the actual
step reached and distinguish that failure from the feature's business behavior.

## Midscene process checks

Use Midscene for new process checks; reuse the project's fixture and model
configuration. If missing, give the [installation reminder](setup.md) and mark
dependent checks blocked. Existing deterministic tests can still run and must
be labeled as such; they do not establish Midscene execution.
Check installed types or [official docs](https://midscenejs.com/)
for the exact API. Use bounded actions, explicit waits, and separate result
assertions; exact requests and values still need deterministic checks.
Record actual model/tool usage. Model unavailability does not invalidate a
separately executed deterministic check, and a runner pass does not prove
that visual AI judgment occurred. Never copy private model gateways or keys.
