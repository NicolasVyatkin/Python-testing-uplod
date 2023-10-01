# Three Words
# Let's teach the Robots to distinguish words and numbers.

# You are given a string with words and numbers separated by whitespaces (one space).
# The words contains only letters. You should check if the string contains three words in succession.
# For example, the string "start 5 one two three 7 end" contains three words in succession.

# Input: A string (str) with words.

# Output: Logic value (bool).

# Examples:

# assert checkio("Hello World hello") == True
# assert checkio("He is 123 man") == False
# assert checkio("1 2 3 4") == False
# assert checkio("bla bla bla bla") == True

# How it is used: This teaches you how to work with strings and introduces some useful functions.

# Precondition: The input contains words and/or numbers. There are no mixed words (letters and digits combined).
# 0 < len(words) < 100

################################################ SOLUTION#####################################################
import numpy as np
import re


def checkio(words: str) -> bool:
    word_counter = 0
    for word in words.split():
        if word.isalpha():
            word_counter += 1
        else:
            word_counter = 0
        if word_counter >= 3:
            return True
    return False


print("Example:")
print(checkio("Hello World hello"))
################################################### OR########################################################


def checkio(words):
    succ = 0
    for word in words.split():
        succ = (succ + 1)*word.isalpha()
        if succ == 3:
            return True
    else:
        return False

################################################### OR########################################################


def checkio(x): return "www" in "".join(
    'w' if w.isalpha() else 'd' for w in x.split())
################################################### OR########################################################


def checkio(words):
    return True if re.search('\D+\s\D+\s\D+', words) else False

################################################### OR########################################################


def checkio(words: str) -> bool:

    # find the index of words
    # use np.diff and re to check succession
    index_gap = np.diff(
        [i for i, w in enumerate(words.split(' ')) if w.isalpha()])

    index_str = ''.join([str(j) for j in index_gap])

    pattern = re.compile(r'11')

    return len(re.findall(pattern, index_str)) > 0
