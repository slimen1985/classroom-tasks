import unittest
import datetime


class UserTestCase(unittest.TestCase):
    def setUp(self) -> None:
        print("setUp")
        self.current_time = datetime.datetime.now()

    @classmethod
    def setUpClass(cls) -> None:
        print("setUpClass")
        cls.current_time_cls = datetime.datetime.now()

    def tearDown(self) -> None:
        print("tearDown")

    @classmethod
    def tearDownClass(cls) -> None:
        print("tearDownClass")

    def test_example_1(self):
        print("example_1")
        print(self.current_time)
        print(self.current_time_cls)

    def test_example_2(self):
        print("example_2")
        print(self.current_time)
        print(self.current_time_cls)
