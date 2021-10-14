from src.Figure import Figure
from src.utils import validate_size


class Triangle(Figure):
    name = 'Triangle'

    def __new__(cls, size_a, size_b, size_c):
        validate_size(size_a, size_b, size_c)
        if cls.check_triangle_existence(size_a, size_b, size_c):
            instance = super(Triangle, cls).__new__(cls)
            instance.size_a = size_a
            instance.size_b = size_b
            instance.size_c = size_c
            return instance

    @staticmethod
    def check_triangle_existence(size_a, size_b, size_c):
        condition_1 = size_a + size_b > size_c
        condition_2 = size_a + size_c > size_b
        condition_3 = size_b + size_c > size_a
        return all((condition_1, condition_2, condition_3))

    @property
    def area(self):
        p = sum((self.size_a, self.size_b, self.size_c)) / 2
        area_value = (p * (p - self.size_a) * (p - self.size_b) * (p - self.size_c))**0.5
        return area_value

    @property
    def perimeter(self):
        return sum((self.size_a, self.size_b, self.size_c))
