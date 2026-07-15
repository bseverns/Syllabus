#!/usr/bin/env python3
"""Validate catalog/menu.json and render the partner-facing menu."""

from __future__ import annotations

import argparse
import json
from collections import defaultdict
from pathlib import Path


def validate_menu(menu_path: Path, repo_root: Path) -> list[str]:
    """Return human-readable errors for invalid deployment claims."""
    menu = json.loads(menu_path.read_text())
    errors: list[str] = []
    offering_ids: set[str] = set()
    resolved_repo_root = repo_root.resolve()
    for offering in menu["offerings"]:
        offering_id = offering["offering_id"]
        if offering_id in offering_ids:
            errors.append(f"{offering_id}: duplicate offering_id")
        offering_ids.add(offering_id)

        readiness = offering["readiness"]["status"]
        if readiness not in {"GO", "GO-P", "ADAPT", "PILOT", "NO"}:
            errors.append(f"{offering_id}: unsupported readiness: {readiness}")
        if offering.get("public") and readiness not in {"GO", "GO-P"}:
            errors.append(f"{offering_id}: public offerings must be GO or GO-P")
        for screen_load in offering.get("screen_load", []):
            if screen_load not in {"S0", "S1", "S2", "S3", "S4"}:
                errors.append(f"{offering_id}: unsupported screen load: {screen_load}")
        equipment = offering.get("equipment", {})
        for equipment_tier in (equipment.get("minimum_tier"), equipment.get("full_tier")):
            if equipment_tier is not None and equipment_tier not in {"E0", "E1", "E2", "E3", "E4"}:
                errors.append(f"{offering_id}: unsupported equipment tier: {equipment_tier}")
        for source_path in offering["repo_paths"]:
            path = Path(source_path)
            if path.is_absolute():
                errors.append(f"{offering_id}: source path must be relative: {source_path}")
                continue
            resolved_path = (resolved_repo_root / path).resolve()
            if not resolved_path.is_relative_to(resolved_repo_root):
                errors.append(f"{offering_id}: source path escapes repository: {source_path}")
                continue
            if not resolved_path.exists():
                errors.append(f"{offering_id}: missing source path: {source_path}")
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
