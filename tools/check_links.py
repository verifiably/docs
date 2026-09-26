#!/usr/bin/env python3
"""Check every Markdown link in this repository, including links into sibling repositories.

A relative link must resolve here, and a `#fragment` on a Markdown target must name a
heading there. A link of the form `https://github.com/verifiably/<repo>/blob/main/<path>`
(or `/tree/main/`) is checked the same way against the sibling checkout `../<repo>`,
because this repository exists to point into the others and those pointers are what rot.
A sibling that is not checked out on this machine is reported and skipped, never passed.

Exit status: 0 when every checked link resolves, 1 otherwise.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
SIBLINGS = ROOT.parent
LINK = re.compile(r"(?<!!)\[[^]]*]\(([^)\s]+)(?:\s[^)]*)?\)")
HEADING = re.compile(r"^#{1,6}\s+(.*?)\s*$", re.MULTILINE)
FENCE = re.compile(r"^```.*?^```", re.MULTILINE | re.DOTALL)
GITHUB = re.compile(r"\Ahttps://github\.com/verifiably/([\w.-]+)/(?:blob|tree)/main/(.+)\Z")
SKIP_DIRS = {".git", "tasks", ".worktrees", ".tt"}


def heading_slugs(text: str) -> set[str]:
    """The anchors GitHub mints: lowercase, drop punctuation, each space a hyphen."""
    slugs = set()
    for heading in HEADING.findall(FENCE.sub("", text)):
        stripped = re.sub(r"[`*_]", "", heading).lower()
        slugs.add(re.sub(r"[^\w\s-]", "", stripped).replace(" ", "-"))
    return slugs


def check_target(source: Path, target: Path, fragment: str, label: str) -> str | None:
    if not target.exists():
        return f"{source.relative_to(ROOT)}: missing target: {label}"
    if fragment and target.suffix == ".md":
        if unquote(fragment) not in heading_slugs(target.read_text(encoding="utf-8")):
            return f"{source.relative_to(ROOT)}: target resolves but its anchor does not: {label}"
    return None


def markdown_files() -> list[Path]:
    return sorted(
        p for p in ROOT.rglob("*.md") if not SKIP_DIRS.intersection(p.relative_to(ROOT).parts)
    )


def main() -> int:
    errors: list[str] = []
    skipped: set[str] = set()
    for path in markdown_files():
        body = FENCE.sub("", path.read_text(encoding="utf-8"))
        for raw in LINK.findall(body):
            parts = urlsplit(raw)
            if github := GITHUB.match(raw.split("#", 1)[0]):
                repo, rel = github.groups()
                sibling = SIBLINGS / repo
                if not sibling.is_dir():
                    skipped.add(repo)
                    continue
                error = check_target(path, sibling / unquote(rel), parts.fragment, raw)
            elif parts.scheme or parts.netloc:
                continue
            elif parts.path.startswith("/"):
                error = f"{path.relative_to(ROOT)}: absolute link is not allowed: {raw}"
            else:
                target = path if not parts.path else path.parent / unquote(parts.path)
                error = check_target(path, target, parts.fragment, raw)
            if error:
                errors.append(error)
    for repo in sorted(skipped):
        print(f"skipped: ../{repo} is not checked out here; its links were not verified", file=sys.stderr)
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
