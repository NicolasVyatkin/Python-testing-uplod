# Lesson 016 Working with files

# parameter "a" writes information to the end of the file
# parameter "w" writes new data and deletes old ones
# parameter "r" read from file

# print("Рworking with a parameter 'a'")
# var = input("Write some thing to save it to the file: ")
# fw = open("workwithfiles/file.txt", "a")
# fw.write("Hello people!!!!\n")
# fw.write(var+"\n")
# fw.close()
#
# print("working with a parameter 'w'")
# var_2 = input("Write some thing to save it to the file: ")
# fw_2 = open("workwithfiles/file2.txt", "w")
# fw_2.write("Hello people!!!!\n")
# fw_2.write(var+"\n")
# fw_2.close()

print("Read from file")
fr = open("workwithfiles/file.txt", "r")
text = fr.read()
fr.close()
print(text)
