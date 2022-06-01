from app.square import Square
from unittest import TestCase
from unittest.mock import MagicMock


class TestSquare(TestCase):
    def setUp(self):
        self._math_mock = MagicMock()
        self._math_mock.power = MagicMock(return_value=25)
        self._square = Square(5, self._math_mock)
        self._math_mock.add = MagicMock(return_value=10)

    def test_area(self):
        self.assertEqual(self._square.area(), 25)

    def test_circumference_of_square(self):
        self.assertEqual(self._square.circumference(), 10)
