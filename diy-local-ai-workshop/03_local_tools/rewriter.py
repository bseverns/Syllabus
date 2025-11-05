#!/usr/bin/env python3
"""rewriter.py – a tiny local text rewriter

Reads text from standard input and rewrites it according to a chosen style.

Usage:
    python rewriter.py --style clarity
    # then paste text, end with Ctrl-D (macOS/Linux) or Ctrl-Z+Enter (Windows)

Styles:
    clarity, kind, brief, formal, casual
"""

from transformers import AutoModelForCausalLM, AutoTokenizer
import argparse
import sys
import textwrap

# Set this to the model your environment supports well.
# Example: "your-org/your-model-name"
MODEL_ID = "REPLACE_WITH_MODEL_ID"

STYLE_INSTRUCTIONS = {
    "clarity": "Rewrite for maximum clarity and directness. Keep the meaning, remove jargon and repetition.",
    "kind": "Rewrite in a warm, kind, and respectful tone. Keep the message honest but gentle.",
    "brief": "Rewrite to be as brief as possible while preserving the core meaning.",
    "formal": "Rewrite in a formal, professional tone suitable for business communication.",
    "casual": "Rewrite in a relaxed, friendly tone as if talking to a peer.",
}


def parse_args():
    parser = argparse.ArgumentParser(description="Rewrite text according to a chosen style.")
    parser.add_argument(
        "--style",
        choices=STYLE_INSTRUCTIONS.keys(),
        default="clarity",
        help="Rewrite style to use.",
    )
    return parser.parse_args()


def load_model_and_tokenizer():
    print(f"[rewriter] Loading model: {MODEL_ID} (this may take a moment)...", file=sys.stderr)
    tokenizer = AutoModelForCausalLM.from_pretrained(MODEL_ID)
    model = AutoModelForCausalLM.from_pretrained(MODEL_ID)
    return model, tokenizer


def build_prompt(text: str, style_key: str) -> str:
    instruction = STYLE_INSTRUCTIONS[style_key]
    return textwrap.dedent(
        f"""

        You are a careful editor.

        {instruction}

        ORIGINAL:
        {text}

        REWRITTEN:
        """

    ).strip()


def rewrite(model, tokenizer, text: str, style_key: str, max_new_tokens: int = 240) -> str:
    prompt = build_prompt(text, style_key)
    inputs = tokenizer(prompt, return_tensors="pt", truncation=True)

    outputs = model.generate(
        **inputs,
        max_new_tokens=max_new_tokens,
        do_sample=True,
        temperature=0.7,
        top_p=0.9,
    )

    full_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    marker = "REWRITTEN:"
    idx = full_text.upper().find(marker)
    if idx != -1:
        return full_text[idx + len(marker) :].strip()
    return full_text.strip()


def read_stdin() -> str:
    if sys.stdin.isatty():
        print(
            "[rewriter] Paste or type text below. End with Ctrl-D (macOS/Linux) or Ctrl-Z then Enter (Windows).\n",
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
    args = parse_args()
    style = args.style

    text = read_stdin()
    if not text:
        print("[rewriter] No input text received. Exiting.", file=sys.stderr)
        return

    model, tokenizer = load_model_and_tokenizer()
    rewritten = rewrite(model, tokenizer, text, style)
    print(rewritten)


if __name__ == "__main__":
    main()
