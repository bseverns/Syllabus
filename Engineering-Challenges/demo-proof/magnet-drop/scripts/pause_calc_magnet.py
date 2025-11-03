"""Pause layer calculator for magnet token.
Usage: python pause_calc_magnet.py --base 1.2 --mag 2.0 --layer 0.25
"""
import argparse
p = argparse.ArgumentParser()
p.add_argument('--base', type=float, required=True)
p.add_argument('--mag', type=float, required=True)
p.add_argument('--layer', type=float, required=True)
a = p.parse_args()
z = a.base + a.mag
layer_1 = int(round(z / a.layer))
print(f'Target Z_pause: {z:.3f} mm')
print('Pause at ~ layer (1-based):', layer_1)
print('Pause at ~ layer (0-based):', layer_1 - 1)
