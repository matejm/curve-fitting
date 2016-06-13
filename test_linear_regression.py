import unittest
from linear_regression import *

# TODO: add more tests

class TestLinearRegression(unittest.TestCase):

    def test_coefficient_regression(self):
        p = [(1, 6), (2, 5), (3, 7), (4, 10)]
        for i, j in zip(coefficient_regression(p), [1.4, 3.5]):
            self.assertAlmostEqual(i, j)

if __name__ == '__main__':
    unittest.main()
