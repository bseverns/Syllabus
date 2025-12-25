/*
  Magnet-Token with Encapsulated Pocket (for pause-and-drop)
  - Print base up to pocket top, pause, drop magnet, resume to encapsulate.
  - Defaults for 10x2 mm magnet; adjust params to match.
*/

// === Parameters ===
token_d     = 40;     // mm outer diameter
base_t      = 1.2;    // mm base thickness under magnet
magnet_d    = 10.0;   // mm magnet diameter
magnet_t    = 2.0;    // mm magnet thickness
cover_t     = 1.0;    // mm printed cover over magnet (>= 3 layers @ 0.32 for 0.5 nozzle; adjust)
clearance   = 0.25;   // radial clearance for pocket (diameter grows by 2*clearance)
chamfer_t   = 0.4;    // small top edge break
$fn = 120;

// Derived
token_h = base_t + magnet_t + cover_t;
pocket_r = (magnet_d/2) + clearance;

// Model: cylinder minus a cylindrical pocket from z=base_t to z=base_t+magnet_t
module token(){
  difference(){
    // main body with a light top chamfer
    minkowski(){
      cylinder(h=token_h - chamfer_t, r=token_d/2 - chamfer_t);
      cylinder(h=chamfer_t, r=chamfer_t);
    }
    // pocket void (centered)
    translate([0,0,base_t])
      cylinder(h=magnet_t + 0.001, r=pocket_r);
  }
}

token();

// Print-time notes:
// - Pause at layer where Z >= base_t + magnet_t (e.g., Z_pause = base_t + magnet_t).
// - Ensure magnet sits fully below that Z before resuming so nozzle won't strike it.
