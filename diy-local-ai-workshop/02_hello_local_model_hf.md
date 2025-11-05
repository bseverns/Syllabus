# Hello Local Model – Python + Hugging Face Path

> **Goal:** By the end of this guide, you will:
> - Create a small Python project
> - Install Hugging Face `transformers` and dependencies
> - Load a text-generation model locally
> - Generate a short response from it

This path is for participants who are comfortable with **Python** and installing packages.  
If that’s not you, stick with the Ollama guide; you can revisit this later.

---

## 1. Create a project folder

Pick a location (e.g., Desktop) and create a folder:

```bash
mkdir local-ai-hf
cd local-ai-hf
```

---

## 2. (Optional but recommended) Create a virtual environment

A virtual environment keeps your workshop packages contained.

```bash
python -m venv .venv
```

Activate it:

- On **macOS / Linux**:

  ```bash
  source .venv/bin/activate
  ```

- On **Windows** (Command Prompt):

  ```bash
  .venv\Scripts\activate
  ```

Your prompt should now show something like `(.venv)` at the beginning.

---

## 3. Install dependencies

We’ll install:

- `transformers` — the Hugging Face model library
- `accelerate` — helpers for device management
- `torch` — the PyTorch backend (CPU version is fine for this workshop)

Run:

```bash
pip install --upgrade pip
pip install transformers accelerate
```

For PyTorch, use the CPU wheel appropriate for your platform. A common pattern:

```bash
pip install torch --index-url https://download.pytorch.org/whl/cpu
```

If you run into issues, ask the instructor; the exact command can vary by OS and Python version.

---

## 4. Choose a model

We need a **small, CPU-friendly** model.

Your instructor will provide a model ID string for you to use, such as:

```text
<your-org/your-chosen-model>
```

Open the model’s page on Hugging Face:

- Note the **license**
- Look at the **Files** tab (this is where the actual weights live)
- Notice the tasks it’s designed for (text generation, etc.)

---

## 5. Write a “hello world” script

Create a file named `hello_local_model.py` in your `local-ai-hf` folder.

Paste in:

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

# Change this to the model your instructor recommends
MODEL_ID = "REPLACE_WITH_MODEL_ID"


def main():
    print(f"Loading model: {MODEL_ID}")
    tokenizer = AutoTokenizer.from_pretrained(MODEL_ID)

    # For workshop simplicity, we use float32 and CPU
    model = AutoModelForCausalLM.from_pretrained(
        MODEL_ID,
        torch_dtype=torch.float32,
    )

    prompt = "Write a short, kind greeting from a local AI model running on my laptop."
    print("\nPROMPT:\n", prompt)

    inputs = tokenizer(prompt, return_tensors="pt")
    with torch.no_grad():
        outputs = model.generate(
            **inputs,
            max_new_tokens=80,
            do_sample=True,
            temperature=0.7,
            top_p=0.9,
        )

    text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    print("\nRESPONSE:\n", text)


if __name__ == "__main__":
    main()
```

Save the file.

When you’re ready, replace `"REPLACE_WITH_MODEL_ID"` with the actual model ID your instructor provides.

---

## 6. Run the script

In your terminal (with the virtual environment active, if you’re using one):

```bash
python hello_local_model.py
```

The first run will:

- Download the tokenizer and model weights from Hugging Face
- Cache them on your machine
- Then run the model to generate text

You should see:

- A “Loading model” message
- The prompt
- The model’s response

If you see errors, don’t panic—most are solvable. Common issues:

- Not enough RAM → try a smaller model or quantized variant (your instructor may suggest alternatives)
- Package conflicts → try a fresh virtual environment or ask for help

---

## 7. Experiment with the generation settings

In `hello_local_model.py`, find the `generate` call:

```python
outputs = model.generate(
    **inputs,
    max_new_tokens=80,
    do_sample=True,
    temperature=0.7,
    top_p=0.9,
)
```

Try:

- Lower `temperature` (e.g., `0.2`) for more deterministic answers
- Higher `temperature` (e.g., `1.0`) for more creative answers
- Change `max_new_tokens` to control length

Re-run the script each time and observe the differences.

---

## 8. Make it interactive (small extension)

If time allows, you can turn this into a simple loop:

Replace the `main()` body with:

```python
def main():
    print(f"Loading model: {MODEL_ID}")
    tokenizer = AutoTokenizer.from_pretrained(MODEL_ID)
    model = AutoModelForCausalLM.from_pretrained(
        MODEL_ID,
        torch_dtype=torch.float32,
    )

    print("Type a prompt and press Enter. Empty line to exit.\n")
    while True:
        prompt = input("You: ").strip()
        if not prompt:
            break

        inputs = tokenizer(prompt, return_tensors="pt")
        with torch.no_grad():
            outputs = model.generate(
                **inputs,
                max_new_tokens=120,
                do_sample=True,
                temperature=0.7,
                top_p=0.9,
            )

        text = tokenizer.decode(outputs[0], skip_special_tokens=True)
        print("Model:", text)
        print()
```

Now:

```bash
python hello_local_model.py
```

and chat in the terminal.

---

## 9. Reflection prompts

Take 2–3 minutes to jot down:

- Something this Python path made clearer than the Ollama path
- Something the Ollama path made easier than this one
- One idea for a **small script or tool** you’d like to build on top of this

We’ll move from “hello model” into focused tools in the next segment.
