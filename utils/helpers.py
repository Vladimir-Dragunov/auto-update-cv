import configparser
import getpass
import os
import sys
import chrome_ver
import wget
import platform
import re
import time
import zipfile
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

program_name = sys.argv[0]
directory_path = os.path.abspath(program_name + '/..')


def wait_for_element(driver, locator, timeout=10):
    wait = WebDriverWait(driver, timeout)
    return wait.until(ec.visibility_of_element_located(locator))


def get_elements_text(driver, locator):
    elements = driver.find_elements(*locator)
    return [element.text for element in elements]


def scroll_to_element(driver, locator):
    element = driver.find_element(*locator)
    driver.execute_script("arguments[0].scrollIntoView();", element)


class Chromedriver:

    def __init__(self):
        self.system = platform.uname().system
        self.chromedriver_path = {'Windows': '\\chromedriver.exe', 'Linux': '/chromedriver', 'Darwin': '/chromedriver'}
        self.chromedriver_zip = {'Windows': '\\chromedriver_win32.zip', 'Linux': '/chromedriver_linux64.zip',
                                 'Darwin': '/chromedriver_mac64.zip'}
        self.chromedriver_ver = {'Windows': '\\chromedriver.exe -v', 'Linux': '/chromedriver -v',
                                 'Darwin': '/chromedriver -v'}
        self.chromedriver_system_name = {'Windows': 'win32', 'Linux': 'linux64', 'Darwin': 'mac64'}

    def get_abs_dir(self):
        if self.system in self.chromedriver_path.keys():
            return directory_path + self.chromedriver_path[self.system]

    def get_version(self):
        if self.system in self.chromedriver_path.keys():
            return re.search(r'\d*\.\d*\.\d*\.\d*', os.popen(directory_path + self.chromedriver_ver[self.system])
                             .read()).group(0)

    def download_current_ver(self):
        if self.system in self.chromedriver_system_name.keys():
            wget.download(url=f'https://chromedriver.storage.googleapis.com/{chrome_ver.get_chrome_version()}'
                              f'/chromedriver_{self.chromedriver_system_name[self.system]}.zip')

    def unzip(self):
        if self.system in self.chromedriver_path.keys() and self.system in self.chromedriver_zip.keys():
            with zipfile.ZipFile(directory_path + self.chromedriver_zip[self.system], 'r') as zip_ref:
                zip_ref.extractall(directory_path)
            os.remove(directory_path + self.chromedriver_zip[self.system])
            os.chmod(directory_path + self.chromedriver_path[self.system], 0o755)
            print('Chromedriver is unzipped, let\'s start')


chromedriver = Chromedriver()


def chromedriver_checker():

    if os.path.exists(chromedriver.get_abs_dir()):
        print('\nChromedriver exist')
        time.sleep(1)
        print('Checking chromedriver version')
        time.sleep(1)
        if chromedriver.get_version() == chrome_ver.get_chrome_version():
            print(f'Chromedriver version is {chromedriver.get_version()} - Google Chrome version is '
                  f'{chrome_ver.get_chrome_version()}')
            print('All fine, let\'s start')
        if chromedriver.get_version() != chrome_ver.get_chrome_version():
            print('You are using an outdated or newer version of Google Chrome, the required for chromedriver version '
                  'is downloaded automatically')
            chromedriver.download_current_ver()
            time.sleep(2)
            chromedriver.unzip()
    else:
        print('Chromedriver is not exist, it will be downloaded automatically')
        chromedriver.download_current_ver()
        time.sleep(2)
        chromedriver.unzip()


def configurator():

    config = configparser.ConfigParser()

    def write_file():
        config.write(open(directory_path + '/config.ini', 'w'))

    if not os.path.exists(directory_path + '/config.ini'):
        config['SETTINGS'] = {
            'site_checked': 'false'
        }

        write_file()

    config.read(directory_path + '/config.ini')
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

        site_login_link, site_resume_link = url[number]

        config.set('SETTINGS', 'site_checked', 'true')
        config.set('SETTINGS', 'site_login_link', site_login_link)
        config.set('SETTINGS', 'site_resume_link', site_resume_link)
        config.set('SETTINGS', 'login', input_login)
        config.set('SETTINGS', 'password', input_password)
        with open('config.ini', 'w') as configfile:
            config.write(configfile)

    # variables from config.ini
    login = config['SETTINGS']['login']
    password = config['SETTINGS']['password']
    site_login = config['SETTINGS']['site_login_link']
    site_resume = config['SETTINGS']['site_resume_link']
    #
    return login, password, site_login, site_resume
