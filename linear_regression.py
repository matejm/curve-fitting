"""
Useful functions for linear regression.
NOTE: Because of solvnig system of equations, errors can be quite large.
"""

def get_error(points):
    """calculates error function coefficients."""
    error = {'k^2': 0, 'kn': 0, 'n^2': 0, 'n': 0, 'k': 0}
    for point in points:
        x, y = point
        # now square this: y = kx + n
        error['k^2'] += x**2
        error['kn'] += 2 * x
        error['k'] += -2 * x * y
        error['n'] += -2 * y
        error['n^2'] += 1
    return error

def solve_2x2_system(s1, s2):
    """Solves 2x2 system of equations."""
    n = -(s2[2] - s1[2] * s2[0] / s1[0]) / (s2[1] - s1[1] * s2[0]/s1[0])
    k = -(n * s1[1] + s1[2]) / s1[0]
    return k, n

def coefficient_regression(points):
    """
    Input: list of points (x, y).
    Finds best linear fit for given points using least squares method.
    Returns coefficient k and n for. They represent line y = kx + n.
    """
    if len(points) == 0:
        return lambda x: 0
    if len(points) == 1:
        return lambda x: points[0][1]
    if len(points) == 2:
        p1, p2 = points
        k = (p2[1] - p1[1]) / (p2[0] - p1[0])
        n = p1[1] - k * p1[0]
        return lambda x: k * x + n

    error = get_error(points)
    # find minimum of error with derivatives
    d_k = [2 * error['k^2'], error['kn'], error['k']]
    d_n = [error['kn'], 2 * error['n^2'], error['n']]

    k, n = solve_2x2_system(d_k, d_n)
    return k, n

def linear_regression(points):
    """
    Input: list of points (x, y).
    Finds best linear fit for given points using least squares method.
    Returns function of a calculated line.
    """
    k, n = coefficient_regression(points)
    return lambda x: k * x + n
