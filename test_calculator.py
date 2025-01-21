import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):
    
    def setUp(self) -> None:
        print("Init Calculator instance.")
        self.calculator = Calculator()

    def test_add_empty_string_returns_zero(self):
        result = self.calculator.add("")
        self.assertEqual(result, 0)

    def test_add_single_string_num_returns_num(self):
        result = self.calculator.add("3")
        self.assertEqual(result, 3)

if __name__ == "__main__":
    unittest.main()
