# Frontend integration and API mocking

## Identify backend mode before execution

| Mode | Meaning | Can establish |
| --- | --- | --- |
| `mock` | All relevant backend dependencies simulated | Frontend behavior against stated scenarios |
| `real` | Relevant requests reach the specified test backend | Observed behavior of that frontend/backend combination |
| `mixed` | Some dependencies real, some simulated | Only the explicitly described combination |
| `none` | No backend involved | Local UI/component behavior |

Use the mode requested by the user or documented by the project. If neither
specifies a mode, prefer isolated local mocks for writes and disclose the choice.
Do not silently redirect existing tests to a different environment.

Enter through the real frontend route for integration checks. Record the actual
app entry, role, revision, and any uncertainty about deployed version. A successful
build or deployment command does not prove the browser loaded that revision.
Check UI, outgoing requests, and final state separately.

## Mocking rules

- Use Bifrost for new proxy/API mock tasks. If the CLI or its agent skill is
  missing, give the [installation reminder](setup.md). Read the installed Bifrost
  skill and current CLI help for rule syntax; do not invent commands.
  Preserve existing MSW, runner interception, HAR/fixture, and mock-server tests.
  Label their actual tool and do not apply competing mocks to the same endpoint.
- Obtain contracts from schemas, documented APIs, or authorized test responses.
  If a contract is assumed, label it as an assumption rather than confirmed behavior.
- Match origin/path, method, target IDs, and relevant parameters precisely.
  Preserve raw types. Do not return generic success for every unknown endpoint.
- Intercept mocked write requests **before** they leave the browser/server client.
  Changing a response after a real write does not undo the write.
- Account for requests made by SSR, loaders, server actions, and service workers:
  browser interception may not see them. Use the project's appropriate boundary
  and verify hits. Do not assume a page-level route handler covers server traffic.
- Stateful scenarios need state transitions and a reset between runs. A fixed
  success payload cannot prove persistence after a subsequent read.
- Verify actual mock hits and record which requests remain real. Rules installed
  without matching traffic are “configured; hits not verified.”
- Restore task-created routes, handlers, servers, and local overrides after the
  run as appropriate. Do not alter unrelated rules or global proxy configuration.

For mock-only requests, deliver rules/fixtures plus start/stop/reset instructions
and observed hit status. No automatic UI acceptance or full report is required.

For Bifrost, scope rules and traffic queries to this task. Verify matching requests
and request interception before claiming mock isolation. Do not change global
proxy/CA trust or unrelated rules automatically. Bifrost skill installation alone
does not prove the proxy is running, routed, or matching traffic.

For requested real-backend checks, remove relevant mocks/HAR/response rewriting
and confirm real traffic using request evidence. Use authorized test accounts
and data. If it fails, preserve that result; a mocked rerun is a separate run
with a separate verdict. Mock success never upgrades a failed real-backend check.
