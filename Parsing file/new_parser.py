def sentece_saver():
    q = open('file_to_search_in.txt')
    r1 = q.read()
    print(r1)
    r1 = repr(r1.split('\n'))
    r1 = r1.replace('\\', '')
    print(r1)
    print(str(type(r1)))
    return r1


sentece_saver()
