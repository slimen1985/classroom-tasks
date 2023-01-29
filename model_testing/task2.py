import unittest


def mult_by_20(values: int) -> int:
    return values * 20


class UserTestCase(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(2 + 2, 4)

    def test_multiply(self):
        self.assertTrue(3 * 3 == 9)

    def test_mult_by_20(self):
        value = 100
        self.assertEqual(mult_by_20(value), value * 20)

    def test_mult_20_wrong(self):
        value = 100
        self.assertNotEqual(mult_by_20(value), value * 30)

