# Lesson 012 For Loop

students = ["Kolin", "Taras", "Nastya", "Olga", "Vlad", "Sveta"]

for f in students:
    if f == "Kolin":
        var = "Engineer " + f
        print(var)
print("students[:3]")
for f in students[:3]:  # selection from list of elements
    print(f)

print("students[1:3]")
for f in students[1:3]:  # selection from list of elements
    print(f)
print("Количество символов в каждом элементе списка")
for f in students:  # selection from list of elements
    print(f + " - " + str(len(f)))
