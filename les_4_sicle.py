"""Sicles"""

# if True:
#     print('true')

"""While operator"""

x = 5  # counter variable

while x > 0:
    print(x)
    x -= 1
else:
    print('You counted to the ' + str(x))

"""Factorial of the number"""
# while True:
#     x = int(input('Please enter the number factorial of what you wanna find: '))
#     count = 0
#     y = 1
#
#     while count < x:
#         count += 1
#         y *= count
#     else:
#         print('Factorial of number '+str(x) +' is: '+ str(y))
#####################################################################################

x = ''

while len(x) < 5:
    y = input('Enter your data: ')
    if y == 'o':
        continue # пропуск одного оборота кода, не выполнит x += y при введении о
    if y=='l':
        print(x)
        break # прекращение цикла при введении l

    x += y
else:
    print(x)
print('Program is keep working')
