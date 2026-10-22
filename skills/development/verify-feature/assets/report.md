# <Feature> — verification report

- Verdict: <result within the agreed scope; failures and gaps first>
- Run: <ID, time, requirement revision, source revision and dirty state>
- Entry: <actual URL, app/deployed revision, role, browser and viewport>
- Scope: <component / integration; backend mode and mocked boundaries>
- Tools: <tools actually used>
- Counts: <PASS / FAIL / BLOCKED / NOT RUN for this run; distinguish scopes>

## Requirement coverage

| Requirement and revision | Case | Test / check | Scope / method | Result | Observed result and evidence |
| --- | --- | --- | --- | --- | --- |
| <precise source and expectation> | <stable ID and name> | <actual test file/title or browser steps> | <level; method> | <actual state> | <observation; relative evidence links> |

## Failures and blockers

### <Case ID> <name>

- Preconditions: <actual data, backend mode, and environment>
- Expected: <source-backed outcome>
- Observed: <failing step and actual result>
- Reason: <product mismatch / tool error / missing prerequisite>
- Evidence: <real screenshot, trace, video timestamp, or log links>
- Next action: <smallest needed action within scope>

## Passing evidence

<Omit when the table is sufficient. For complex processes add critical actions,
expected/actual results, and existing evidence links.>

## Retries and TDD

<Link actual failed/retry runs and revisions if present. TDD: actual red/green
records, not recorded, or not applicable. Do not fabricate past execution.>

## Boundaries and unverified cases

<Blocked/not-run cases, assumed contracts, injected component environment,
backend limits, unverified app revision, missing visual judgment, or artifacts.>
