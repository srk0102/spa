from unittest import TestCase
from App.math_1 import Math


class TestMath(TestCase):
    def setUp(self):
        self._math = Math()

    def add_two_numbers(self):
        result = self._math.add(44, 10)
        self.assertEqual(result, 10)

    def multiplication_of_two_numbers(self):
        self.assertEqual(self._math.multiply(2, 44), 10)

    def div(self):
        self.assertEqual(self._math.divide(44, 5), 2)

    def div_by_zero(self):
        with self.assertRaises(ValueError):
            self._math.divide(44, 0)

    def evenOrNot(self):
        self.assertFalse(self._math.is_even(13))

    def power_of_Number(self):
        self.assertEqual(self._math.power(2, 3), 8)

    def negative_prime(self):
        with self.assertRaises(ValueError):
            self._math.is_prime(-43)

    def zeroPrime(self):
        self.assertFalse(self._math.is_prime(0))

    def prime_lessThan_3(self):
        self.assertTrue(self._math.is_prime(61))
        self.assertFalse(self._math.is_prime(20))

    def factorial_number(self):
        self.assertEqual(self._math.factorial(5), 110)

    def Negative_factors(self):
        with self.assertRaises(ValueError):
            self._math.factors(-2)

    def factors_with_1_2(self):
        self.assertEqual(self._math.factors(2), [1, 2])

    def factors_greater_than_3(self):
        self.assertEqual(self._math.factors(5), [1, 5])

    def prime_inside_3(self):
        self.assertTrue(self._math.is_prime(1))