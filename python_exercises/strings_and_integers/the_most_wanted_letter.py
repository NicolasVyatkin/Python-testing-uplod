# The Most Wanted Letter
# You are given a text, which contains different English letters and punctuation symbols. You should find the
# most frequent letter in the text. The letter returned must be in lower case.
# While checking for the most wanted letter, casing does not matter, so for the purpose of your search, "A" == "a".
# Make sure you do not count punctuation symbols, digits and whitespaces, only letters.

# example

# If you have two or more letters with the same frequency, then return the letter which comes first in the Latin
# alphabet. For example -- "one" contains "o", "n", "e" only once for each, thus we choose "e".

# Input: A text for analysis as a string (str).

# Output: The most frequent letter in lower case as a string (str).

# Examples:

# assert checkio("Hello World!") == "l"
# assert checkio("How do you do?") == "o"
# assert checkio("One") == "e"
# assert checkio("Oops!") == "o"
# 1
# 2
# 3
# 4
# How it is used: For most decryption tasks you need to know the frequency of occurrence for various letters in a
# section of text. For example: we can easily crack a simple addition or substitution cipher if we know the frequency
# in which letters appear. This is interesting stuff for language experts!

# Precondition:
# A text contains only ASCII symbols.
# 0 < len(text) ≤ 105

################################################ SOLUTION#####################################################
import numpy as np
import string


def checkio(text: str) -> str:
    counter = 0
    to_lower = text.lower()
    most_wanted = to_lower[0]
    for i in to_lower:
        if i.isalpha():
            if to_lower.count(i) > counter:
                most_wanted = i
                counter = to_lower.count(i)
            elif to_lower.count(i) == counter:
                if i < most_wanted:
                    most_wanted = i
                    counter = to_lower.count(i)
    print('The most wanted letter in the text is', '"',
          most_wanted, '"', 'you can see it ', counter, 'times')
    return most_wanted


print("Example:")
print(checkio("Hello World!"))
################################################### OR########################################################


def checkio(text):
    """
    We iterate through latyn alphabet and count each letter in the text.
    Then 'max' selects the most frequent letter.
    For the case when we have several equal letter,
    'max' selects the first from they.
    """
    text = text.lower()
    return max(string.ascii_lowercase, key=text.count)

################################################### OR########################################################


def checkio(t): return max('abcdefghijklmnopqrstuvwxyz', key=t.lower().count)

################################################### OR########################################################


def checkio(t): return max(map(chr, range(97, 123)), key=t.lower().count)
################################################### OR########################################################


def checkio(text):
    uniq, cnts = np.unique(
        np.array([ch for ch in text.lower() if ch.isalpha()]), return_counts=1)
    return min(list(zip(uniq, cnts)), key=lambda x: (-x[1], x[0]))[0]
