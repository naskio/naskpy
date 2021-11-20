import unittest
from naskpy.io import get_project_dir, split_path, get_parent_folder
from pathlib import Path

BASE_DIR = Path(__file__).parent.absolute()
TESTING_DATA = BASE_DIR / 'testing_data'


class IOTestCase(unittest.TestCase):
    def test_get_project_dir(self):
        self.assertEqual(BASE_DIR.parent.absolute(), get_project_dir())

    def test_get_base_path(self):
        p = TESTING_DATA / 'v.png'
        self.assertTupleEqual(split_path(p), ('v.png', 'v', 'png'))

    def test_get_parent_folder(self):
        p = TESTING_DATA / 'v.png'
        self.assertEqual(get_parent_folder(p), TESTING_DATA)


if __name__ == '__main__':
    unittest.main()
