What this change does: The seven-line amendment makes the tilde-aware checker an explicit prerequisite for the historical guard commands. It identifies ops commit `79f1235` and requires the reviewed candidate’s explicit path until shipment.

Findings: Critical 0; Important 0; Minor 0.

Prior finding: Resolved at `65862cb0eae2784bea0bbb4e0ba5c9a8304939e2`, in `.worktrees/vdocs-f6fd54/docs/plans/2026-10-09-readme-template.md:23`. The amendment removes the ambiguity that an older vendored checker suffices. The existing guard commands remain usable through the stated substitution.

I checked the correction against frozen cleanup revision `cd8657ed902bfd3feab6e3bdf08ee092a255b469`, the connected rollout commands, and the candidate’s tilde detection. The candidate’s SHA-256 matches both the supplied hash and ops commit `79f1235`. The corrective diff passes `git diff --check`; the task worktree is clean.

Reviewer: `codex/gpt-6.1-sol`, freshly verified through `relay model`.

Verdict: Accept. Ship the corrective documentation change.

Not checked: I did not execute the historical rollout or repeat the controller’s test suites; neither is needed to judge this prerequisite. Checker shipment remains separate. No files changed or processes left running.
