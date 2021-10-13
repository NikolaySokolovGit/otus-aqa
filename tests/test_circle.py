import pytest

from src.Circle import Circle
from src.Rectangle import Rectangle
from src.Square import Square
from src.Triangle import Triangle


class TestCircle:
    def test_create_positive(self):
        """Круг создается по значению радиуса"""
        circle = Circle(1)
        assert circle

    def test_triangle_parameters(self):
        """У круга есть параметры name, perimeter, area"""
        circle = Circle(1)
        assert circle.perimeter
        assert circle.area
        assert circle.name

    @pytest.mark.parametrize('figure', (
            pytest.param(Circle(1), id='Circle'),
            pytest.param(Rectangle(1, 2), id='Rectangle'),
            pytest.param(Square(1), id='Square'),
            pytest.param(Triangle(1, 1, 1), id='Triangle'),
    ))
    def test_add_area(self, figure):
        """Метод add_area возвращает сумму площадей фигур"""
        circle = Circle(1)
        assert circle.add_area(figure) == sum((circle.area, figure.area))

    def test_add_area_negative(self):
        """Если методу add_area передана не геометрическая фигура, то выбрасывается ошибка ValueError"""
        with pytest.raises(ValueError) as exc:
            circle = Circle(1)
            circle.add_area("it's not a figure")
        assert exc.value.args[0] == 'figure must be a Figure class instance'
