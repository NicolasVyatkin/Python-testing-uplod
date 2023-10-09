# Non-unique Elements

# You are given a non-empty sequence of integers. For this task, you should return Iterable consisting
# of only the non-unique elements from the initial sequence. To do so you will need to remove all unique
# elements (elements which are contained in a given sequence only once). When solving this task, do not
# change the order of the elements. Example: in [1, 2, 3, 1, 3] elements 1, 3 are non-unique and result
# will be [1, 3, 1, 3].

# non-unique-elements

# Input: List of integers (int).

# Output: List or another Iterable (tuple, iterator, genetor) of integers (int).

# Examples:

# assert list(checkio([1, 2, 3, 1, 3])) == [1, 3, 1, 3]
# assert list(checkio([1, 2, 3, 4, 5])) == []
# assert list(checkio([5, 5, 5, 5, 5])) == [5, 5, 5, 5, 5]
# assert list(checkio([10, 9, 10, 10, 9, 8])) == [10, 9, 10, 10, 9]


# How it is used: This mission will help you to understand how to manipulate sequences, something that
# is the basis for solving more complex tasks. The concept can be easily generalized for real world tasks.
# For example: if you need to clarify statistics by removing low frequency elements (noise).

# You can find out more about Python lists in one of our articles featuring lists, tuples, array.array and
# numpy.array.

# Precondition:
# 0 < len(data) < 1000

################################################ SOLUTION#####################################################
from numpy import unique, asarray
from collections.abc import Iterable


def checkio(data: list[int]) -> Iterable[int]:
    return [item for item in data if data.count(item) > 1]

################################################### OR########################################################


def checkio(d): return [x for x in d if d.count(x) > 1]
################################################### OR########################################################
def checkio(d): return list(filter(lambda i: d.count(i) - 1, d))
################################################### OR########################################################


def checkio(data):
    from collections import Counter
    nonunique = Counter(data) - Counter(set(data))
    return [x for x in data if x in nonunique]

################################################### OR########################################################


def checkio(data):
    u, ri, c = unique(asarray(data), return_inverse=True, return_counts=True)
    return [int(u[i]) for i in ri if c[i] > 1]
