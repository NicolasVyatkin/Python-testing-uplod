# Reverse Every Ascending

# Create and return a new Iterable that contains the same elements as the given list items, but with
# the reversed order of the
# elements inside every maximal strictly ascending subsequence. This function should not modify the
# contents of the original list.

# example

# Input: List of integers (int).

# Output: List or another Iterable (tuple, iterator, generator) of integers (int).

# Examples:

# assert list(reverse_ascending([1, 2, 3, 4, 5])) == [5, 4, 3, 2, 1]
# assert list(reverse_ascending([5, 7, 10, 4, 2, 7, 8, 1, 3])) == [
#     10,
#     7,
#     5,
#     4,
#     8,
#     7,
#     2,
#     3,
#     1,
# ]
# assert list(reverse_ascending([5, 4, 3, 2, 1])) == [5, 4, 3, 2, 1]
# assert list(reverse_ascending([])) == []

# Precondition: given sequence includes only integers.

# The mission was taken from Python CCPS 109 Fall 2018. It’s being taught for Ryerson Chang School of
# Continuing Education by Ilkka Kokkarinen

################################################ SOLUTION#####################################################
import numpy as np
from numpy import split as s, where as w, diff as d
from collections.abc import Iterable


def reverse_ascending(items: list[int]) -> Iterable[int]:
    result_list = []
    start_elem = 0
    for i in range(1, len(items)):
        if items[i] <= items[i-1]:
            result_list += items[start_elem:i][::-1]
            start_elem = i
    return result_list+items[start_elem:][::-1]
################################################### OR########################################################
# to_list = lambda f: lambda *args, **kwargs: list(f(*args, **kwargs))

# @to_list # Outputs doesn't have to be lists in "Check" tests.


def reverse_ascending(iterable):
    ascending = []
    for elem in iterable:
        if ascending and ascending[-1] >= elem:
            yield from reversed(ascending)
            ascending = []
        ascending.append(elem)
    yield from reversed(ascending)

################################################### OR########################################################


def reverse_ascending(t): return sum(
    [list(x)[::-1] for x in s(t, w(d(t) <= 0)[0]+1)], [])
################################################### OR########################################################


def reverse_ascending(items):
    for s in range(1, len(items)):
        if items[s] <= items[s-1]:
            return items[:s][::-1]+reverse_ascending(items[s:])
    return items[::-1]

################################################### OR########################################################


def reverse_ascending(items):
    new_list = list()

    result = np.split(items, np.where(np.diff(items) <= 0)[0] + 1)

    for item in result:
        new_list.extend(sorted(list(item), reverse=True))

    return new_list
