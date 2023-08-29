import os

while True:
    site = input('Please enter the site you wanna wisit or\nfinish if you wanna stop wisit sites: ')

    if site=='finish':
        print('You finished your internet session')
        break

    if 'https://' in site:
        os.system('start ' + site)
        print('if')
    elif 'www.' in site:
        site = 'https://' + site

        os.system('start ' + site)
        print('elif')
    else:
        site = 'https://www.' + site
        os.system('start ' + site)
        print('else')
