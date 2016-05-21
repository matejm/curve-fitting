from polynomial_interpolation import interpolate

def coefficients_to_string(coefficients):
    s = []
    for i, j in enumerate(coefficients[::-1]):
        if j:
            if j == int(j): j = int(j)
            foo = ''
            if j == -1 and i != 0:
                foo += '-'
            elif j != 1 or i == 0:
                foo += str(j)
            if i:
                foo += 'x'
                if i != 1: foo += '^' + str(i)
            s.append(foo)
    if not s:
        s = ['0']
    s.reverse()
    out = 'f(x) = ' + s[0]
    for i in s[1:]:
        if i[0] == '-':
            out += ' - ' + i[1:]
        else:
            out += ' + ' + i
    return out


def main():
    print('Polynomial interpolation')
    print('Enter coordinates of points split with space. Terminate input with empty line')
    points = []
    i = 1
    while True:
        try:
            x, y = input('Point {}: '.format(i)).split()
            x, y = float(x), float(y)
            points.append((x, y))
        except ValueError:
            break
        i += 1

    coefficients = interpolate(points)

    for i in range(len(coefficients)):
        x = coefficients[i]
        x = float('{:.10f}'.format(x))  # gaussian elimination has a big error...
        x = int(x) if int(x) == x else x
        coefficients[i] = x

    polynomial = coefficients_to_string(coefficients)
    print(polynomial)

if __name__ == '__main__':
    main()
