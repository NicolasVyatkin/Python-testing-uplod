"""04:43:14"""
"""%s, .format, f-string"""

enter = input('Please enter your name: ')
print('Old method')
t = 'Hello %s, I am %s using method "%s"' % (enter, 'Python', '%s')
print(t + '\n')
print('Newer method .format')
f = 'Hello {1}, I am {0} using method ".format"'.format(enter, 'Python')
print(f + '\n')
print('Newest and fastest method f-string from Python 3.6 ')
var='some string'
d = f'Hello {enter}, I can do it in "f-string": summ 2+2={2 + 2} + {len(var)}'
print(d + '\n')
