# Single schematic (text) + build notes

This is the “core crusher”:
- Audio bias + buffer (MCP602)
- Clock (NE555) + cleanup (CD40106)
- Sample/hold (CD4051 + hold cap to Vref)
- Output buffer (MCP602)
- CV-controlled crush via NE555 pin 5 (CTRL)

For a pin-accurate netlist, see:
- [`schematic/netlist.md`](netlist.md)

> Teaching note: this is intentionally “the simple, robust version” for the AE 0–5V world.
> Extensions (4017 patterns, stepped depth, etc.) live in `extensions/`.
