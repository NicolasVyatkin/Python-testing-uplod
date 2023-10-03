# Fuzzy String Matching - unfinised

# Given two strings and a permissible number of character differences, determine if the strings can be considered
# approximately equal.

# example

# Input: Three arguments: two strings (str) and one integer (int).

# Output: Logic value (bool).

# Examples:

# assert fuzzy_string_match("apple", "appel", 2) == True
# assert fuzzy_string_match("apple", "bpple", 1) == True
# assert fuzzy_string_match("apple", "bpple", 0) == False
# assert fuzzy_string_match("apple", "apples", 1) == True

# How it’s used:

# spell-checking algorithms where slight differences can be ignored;
# searching algorithms in databases to find entries that closely match the query;
# DNA sequence matching where certain differences might be allowed.
# Precondition:

# 0 <= threshold <= max(len(str1), len(str2)).

################################################ SOLUTION#####################################################

from fuzzywuzzy import fuzz


def fuzzy_string_match(str1: str, str2: str, threshold: int) -> bool:
    counter = 0

    for a in str1:
        for b in str2:
            if a == b:
                counter += 1

    return counter


print("Example:")
print(fuzzy_string_match("apple", "appel", 2))
################################################### OR########################################################
################################################### OR########################################################
################################################### OR########################################################
################################################### OR########################################################
