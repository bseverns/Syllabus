# Prompt Recipes for Local AI

These prompts are meant to be used with **local models** — via Ollama, the Python scripts, or other interfaces.

Feel free to adapt them to your context. The goal is to be concrete and honest about what you want the model to do.

---

## 1. Warm-up prompts (getting a feel for the model)

Use these at the beginning of the workshop:

1. **Plain-language explanation**

   > Explain what a language model is in two sentences, as if I were 10 years old.

2. **Capabilities snapshot**

   > List five things you are good at and five things you are *not* good at as a language model.

3. **Local pride**

   > Write a short note introducing yourself as a local AI model running on my laptop.  
   > Mention privacy and offline use.

4. **Tone check**

   > Rewrite the following sentence in three different tones: formal, casual, and playful.  
   >  
   > `I am learning how to run AI models on my own computer.`

---

## 2. Work-oriented prompts

### 2.1. Summarizing

Use with `summarizer.py` or in an Ollama / Python chat.

**Baseline summary**

> Summarize the following text into 5 bullet points.  
> Each bullet should be under 20 words.  
> Preserve key facts and important caveats. Do not invent details.  
>  
> TEXT:  
> [paste text here]

**Audience-aware summary**

> Summarize the following text into 5 bullet points for a non-technical audience.  
> Avoid jargon, but keep important nuance.  
>  
> TEXT:  
> [paste text here]

### 2.2. Drafting & revising emails

**Drafting a first version**

> I need to write an email with the following purpose and constraints.  
> PURPOSE: [describe situation]  
> TONE: [e.g. kind but firm]  
> LENGTH: [e.g. 1–2 paragraphs]  
> Please draft a possible email.

**Rewriting an existing email**

Use this with `rewriter.py` (e.g., style: `kind` or `clarity`):

> Rewrite the following email to improve clarity and kindness.  
> Keep the core message and any specific details.  
>  
> EMAIL:  
> [paste email here]

### 2.3. Idea generation

**Brainstorming**

> I need ideas for [project or task].  
> Generate 10 ideas, mixing safe/obvious ones with a few more experimental options.  
> For each idea, include one sentence on risks or downsides.

**Constrained ideation**

> Suggest 7 ideas for [context] that:  
> - Can be done with minimal budget  
> - Respect privacy and consent  
> - Are feasible for a small team  
>  
> Present them as a numbered list.

---

## 3. Learning & reflection prompts

### 3.1. Understanding the model’s limits

> Describe 5 specific tasks where a local language model like you is likely to perform poorly.  
> For each, explain why.

> Given that you do not access the internet and rely on training data that may be out of date,  
> list ways a human should double-check your answers in high-stakes situations.

### 3.2. Building boundaries

These are for humans, not models—but you can still ask the model to help you think.

> Help me draft a short personal policy for when I will *not* use AI tools.  
> Include at least 3 examples and explain the reasoning behind each.

> Help me write a one-paragraph “AI use statement” I could share with colleagues,  
> explaining how I plan to use local AI tools in my work and what I will keep strictly human.

---

## 4. Technical exploration prompts

Use these for participants who want to go deeper technically.

### 4.1. Inspecting behavior

> I will paste several prompts and your responses.  
> After that, analyze your own behavior: where were you confident, where did you hedge, and where did you hallucinate?

### 4.2. Model comparison

When you have two models installed, run this prompt on both and compare:

> Explain, in 5 bullet points, the tradeoffs between running a small local model and using a large cloud model.  
> Mention privacy, cost, speed, quality, and hardware requirements.

Then discuss:

- Which model gave a clearer explanation?
- Which one was more cautious or nuanced?

---

## 5. For future experiments

You can extend these patterns into:

- Drafting lesson plans or workshop outlines
- Refactoring code (for those with programming background)
- Generating practice questions for self-study
- Creating outlines for reports or presentations

The core template, whenever you write a new prompt:

1. **Role or framing**  
   “You are a [kind / careful / critical] assistant…”
2. **Task description**  
   What exactly you want: summarize, rewrite, compare, brainstorm, etc.
3. **Constraints**  
   Length, tone, format (bullets, paragraphs, etc.), what *not* to do.
4. **Input**  
   The text, data, or situation.
5. **Output format**  
   Bulleted list, numbered items, sections, etc.

Clarity here is an act of care: for yourself, for others, and for the systems you’re building around these models.
