// Dimension Token Template
// Target Lunch Labs / createMPLS
// Units are millimeters.

// Main dimensions
width = 30;
depth = 18;
thickness = 3;

// Raised label settings
label_text = "TGT";   // Keep it short: 1-3 letters works best.
label_height = 0.9;
label_size = 8;

// Optional hole settings
use_hole = true;
hole_diameter = 4;
hole_center_from_edge = 5;

$fn = 48;

module token_base() {
    cube([width, depth, thickness], center = false);
}

module tag_hole() {
    translate([hole_center_from_edge, depth/2, -0.5])
        cylinder(h = thickness + 1, d = hole_diameter, center = false);
}

module raised_label() {
    translate([width/2, depth/2, thickness])
        linear_extrude(height = label_height)
            text(label_text, size = label_size, halign = "center", valign = "center");
}

// Final object
if (use_hole) {
    difference() {
        token_base();
        tag_hole();
    }
    raised_label();
} else {
    token_base();
    raised_label();
}
