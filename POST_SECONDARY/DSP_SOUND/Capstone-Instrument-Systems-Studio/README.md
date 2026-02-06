# #7 — Capstone: Instrument + Systems Studio (12 weeks)
**Build the thing that can survive other people.**

This capstone stitches the whole sequence together:
signals → DSP → mapping → real-time firmware → applied audio → **a shipped instrument/system**.

The goal is not “a cool prototype.”  
The goal is **a tool with a user**, a release, and a story that holds up under stress.

## Single track, optional lanes
Everyone follows the same studio arc; you choose a lane for deployment:
- `lanes/instrument/` — MIDI controller / embedded instrument (hardware + firmware)
- `lanes/plugin/` — VST/AU effect or instrument
- `lanes/installation/` — interactive system (sensors, network, multi-device)
- `lanes/curricula/` — build teaching-ready materials around the artifact
- `lanes/release/` — packaging, docs, test plans, maintainability

You can mix lanes, but pick **one primary lane** by Week 3.

## Outcomes
Students can:
- design a system architecture with explicit contracts (timing, protocols, parameters)
- implement reliability features (safe mode, defaults, diagnostics, recovery)
- create a measurement + listening test suite (golden files, bench checklist)
- write end-user documentation that actually works
- ship a release (tag, changelog, versioning) and demonstrate in public
- produce a portfolio artifact with reproducible build/run steps

## Repo map
- `syllabus/` • `sessions/` • `assignments/`
- `project/` capstone brief + report templates
- `docs/` end-user docs templates + examples
- `bench/` QA checklists + test procedures
- `tests/` measurement scaffolds (audio + firmware + interaction)
- `lanes/` optional deployment lanes
- `resources/` patterns for reliability, documentation, and consent-forward design
- `release/` versioning + changelog templates

_Last updated: 2026-02-05_
