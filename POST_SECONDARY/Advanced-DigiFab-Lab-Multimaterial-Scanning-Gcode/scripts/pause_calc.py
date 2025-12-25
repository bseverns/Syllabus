"""Compute pause layer given target Z and layer height.

Usage:
  python scripts/pause_calc.py --z 1.25 --layer 0.25

Outputs:
  Layer index to pause at (0-based and 1-based forms).
"""
import argparse, math
p = argparse.ArgumentParser()
p.add_argument('--z', type=float, required=True, help='target height in mm')
p.add_argument('--layer', type=float, required=True, help='layer height in mm')
args = p.parse_args()
layer_1based = int(round(args.z / args.layer))
print('Pause at ~ layer (1-based):', layer_1based)
print('Pause at ~ layer (0-based):', layer_1based - 1)
