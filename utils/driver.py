import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


def executable_path():

    if os.uname().sysname == 'Windows':
        driver_path = '../applications/chromedriver.exe'
        return driver_path
    else:
        driver_path = '../applications/chromedriver'
        return driver_path


def get_driver(headless=False):
    chrome_options = Options()
    chrome_service = Service(executable_path=executable_path())
    if headless:
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('no-sandbox')
        chrome_options.add_argument('--window-size=1920,1080')
        chrome_options.add_argument('--disable-extensions')
    driver = webdriver.Chrome(chrome_options=chrome_options, service=chrome_service)
    driver.implicitly_wait(10)
    return driver
