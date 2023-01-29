import unittest
from unittest.mock import Mock


def get_word(text: str) -> str|list:
    if " " in text:
        return text.split()
    return text.upper()


class TestGetWords(unittest.TestCase):

    def test_string_processing(self):
        text = "bar"
        self.assertEqual(get_word(text), text.upper())
        self.assertTrue(text.upper())

    def test_string_processing_list(self):
        text_ = " Hi world"
        self.assertIsInstance(get_word(text_), list)



