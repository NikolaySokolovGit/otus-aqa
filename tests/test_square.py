import pytest

from src.Circle import Circle
from src.Rectangle import Rectangle
from src.Square import Square
from src.Triangle import Triangle


class TestSquare:
    def test_create_positive(self):
        """Квадрат создается по значению одной стороны"""
        square = Square(1)
        assert square

    def test_triangle_parameters(self):
        """У круга есть параметры name, perimeter, area"""
        square = Square(1)
        assert square.perimeter
        assert square.area
        assert square.name

    @pytest.mark.parametrize('figure', (
            pytest.param(Circle(1), id='Circle'),
            pytest.param(Rectangle(1, 2), id='Rectangle'),
            pytest.param(Square(1), id='Square'),
            pytest.param(Triangle(1, 1, 1), id='Triangle'),
    ))
    def test_add_area(self, figure):
        """Метод add_area возвращает сумму площадей фигур"""
        square = Square(1)
        assert square.add_area(figure) == sum((square.area, figure.area))

    def test_add_area_negative(self):
        """Если методу add_area передана не геометрическая фигура, то выбрасывается ошибка ValueError"""
        with pytest.raises(ValueError) as exc:
            square = Square(1)
            square.add_area("it's not a figure")
        assert exc.value.args[0] == 'figure must be a Figure class instance'
