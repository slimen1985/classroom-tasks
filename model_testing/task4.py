import unittest


class UnitTestcase(unittest.TestCase):

    def test_example(self):
        self.assertGreater(20,10)
        self.assertGreaterEqual(20, 20)
        self.assertIsInstance(20, str)
        self.assertLess(10, 20)
        self.assertRegex("test test", r'^test')

        with self.assertRaises(TypeError):
            raise AssertionError