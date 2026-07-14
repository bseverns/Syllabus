# ClassHub Import Notes

These files package `Build Your Block` for the ClassHub syllabus ingest flow while staying aligned with the current **7-week intensive** version of the course.

## Files

- `public_overview_classhub.md`: public-facing overview source
- `teacher_plan_classhub.md`: parseable teacher-plan source
- `weekly_handoff_classhub.md`: quick weekly implementation companion for humans, not the ingest script

## Suggested import command

From the `selfhosted-classhub` repo:

```bash
python3 scripts/ingest_syllabus_md.py \
  --sessions-md /path/to/Syllabus/PRIMARY/Build_Your_Block/classhub_import/teacher_plan_classhub.md \
  --overview-md /path/to/Syllabus/PRIMARY/Build_Your_Block/classhub_import/public_overview_classhub.md \
  --slug build_your_block \
  --title "Build Your Block: A Neighborhood Makers Lab" \
  --default-ui-level elementary
```

## Why this layer exists

The core repo files are written for live facilitation. This folder keeps the smaller, stricter source format that ClassHub can ingest cleanly.

For fast rollout, use this folder in two layers:

- ingest `public_overview_classhub.md` and `teacher_plan_classhub.md`
- keep `weekly_handoff_classhub.md` open during planning or week-to-week facilitation

This import layer now mirrors the intensive package:

- 7 weeks
- 28 sessions
- 1.75-hour studio blocks
- early capstone identity
- narrower tool pathways
- earlier testing, clarity, durability, and showcase logic

## Import note

In this version, each actual studio session is treated as one ClassHub session so the LMS reflects the real pacing of the intensive.

## Fast handoff

If a new site needs to move quickly:

- read `teacher_plan_classhub.md` for the parseable 28-session plan
- read `weekly_handoff_classhub.md` for weekly must-haves, likely failure points, and carry-forward outputs
- pull templates from `../templates/` for capstone planning, project status, durability checks, and session parking
- use the matching files in `../facilitator/field_guides/` when live teaching starts
