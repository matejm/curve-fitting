"""Simplest interpolation method"""

def nearest_neighbor_interpolation(points):
    """
    Input: list of points (x, y).
    Returns a function f(x) which returns y value of nearest neighbor for given
    x. At the midpoints (when distances to 2 closest points are the same) value
    of point with lower x value is returned.
    """
    points.sort(key=lambda x: x[0])
    def f(x):
        if x < points[0][0]:
            return points[0][1]
        for i in range(1, len(points)):
            if points[i][0] < x:
                continue
            if abs(points[i][0] - x) < abs(points[i-1][0] - x):
                return points[i][1]
            return points[i-1][1]
        return points[-1][1]
    return f
