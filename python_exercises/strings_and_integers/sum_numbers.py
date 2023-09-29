# Sum Numbers
# In a given text you need to sum the numbers while excluding any digits that form part of a word.

# The text consists of numbers, spaces and letters from the English alphabet.

# Input: A string (str).

# Output: An integer (int).

# Examples:

# assert sum_numbers("hi") == 0
# assert sum_numbers("who is 1st here") == 0
# assert sum_numbers("my numbers is 2") == 2
# assert (
#     sum_numbers(
#         "This picture is an oil on canvas painting by Danish artist Anna Petersen between 1845 and 1910 year"
#     )
#     == 3755
# )

################################################ SOLUTION#####################################################
def sum_numbers(text: str) -> int:
    new_list = text.split(' ')
    sum_num_in_line = 0
    for i in new_list:
        if i.isnumeric():
            sum_num_in_line = sum_num_in_line+int(i)

    return sum_num_in_line


print("Example:")
print(sum_numbers("hi"))
################################################### OR########################################################


def sum_numbers(text): return sum(int(word)
                                  for word in text.split() if word.isdigit())


################################################### OR########################################################
sum_numbers = lambda t, r=__import__("re").compile(
    r'\b\d+\b'): sum(map(int, r.findall(t)))
################################################### OR########################################################


def sum_numbers(text: str) -> int:
    return sum(map(int, filter(str.isdigit, text.split())))
