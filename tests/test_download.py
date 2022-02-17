import unittest
from pathlib import Path
import shutil

from naskpy.download import g_download_multiple, download, download_multiple

BASE_DIR = Path(__file__).parent.absolute()
TEST_DIR = BASE_DIR / "testing_data" / 'download'


class DownloadTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.dir = TEST_DIR
        if not cls.dir.exists():
            cls.dir.mkdir(parents=True)

    def test_g_download_multiple(self):
        urls = [
            "https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png",
            "https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png",
            "https://www.google.com/images/branding/googlelogo/2x/sadasdas.png",
        ]
        filepaths = [
            self.dir / 'gd_1.png',
            self.dir / 'gd_2.png',
            self.dir / 'gd_3.png',
        ]
        expected = [
            True,
            True,
            False,
        ]
        g_download_multiple(urls, filepaths)
        for i in range(len(urls)):
            self.assertEqual(expected[i], filepaths[i].exists())

    def test_download(self):
        urls = [
            "https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png",
            "https://www.google.com/images/branding/googlelogo/2x/sadasdas.png",
        ]
        filepaths = [
            self.dir / 'd_1.png',
            self.dir / 'd_2.png',
        ]
        expected = [
            True,
            False,
        ]
        for i in range(len(urls)):
            download(urls[i], filepaths[i])
            self.assertEqual(expected[i], filepaths[i].exists())

    def test_download_multiple(self):
        urls = [
            "https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png",
            "https://www.google.com/images/branding/googlelogo/2x/sadasdas.png",
        ]
        filepaths = [
            self.dir / 'dm_1.png',
            self.dir / 'dm_2.png',
        ]
        expected = [
            True,
            False,
        ]
        download_multiple(urls, filepaths)
        for i in range(len(urls)):
            self.assertEqual(expected[i], filepaths[i].exists())

    @classmethod
    def tearDownClass(cls):
        if cls.dir.exists():
            shutil.rmtree(cls.dir)


if __name__ == "__main__":
    unittest.main()
