"""Torque calculator.
Usage:
  python scripts/torque_from_mass.py --radius_mm 100 --mass_g 200
"""
import argparse
p = argparse.ArgumentParser()
p.add_argument('--radius_mm', type=float, required=True)
p.add_argument('--mass_g', type=float, required=True)
a = p.parse_args()
torque_Nm = (a.radius_mm/1000.0) * (a.mass_g/1000.0) * 9.81
print(f'Torque ≈ {torque_Nm:.3f} N·m')
