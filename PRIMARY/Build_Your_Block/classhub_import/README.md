# ClassHub Import Notes

These files package `Build Your Block` for the ClassHub syllabus ingest flow while staying aligned with the stronger repo-native course package.

## Files

- `public_overview_classhub.md`: public-facing overview source
- `teacher_plan_classhub.md`: parseable teacher-plan source

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

The core course files are written for live facilitation. This folder keeps a smaller, stricter source format that ClassHub can ingest cleanly without flattening the course identity.

This import layer now mirrors the stronger package assumptions:

- one ClassHub session per course week
- consistent weekly structure
- mixed-age adaptations
- clear fastest-success targets
- tech-failure backup thinking
- process-centered documentation
- explicit capstone continuity

## Main package references

If a staff team wants the fuller implementation layer, point them to:

- `../README.md`
- `../SYLLABUS.md`
- `../docs/MINIMUM_VIABLE_IMPLEMENTATION.md`
- `../docs/ASSESSMENT_AND_DOCUMENTATION.md`
- `../facilitator/IMPLEMENTATION_NOTES.md`
- `../templates/CAPSTONE_PROJECT_PLANNER.md`
- `../templates/WEEKLY_PROJECT_STATUS_CARD.md`
- `../templates/DURABILITY_AND_USER_TEST_CHECKLIST.md`

## Import note

In this import layer, each weekly plan is treated as one ClassHub session so the LMS can ingest the full 16-week arc quickly without flattening the original four-day teaching rhythm.
