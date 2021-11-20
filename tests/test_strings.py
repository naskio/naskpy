import unittest
from naskpy.strings import split_url


class StringsTestCase(unittest.TestCase):
    def test_split_url(self):
        url = "https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png?key=value"
        self.assertEqual(split_url(url), ("googlelogo_color_272x92dp.png", "googlelogo_color_272x92dp", "png"))


if __name__ == '__main__':
    unittest.main()
