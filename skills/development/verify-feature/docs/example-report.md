# Profile form — illustrative verification report

> This is a fictional format example, not execution evidence. The observations
> below demonstrate reporting style. No screenshots, traces, or test logs were
> generated for these fictional cases; real reports must link actual artifacts.

- Verdict: **Acceptance would fail in this example**: input is lost after a failed save; persistence is blocked.
- Run/version/entry: illustrative only, not recorded.
- Scope: frontend integration; `mock` backend.
- Tools: no tools executed for this example.
- Illustrative counts: PASS 1 / FAIL 1 / BLOCKED 1 / NOT RUN 0.

## Requirement coverage

| Requirement | Case | Result | Illustrative observation | Evidence |
| --- | --- | --- | --- | --- |
| AC-1 Failed save retains entered name | VF-01 | FAIL | After a 500 response, the field reverted to its original value | None; format example |
| AC-2 Retry submits once | VF-02 | PASS | One click produced one request with the edited name | None; format example |
| AC-3 Reload preserves saved name | VF-03 | BLOCKED | Mock responses were static; persistence could not be established | None; format example |

## Failure: VF-01

- Expected: after a save error, keep the user's typed name and show the error.
- Illustrative actual result: the error appeared, but the name reset.
- Failure point: form state after the failing response.
- Reason: product behavior mismatch in this fictional scenario.
- Next action: preserve the failure evidence in a real run; fix only if authorized,
  then rerun VF-01 in a new run directory.

## Boundaries

Mock success would not establish real backend persistence. A static mock response
cannot settle AC-3. No actual acceptance conclusion can be drawn from this example.
Start real work from the [report template](../assets/report.md) and
[case template](../assets/case.md).
