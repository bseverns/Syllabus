"""Pause-layer calculator for magnet-drop demo.

Given base thickness, magnet thickness, and layer height,
compute the target Z and layer indices.

Usage:
  python scripts/pause_calc_magnet.py --base 1.2 --mag 2.0 --layer 0.25
"""
import argparse, math
p = argparse.ArgumentParser()
p.add_argument('--base', type=float, required=True, help='base thickness (mm)')
p.add_argument('--mag', type=float, required=True, help='magnet thickness (mm)')
p.add_argument('--layer', type=float, required=True, help='layer height (mm)')
a = p.parse_args()
z = a.base + a.mag
layer_1 = int(round(z / a.layer))
print(f'Target Z_pause: {z:.3f} mm')
print('Pause layer ~ (1-based):', layer_1)
print('Pause layer ~ (0-based):', layer_1 - 1)
