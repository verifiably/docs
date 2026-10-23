---
id: vdocs-9ca77b
title: Pilot one guided tour of a verifiably repository and record which checks helped
status: doing
priority: 2
size: s
complexity: mid
process: direct
owner: main
created: 2026-10-14T15:10:17Z
updated: 2026-10-23T18:50:55Z
started: 2026-10-14T15:40:43Z
depends: []
parent: vdocs-d2d5ed
tags: [docs]
source: docs/notes/2026-10-14-guided-tours-brief.md
agent: claude-code/claude-opus-5-5
---

Question: Does a live, agent-led tour down the scale ladder (ecosystem, layer, repository, subsystem, authority design, code), with an understanding check at each scale, leave the user able to explain one repository and say which repository owns which behaviour? Which kind of check helped most (explaining it back, predicting behaviour, choosing between options, quiz)?
Where to start: alternative A and the scale ladder in docs/notes/2026-10-14-guided-tours-brief.md (§2, §4); overview.md, README.md, and the chosen member's identity.toml, README.md and authority documents. Ask the user which repository to tour (and whether to reach past verifiably into the shared tooling) before starting.
Bound: One session, with the user present, over one repository; nothing is committed except the result in the brief. No skill, no written tours, no tooling.
Expected result: Record on this task and in the brief (§5 and §6) which checks helped and which did not, where the distillation should land, and a recommendation: a skill, written tours, or stop.
Ideas it wakes: On completion, run `tasks note vdocs-c96d1b --no-reviewed "<finding>"` before this result's branch merges.

## Notes

- 2026-10-14T15:40:43Z (main): started
  provenance: {"harness_session":"claude-code:a1b536c8-7e64-40a9-97ca-bb33b760dfc6","harness_session_source":"CLAUDE_CODE_SESSION_ID"}
