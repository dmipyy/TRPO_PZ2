import unittest
from calc import Calculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(5, 2), 3)
        self.assertEqual(self.calc.subtract(1, -1), 2)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(2, 3), 6)
        self.assertEqual(self.calc.multiply(-2, 3), -6)

    def test_divide(self):
        self.assertEqual(self.calc.divide(6, 2), 3)
        with self.assertRaises(ZeroDivisionError):
            self.calc.divide(5, 0)
    
    def test_pow(self):
        self.assertEqual(self.calc.pow(2, 3), 8)
        self.assertEqual(self.calc.pow(2, 0), 1)
        self.assertEqual(self.calc.pow(2, -1), 0.5)
    
    def test_XOR(self):
        self.assertEqual(self.calc.XOR(5, 3), 6)
        self.assertEqual(self.calc.XOR(0, 1), 1)
        self.assertEqual(self.calc.XOR(1, 1), 0)


if __name__ == '__main__':
    unittest.main()