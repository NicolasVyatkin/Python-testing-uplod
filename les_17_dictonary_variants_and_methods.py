price = {'meat': 3, 'bread': 1, 'potato': 0.5, 'water': 0.2}
# print('Basic prises - ' + str(price))
#
# new_price={}
# for i in price:
#     new_price[i] = round((price[i] * 0.85), 2)  # 15% discount
# print('Prises with discount 15% - ' + str(new_price))

###################################################################
print('First sickle')
for i in price.items():
    print(i, end='; ')
print('Second sickle')
new = {}
for key, value in price.items():  # switching pleases key and value
    print(key, end=' - ')
    print(value, end='; ')
    new[value] = key
print(new)
###################################################################
print('Third sickle')
for value in price.values():
    print(value, end='; ')
###################################################################
print('')
print('Forth sickle')
for keys in price.keys():
    print(keys, end='; ')

