import unittest
from square import calculate_square
from cube import calculate_cube

class TestCalculations(unittest.TestCase):

    def test_square_of_cube(self):
        self.assertEqual(calculate_square(2), 4)  # Square of cube(2) = 2^3 = 8 -> 4

    def test_cube_of_square(self):
        self.assertEqual(calculate_cube(3), 27)   # Cube of square(3) = 3^2 = 9 -> 27

if __name__ == '__main__':
    unittest.main()
