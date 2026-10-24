---
id: vdocs-c96d1b
title: Guided tours of the ecosystem with understanding checks
status: idea
priority: 2
reviewed: true
reviewed_at: 2026-10-24T15:41:57Z
created: 2026-10-13T23:17:11Z
updated: 2026-10-24T15:41:57Z
depends: [vdocs-9ca77b, vdocs-e4318e]
parent: vdocs-d2d5ed
tags: [quick-add]
source: "mindful:thought:f8b1c13fb4502058974da40ef793bc17"
agent: claude-code/claude-opus-5-5
---

Walk the user through the codebases and systems at several scales (a guided, multiscale tour), then check understanding and distill what was learned (self-assessment). Personal learning first: work it in a vdocs worktree; if it proves useful, polish it into vdocs, or elsewhere, later.

Source: mindful:thought:f8b1c13fb4502058974da40ef793bc17

## References

- brief (input, required, kind=brief): docs/notes/2026-10-14-guided-tours-brief.md — first pilot evidence and rules for the second pilot; read before deciding whether to write a skill

## Notes

- 2026-10-14T15:10:29Z (main): scope: briefed; tour format open (live agent-led tour vs written vs rendered from identity tree); parented under goal vdocs-d2d5ed; depends on pilot vdocs-9ca77b; brief: docs/notes/2026-10-14-guided-tours-brief.md
- 2026-10-23T18:53:06Z (docs/tour-pilot-findings): pilot vdocs-9ca77b done: checks that make the learner run the model (predict, placement) helped most; a closing mixed quiz exposed the only lasting misconception; tours also found stale docs in three places. Recommendation: a skill carrying the ladder, check kinds and tour rules, piloted on a second repository first; written tours rejected. See brief §7.
- 2026-10-24T00:43:14Z (main): first pilot recommends a second pilot before writing the skill; it is vdocs-e4318e, which this idea now waits on
- 2026-10-24T15:41:57Z (main): scope: briefed; checked the canonical mindful source and first pilot vdocs-9ca77b against brief revision be4a072; prediction and placement checks helped, while the mixed quiz exposed a remaining misconception; portability beyond beliefs is still unanswered, so reuse second pilot vdocs-e4318e under existing goal vdocs-d2d5ed rather than scope a skill now; retained its dependency, linked the existing brief, and made the follow-up finding and wake-note obligations explicit; brief: docs/notes/2026-10-14-guided-tours-brief.md; no new evidence warrants a handoff edit
