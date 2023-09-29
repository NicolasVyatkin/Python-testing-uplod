# # Bird Language
# Stephan has a friend who happens to be a little mechbird. Recently, he was trying to teach it how to speak
# basic language. Today the bird spoke its first word: "hieeelalaooo". This sounds a lot like "hello", but with
# too many vowels. Stephan asked Nikola for help and he helped to examine how the bird changes words. With the
# information they discovered, we should help them to make a translation module.

# The bird converts words by two rules:
# - after each consonant letter the bird appends a random vowel letter (l ⇒ la or le);
# - after each vowel letter the bird appends two of the same letter (a ⇒ aaa);
# Vowels letters == "aeiouy".
# example

# You are given an ornithological phrase as several words which are separated by white-spaces (each pair of
#                                                                                              words by one whitespace).
# The bird does not know how to punctuate its phrases and only speaks words as letters. All words are given in lowercase.
# You should translate this phrase from the bird language to something more understandable.

# Input: A bird phrase as a string (str).

# Output: The translation as a string (str).

# Examples:

# assert translate("hieeelalaooo") == "hello"
# assert translate("hoooowe yyyooouuu duoooiiine") == "how you doin"
# assert translate("aaa bo cy da eee fe") == "a b c d e f"
# assert translate("sooooso aaaaaaaaa") == "sos aaa"
# 1
# 2
# 3
# 4
# How it is used: This is a similar cipher to those used by children when they invent their own "bird" language.
# Now you will be ready to crack the code.

# Precondition: re.match("\A([a-z]+\ ?)+(?<!\ )\Z", phrase)
# A phrase always has the translation.

################################################ SOLUTION#####################################################
import functools
import re


def translate(text: str) -> str:
    VOWELS = "aeiouy "

    for c in VOWELS:
        text = text.replace(c*3, c)

    text = list(text)

    for i, c in enumerate(text):
        if c not in VOWELS:
            del text[i+1]

    return ''.join(text)


print("Example:")
print(translate("hieeelalaooo"))
################################################### OR########################################################
VOWELS = "aeiouy"


def translate(phrase):
    output = ""
    c = 0

    while c < len(phrase):
        output += phrase[c]
        if phrase[c] in VOWELS:
            c = c + 3
        elif phrase[c] == ' ':
            c = c + 1
        else:
            c = c + 2

    return output


################################################### OR########################################################
translate = functools.partial(re.sub, r"(\w)(\1\1|.)", r"\1")
################################################### OR########################################################


def translate(s): return s and s[0] + \
    translate(s[1+(s[0] != ' ')+(s[0] in 'aeiouy'):])


################################################### OR########################################################
VOWELS = "aeiouy"


def translate(phrase):
    phrase = list(phrase)
    # print(phrase)
    for x in range(len(phrase)):
        try:
            if phrase[x] not in VOWELS and phrase[x+1] in VOWELS and phrase[x] != ' ':
                phrase.pop(x+1)
        except IndexError:
            continue
    phrase = ''.join(phrase)

    for x in range(len(phrase)):
        try:
            if phrase[x] in VOWELS and phrase[x] == phrase[x+1] and phrase[x] == phrase[x+2]:
                phrase = phrase.replace(phrase[x]*3, phrase[x])
        except IndexError:
            continue
    return phrase
