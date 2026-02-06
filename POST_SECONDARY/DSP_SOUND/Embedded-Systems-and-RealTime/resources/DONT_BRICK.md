# Don’t Brick the Device (configuration + persistence)

- Always validate config before applying.
- Save atomically (write whole struct; verify checksum if possible).
- Version configs; migrate forward.
- Keep a hardware “recovery” path:
  - hold a button on boot → safe mode
  - safe mode ignores user mappings and uses defaults
- Always keep a factory reset that works offline.
