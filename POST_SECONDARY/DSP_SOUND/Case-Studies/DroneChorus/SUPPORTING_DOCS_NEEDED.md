# Supporting Docs Needed (FPV “Deeper Ocean” Checklist)

Drone Chorus already documents the **performance system** well. The next frontier is
helping newcomers cross the FPV boundary without drowning.

This is a prioritized list of supporting docs you can add (either in this repo,
or as a sibling “FPV primer” repo that Drone Chorus can link to).

## Tier 1 — On‑ramp essentials (highest value)
1. **FPV glossary + parts map** (FC, ESC, VTX/VRX, UART, MSP, receiver, ELRS, etc.)
2. **Betaflight setup “minimum viable telemetry”**
   - how to confirm MSP is enabled on the right port
   - how to identify the serial device on each OS
3. **Bench mode / props‑off doctrine**
   - safe testing procedures, arming discipline, throttle caps, cages
4. **Telemetry semantics**
   - what roll/pitch/yaw/throttle/RSSI/VBAT actually represent
   - what *ranges* are typical and why normalization choices matter

## Tier 2 — Classroom + rehearsal robustness
5. **Known-good hardware recipes**
   - “one whoop that works” BOM suggestions (keep this brand-agnostic if desired)
   - USB/UART adapters that don’t flake out
6. **Troubleshooting decision tree**
   - “No serial device” / “No MSP frames” / “MIDI port missing” / “Rack not responding”
7. **Safety & accessibility expansion**
   - hearing protection / limiter defaults
   - audience distance, cage design, signage
   - inclusivity notes: how to let learners participate without flying

## Tier 3 — Performance craft
8. **Mapping cookbook**
   - “calm hover” mappings vs “chaos mappings”
   - recommended curves/slews for different airframes
9. **VCV patch anatomy**
   - how to duplicate voices, assign channels, and keep the patch legible
10. **OBS broadcast patterns**
   - stable scene conventions + overlays that teach the mapping

## Tier 4 — Legal / site considerations (keep lightweight + link out)
11. **Where you can fly + how to check rules**
    - keep this as a pointer doc (rules change; don’t freeze them in markdown)
12. **Community norms**
    - indoor flying etiquette, consent and signage, liability boundaries

## What already exists (so you don’t duplicate work)
- Control + wiring: `docs/CONTROL_STACK_PLAYBOOK.md`
- Safety preflight: `docs/checklists/SAFETY.md`
- Rehearsal craft: `docs/EXPERIENCE_PLAYBOOK.md`
- Audience legibility: `docs/UX_MAP.md` + `docs/audience-card.md`
- Sample logs + replay crate: `data/README.md` + `scripts/generate_sample_logs.py`
- Broadcast setup: `obs/README.md`

## Suggested location for new docs
- In-repo: `docs/fpv-primer/` for Tier 1–2
- Or sibling repo: `fpv-primer/` with Drone Chorus linking into it from README
