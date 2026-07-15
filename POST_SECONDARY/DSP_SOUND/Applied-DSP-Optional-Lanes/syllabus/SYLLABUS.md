# Syllabus — Applied DSP (12 weeks)

**Loop:** build → measure → listen → document → optimize → ship.

Single track: shared DSP core (`dsp/`).  
Optional lanes: choose deployment (`lanes/`).

See `syllabus/SCHEDULE.md`.

## ClassHub Delivery Map

| Phase | Required private evidence | ClassHub materials |
| --- | --- | --- |
| Weeks 1–3 — pipeline/parameters/filters | Golden input/output, level and CPU baseline, taper/smoothing evidence, filter response, stability bounds, and code version | Measurement checklist; private code/data/plot uploads; reflection |
| Weeks 4–7 — delay/nonlinearity/dynamics/modulation | Before/after audio, headroom/DC/alias checks, envelope response, and parameter tests | DSP-safety checklist; private audio/code/data; midpoint rubric |
| Weeks 8–10 — reverb/chaos/presets | Scoped reverb evidence, bounded stochastic test, versioned preset schema, migration/import/export result | Reliability checklist; private files/audio; design-log reflection |
| Weeks 11–12 — optimize/release | Before/after CPU/allocation measures, regression/golden comparisons, docs, release notes, and demo | Final rubric; private portfolio upload; optional gallery excerpt |

Do not accept DSP changes by listening alone: preserve plots, golden comparisons, or CPU measurements. Keep lane deployment details and unreleased source private.
