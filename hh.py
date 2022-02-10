import time
from datetime import datetime
from config import *
from pyvirtualdisplay import Display
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

# set date and time in dd/mm/YY H/M/S
now = datetime.now()
date_cron = now.strftime("%d/%m/%Y %H:%M:%S")
#

# headless mode via pyvirtualdisplay
display = Display(visible=False, size=(800, 600))
display.start()
#

# login and password from config.py
Login = input_login_hh
Password = input_password

# setting path for web driver path and log path
chrome_service = Service(executable_path=crontab_chromedriver_path)
driver = webdriver.Chrome(service=chrome_service, service_log_path=crontab_chromedriver_log)
#

# set web page
driver.get("https://hh.ru/account/login")
driver.set_page_load_timeout(7)
#

# define button "login with password" and click
button_login = driver.find_element(By.CSS_SELECTOR, "button.bloko-link_pseudo[data-qa='expand-login-by-password']")
button_login.click()
time.sleep(5)
#

# define input login and send keys
input_login = driver.find_element(By.CSS_SELECTOR, "input[data-qa='login-input-username']")
input_login.send_keys(Login)
time.sleep(5)
#

# define input password and send keys
input_password = driver.find_element(By.CSS_SELECTOR, "input[data-qa='login-input-password']")
input_password.send_keys(Password)
time.sleep(5)
#

# define button "join"
button_submit = driver.find_element(By.CSS_SELECTOR, "button[data-qa='account-login-submit']")
button_submit.click()
time.sleep(5)
#

# set web page
driver.get("https://hh.ru/applicant/resumes")
driver.set_page_load_timeout(7)
#

# define resume refresh button
button_refresh = driver.find_element(By.CSS_SELECTOR, "button.bloko-link[data-qa='resume-update-button']")
#

if button_refresh.text == 'Поднимать автоматически' or button_refresh.text == 'Сделать видимым':
    print(date_cron, 'Time is not over!')
    driver.quit()
else:
    time.sleep(5)
    button_refresh.click()
    print(date_cron, 'All done!')
    driver.quit()
