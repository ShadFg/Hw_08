import unittest
from main import Calculator

class MyTest(unittest.TestCase):
    def testPlus(self):
        calculator = Calculator()
        self.assertEqual(calculator.plus(1, 2), 3)

    def testMinus(self):
        calculator = Calculator()
        self.assertEqual(calculator.minus(5, 3), 2)

    def testMultiply(self):
        calculator = Calculator()
        self.assertEqual(calculator.multiply(3, 4), 12)

    def testDivide(self):
        calculator = Calculator()
        self.assertEqual(calculator.divide(10, 2), 5)

    def testIncorrectInput(self):
        calculator = Calculator()
        self.assertEqual(calculator.plus("a", 2), "Incorrect Input")

if __name__ == "__main__":
    unittest.main()