# Count Divisibles in Range (simplified)  - add new solutions later

# Given two integers, n and k, the task is to count how many numbers between 1 and n (inclusive)
# are divisible by k.

# example

# Input: Two integers (int).

# Output: Integer (int).

# Examples:

# assert count_divisible(10, 2) == 5
# assert count_divisible(10, 3) == 3
# assert count_divisible(10, 5) == 2
# assert count_divisible(15, 4) == 3

# How it’s used: this function can be useful in number theory problems, statistical computations,
# and various other mathematical and practical scenarios where such a count is needed.

# Precondition:

# 1 <= k <= n <= 10**9.

################################################ SOLUTION#####################################################
def count_divisible(n: int, k: int) -> int:
    counter = 0
    for i in range(1, n+1):
        if i % k == 0:
            counter += 1

    return counter


print("Example:")
print(count_divisible(1000000000, 2))

################################################### OR########################################################
################################################### OR########################################################
################################################### OR########################################################
################################################### OR########################################################
