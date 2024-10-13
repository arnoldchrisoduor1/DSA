import unittest
from multiple_sum import solution  # Import the solution function

class TestSolution(unittest.TestCase):

    def test_negative_number(self):
        self.assertEqual(solution(-5), 0)  # Should return 0 for negative input

    def test_zero(self):
        self.assertEqual(solution(0), 0)  # Should return 0 for input 0

    def test_below_three(self):
        self.assertEqual(solution(1), 0)  # No multiples below 1
        self.assertEqual(solution(2), 0)  # No multiples below 2

    def test_multiples_below_10(self):
        self.assertEqual(solution(10), 23)  # Multiples: 3, 5, 6, 9 -> Sum = 23

    def test_multiples_below_20(self):
        self.assertEqual(solution(20), 78)  # Multiples: 3, 5, 6, 9, 10, 12, 15, 18 -> Sum = 78

    def test_large_number(self):
        self.assertEqual(solution(1000), 233168)  # Test with a larger number

if __name__ == '__main__':
    unittest.main()
