# AI at Work with Microsoft Learn

A 6-week hybrid workforce studio for high school students preparing for professional settings

This repo packages a **Syllabus-repo style course bundle** designed for a **GenSys Works partnership context** and tuned for a weekly rhythm of:
- **Day 1:** in-person
- **Day 2:** distance-learning
- **Day 3:** in-person
- **Day 4:** distance-learning

The course keeps the original 24-session / 48-hour structure while flexing toward a Microsoft AI fundamentals credential pathway.

## Certification strategy

This version is built around a **Microsoft AI fundamentals study alignment** plus selected **Microsoft Learn** study routines. The design goal is not to turn the whole class into test prep. Instead, students learn the practical workplace uses of AI while also building the vocabulary, concepts, and confidence needed to pursue a Microsoft credential.

**Important note:** Microsoft still offers **Exam AI-900: Azure AI Fundamentals** through **June 30, 2026**, but Microsoft has announced a transition to **Exam AI-901** and newer Microsoft Foundry-oriented training in 2026. Before launch, staff should verify the current certification name, exam code, links, policies, and domain wording on Microsoft Learn / Credentials.

## Design logic

The sequence intentionally begins with the more foundational and sometimes "boring" parts of workplace technology:
- how digital systems work
- how AI tools differ from search and software
- files, folders, versions, permissions
- prompting, checking, and revising
- privacy, risk, bias, and professional judgment

The back half shifts into practicum:
- writing and admin workflows
- role-based workplace simulations
- personal toolkit building
- Microsoft Learn review routines
- a final capstone workflow students can demonstrate

## Hybrid continuity model

Every week follows the same spine so students never have to wonder what comes next:
- **In-person A:** launch, model, and guided practice
- **Distance B:** Microsoft Learn module + notes + small evidence artifact
- **In-person C:** studio build, coaching, and correction
- **Distance D:** quiz / reflection / portfolio update / bridge note for next week

## Repo map

```text
course/
  COURSE_OVERVIEW.md
  SYLLABUS.md
  SCOPE_AND_SEQUENCE.md
  MICROSOFT_CERT_ALIGNMENT.md
  HYBRID_CONTINUITY_MODEL.md
  ASSESSMENT_RUBRIC.md
  CAPSTONE.md
  sessions/
  student-toolkit/
  instructor/
  admin/
```

## Suggested use

- Start with `course/COURSE_OVERVIEW.md`
- Use `course/SYLLABUS.md` for the public-facing syllabus
- Use `course/MICROSOFT_CERT_ALIGNMENT.md` to explain the credential logic
- Use `course/HYBRID_CONTINUITY_MODEL.md` to keep the in-person / distance rhythm stable
- Use `course/sessions/` for daily delivery
- Duplicate items in `course/student-toolkit/` so each student gets a working doc set
- Use `course/admin/ONE_PAGER.md` and `course/admin/CREDENTIAL_VALUE_NOTE.md` for partner conversations

## Student reference layer

The student toolkit now includes two non-template anchor docs for concepts and deeper reading:

- `course/student-toolkit/AI_SYSTEMS_FLOW_REFERENCE.md`
- `course/student-toolkit/AI_DEEPER_DIVES_AND_REFERENCES.md`

These are meant to give students a more stable map of AI systems, responsible use, and reputable follow-up reading instead of leaving concept-building to isolated session notes.

## ClassHub import

This course now includes a ClassHub ingest layer:

- `classhub_import/public_overview_classhub.md`
- `classhub_import/teacher_plan_classhub.md`
- `classhub_import/README.md`

Those files are formatted for the `ingest_syllabus_md.py` workflow in the sibling `selfhosted-classhub` repo, so the course can be packaged for fast LMS import without flattening the richer course bundle.

## Notes

This package is written in Markdown-first form so it can be:
- versioned in Git
- edited quickly
- imported into a larger Syllabus repo
- turned into PDFs later
- adapted for different workforce or internship partner contexts

## License

MIT
