# First Word (simplified)
# You are given a string and you have to find its first word.

# The input string consists of only English letters and spaces.
# There aren�t any spaces at the beginning and the end of the string.
# Input: A string (str).

# Output: A string (str).

# Examples:

# assert first_word("Hello world") == "Hello"
# assert first_word("a word") == "a"
# assert first_word("greeting from CheckiO Planet") == "greeting"
# assert first_word("hi") == "hi"

# How it is used: The first word is a command in a command line.

# Precondition: The text can contain a-z, A-Z and spaces.

###################### SOLUTION######################
def first_word(text: str) -> str:
    first_word = []
    first_word = text.split(' ')

    return first_word[0]


print("Example:")
print(first_word("Hello world"))
######################### OR#########################


def first_word(text):
    index = text.find(" ")
    return text[:index] if index != -1 else text

######################### OR#########################


def first_word(s): return s.split()[0]
######################### OR#########################


def first_word(text: str) -> str:
    i = 0
    while i < len(text) and text[i] != ' ':
        i += 1
    return text[:i]
