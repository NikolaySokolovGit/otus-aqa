from abc import ABC, abstractmethod

from src.utils import validate_size


class Figure(ABC):
    def __init__(self, *args):
        print('init')
        validate_size(*args)

    @property
    @abstractmethod
    def area(self):
        pass

    @property
    @abstractmethod
    def perimeter(self):
        pass

    def add_area(self, figure):
        if not isinstance(figure, Figure):
            raise ValueError('figure must be a Figure class instance')
        return self.area + figure.area
