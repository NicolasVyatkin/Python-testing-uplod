x = 5  # global variable


def name():
    y = 10  # local variable
    print('Global variable - ' + str(x))
    return ('Local variable in function - ' + str(y))


h = name()
print(h)


def nane_2():
    x = 10
    print('Local variable in function - ' + str(x))


nane_2()


def nane_3():
    global x
    x = 100
    print('New value of he global variable - ' + str(x))


nane_3()
#############################################################
# Структурирование кода
x = 5


def name2():
    x = 1000
    return name3(x)


def name3(par):
    print(par)


name2()
############################################################
# Запуск функции в функции

x=5
def name4():
    x = 13
    def name5():
        nonlocal x # замена значения переменной в материнской функции
        x=133
        print('Function in function - '+str(x))
    name5()
    print('Function - '+str(x))
name4()
print('Global variable - ' + str(x))

