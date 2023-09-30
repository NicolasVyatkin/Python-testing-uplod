# The Longest Word - edit later

# This function should take a string without punctuation marks as an input and return the longest word in the string.
# If there are multiple words of the same length, return the first one that appears.

# example

# Input: String (str).

# Output: String (str).

# Examples:

# assert longest_word("hello world") == "hello"
# assert longest_word("openai gpt-4") == "openai"
# assert longest_word("this is a sentence") == "sentence"
# assert longest_word("the quick brown fox") == "quick"

# How it’s used:

# in natural language processing tasks, like text analysis;
# in search algorithms, to find key words or tags in a text.
# Preconditions:

# sentence ∈ string;
# length(sentence) >= 0.

################################################ SOLUTION#####################################################
def longest_word(sentence: str) -> str:
    sentence_list = sentence.split()
    sentence_len = []
    for i in sentence_list:
        sentence_len.append(len(i))
    return sentence_list[sentence_len.index(max(sentence_len))] if sentence != '' else sentence


print("Example:")
print(longest_word(""))
################################################### OR########################################################
################################################### OR########################################################
################################################### OR########################################################
################################################### OR########################################################
