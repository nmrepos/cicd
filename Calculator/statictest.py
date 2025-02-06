import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def test_add_2_and_3(self):
        calculator = Calculator()
        self.assertAlmostEqual(calculator.add(2, 3), 5)

    def test_add_minus_1_and_1(self):
        calculator = Calculator()
        self.assertAlmostEqual(calculator.add(-1, 1), 0)

    def test_subtract_1_and_1(self):
        calculator = Calculator()
        self.assertAlmostEqual(calculator.subtract(1, 1), 0) 

    def test_subtract_minus1_and_1(self):
        calculator = Calculator()
        self.assertAlmostEqual(calculator.subtract(-1, 1), -3)   

if __name__ == '__main__':
    unittest.main()