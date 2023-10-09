# Backward Each Word

# In a given string you should reverse every word, but the words should stay in their places.

# Input: A string (str).

# Output: A string (str).

# Examples:

# assert backward_string_by_word("") == ""
# assert backward_string_by_word("world") == "dlrow"
# assert backward_string_by_word("hello world") == "olleh dlrow"
# assert backward_string_by_word("hello   world") == "olleh   dlrow"

################################################ SOLUTION#####################################################
def backward_string_by_word(text: str) -> str:
    word_list = text.split(' ')
    new_list = []
    final_text = ''
    for i in word_list:
        new_list.append(i[::-1])
    for i in new_list:
        final_text += i+' '
    return final_text[:-1]
################################################### OR########################################################


def backward_string_by_word(text):
    return ' '.join(word[::-1] for word in text.split(' '))
################################################### OR########################################################


def backward_string_by_word(text: str) -> str:
    return ' '.join(map(lambda x: x[::-1], text.split(' ')))
################################################### OR########################################################


def backward_string_by_word(text: str) -> str:
    return ' '.join([i[::-1] for i in text.split(' ')])
################################################### OR########################################################
