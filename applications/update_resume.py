from pages.login_page import LoginPage
from pages.resume_page import ResumePage
from utils.driver import get_driver
from utils.helpers import configurator, chromedriver_checker


class UpdateResume:

    def __init__(self, login, password, login_url, resume_url):
        self.driver = None
        self.login_page = None
        self.resume_page = None
        self.login = login
        self.password = password
        self.login_url = login_url
        self.resume_url = resume_url

    def set_up(self):
        self.driver = get_driver(headless=False)
        self.login_page = LoginPage(self.driver, self.login_url)
        self.login_page.load()
        self.login_page.page_login(login=self.login, password=self.password)

    def update(self):
        self.resume_page = ResumePage(self.driver, self.resume_url)
        self.resume_page.load()
        self.resume_page.update()

    def tear_down(self):
        self.driver.close()
        self.driver.quit()


if __name__ == '__main__':
    chromedriver_checker()
    login, password, site_login, site_resume = configurator()
    update = UpdateResume(login, password, site_login, site_resume)
    update.set_up()
    update.update()
    update.tear_down()
