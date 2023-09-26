# Just Fizz!
# You should write a function that will receive a positive integer and return: "Fizz" if the number is 
# divisible by 3 (3, 6, 9 ...) otherwise convert the given number to a string (2 -> "2").

# Input: An integer (int).

# Output: A string (str).

# Examples:

# assert checkio(15) == "Fizz"
# assert checkio(6) == "Fizz"
# assert checkio(10) == "10"
# assert checkio(7) == "7"

######################SOLUTION######################
def checkio(num: int) -> str:        
    if num % 3==0:
        r="Fizz"
    else:
        r=str(num)    
    return r

print("Example:")
print(checkio(3))
#########################OR#########################
def checkio(num: int) -> str:
    return ('Fizz', str(num))[bool(num%3)]
#########################OR#########################
def checkio(x):
    if x % 3:
        return str(x)
    else:
        return "Fizz"
