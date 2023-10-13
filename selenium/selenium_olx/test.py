import time
import json

from save_to_file import save_to_file

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


# driver = webdriver.Chrome()
# driver.add_virtual_authenticator('excludeSwitches', ['enable-logging'])
chrome_options = Options()
chrome_options.add_argument("--ignore-certificate-errors")
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()
driver.get('https://www.olx.ua/')


def site_starter():
    # clicking_times=0
    search_field = driver.find_element(By.ID, "headerSearch")
    search_field.clear()
    search_field.send_keys('w123 капот')
    search_field.send_keys(Keys.RETURN)
    clicking_field = driver.find_elements(By.CLASS_NAME, 'css-rc5s2u')
    clicking_field_id = driver.find_elements(By.CLASS_NAME, 'css-1sw7q4x')
    ids = []
    links = []

    # код который создаёт словарь id : ссылка на объявление по id
    for i in clicking_field:
        advt_link = i.get_attribute('href')
        links.append(advt_link)
    for i in clicking_field_id:
        advt_id = i.get_attribute('id')
        ids.append(advt_id)
    advt_dictionary = dict(zip(ids, links))  # словарь id : ссылки
    # print(advt_dictionary)
    # код который создаёт словарь id : текстовое наполнение объявления по id
    counter = 1
    text_list = []
    for site in links:
        if counter <= 3:
            driver.get(site)
            text_field = driver.find_element(
                By.XPATH, '//*[@id="mainContent"]/div[3]/div[3]/div[1]/div[2]/div[4]/div').text
            counter += 1
            text_list.append(text_field.replace('\n', ' '))
    # print(text_list[2])
    text_with_id = dict(zip(ids, text_list))  # словарь id : текст объявления
    # print(text_with_id)
    return text_with_id

# class that saves dictionary to file


# def save_to_file(some_dict):
#     with open('result-current_datetime.txt', 'w', encoding="utf-8") as file:
#         file.write(json.dumps(some_dict))

    # links_list =
    # while clicking_times<=4:
    #     i.click()
    #     time.sleep(5)
    #     clicking_times+=1
    #     driver.back()

    # clicking_field.click()
    # time.sleep(5)
    # clicking_times+=1
    # driver.back()
    # pass
    ########### OK##################################
    # ids = driver.find_elements(By.TAG_NAME,'h6')
    # d=[]
    # for e in ids:

    #     if len(d)<=2:
    #         text= e.text.encode()
    #         #print(text)
    #         #print('TEST')
    #         d.append(text)
    # print('Print d')
    # print(d)
    ########### OK##################################

    # print('TEST')
    # print(b'\xd1\x82\xd0\xb5\xd1\x81\xd1\x82\xd1\x82\xd0\xb5\xd1\x81\xd1\x82'.decode("utf-8"))

    # announcement_names = driver.find_elements(By.CLASS_NAME,'css-16v5mdi er34gjf0')
    # d=[]
    # for id, announcement_name in zip(ids, announcement_names):
    #     id = id.text
    #     announcement_name = announcement_name.text

    #     # print(id, announcement_name)
    #     d.append((id,announcement_name))
    #     print(d)

    # pass

# def save_to_dict():
#     site_starter()
#     #dict_to_save_in={id,announcement_name}

#     ids = driver.find_elements(By.TAG_NAME,'id')
#     announcement_names = driver.find_elements(By.CLASS_NAME,'css-16v5mdi er34gjf0')

#     for id, announcement_name in zip(ids, announcement_names):
#         id = id.text
#         announcement_name = announcement_name.text

#     print(id, announcement_name)


save_to_file(site_starter())
