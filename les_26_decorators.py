"""05:56:53"""
def decor(f):
    def wrapper(): # Обязательная форма для написания
        print('First decorated code')
        f()
        print('Second decorated code')
    return wrapper 

def error_finder(f):
    def wrapper(): # Обязательная форма для написания
        try:
            h=f()
        except Exception:
            print('Please enter number again')
            h=f()
        return h        
    return wrapper 

# @decor # make=decor(make)
# def make():
#     enter = input('Please enter something...')
#     print(enter)

#h=make
#h()
#make()
#######################Example########################
@error_finder
def make():
    enter = float(input('Please enter the number: '))
    return enter
@error_finder
def make2():
    enter = float(input('Please enter another one number: '))
    return enter

make2()
make()