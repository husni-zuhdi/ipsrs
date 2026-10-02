# i) Create a function mul() that multiplies all given arguments. It can handle any number of arguments.
def mul(*args):
    res = 1
    for num in args:
        res *= num
    return res


if __name__ == "__main__":
    print("multiply of 3x4x5 : ", mul(3, 4, 5))
    print("multiply of -3x4x5 : ", mul(-3, 4, 5))
    print("multiply of 10x4x5x0.5 : ", mul(10, 4, 5, 0.5))
