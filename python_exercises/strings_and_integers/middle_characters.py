# Middle Characters
# You are given some string where you need to find its middle character(s). The string may contain one word,
# a few symbols or a whole sentence. If the length of the string is even, then you should return two middle characters,
# but if the length is odd, return just one. For more details look at the Example.

# example

# If you want to practice more with the similar case, try Median mission.

# Input: A string (str).

# Output: The middle character(s) as string (str).

# Examples:

# assert middle("example") == "m"
# assert middle("test") == "es"

# How it is used: for work with texts.

# Precondition: 1 <= the length of the text <= 100.

################################################ SOLUTION#####################################################
def middle(text: str) -> str:
    middle_sumbols = ''
    if len(text) % 2 == 0:
        middle_sumbols = text[int(len(text)/2-1)]+text[int(len(text)/2)]
    else:
        middle_sumbols = text[int(len(text)/2)]

    return middle_sumbols


print("Example:")
print(middle("example"))
################################################### OR########################################################


def middle(text):
    n = len(text) // 2 + 1
    return text[-n:n]
################################################### OR########################################################


def middle(text):
    n = len(text) // 2
    return text[~n:n+1]
################################################### OR########################################################


def middle(text):
    return (text[(len(text)-1)//2:(len(text)-1)//2*-1] or text)

################################################### OR########################################################
