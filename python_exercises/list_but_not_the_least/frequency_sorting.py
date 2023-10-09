# Frequency Sorting

# Sort the given sequence so that its elements should be grouped and those groups end up in the decreasing
# frequency order,
# that is, the number of times element appears in the sequence. If two elements have the same frequency,
# their groups should end up according to the natural order of elements.
# For example: [5, 2, 4, 1, 1, 1, 3] ==> [1, 1, 1, 2, 3, 4, 5].

# If you want to practice more with the similar case, try Sort Array by Element Frequency mission.

# Input: List of integers (int).

# Output: List or another Iterable (tuple, iterator, generator) of integers (int).

# Examples:

# assert list(frequency_sorting([1, 2, 3, 4, 5])) == [1, 2, 3, 4, 5]
# assert list(frequency_sorting([3, 4, 11, 13, 11, 4, 4, 7, 3])) == [
#     4,
#     4,
#     4,
#     3,
#     3,
#     11,
#     11,
#     7,
#     13,
# ]

# How it is used: For analyzing data using mathematical statistics and mathematical analysis, and for
# finding trends and predicting future changes (systems, phenomena, etc.).

# Preconditions:

# list length <= 100;
# max number <= 100.
# The mission was taken from Python CCPS 109. It is taught for Ryerson Chang School of Continuing Education
# by Ilkka Kokkarinen

################################################ SOLUTION#####################################################

import numpy as np
from typing import List
from collections import Counter
from collections.abc import Iterable


def frequency_sorting(numbers: list[int]) -> Iterable[int]:
    return sorted(sorted(numbers), key=numbers.count, reverse=True)
################################################### OR########################################################


def checkio(numbers):
    return sorted(sorted(numbers), key=numbers.count, reverse=True)
################################################### OR########################################################


def frequency_sorting(numbers):
    return sorted(numbers, key=lambda a: (-numbers.count(a), a))

################################################### OR########################################################


def frequency_sorting(numbers: List[int]) -> List[int]:
    count = Counter(numbers)
    numbers.sort(key=lambda x: (-count[x], x))
    return numbers

################################################### OR########################################################


def frequency_sorting(numbers):

    n = sorted(numbers)
    n = {i: n.count(i) for i in n}

    n_l = sorted(n, key=lambda s: n[s], reverse=True)

    m = [[i, n[i]] for i in n_l]

    c = []
    for i in m:
        i = list(np.repeat(i[0], i[1]))
        c.extend(i)
    return c
