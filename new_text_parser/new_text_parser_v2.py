"""Info"""


def file_parser(text):
    with open(text, encoding='utf-8') as i:
        text = []
        text = repr(i.read().replace('\n', ''))
        text = text.replace('\\', '')
        # --text = repr(text.replace('\\', ' ').split(". "))
        # --for i in text:
        # --text = text.replace('\\', '')
        text2 = text.split('. ')
        return text2


p = file_parser('test_file.txt')  # ok

# print(next(p))

# for i in p:
#     #z=i.replace(' ', ' ')
#     print(i)

print(p[4])  # ok


def word_finder(some_list):
    text_to_find = input('Please enter the text you wanna find: ')
    counter = 0
    for i in some_list:
        if text_to_find in i:
            print(i)
            counter += 1
    print('Thehe are', counter, 'senteses in the file')


word_finder(p)

# text3 = input('Enter some thing: ')
# print(text3)

# s = p.split('. ')
# print(s[0])


# def count_big_letters(s):
#     counter = 0

#     for ch in s:
#         if ch.isupper():
#             counter += 1
#     return 'There are ', counter, ' big letters in the text'

# print(count_big_letters(p))


# def sentence_finder(s):
#     arr = []
#     text = 'He'
#     for i in s:
#         for j in i:
#             if j == text:
#                 arr.append(i)
#     return arr
# print(sentence_finder(p))


# def sentence_printer(p):
#     for i in p:
#         print(p[i]+'\n')
