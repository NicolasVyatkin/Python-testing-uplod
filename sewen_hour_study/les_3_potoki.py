# Условные операторы

if True:
    print('if')
elif True:
    print('ilif')
else:
    print('else')

# Операторы сравнения
# == - равенство
# <=, >=, >, < - больше-меньще
# != - не равенство

###############################################################
x = 0

if x == 0:
    print('if')
elif x > 0:
    print('ilif')
else:
    print('else')
##############################################################
# or - выполниться при одном из услолвий
# and - все условия должны выполняться для работы кода
# not - if not x == 0: заменит на True False

x = input('Please enter your number ')
if x == 0:
    x = 1
    print('x was 0')
elif type(x) == type(5) or type(x) == type(5.5):
    print('x is OK')
else:
    x = 1
    print('x is with wrong type of data')

print(100 / x)
