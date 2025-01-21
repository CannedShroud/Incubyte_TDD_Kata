import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):
    
    def setUp(self) -> None:
        print("Init Calculator instance.")
        self.calculator = Calculator()

if __name__ == "__main__":
    unittest.main()
