# Right to Left

# You are given a sequence of strings. You should join these strings into a chunk of text
# where the initial strings are separated by commas. As a joke on the right handed robots,
# you should replace all cases of the words "right" with the word "left", even if it's a
# part of another word. All strings are given in lowercase.

# Input: A sequence of strings (str).

# Output: The text as a comma-separated string (str).

# Examples:

# assert left_join(("left", "right", "left", "stop")) == "left,left,left,stop"
# assert left_join(("bright aright", "ok")) == "bleft aleft,ok"
# assert left_join(("brightness wright",)) == "bleftness wleft"
# assert left_join(("enough", "jokes")) == "enough,jokes"

# How it is used: This is a simple example of operations using strings and sequences.

# Precondition:
# 0 < len(phrases) < 42

################################################ SOLUTION#####################################################

import numpy as np


def left_join(phrases: tuple[str]) -> str:
    final_str = ''
    for i in phrases:
        final_str += i+','
    final_str = final_str.replace('right', 'left')[:-1]
    return final_str


print("Example:")
print(left_join(("left", "right", "left", "stop")))
################################################### OR########################################################


def left_join(phrases):
    """
        Join strings and replace "right" to "left"
    """
    return (",".join(phrases)).replace("right", "left")
################################################### OR########################################################


def left_join(phrases):
    return ','.join(map(lambda x: x.replace('right', 'left'), phrases))
################################################### OR########################################################


def left_join(phrases):
    return ",".join(phrases).replace("right", "left")

################################################### OR########################################################


class right_to_left():
    def __init__(self, phrases):
        self.phrases = phrases

    def perform(self):
        replaced_words_array = np.array(
            [p.replace('right', 'left') for p in self.phrases])
        replaced_words_list = replaced_words_array.tolist()
        return ",".join(replaced_words_list)


def left_join(phrases: tuple) -> str:
    foo = right_to_left(phrases)
    return foo.perform()
