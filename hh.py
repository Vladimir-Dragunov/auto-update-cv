import time

from pyvirtualdisplay import Display
from selenium import webdriver
from selenium.webdriver.common.by import By

display = Display(visible=0, size=(800, 600))
display.start()

Login = '' # Ваш логин
Password = '' # Ваш пароль

driver = webdriver.Firefox()
driver.get("https://rabota.by/account/login")

button_login = driver.find_element(By.CSS_SELECTOR, 'span.bloko-link-switch') # Вход с паролем
button_login.click()
time.sleep(5)

input_login = driver.find_element(By.CSS_SELECTOR, "input[data-qa='login-input-username']") # Внесение данных в поле логин
input_login.send_keys(Login)
time.sleep(5)

input_password = driver.find_element(By.CSS_SELECTOR, "input[data-qa='login-input-password']") # Внесение данных в поле пароль
input_password.send_keys(Password)
time.sleep(5)

button_submit = driver.find_element(By.CSS_SELECTOR, "button[data-qa='account-login-submit']") # Вход на сайт
button_submit.click()
time.sleep(5)

driver.get("https://rabota.by/applicant/resumes") # Переход на страницу с резюме

element = driver.find_element(By.CSS_SELECTOR, "button[data-qa='resume-update-button']") # Определение кнопки, для последующей работы с ней

if element.text == 'Поднимать автоматически': # Если кнопка имеет текст - Поднимать автоматически, то прерывается работа скрипта
    driver.close()
else:
    time.sleep(5)
    submit = driver.find_element(By.CSS_SELECTOR, "button[data-qa='resume-update-button']")  # Если кнопка не имеет текст - Поднимать автоматически, то кнопка прожимается и завершается работа скрипта
    submit.click()
    driver.close()

