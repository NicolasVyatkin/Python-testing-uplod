# Sort Except Zero

# Sort the integers in sequence in sequence. But the position of zeros should not be changed.

# Input: List of integers (int).

# example

# Output: List or another Iterable (tuple, generator, iterator) of integers (int).

# Examples:

# assert list(except_zero([5, 3, 0, 0, 4, 1, 4, 0, 7])) == [1, 3, 0, 0, 4, 4, 5, 0, 7]
# assert list(except_zero([0, 2, 3, 1, 0, 4, 5])) == [0, 1, 2, 3, 0, 4, 5]
# assert list(except_zero([0, 0, 0, 1, 0])) == [0, 0, 0, 1, 0]
# assert list(except_zero([4, 5, 3, 1, 1])) == [1, 1, 3, 4, 5]

# Precondition:

# All numbers are non-negative.

################################################ SOLUTION#####################################################
import numpy
from typing import Iterable, List
from typing import Iterable
from collections.abc import Iterable


def except_zero(items: list[int]) -> Iterable[int]:
    zero_index = []
    no_ziroe_list = []
    for i in range(len(items)):
        if items[i]:
            no_ziroe_list.append(items[i])
        else:
            zero_index.append(i)
    no_ziroe_list.sort()
    for j in zero_index:
        no_ziroe_list.insert(j, 0)
    return no_ziroe_list

################################################### OR########################################################


def except_zero(items: list) -> Iterable:
    # make iterator for sorted non-zero element
    it = iter(sorted(e for e in items if e))
    # insert 0
    yield from [next(it) if e else 0 for e in items]
################################################### OR########################################################


def except_zero(L):
    s = iter(sorted(filter(None, L)))
    return [x and next(s) for x in L]

################################################### OR########################################################


def except_zero(items: List[int]) -> Iterable[int]:
    sorted_non_zeros = sorted((item for item in items if item))
    i = 0
    for item in items:
        if not item:
            yield 0
            continue
        yield sorted_non_zeros[i]
        i += 1

################################################### OR########################################################


def except_zero(items):
    items = numpy.r_[items]
    items[items != 0] = sorted(items[items != 0])
    return items
