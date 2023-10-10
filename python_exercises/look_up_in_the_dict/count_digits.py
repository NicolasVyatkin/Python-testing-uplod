# Count Digits

# You need to count the number of digits in a given string.

# Input: String.

# Output: Integer.

# Examples:

# assert count_digits("hi") == 0
# assert count_digits("who is 1st here") == 1
# assert count_digits("my numbers is 2") == 1
# assert (
#     count_digits(
#         "This picture is an oil on canvas painting by Danish artist Anna Petersen between 1845 and 1910 year"
#     )
#     == 8
# )

################################################ SOLUTION#####################################################
def count_digits(text: str) -> int:
    counter = 0
    for i in text:
        if i.isdigit():
            counter += 1

    return counter


print("Example:")
print(count_digits("hi"))
################################################### OR########################################################


def count_digits(text: str) -> int:
    return sum(c.isdigit() for c in text)
################################################### OR########################################################


def count_digits(text: str) -> int:
    return sum(text.count(digit) for digit in '1234567890')
################################################### OR########################################################


def count_digits(text: str) -> int:
    return sum(map(str.isdigit, text))
################################################### OR########################################################


def count_digits(text: str) -> int:
    import numpy as np
    new_text = text.replace(" ", "")
    n = np.array([])
    m = np.array([])
    for i in new_text:
        try:
            n = np.append(n, int(i))
        except:
            res = 0

    return (len(n))
