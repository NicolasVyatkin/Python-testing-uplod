"""06:10:37"""
"""Generators for lists, sets, dictionaries"""

h=[9,8,7,4,5,6,3,2,1,5,5,-2]

newh=[]
for x in h:
    if x%2==0:
        newh.append(x*2)
print(newh)

# """"List generator"""

# n=[x*2 for x in h]
# print(n)
# """"Set generator"""
# z={x*3 for x in h}
# print(z)
# """"Dictionary generator"""
# f={x:x*2 for x in h}
# print(f)

g=[x*2 for x in h if x%2==0 and x>0 ]
print(g)