"""Methods"""
z = {1, 2, 15, 148, 3, 4, 56, 7, 8}
x = {1, 15, '3', '4', '6', '8', '2', '10'}
y = {1, 2, 3, 19, 126}

z.add(568)  # ads new unique element to the set(mnogestvo)
z.discard(2)  # removing element from the set without checking
# z.remove(228) # removing element from the set with error if there is no such element
z = z.union(x)  # unites two or more sets
# a = z.update(y)  # unites two or more sets
i = z.intersection(x)  # searching in x set for same elements in set z
d = z.difference(x)  # searching in x set for unique elements from set z

print(z)
print(i)
print(d)
