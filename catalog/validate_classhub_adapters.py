#!/usr/bin/env python3
"""Validate cataloged ClassHub Markdown adapters without importing ClassHub."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

if __package__:
    from .build_menu import resolve_classhub_adapter_paths
else:
    from build_menu import resolve_classhub_adapter_paths


SESSION_RE = re.compile(r"^#{1,6}\s+Session\s+(\d+):\s+(.+?)\s*$", re.MULTILINE)
SLUG_RE = re.compile(r"^Lesson slug \(for course\.yaml\):\s*(.*?)\s*$", re.MULTILINE)
VALID_SLUG_RE = re.compile(r"^s\d{2}-[a-z0-9]+(?:-[a-z0-9]+)*$")
METADATA_RE = re.compile(r"^([A-Za-z][A-Za-z ]+):\s*(.+?)\s*$", re.MULTILINE)
SECTION_NAMES = {
    "teacher prep",
    "materials",
    "agenda",
    "submission",
    "classhub materials",
    "checkpoints",
    "common stuck points + fixes",
    "extensions",
    "local anchors",
    "example variants",
    "community glossary",
    "offline handout",
}
OPTIONAL_SECTION_LABELS = {
    "submission": "Submission",
    "classhub materials": "ClassHub materials",
    "offline handout": "Offline handout",
}
LOCALIZED_LINE_RE = re.compile(
    r"^- (Spanish|Somali|Sgaw Karen) (goal|do now|submit|safety):\s+\S.+$"
)


def _metadata(text: str) -> dict[str, str]:
    first_session = SESSION_RE.search(text)
    header = text[: first_session.start()] if first_session else text
    return {key.strip().lower(): value.strip() for key, value in METADATA_RE.findall(header)}


def _session_count(metadata: dict[str, str]) -> int | None:
    raw = metadata.get("total sessions") or metadata.get("session count")
    if raw is None:
        return None
    match = re.search(r"\d+", raw)
    return int(match.group()) if match else None


def _grade_range(raw: str) -> set[int] | None:
    normalized = raw.lower().replace("–", "-").replace("—", "-")
    match = re.search(r"(\d+)(?:st|nd|rd|th)?\s*-\s*(\d+)(?:st|nd|rd|th)?", normalized)
    if match:
        start, end = map(int, match.groups())
        return set(range(start, end + 1)) if start <= end else None
    named = {
        "middle school": set(range(6, 9)),
        "early high school": set(range(9, 11)),
        "high school": set(range(9, 13)),
    }
    return named.get(normalized.strip())


def _canonical_grades(age_bands: list[str]) -> set[int] | None:
    grades: set[int] = set()
    for age_band in age_bands:
        parsed = _grade_range(age_band)
        if parsed is None:
            return None
        grades.update(parsed)
    return grades


def _section_label(line: str) -> str | None:
    stripped = line.strip()
    if stripped.startswith("#"):
        stripped = stripped.lstrip("#").strip()
    normalized = stripped.rstrip(":").lower()
    return normalized if normalized in SECTION_NAMES else None


def _optional_sections(text: str) -> list[tuple[str, str, list[str], int]]:
    lines = text.splitlines()
    sections: list[tuple[str, str, list[str], int]] = []
    for index, line in enumerate(lines):
        normalized = _section_label(line)
        if normalized not in OPTIONAL_SECTION_LABELS:
            continue
        content: list[str] = []
        for candidate in lines[index + 1 :]:
            if SESSION_RE.match(candidate) or _section_label(candidate) is not None:
                break
            content.append(candidate)
        displayed = line.strip().lstrip("#").strip().rstrip(":")
        sections.append((normalized, displayed, content, index + 1))
    return sections


def _validate_optional_sections(text: str, prefix: str) -> list[str]:
    errors: list[str] = []
    offline_line_numbers: set[int] = set()
    for name, displayed, lines, line_number in _optional_sections(text):
        expected = OPTIONAL_SECTION_LABELS[name]
        if displayed != expected:
            errors.append(f"{prefix}: line {line_number}: use section label '{expected}'")
        bullets = [(offset, line.strip()) for offset, line in enumerate(lines, line_number + 1) if line.strip().startswith("- ")]
        if name == "submission":
            if not bullets:
                errors.append(f"{prefix}: line {line_number}: Submission must contain labeled bullets")
            seen: set[str] = set()
            for offset, bullet in bullets:
                match = re.fullmatch(r"- (Type|Accepted|Naming):\s+(.+)", bullet)
                if not match:
                    errors.append(f"{prefix}: line {offset}: malformed Submission bullet")
                    continue
                label = match.group(1)
                if label in seen:
                    errors.append(f"{prefix}: line {offset}: duplicate Submission {label} bullet")
                seen.add(label)
        elif name == "classhub materials":
            if not bullets:
                errors.append(f"{prefix}: line {line_number}: ClassHub materials must contain pipe-delimited rows")
            for offset, bullet in bullets:
                parts = [part.strip() for part in bullet[2:].split("|")]
                if len(parts) not in {3, 4} or not all(parts[:3]):
                    errors.append(f"{prefix}: line {offset}: malformed ClassHub materials row")
                    continue
                material_type = parts[0]
                if material_type not in {"Checklist", "Reflection", "Rubric", "Gallery"}:
                    errors.append(f"{prefix}: line {offset}: unsupported ClassHub material type: {material_type}")
                if material_type in {"Checklist", "Reflection"} and len(parts) != 3:
                    errors.append(f"{prefix}: line {offset}: {material_type} rows require three fields")
                if len(parts) == 4 and not parts[3].isdigit():
                    errors.append(f"{prefix}: line {offset}: ClassHub material limit must be an integer")
        elif name == "offline handout":
            for offset, bullet in bullets:
                if re.match(r"- (spanish|somali|sgaw karen|karen)\b", bullet, re.IGNORECASE):
                    offline_line_numbers.add(offset)
                    if not LOCALIZED_LINE_RE.fullmatch(bullet):
                        errors.append(f"{prefix}: line {offset}: malformed localized Offline handout line")

    for line_number, line in enumerate(text.splitlines(), 1):
        if re.match(r"\s*- (spanish|somali|sgaw karen|karen)\b", line, re.IGNORECASE):
            if line_number not in offline_line_numbers:
                errors.append(
                    f"{prefix}: line {line_number}: localized handout line must be inside Offline handout"
                )
    return errors


def validate_adapter(offering: dict, repo_root: Path) -> list[str]:
    """Return compatibility errors for one catalog offering's ClassHub adapter."""
    offering_id = offering["offering_id"]
    required_paths, errors = resolve_classhub_adapter_paths(offering, repo_root)
    if required_paths is None:
        return errors
    teacher_path = required_paths["teacher_plan_classhub.md"]
    public_path = required_paths["public_overview_classhub.md"]

    teacher = teacher_path.read_text(encoding="utf-8")
    public = public_path.read_text(encoding="utf-8")
    teacher_meta = _metadata(teacher)
    public_meta = _metadata(public)
    for source_name, text, metadata in (
        ("teacher plan", teacher, teacher_meta),
        ("public overview", public, public_meta),
    ):
        if not re.search(r"^#\s+\S", text, re.MULTILINE):
            errors.append(f"{offering_id}: {source_name} has no parseable title")
        if not re.fullmatch(r"[a-z0-9_]+", metadata.get("course slug", "")):
            errors.append(f"{offering_id}: {source_name} has no parseable Course slug")
        audience = metadata.get("grade level") or metadata.get("grade band") or metadata.get("age band")
        if audience is None or _grade_range(audience) is None:
            errors.append(f"{offering_id}: {source_name} has no parseable grade/age metadata")
        if _session_count(metadata) is None:
            errors.append(f"{offering_id}: {source_name} has no parseable session count")

    if teacher_meta.get("course slug") != public_meta.get("course slug"):
        errors.append(f"{offering_id}: teacher/public Course slug values differ")
    teacher_count = _session_count(teacher_meta)
    public_count = _session_count(public_meta)
    if teacher_count is not None and public_count is not None and teacher_count != public_count:
        errors.append(f"{offering_id}: teacher/public session counts differ")

    sessions = list(SESSION_RE.finditer(teacher))
    session_numbers = [int(match.group(1)) for match in sessions]
    if not sessions:
        errors.append(f"{offering_id}: teacher plan has no parseable Session headings")
    if len(session_numbers) != len(set(session_numbers)):
        errors.append(f"{offering_id}: duplicate session numbers")
    if teacher_count is not None and len(sessions) != teacher_count:
        errors.append(
            f"{offering_id}: parsed {len(sessions)} sessions but metadata declares {teacher_count}"
        )

    explicit_slugs: list[str] = []
    for index, session in enumerate(sessions):
        session_number = int(session.group(1))
        body_end = sessions[index + 1].start() if index + 1 < len(sessions) else len(teacher)
        body = teacher[session.end() : body_end]
        if body.startswith("\r\n"):
            body = body[2:]
        elif body.startswith("\n"):
            body = body[1:]
        body_lines = body.splitlines()
        slugs = [
            match.group(1)
            for line in body_lines[:40]
            if (match := SLUG_RE.fullmatch(line))
        ]
        for line_number, line in enumerate(body_lines[40:], 41):
            if SLUG_RE.fullmatch(line):
                errors.append(
                    f"{offering_id}: Session {session_number:02d} has explicit Lesson slug "
                    f"after ClassHub's 40-line metadata window (body line {line_number})"
                )
        if len(slugs) > 1:
            errors.append(f"{offering_id}: Session {session_number:02d} has multiple explicit Lesson slug lines")
        for slug in slugs:
            explicit_slugs.append(slug)
            if not VALID_SLUG_RE.fullmatch(slug):
                errors.append(f"{offering_id}: malformed explicit Lesson slug: {slug}")
            elif not slug.startswith(f"s{session_number:02d}-"):
                errors.append(
                    f"{offering_id}: explicit Lesson slug does not match Session {session_number:02d}: {slug}"
                )
    duplicates = sorted({slug for slug in explicit_slugs if explicit_slugs.count(slug) > 1})
    for slug in duplicates:
        errors.append(f"{offering_id}: duplicate explicit Lesson slug: {slug}")

    canonical = _canonical_grades(offering.get("age_bands", []))
    if canonical is None:
        errors.append(f"{offering_id}: catalog age_bands cannot be compared to adapter audience")
    else:
        for source_name, metadata in (("teacher plan", teacher_meta), ("public overview", public_meta)):
            raw_audience = metadata.get("grade level") or metadata.get("grade band") or metadata.get("age band")
            adapter_grades = _grade_range(raw_audience or "")
            if adapter_grades is not None and not adapter_grades.issubset(canonical):
                errors.append(
                    f"{offering_id}: {source_name} audience '{raw_audience}' is outside catalog age_bands"
                )

    errors.extend(_validate_optional_sections(teacher, offering_id))
    return errors


def validate_cataloged_adapters(menu_path: Path, repo_root: Path) -> list[str]:
    resolved_repo_root = repo_root.resolve()
    candidate_menu_path = menu_path if menu_path.is_absolute() else resolved_repo_root / menu_path
    resolved_menu_path = candidate_menu_path.resolve()
    if not resolved_menu_path.is_relative_to(resolved_repo_root):
        return [f"menu path escapes repository: {menu_path}"]
    if not resolved_menu_path.is_file():
        return [f"missing menu path: {menu_path}"]
    menu = json.loads(resolved_menu_path.read_text(encoding="utf-8"))
    errors: list[str] = []
    for offering in menu["offerings"]:
        if offering.get("classhub_import_path"):
            errors.extend(validate_adapter(offering, resolved_repo_root))
    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--menu", type=Path, default=Path("catalog/menu.json"))
    parser.add_argument("--repo-root", type=Path, default=Path("."))
    args = parser.parse_args()
    errors = validate_cataloged_adapters(args.menu, args.repo_root)
    if errors:
        print("\n".join(errors))
        return 1
    print("ClassHub adapters valid")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
