"""Compute compound gear ratios from pairs.
Usage:
  python scripts/gear_ratio_calc.py 12:36 10:40
Outputs overall ratio (driver:driven).
"""
import sys
ratio = 1.0
pairs = []
for arg in sys.argv[1:]:
  a,b = arg.split(':')
  a,b = float(a), float(b)
  ratio *= (b/a)
  pairs.append((a,b))
print('Pairs:', pairs)
print('Overall ratio (driven/driver):', ratio)
