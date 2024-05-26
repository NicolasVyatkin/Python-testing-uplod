str_1="нello"
str_2="WORLD"

print(dir(str_1)) #displays in the console a list of all actions applicable to the current variable type

print(str_1.upper())# converts all characters to uppercase
print(str_1.title())# converts the first character to uppercase
print(str_2.lower())# converts all characters to lowercase

name = "Taras"
a= "Hello {}"
result = a.format(name)# passing a value to a pre-reserved area
print(result)

first_name = "Taras"
last_name = "Zincheko"
b= "Hello {} {}"
result_2 = b.format(first_name,last_name)# passing the value of two variables into a pre-reserved area
print(result_2)

result_3 = f'My name is {first_name} {last_name}'# f string notation
print(result_3)