from polynomial_interpolation import coefficient_interpolation, coefficients_to_string

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

    coefficients = coefficient_interpolation(points)

    for i in range(len(coefficients)):
        x = coefficients[i]
        x = float('{:.10f}'.format(x))  # gaussian elimination has a big error...
        x = int(x) if int(x) == x else x
        coefficients[i] = x

    polynomial = coefficients_to_string(coefficients)
    print('f(x) =', polynomial)

if __name__ == '__main__':
    main()
