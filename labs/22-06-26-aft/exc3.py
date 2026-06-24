# create an abstract class for shapes
# area, perimiter

from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimiter(self) -> float:
        pass


class Square(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimiter(self):
        return 2 * (self.length + self.width)


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return pi * self.radius**2

    def perimiter(self) -> float:
        return 2 * pi * self.radius


square = Square(4, 5)
circle = Circle(4)

print(square.area())

print(circle.area())
