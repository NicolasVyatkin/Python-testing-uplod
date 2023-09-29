# First Word
# I might see a simplified version of this mission already First Word (simplified).
# This mission is a little bit more complex as not only English letters can be in the given string.

# You are given a string where you have to find its first word.

# When solving a task pay attention to the following points:

# There can be dots and commas in a string.
# A string can start with a letter or, for example, one/multiple dot(s) or space(s).
# A word can contain an apostrophe and it's a part of a word.
# The whole text can be represented with one word and that's it.
# Input: A string (str).

# Output: A string (str).

# Examples:

# assert first_word("Hello world") == "Hello"
# assert first_word(" a word ") == "a"
# assert first_word("don't touch it") == "don't"
# assert first_word("greetings, friends") == "greetings"
# 1
# 2
# 3
# 4
# How it is used: the first word is a command in a command line

# Precondition: the text can contain a-z A-Z , . '

################################################ SOLUTION#####################################################
import re


def first_word(text: str) -> str:
    text = text.replace('.', ' ').replace(',', ' ').split()
    return text[0]


print("Example:")
print(first_word("Hello world"))
################################################### OR########################################################


def first_word(text: str) -> str:
    return re.search("([\w']+)", text).group(1)

################################################### OR########################################################


def first_word(t): return ''.join([x, ' '][x in '.,'] for x in t).split()[0]
################################################### OR########################################################


def first_word(text: str) -> str:
    i = 0
    while i < len(text) and text[i] in ',. ':
        i += 1
    j = i
    while j < len(text) and text[j] not in ',. ':
        j += 1
    return text[i:j]
