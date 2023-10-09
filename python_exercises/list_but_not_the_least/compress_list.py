# Compress List

# A given sequence should be "compressed" in a way so, instead of two (or more) equal elements,
# staying one after another, there should be only one in the result sequence.

# example

# Input: List.

# Output: "Compressed" List or another Iterable (tuple, iterator, generator).

# Examples:

# assert list(compress([5, 5, 5, 4, 5, 6, 6, 5, 5, 7, 8, 0, 0])) == [
#     5,
#     4,
#     5,
#     6,
#     5,
#     7,
#     8,
#     0,
# ]
# assert list(compress([1, 1, 1, 1, 2, 2, 2, 1, 1, 1])) == [1, 2, 1]
# assert list(compress([7, 7])) == [7]
# assert list(compress([])) == []

################################################ SOLUTION#####################################################
from typing import Iterable
import numpy as np
import itertools
from itertools import groupby
from collections.abc import Iterable


def compress(items: list[int]) -> Iterable[int]:
    return [items[i] for i in range(len(items)) if i == 0 or items[i] != items[i-1]]

################################################### OR########################################################


def compress(items):
    for key, _ in groupby(items):
        yield key

################################################### OR########################################################


def compress(l): return (i for i, _ in itertools.groupby(l))

################################################### OR########################################################


def compress(x): return [x[i]
                         for i in range(len(x)) if i == 0 or x[i] != x[i-1]]
################################################### OR########################################################


def compress(items: list) -> Iterable:

    if len(items) == 0:
        return items
    else:
        different = (np.diff(items) != 0)
        different = np.insert(different, 0, -1)

        return list(np.array(items)[different])
