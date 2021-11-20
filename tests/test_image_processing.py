import unittest
from pathlib import Path
from PIL import Image
from naskpy.image_processing import resize_by_width, resize_by_height, to_square, resize, get_remote_image
from naskpy.io import split_path

BASE_DIR = Path(__file__).parent.absolute()
TESTING_DATA = BASE_DIR / 'testing_data'


class ImageProcessingTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.imageH = Image.open(TESTING_DATA / 'h.png')
        cls.imageV = Image.open(TESTING_DATA / 'v.png')
        cls.imageSquare = Image.open(TESTING_DATA / 'vh.png')

    def test_preconditions(self):
        # horizontal
        self.assertEqual(self.imageH.size[0], 500)
        self.assertNotEqual(self.imageH.size[1], 500)
        # vertical
        self.assertNotEqual(self.imageV.size[0], 500)
        self.assertEqual(self.imageV.size[1], 500)
        # square
        self.assertTupleEqual(self.imageSquare.size, (500, 500))

    def test_resize_by_width(self):
        nw_s = [250, 750]
        for nw in nw_s:
            image_resized = resize_by_width(self.imageH, nw)
            self.assertEqual(image_resized.size[0], nw)
            self.assertNotEqual(image_resized.size[1], nw)

    def test_resize_by_height(self):
        nh_s = [250, 750]
        for nh in nh_s:
            image_resized = resize_by_height(self.imageV, nh)
            self.assertNotEqual(image_resized.size[0], nh)
            self.assertEqual(image_resized.size[1], nh)

    def test_to_square(self):
        side_length = [250, 500, 750]
        images = [self.imageSquare, self.imageV, self.imageH]
        ccs = [True, False]
        for image in images:
            for sl in side_length:
                for cc in ccs:
                    image_squared = to_square(image, sl, fill_color=(255, 255, 255, 0),
                                              center_crop=cc)  # white background
                    self.assertTupleEqual(image_squared.size, (sl, sl))

    def test_resize(self):
        sizes = [(250, 100), (500, 500), (750, 1000)]
        images = [self.imageSquare, self.imageV, self.imageH]
        ccs = [True, False]
        for image in images:
            for s in sizes:
                for cc in ccs:
                    image_resized = resize(image, s, crop=cc, position=('top', 'left'))
                    self.assertTupleEqual(image_resized.size, s)

    def test_get_remote_image(self):
        url = 'https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png'
        image = get_remote_image(url)
        self.assertIsInstance(image, Image.Image)
        self.assertTupleEqual(image.size, (544, 184))


if __name__ == '__main__':
    unittest.main()
