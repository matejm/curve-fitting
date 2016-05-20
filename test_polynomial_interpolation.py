import unittest
from polynomial_interpolation import *

class TestPolinomialInterpolation(unittest.TestCase):

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

if __name__ == '__main__':
    unittest.main()
