# Foundations of Signals and Systems — Facilitator Launch Guide

Use this guide with `syllabus/SYLLABUS.md`, `syllabus/SCHEDULE.md`, and the weekly session files. It supplies the preflight, material plan, programming on-ramp, access routes, and recovery moves that turn the repository into a launchable course package.

## Delivery boundary

The documented course is 12 weeks for advanced high-school or undergraduate makers. It can run in either format:

- one 150–180 minute studio/lab each week; or
- two 75-minute meetings, with concept/listening work first and notebook lab work second.

Python experience is helpful but not required when the Week 0 bridge below is provided. Basic algebra and graph-reading remain real prerequisites; use `resources/MATH_PRIMER.md` and a local tutoring/support route when those skills are still developing.

## Materials for each student

- Python/Jupyter-capable computer or reliable hosted-notebook access;
- private course folder or repository with save/reopen/version history;
- headphones with a safe listening-level option;
- notebook or paper for sketches, predictions, and equations;
- the supplied notebooks, generated sample signals, math primer, and glossary.

For the room:

- instructor display and speakers used only at a comfortable level;
- a known-good course environment and offline copy of required packages;
- one frozen, executed copy of every weekly notebook;
- sample `.wav`, `.csv`, and plot exports for no-audio/device recovery;
- loaner headphones and a no-headphones analysis route;
- accessible shared storage or LMS/ClassHub handoff.

Microphones, personal recordings, sensors, and GitHub accounts are optional. Do not require students to record themselves or publish repositories.

## Mandatory software preflight

On the same operating-system image students will use:

1. Create the environment from `setup/ENVIRONMENT.md`.
2. Install the pinned/local approved dependency set from `requirements.txt`.
3. Run `scripts/generate_samples.py`.
4. Open, run all, save, close, and reopen every notebook.
5. Confirm plots render and exported files land in an approved writable folder.
6. Test the no-live-audio route using saved clips and plots.
7. Test notebook submission without exposing credentials or unrelated files.
8. Save the working Python/package versions and a clean environment export.

If the complete smoke test has not passed, delay launch or use an institutionally supported hosted image. Package documentation is ready; the local runtime still controls delivery.

## Week 0 bridge for limited programming exposure

Run as one 90-minute lab or two 45-minute blocks.

### Bridge A — Notebook confidence

- open the known-good Week 1 copy;
- identify a text cell, code cell, run button, output, and error message;
- change one labeled number and predict what the plot will do;
- run one cell, then restart and run all;
- save a new named copy and reopen it.

### Bridge B — Read a signal experiment

- locate the input array/signal;
- locate the operation or transformation;
- locate the plot or saved output;
- compare before/after with one sentence or spoken note;
- intentionally enter one safe invalid value, read the error together, undo, and rerun.

Readiness means a student can run, change, compare, save, and ask a specific question with available supports. Typing speed, Git command memory, and recalling Python syntax without examples are not readiness measures.

## Plain-language opening

Say this before the first lab:

> You are not expected to arrive fluent in Python or advanced math. We will use code as a laboratory instrument: change one labeled part, observe what changes, and explain the result. A plot, listening note, diagram, or spoken walkthrough can all show understanding.

Shared words:

- **signal:** a value that changes across time, space, or samples;
- **sample:** one recorded measurement;
- **system:** a process that transforms an input into an output;
- **time domain:** how a signal changes across time or sample number;
- **frequency domain:** how much different rates of repetition contribute;
- **filter:** a system that changes selected parts of a signal;
- **parameter:** a value chosen to control a process;
- **reproducible:** another person can follow the saved steps and obtain the intended result.

## Default 165-minute rhythm

| Time | Move |
| --- | --- |
| 0–15 min | Listening/plot observation and visible question |
| 15–35 min | Concept demonstration with one input and one transformation |
| 35–55 min | Guided prediction and first notebook cells |
| 55–65 min | Screen/listening break |
| 65–110 min | Core lab in pairs or individually |
| 110–125 min | Quiet reset and checkpoint |
| 125–150 min | Extension, comparison, or assignment start |
| 150–165 min | Save outputs, reflection, submission check, and next step |

## Access and participation routes

- Provide plot descriptions, data tables, and numeric summaries; do not make color or audio the only evidence.
- Caption instructional video and provide written steps for spoken demonstrations.
- Offer saved audio plus waveform/spectrum evidence when live playback or hearing access is a barrier.
- Let students use synthetic, public, or instructor-provided signals instead of personal recordings.
- Accept typed, handwritten, spoken, or screen-recorded explanation when the same reasoning is visible.
- Pair with rotating `operator` and `analyst/navigator` roles; both students predict and explain.
- Keep listening levels moderate and normalize instructor examples before class.

## Common-stuck and recovery guide

| Symptom | Next move |
| --- | --- |
| Notebook opens with the wrong kernel | Select the approved kernel; if unavailable, use the frozen executed copy while support repairs the environment |
| A student runs cells out of order | Restart kernel, run all, then make one labeled change |
| Audio backend fails | Export/read the `.wav`, inspect plots/data, or use the supplied reference clip |
| Package/import error | Record the environment and error; move to the executed notebook rather than spending the whole session reinstalling |
| Plot looks blank or extreme | Check array length, units, axis limits, sample rate, and parameter range one at a time |
| Math notation blocks progress | Return to input → operation → output; use a numeric example and diagram before symbolic form |
| Student copies code without understanding | Ask for a prediction, one parameter change, observed result, and explanation of the changed line |
| Git/repository workflow fails | Save a timestamped notebook and reflection to private course storage; restore version control later |

## Evidence and completion

Each week, preserve a runnable notebook or executed equivalent, required plots/exports, assignment responses, and a short reflection. The final project must include an input, transformation, output, two visualizations, parameter comparison, documented failure mode, reproducible run instructions, and critique response.

After delivery, record actual environment versions, notebook failures, audio/access routes used, time spent on the bridge, and changes needed before the next launch.
