import json
import tempfile
import unittest
from pathlib import Path

from catalog.build_menu import render_menu, validate_menu


class ValidateMenuTest(unittest.TestCase):
    def test_rejects_an_offering_with_a_missing_repo_path(self):
        menu = {
            "offerings": [
                {
                    "offering_id": "missing-source",
                    "public_title": "Missing Source",
                    "age_bands": ["Adult"],
                    "formats": ["workshop"],
                    "screen_load": ["S0"],
                    "equipment": {"minimum_tier": "E0", "full_tier": "E0", "summary": "Handouts"},
                    "readiness": {"status": "GO", "note": "Ready"},
                    "repo_paths": ["does-not-exist"],
                    "preflight_required": [],
                    "public": True,
                }
            ]
        }
        with tempfile.TemporaryDirectory() as directory:
            menu_path = Path(directory) / "menu.json"
            menu_path.write_text(json.dumps(menu))
            errors = validate_menu(menu_path, Path(directory))

        self.assertIn("missing-source: missing source path: does-not-exist", errors)

    def test_rejects_an_unknown_readiness_status(self):
        menu = {
            "offerings": [
                {
                    "offering_id": "bad-status",
                    "public_title": "Bad Status",
                    "summary": "Test fixture.",
                    "age_bands": ["Adult"],
                    "formats": ["workshop"],
                    "screen_load": ["S0"],
                    "equipment": {"minimum_tier": "E0", "full_tier": "E0", "summary": "Handouts"},
                    "readiness": {"status": "MAYBE", "note": "Invalid"},
                    "repo_paths": [],
                    "preflight_required": [],
                    "public": False,
                }
            ]
        }
        with tempfile.TemporaryDirectory() as directory:
            menu_path = Path(directory) / "menu.json"
            menu_path.write_text(json.dumps(menu))
            errors = validate_menu(menu_path, Path(directory))

        self.assertIn("bad-status: unsupported readiness: MAYBE", errors)

    def test_renders_only_public_offerings_with_equipment_and_readiness(self):
        menu = {
            "offerings": [
                {
                    "offering_id": "ready",
                    "public_title": "Ready Workshop",
                    "summary": "A ready workshop.",
                    "age_bands": ["Adult"],
                    "formats": ["workshop"],
                    "screen_load": ["S1"],
                    "equipment": {"minimum_tier": "E1", "full_tier": "E2", "summary": "A tote"},
                    "readiness": {"status": "GO-P", "note": "Preflight accounts"},
                    "repo_paths": ["docs/ready"],
                    "preflight_required": ["accounts"],
                    "public": True,
                },
                {
                    "offering_id": "future",
                    "public_title": "Future Workshop",
                    "age_bands": ["Adult"],
                    "formats": ["workshop"],
                    "screen_load": ["S0"],
                    "equipment": {"minimum_tier": "E0", "full_tier": "E0", "summary": "Paper"},
                    "readiness": {"status": "PILOT", "note": "Not ready"},
                    "repo_paths": ["docs/future"],
                    "preflight_required": [],
                    "public": False,
                },
            ]
        }

        rendered = render_menu(menu)

        self.assertIn("Ready Workshop", rendered)
        self.assertIn("E1→E2", rendered)
        self.assertIn("GO-P", rendered)
        self.assertNotIn("Future Workshop", rendered)


if __name__ == "__main__":
    unittest.main()
