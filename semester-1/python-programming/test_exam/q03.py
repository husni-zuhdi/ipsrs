# Q3 A year Y is a leap year if it is either :
# (a) a multiple of 4 and not a multiple of 100
# (b) a multiple of 400
# Write a function that checks whether a year is a leap year or not. Test it on the following years :
# 1900, 2000, 2008, 2018
def leap_year(year: int) -> bool:
    if year % 400 == 0:
        return True
    if year % 4 == 0 and year % 100 != 0:
        return True
    return False

if __name__ == '__main__':
    print("1900 is a leap year: ", leap_year(1900))
    print("2000 is a leap year: ", leap_year(2000))
    print("2008 is a leap year: ", leap_year(2008))
    print("2018 is a leap year: ", leap_year(2018))
