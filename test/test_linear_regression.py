import unittest
from linear_regression import *

class TestLinearRegression(unittest.TestCase):

    def test_get_error(self):
        e = {'k^2': 1, 'kn': 2, 'n^2': 1, 'n': -2, 'k': -2}
        self.assertEqual(get_error([(1, 1)]), e)
        e = {'k^2': 9, 'kn': 6, 'n^2': 1, 'n': -4, 'k': -12}
        self.assertEqual(get_error([(3, 2)]), e)
        e = {'k^2': 10, 'kn': 8, 'n^2': 2, 'n': -6, 'k': -14}
        self.assertEqual(get_error([(1, 1), (3, 2)]), e)
        e = {'k^2': 11, 'kn': 6, 'n^2': 3, 'n': -12, 'k': -8}
        self.assertEqual(get_error([(3, 2), (1, 1), (-1, 3)]), e)

    def test_solve_2x2_system(self):
        self.assertEqual(solve_2x2_system([1, 1, 1], [1, 0, -1]), (1, -2))
        self.assertEqual(solve_2x2_system([1, 2, 3], [3, 2, 1]), (1, -2))
        self.assertEqual(solve_2x2_system([1, 2, 0], [2, 1, 0]), (0, 0))
        self.assertEqual(solve_2x2_system([1, 1, -1], [1, 0, -1]), (1, 0))
        self.assertEqual(solve_2x2_system([1, 2, -1], [1, 6, -2]), (0.5, 0.25))

    def test_coefficient_regression(self):
        p = [(5, 5), (1, 5), (3, 7), (3, 3)]
        for i, j in zip(coefficient_regression(p), [0, 5]):
            self.assertAlmostEqual(i, j)
        p = [(1, 2), (2, 3), (3, 4), (4, 5)]
        for i, j in zip(coefficient_regression(p), [1, 1]):
            self.assertAlmostEqual(i, j)
        p = [(1, 3), (2, 2), (3, 5), (4, 1)]
        for i, j in zip(coefficient_regression(p), [-0.3, 3.5]):
            self.assertAlmostEqual(i, j)
        p = [(1, 6), (2, 5), (3, 7), (4, 10)]
        for i, j in zip(coefficient_regression(p), [1.4, 3.5]):
            self.assertAlmostEqual(i, j)

if __name__ == '__main__':
    unittest.main()
