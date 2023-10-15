'''Configurating module'''
import pytest
from selenium import webdriver
from selenium.webdriver.chrome. service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture()
def driver():
    """function that adds driver"""
    driver_service = Service(ChromeDriverManager().install())
    driver_chrome = webdriver.Chrome(service=driver_service)
    driver_chrome.maximize_window()
    yield driver_chrome
    driver_chrome.quit()
