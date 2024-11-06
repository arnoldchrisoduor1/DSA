import unittest
from arrayDiff import array_diff

class TestArrayDiff(unittest.TestCase):
    def test_basic_case(self):
        self.assertEqual(array_diff([1, 2], [1]), [2])

    def test_multiple_occurrences(self):
        self.assertEqual(array_diff([1, 2, 2, 2, 3], [2]), [1, 3])

    def test_with_duplicates_in_a(self):
        self.assertEqual(array_diff([1, 2, 3, 3, 3, 4], [3]), [1, 2, 4])

    def test_empty_b(self):
        self.assertEqual(array_diff([1, 2, 3], []), [1, 2, 3])

    def test_empty_a(self):
        self.assertEqual(array_diff([], [1, 2]), [])

    def test_all_elements_in_b(self):
        self.assertEqual(array_diff([1, 2], [1, 2]), [])
        
if __name__ == "__main__":
    unittest.main()