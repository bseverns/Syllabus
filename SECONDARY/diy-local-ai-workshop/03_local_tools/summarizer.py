#!/usr/bin/env python3
"""summarizer.py – a tiny local text summarizer

Reads text from standard input, sends it to a local language model
with a summarization prompt, and prints a bullet-point summary.

Usage:
    python summarizer.py
    # then paste text, end with Ctrl-D (macOS/Linux) or Ctrl-Z+Enter (Windows)

or:

    cat long.txt | python summarizer.py
"""

from transformers import AutoModelForCausalLM, AutoTokenizer
import sys
import textwrap

# Set this to the model your environment supports well.
# Example: "your-org/your-model-name"
MODEL_ID = "REPLACE_WITH_MODEL_ID"


def load_model_and_tokenizer():
    print(f"[summarizer] Loading model: {MODEL_ID} (this may take a moment)...", file=sys.stderr)
    tokenizer = AutoTokenizer.from_pretrained(MODEL_ID)
    model = AutoModelForCausalLM.from_pretrained(MODEL_ID)
    return model, tokenizer


def build_prompt(text: str) -> str:
    # You can tune this prompt to your context.
    return textwrap.dedent(
        f"""

        You are a concise, careful assistant.

        Summarize the following text into 5 bullet points.
        Each bullet should be under 20 words.
        Preserve key facts and important caveats. Do not invent details.

        TEXT:
        {text}

        SUMMARY (5 bullet points):
        """

    ).strip()


def summarize(model, tokenizer, text: str, max_new_tokens: int = 200) -> str:
    prompt = build_prompt(text)
    inputs = tokenizer(prompt, return_tensors="pt", truncation=True)

    outputs = model.generate(
        **inputs,
        max_new_tokens=max_new_tokens,
        do_sample=True,
        temperature=0.4,  # lower temperature for more consistency
        top_p=0.9,
    )

    full_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    # Return only the part after "SUMMARY" if present
    marker = "SUMMARY"
    idx = full_text.upper().find(marker)
    if idx != -1:
        return full_text[idx + len(marker) :].strip()
    return full_text.strip()


def read_stdin() -> str:
    if sys.stdin.isatty():
        print(
            "[summarizer] Paste or type text below. End with Ctrl-D (macOS/Linux) or Ctrl-Z then Enter (Windows).\n",
            file=sys.stderr,
        )
    chunks = []
    try:
        for line in sys.stdin:
            chunks.append(line)
    except KeyboardInterrupt:
        pass
    return "".join(chunks).strip()


def main():
    text = read_stdin()
    if not text:
        print("[summarizer] No input text received. Exiting.", file=sys.stderr)
        return

    model, tokenizer = load_model_and_tokenizer()
    summary = summarize(model, tokenizer, text)
    print(summary)


if __name__ == "__main__":
    main()
