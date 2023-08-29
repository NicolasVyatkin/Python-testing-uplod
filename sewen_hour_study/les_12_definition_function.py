# параметры и аргументы функций
def count_list(par, par2=False, count=0):
    # count=0
    if par2 == True:
        typ = type(par[0])
        for i in par:
            count += 1
        return ('There are ' + str(count) + ' elements in the list ' + str(par)), typ


    else:
        for i in par:
            count += 1
        return ('There are ' + str(count) + ' elements in the list ' + str(par))


j = [9, 8, 7, 6, 5, 4, 3]
print(count_list(j))

h = ['a', 'b', 'c']
print(count_list(h))

k = [9, 8, 7, 2, 8, 3]
print(count_list(k, count=-2))

h, p = count_list('some line', True)
print(str(h))
print(str(p))
