# Create a function poly() that can be called with any number N of parameters, which are the coefficients of a N -th order polynomial. It returns another function, which takes one argument x and
# returns the value of the polynomial for x .
def poly(*args):
    def poly_result(x):
        res = 0
        for order, coef in enumerate(args):
            res += coef * x ** (order)
        return res

    return poly_result


if __name__ == "__main__":
    poly_fn = poly(1, 2, 3)
    print("Result of 1 + 2*3 + 3*3^2 ", poly_fn(3))
    poly_fn_b = poly(9, 8)
    print("Result of 9 + 8*10 ", poly_fn_b(10))
