# Create a function reduce(iterable, func) that applies the function func(a, b) two by two for each
# element of iterable , so that the result is a single value.
from typing import Iterable


def reduce(iterable: Iterable, func):
    # Initiate first value
    res = iterable[0]

    # Get enum with nice and handful index
    for idx, num in enumerate(iterable):
        # Skip first index as it already in the init value of res
        if idx == 0:
            continue
        res = func(res, num)
    return res


def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mult(a, b):
    return a * b


if __name__ == "__main__":
    print("sum of 3+4+5 : ", reduce([3, 4, 5], add))
    print("sub of 200-10-20 : ", reduce([200, 10, 20], sub))
    print("sum of 1*2*3 : ", reduce([1, 2, 3], mult))
