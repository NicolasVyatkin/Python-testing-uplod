# Fibonacci Poem - add more solutions later

# This mission is inspired by the following Brian Bilston's facebook post:

# poem

# Split a given text into multiline one with "\n", where each line includes number of words equal to the
# current Fibonacci number.

# Here are some clarifications:

# Fibonacci sequence starts from 0, 1, but the result string should include only non-empty lines;
# in case, there are not enough words for current line - complement to proper length with "_";
# punctuation marks are considered as a part of a previous or next word.
# Let's look at the schematic example ("w" for a word):

# "w w w w w w w w" -> '''w
#                         w
#                         w w
#                         w w w
#                         w _ _ _ _'''
# Input: A string (str).

# Output: A string (str).

# Examples:

# assert fibo_poem("") == ""
# assert fibo_poem("Django framework") == "Django\nframework"
# assert fibo_poem("Zen of Python") == "Zen\nof\nPython _"
# assert (
#     fibo_poem("There are three kinds of lies: Lies, damned lies, and the benchmarks.")
#     == "There\nare\nthree kinds\nof lies: Lies,\ndamned lies, and the benchmarks."
# )

################################################ SOLUTION#####################################################
def fibo_poem(text: str) -> str:
    f_0, f, res, text_list = 0, 1, [], text.split()
    while text_list:
        if len(text_list) < f:
            text_list.extend('_' * (f - len(text_list)))
        res.append(text_list[:f])
        text_list = text_list[f:]
        f_0, f = f, f_0 + f
    return '\n'.join(' '.join(k) for k in res)


print("Example:")
print(fibo_poem("Zen of Python"))
################################################### OR########################################################
################################################### OR########################################################
################################################### OR########################################################
################################################### OR########################################################
