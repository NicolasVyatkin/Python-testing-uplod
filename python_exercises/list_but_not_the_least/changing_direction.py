# Changing direction

# You are given a sequence of integers. Your task in this mission is to find, how many times the sorting
# direction was changed in the given sequence. If the elements are equal - the previous sorting direction
# remains the same, if the sequence starts from the same elements - look for the next different to determine
# the sorting direction.

# Let's look at the scheme:

# changing_dir

# There are three sorting directions:

# on the chunk 1, 2, 2 - up (increasing);
# on the chunk 2, 1 - down (decreasing);
# and on the chunk 1, 2, 2 - up again.
# So, you have two points of changing the sorting direction: #1 - from up to down, and #2 - from down to up.
# That's the result your function should return.
# Input: List of integers (int).

# Output: An integer (int).

# Examples:

# assert changing_direction([1, 2, 3, 4, 5]) == 0
# assert changing_direction([1, 2, 3, 2, 1]) == 1
# assert changing_direction([1, 2, 2, 1, 2, 2]) == 2

# Preconditions:

# the sequence is non-empty;
# the elements are positive integers.

################################################ SOLUTION#####################################################
from scipy.signal import argrelmin, argrelmax
from itertools import groupby
from numpy import array
from typing import List
from itertools import pairwise
from typing import Iterable
from operator import sub
from itertools import groupby, pairwise, starmap


def changing_direction(elements: list[int]) -> int:
    dirs = []
    for i, j in zip(elements, elements[1:]):
        if j > i and (not dirs or dirs[-1] == '-'):
            dirs.append('+')
        elif j < i and (not dirs or dirs[-1] == '+'):
            dirs.append('-')

    return len(dirs) - bool(dirs)
################################################### OR########################################################


def changing_direction(elements: list) -> int:
    dir = count = 0
    for a, b in zip(elements, elements[1:]):
        dir2 = a - b
        if dir2:
            if dir2 * dir < 0:
                count += 1
            dir = dir2
    return count

################################################### OR########################################################


def changing_direction(directions: Iterable[int]) -> int:
    nonzero_diffs = filter(None, starmap(sub, pairwise(directions)))
    signed_groups = groupby(nonzero_diffs, key=lambda x: x > 0)
    nb_signs = sum(1 for _ in signed_groups)
    nb_changes = max(0, nb_signs - 1)
    return nb_changes

################################################### OR########################################################


def changing_direction(e: list) -> int:
    return sum(x*y < 0 for x, y in pairwise(x-y for x, y in pairwise(e) if x != y))

################################################### OR########################################################


def changing_direction(elements: List[int]) -> int:

    # remove consecutive elements to have unique minima and maxima
    elements = [value for value, _ in groupby(elements)]

    # convert to numpy array to use agrelmin/max
    elements = array(elements)

    # find all minima and maxima
    minima, = argrelmin(elements)
    maxima, = argrelmax(elements)

    # read amounts
    num_of_minima, = minima.shape
    num_of_maxima, = maxima.shape

    return num_of_minima + num_of_maxima
