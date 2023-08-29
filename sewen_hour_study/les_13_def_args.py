# переменное количество аргументов * - упаковывает переданные аргументы в кортеж

def name(g, h, *args, key):  # *args - обязательный формат не именованый аргумент;
    #  key - ключевые параметры после *args; g, h - именованные аргументы
    print(h)
    print(g)
    print(args)
    print(key)

name(7, 9, 8, 7, 9, key=10)

#######################################################################################

print('Metod that creates list with uniqe walues from any other lists')
def exclusive_item(*args, key=False):
    new_list=[]
    for i in args:
        for y in i:
            if y not in new_list:
                new_list.append(y)
    if key==True:
        new_list.sort()
    return new_list


z=[9,8,7]
x=[8,8,9,7,6,5]
c=[1,2,3,4,5,6,7,8]

t=exclusive_item(z,x,c, key=True)
print('First list: '+str(z))
print('Second list: '+str(x))
print('Third list: '+str(c))
print('List with all uniq walues: '+ str(t))
