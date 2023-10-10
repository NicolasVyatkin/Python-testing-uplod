# Golden Pyramid

# Our Robo-Trio need to train for future journeys and treasure hunts. Stephan has built a special flat model
# of a pyramid. Now the robots can train for speed gold running. They start at the top of the pyramid and must
# collect gold in each room, choose to take the left or right path and continue down to the next level. To
# optimize their gold runs, Stephan need to know the maximum amount of gold that can be collected in one run.

# Consider a list of lists in which the first list has one integer and each consecutive list has one more
# teger then the last. Such a list of lists would look like a pyramid. You should write a program that will
# help Stephan find the highest possible sum on the most profitable route down the pyramid. All routes down the
# pyramid involve stepping down and to the left or down and to the right.

# Tips: Think of each step down to the left as moving to the same index location or to the right as one index
# location higher. Be very careful if you plan to use recursion here.

# sum-in-triangles

# Input: A pyramid as a list of lists of integers.

# Output: The maximum possible sum as an integer.

# Examples:

# assert (
#     count_gold(
#         [
#             [1],
#             [2, 3],
#             [3, 3, 1],
#             [3, 1, 5, 4],
#             [3, 1, 3, 1, 3],
#             [2, 2, 2, 2, 2, 2],
#             [5, 6, 4, 5, 6, 4, 3],
#         ]
#     )
#     == 23
# )
# assert (
#     count_gold(
#         [
#             [1],
#             [2, 1],
#             [1, 2, 1],
#             [1, 2, 1, 1],
#             [1, 2, 1, 1, 1],
#             [1, 2, 1, 1, 1, 1],
#             [1, 2, 1, 1, 1, 1, 9],
#         ]
#     )
#     == 15
# )
# assert count_gold([[9], [2, 2], [3, 3, 3], [4, 4, 4, 4]]) == 18
# assert (
#     count_gold(
#         [[2], [7, 9], [0, 8, 6], [4, 7, 6, 8], [0, 5, 5, 4, 1], [9, 1, 0, 1, 6, 9]]
#     )
#     == 35
# )

# How it is used: this is a classical problem which shows you how to use dynamic programming. This concept
# is a core component of many optimizations tasks.

# Preconditions:

# 0 < len(pyramid) ≤ 20;
# all(all(0 < x < 10 for x in row) for row in pyramid).

################################################ SOLUTION#####################################################
import numpy


def count_gold(pyramid: list[list[int]]) -> int:
    pyramid = [list(t) for t in pyramid]
    for y in range(1, len(pyramid)):
        for x in range(len(pyramid[y])):
            l = 0 if x == 0 else pyramid[y - 1][x - 1]
            r = 0 if x >= len(pyramid[y - 1]) else pyramid[y - 1][x]
            pyramid[y][x] += max(l, r)
    return max(pyramid[-1])


print("Example:")
print(
    count_gold(
        [
            [1],
            [2, 3],
            [3, 3, 1],
            [3, 1, 5, 4],
            [3, 1, 3, 1, 3],
            [2, 2, 2, 2, 2, 2],
            [5, 6, 4, 5, 6, 4, 3],
        ]
    )
)
################################################### OR########################################################


def count_gold(pyramid):
    py = [list(i) for i in pyramid]
    for i in reversed(range(len(py)-1)):
        for j in range(i+1):
            py[i][j] += (max(py[i+1][j], py[i+1][j+1]))

    return py[0][0]

################################################### OR########################################################


def count_gold(p): return __import__("functools").reduce(lambda D, r: [x+max(D[j], D[j+1])
                                                                       for j, x in enumerate(r)], p[-2::-1], list(p[-1]))[0]
################################################### OR########################################################


def count_gold(pyramid):
    l = len(pyramid)-1
    zv = [list(format(x, '0'+str(l)+'b')) for x in range(2**l)]
    im = [[0]+list(numpy.cumsum([int(x) for x in l])) for l in zv]
    ms = max([sum([x[i] for i, x in zip(iv, pyramid)]) for iv in im])
    return ms
