# Lesson 015 Working with dictionaries and sets

# List - prints all objects exactly as in the list
print("List")
family_1 = ["Kolin", "Taras", "Nastya", "Kolin", "Olga", "Vlad", "Sveta"]
print(family_1)

# sets - prints only unique objects, prints in random order
print("sets")
family_2 = {"Kolin", "Taras", "Nastya", "Kolin", "Olga", "kolin", "Vlad", "Sveta"}
print(family_2)

# dictionary (key:value)
print("dictionary (key:value)")
family_3 = {"Dad": "Kolin", "Ukrainian": "Taras", "Son": "Vlad", "Mom": "Sveta"}
print(family_3["Dad"])

# Looping through a dictionary for
print("Looping through a dictionary for")
for v, k in family_3.items():
    print(v + " - " + k)
