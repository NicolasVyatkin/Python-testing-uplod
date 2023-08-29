"""Search for some thing enywere you want"""

x = 'qwertyuiopasdfghjklzxcvbnm'
y = input('Enter the symbol you wanna find: ')

for f in x:
    count = 0
    for r in y:
        if f == r:
            count += 1
    if count>0:
        print('There are ', count,  ' letters ',f, ' in line you printed')

"""range function for creation lists e.t.s."""

# for f in range(start,stop,step):
#     print(x)

for f in range(10,-20,-3):
    print(str(f))

