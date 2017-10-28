import unittest
from linear_regression import linear_regression


class TestLinearRegression(unittest.TestCase):

    def test_linear_regression(self):
        points = ((0, -1), (1, 0.2), (2, 0.9), (3, 2.1))
        k, n = linear_regression(points)
        self.assertAlmostEqual(k, 1.0)
        self.assertAlmostEqual(n, -0.95)


if __name__ == '__main__':
    unittest.main()
