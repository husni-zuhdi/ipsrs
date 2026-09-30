# Q5 A matrix can be represented by a list of lists. For example : M = [[1, 4, 2], [3, 0, 5], [2, 1, 3]]. Write a
# function that finds the largest element of such a matrix and returns both its value and its position
# (row and column index). For the matrix above, the function should return (5, 1, 2).
from typing import List


def max_val(M: List[List[int]]):
    max = (0, 0, 0)
    for y, row in enumerate(M):
        for x, val in enumerate(row):
            if val > max[0]:
                max = (val, y, x)
    return max

if __name__ == '__main__':
    M = [[1, 4, 2], [3, 0, 5], [2, 1, 3]]
    N = [[1, 10, 2], [3, 0, 5], [2, 1, 3]]
    print("max value of M: ", max_val(M))
    print("max value of N: ", max_val(N))
