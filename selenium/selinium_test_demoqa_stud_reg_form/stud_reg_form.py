from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


link_rozetka = 'https://rozetka.com.ua/ua/'
search_element = 'Ноутбуки Asus'

chrome_options = Options()
chrome_options.add_argument("--ignore-certificate-errors")
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
browser = webdriver.Chrome(options=chrome_options)
browser.maximize_window()
browser.get(link_rozetka)

search_field = browser.find_element(
    By.XPATH, "/html/body/app-root/div/div/rz-header/rz-main-header/header/div/div/div/form/div/div[1]/input")

search_field.clear()
search_field.send_keys(search_element)
# search_field.send_keys(Keys.RETURN)

search_button = browser.find_element(
    By.XPATH, '/html/body/app-root/div/div/rz-header/rz-main-header/header/div/div/div/form/button')
search_button.click()

compare_element = browser.find_element(
    By.XPATH, '/html/body/app-root/div/div/rz-category/div/main/div[1]/div/h1')

# print(compare_element.text)

if search_element == compare_element.text:
    print('Test OK')
else:
    print('Test failed')
