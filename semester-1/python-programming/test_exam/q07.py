# Q7 Write a function that computes the k smallest values of a list of integers. Both the list and the
# value of k are arguments of the function. Describe this function with a docstring.
from typing import List

def min_values(l: List[int], k: int) -> List[int]:
    """
    min_values take arguments l as list of integers and k as an integer that
    represent the count of the smallest values in the list. Returned the list of
    k smallest values 
    """
    sorted_l = sorted(l)
    return sorted_l[0:k]

if __name__ == '__main__':
    l = [7,5,2,8,9,3,1,2,8,1, 0]
    print("smallest 3 values of the list: ", min_values(l, 3))
