import os

site = input('Please enter the site you wanna wisit: ')

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
