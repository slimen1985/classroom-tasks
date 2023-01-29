class Figure:
    def __init__(self, shape):
        self.__shape = shape

    @property
    def shape(self):
        return self.__shape

    def get_square(self):
        pass


class Rectangle(Figure):
    def __init__(self, shape, length, height):
        super().__init__(shape)
        self.__length = length
        self.__height = height

    @property
    def length(self):
        return self.__length

    @property
    def height(self):
        return self.__height

    def get_square(self):
        return self.__length * self.__height


rectangle = Rectangle("rectangle", 8, 5)
try:
    print(rectangle.get_square())
except TypeError as err:
    print(f"An error {err} raised")
else:
    print("Success!")