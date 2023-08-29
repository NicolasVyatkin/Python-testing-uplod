"""05:10:00"""
"""with-as context manager or try-finally construction"""

"""All data will be lost, because file was not close after ERROR"""
# try:
#     r = open('les_24_test.txt', 'a')
#     r.write('someting - 1' + '\n')
#     10/0
#     r.write('something - 2')
# finally:
#     r.close()
#
#     print('Everything is OK')

"""Data before ERROR will be saved, because because of using "with-as" context manager"""
r = 12
b = 'some string'


def withas():
    """Function that is better to use than try-finally"""
    with open('les_24_test.txt', 'a') as r:  # this is equal "r = open('les_24_test.txt', 'a')"
        r.write('someting - 1' + '\n')
        # 10 / 0
        r.write('something - 2')
        # "with-as" construction closes file automatically
    print('Everything is OK')


######################Element for imports in 25 lesson#########################

def informer(a):
    """Function that prints a massage"""
    print('I just print this massage and number ', a)


if __name__ == '__main__':  # check that stops starting code in file you import in
    informer(55)
    print(r)
