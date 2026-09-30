# Q1 Write a function that returns both x^2 and √x for an input number x.
def sqr_n_sqrt(x):
    return (x**2, float(x)**0.5)


if __name__ == '__main__':
    print(sqr_n_sqrt(4))
    print(sqr_n_sqrt(9.0))
    print(sqr_n_sqrt(-4))
    print(sqr_n_sqrt(-25.0))
