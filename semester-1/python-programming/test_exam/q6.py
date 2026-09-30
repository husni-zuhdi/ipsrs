# Q6 Consider a list of integer values. Return all elements that are equal to their index in the list. Here is an example : the result for [7,5,2,8,9,3,1,2,8,1] is [2,8]
from typing import List

def same_val_idx(l: List[int]) -> List[int]:
    res = []
    for (idx, val) in enumerate(l):
        if idx == val:
            res.append(val)
    return res

if __name__ == '__main__':
    l = [7,5,2,8,9,3,1,2,8,1]
    print("same index and values: ", same_val_idx(l))

