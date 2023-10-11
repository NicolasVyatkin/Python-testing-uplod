# Adjacent Letters - add more solutions

# You are given a string, where all letters are of same case. This string could include adjacent letters -
# two the same letters together ("aa", "bb" etc). Your task in this mission is to remove both these letters.
# If after removing one pair a new appears - remove it as well! Each such pair should be removed from string
# until no one remains. Good luck!

# Input: String (str).

# Output: String (str).

# Examples:

# assert adjacent_letters("adjacent_letters") == "adjacent_lrs"
# assert adjacent_letters("") == ""
# assert adjacent_letters("aaa") == "a"
# assert adjacent_letters("ABBA") == ""

################################################ SOLUTION#####################################################
def adjacent_letters(line: str) -> str:

    stack = []
    for s in line:
        if stack and stack[~0] == s:
            stack.pop()
        else:
            stack.append(s)
    return ''.join(stack)


print("Example:")
print(adjacent_letters("adjacent_letters"))  # == "adjacent_lrs"
################################################### OR########################################################
################################################### OR########################################################
################################################### OR########################################################
################################################### OR########################################################
