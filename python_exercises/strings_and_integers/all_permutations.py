# All Permutations  - add new solutions later

# Given a string, return all possible permutations of its characters, sorted alphabetically.

# example

# Input: String (str).

# Output: Iterable of strings (str).

# Examples:

# assert list(string_permutations("ab")) == ["ab", "ba"]
# assert list(string_permutations("abc")) == ["abc", "acb", "bac", "bca", "cab", "cba"]
# assert list(string_permutations("a")) == ["a"]

# How it’s used:

# puzzles and games like Scrabble where word combinations matter;
# cryptography to test possible keys given a set of characters;
# data analysis in genetics for possible gene combinations.

################################################ SOLUTION#####################################################
from collections.abc import Iterable
from itertools import permutations


def string_permutations(s: str) -> Iterable[str]:

    return sorted([''.join(p) for p in permutations(s)])


print("Example:")
print(list(string_permutations("aab")))


################################################### OR########################################################
# result = [''.join(j) for i in range(1, len(s))
#           for j in permutations(s, i)]
# result = []
# for i in permutations(s):
#     for j in i:
#         ''.join(j)
################################################### OR########################################################
# return sorted([''.join(j) for i in range(len(s), len(s)+1) for j in permutations(s, i)])
################################################### OR########################################################
################################################### OR########################################################
