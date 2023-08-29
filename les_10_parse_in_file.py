import os
import time

"""('C:\\Users\\Колин\\Desktop\\Test folder', 
['Folder 1', 'Folder 2'], 
['71.jpg', 'drevo-zhiz.jpeg', 'images.jpeg', 'Text_3.txt', 'Text_4.txt'])"""

spisok = []

for addres, dirs, files in os.walk('C:\\Users\Колин\Desktop\Test folder'):
    #  заходит в каждую папку и выдаёт ёё содержимое в кортеж
    # spisok.append(addres) # список из каталогов
    # for file in files: # список из файлов
    #     spisok.append(os.path.join(addres, file))

    for file in files:
        full = os.path.join(addres, file)
        # if '.txt' in full: #запись всех файлов с расширением .txt
        if time.time() - os.path.getctime(full) < 86400: #запись всех файлов созданных в течении суток(86400 сек)
            spisok.append(full)
print(spisok)
