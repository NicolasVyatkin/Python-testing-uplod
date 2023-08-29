"""06:52:02"""
from dis import dis
# def some(x):
#     return x/5
# print(some(7))
# print(dis(some))
######EQAL#####
# var = lambda x:x/5
# print(var(7))
# print(dis(var))

"""Lambda for list sort"""
list_of = [['Adam',29],['Jonny',3*1/12],['Jess',25]]
print('Sort method')
def s(x):
    return x[1]

r=sorted(list_of,key=s)
print('regular function ',r)

############OR##############

r=sorted(list_of, key=lambda x: x[1])
print('lambda function ',r)

"""Lambda for list filter"""

print('\n','Filter method with lambda function')
x=list(filter(lambda x: x[1]>18,list_of))
print(x)
