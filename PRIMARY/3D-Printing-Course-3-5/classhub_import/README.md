# ClassHub Import Notes

These files package `3D Printing Course (Grades 3-5)` for the ClassHub syllabus ingest flow.

## Files

- `public_overview_classhub.md`: public-facing overview source
- `teacher_plan_classhub.md`: parseable teacher-plan source

## Suggested import command

From the `selfhosted-classhub` repo:

```bash
python3 scripts/ingest_syllabus_md.py \
  --sessions-md /path/to/Syllabus/PRIMARY/3D-Printing-Course-3-5/classhub_import/teacher_plan_classhub.md \
  --overview-md /path/to/Syllabus/PRIMARY/3D-Printing-Course-3-5/classhub_import/public_overview_classhub.md \
  --slug printing_course_grades_3_5 \
  --title "3D Printing Course (Grades 3-5)" \
  --default-ui-level elementary
```

## Why this layer exists

The course already has strong repo-native materials, especially around weekly lessons, print-ops, safety, and queue management. This folder adds the smaller, stricter source files that ClassHub ingest expects:

- public overview metadata
- `Session NN: Title` headings
- `Mission`
- `Teacher prep`
- `Materials`
- `Checkpoints`
- `Common stuck points + fixes`
- `Extensions`

In this import layer, each week is treated as one ClassHub session so the LMS can ingest the full 11-week arc quickly while preserving the original print workflow.
