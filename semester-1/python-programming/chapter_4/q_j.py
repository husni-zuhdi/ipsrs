# Create a function sumdebug() that sums all given values. It can handle any number of values, and an
# optional debug argument, that if set to True , also displays the supplied values.
def sumdebug(debug=False, *args):
    if debug == True:
        print("Arguments: ", args)
    res = 0
    for num in args:
        res += num
    return res


if __name__ == "__main__":
    print("sum of 3+4+5 : ", sumdebug(3, 4, 5))
    print("sum of -3+4+5 with debug flag: ", sumdebug(True, -3, 4, 5))
    print("sum of 10+4+5+0.5 : ", sumdebug(10, 4, 5, 0.5))
