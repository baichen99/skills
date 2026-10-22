# Cases and requirement mapping

Reuse the project's case format and IDs. Otherwise use the [case template](../assets/case.md).
Case definitions hold expectations and bindings; execution results belong to each
run report. Do not maintain competing copies of “latest passing status.”

- Cite a precise requirement item and revision, or quote the user's explicit expectation.
- Use stable case IDs, such as `VF-01 Save failure preserves input`.
- Bind automated cases to an actual file and test title. Include the ID in the title.
- For direct browser/screenshot checks, record the actual entry and performed
  steps instead of inventing a script path.
- One requirement can map to multiple cases or levels; one case can cover multiple
  requirements. Keep the mapping explicit and the execution results separate.
- Inventory every required case for full acceptance. A subset passing does not
  imply full coverage. Retries and repeated runs do not add covered requirements.

Choose cases around an observable goal, such as “save fails, input stays, retry
succeeds.” Assert critical steps individually instead of delegating the entire
feature to one broad AI action. Add edge cases where they could change the result,
not every possible combination by default.

## If TDD is part of the task

Define expected behavior first; write and run one failing case, implement the
smallest change, then rerun. Keep the actual red/green logs and revisions.
Compile errors, missing packages, and bad locators are not evidence of a failing
business assertion. A separate TDD skill is optional.

For already implemented features, execute the current verification directly.
Do not fabricate a prior red run. If fixes are authorized, preserve the observed
failure and subsequent rerun as separate evidence.
