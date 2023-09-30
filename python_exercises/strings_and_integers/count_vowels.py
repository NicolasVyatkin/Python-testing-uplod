# Count Vowels - edit later

# This function should take a string as an input and return the count of vowels (a, e, i, o, u) in the string.
# The function should be case-insensitive.

# example

# Input: String (str).

# Output: Integer (int).

# Examples:

# assert count_vowels("hello") == 2
# assert count_vowels("openai") == 4
# assert count_vowels("typescript") == 2
# assert count_vowels("a") == 1

# How it’s used:

# in natural language processing tasks, like text analysis and statistics;
# in text-based games or learning applications, for instance, to calculate the difficulty level of a word or phrase.
# Preconditions:

# text ∈ string;
# length(text) >= 0.

################################################ SOLUTION#####################################################
VOWELS = 'aeiouAEIOU'


def count_vowels(text: str) -> int:
    counter = 0
    for i in text:
        if i in VOWELS:
            counter += 1
    return counter


print("Example:")
print(count_vowels("The quick brown fox"))

################################################### OR########################################################
################################################### OR########################################################
################################################### OR########################################################
################################################### OR########################################################
