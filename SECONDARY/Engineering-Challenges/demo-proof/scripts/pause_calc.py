"""Compute pause layer given Z and layer height.
Usage: python pause_calc.py --z 1.25 --layer 0.25
"""
import argparse
p = argparse.ArgumentParser()
p.add_argument('--z', type=float, required=True)
p.add_argument('--layer', type=float, required=True)
a = p.parse_args()
layer_1 = int(round(a.z / a.layer))
print('Pause at ~ layer (1-based):', layer_1)
print('Pause at ~ layer (0-based):', layer_1 - 1)
