import sys

url_list = ['les_23_1_text.txt', 'les_23_2_text.txt', 'les_23_3_text.txt', 'les_23_41_text.txt']

list_defect = []
list_info = []
try:
    for url in url_list:
        try:
            r = open(url)
            #print('File: ', url, 'info in this file - ', r.read())
            list_info.append(r.read())
        except FileNotFoundError:
            #print('File ', url, 'is not found')
            list_defect.append(url)
            sys.exit()# exit from the program
            continue
finally:
    r=open('les_23_saved_info.txt','a')
    for i in list_info:
        r.write(i)
    r.write(str(list_defect))
    r.close()
    print('All info saved in les_23_seved_info.txt')




print(list_defect)
print(list_info)
