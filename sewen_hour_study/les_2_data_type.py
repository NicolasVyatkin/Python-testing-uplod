def printer_for_var(a):
    print("Type of the variable - " + str(type(a)))


a = None
print("Type of the variable 'a = None' - " + str(type(a)))
a = 1
print("Type of the variable 'a = 1' - " + str(type(a)))
a = 1.0
print("Type of the variable 'a = 1.0' - " + str(type(a)))
a = 1 + 1j
print("Type of the variable 'a = 1 + 1j' - " + str(type(a)))
a = '1'
print("Type of the variable 'a = '1'' - " + str(type(a)))
a = [1, 1, 'a']
print("Type of the variable 'a = [1, 1, 'a']' - " + str(type(a)))
a = (1, 1, 'a')
print("Type of the variable 'a = (1, 1, 'a')' - " + str(type(a)))
a = {1, 1, 'a'}
print("Type of the variable 'a = {1, 1, 'a'}' - " + str(type(a)))
a = {'a': 1, 'b': 2}
print("Type of the variable 'a = {'a': 1, 'b': 2}' - " + str(type(a)))
a = True
print("Type of the variable 'a = True' - " + str(type(a)))

#############################################################################

x = float(input('Enter first number: '))
y = float(input('Enter second number: '))
r = x+y
print('Result: '+str(r))
