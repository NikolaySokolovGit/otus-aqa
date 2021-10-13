from math import pi

from src.Figure import Figure


class Circle(Figure):
    def __init__(self, radius):
        self.radius = radius

    @property
    def area(self):
        return pi * self.radius**2

    @property
    def perimeter(self):
        return 2 * pi * self.radius
