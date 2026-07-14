#!/usr/bin/env python3
"""Validate catalog/menu.json and render the partner-facing menu."""

from __future__ import annotations

import argparse
import json
from collections import defaultdict
from pathlib import Path


def validate_menu(menu_path: Path, repo_root: Path) -> list[str]:
    """Return human-readable errors for source paths that do not resolve."""
    menu = json.loads(menu_path.read_text())
    errors: list[str] = []
    for offering in menu["offerings"]:
        readiness = offering["readiness"]["status"]
        if readiness not in {"GO", "GO-P", "ADAPT", "PILOT", "NO"}:
            errors.append(f"{offering['offering_id']}: unsupported readiness: {readiness}")
        for source_path in offering["repo_paths"]:
            if not (repo_root / source_path).exists():
                errors.append(f"{offering['offering_id']}: missing source path: {source_path}")
    return errors


def render_menu(menu: dict) -> str:
    """Render public offerings into a compact, partner-facing Markdown menu."""
    by_age_band: dict[str, list[dict]] = defaultdict(list)
    for offering in menu["offerings"]:
        if offering["public"]:
            for age_band in offering["age_bands"]:
                by_age_band[age_band].append(offering)

    lines = [
        "# Workshop Menu",
        "",
        "Hands-on creative technology experiences, selected from the full curriculum archive. "
        "Equipment and readiness labels are for internal deployment planning; partners pick the experience.",
        "",
    ]
    for age_band, offerings in by_age_band.items():
        lines.extend([f"## {age_band}", ""])
        for offering in offerings:
            equipment = offering["equipment"]
            readiness = offering["readiness"]
            sources = ", ".join(f"[`{path}`](../{path})" for path in offering["repo_paths"])
            lines.extend(
                [
                    f"### {offering['public_title']}",
                    "",
                    offering["summary"],
                    "",
                    f"**Formats:** {', '.join(offering['formats'])}  ",
                    f"**Screen load:** {'–'.join(offering['screen_load'])}  ",
                    f"**Equipment:** {equipment['minimum_tier']}→{equipment['full_tier']} — {equipment['summary']}  ",
                    f"**Documentation:** {readiness['status']} — {readiness['note']}  ",
                    f"**Source:** {sources}",
                    "",
                ]
            )
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--menu", type=Path, default=Path("catalog/menu.json"))
    parser.add_argument("--repo-root", type=Path, default=Path("."))
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    errors = validate_menu(args.menu, args.repo_root)
    if errors:
        print("\n".join(errors))
        return 1

    menu = json.loads(args.menu.read_text())
    rendered = render_menu(menu)
    if args.output:
        args.output.write_text(rendered)
        print(f"wrote {args.output}")
    else:
        print(rendered)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
