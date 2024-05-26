# a function is a named block of code that performs a specific action
num_1 = 10
num_2 = 20
result = num_1 + num_2
print(result)


def summ(num_1, num_2):  # function
    result = num_1 + num_2
    print(result)


summ(20, 30)  # function call
summ("Hello ", "World")
summ(num_2="Hello", num_1="World ")  # forcing a sequence of variables to be assigned


def hi():
    name = input("Please type your name:")
    age = int(input("Please type your age:"))
    print("Hello my name is " + name.title() + " I am " + str(age) + " y.o.")

hi()


name="Kolin"
age="30"
def new_hi(name,age):
    result = ("Hello my name is " + name.title() + " I am " + str(age) + " y.o.")
    return result
some_var=new_hi(name,age)
print(some_var)
