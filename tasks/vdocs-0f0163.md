---
id: vdocs-0f0163
title: Consistent READMEs across the verifiably repositories
status: done
priority: 2
created: 2026-10-09T18:36:11Z
updated: 2026-10-10T12:23:00Z
completed: 2026-10-10T12:23:00Z
depends: [autonomy-548e33, sci-fdacb1, nodes-de0dc1, atoms-cd15b4, beliefs-7f8ec2]
tags: [docs]
source: docs/notes/2026-10-09-readme-template-brief.md
agent: claude-code/claude-opus-5-5
---

Every verifiably repository's README follows one template kept in verifiably/docs: what the project is, where it sits in the ecosystem, how to install and use it, and where the detail lives, with bookkeeping moved into docs/. Brief: docs/notes/2026-10-09-readme-template-brief.md. The template is designed by the design child; its plan files one rollout task per repository (absorbing autonomy-6e0015 and sci-edc546). Cross-family goal: ops-81f03b.

## Notes

- 2026-10-10T12:11:30Z (main): atoms-cd15b4 landed (atoms main a261cc1, unpushed); family check now lists only beliefs missing. Plan gap for remaining rollouts: grep the member's tests for reads of AGENTS.md/README.md before rewriting them — atoms' test_fs_architecture.py asserted AGENTS.md sentences the plan dropped
- 2026-10-10T12:23:00Z (main): done
  provenance: {"harness_session":"claude-code:6fef0b1e-d639-470a-8bfe-b18a2ad18564","harness_session_source":"CLAUDE_CODE_SESSION_ID"}
- 2026-10-10T12:23:00Z (main): Every member README follows the family template from verifiably/docs: family.toml, rendered family regions, the contract sections, bookkeeping moved to docs/ indexes; all five rollouts merged and the home's family check passes
  provenance: {"harness_session":"claude-code:6fef0b1e-d639-470a-8bfe-b18a2ad18564","harness_session_source":"CLAUDE_CODE_SESSION_ID"}
