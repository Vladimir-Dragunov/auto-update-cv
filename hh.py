import time
import configparser
import getpass
import os
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException

config = configparser.ConfigParser()

def write_file():
    config.write(open('config.ini', 'w'))

if not os.path.exists('config.ini'):
    config['SETTINGS'] = {
        'site_checked': 'false'
    }

    write_file()

config.read('config.ini')
site_check = config['SETTINGS']['site_checked']

if site_check == 'false':
    print('Выберите сайт: \n [1] - rabota.by \n [2] - hh.ru')

    url = {1: ('https://rabota.by/account/login', 'https://rabota.by/applicant/resumes'),
           2: ('https://hh.ru/account/login', 'https://hh.ru/applicant/resumes')}

    while True:
        try:
            number = int(input())
        except ValueError:
            print('Введите правильное значение')
            number = None
            continue

        if number in url.keys():
            break
        else:
            print('Введите правильно значение')

    input_login = input('Введите логин: ')
    input_password = getpass.getpass(prompt='Введите пароль: ')
    driver_path = input('Введите путь к chromedriver: ')
    log_path = input('Введите путь где будет лежать лог файл: ')

    site_login_link, site_resume_link = url[number]

    config.set('SETTINGS', 'site_checked', 'true')
    config.set('SETTINGS', 'site_login_link', site_login_link)
    config.set('SETTINGS', 'site_resume_link', site_resume_link)
    config.set('SETTINGS', 'login', input_login)
    config.set('SETTINGS', 'password', input_password)
    config.set('SETTINGS', 'driver_path', driver_path)
    config.set('SETTINGS', 'log_path', log_path)
    with open('config.ini', 'w') as configfile:
        config.write(configfile)


# set date and time in dd/mm/YY H/M/S
now = datetime.now()
date_cron = now.strftime("%d/%m/%Y %H:%M:%S")
#

# variables from config.ini
login = config['SETTINGS']['login']
password = config['SETTINGS']['password']
driver_path = config['SETTINGS']['driver_path']
log_path = config['SETTINGS']['log_path']
site_login = config['SETTINGS']['site_login_link']
site_resume = config['SETTINGS']['site_resume_link']
#

# chrome options
driver_options = webdriver.ChromeOptions()
driver_options.add_argument("no-sandbox")
driver_options.add_argument("--headless")
driver_options.add_argument("--disable-gpu")
driver_options.add_argument("--window-size=1920,1080")
driver_options.add_argument("--disable-extensions")
driver_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36")
#

# setting path for web driver path and log path
chrome_service = Service(executable_path=driver_path)
driver = webdriver.Chrome(service=chrome_service, service_log_path=log_path, options=driver_options)
#

# set web page
try:
    driver.get(site_login)
    driver.implicitly_wait(10)
except TimeoutException:
    print(date_cron, "Can't go on", site_login)
    driver.quit()
#

# define button "login with password" and click
try:
    button_login = driver.find_element(By.CSS_SELECTOR, "button.bloko-link_pseudo[data-qa='expand-login-by-password']")
    button_login.click()
    time.sleep(5)
except NoSuchElementException:
    print(date_cron, "Can't see button with expanded menu")
    driver.quit()
#

# define input login and send keys
try:
    input_login = driver.find_element(By.CSS_SELECTOR, "input[data-qa='login-input-username']")
    input_login.send_keys(login)
    time.sleep(5)
except NoSuchElementException:
    print(date_cron, "Can't see input with username")
    driver.quit()
#

# define input password and send keys
try:
    input_password = driver.find_element(By.CSS_SELECTOR, "input[data-qa='login-input-password']")
    input_password.send_keys(password)
    time.sleep(5)
except NoSuchElementException:
    print(date_cron, "Can't see input with password")
    driver.quit()
#

# define button "join"
try:
    button_submit = driver.find_element(By.CSS_SELECTOR, "button[data-qa='account-login-submit']")
    button_submit.click()
    time.sleep(5)
except NoSuchElementException:
    print(date_cron, "Can't see button login button")
    driver.quit()
#

# set web page
try:
    driver.get(site_resume)
    driver.implicitly_wait(10)
except TimeoutException:
    print(date_cron, "Can't go on", site_resume)
    driver.quit()
#

# define resume refresh button and execute
try:
    time.sleep(15)
    button_refresh = driver.find_element(By.XPATH, '//button[@data-qa="resume-update-button_actions"]')
    driver.execute_script("return arguments[0].scrollIntoView();", button_refresh)
except NoSuchElementException:
    print(date_cron, "Can't see refresh button")
    driver.quit()
finally:
    button_refresh = driver.find_element(By.XPATH, '//button[@data-qa="resume-update-button_actions"]')
    driver.execute_script("return arguments[0].scrollIntoView();", button_refresh)
    if button_refresh.text == 'Поднимать автоматически' or button_refresh.text == 'Сделать видимым':
        print(date_cron, 'Time is not over!')
        driver.quit()
    else:
        time.sleep(5)
        button_refresh.click()
        print(date_cron, 'All done!')
        driver.quit()
#
