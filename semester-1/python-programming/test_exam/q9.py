# Q9 A date and time information is written as a list of six numbers with the following format [YYYY,
# MM, DD, HH, MM, SS]. Write a function that checks whether a list is a valid date and time code
# (February has 28 days, January, March, May, July, August, October and December have 31).
from typing import List


def is_valid_date(l: List[int]) -> bool:
    is_valid_year = l[0] > 0 and l[0] <= 9999
    is_valid_month = l[1] > 0 and l[1] <= 12
    is_valid_day = False
    if l[1] == 2:
        is_valid_day = l[2] > 0 and l[2] <= 28
    elif l[1] in [1, 3, 5, 7, 8, 10, 12]:
        is_valid_day = l[2] > 0 and l[2] <= 31
    else:
        is_valid_day = l[2] > 0 and l[2] <= 30
    is_valid_hour = l[3] >= 0 and l[3] <= 24
    is_valid_minute = l[4] >= 0 and l[4] <= 60
    is_valid_second = l[5] >= 0 and l[5] <= 60
    return (
        is_valid_year
        and is_valid_month
        and is_valid_day
        and is_valid_hour
        and is_valid_minute
        and is_valid_second
    )


if __name__ == "__main__":
    date_time_1 = [2010, 9, 9, 13, 39, 40]
    date_time_2 = [2010, 12, 9, 13, 0, 40]
    date_time_3 = [-90, 9, 9, 13, 39, 40]
    date_time_4 = [2010, 2, 31, 13, 39, 40]
    date_time_5 = [10000, 9, 9, 13, 39, 40]
    print("is ", date_time_1, " in correct format? : ", is_valid_date(date_time_1))
    print("is ", date_time_2, " in correct format? : ", is_valid_date(date_time_2))
    print("is ", date_time_3, " in correct format? : ", is_valid_date(date_time_3))
    print("is ", date_time_4, " in correct format? : ", is_valid_date(date_time_4))
    print("is ", date_time_5, " in correct format? : ", is_valid_date(date_time_5))
