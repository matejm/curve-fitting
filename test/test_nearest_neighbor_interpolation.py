import unittest
from nearest_neighbor_interpolation import *

class TestNearestNeighborInterpolation(unittest.TestCase):
    def check_functions_equal(self, f1, f2):
        """This does NOT guarantee that function are equal."""
        for x in range(-30, 30):
            print(x, f1(x), f2(x))
            self.assertEqual(f1(x), f2(x))
            self.assertEqual(f1(x / 2000), f2(x / 2000))

    def test_nearest_neighbor_interpolation(self):
        f = lambda x: 1
        self.check_functions_equal(nearest_neighbor_interpolation([(1, 1)]), f)
        f = lambda x: 1 if x <= 1.5 else 2
        self.check_functions_equal(nearest_neighbor_interpolation([(1, 1),
            (2, 2)]), f)
        f = lambda x: 0 if abs(x) <= 4 and x != -4 else 9
        self.check_functions_equal(nearest_neighbor_interpolation([(0, 0),
            (-8, 9), (8, 9)]), f)


if __name__ == '__main__':
    unittest.main()
