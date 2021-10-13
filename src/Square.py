from src.Figure import Figure


class Square(Figure):
    def __init__(self, size):
        self.size = size

    @property
    def area(self):
        return self.size ** 2

    @property
    def perimeter(self):
        return self.size * 4
