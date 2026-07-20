# Foundations of Signals and Systems — Weekly Field Guide

Use this after the full launch preflight. The linked session, notebook, and assignment remain authoritative; this is the one-screen weekly teaching view.

| Week | Prep first | Minimum evidence before release | Common stuck response | Complete fallback |
| --- | --- | --- | --- | --- |
| 1 — signals | Generate samples; freeze working sine/square notebook; normalize clips | Two same-scale waveform plots and one observation separating seeing/listening | Confusing frequency and amplitude → vary only one, then label units | Printed plots/data plus reference clips or visual-only comparison |
| 2 — operations | Prepare shifted/scaled signal and RMS/correlation examples | Before/after shift, three RMS values, and one correlation interpretation | Index vs time confusion → mark sample 0 and convert one index to seconds | Small numeric arrays calculated/annotated by hand |
| 3 — convolution | Prepare impulse, moving-average, and echo kernels | Input/kernel/output plot and plain-language convolution explanation | Treating kernel as unexplained recipe → slide/flip it across a five-sample paper example | Paper-strip convolution and supplied executed output |
| 4 — recursion | Keep stable and intentionally unstable coefficient examples | Two impulse responses and a recorded stability boundary | Runaway output → stop execution, restore known-good value, inspect feedback coefficient | Trace five recursion steps in a table |
| 5 — Fourier series | Prepare identical-axis reconstructions at several harmonic counts | Labeled 1/3/5/10-harmonic comparison and artifact explanation | “More harmonics = better” → name target, residual artifact, and cost | Overlay supplied component waves on printed axes |
| 6 — FFT/windows | Prepare non-bin-centered tone and three window results | Same-data window comparison with leakage/main-lobe tradeoff | Reading every bin as a real tone → mark expected frequency and window effect | Inspect supplied spectra and choose defensible interpretation |
| 7 — sampling | Prepare safe and aliased tones plus bit-depth examples | Predicted/observed alias and quantization comparison | Nyquist stated as magic number → draw sample points on one cycle | Paper sampling grid and supplied playback/plots |
| 8 — FIR | Prepare known signal with wanted/unwanted bands | FIR response, input/output comparison, and tap-count tradeoff | Cutoff chosen without purpose → restate wanted/unwanted content first | Compare supplied filters and recommend one with evidence |
| 9 — IIR | Prepare stable design and bounded failure example | Response, impulse decay, stability check, and FIR/bypass comparison | Resonance explored without limits → restore safe parameters and define test range | Analyze supplied stable/unstable responses without processing audio |
| 10 — features | Prepare spectrogram/feature trace with one misleading moment | Parameter-labeled spectrogram and feature limitation | Feature treated as meaning → separate calculation from interpretation | Annotate supplied spectrogram/table and critique one feature |
| 11 — noise | Prepare clean/noisy pair and conservative denoising baseline | Before/after measure, plot, damage note, and refusal condition | Higher SNR treated as total success → inspect removed/residual content | Compare supplied A/B evidence and select/no-select method |
| 12 — showcase | Test every project run route; prepare private demo option | Reproducible run, two views, parameter comparison, failure mode, critique response | Demo depends on hidden environment/file → use frozen output, document missing dependency | Poster/diagram/executed notebook walkthrough with identical rubric |

## Weekly release check

Before students leave: notebook or executed equivalent saved, outputs visible, assignment path understood, reflection started, private data/credentials excluded, and a precise next action recorded.
