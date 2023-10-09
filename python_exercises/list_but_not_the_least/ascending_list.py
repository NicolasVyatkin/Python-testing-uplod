# Ascending List

# Determine whether a sequence of elements is ascending such that each of its elements is strictly larger
# than (and not merely equal to) the preceding element. Empty sequence is considered as ascending.

# Input: List with integers (int).

# Output: Logic value (bool).

# Examples:

# assert is_ascending([-5, 10, 99, 123456]) == True
# assert is_ascending([99]) == True
# assert is_ascending([4, 5, 6, 7, 3, 7, 9]) == False
# assert is_ascending([]) == True

# The mission was taken from Python CCPS 109 Fall 2018. It is taught for Ryerson Chang School of
# Continuing Education by Ilkka Kokkarinen

################################################ SOLUTION#####################################################
import numpy
from typing import Iterable


def is_ascending(items: list[int]) -> bool:
    i = 0
    try:
        while items[i] < items[i+1]:
            i += 1
        return False
    except IndexError:
        return True

################################################### OR########################################################


def is_ascending(items: Iterable[int]) -> bool:
    return all(items[i] < items[i+1] for i in range(len(items)-1))

################################################### OR########################################################


def is_ascending(l): return all(map(int.__lt__, l, l[1:]))
################################################### OR########################################################


def is_ascending(items):
    return all(items[i] < items[i+1] for i in range(len(items) - 1))

################################################### OR########################################################


def is_ascending(items: Iterable[int]) -> bool:
    # your code here
    for i in range(len(items)):
        if items.count(items[i]) > 1:
            return False
    items2 = items.copy()
    items2.sort()
    return numpy.array_equal(items2, items)
