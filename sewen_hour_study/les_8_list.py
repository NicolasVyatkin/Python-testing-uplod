print('Practice block')

k = list(range(1, 21, ))  # создание листа функцией range
print('Basic list ' + str(k))
# создание списков чётных и не чётных чисел
b = k.copy()  # or b = k[::]or b = k[0::]
m = []
for i in k:
    if i % 2 == 0:
        m.append(i)
        k.remove(i)

else:
    print('Чётный лист ' + str(m))  # or b = k[1::2]
    print('Не чётный лист ' + str(k))  # or b = k[0::2]

##############################################################################################
print('Operator block')
x = [9, 8, 7, 6, 5, 7]
x.append(124)  # add element to the end of the list
x.insert(2, 15)  # add element to the list by index (2-index in the list)
print(x)
print('The are ' + str(x.count(7)) + ' elements 7 in the list')  # counts elements in the list
x.sort()  # sorting list
print(x)
x.reverse()  # reverse sorting list
print(x)
y = x.pop(2)  # deletes last element or element by index
print(y)
x.remove(15)  # removes element by name
print(x)
# x.clear() # removes everything from the list
# print(x)
x.extend(['a', 'b'])  # ads new variables to the list
print(x)
h = x.copy()  # copy list to new variable
print(h)
