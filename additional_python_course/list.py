# Lesson 011 Lists
personal = ["Kolin", "Taras", "Nastya", "Olga"]
index = int(input("Please enter the index of the person: "))
print("You have choosed employee " + personal[index] + " with index " + str(index))

result = personal[0] + " and " + personal[3]
print(result + " - best employs")
####################################################################################
number = [1, 23, 12, 4]
result_num = number[0] + number[3]
print(result_num)

print(len(personal))  # number of elements in the list
print(personal[-1])  # accessing the last element of the list
print(personal[0:3])  # range of objects from zero to third not inclusive
print(personal[1:])  # range of objects from the first index to the end of the list

###################################################################################

personal.append("Vladislav")  # add new element to the end of the list
print(personal)

# # creation of the list that contains two prewious lists

# pn.append(personal)
# pn.append(number)
# or

pn = [personal, number]
print(pn)
