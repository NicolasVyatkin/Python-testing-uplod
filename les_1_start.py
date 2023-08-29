number = 4
number = 5
number_2 = 8
result = number + number_2
print(result)

num_1 = num_2 = 5
print(num_1, num_2)

num1, num2 = 5, 7
print(num1, num2)

"""Обмен значениями"""
swap1 = 8
swap2 = 9
swap1, swap2 = swap2, swap1+swap2
print(swap1, swap2)

swap2=swap2-number
"""or"""
swap2-=number

"""Распаковка списка по переменным"""
#  * - arg
z,x,*c=[10,15,20,5,89]
print(z)
print(x)
print(c)

z,*x,c=[10,15,20,5,89]
print(z)
print(x)
print(c)

*z,x,c=[10,15,20,5,89]
print(z)
print(x)
print(c)
