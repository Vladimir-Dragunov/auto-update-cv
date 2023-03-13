import time
from selenium.webdriver.common.by import By


class LoginPage:

    def __init__(self, driver, login_page_url):
        self.driver = driver
        self.login_page = login_page_url
        self.expand_button = (By.CSS_SELECTOR, "button.bloko-link_pseudo[data-qa='expand-login-by-password']")
        self.login = (By.CSS_SELECTOR, "input[data-qa='login-input-username']")
        self.password = (By.CSS_SELECTOR, "input[data-qa='login-input-password']")
        self.login_button = (By.CSS_SELECTOR, "button[data-qa='account-login-submit']")

    def load(self):
        self.driver.get(self.login_page)

    def page_login(self, login, password):
        self.driver.find_element(*self.expand_button).click()
        time.sleep(5)
        self.driver.find_element(*self.login).send_keys(login)
        self.driver.find_element(*self.password).send_keys(password)
        self.driver.find_element(*self.login_button).click()
        time.sleep(5)
