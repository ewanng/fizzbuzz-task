import unittest
from src.fizzbuzz import fizzbuzz


class TestFizzBuzz(unittest.TestCase):

    # initial test with small numbers within range of 1-100
    def test_fizzbuzz(self):
        self.assertEqual(
            fizzbuzz(1, 15), [
                1, 2, 3, 'fizz', 4, 5, 'buzz', 6, 'fizz', 7, 8, 9, 'fizz', 10,
                'buzz', 11, 12, 'fizz', 13, 14, 15, 'fizz', 'buzz'])

    # second test with integers that have a big range and both divisible by 3
    def test_fizzbuzz2(self):
        self.assertEqual(
            fizzbuzz(3, 90), [
                3, 'fizz', 4, 5, 'buzz', 6, 'fizz', 7, 8, 9, 'fizz', 10,
                'buzz', 11, 12, 'fizz', 13, 14, 15, 'fizz', 'buzz', 16, 17, 18,
                'fizz', 19, 20, 'buzz', 21, 'fizz', 22, 23, 24, 'fizz', 25,
                'buzz', 26, 27, 'fizz', 28, 29, 30, 'fizz', 'buzz', 31, 32, 33,
                'fizz', 34, 35, 'buzz', 36, 'fizz', 37, 38, 39, 'fizz', 40,
                'buzz', 41, 42, 'fizz', 43, 44, 45, 'fizz', 'buzz', 46, 47, 48,
                'fizz', 49, 50, 'buzz', 51, 'fizz', 52, 53, 54, 'fizz', 55,
                'buzz', 56, 57, 'fizz', 58, 59, 60, 'fizz', 'buzz', 61, 62, 63,
                'fizz', 64, 65, 'buzz', 66, 'fizz', 67, 68, 69, 'fizz', 70,
                'buzz', 71, 72, 'fizz', 73, 74, 75, 'fizz', 'buzz', 76, 77, 78,
                'fizz', 79, 80, 'buzz', 81, 'fizz', 82, 83, 84, 'fizz', 85,
                'buzz', 86, 87, 'fizz', 88, 89, 90, 'fizz', 'buzz'])

    # Third test with both start and end numbers divisible by 5
    def test_fizzbuzz3(self):
        self.assertEqual(
            fizzbuzz(10, 60), [
                10, 'buzz', 11, 12, 'fizz', 13, 14, 15, 'fizz', 'buzz', 16, 17,
                18, 'fizz', 19, 20, 'buzz', 21, 'fizz', 22, 23, 24, 'fizz', 25,
                'buzz', 26, 27, 'fizz', 28, 29, 30, 'fizz', 'buzz', 31, 32, 33,
                'fizz', 34, 35, 'buzz', 36, 'fizz', 37, 38, 39, 'fizz', 40,
                'buzz', 41, 42, 'fizz', 43, 44, 45, 'fizz', 'buzz', 46, 47, 48,
                'fizz', 49, 50, 'buzz', 51, 'fizz', 52, 53, 54, 'fizz', 55,
                'buzz', 56, 57, 'fizz', 58, 59, 60, 'fizz', 'buzz'])


if __name__ == '__main__':
    unittest.main()
