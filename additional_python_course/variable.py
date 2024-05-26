# Lesson 9 Scope

var_1 = 10  # global variables
var_2 = 20  # global variables
print(var_1, var_2)


def summ():
    result = var_1 + var_2
    print(result)


print("Function with global variables: ")
summ()


def summ():
    var_1 = 30  # local variables
    var_2 = 40  # local variables
    result = var_1 + var_2
    print(result)


print("Function with local variables: ")
summ()


def sub():
    var_2 = 40
    result = var_1 - var_2
    print(result)


print("Function with global variables: ")
sub()
