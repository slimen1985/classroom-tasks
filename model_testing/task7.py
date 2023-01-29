import unittest
from unittest.mock import Mock


class SimpleClass:
    def __init__(self):
        self.value = 1

    def return_value(self):
        return self.value


class TestSimpleClass(unittest.TestCase):

    def setUp(self) -> None:
        self.simple_class = SimpleClass()
        self.simple_class.return_value = Mock(side_effect=lambda x: x + 1)

    def test_return_value(self):
        self.assertEqual(self.simple_class.return_value(1), 2)