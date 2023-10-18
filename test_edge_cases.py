import unittest
from src.fizzbuzz import fizzbuzz


class TestFizzBuzz(unittest.TestCase):

    # Testing with a start number less than 1
    def test_below_range(self):
        self.assertEqual(
            fizzbuzz(0, 67),
            "Invalid input: start and end numbers need to be between 1 and 100")

    # Testing with an end number greater than 100
    def test_above_range(self):
        self.assertEqual(
            fizzbuzz(60, 8502),
            "Invalid input: start and end numbers need to be between 1 and 100")

    # Testing with a start number greater than the end number
    def test_start_greater_than_end_number(self):
        self.assertEqual(
            fizzbuzz(79, 12),
            "Invalid input: start number greater than end number")

    # Testing with negative start and end numbers
    def test_negative_numbers(self):
        self.assertEqual(
            fizzbuzz(-79, -12),
            "Invalid input: start and end numbers need to be between 1 and 100")

    # Testing with floating point start and end numbers
    def test_floating_points(self):
        self.assertEqual(
            fizzbuzz(5.2, 70.5),
            "Invalid input: please enter integers only")

    # Testing with equal start and end numbers
    def test_equal_start_and_end(self):
        self.assertEqual(
            fizzbuzz(50, 50), "Invalid input: start and end numbers cannot be equal")

    # Testing with non numbers start and end arguments
    def test_non_numeric(self):
        self.assertEqual(
            fizzbuzz("String", []),
            "Invalid input: please enter integers only")


if __name__ == '__main__':
    unittest.main()
