import pytest

from src.Circle import Circle
from src.Rectangle import Rectangle
from src.Square import Square
from src.Triangle import Triangle


class TestRectangleCircle:
    def test_create_positive(self):
        """Прямоугольник создается по значению двух сторон"""
        rectangle = Rectangle(1, 2)
        assert rectangle

    def test_triangle_parameters(self):
        """У прямоугольника есть параметры name, perimeter, area"""
        rectangle = Rectangle(1, 2)
        assert rectangle.perimeter
        assert rectangle.area
        assert rectangle.name

    @pytest.mark.parametrize('figure', (
            pytest.param(Circle(1), id='Circle'),
            pytest.param(Rectangle(1, 2), id='Rectangle'),
            pytest.param(Square(1), id='Square'),
            pytest.param(Triangle(1, 1, 1), id='Triangle'),
    ))
    def test_add_area(self, figure):
        """Метод add_area возвращает сумму площадей фигур"""
        rectangle = Rectangle(1, 2)
        assert rectangle.add_area(figure) == sum((rectangle.area, figure.area))

    def test_add_area_negative(self):
        """Если методу add_area передана не геометрическая фигура, то выбрасывается ошибка ValueError"""
        with pytest.raises(ValueError) as exc:
            rectangle = Rectangle(1, 2)
            rectangle.add_area("it's not a figure")
        assert exc.value.args[0] == 'figure must be a Figure class instance'
