# The Cheapest Flight

# As the input you get the flight schedule as an list, each element of which is the price of a direct flight
# between 2 cities (list of 3 elements - 2 city names as a string, and a flight price).

# Planes fly in both directions and the price in both directions is the same. There is a possibility that there
# are no direct flights between cities.

# Find the price of the cheapest flight between cities that are given as the 2nd and 3rd arguments. In case the
# flight can not be performed, return 0.

# Input: 3 arguments: the flight schedule as a list of lists, city of departure and destination city as strings.

# Output: The best price as integer.

# Examples:

# assert (
#     cheapest_flight([["A", "C", 100], ["A", "B", 20], ["B", "C", 50]], "A", "C") == 70
# )
# assert (
#     cheapest_flight([["A", "C", 100], ["A", "B", 20], ["B", "C", 50]], "C", "A") == 70
# )
# assert (
#     cheapest_flight(
#         [
#             ["A", "C", 40],
#             ["A", "B", 20],
#             ["A", "D", 20],
#             ["B", "C", 50],
#             ["D", "C", 70],
#         ],
#         "D",
#         "C",
#     )
#     == 60
# )
# assert (
#     cheapest_flight([["A", "C", 100], ["A", "B", 20], ["D", "F", 900]], "A", "F") == 0
# )

# How it can be used: In everyday life to find the optimal combination.

# Preconditions:

# price is always integer;
# the flight schedule contains at least one element;
# both cities are in the schedule.

################################################ SOLUTION#####################################################
import numpy as np
from scipy.sparse.csgraph import dijkstra
from typing import List


def cheapest_flight(costs: List, kai: str, jie: str) -> int:
    a = costs
    start = kai
    end = jie

    if start > end:
        yy = start
        start = end
        end = yy

    jihe = []
    for i in a:
        if i[0] not in jihe:
            jihe.append(i[0])
        if i[1] not in jihe:
            jihe.append(i[1])
    ss = 0
    num = []

    def pick(a, start, end, jihe, ss, num):
        for j in a:
            if (j[0] == end and j[1] == start) or (j[0] == start and j[1] == end):
                num.append(j[2])
                a.remove(j)
        x = []
        for i in range(0, len(a)-1):
            for j in range(i+1, len(a)):
                if a[i][0] == a[j][1]:
                    x.append([a[i][1], a[j][0], a[i][2]+a[j][2]])
                elif a[i][1] == a[j][0]:
                    x.append([a[i][0], a[j][1], a[i][2]+a[j][2]])
                elif a[i][1] == a[j][1]:
                    x.append([a[i][0], a[j][0], a[i][2]+a[j][2]])
                elif a[i][0] == a[j][0]:
                    x.append([a[i][1], a[j][1], a[i][2]+a[j][2]])

        for j in x:
            if (j[0] == end and j[1] == start) or (j[0] == start and j[1] == end):
                num.append(j[2])
                x.remove(j)

        for i in a:
            for j in x:
                if (j[0] == i[0] and j[1] == i[1] and j[2] >= i[2]) or (j[0] == i[1] and j[1] == i[0] and j[2] >= i[2]):
                    x.remove(j)
        for j in x:
            a.append(j)
        x = []
        ss += 1
        if ss < len(jihe)-1:
            return pick(a, start, end, jihe, ss, num)
        elif ss == len(jihe)-1:
            xxx = sorted(num)
        if xxx != []:
            return xxx[0]
        else:
            return 0

    return pick(a, start, end, jihe, ss, num)
################################################### OR########################################################


def cheapest_flight(data, start, stop):
    stack, found, best = [(start, 0)], False, 1e9
    while stack:
        path, price = stack.pop()
        if path[-1] == stop:
            best, found = min(best, price), True
            continue
        for a, b, p in data:
            stack += [(path+b, price+p)]*(a == path[-1] and b not in path)
            stack += [(path+a, price+p)]*(b == path[-1] and a not in path)
    return best*found

################################################### OR########################################################


def cheapest_flight_1(costs, a: str, b: str):
    if a == b:
        return 0
    else:
        costs += [[s[1], s[0], s[2]] for s in costs]
        try:
            return min(s[2] + cheapest_flight_1([t for t in costs if a not in t], s[1], b) for s in costs if a == s[0])
        except ValueError:
            return 2e30


def cheapest_flight(costs, a, b):
    return 0 if cheapest_flight_1(costs, a, b) >= 2e30 else cheapest_flight_1(costs, a, b)

################################################### OR########################################################


def matrix_genetor(vex_num):
    data_matrix = []
    for i in range(vex_num):
        one_list = []
        for j in range(vex_num):
            one_list.append(9999)
        data_matrix.append(one_list)
    return data_matrix


def c_index(x): return ord(str(x)) - ord("A")


def cheapest_flight(costs: List, a: str, b: str) -> int:
    nums_vertex = 0
    for cost in costs:
        nums_vertex = max(c_index(cost[0]), c_index(cost[1])) + 1
    matrix = matrix_genetor(nums_vertex)
    for cost in costs:
        u, v, c = cost
        matrix[c_index(u)][c_index(v)] = c
        matrix[c_index(v)][c_index(u)] = c

    for k in range(nums_vertex):
        for i in range(nums_vertex):
            for j in range(nums_vertex):
                matrix[i][j] = min(matrix[i][j], matrix[i][k] + matrix[k][j])

    result = matrix[c_index(a)][c_index(b)]
    return 0 if result == 9999 else result

################################################### OR########################################################


def cheapest_flight(costs: List, a: str, b: str) -> int:
    cities = set()
    for cost in costs:
        cities.update({cost[0], cost[1]})
    cities = sorted(cities)
    graph = np.zeros((len(cities), len(cities)))
    for city1, city2, cost in costs:
        graph[cities.index(city1)][cities.index(city2)] = cost
    m = dijkstra(graph, directed=False)
    dist = m[cities.index(a)][cities.index(b)]
    return int(dist) if dist >= 0 and dist != np.inf else 0
