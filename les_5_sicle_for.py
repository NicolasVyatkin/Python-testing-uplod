"""Цыкл for"""
m = 'first line of the text a'
counter = 0
for f in m:
    if f == 't':
        continue # пропускает все буквы t
        print('There is ' + str(counter+1) + ' sumbols t in te line')
        counter += 1
    print(f)
    # if f == 'a':
    #     break
else:
    print('Sicle finished, there are ' + str(counter) + ' sumbols t in the line')

print('Program is continying running')
