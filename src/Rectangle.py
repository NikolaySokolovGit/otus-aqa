from src.Figure import Figure


class Rectangle(Figure):
    def __init__(self, size_a, size_b):
        super().__init__(size_a, size_b)
        self.size_a = size_a
        self.size_b = size_b

    @property
    def area(self):
        return self.size_a * self.size_b

    @property
    def perimeter(self):
        return self.size_a * 2 + self.size_b * 2
