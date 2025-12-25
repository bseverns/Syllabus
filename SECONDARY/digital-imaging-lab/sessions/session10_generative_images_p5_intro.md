# Session 10 — Generative Images with Code (p5.js Intro)

> **Local notes (edit before teaching this session):**  
> - Site / room:  
> - Devices / cameras available:  
> - Image editor(s) in use today:  
> - Where students should save work from this session:  
> - Any schedule tweaks (shortened class, assembly, etc.):  

## Goals

- Show that images can be made and transformed through code.
- Give students a tiny taste of p5.js or similar.
- Generate at least one code-assisted image for Experimental Series.

## A-Block (≈45 min)

### 1. Warm-up: code vs hand (10 min)

- Show an abstract image.
- Ask: “Do you think this was drawn by hand or by code?”
- Reveal that it was generated.

### 2. Mini-lesson: p5.js basics (25–30 min)

In p5.js web editor (or equivalent):

- Write a simple sketch together:
  - `setup()`, `draw()`.
  - Fill the background.
  - Draw some shapes.
- Then:
  - Load an image (if feasible) and apply a simple filter,  
    **or**
  - Use randomness to place shapes and generate a pattern.

Example pattern-only approach (easier for beginners):

- Random rectangles or circles with a limited palette.
- Use `mouseIsPressed` or key press to save an image (`saveCanvas`).

### 3. Connect to series (5–10 min)

- Ask students how this could feed into their Experimental Series:
  - Background textures,
  - Overlays,
  - Standalone pieces.

## B-Block (≈45 min)

### 4. Student coding time (30–35 min)

Students:

- Modify the shared sketch:
  - Change colors, sizes, distributions.
  - Add one new behavior (e.g., movement, more randomness).
- Save at least one generated image for later editing.

Teacher:

- Support students at different coding comfort levels:
  - Some may just remix parameters.
  - Others may add new functions.

### 5. Quick share (5–10 min)

- Show a few generative results.
- Ask:
  - “What surprised you about what the code did?”

### 6. Exit ticket (5 min)

Prompt:

> What is one thing you wish you could make code do to an image?

## Prep

- Session 11: mostly workday. Prepare check-in questions and pacing tasks.
