import unittest
from src.calculator import sum, substract, multiply, divide
class CalculatorTests(unittest.TestCase):
    def test_sum(self):
        assert sum(2, 3) == 5

    def test_subtraction(self):
        assert substract(5, 2) == 3

    def test_multiplication(self):
        assert multiply(2, 3) == 6

    def test_division(self):
        assert divide(6, 3) == 2
        with self.assertRaises(ValueError):
            divide(5, 0)