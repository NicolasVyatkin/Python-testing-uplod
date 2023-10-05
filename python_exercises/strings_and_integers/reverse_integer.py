# Reverse Integer - add more solutions

# Reverse the digits of a given integer. For instance, 1234 should become 4321. For negative integers,
# the sign should remain in the front; e.g., -123 becomes -321.

# Input: Integer (int).

# Output: Integer (int).

# Examples:

# assert reverse_digits(1234) == 4321
# assert reverse_digits(0) == 0
# assert reverse_digits(-123) == -321
# assert reverse_digits(5) == 5

# How it’s used: this function can be utilized in various algorithmic challenges, number-based puzzles,
# and certain numerical calculations.

# Precondition:

# −109 ≤ num ≤ 109.

################################################ SOLUTION#####################################################

def reverse_digits(num: int) -> int:
    result = 0
    if num > + 0:
        result = str(num)[::-1]
    else:
        result = str(num)[0]+str(num)[:0:-1]

    return int(result)


print("Example:")
print(reverse_digits(-32))
################################################### OR########################################################
################################################### OR########################################################
################################################### OR########################################################
################################################### OR########################################################
