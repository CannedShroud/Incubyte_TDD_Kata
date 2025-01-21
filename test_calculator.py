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

    def test_add_two_string_num_returns_sum(self):
        result = self.calculator.add("1,2")
        self.assertEqual(result, 1+2)

    def test_add_n_string_num_returns_sum(self):
        result = self.calculator.add("1,2,3,4,5")
        self.assertEqual(result, 15)

if __name__ == "__main__":
    unittest.main()
