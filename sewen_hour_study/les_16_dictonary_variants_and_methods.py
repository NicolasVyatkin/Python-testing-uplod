d1 = {'a': 7}  # first way of creation dictionary
d1['b'] = 9  # adding new pare to the list d1
print('Basic dictionary d1 - ' + str(d1))
d1['a'] = 134  # changing by key
print('Changed dictionary by changing key "a" - ' + str(d1))
del d1['a']  # deleting by key
print('Changed dictionary by deleting key "a" - ' + str(d1))
#############################################################
d2 = dict(a=7)  # second way of creation dictionary
print('Basic dictionary d2 - ' + str(d2))
d4 = dict([['s', [10, 15, 20]], ['f', 4], ['g', 18]])  # one more way to use dict operator
print('Basic dictionary d4 - ' + str(d4))
#############################################################
d3 = dict.fromkeys([1, 2, 3, 4], ['dgd'])  # third way of creation dictionary
print('Basic dictionary d3 - ' + str(d3))
#############################################################
"""METHODS OF THE DICTIONARIES"""
d5 = dict([['a', 15], ['b', 25], ['c', 18], ['g', 55]])

d6 = d5.copy()  # creating new copy of the dictionary
print(d5.items())
print(d5.keys())
print(d5.values())
d5.update(d4)
print(d5)

users = {
    'Kolin': {'password': 87626, 'id': 16134},
    'Jimmy': {'password': 18226, 'id': 67867},
    'Bob': {'password': 324354, 'id': 16345}
}
print(users['Kolin']['password'])
############################################################
price = {'meat': 3, 'bread': 1, 'potato': 0.5, 'water': 0.2}


def buy():
    pay = 0
    while True:
        enter = str(input('What you wanna buy?\n'))
        if enter == 'end':
            break
        pay += price[enter]
    return pay


print('Your total price of the goods is - ' + str(buy()))
