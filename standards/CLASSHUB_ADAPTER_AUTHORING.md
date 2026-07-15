# ClassHub Adapter Authoring

Add or revise a `classhub_import` adapter when a catalog offering is scheduled for ClassHub delivery. Do not retrofit every historical course merely to populate newer optional fields.

- ClassHub preserves `Lesson slug (for course.yaml): sNN-explicit-slug` values. Keep each explicit slug unique, lowercase, dash-separated, and aligned with its session number; title-derived differences are allowed.
- Optional `Submission` and `ClassHub materials` sections compile into ClassHub's existing coursepack fields. Use `Type:`, `Accepted:`, and `Naming:` bullets for submissions. Use `Checklist | Title | item; item`, `Reflection | Title | prompt`, `Rubric | Title | criterion; criterion | scale`, or `Gallery | Title | .png,.jpg | max MB` material rows. Historical sessions do not need these sections added wholesale.
- Optional `Offline handout` lines may provide human-authored `Spanish`, `Somali`, or `Sgaw Karen` `goal`, `do now`, `submit`, and `safety` wording. Missing localized fields fall back to English.

Never invent or machine-fill translations. Add localized wording only when an existing, reviewed translation is available, and otherwise keep the English fallback.
