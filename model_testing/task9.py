import unittest
import unittest.mock
from unittest.mock import patch


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


class UserUnitTest(unittest.TestCase):

    @unittest.mock.patch('task9.get_sum')
    def test_sum_values(self, mocked_sum):
        get_sum(10, 20)
        self.assertTrue(mocked_sum.called)

    @unittest.mock.patch('task9.get_sum')
    def test_sum_values_called_with(self, mocked_sum):
        get_sum(10, 20)
        self.assertTrue(mocked_sum.called)
        self.assertEqual(mocked_sum.call_count, 1)
        #Функция вызывалась со значениями 10, 20
        mocked_sum.assert_called_with(10, 20)

    @unittest.mock.patch('task9.get_sum')
    def test_reset_mock(self, mocked_sum):
        get_sum(10, 20)
        get_sum(10, 20)
        #Функция вызывалась 2 раза
        self.assertTrue(mocked_sum.called)
        self.assertEqual(mocked_sum.call_count, 2)

        mocked_sum.assert_called()
        # Функция вызывалась со значениями 10, 20
        mocked_sum.assert_called_with(10, 20)

        # Сбрасывает вызов функции
        mocked_sum.reset_mock()

        self.assertEqual(mocked_sum.call_count, 0)
        self.assertFalse(mocked_sum.called)

    @unittest.mock.patch('task9.get_sum', return_value=30)
    def test_mock_return_val(self, mocked_sum):
        res1 = get_sum(10, 20)
        res2 = get_sum(10, 20)

        self.assertEqual(res2, 30)
