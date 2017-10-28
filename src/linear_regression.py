import numpy as np

"""
Useful functions for linear regression.
NOTE: Because of solvnig system of equations, errors can be quite large.
"""


def linear_regression(points):
    """
    :points list of points (x, y).
    Finds best linear fit for given points using least squares method.
    :return function of a calculated line.
    """
    x = np.array([i[0] for i in points])
    y = np.array([i[1] for i in points])

    A = np.vstack([x, np.ones(len(x))]).T

    k, n = np.linalg.lstsq(A, y)[0]

    return k, n
