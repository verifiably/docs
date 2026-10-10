---
id: vdocs-9c6112
title: Tidy the deferred minors from the README template review
status: doing
priority: 3
size: xs
complexity: low
process: direct
owner: main
created: 2026-10-10T11:26:12Z
updated: 2026-10-10T13:11:44Z
started: 2026-10-10T13:11:44Z
depends: []
tags: [docs]
agent: claude-code/claude-fable-5-1
---

Four minors deferred at the 2026-10-09 whole-branch review of the README template work: (1) justfile header says just gate is what pre-push runs, but hook-pre-push also runs ops-docs family check; (2) docs/specs/2026-10-09-readme-template-design.md section 3 says the summary is 223 characters, the parsed value is 224; (3) the rollouts' common step 5 in docs/plans/2026-10-09-readme-template.md deletes the template's guidance comment but leaves a double blank line; include the blank line in the deleted range; (4) tools/check_links.py docstring says 'under templates/' but SKIP_DIRS matches that directory name at any depth, like the tasks entry.

## Notes

- 2026-10-10T13:11:44Z (main): started
  provenance: {"harness_session":"claude-code:18a9dca7-1937-4f13-8c34-b306392701a9","harness_session_source":"CLAUDE_CODE_SESSION_ID"}
