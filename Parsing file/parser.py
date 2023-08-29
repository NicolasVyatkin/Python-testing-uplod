def word_saver():
    q = open('file_to_search_in.txt')
    r1 = q.read()
    list_znk = ['(', ')', '"', ',', '.', '\n']  # symbols that we need to delete
    for i in list_znk:
        r1 = r1.replace(i, '')
    print(r1)
    r2 = r1.split()  # creates list from elements divided by space " "
    print(r2)
    return r2


def sentece_saver():
    q = open('file_to_search_in.txt')
    r1 = q.read()
    #list_znk = ['\n']  # symbols that we need to delete
    print(r1)
    #for i in list_znk:
        #r1 = repr(r1.replace(i, ' ').split('.'))
    r1 = repr(r1.split('\n'))
    r1=r1.replace('\\', '')
    print(r1)
    print(str(type(r1)))
    return r1




# def to_raw(string):
#     return fr"{string}"

def cleaner(some_list):
    #some_list[i] = [w.replace(r'\'', '') for w in some_list]
    print("Original list_1: ", some_list)
    dict_1 = {'King': 'G', '\\\\': 'n'}
    for i in range(len(some_list)):
        if some_list[i] in dict_1:
            some_list[i] = dict_1[some_list[i]]
    print("Updated list_1: ", some_list)

#cleaner(sentece_saver())

def text_finder_in_string(some_list):
    text = input('Please enter text you wanna find: ')
    count = 0
    test = some_list.find(text)
    print(test)

def text_finder_in_list_of_strings(some_list):
    entered_text = str(input('Please enter text you wanna find: '))
    res = 0
    for i in some_list:
        resultant_str = [x for x in entered_text if(x in i)]
        print(resultant_str)

#sentece_saver()

text_finder_in_string(sentece_saver())
# print(text_finder(word_saver()))
#print(text_finder(sentece_saver()))

# text_saver()
