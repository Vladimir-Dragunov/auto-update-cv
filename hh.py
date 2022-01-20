import time
import os

from pyvirtualdisplay import Display
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service

firefox_options = Options()

display = Display(visible=0, size=(800, 600))
display.start()

Login = os.environ['input_login_hh'] # Ваш логин
Password = os.environ['input_password'] # Ваш пароль

crontab_geckodriver_path = '/usr/bin/geckodriver'
crontab_geckodriver = '/home/dragunov/Logs/crontab_geckodriver.log' # Путь для лога
service = Service(executable_path=crontab_geckodriver_path, log_path=crontab_geckodriver) # Запуск бинарника
driver = webdriver.Firefox(options=firefox_options, service=service)

driver.get("https://rabota.by/account/login")
driver.set_page_load_timeout(7)

button_login = driver.find_element(By.CSS_SELECTOR, "button.bloko-link-switch[data-qa='expand-login-by-password']") # Вход с паролем
button_login.click()
time.sleep(5)

input_login = driver.find_element(By.CSS_SELECTOR, "input[data-qa='login-input-username']") # Внесение данных в поле логин
input_login.send_keys(Login)
time.sleep(5)

input_password = driver.find_element(By.CSS_SELECTOR, "input[data-qa='login-input-password']")  # Внесение данных в поле пароль
input_password.send_keys(Password)
time.sleep(5)

button_submit = driver.find_element(By.CSS_SELECTOR, "button[data-qa='account-login-submit']") # Вход на сайт
button_submit.click()
time.sleep(5)

driver.get("https://rabota.by/applicant/resumes") # Переход на страницу с резюме
driver.set_page_load_timeout(7)

element = driver.find_element(By.CSS_SELECTOR, "button[data-qa='resume-update-button']") # Определение кнопки, для последующей работы с ней

if element.text == 'Поднимать автоматически' or element.text == 'Сделать видимым': # Если кнопка имеет текст - Поднимать автоматически, то прерывается работа скрипта
    driver.quit()
else:
    time.sleep(5)
    submit = driver.find_element(By.CSS_SELECTOR, "button[data-qa='resume-update-button']")  # Если кнопка не имеет текст - Поднимать автоматически, то кнопка прожимается и завершается работа скрипта
    submit.click()
    driver.quit()
    
