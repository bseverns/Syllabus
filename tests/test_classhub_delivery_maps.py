import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]


def canonical_syllabi() -> list[Path]:
    return sorted(
        path
        for path in REPO_ROOT.rglob("*.md")
        if "syllabus" in path.name.lower()
        and "archive" not in path.parts
        and "in-progress" not in path.parts
        and not path.stem.lower().endswith("_enrichment")
    )


class ClassHubDeliveryMapTest(unittest.TestCase):
    def test_every_canonical_syllabus_has_a_classhub_delivery_map(self):
        missing = []
        malformed = []
        for path in canonical_syllabi():
            relative_path = str(path.relative_to(REPO_ROOT))
            text = path.read_text(encoding="utf-8")
            if "## ClassHub Delivery Map" not in text:
                missing.append(relative_path)
                continue
            section = text.split("## ClassHub Delivery Map", 1)[1].split("\n## ", 1)[0]
            if "ClassHub materials" not in section or "| --- |" not in section:
                malformed.append(relative_path)

        self.assertEqual(missing, [])
        self.assertEqual(malformed, [])


if __name__ == "__main__":
    unittest.main()
