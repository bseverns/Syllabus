# ClassHub Import Notes

These files package `AI in Your Feed` for the ClassHub syllabus ingest flow.

## Files

- `public_overview_classhub.md`: public-facing overview source
- `teacher_plan_classhub.md`: parseable teacher-plan source

## Suggested import command

From the `selfhosted-classhub` repo:

```bash
python3 scripts/ingest_syllabus_md.py \
  --sessions-md /path/to/Syllabus/SECONDARY/AI_in_Your_Feed/classhub_import/teacher_plan_classhub.md \
  --overview-md /path/to/Syllabus/SECONDARY/AI_in_Your_Feed/classhub_import/public_overview_classhub.md \
  --slug ai_in_your_feed \
  --title "AI in Your Feed: Create, Explore, Protect" \
  --default-ui-level secondary
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
