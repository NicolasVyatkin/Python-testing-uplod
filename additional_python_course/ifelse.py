# Lesson 010 Conditional statements_ if, else, elif

age = 25
name = "Kolin"
if age == 25 and name == "Kolin":
    print("My name is " + name + " I am " + str(age) + " y.o. ")
elif age > 25:
    print("I'm more than " + str(age) + " y.o.")
else:
    print("I'm more than " + str(age) + " y.o.")

##############################################################################
if age == 23 or name == "Taras":
    print("My name is " + name + " I am " + str(age) + " y.o. ")
else:
    print("My name is " + name + " I am les than " + str(age) + " y.o.")

#############################################################################
# Условие по определённому символу/символам в переменной
name = "Kolin"
if "Kol" in name == "Kolin":
    print("My name is " + name)
else:
    print("My name is not " + name)
#############################################################################
# Банкомат
pin = 1234
print("Please enter your pin-code:")
user_pin = int(input())

if pin == user_pin:
    print("What summ you wanna receive:")
    summ = int(input())
else:
    print("Error, please enter correct pin-code. You have two tries")
    user_pin = int(input())
    if pin == user_pin:
        print("What summ you wanna receive:")
        summ = int(input())
    else:
        print("Error, please enter correct pin-code. You have one try")
        user_pin = int(input())
        if pin == user_pin:
            print("What summ you wanna receive:")
            summ = int(input())
        else:
            print("Error, your card is blocked. Please contact your bank")
