import time

from selenium.webdriver.common.by import By
from utils.helpers import scroll_to_element


class ResumePage:

    def __init__(self, driver, resume_page_url):
        self.driver = driver
        self.resume_page = resume_page_url
        self.update_button = (By.XPATH, '//button[@data-qa="resume-update-button_actions"]')

    def load(self):
        return self.driver.get(self.resume_page)

    def update(self):
        button = self.driver.find_element(*self.update_button)
        time.sleep(10)
        scroll_to_element(self.driver, self.update_button)
        if button.text == 'Поднимать автоматически' or \
                button.text == 'Сделать видимым':
            print('Time is not over')
            self.driver.close()
            self.driver.quit()
        else:
            self.driver.find_element(*self.update_button).click()
            print('All done!')
