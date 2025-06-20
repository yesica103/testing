import unittest
from src.calculator import sum, substract
class CalculatorTests(unittest.TestCase):
    def test_sum(self):
        assert sum(2, 3) == 5

    def test_subtraction(self):
        assert substract(5, 2) == 3