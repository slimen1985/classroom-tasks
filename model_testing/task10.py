import sys
import unittest


class TestSkip(unittest.TestCase):

    @unittest.skip("Skip this function")
    def test_skipped(self):
        self.fail("This function should be skipped")

    @unittest.skipIf(sys.version_info.major < 2, "Skip if python version less than 2")
    def test_version(self):
        print("This test ran")

    @unittest.skipUnless(sys.platform.startswith("win"), "Skip due to OS name")
    def test_function(self):
        print("This test ran")
