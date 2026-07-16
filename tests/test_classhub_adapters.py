import json
import tempfile
import unittest
from pathlib import Path

from catalog.validate_classhub_adapters import validate_adapter, validate_cataloged_adapters


REPO_ROOT = Path(__file__).resolve().parents[1]
EXPECTED_ADAPTER_PATHS = {
    "PRIMARY/3D-Printing-Course-3-5/classhub_import",
    "PRIMARY/Build_Your_Block/classhub_import",
    "SECONDARY/AI_in_Your_Feed/classhub_import",
    "SECONDARY/ExplorationSoundDesign/classhub_import",
    "SECONDARY/ai-at-work/classhub_import",
    "SECONDARY/digital-imaging-lab/classhub_import",
}


def write_adapter(root: Path, teacher: str, public: str) -> dict:
    adapter = root / "course/classhub_import"
    adapter.mkdir(parents=True)
    (adapter / "teacher_plan_classhub.md").write_text(teacher)
    (adapter / "public_overview_classhub.md").write_text(public)
    return {
        "offering_id": "fixture",
        "age_bands": ["High school"],
        "classhub_import_path": "course/classhub_import",
    }


PUBLIC_FIXTURE = """# Fixture Course

Course slug: fixture_course
Grade level: 9th-12th
Total sessions: 1
"""


