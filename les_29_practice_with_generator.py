"""06:43:56"""
# def some():
#     list_text=[]
#     with open('les_23_seved_info.txt', encoding='utf-8') as r:
#         for x in r:
#             list_text.append(x)
#     return list_text

# for i in some():
#     print(i.split())

"""Generator method"""
def some():
    with open('les_23_seved_info.txt', encoding='utf-8') as r:
        for x in r:
            yield x

p=some()
print(next(p))

for i in p:
    print(i)