"""Adding all info from files to one set"""
print()
new = set("Adding all info from files to one set")

r = open('text.txt')
# print(r.read().split())  # split - creating list, deletes all spaces and punctyation(, . : ; ! e.t.s.)
new.update(set(r.read().split()))  # creates set with unique elements
r.close()

r = open('text2.txt')
# print(r.read().split())  # split - creating list, deletes all spaces and punctyation(, . : ; ! e.t.s.)
new.update(set(r.read().split()))  # creates set with unique elements
r.close()

print(new)

"""Searching for un unique elements in two files"""
"""Using for tags and SEO optimization """
print("Searching for same elements between two files")
r = open('text.txt')
r1 = set(r.read().split())  # creates set with unique elements
r.close()

r = open('text2.txt')
r2 = set(r.read().split())  # creates set with unique elements
r.close()

new2 = r1.intersection(r2)
print(new2)
print("Searching for unique elements between two files")
new2 = r1.difference(r2)
print(new2)

