# ClassHub Import Notes

These files package `Build Your Block` for the ClassHub syllabus ingest flow.

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

The course already has strong repo-native materials. This folder adds the smaller, stricter source files that ClassHub ingest expects:

- public overview metadata
- `Session NN: Title` headings
- `Mission`
- `Teacher prep`
- `Materials`
- `Checkpoints`
- `Common stuck points + fixes`
- `Extensions`

In this import layer, each weekly plan is treated as one ClassHub session so the LMS can ingest the full arc quickly without flattening the original four-day weekly rhythm.
