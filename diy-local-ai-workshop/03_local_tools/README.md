# Local Tools – Small, Opinionated Scripts

This folder contains example Python scripts that wrap a local language model into focused tools:

- `summarizer.py` — Turn long text into bullet-point summaries
- `rewriter.py` — Rewrite text for clarity and tone

They are intentionally simple:

- Single-file scripts
- Command-line usage
- Easy to read and modify

> **Note:** These scripts assume you have:
> - Python 3.9+ installed
> - `transformers`, `accelerate`, and `torch` installed
> - A reasonably small, CPU-friendly model

You must set the `MODEL_ID` constant in each script to match the model you want to use.

---

## Setup

From the root of your project:

```bash
cd 03_local_tools
python -m venv .venv   # optional, but recommended
source .venv/bin/activate  # macOS/Linux
# .venv\Scripts\activate   # Windows (Command Prompt)

pip install --upgrade pip
pip install transformers accelerate
pip install torch --index-url https://download.pytorch.org/whl/cpu
```

Adjust the PyTorch install command as needed for your platform.

---

## `summarizer.py`

A command-line tool that:

- Reads text from standard input (you paste or pipe in text)
- Feeds it to a local model with a “summarize into bullet points” prompt
- Prints the summary to standard output

### Usage

From inside `03_local_tools`:

```bash
python summarizer.py
```

Then either:

- Paste text directly into the terminal, press Enter after each line, and finish with:
  - `Ctrl + D` (macOS/Linux)
  - `Ctrl + Z` then Enter (Windows)
- Or pipe text in:

  ```bash
  cat long_article.txt | python summarizer.py
  ```

---

## `rewriter.py`

A command-line tool that:

- Reads text from standard input
- Asks the model to rewrite it according to a chosen *style* (clarity, kindness, brevity, etc.)
- Prints the rewritten version

### Usage

```bash
python rewriter.py --style clarity
```

Paste text, end input, and see the rewritten version.

Available styles (by default):

- `clarity`
- `kind`
- `brief`
- `formal`
- `casual`

You can define more styles by editing the `STYLE_INSTRUCTIONS` dictionary inside the script.

---

## Adapting these tools

These scripts are meant as **starting points**. You might:

- Change prompts to match your work (e.g., “rewrite in the voice of our organization”)
- Add file-based input/output (e.g., `--in myfile.txt --out summary.txt`)
- Wrap them in a small web server (Flask/FastAPI) for browser use
- Integrate into shell scripts, Makefiles, or editors

The pattern is always:

1. Decide on a narrow task and a clear “contract”
2. Capture that task in a carefully written prompt
3. Call the model with consistent parameters
4. Wrap it in the most comfortable interface for your daily life

Small, honest tools are often more transformative than big, vague ones.
