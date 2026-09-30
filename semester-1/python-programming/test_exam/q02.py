# Q2 Write a function that returns the opposite of a number (meaning −x for an input x) if it is even and its inverse if it is odd. Print an error message if x is zero
def opp_or_inv(x):
    if x == 0:
        return 0
    if x % 2 == 0:
        return -x
    else:
        return 1/x

if __name__ == '__main__':
    print(opp_or_inv(4))
    print(opp_or_inv(9.0))
    print(opp_or_inv(0))
    print(opp_or_inv(-4))
    print(opp_or_inv(-25.0))
