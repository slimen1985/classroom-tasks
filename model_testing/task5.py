import unittest


def get_sum(a, b):
    return a + b


def get_sub(a, b):
    return a - b


def get_mult(a, b):
    return a * b


def get_div(a, b):
    if b == 0:
        raise ZeroDivisionError("b value should not be equal 0")
    return a / b


class UtilstestCase(unittest.TestCase):

    def test_get_sum(self):
        val1 = 3
        val2 = 4
        result = get_sum(val1, val2)
        self.assertEqual(result, val1 + val2)
        self.assertIsInstance(result, int)

    def test_get_sub(self):
        val1 = 6
        val2 = 4
        result = get_sub(val1, val2)
        self.assertEqual(result, val1 - val2)

    def test_get_mult(self):
        val1 = 4
        val2 = 4
        result = get_mult(val1, val2)
        self.assertEqual(result, val1 * val2)

    def test_get_div(self):
        val1 = 8
        val2 = 2
        result = get_div(val1, val2)
        self.assertEqual(result, val1 / val2)

    def test_get_div_zero(self):
        with self.assertRaises(ValueError):
            get_div(0, 20)



