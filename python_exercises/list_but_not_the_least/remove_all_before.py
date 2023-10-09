# Remove All Before

# Not all of the elements are important. What you need to do here is to remove from the sequence all of
# the elements before the given one.

# example

# For the illustration we have a sequence [1, 2, 3, 4, 5] and we need to remove all elements that go before
# 3 - which are 1 and 2.

# We have two edge cases here: (1) if a cutting element cannot be found, then the sequence shoudn't be
# changed. (2) if the sequence is empty, then it should remain empty.

# Input: List and the border element.

# Output: List or another Iterable (tuple, iterator, generator).

# Examples:

# assert list(remove_all_before([1, 2, 3, 4, 5], 3)) == [3, 4, 5]
# assert list(remove_all_before([1, 1, 2, 2, 3, 3], 2)) == [2, 2, 3, 3]
# assert list(remove_all_before([1, 1, 2, 4, 2, 3, 4], 2)) == [2, 4, 2, 3, 4]
# assert list(remove_all_before([1, 1, 5, 6, 7], 2)) == [1, 1, 5, 6, 7]

################################################ SOLUTION#####################################################
from typing import Iterable
from collections.abc import Iterable


def remove_all_before(items: list, border: int) -> Iterable:
    if border not in items:
        return items
    border_ind_in_items = items.index(border)
    return items[border_ind_in_items:]
################################################### OR########################################################


def remove_all_before(items, border):
    try:
        return items[items.index(border):]
    except ValueError:
        return items

################################################### OR########################################################


def remove_all_before(i, b): return b in i and i[i.index(b):] or i
################################################### OR########################################################


def remove_all_before(items: list, border: int) -> Iterable:

    return items[items.index(border):] if border in items else items

################################################### OR########################################################


def remove_all_before(items: list, border: int) -> Iterable:

    import numpy
    arr = numpy.array(items)
    try:
        i = list(arr).index(border)
        b = i
    except ValueError:
        b = 0
    return arr[b:]
