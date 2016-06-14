import unittest
from polynomial_interpolation import *

class TestPolinomialInterpolation(unittest.TestCase):

    def test_coefficients_to_string(self):
        self.assertEqual(coefficients_to_string([1]), '1')
        self.assertEqual(coefficients_to_string([1, 1]), 'x + 1')
        self.assertEqual(coefficients_to_string([1, 1, 1]), 'x^2 + x + 1')
        self.assertEqual(coefficients_to_string([1, 2, 3]), 'x^2 + 2x + 3')
        self.assertEqual(coefficients_to_string([1, 0]), 'x')
        self.assertEqual(coefficients_to_string([5, 0, 2]), '5x^2 + 2')
        self.assertEqual(coefficients_to_string([-1, -1]), '-x - 1')
        self.assertEqual(coefficients_to_string([-2, 0, 0, 4]), '-2x^3 + 4')

    def test_points_to_matrix(self):
        a = [(0, 0)]
        self.assertEqual(points_to_matrix(a), ([[1]], [0]))
        a = [(6, 5)]
        self.assertEqual(points_to_matrix(a), ([[1]], [5]))
        a = [(0, 0), (1, 1)]
        self.assertEqual(points_to_matrix(a), ([[0, 1], [1, 1]], [0, 1]))
        a = [(2, 3), (3, 4)]
        self.assertEqual(points_to_matrix(a), ([[2, 1], [3, 1]], [3, 4]))
        a = [(1, 2), (2, 3), (3, 4)]
        self.assertEqual(points_to_matrix(a), ([[1, 1, 1], [4, 2, 1], [9, 3, 1]],
            [2, 3, 4]))
        a = [(0, 0), (1, 1), (2, 2), (3, 3)]
        self.assertEqual(points_to_matrix(a), ([[0, 0, 0, 1], [1, 1, 1, 1],
            [8, 4, 2, 1], [27, 9, 3, 1]], [0, 1, 2, 3]))

    def test_join_matrices(self):
        a, b = [[1]], [2]
        self.assertEqual(join_matrices(a, b), [[1, 2]])
        a, b = [[1, 1], [1, 1]], [2, 2]
        self.assertEqual(join_matrices(a, b), [[1, 1, 2], [1, 1, 2]])
        a, b = [[1, 2, 3], [1, 1, 1], [0, 0, 0], [3, 2, 1]], [9, 6, 7, 8]
        self.assertEqual(join_matrices(a, b), [[1, 2, 3, 9], [1, 1, 1, 6],
            [0, 0, 0, 7], [3, 2, 1, 8]])

    def test_gaussian_elimination(self):
        a = [[1, 1, 1], [0, 1, 1]]
        self.assertEqual(gaussian_elimination(a), [[1, 1, 1], [0, 1, 1]])
        a = [[0, 1, 1], [1, 1, 1]]
        self.assertEqual(gaussian_elimination(a), [[1, 1, 1], [0, 1, 1]])
        a = [[0, 0, 0, 1, 1], [0, 0, 1, 1, 1], [0, 1, 1, 1, 1], [1, 1, 1, 1, 1]]
        self.assertEqual(gaussian_elimination(a), [[1, 1, 1, 1, 1], [0, 1, 1, 1,
            1], [0, 0, 1, 1, 1], [0, 0, 0, 1, 1]])
        a = [[1, 1, 1], [1, 2, 1]]
        self.assertEqual(gaussian_elimination(a), [[1, 1, 1], [0, 1, 0]])
        a = [[2, 2, 1, 2], [1, 2, 2, 2], [1, 1, 1, 1]]
        self.assertEqual(gaussian_elimination(a), [[2, 2, 1, 2], [0, 1, 1.5, 1],
            [0, 0, 0.5, 0]])

    def test_solve_system(self):
        self.assertEqual(solve_system([[1, 1, 1], [0, 1, 1]]), [0, 1])
        self.assertEqual(solve_system([[1, 1, 3], [0, 2, 2]]), [2, 1])
        self.assertEqual(solve_system([[2, 1, 4], [0, 1, 1]]), [3/2, 1])
        self.assertEqual(solve_system([[2, 2, 10], [0, 4, 8]]), [3, 2])

    def check_functions_equal(self, f1, f2):
        """This does NOT guarantee that function are equal."""
        for x in range(-500, 500, 20):
            self.assertEqual(f1(x), f2(x))  # larger scale
            self.assertAlmostEqual(f1(x / 2000), f2(x / 2000))  # smaller scale

    def test_coefficient_interpolation(self):
        a = [(1, 1), (2, 2)]
        self.assertEqual(coefficient_interpolation(a), [1, 0])
        a = [(1, 3), (2, 4)]
        self.assertEqual(coefficient_interpolation(a), [1, 2])
        a = [(1283, 6)]
        self.assertEqual(coefficient_interpolation(a), [6])
        a = [(1, 2), (2, 8), (3, 18)]
        self.assertEqual(coefficient_interpolation(a), [2, 0, 0])

    def test_polynomial_interpolation(self):
        p = lambda x: x + 1
        self.check_functions_equal(p, polynomial_interpolation([(0, 1), (2, 3)]))
        p = lambda x: x**2 + 5
        self.check_functions_equal(p, polynomial_interpolation([(1, 6), (3, 14),
            (-1, 6)]))
        p = lambda x: x**3 + 2*x**2 + 3*x - 1
        self.check_functions_equal(p, polynomial_interpolation([(1, 5), (2, 21),
            (0, -1), (-2, -7)]))

if __name__ == '__main__':
    unittest.main()
