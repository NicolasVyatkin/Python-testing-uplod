# Beginning Zeros

# You have a string that consist only of digits. You need to find how many zero digits ("0") are at
# the beginning of the given string.

# Input: A string (str), that consists of digits.

# Output: An integer (int).

# Examples:

# assert beginning_zeros("100") == 0
# assert beginning_zeros("001") == 2
# assert beginning_zeros("100100") == 0
# assert beginning_zeros("001001") == 2

# Precondition: 0-9

################################################ SOLUTION#####################################################
def beginning_zeros(a: str) -> int:
    zero_couner = 0
    numbers = [int(item) for item in a]
    for number in numbers:
        if numbers[0] == 0:
            if number == 0:
                zero_couner += 1
            else:
                break
    print(numbers)
    return zero_couner


print("Example:")
print(beginning_zeros("10"))
################################################### OR########################################################


def beginning_zeros(number: str) -> int:
    return len(number) - len(number.lstrip('0'))

################################################### OR########################################################


def beginning_zeros(number: str) -> int:
    str_int = str(int(number))
    return len(number) - len(str_int) + (str_int == '0')
################################################### OR########################################################


def beginning_zeros(number: str) -> int:
    return len(number) - len(number.lstrip('0'))
