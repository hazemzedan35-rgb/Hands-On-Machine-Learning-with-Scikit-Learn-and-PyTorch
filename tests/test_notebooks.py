"""Lightweight checks to keep starter notebooks valid and executable."""
from pathlib import Path
import unittest

import nbformat
from nbclient import NotebookClient

ROOT = Path(__file__).resolve().parents[1]
NOTEBOOKS = [
    ROOT / "days/day-01-ml-landscape/day_01_starter_lab.ipynb",
    ROOT / "days/day-02-challenges-validation/day_02_starter_lab.ipynb",
]


class NotebookTests(unittest.TestCase):
    def test_notebooks_have_valid_structure(self):
        for file in (ROOT / "days").glob("**/*.ipynb"):
            with self.subTest(file=file.name):
                nb = nbformat.read(file, as_version=4)
                nbformat.validate(nb)
                self.assertTrue(any(c.cell_type == "code" for c in nb.cells))

    def test_notebooks_execute(self):
        for file in NOTEBOOKS:
            with self.subTest(file=file.name):
                nb = nbformat.read(file, as_version=4)
                NotebookClient(
                    nb,
                    timeout=120,
                    kernel_name="python3",
                    resources={"metadata": {"path": str(file.parent)}},
                ).execute()


if __name__ == "__main__":
    unittest.main()
