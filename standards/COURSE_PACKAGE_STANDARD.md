# Course Package Standard

This standard makes the catalog the source of truth for **delivery claims**. Existing age-band folders remain historical and practical locations; they are not canonical audience metadata.

Apply this when creating a new package or changing an offering's readiness. Do not retrofit the archive merely to satisfy this document.

## Content types

| Type | Meaning | Public shelf rule |
| --- | --- | --- |
| Offering | A selectable experience described for a partner. | May point to one or more packages. |
| Course package | A complete, teachable system. | Can be `GO` or `GO-P`. |
| Module | A reusable activity or part of a package. | Not listed alone unless deliberately sold as an offering. |
| Brief | A proposed or partial package. | `ADAPT`, `PILOT`, or `NO`; never a ready offering. |

## Audience truth

Record audience in the catalog, not directory position. Each audience claim must be one of:

- `documented` — the package was written and scaffolded for this band.
- `adaptable` — a source package could be responsibly changed for this band, but that version is not documented.

Use this shape when adding audience metadata to a catalog record:

```json
"audiences": [
  {"band": "middle-school", "status": "documented"},
  {"band": "high-school", "status": "adaptable"}
]
```

## GO contract

A **course package** is `GO` only when a competent facilitator can run the exact documented offering without inventing its learning sequence, materials plan, or assessment approach. The package must include equivalent material for:

- orientation: audience, duration, purpose, and a quick start;
- teaching sequence: session plans or an explicit scope and sequence;
- facilitation: setup, pacing, safety, and common-stuck guidance;
- materials: tote/BOM and room or device requirements;
- learner work: prompts, cards, handouts, or clearly stated build directions;
- evidence: assessment, reflection, or observable completion criteria;
- communication: a public-facing description suitable for a partner or family.

A **short workshop** may meet the same contract in a smaller shape: run sheet, materials/setup, participant artifact/prompt, facilitator notes, and completion/reflection check.

`GO-P` meets the package contract but has mandatory site-specific preflight such as accounts, device compatibility, machine calibration, safety approval, or an experienced technical lead.

## Other readiness states

- `ADAPT`: source is strong; the claimed audience or offering shape is not packaged.
- `PILOT`: a lead facilitator can plausibly deliver it, but package gaps remain.
- `NO`: no responsible delivery claim yet.

Only `GO` and `GO-P` may appear in a public-ready shelf by default.

## What the catalog records

`catalog/menu.json` is canonical for offering title, audience claim, screen load, equipment burden, readiness, preflight, and source paths. Generated menus are views; do not edit them by hand.

Keep package-specific details beside the package. Add a field to catalog data only when it is needed to select, deploy, or verify an offering across sites.

## Validation boundary

The current generator validates source paths and readiness vocabulary. Add artifact-level readiness validation only after two or more ready packages use the same stable file contract; do not force a single folder layout onto the historical archive first.
