from src.Figure import Figure


class Square(Figure):
    name = 'Square'

    def __init__(self, size):
        super().__init__(size)
        self.size = size

    @property
    def area(self):
        return self.size ** 2

    @property
    def perimeter(self):
        return self.size * 4


if __name__ == '__main__':
    s = Square('string')