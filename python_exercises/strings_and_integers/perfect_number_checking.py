# Perfect Number Checking - add new solutions later

# A perfect number is a positive integer that is equal to the sum of its proper divisors, excluding itself.
# For example, 28 is a perfect number because its divisors are 1, 2, 4, 7, and 14, and their sum is 28.

# Input: Integer (int).

# Output: Logic value (bool).

# Examples:

# assert is_perfect(6) == True
# assert is_perfect(2) == False
# assert is_perfect(28) == True
# assert is_perfect(20) == False

# How it’s used: perfect numbers have a historical significance in number theory and have been studied in
# various mathematical and mystical contexts. This function could be useful in mathematical research,
# cryptography, or just general problem-solving.

# Precondition:

# 1 <= n <= 10**8

################################################ SOLUTION#####################################################
def is_perfect(n: int) -> bool:
    dividors = []
    perfect_dividors = []

    for i in range(1, n):
        dividors.append(i)
    for i in dividors:
        if n % i == 0:
            perfect_dividors.append(i)
    return True if sum(perfect_dividors) == n else 0


print("Example:")
print(is_perfect(28))

################################################### OR########################################################
################################################### OR########################################################
################################################### OR########################################################
################################################### OR########################################################
