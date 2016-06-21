"""Another common interpolation method."""

def linear_interpolation(points):
    """
    Input: list of points (x, y).
    Returns a function f(x) which returns y value of line through two closests
    points for given x.
    """
    points.sort(key=lambda x: x[0])
    xs = [p[0] for p in points]
    ys = [p[1] for p in points]
    def f(x):
        for i in range(len(xs)):
            if xs[i] > x:
                break
        if i == 0: i += 1
        k = (ys[i] - ys[i-1]) / (xs[i] - xs[i-1])
        return ys[i-1] + k * (x - xs[i-1])
    return f
