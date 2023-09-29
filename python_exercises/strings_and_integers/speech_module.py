# Speech Module
# Stephen's speech module is broken. This module is responsible for his number pronunciation.
# He has to click to input all of the numerical digits in a figure, so when there are big numbers it can take him
# a long time. Help the robot to speak properly and increase his number processing speed by writing a new speech
# module for him. All the words in the string must be separated by exactly one space character. Be careful with
# spaces - it's hard to see if you place two spaces instead one.

# Input: An integer (int).

# Output: A string (str).

# Examples:

# assert checkio(1) == "one"
# assert checkio(2) == "two"
# assert checkio(3) == "three"
# assert checkio(4) == "four"
# 1
# 2
# 3
# 4
# How it is used: This concept may be useful for the speech synthesis software or automatic reports systems.
# This system can also be used when writing a chatbot by assigning words or phrases numerical values and having
# a system retrieve responses based on those values.

# Precondition:0 < number < 1000

################################################ SOLUTION#####################################################
FIRST_TEN = ["one", "two", "three", "four",
             "five", "six", "seven", "eight", "nine"]
SECOND_TEN = [
    "ten",
    "eleven",
    "twelve",
    "thirteen",
    "fourteen",
    "fifteen",
    "sixteen",
    "seventeen",
    "eighteen",
    "nineteen",
]
OTHER_TENS = [
    "twenty",
    "thirty",
    "forty",
    "fifty",
    "sixty",
    "seventy",
    "eighty",
    "ninety",
]
HUNDRED = "hundred"


def checkio(num: int) -> str:
    number_to_list = [int(item) for item in str(num)]
    print(number_to_list)
    text_number = ''
    for i in number_to_list:
        if number_to_list[-1] and len(number_to_list) == 1:
            text_number = FIRST_TEN[i-1]
        elif len(number_to_list) == 2 and number_to_list[0] == 1:
            text_number = SECOND_TEN[num-10]
        elif len(number_to_list) == 2 and number_to_list[1] == 0:
            text_number = OTHER_TENS[number_to_list[0]-2]
        elif len(number_to_list) == 2 and number_to_list[0] >= 2:
            text_number = OTHER_TENS[number_to_list[0]-2] + \
                ' '+FIRST_TEN[number_to_list[1]-1]
        elif len(number_to_list) == 3 and number_to_list[-1] == 0 and number_to_list[1] == 0:
            text_number = FIRST_TEN[number_to_list[0]-1] + ' ' + HUNDRED
        elif len(number_to_list) == 3 and number_to_list[1] == 0:
            text_number = FIRST_TEN[number_to_list[0]-1] + \
                ' ' + HUNDRED + ' '+FIRST_TEN[number_to_list[-1]-1]
        elif len(number_to_list) == 3 and number_to_list[-1] == 0:
            text_number = FIRST_TEN[number_to_list[0]-1] + \
                ' ' + HUNDRED + ' '+OTHER_TENS[number_to_list[1]-2]
        elif len(number_to_list) == 3 and number_to_list[1] == 1:
            text_number = FIRST_TEN[number_to_list[0]-1] + \
                ' ' + HUNDRED + ' '+SECOND_TEN[number_to_list[1]+1]
        elif len(number_to_list) == 3 and number_to_list[1] >= 2:
            text_number = FIRST_TEN[number_to_list[0]-1] + ' ' + HUNDRED + ' ' + \
                OTHER_TENS[number_to_list[1]-2]+' ' + \
                FIRST_TEN[number_to_list[-1]-1]
        else:
            text_number = 'One thousand'
    return text_number


print("Example:")
print(checkio(4))
################################################### OR########################################################
FIRST_TEN = ["one", "two", "three", "four", "five", "six", "seven",
             "eight", "nine"]
SECOND_TEN = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
              "sixteen", "seventeen", "eighteen", "nineteen"]
OTHER_TENS = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy",
              "eighty", "ninety"]
HUNDRED = "hundred"


def checkio(number):

    n = number // 100
    t = [FIRST_TEN[n-1], HUNDRED] if n > 0 else []

    n = (number // 10) % 10
    t += [OTHER_TENS[n-2]] if n > 1 else []

    n = number % (10 if n > 1 else 20)
    t += [(FIRST_TEN+SECOND_TEN)[n-1]] if n > 0 else []

    return ' '.join(t)
################################################### OR########################################################


def checkio(n, d=dict(enumerate(" one two three four five six seven eight nine ten eleven twelve".split(" ")))):
    def i(s, j=iter("o en ree ir ve f t ".split(" "))):
        for k in j:
            s = __import__("re").sub(k + "$", next(j), s)
        return s
    return (d[n//100]+" hundred "*(n > 99)+d.get(n % 100, n % 100 < 20 and i(d[n % 10])+"teen" or i(d[n//10 % 10]).replace("u", "")+"ty "+d[n % 10])).strip()


################################################### OR########################################################
FIRST_TEN = ["zero", "one", "two", "three", "four",
             "five", "six", "seven", "eight", "nine"]
SECOND_TEN = ["ten", "eleven", "twelve", "thirteen", "fourteen",
              "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
OTHER_TENS = ["twenty", "thirty", "forty", "fifty",
              "sixty", "seventy", "eighty", "ninety"]
HUNDRED = "hundred"

print(305 // 100)


def checkio(number):
    result = []
    if number >= 100:
        result.append(FIRST_TEN[number // 100] + " hundred")
    if (number % 100) // 10 > 1:
        result.append(OTHER_TENS[((number % 100) // 10) - 2])
    if (number % 100) // 10 == 1:
        result.append(SECOND_TEN[number % 10])
    elif (number % 10) > 0:
        result.append(FIRST_TEN[number % 10])

    return ' '.join(result)
