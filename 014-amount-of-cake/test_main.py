# test_cake_calculator.py

import unittest
from main import CakeCalculator

class TestCakeCalculator(unittest.TestCase):

    def test_basic_case(self):
        calc = CakeCalculator()
        recipe = {'flour': 500, 'sugar': 200, 'eggs': 1}
        available = {'flour': 1200, 'sugar': 1200, 'eggs': 5, 'milk': 200}
        self.assertEqual(calc.max_cakes(recipe, available), 2)

    def test_missing_ingredient(self):
        calc = CakeCalculator()
        recipe = {'apples': 3, 'flour': 300, 'sugar': 150, 'milk': 100, 'oil': 100}
        available = {'sugar': 500, 'flour': 2000, 'milk': 2000}
        self.assertEqual(calc.max_cakes(recipe, available), 0)

    def test_instance_based(self):
        recipe = {'flour': 100, 'sugar': 50}
        available = {'flour': 500, 'sugar': 200}
        calc = CakeCalculator(recipe, available)
        self.assertEqual(calc.max_cakes(), 4)

    def test_zero_available(self):
        recipe = {'eggs': 2}
        available = {}
        calc = CakeCalculator()
        self.assertEqual(calc.max_cakes(recipe, available), 0)

    def test_error_on_missing_input(self):
        calc = CakeCalculator()
        with self.assertRaises(ValueError):
            calc.max_cakes()

if __name__ == '__main__':
    unittest.main()
