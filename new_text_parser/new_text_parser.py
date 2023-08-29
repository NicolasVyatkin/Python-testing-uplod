"""Generator method"""
def file_parser(text):
    with open(text, encoding='utf-8') as i:
        for j in i:
            r=j.replace('\n', ' ').split('.')
            #r=j.join('\n')

            yield r

p=file_parser('test_file.txt')
#print(next(p))

for i in p:
    #z=i.replace(' ', ' ')
    print(i)