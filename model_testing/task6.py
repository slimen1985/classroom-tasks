import unittest

class Car:
    def __init__(self, brand):
        self.__brand = brand
        self.__speed_map = {
            "BMW": 300,
            "Nissan": 250,
        }
        self.__speed = self.__get_speed()

    def __get_speed(self):
        return self.__speed_map.get(self.__brand, 0)

    def get_time(self, dist: int) -> float:
        return dist / self.__speed


# car = Car("BMW")
# time_ = car.get_time(300)
# print(time_)


class TestCar(unittest.TestCase):

    def setUp(self) -> None:
        car_name = "Nissan"
        test_car = "Opel"
        self.car_test = Car(test_car)
        self.car = Car(car_name)

    def test_get_time(self):
        dist = 250
        self.assertEqual(self.car.get_time(dist), 1.0)
        self.assertIsInstance(self.car.get_time(dist), float)

    def test_get_time_zero(self):
        dist = 300
        with self.assertRaises(ZeroDivisionError):
            self.car_test.get_time(dist)


