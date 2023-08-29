# список изменяемый тип данных

m = [1, 2, 7, 3, 5, 'f', [1, 2], ['d', 'g']]

print(m[-1]) #обращение к последнему элементу списка
print('Lengh in the list m ' +str(len(m)))
print('first list - '+str(m))
m[0]=1256# changing the list
print('chenged list - '+str(m))
m[0]=1256+m[3]# changing the list
print('chenged list - '+str(m))
m[1],m[2]=m[2],m[1]# changing the list
print('chenged list - '+str(m))
m=m*2# changing the list doubling
print('chenged list - '+str(m))

j=[[5,7],[10,55],['some ','text']]
n=list('string')#создание листа из символов слова
print(n)

k=list(range(1,99,15))#создание листа функцией range
print(k)
# создание нового списка без значения 31
m=[]
for i in k:
    if i ==31:
        continue
    m+=[i]
else:
    print(m)



