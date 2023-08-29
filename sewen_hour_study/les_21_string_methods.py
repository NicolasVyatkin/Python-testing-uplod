"""4:30:22"""
s = 'some Text String'
print(s[0:6])  # string like a list has indexes
print('str' in s)
print(s.upper())
print(s.capitalize())
print(s.lower())
plase = 'D:/Java&JS/Floor/somefile.jpg'
plase2 = plase.replace('/', '\\')
print(plase2)
r = plase2.split('\\')
print(r[-1])

"""Practice"""

print('\nPractice parsing file\n')
q = open('textfortest.txt')
r1 = q.read()
list_znk = ['(', ')', '"', '\n']  # symbols that we need to delete
for i in list_znk:
    r1 = r1.replace(i, '')
print(r1)
r2 = r1.split()  # creates list from elements divided by space " "
print(r2)
new_text = '_*_'.join(r2)
print(new_text)
