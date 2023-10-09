# Words Order

# You have a text and a sequence of words. You need to check if the words in sequence appear in the
# same order as in the given text.

# Cases you should expect while solving this challenge:

# a word from the sequence is not in the text - your function should return False;
# any word can appear more than once in a text - use only the first one;
# two words in the given sequence are the same - your function should return False;
# the condition is case sensitive, which means 'hi' and 'Hi' are two different words;
# the text includes only English letters and spaces.
# Input: Two arguments. The first one is a given text as a string (str), the second is list of words as
# strings (str).

# Output: Logic value (bool).

# Examples:

# assert words_order("hi world im here", ["world", "here"]) == True
# assert words_order("hi world im here", ["here", "world"]) == False
# assert words_order("hi world im here", ["world"]) == True
# assert words_order("hi world im here", ["world", "here", "hi"]) == False

################################################ SOLUTION#####################################################
import re


def words_order(text: str, words: list) -> bool:
    text_list = text.split(' ')
    i = -1
    for word in words:
        if word in text_list and text_list.index(word) > i:
            i = text_list.index(word)
            continue
        return False
    return True
################################################### OR########################################################


def words_order(text, words):
    text_words = {w for w in text.split() if w in words}
    return list(sorted(text_words, key=text.index)) == words

################################################### OR########################################################


def words_order(text, words):
    return len(set(words)) == len(words) and \
        not not re.search(r'\b' + r'\b.*\b'.join(words) + r'\b', text)
################################################### OR########################################################


def words_order(text: str, words: list) -> bool:
    # A word that appears twice make this simple.
    if len(set(words)) != len(words):
        return False
    # Look for words indexes with a simple iteration on text words.
    words = {word: -1 for word in words}  # A dict remembers insertion order.
    for n, text_word in enumerate(text.split()):
        if text_word in words and words[text_word] == -1:
            words[text_word] = n
    # Make sure all words are in the text and indexes are increasing.
    last = -1
    for index in words.values():
        if index <= last:
            return False
        last = index
    return True
################################################### OR########################################################


def words_order(text: str, words: list) -> bool:
    # your code here
    import numpy as np
    text_split = text.split(" ")
    lg = len(words)

    count_list = np.array([text_split.count(x) for x in words])
    # print(count_list)
    if np.sum(count_list != 0) == lg:
        index_list = np.array([text_split.index(x) for x in words])
        # print(index_list)
        return np.sum(index_list == np.sort(index_list)) == lg\
            and len(np.unique(index_list)) == lg
    else:
        return False
