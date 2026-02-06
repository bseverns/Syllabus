# Week 04 — Difference equations, feedback, and stability

## Goals
- Implement a simple recursive (IIR) filter.
- Observe how feedback creates resonance and instability.
- Relate recursion to poles/zeros at an intuitive level.

## Session arc (suggested timing)
1. **Warm-up (10 min)** — listen to a feedback squeal example; ask: what’s repeating?
2. **Mini-lecture (25 min)** — difference equations; FIR vs IIR; stability as ‘does it blow up?’
3. **Guided lab (60–80 min)** — code a 1st-order IIR; sweep coefficients; watch ringing and blow-ups
4. **Share-out (15 min)** — students share a stable and unstable setting and describe the difference
5. **Close (10 min)** — set expectations: we’ll keep math gentle, but precise

## Prep (instructor)
- Have a visual for “feedback loop” (block diagram).
- Pick safe coefficient ranges for first experiments.

## Materials
- JupyterLab + Python env
- Headphones

## Extensions (if time / advanced track)
- Add a second pole/zero and show a notch-ish effect.
- Preview z-plane without going deep.

## Exit ticket (5 min)
If an IIR filter explodes, what does that mean in the real world?

## Links
- Lab notebook: `labs/week04_difference_equations.ipynb`
- Assignment: `assignments/hw04_iir_basics.md`
