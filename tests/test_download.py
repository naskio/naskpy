import unittest
from pathlib import Path
import shutil

from naskpy.download import g_download_multiple, download

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
        ]
        filepaths = [
            self.dir / 'g_1.png',
            self.dir / 'g_2.png',
        ]
        g_download_multiple(urls, filepaths)
        for filepath in filepaths:
            self.assertTrue(filepath.exists())

    def test_download(self):
        url = "https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png"
        path = self.dir / "d.png"
        download(url, path)
        self.assertTrue(path.exists())

    @classmethod
    def tearDownClass(cls):
        if cls.dir.exists():
            shutil.rmtree(cls.dir)


if __name__ == "__main__":
    unittest.main()
