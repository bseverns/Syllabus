# DIY Local AI – Owning Your Own Model (3-Hour Workshop)

This workshop is about *agency*, not hype.

In three hours, participants will:

- Install and run a **local language model** on their own machine
- Understand the basic moving parts: **weights, runtime, interface**
- Compare different small models and their tradeoffs
- Wrap a model in a tiny, focused **command-line tool** (summarizer, rewriter, etc.)
- Leave with ideas and prompts for using local AI *on their terms*

---

## Audience

- Adults with mixed technical backgrounds  
- Comfortable installing software, copying commands, and using a terminal
- No prior ML/AI background required

Recommended:

- Familiarity with basic computer concepts (files, folders, copy/paste)
- Some comfort with a terminal / command prompt (helpful but not required)

---

## Learning goals

By the end of the session, participants should be able to:

1. Explain, in their own words, the difference between:
   - Cloud-hosted AI
   - Locally running AI models

2. Install and run at least one **local LLM** via:
   - **Ollama** (primary path)  
   - Or **Python + Hugging Face** (`transformers`) for those comfortable with Python

3. Identify the key pieces of a local setup:
   - **Model weights** (files that *are* the trained network)
   - **Runtime / engine** (Ollama, Python scripts, etc.)
   - **Interface** (CLI, simple scripts, web UI)

4. Use a local model to:
   - Summarize text
   - Rewrite or polish text
   - Explore creative prompts

5. Articulate personal boundaries:
   - What they are willing to trust a local model with
   - What they are not willing to outsource

---

## Session overview (3 hours)

**0:00 – 0:30 — Framing & Orientation**

- Quick check-in: where participants are seeing AI in their lives
- Cloud vs local: what changes when the model runs on *your* hardware
- Safety, privacy, and limits (high-level)

**0:30 – 2:00 — Main Build: Hello Local Model**

- Install **Ollama** (primary path)
- Pull a small model and have a first “conversation”
- (Parallel track for Python users) Run a simple Hugging Face script
- Guided prompt experiments: creative, explanatory, and practical prompts
- Short paired “micro-projects” using real participant tasks

**2:00 – 2:45 — Owning the Stack a Bit More**

- Model sizes, quantization, and performance
- Swapping models and comparing behavior
- Building a tiny CLI “tool” (summarizer, rewriter, etc.)

**2:45 – 3:00 — Reflection & Next Steps**

- Where local AI fits into their workflows
- Boundaries and ethics in the small
- Pointers to next steps and further learning

---

## Repository map

This repository supports the workshop:

- `README.md` — You are here. High-level overview.
- `01_hello_local_model_ollama.md` — Step-by-step guide for the Ollama path.
- `02_hello_local_model_hf.md` — Step-by-step guide for the Python + Hugging Face path.
- `03_local_tools/`
  - `README.md` — How to use the example tools.
  - `summarizer.py` — A local text summarizer script.
  - `rewriter.py` — A local text rewriter script (tone/clarity helper).
- `prompts.md` — A curated set of prompt “recipes” for participants.
- `INSTRUCTOR_NOTES.md` — Minute-by-minute flow and facilitator guidance.

You can treat `01_` and `02_` as student-facing handouts (with a few instructor notes sprinkled in).

---

## Prerequisites

### Hardware

These are guidelines, not hard rules:

- **Minimum**:
  - 4-core CPU
  - 8 GB RAM
  - 20–30 GB free disk space
- **Recommended**:
  - 16 GB+ RAM
  - SSD storage
  - Optional but helpful: discrete GPU (NVIDIA, Apple Silicon, etc.)

Older laptops can still run **very small** or heavily quantized models; they’ll just be slower.

### Operating systems

- Windows 10 / 11
- macOS (Intel or Apple Silicon)
- Linux (recent distribution)

### Software

For **all participants**:

- A modern web browser
- A terminal / command prompt
- A text editor (VS Code, Sublime, Notepad++, etc.)

For the **Python track** (optional, not required for everyone):

- Python 3.9+ installed
- Ability to install Python packages via `pip`

---

## Before the workshop (instructor checklist)

1. **Choose a default model for Ollama**

   - Pick a small, reasonably fast general-purpose chat / assistant model.
   - Confirm that it runs comfortably on your own machine.
   - Write the exact model name you choose into `INSTRUCTOR_NOTES.md` and your slides (not into the student handouts).

2. **Decide on a Python example model**

   - Choose a CPU-friendly text-generation model.
   - Test the example script in `02_hello_local_model_hf.md` end-to-end.
   - Add the model ID you chose to `INSTRUCTOR_NOTES.md`.

3. **Test both flows on at least two machines**

   - One “nice” machine (good RAM/CPU)
   - One older / modest machine

4. **Clone this repo to your teaching machine**

   - Open the `.md` files for easy projection
   - Have the Python scripts ready to run

5. **Think about your local context**

   - What are the most relevant use cases for your participants?
   - Where do privacy, bias, or institutional constraints show up?

You can annotate `prompts.md` with examples tailored to your org or region.

---

## During the workshop

Use:

- `01_hello_local_model_ollama.md` as your main “walkthrough” script.
- `02_hello_local_model_hf.md` for the subset of participants who are comfortable with Python.
- `03_local_tools/` as the basis for the “tool-building” segment near the end.
- `prompts.md` to seed experiments and pair-work.
- `INSTRUCTOR_NOTES.md` as your backstage script.

Encourage participants to fork, tweak, and rename the tools. The goal isn’t to memorize commands; it’s to feel that the stack is legible and re-shapeable.

---

## After the workshop

You might ask participants to:

- Keep a short **log** of how they use their local model for 1–2 weeks
- Note:
  - What it did well
  - Where it struggled
  - Where they decided *not* to use it

Those notes become raw material for a follow-up session, a community of practice, or even an internal “local AI playbook.”

May this repo be a small, sturdy starting point for people claiming their own computational space.
