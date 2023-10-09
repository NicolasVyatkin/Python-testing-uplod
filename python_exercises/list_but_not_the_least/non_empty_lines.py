# Non Empty Lines


# You need to count how many non-empty lines a given text has.

# An empty line is a line without symbols or the one that contains only spaces.

# Input: A text (str).

# Output: An integer (int).

# Examples:

# assert non_empty_lines("one simple line\n") == 1
# assert non_empty_lines("") == 0
# assert non_empty_lines("\nonly one line\n            ") == 1
# assert (
#     non_empty_lines(
#         "\nLorem ipsum dolor sit amet,\n\nconsectetur adipiscing elit\nNam odio nisi, aliquam\n            "
#     )
#     == 3
# )

################################################ SOLUTION#####################################################
import numpy as np
import re


def non_empty_lines(text: str) -> int:
    new_text = repr(text.replace('\n', '.')).replace(' ', '').replace(
        ',', '').replace("'", '').replace("?", '').split('.')
    print(new_text)
    counter = 0
    for i in new_text:
        if i.lower().isalpha():
            counter += 1
    return counter
################################################### OR########################################################


def non_empty_lines(text: str) -> int:
    return sum(bool(line.strip()) for line in text.splitlines())

################################################### OR########################################################


class line_counter:
    '''
    This is a pointless class, but trying to use 'with'
    for something other than managing external resources
    since CheckiO missions don't seem to use external data.

    Has anyone found a use for 'with' in CheckiO?
    '''

    def __init__(self, text):
        self.text = text

    def __enter__(self):
        return self

    def __exit__(self, *exc):
        return

    def count(self):
        return len([line for line in self.text.splitlines() if not re.fullmatch(' *', line)])


def non_empty_lines(text: str) -> int:
    with line_counter(text) as lines:
        return lines.count()

################################################### OR########################################################


def non_empty_lines(text: str) -> int:
    # your code here
    lines = text.split("\n")
    # remove empty spaces
    lines = np.array([line.strip() for line in lines])
    # extract all non empty values by using boolean mask
    lines_not_empty = lines[lines != ""]
    return len(lines_not_empty)
