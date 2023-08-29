"""Generator method"""
def file_parser():
    with open('test_file.txt', encoding='utf-8') as i:
        for j in i:
                        
            yield j

p=file_parser()
#z=(x.split('\\')[1] for x in h if '.com' in x)

for i in p:
    #if '\n' in i:
    z=i.replace('\n', ' ')

    k=z.split ('.')     
    print(k)