# Lesson 019 Working with exceptions. Try&Except design

a = int(input("Please enter the first number: "))
b = int(input("Please enter the second number: "))

try:
    result = int(a / b)

except ZeroDivisionError:
    result = 0
    print("You cant divide on 0!!")
print("Result of the dividing a by b: " + str(result))

# ZeroDivisionError
