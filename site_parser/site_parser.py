"""Program that is looking for vacansy"""
import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

#Code for parsing olx.ua

URL_TEMPLATE = "https://www.olx.ua/zapchasti-dlya-transporta/avtozapchasti/kryachki/?currency=UAH"
FILE_NAME = "olx.csv"


def parse(url = URL_TEMPLATE):
    result_list = {'href': [], 'title': [], 'about': []}
    r = requests.get(url)
    print(r.status_code) #Service info
    print(r.text)
    with open('site_html_code_olx.html', 'w', encoding="utf-8") as file: #Saving html code of the site to html file
        file.write(r.text)    
    soup = bs(r.text, "html.parser")  #Finding and saving some elements from the site to the file
    vacancies_names = soup.find_all('h6', class_='css-16v5mdi er34gjf0')
    vacancies_info = soup.find_all('span', class_='css-1c0ed4l')
    #vacancies_names = soup.find_all('h2', class_='add-bottom-sm')
    #vacancies_info = soup.find_all('p', class_='overflow')
    for name in vacancies_names:
        result_list['href'].append('https://www.olx.ua'+name.a['href'])
        result_list['title'].append(name.a['title'])
    for info in vacancies_info:
        result_list['about'].append(info.text)
    return result_list


df = pd.DataFrame(data=parse())
df.to_csv(FILE_NAME)

#Code for parsing work.ua

# URL_TEMPLATE = "https://www.work.ua/jobs-odesa/?setlp=ua&page=2"
# FILE_NAME = "work.csv"


# def parse_work(url = URL_TEMPLATE):
#     result_list = {'href': [], 'title': [], 'about': []}
#     r = requests.get(url)
#     """Service info"""
#     print(r.status_code)
#     print(r.text)
#     """Saving html code of the site to html file"""
#     with open('site_html_code_work.html', 'w', encoding="utf-8") as file:
#         file.write(r.text)
#     """Finding and saving some elrments from the site to the file"""
#     soup = bs(r.text, "html.parser")
#     vacancies_names = soup.find_all('h2', class_='add-bottom-sm')
#     vacancies_info = soup.find_all('p', class_='overflow')
#     for name in vacancies_names:
#         result_list['href'].append('https://www.work.ua'+name.a['href'])
#         result_list['title'].append(name.a['title'])
#     for info in vacancies_info:
#         result_list['about'].append(info.text)
#     return result_list


# df_work = pd.DataFrame(data=parse_work())
# df_work.to_csv(FILE_NAME)