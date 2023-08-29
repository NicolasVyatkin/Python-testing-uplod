"""04:50:10"""
"""Finding exception - try-exept-finaly"""
while True:
    try:
        enter = float(input('Please enter your number: '))
        print(100 / enter)
        break
    except ValueError:
        print('You entered non numeral value!!!')
        # enter = float(input('Please enter your number: '))
    except ZeroDivisionError:
        print('Please enter non zero value!!!')
    else:
        print('Great, you have done it from the first try!!!)')  # it will work if break is comented
    finally:
        print('Finaly - It prints in any case ')
print('You have entered ', enter, ' number')
