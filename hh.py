import time
from datetime import datetime
from config import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException

# set date and time in dd/mm/YY H/M/S
now = datetime.now()
date_cron = now.strftime("%d/%m/%Y %H:%M:%S")
#

# login and password from config.py
Login = input_login_hh
Password = input_password

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
chrome_service = Service(executable_path=crontab_chromedriver_path)
driver = webdriver.Chrome(service=chrome_service, service_log_path=crontab_chromedriver_log, options=driver_options)
#

# set web page
url = ["https://rabota.by/account/login", "https://rabota.by/applicant/resumes"]
try:
    driver.get(url[0])
    driver.implicitly_wait(10)
except TimeoutException:
    print(date_cron, "Can't go on", url[0])
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
    input_login.send_keys(Login)
    time.sleep(5)
except NoSuchElementException:
    print(date_cron, "Can't see input with username")
    driver.quit()
#

# define input password and send keys
try:
    input_password = driver.find_element(By.CSS_SELECTOR, "input[data-qa='login-input-password']")
    input_password.send_keys(Password)
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
    driver.get(url[1])
    driver.implicitly_wait(10)
except TimeoutException:
    print(date_cron, "Can't go on", url[1])
    driver.quit()
#

# define resume refresh button and execute
try:
    time.sleep(15)
    button_refresh = driver.find_element(By.XPATH, '//button[@data-qa="resume-update-button"]')
except NoSuchElementException:
    print(date_cron, "Can't see refresh button")
    driver.quit()
finally:
    button_refresh = driver.find_element(By.XPATH, '//button[@data-qa="resume-update-button"]')
    if button_refresh.text == 'Поднимать автоматически' or button_refresh.text == 'Сделать видимым':
        print(date_cron, 'Time is not over!')
        driver.quit()
    else:
        time.sleep(5)
        button_refresh.click()
        print(date_cron, 'All done!')
        driver.quit()
#
