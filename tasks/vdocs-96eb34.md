---
id: vdocs-96eb34
title: "overview.md step 7: only a Belief carries the input fingerprint, not every answer"
status: todo
priority: 3
size: xs
complexity: low
process: direct
created: 2026-10-25T19:37:56Z
updated: 2026-10-25T19:37:56Z
depends: []
tags: []
agent: claude-code
origin: agent
---

overview.md 'One building block' step 7 says the answer 'always comes with a fingerprint of every record and rule it used'. In beliefs (741fea1) only Belief carries belief_input_digest; NoBelief and Refused carry none, and the PHF19 example itself ends in NoBelief. Found while drawing the NCI talk's record diagram (mm-042149). The overview's record diagram also omits the belief node and hangs verification off the run, while the beliefs guide README's diagram has belief and the contract has verification verifies assessment.

## Notes

- 2026-10-25T19:37:56Z (add): created
  provenance: {"harness_session":"claude-code:7e453417-3f37-4c18-9c2b-769acf75361f","harness_session_source":"CLAUDE_CODE_SESSION_ID","origin":"agent"}
