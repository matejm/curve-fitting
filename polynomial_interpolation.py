def points_to_matrix(points):
    """List of points (x, y) is transformed into system of linear equations."""
    degree = len(points) - 1
    matrix = [[] for i in range(degree + 1)]
    vector = []
    for i, point in enumerate(points):
        for j in range(degree, -1, -1):
            matrix[i].append(point[0] ** j)
        vector.append(point[1])
    return matrix, vector

def join_matrices(matrix, vector):
    for i in range(len(matrix)):
        matrix[i].append(vector[i])
    return matrix

def gaussian_elimination(matrix):
    """Joins given matrix and vector in new matrix and transforms it into upper
    triangular matrix."""
    n = len(matrix)
    for i in range(n):
        # find max element and swap lines of remaining unsolved matrix
        max_elem = abs(matrix[i][i])
        max_row = i
        for j in range(i + 1, n):
            if max_elem < abs(matrix[j][i]):
                max_elem = abs(matrix[j][i])
                max_row = j
        if max_row != i:
            matrix[i], matrix[max_row] = matrix[max_row], matrix[i]
        # make all rows below this one 0 in this column
        for j in range(i + 1, n):
            r = []
            c = - matrix[j][i] / matrix[i][i]
            for k in matrix[i]:
                r.append(c * k)
            matrix[j] = [a + b for a, b in zip(matrix[j], r)]

    return matrix

def solve_system(matrix):
    """Solves system of linear equations for upper triangular matrix."""
    coefficients = []
    matrix.reverse()  # for easy access
    coefficients.append(matrix[0][-1] / matrix[0][-2])  # first is solved
    for i in range(1, len(matrix)):
        # sub all already known coefficients...
        a = 0
        for j in range(i):
            a += (coefficients[j] * matrix[i][-j - 2])
        coefficients.append((matrix[i][-1] - a) / matrix[i][-i - 2])
    coefficients.reverse()
    return coefficients

def interpolate(points):
    """
    Input: list of points (x, y) of a lenght n.
    Finds a polynomial of degree n-1 which goes exactly through these points.
    Returns a list of coefficients of a polynomial.
    NOTE: Because system of equations if computed using Gaussian elimination,
    errors can be quite large.
    """
    matrix, vector = points_to_matrix(points)
    matrix = join_matrices(matrix, vector)
    matrix = gaussian_elimination(matrix)
    coefficients = solve_system(matrix)
    return coefficients
