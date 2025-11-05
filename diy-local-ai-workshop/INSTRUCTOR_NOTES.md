# INSTRUCTOR_NOTES – DIY Local AI Workshop

This file is your backstage script. Participants do **not** need to see it.

You can customize model choices, timing, and emphases here without editing the student handouts.

---

## 1. Model choices (fill these in before teaching)

**Ollama path**

- Default model name for workshop demos:  
  `MODEL_NAME_OLLAMA = "<fill-in-chosen-model-name>"`

Guidelines when choosing:

- Small enough to run on 8–16 GB RAM machines.
- General-purpose chat/assistant behavior.
- Reasonable response speed on CPU-only laptops.

**Python + Hugging Face path**

- Default model ID for `hello_local_model.py`:  
  `MODEL_ID = "<fill-in-hf-model-id>"`

Guidelines when choosing:

- Task: text-generation / causal language modeling.
- CPU-friendly; test on at least one modest machine.
- License appropriate for your audience (e.g., allow workshop use).

**Local tools (`summarizer.py`, `rewriter.py`)**

- Set `MODEL_ID = "<fill-in-hf-model-id>"` in both scripts.
- Ideally, use the same model as in `hello_local_model.py` for consistency.

---

## 2. Minute-by-minute flow (3 hours)

### 0:00–0:10 – Arrival & check-in

- Greet participants, confirm Wi-Fi access.
- Quick pairs/triads:
  - “Where have you seen AI show up in your life this month?”
  - “What’s one thing you’re curious or nervous about today?”

### 0:10–0:25 – Framing talk

Key beats:

1. Cloud vs local:
   - Cloud: someone else’s computer, usage-based billing, terms of service.
   - Local: your machine, your rules, constrained by your hardware.
2. Components:
   - Weights (the “brain file”)
   - Runtime/engine (Ollama or Python)
   - Interface (CLI, script, GUI)
3. Why this matters:
   - Privacy, sovereignty, experimentation, teaching/learning.

Invite 2–3 questions, park deeper ones for later.

### 0:25–0:35 – Quick logistics check

- Ask who:
  - Brought Windows / macOS / Linux.
  - Has Python experience.
- Decide:
  - Majority follows **Ollama**.
  - Python folks can shadow the Hugging Face path during longer download times.

---

### 0:35–1:05 – Install & run via Ollama

Use `01_hello_local_model_ollama.md`.

1. Install Ollama.
2. Confirm `ollama --version`.
3. Pull your chosen small model.
4. Run `ollama run <model-name>`.
5. Prompt warm-ups:
   - greeting
   - explanation of language models
   - “three ways you could help me”

**Teaching moves:**

- Narrate what’s happening (“Now we’re downloading weights”, etc.).
- Pause after first successful responses; celebrate.
- Ask: “How does this feel different from using a website?”

---

### 1:05–1:25 – Optional parallel: Python + Hugging Face

Use `02_hello_local_model_hf.md`.

For Python-friendly participants (or as a demo):

1. Create `local-ai-hf/` and virtualenv.
2. Install `transformers`, `accelerate`, and `torch`.
3. Write `hello_local_model.py` with chosen `MODEL_ID`.
4. Run once, watch it download and respond.
5. Adjust temperature/max tokens once to show behavior changes.

Everyone else:

- Continue exploring prompts in Ollama.
- Begin using `prompts.md` as a menu.

---

### 1:25–1:40 – Guided prompt exploration (whole group)

Project a handful of prompts from `prompts.md`:

- Plain-language explanation
- Capabilities + limits
- Local pride
- Tone check

Have participants:

- Run them locally.
- Pair up and compare outputs.
- Note:
  - Speed
  - Clarity
  - Where the model seems overconfident or vague

Capture 3–4 observations on a whiteboard.

---

### 1:40–2:00 – Micro-projects

Prompt:

> “Pick one *real* task from your work or life that might benefit from a local model.  
> Try it, write down what worked and what didn’t.”

Examples to seed:

- Summarizing a policy or article.
- Drafting a difficult email.
- Brainstorming ideas for a program, workshop, or event.
- Rephrasing complex instructions for a non-technical audience.

Have pairs/triads:

- Attempt the task locally.
- Write on a sticky / shared doc:
  - Task
  - What the model did well
  - What felt off or risky

---

### 2:00–2:15 – Model sizes & swapping

Short talk + demo:

- Show example file sizes on your machine (small vs bigger model).
- Explain:
  - More parameters → more capacity, more resource usage.
  - Quantization as compression + trade-offs.
- In Ollama:
  - If bandwidth allows, show switching to another model (`ollama pull` then `ollama run`).
  - Reuse the *same* prompt on both and compare.

Keep this conceptual, not exhaustive.

---

### 2:15–2:35 – Building tiny tools

Switch to `03_local_tools/README.md`.

1. Explain the pattern:
   - Local model
   - Carefully written prompt
   - Thin wrapper (CLI tool)
2. Walk through `summarizer.py`:
   - Where `MODEL_ID` lives.
   - How `build_prompt` encodes the “contract”.
   - How stdin/stdout are used.
3. Run `summarizer.py` on:
   - A policy or article excerpt.
   - A workshop description.

If time, repeat with `rewriter.py`:

- Show `STYLE_INSTRUCTIONS` dictionary.
- Run a “kind” rewrite on a sharp email.

Invite participants to change one line in the prompt to suit their world.

---

### 2:35–2:50 – Boundaries & next steps

Facilitated reflection:

- “Name one use case where a local model feels clearly helpful.”
- “Name one situation where you would *not* use AI at all.”

Then share a short “next steps” menu:

- **Path 1 – Better UIs:** local web UIs, editor integrations.
- **Path 2 – Better models:** exploring HF model hub, reading licenses.
- **Path 3 – Integrations:** scripting around your own data (notes, docs, code).

---

### 2:50–3:00 – Closing

Ask each person to write (or say) one sentence:

> “In the next month, I might use local AI to ________, but I will *not* use it to ________.”

Optionally, collect these (anonymized) as input for future sessions.

---

## 3. Common pitfalls & backup plans

- **Slow/failed downloads**
  - Have at least one fully prepared “demo machine”.
  - Encourage sharing in small groups.
  - If needed, screen-share your terminal and treat others as “navigator pairs”.

- **Python install hell**
  - Keep the Python track optional.
  - Focus on conceptual understanding; it’s okay if some only watch the demo.

- **Over-trusting answers**
  - Repeatedly remind: “Local doesn’t mean correct.”
  - Use the “limits” prompts in `prompts.md` to foreground this.

- **Anxiety about job displacement**
  - Acknowledge it directly.
  - Frame local tools as *augmentations* and as a way to reclaim some control.

---

## 4. Variants & extensions

- **Shorter format (2 hours)**
  - Trim or drop the Python path.
  - Focus on Ollama + one or two tools.

- **Longer format (multi-session)**
  - Add:
    - Local document indexing / RAG
    - Simple web UI around the tools
    - Collaborative “local AI playbook” writing

- **Technical deep-dive**
  - Dig further into:
    - Tokenization
    - Model architectures
    - Quantization and hardware acceleration

---

Adjust these notes as you run the workshop and learn from the field.  
Treat them as a living script, not a fixed score.
