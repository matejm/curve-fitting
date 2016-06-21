import unittest
from linear_interpolation import *

class TestLinearInterpolation(unittest.TestCase):
    def check_functions_equal(self, f1, f2):
        """This does NOT guarantee that function are equal."""
        for x in range(-30, 30):
            print(x, f1(x), f2(x))
            self.assertEqual(f1(x), f2(x))
            self.assertAlmostEqual(f1(x / 2000), f2(x / 2000))

    def test_linear_interpolation(self):
        f = lambda x: x
        self.check_functions_equal(linear_interpolation([(1, 1), (2, 2)]), f)
        f = lambda x: 2*x + 1
        self.check_functions_equal(linear_interpolation([(0, 1), (1, 3)]), f)
        f = lambda x: x if x >= 0 else -x
        self.check_functions_equal(linear_interpolation([(-1, 1), (0, 0), (1, 1)]), f)
        f = lambda x: abs(x) + 3 if abs(x) > 3 else 6
        self.check_functions_equal(linear_interpolation([(-7, 10), (-3, 6),
            (3, 6), (7, 10)]), f)
        f = lambda x: 2*x + 3 if x > 3 else (3*x if x > -5 else 2*x - 5)
        self.check_functions_equal(linear_interpolation([(10, 23), (3, 9),
            (0, 0), (-5, -15), (-100, -205)]), f)

if __name__ == '__main__':
    unittest.main()
