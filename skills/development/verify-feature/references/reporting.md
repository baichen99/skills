# Reports and evidence

Use the [report template](../assets/report.md) for full acceptance; shorten it for
a small check. Write in the user's language. Lead with the result and gaps.

Record run ID/time, requirement revision, source/deployed version and dirty state,
entry URL, role, viewport/browser, scope, backend mode, mocked boundaries, and tools
actually used. If a deployed revision is unknown, say so and limit the verdict.

Use PASS, FAIL, BLOCKED, and NOT RUN consistently. Count case execution items for
this run, not retries or accumulated history. Keep component and integration
results distinguishable. Collected but unexamined images do not constitute PASS.

For passing cases, include observed result, comparison/ assertion basis, and
evidence. For failures and blockers, add the failing step, expected versus actual,
reason category, and next action. For processes, link meaningful screenshots or
trace/video timestamps. Include only artifacts that were actually generated.

Archive evidence under the project's stable artifact directory, for example
`verification/<run-id>/`. Keep reports and evidence in the same tree where
practical, with relative links. Copy needed temporary outputs before delivery.
Retain failing runs and retries separately. Existing runner HTML reports can be
linked as attachments; a dashboard or persistent server is unnecessary.

## Link check

```sh
python3 <skill-directory>/scripts/check_report_links.py <report.md>
```

Python 3.9+; standard library only. Checks supported local inline/image links,
full/collapsed reference links, files, ATX heading anchors, and explicit HTML
anchors. Ignores fenced/inline code and does not fetch remote URLs. It is a small
report checker, not a complete CommonMark/GitHub renderer: shortcut references,
Setext headings, directory links, and complex nested markup are outside its scope.
For unsupported syntax use file/browser inspection. A pass only means the
recognized local links resolve, not that a report has sufficient evidence.

Inspect relevant visual evidence and open the report before delivery. Check
external URLs with available tools when access matters; report unavailable access.
Redact credentials, personal data, private API responses, and authentication
state before sharing. Raw traces/HAR/video can contain sensitive information.

State the accepted scope and backend mode in the conclusion. Say full acceptance
passed only when all required cases passed on the target version. List all
blocked/not-run cases and contract assumptions without turning them into success.
