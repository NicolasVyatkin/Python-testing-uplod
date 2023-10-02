# Longest Common Prefix  - add new solutions later

# This function should take an list of strings and determine the longest common prefix among all the strings.
# If there is no common prefix, it should return an empty string.

# example

# Input: List of strings (str).

# Output: String (str).

# Examples:

# assert longest_prefix(["flower", "flow", "flight"]) == "fl"
# assert longest_prefix(["dog", "racecar", "car"]) == ""
# assert longest_prefix(["apple", "application", "appetizer"]) == "app"
# assert longest_prefix(["a"]) == "a"

# How it’s used:

# in autocomplete systems to suggest the most likely completion;
# in file systems to suggest directory names based on current input;
# in DNA sequence alignment to identify common substrings.

################################################ SOLUTION#####################################################
# import os


# def longest_prefix(arr: list[str]) -> str:

#     return os.path.commonprefix(arr)


################################################### OR########################################################
def longest_prefix(arr: list[str]) -> str:
    letter_groups, longest_pre = zip(*arr), ""
    # print(letter_groups, longest_pre)
    # [('f', 'f', 'f'), ('l', 'l', 'l'), ('o', 'o', 'i'), ('w', 'w', 'g')]
    for letter_group in letter_groups:
        if len(set(letter_group)) > 1:
            break
        longest_pre += letter_group[0]
    return longest_pre


print("Example:")
print(longest_prefix(["flower", "flow", "flight"]))
################################################### OR########################################################
################################################### OR########################################################
################################################### OR########################################################
