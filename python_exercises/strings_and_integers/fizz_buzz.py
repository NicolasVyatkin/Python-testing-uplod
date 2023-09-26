# Fizz Buzz
# "Fizz buzz" is a word game we will use to teach the robots about division. Let's learn computers.

# You should write a function that will receive a positive integer and return:
# "Fizz Buzz" if the number is divisible by 3 and by 5;
# "Fizz" if the number is divisible by 3;
# "Buzz" if the number is divisible by 5;
# The number as a string for other cases.
# Input: An integer (int).

# Output: A string (str).

# Examples:

# assert checkio(15) == "Fizz Buzz"
# assert checkio(6) == "Fizz"
# assert checkio(10) == "Buzz"
# assert checkio(7) == "7"
# 1
# 2
# 3
# 4
# How it is used: Here you can learn how to write the simplest function and work with if-else statements.

# Precondition: 0 < number ? 1000

############################SOLUTION############################
def checkio(num: int) -> str:        
    if num%3==0 | num%5==0:
        r="Fizz Buzz"
    elif num%3==0:
        r="Fizz"
    elif num%5==0:
        r='Buzz'
    else:
        r=str(num)    
    return r


print("Example:")
print(checkio(15))
################################OR###############################
def checkio(number):
    if number % 15 == 0:
        return 'Fizz Buzz'
    if number % 5 == 0:
        return 'Buzz'
    if number % 3 == 0:
        return 'Fizz'
    return str(number)
################################OR###############################
checkio=lambda n:("Fizz "*(1-n%3)+"Buzz "*(1-n%5))[:-1]or str(n)
################################OR###############################
import numpy as np

def checkio(a):
    if (np.mod(a,5)==0)&(np.mod(a,3)==0):
        n="Fizz Buzz"
        print('lol')
    elif np.mod(a,3)==0:
        n="Fizz"
    elif np.mod(a,5)==0:
        n="Buzz"
    else:
        n=str(a)
    return n
