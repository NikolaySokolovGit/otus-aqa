import pytest as pytest

from src.Circle import Circle
from src.Rectangle import Rectangle
from src.Square import Square
from src.Triangle import Triangle


class TestTriangle:
    def test_create_positive(self):
        """Треугольник создается по трем сторонам"""
        triangle = Triangle(1, 1, 1)
        assert triangle

    @pytest.mark.parametrize('size_a, size_b, size_c', (
        pytest.param(1, 2, 1),
        pytest.param(2, 1, 1),
        pytest.param(1, 1, 2),
    ))
    def test_triangle_doesnt_exist(self, size_a, size_b, size_c):
        """При создании несуществующего треугольника должно возвращаться None"""
        triangle = Triangle(size_a, size_b, size_c)
        assert triangle is None, f"Треугольник со сторонами {size_a, size_b, size_c} не существует"

    def test_triangle_parameters(self):
        """У треугольника есть параметры"""
        triangle = Triangle(1, 1, 1)
        assert triangle.perimeter
        assert triangle.area
        assert triangle.name

    @pytest.mark.parametrize('figure', (
            pytest.param(Circle(1), id='Circle'),
            pytest.param(Rectangle(1, 2), id='Rectangle'),
            pytest.param(Square(1), id='Square'),
            pytest.param(Triangle(1, 1, 1), id='Triangle'),
    ))
    def test_add_area(self, figure):
        """Метод add_area возвращает сумму площадей фигур"""
        triangle = Triangle(1, 1, 1)
        assert triangle.add_area(figure) == sum((triangle.area, figure.area))

    def test_add_area_negative(self):
        """Если методу add_area передана не геометрическая фигура, то выбрасывается ошибка ValueError"""
        with pytest.raises(ValueError) as exc:
            triangle = Triangle(1, 1, 1)
            triangle.add_area("it's not a figure")
        assert exc.value.args[0] == 'figure must be a Figure class instance'
