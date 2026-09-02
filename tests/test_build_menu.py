import json
import re
import tempfile
import unittest
from pathlib import Path
from urllib.parse import unquote

from catalog.build_menu import render_menu, validate_menu


REPO_ROOT = Path(__file__).parents[1]


def broken_local_markdown_links(root: Path) -> list[str]:
    # ponytail: inline links only; use a Markdown parser if reference links need enforcement.
    broken = []
    for markdown_path in root.rglob("*.md"):
        for line_number, line in enumerate(markdown_path.read_text(errors="replace").splitlines(), 1):
            for target in re.findall(r"(?<!!)\[[^\]]*\]\(([^)]+)\)", line):
                target = target.strip("<>")
                if target.startswith(("http://", "https://", "mailto:", "tel:", "#", "data:")):
                    continue
                target = unquote(target.split("#", 1)[0])
                if target and not (markdown_path.parent / target).exists():
                    broken.append(f"{markdown_path.relative_to(root)}:{line_number} -> {target}")
    return broken


class ValidateMenuTest(unittest.TestCase):
    def test_build_together_pilot_is_packaged_and_cataloged(self):
        package = REPO_ROOT / "FAMILIES/Build-Together"
        self.assertTrue((package / "README.md").is_file())
        self.assertTrue((package / "SYLLABUS.md").is_file())

        menu = json.loads((REPO_ROOT / "catalog/menu.json").read_text())
        offering = next(item for item in menu["offerings"] if item["offering_id"] == "build-together-family")
        self.assertEqual(offering["readiness"]["status"], "PILOT")
        self.assertFalse(offering["public"])
        self.assertEqual(offering["repo_paths"], ["FAMILIES/Build-Together"])

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

    def test_rejects_a_repo_path_outside_the_repository(self):
        menu = {
            "offerings": [
                {
                    "offering_id": "outside-source",
                    "readiness": {"status": "GO"},
                    "repo_paths": ["../outside-source.md"],
                    "public": False,
                }
            ]
        }
        with tempfile.TemporaryDirectory() as directory:
            parent = Path(directory)
            repo_root = parent / "repo"
            repo_root.mkdir()
            (parent / "outside-source.md").touch()
            menu_path = repo_root / "menu.json"
            menu_path.write_text(json.dumps(menu))
            errors = validate_menu(menu_path, repo_root)

        self.assertIn("outside-source: source path escapes repository: ../outside-source.md", errors)

    def test_rejects_an_absolute_repo_path(self):
        with tempfile.TemporaryDirectory() as directory:
            repo_root = Path(directory)
            source_path = repo_root / "source.md"
            source_path.touch()
            menu = {
                "offerings": [
                    {
                        "offering_id": "absolute-source",
                        "readiness": {"status": "GO"},
                        "repo_paths": [str(source_path)],
                        "public": False,
                    }
                ]
            }
            menu_path = repo_root / "menu.json"
            menu_path.write_text(json.dumps(menu))
            errors = validate_menu(menu_path, repo_root)

        self.assertIn(f"absolute-source: source path must be relative: {source_path}", errors)

    def test_rejects_a_repo_symlink_that_escapes_the_repository(self):
        menu = {
            "offerings": [
                {
                    "offering_id": "symlink-source",
                    "readiness": {"status": "GO"},
                    "repo_paths": ["linked-source.md"],
                    "public": False,
                }
            ]
        }
        with tempfile.TemporaryDirectory() as directory:
            parent = Path(directory)
            repo_root = parent / "repo"
            repo_root.mkdir()
            outside_source = parent / "outside-source.md"
            outside_source.touch()
            (repo_root / "linked-source.md").symlink_to(outside_source)
            menu_path = repo_root / "menu.json"
            menu_path.write_text(json.dumps(menu))
            errors = validate_menu(menu_path, repo_root)

        self.assertIn("symlink-source: source path escapes repository: linked-source.md", errors)

    def test_rejects_an_invalid_classhub_import_path(self):
        menu = {
            "offerings": [
                {
                    "offering_id": "bad-classhub-path",
                    "readiness": {"status": "GO"},
                    "repo_paths": [],
                    "classhub_import_path": "../classhub_import",
                    "public": False,
                }
            ]
        }
        with tempfile.TemporaryDirectory() as directory:
            repo_root = Path(directory) / "repo"
            repo_root.mkdir()
            menu_path = repo_root / "menu.json"
            menu_path.write_text(json.dumps(menu))
            errors = validate_menu(menu_path, repo_root)

        self.assertIn(
            "bad-classhub-path: classhub_import_path escapes repository: ../classhub_import",
            errors,
        )

    def test_rejects_a_classhub_import_directory_missing_required_files(self):
        menu = {
            "offerings": [
                {
                    "offering_id": "incomplete-classhub-adapter",
                    "readiness": {"status": "GO"},
                    "repo_paths": [],
                    "classhub_import_path": "course/classhub_import",
                    "public": False,
                }
            ]
        }
        with tempfile.TemporaryDirectory() as directory:
            repo_root = Path(directory)
            adapter_path = repo_root / "course/classhub_import"
            adapter_path.mkdir(parents=True)
            (adapter_path / "teacher_plan_classhub.md").touch()
            menu_path = repo_root / "menu.json"
            menu_path.write_text(json.dumps(menu))
            errors = validate_menu(menu_path, repo_root)

        self.assertIn(
            "incomplete-classhub-adapter: classhub_import_path missing "
            "public_overview_classhub.md: course/classhub_import",
            errors,
        )

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

    def test_rejects_duplicate_offering_ids(self):
        offering = {
            "offering_id": "duplicate",
            "readiness": {"status": "GO"},
            "repo_paths": [],
            "public": False,
        }
        menu = {"offerings": [offering, offering]}
        with tempfile.TemporaryDirectory() as directory:
            menu_path = Path(directory) / "menu.json"
            menu_path.write_text(json.dumps(menu))
            errors = validate_menu(menu_path, Path(directory))

        self.assertIn("duplicate: duplicate offering_id", errors)

    def test_rejects_public_offerings_that_are_not_ready(self):
        menu = {
            "offerings": [
                {
                    "offering_id": "pilot",
                    "readiness": {"status": "PILOT"},
                    "repo_paths": [],
                    "public": True,
                }
            ]
        }
        with tempfile.TemporaryDirectory() as directory:
            menu_path = Path(directory) / "menu.json"
            menu_path.write_text(json.dumps(menu))
            errors = validate_menu(menu_path, Path(directory))

        self.assertIn("pilot: public offerings must be GO or GO-P", errors)

    def test_rejects_unknown_screen_and_equipment_labels(self):
        menu = {
            "offerings": [
                {
                    "offering_id": "bad-labels",
                    "screen_load": ["S5"],
                    "equipment": {"minimum_tier": "E0", "full_tier": "E5"},
                    "readiness": {"status": "GO"},
                    "repo_paths": [],
                    "public": False,
                }
            ]
        }
        with tempfile.TemporaryDirectory() as directory:
            menu_path = Path(directory) / "menu.json"
            menu_path.write_text(json.dumps(menu))
            errors = validate_menu(menu_path, Path(directory))

        self.assertIn("bad-labels: unsupported screen load: S5", errors)
        self.assertIn("bad-labels: unsupported equipment tier: E5", errors)

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

    def test_checked_in_menu_matches_generated_menu(self):
        menu = json.loads((REPO_ROOT / "catalog/menu.json").read_text())
        self.assertEqual((REPO_ROOT / "catalog/MENU.md").read_text(), render_menu(menu))

    def test_checked_in_menu_validates(self):
        self.assertEqual([], validate_menu(REPO_ROOT / "catalog/menu.json", REPO_ROOT))

    def test_repository_has_no_broken_local_markdown_links(self):
        self.assertEqual([], broken_local_markdown_links(REPO_ROOT))


if __name__ == "__main__":
    unittest.main()
