# Sum of Integers - add more solutions

# Calculate sum of integers from 1 to given N (including).

# example

# Input: Integer (int).

# Output: Integer (int).

# Examples:

# assert sum_upto_n(1) == 1
# assert sum_upto_n(2) == 3
# assert sum_upto_n(3) == 6
# assert sum_upto_n(4) == 10

# How it’s used: this function can be used in a variety of mathematical and algorithmic contexts, such as in calculating the nth triangular number,
# determining the cost for certain operations in algorithms, etc.

# Precondition:

# 1 ≤ N ≤ 900.

################################################ SOLUTION#####################################################

def sum_upto_n(N: int) -> int:

    return sum(range(N+1))


print("Example:")
print(sum_upto_n(2))
################################################### OR########################################################
################################################### OR########################################################
################################################### OR########################################################
################################################### OR########################################################
