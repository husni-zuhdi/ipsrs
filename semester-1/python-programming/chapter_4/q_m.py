# m) Create a generator function fact(N) that yields n! for every integer n from 1 to N.
def fact(N: int):
    prev_yield = 1
    for num in range(1, N + 1):
        prev_yield *= num
        yield prev_yield
    return N


if __name__ == "__main__":
    n = 6
    res = fact(n)
    for i in range(6):
        print("Yielded at idx ", i, " is: ", next(res))
