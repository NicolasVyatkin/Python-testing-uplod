"""06:30:56"""
"""Expression Generators"""
import os

h=['https:\\www.site.com','https:\\www.somesite.com',
'https:\\www.someuselessite.com',
'https:\\www.littlesity.com','https:\\www.bigsite.net ']

# n=[x.split('\\')[1] for x in h if '.com' in x] # list generator
# print(n)
# print(type(n),'\n')

# z=(x.split('\\')[1] for x in h if '.com' in x) # expression generator

# не выгружается в память скопом так как список, а итерируется по одной переменной. Тем самым экономя память

# print(type(z),'\n')
# for i in z:
#     print(i)
print('start')
n=[x for x in os.walk('C:\\')]
print('here')
z=(x for x in os.walk('C:\\'))
print('there')
print(n.__sizeof__())
print(z.__sizeof__())