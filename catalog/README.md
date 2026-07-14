# Catalog and Menu

`index.json` is the archive index. `menu.json` is the smaller deployment-aware layer used to create a partner-facing workshop menu without flattening the archive into marketing claims.

## Menu fields

| Field | Use |
| --- | --- |
| `public_title` | Partner-facing experience name. |
| `repo_paths` | Exact source material to audit before delivery. |
| `screen_load` | S0–S4 participation screen-use label. |
| `equipment` | E0–E4 minimum/full deployment burden. |
| `readiness` | Documentation status, separate from equipment burden. |
| `preflight_required` | What must be confirmed locally before delivery. |
| `public` | `true` renders in `MENU.md`; `false` keeps a concept in the internal development queue. |

### Screen-load labels

- **S0 — Unplugged:** no participant screens.
- **S1 — Glimpse:** brief shared display or facilitator documentation.
- **S2 — Tool burst:** short paired programming, editing, or CAD use.
- **S3 — Mixed studio:** screens are a production tool for part of the session.
- **S4 — Screen studio:** software is the primary workspace; include critique and physical/social breaks.

### Equipment tiers

- **E0 — Tote:** handouts, cardboard, loose LEGO, markers, simple hand tools.
- **E1 — Powered tote:** batteries, LEDs, motors, small circuit kits, or a speaker.
- **E2 — Device lab:** ordinary laptops/Chromebooks, shared standard WLAN, accounts, and headphones.
- **E3 — Mobile technical lab:** specialized kits, microcontrollers, audio rigs, printers, or charging gear.
- **E4 — Temporary infrastructure:** flight zone, machine fleet, CNC, multi-station simulation, RF plan, or private WLAN.

### Documentation readiness

- **GO:** a competent facilitator can deliver the documented offering directly from the repo.
- **GO-P:** documentation supports delivery; local technical/site preflight is mandatory.
- **ADAPT:** a strong source exists, but this public version or age band is not yet documented.
- **PILOT:** credible for a lead facilitator, but gaps prevent a standard offering.
- **NO:** not enough repo support to list as an offering.

## Build and verify

```bash
python3 -m unittest discover -s tests -v
python3 catalog/build_menu.py --output catalog/MENU.md
```

The build validates every `repo_paths` value before writing the generated menu. Do not hand-edit `MENU.md`; edit `menu.json` and regenerate.
