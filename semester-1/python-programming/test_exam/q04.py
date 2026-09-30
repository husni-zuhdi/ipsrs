# Q4 Write a function that compute the value of π using the Bailey–Borwein–Plouffe formula :
# ![link](https://en.wikipedia.org/wiki/Bailey%E2%80%93Borwein%E2%80%93Plouffe_formula)
# the number of terms is an argument with default value 5. The different terms are returned only if
# the argument return_terms is True. Compare the result with the value of π from the math module.
def pi_bbp(x=5, return_terms: bool = False):
    if not return_terms:
        x = 5 # Reset term to default
    pi = 0.0
    for k in range(x):
        pi += (1/16**k) * ((4 / (8*k + 1)) - (2 / (8*k +4)) - (1 / (8*k + 5)) - (1 / (8*k + 6)))
    return pi

from math import pi

if __name__ == '__main__':
    print("pi from math: ", pi)
    print("pi default: ", pi_bbp(), ". Diff (%): ", ((abs(pi_bbp() - pi)) / pi)*100)
    print("pi k=10 with no return_terms: ", pi_bbp(10, False), ". Diff (%): ", ((abs(pi_bbp(10, False) - pi)) / pi)*100)
    print("pi k=10 with return_terms: ", pi_bbp(10, True), ". Diff (%): ", ((abs(pi_bbp(10, True) - pi)) / pi)*100)
    print("pi k=25 with return_terms: ", pi_bbp(25, True), ". Diff (%): ", ((abs(pi_bbp(25, True) - pi)) / pi)*100)