class ClassHubAdapterCompatibilityTest(unittest.TestCase):
    def test_all_six_cataloged_adapters_are_compatible(self):
        menu = json.loads((REPO_ROOT / "catalog/menu.json").read_text())
        paths = {
            offering["classhub_import_path"]
            for offering in menu["offerings"]
            if offering.get("classhub_import_path")
        }
        self.assertEqual(EXPECTED_ADAPTER_PATHS, paths)
        self.assertEqual(
            [],
            validate_cataloged_adapters(REPO_ROOT / "catalog/menu.json", REPO_ROOT),
        )

    def test_accepts_corrected_optional_section_formats(self):
        teacher = """# Fixture Teacher Plan

Course slug: fixture_course
Grade level: 9th-12th
Total sessions: 1

# Session 01: Test and Share
Lesson slug (for course.yaml): s01-explicit-evidence
Mission: Test one change.

Submission
- Type: file
- Accepted: .pdf, .png
- Naming: evidence-v1.pdf

ClassHub materials
- Checklist | Test checklist | Change one thing; Retest the same condition
- Reflection | Exit reflection | What evidence changed your mind?
- Rubric | Evidence rubric | Clear claim; Specific evidence | 5
- Gallery | Share image | .png,.jpg | 12

Offline handout
- Goal: Test one change.
- Spanish goal: Reviewed localized goal wording.
- Somali do now: Reviewed localized do-now wording.
- Sgaw Karen submit: Reviewed localized submission wording.
"""
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            offering = write_adapter(root, teacher, PUBLIC_FIXTURE)
            self.assertEqual([], validate_adapter(offering, root))

    def test_rejects_duplicate_or_malformed_explicit_slugs(self):
        teacher = """# Fixture Teacher Plan

Course slug: fixture_course
Grade level: 9th-12th
Total sessions: 2

# Session 01: First
Lesson slug (for course.yaml): s01-duplicate

# Session 02: Second
Lesson slug (for course.yaml): s01-duplicate
"""
        public = PUBLIC_FIXTURE.replace("Total sessions: 1", "Total sessions: 2")
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            offering = write_adapter(root, teacher, public)
            errors = validate_adapter(offering, root)

        self.assertIn(
            "fixture: explicit Lesson slug does not match Session 02: s01-duplicate",
            errors,
        )
        self.assertIn("fixture: duplicate explicit Lesson slug: s01-duplicate", errors)

    def test_accepts_a_slug_on_body_line_40_and_rejects_one_on_line_41(self):
        body_prefix = "\n".join(f"Line {line_number}" for line_number in range(1, 40))
        teacher = f"""# Fixture Teacher Plan

Course slug: fixture_course
Grade level: 9th-12th
Total sessions: 2

# Session 01: In Window
{body_prefix}
Lesson slug (for course.yaml): s01-in-window

# Session 02: Too Late
{body_prefix}
Line 40
Lesson slug (for course.yaml): s02-too-late
"""
        public = PUBLIC_FIXTURE.replace("Total sessions: 1", "Total sessions: 2")
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            offering = write_adapter(root, teacher, public)
            errors = validate_adapter(offering, root)

        self.assertEqual(
            [
                "fixture: Session 02 has explicit Lesson slug after ClassHub's "
                "40-line metadata window (body line 41)"
            ],
            errors,
        )

    def test_rejects_classhub_path_traversal_and_absolute_paths(self):
        with tempfile.TemporaryDirectory() as directory:
            parent = Path(directory)
            repo_root = parent / "repo"
            outside_root = parent / "outside"
            repo_root.mkdir()
            offering = write_adapter(outside_root, "", "")

            offering["classhub_import_path"] = "../outside/course/classhub_import"
            self.assertEqual(
                [
                    "fixture: classhub_import_path escapes repository: "
                    "../outside/course/classhub_import"
                ],
                validate_adapter(offering, repo_root),
            )

            offering["classhub_import_path"] = str(outside_root / "course/classhub_import")
            self.assertEqual(
                [
                    "fixture: classhub_import_path must be relative: "
                    f"{outside_root / 'course/classhub_import'}"
                ],
                validate_adapter(offering, repo_root),
            )

    def test_rejects_an_adapter_directory_symlink_that_escapes_the_repo(self):
        with tempfile.TemporaryDirectory() as directory:
            parent = Path(directory)
            repo_root = parent / "repo"
            outside_root = parent / "outside"
            repo_root.mkdir()
            write_adapter(outside_root, "", "")
            (repo_root / "linked-adapter").symlink_to(outside_root / "course/classhub_import")
            offering = {
                "offering_id": "fixture",
                "age_bands": ["High school"],
                "classhub_import_path": "linked-adapter",
            }

            self.assertEqual(
                ["fixture: classhub_import_path escapes repository: linked-adapter"],
                validate_adapter(offering, repo_root),
            )

    def test_rejects_a_required_file_symlink_that_escapes_the_repo(self):
        with tempfile.TemporaryDirectory() as directory:
            parent = Path(directory)
            repo_root = parent / "repo"
            adapter = repo_root / "course/classhub_import"
            adapter.mkdir(parents=True)
            outside_teacher = parent / "teacher_plan_classhub.md"
            outside_teacher.write_text("outside")
            (adapter / "teacher_plan_classhub.md").symlink_to(outside_teacher)
            (adapter / "public_overview_classhub.md").write_text(PUBLIC_FIXTURE)
            offering = {
                "offering_id": "fixture",
                "age_bands": ["High school"],
                "classhub_import_path": "course/classhub_import",
            }

            self.assertEqual(
                [
                    "fixture: classhub_import_path file escapes repository: "
                    "course/classhub_import/teacher_plan_classhub.md"
                ],
                validate_adapter(offering, repo_root),
            )

    def test_resolves_a_caller_supplied_relative_menu_from_repo_root(self):
        with tempfile.TemporaryDirectory() as directory:
            repo_root = Path(directory)
            menu_path = repo_root / "config/menu.json"
            menu_path.parent.mkdir()
            menu_path.write_text(json.dumps({"offerings": []}))

            self.assertEqual(
                [],
                validate_cataloged_adapters(Path("config/menu.json"), repo_root),
            )

    def test_rejects_a_caller_supplied_menu_that_escapes_the_repo(self):
        with tempfile.TemporaryDirectory() as directory:
            parent = Path(directory)
            repo_root = parent / "repo"
            repo_root.mkdir()
            (parent / "menu.json").write_text(json.dumps({"offerings": []}))

            self.assertEqual(
                ["menu path escapes repository: ../menu.json"],
                validate_cataloged_adapters(Path("../menu.json"), repo_root),
            )

    def test_rejects_an_adapter_age_band_outside_the_catalog_audience(self):
        teacher = """# Fixture Teacher Plan

Course slug: fixture_course
Grade level: 3rd-5th
Total sessions: 1

# Session 01: First
Lesson slug (for course.yaml): s01-first
"""
        public = PUBLIC_FIXTURE.replace("9th-12th", "3rd-5th")
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            offering = write_adapter(root, teacher, public)
            errors = validate_adapter(offering, root)

        self.assertIn(
            "fixture: teacher plan audience '3rd-5th' is outside catalog age_bands",
            errors,
        )
        self.assertIn(
            "fixture: public overview audience '3rd-5th' is outside catalog age_bands",
            errors,
        )

    def test_rejects_malformed_optional_labels_and_rows(self):
        teacher = """# Fixture Teacher Plan

Course slug: fixture_course
Grade level: 9th-12th
Total sessions: 1

# Session 01: First
Lesson slug (for course.yaml): s01-first

Classhub materials
- Worksheet | Missing contract | body

Offline handout
- Karen goal: Invented wording
"""
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            offering = write_adapter(root, teacher, PUBLIC_FIXTURE)
            errors = validate_adapter(offering, root)

        self.assertIn("fixture: line 10: use section label 'ClassHub materials'", errors)
        self.assertIn(
            "fixture: line 11: unsupported ClassHub material type: Worksheet",
            errors,
        )
        self.assertIn(
            "fixture: line 14: malformed localized Offline handout line",
            errors,
        )


if __name__ == "__main__":
    unittest.main()
