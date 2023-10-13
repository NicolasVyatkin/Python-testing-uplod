from save_to_file import save_to_file
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--ignore-certificate-errors")
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()
driver.get('https://www.olx.ua/')


def site_starter():
    search_field = driver.find_element(By.ID, "headerSearch")
    search_field.clear()
    search_field.send_keys('w123 капот')
    search_field.send_keys(Keys.RETURN)
    clicking_field = driver.find_elements(By.CLASS_NAME, 'css-rc5s2u')
    clicking_field_id = driver.find_elements(By.CLASS_NAME, 'css-1sw7q4x')
    ids = []  # list with IDs
    links = []  # list with links
    # code that creates dictionary with id : link to the advt with this id
    for i in clicking_field:
        advt_link = i.get_attribute('href')
        links.append(advt_link)
    for i in clicking_field_id:
        advt_id = i.get_attribute('id')
        ids.append(advt_id)
    advt_dictionary = dict(zip(ids, links))  # dictionary id : links
    # code that creates dictionary with id : text in the advt with this id
    counter = 1
    text_list = []
    for site in links:
        if counter <= 3:
            driver.get(site)
            text_field = driver.find_element(
                By.XPATH, '//*[@id="mainContent"]/div[3]/div[3]/div[1]/div[2]/div[4]/div').text
            counter += 1
            text_list.append(text_field.replace('\n', ' '))
    # dictionary id : text in the advt with this id
    text_with_id = dict(zip(ids, text_list))
    return text_with_id


save_to_file(site_starter())