- 2026-10-14T15:40:43Z (main): tour repository: beliefs (user's choice); verifiably only, no shared tooling
- 2026-10-14T15:41:14Z (main): parked (waiting on user): user answers tour check 1 (explain-back: why verification is not evidence; effect of a new paper on the PHF19 belief) and rates it; then agent gives feedback and runs stop 2 (layers, ownership check), stops 3-5, and records the findings in the brief in a .worktrees/ worktree
  provenance: {"harness_session":"claude-code:a1b536c8-7e64-40a9-97ca-bb33b760dfc6","harness_session_source":"CLAUDE_CODE_SESSION_ID"}
- 2026-10-14T19:14:36Z (main): resumed
  provenance: {"harness_session":"claude-code:a1b536c8-7e64-40a9-97ca-bb33b760dfc6","harness_session_source":"CLAUDE_CODE_SESSION_ID"}
- 2026-10-14T19:14:37Z (main): check 1 (ecosystem, explain-back): user rated helped; answers right in substance, missed that verification is a gate on the assessment rather than independence, and that a paper can still steer what is analysed
- 2026-10-14T19:16:08Z (main): finding: preparing stop 2 surfaced overview drift — layer-state column (2026-09-26) says autonomy 'Designed, not started'; autonomy README says the envelope's first half is built
- 2026-10-14T19:16:08Z (main): parked (waiting on user): user answers tour check 2 (layer ownership A-F) and rates it; then agent gives feedback and runs stops 3-5, then records findings in the brief in a .worktrees/ worktree
  provenance: {"harness_session":"claude-code:a1b536c8-7e64-40a9-97ca-bb33b760dfc6","harness_session_source":"CLAUDE_CODE_SESSION_ID"}
- 2026-10-22T22:31:26Z (main): resumed
  provenance: {"harness_session":"claude-code:1c0c67d0-b42a-41c8-b844-5ee4b3df93e9","harness_session_source":"CLAUDE_CODE_SESSION_ID"}
- 2026-10-22T22:31:56Z (main): finding: overview drift grew by 2026-10-22 — autonomy README now lists tiers, closing check, sandbox and autonomy run's launch side as built; overview still says 'Designed, not started'
- 2026-10-22T22:31:57Z (main): parked (waiting on user, review): user answers tour check 2 (layer ownership A-F, re-posed 2026-10-22) and rates it; then agent gives feedback, runs stops 3-5, and records findings in the brief in a .worktrees/ worktree
  provenance: {"harness_session":"claude-code:1c0c67d0-b42a-41c8-b844-5ee4b3df93e9","harness_session_source":"CLAUDE_CODE_SESSION_ID"}
- 2026-10-23T16:54:10Z (main): resumed
  provenance: {"harness_session":"claude-code:1c0c67d0-b42a-41c8-b844-5ee4b3df93e9","harness_session_source":"CLAUDE_CODE_SESSION_ID"}
- 2026-10-23T16:54:10Z (main): check 2 (layer ownership A-F, choose-between): user rated a little helpful; 5/6 right, D (verification refusing belief) answered atoms, owner is beliefs; user: shuffle the items rather than presenting them in stack order, which gives the answers away
- 2026-10-23T16:54:40Z (main): finding: beliefs docs/guide/README.md (updated 2026-09-26) also says 'The autonomy layer is not started'; same drift as the overview, in a member guide
- 2026-10-23T16:54:41Z (main): parked (waiting on user, review): user answers stop 3 check (predict P1-P4 on beliefs: claim identity, independence count, retraction, no evidence) and rates it; then agent gives feedback, runs stops 4 (subsystems) and 5 (authority design and code), and records findings in the brief in a .worktrees/ worktree
  provenance: {"harness_session":"claude-code:1c0c67d0-b42a-41c8-b844-5ee4b3df93e9","harness_session_source":"CLAUDE_CODE_SESSION_ID"}
- 2026-10-23T17:03:09Z (main): resumed
  provenance: {"harness_session":"claude-code:1c0c67d0-b42a-41c8-b844-5ee4b3df93e9","harness_session_source":"CLAUDE_CODE_SESSION_ID"}
- 2026-10-23T17:03:28Z (main): check 3 (repository, predict P1-P4): user rated useful; P1, P2 right; P3 belief right but said the record is updated (it is a separate retraction record; records are immutable); P4 said 0 (it is 'no evidence', never zero), reason right. User: mm30 is a meta-analysis aggregating many datasets, a poor example for single-dataset independence; the kernel handles it through pairwise dataset-lineage closures
- 2026-10-23T17:03:29Z (main): finding: beliefs subsystem READMEs are stale: python/README.md is headed 'science — Python' and its 'What is here' table lists one module of ~60; ts/README.md says 'Science is Python-primary'. Bears on vdocs-946c49, whose subsystem abstracts draw on these files
- 2026-10-23T17:03:30Z (main): parked (waiting on user, review): user answers stop 4 check (which tree a change lands in, W-Z) and rates it; then agent gives feedback, runs stop 5 (authority design and code), and records findings in the brief in a .worktrees/ worktree
  provenance: {"harness_session":"claude-code:1c0c67d0-b42a-41c8-b844-5ee4b3df93e9","harness_session_source":"CLAUDE_CODE_SESSION_ID"}
- 2026-10-23T18:01:15Z (main): resumed
  provenance: {"harness_session":"claude-code:1c0c67d0-b42a-41c8-b844-5ee4b3df93e9","harness_session_source":"CLAUDE_CODE_SESSION_ID"}
- 2026-10-23T18:01:51Z (main): check 4 (subsystem, where-does-it-land W-Z): user rated useful; 3/4; Y (TS handed a retiring contract) answered both+fixtures, answer is refused; finding: Y was a predict item inside a placement list, so keep one item type per check. User asked what 'shared/canonical value encoding' means: the README names it without defining it, a gap a tour surfaces
- 2026-10-23T18:01:52Z (main): parked (waiting on user, review): user answers stop 5 quiz (Q1-Q4) and rates it; then agent gives feedback and records findings in the brief (sections 5 and 6) in a .worktrees/ worktree, notes vdocs-c96d1b, and closes the pilot
  provenance: {"harness_session":"claude-code:1c0c67d0-b42a-41c8-b844-5ee4b3df93e9","harness_session_source":"CLAUDE_CODE_SESSION_ID"}
- 2026-10-23T18:50:55Z (main): resumed
  provenance: {"harness_session":"claude-code:1c0c67d0-b42a-41c8-b844-5ee4b3df93e9","harness_session_source":"CLAUDE_CODE_SESSION_ID"}
