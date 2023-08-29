# функция закрытый блок кода, переменные в функции не видны в основной области видимости

print('Before function')

def show():
    print('Fynction that printed text')


def show_2():
    x = 7
    return x


show()  # starting function
y = show_2()

print('Number in function show_2 is ' + str(y))
z = show_2() + 9
print(z)

print('After function')
