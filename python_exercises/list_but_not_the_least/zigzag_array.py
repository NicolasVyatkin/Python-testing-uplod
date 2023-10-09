# Zigzag Array

# Your function should create a list of lists, that represents a two-dimensional grid with the given number
# of rows and cols.

# This grid should contain integers (int) from start to start + rows * cols - 1 in ascending order, but the
# elements of every
# odd-index row have to be listed in descending order, so that when read in ascending order, the numbers zigzag
# through the two-dimensional grid.

# example

# Input: Two integers (int) - rows and columns. One optional integer (int) - start.

# Output: List of lists.

# Examples:

# assert create_zigzag(3, 5) == [[1, 2, 3, 4, 5], [10, 9, 8, 7, 6], [11, 12, 13, 14, 15]]
# assert create_zigzag(5, 1) == [[1], [2], [3], [4], [5]]
# assert create_zigzag(3, 3, 5) == [[5, 6, 7], [10, 9, 8], [11, 12, 13]]

# The mission was taken from Python CCPS 109 Fall 2018. It is taught for Ryerson Chang School of Continuing
# Education by Ilkka Kokkarinen

################################################ SOLUTION#####################################################
import numpy as np
from itertools import count, islice
from typing import List
from itertools import count as count_from


def create_zigzag(rows: int, cols: int, start: int = 1) -> list[list[int]]:
    z_array = [[start+c+cols*r for c in range(cols)] for r in range(rows)]
    for (i, row) in enumerate(z_array):
        if i % 2 == 1:
            z_array[i] = list(reversed(row))
    return z_array

################################################### OR########################################################


def create_zigzag(rows: int, cols: int, start: int = 1) -> List[List[int]]:
    it = count(start)
    return [list(islice(it, cols))[::(-1)**row] for row in range(rows)]

################################################### OR########################################################


def create_zigzag(r, c, s=1, R=range): return [
    [*R(s+i*c, s+i*c+c)][::1-i % 2*2]for i in R(r)]
################################################### OR########################################################


def create_zigzag(rows: int, cols: int, start: int = 1) -> List[List[int]]:
    numbers = range(start, start+rows*cols)
    array = []
    for row in range(rows):
        array.append(list(numbers[row*cols:(row+1)*cols]))
        if row % 2 == 1:
            array[-1].reverse()
    return array

################################################### OR########################################################


def create_zigzag(rows: int, cols: int, start: int = 1) -> List[List[int]]:
    """ Return list of lists of ints, starting with start, increasing by one,
        with odd-numbered rows increasing from right to left.
    """
    if rows == 0:
        return []
    filter_e = np.array([[i % 2 == 0] for i in range(rows)])
    filter_o = np.invert(filter_e)
    result_e = np.arange(start, start+rows*cols).reshape(rows, cols)
    return (result_e * filter_e + np.fliplr(result_e) * filter_o).tolist()
