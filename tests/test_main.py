import unittest

from naskpy.main import hello_world


class MainTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("setUpClass")

    def setUp(self):
        print("setUp")

    def test_hello_world(self):
        print("test_hello_world")
        self.assertEqual(hello_world(), "Hello world!")

    def test_hello_world_2(self):
        print("test_hello_world_2")
        self.assertNotEqual(hello_world(), "Hello world! 2")

    def tearDown(self):
        print("tearDown")

    @classmethod
    def tearDownClass(cls):
        print("tearDownClass")
