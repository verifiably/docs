What this change does: Replaces 12 machine-layout findings across three historical documents with portable descriptions and checker invocations. The historical projects, decisions, remaining grep guards, attachments, and review ledgers are preserved.

Reviewer: `codex/gpt-6.1-sol`, verified using a fresh `timeout 2 relay model --harness codex --pretty`.

Reviewed frozen range `2d275db0a356f37803927401dfc0dfdee69724b0` → `cd8657ed902bfd3feab6e3bdf08ee092a255b469`.

**Strengths**

- Changes stay within the three reported documents and the task record. No runtime code, vendored tools, exemptions, attachments, or review ledgers change.
- Reworded evidence retains which projects had home-relative links and which historical conventions were removed.
- The plan retains its stack-name, relative-link, and obsolete-organization grep guards.
- `git diff --check` passes. The candidate checker’s SHA-256 matches the supplied reviewed value.

**Findings: Critical 0; Important 0; Minor 1**

1. **The replacement guard needs an explicit checker prerequisite.**  
   File: `.worktrees/vdocs-f6fd54/docs/plans/2026-10-09-readme-template.md:487`, also the five rollout command blocks.

   The removed grep arm detected home-relative checkout paths. The replacement invokes whichever `tools/ops-check` the member already has; the common setup updates only `ops-docs`. A controlled, read-only probe confirmed that the frozen vendored checker misses a home-relative registered-checkout sample that the removed grep arm detects.

   This leaves a documentation limitation until the stricter checker ships. Severity is Minor because these are historical examples and this task neither executes them nor changes an active gate.

   Recommended clarification: state that the amended layout guards require the tilde-aware checker from `ops-295f8d`, using its reviewed candidate explicitly until shipment. This task need not vendor it or rerun the historical rollout.

**Declined to judge**

- Reexecution of the old rollout and current correctness of its unchanged installation/runtime examples: outside this historical portability cleanup.
- The candidate checker’s overall implementation correctness: separately reviewed upstream; this review verified its supplied hash and examined the replacement guard’s dependency.

**Ready to merge: Yes**, with the minor limitation recorded. The cleanup meets its bounded scope; the proposed historical-plan clarification would resolve the remaining ambiguity.

Not rerun: project suites or old rollout; the controller supplied passing check results, including supplemental sibling-link verification. Residual risk is limited to using the amended historical examples with an older checker.
