from header import *

program_name = sys.argv[0]
directory_path = os.path.abspath(program_name + '/..')


def clear_console():
    if os.name() == 'nt': # Windows
        os.system('cls')
    else: # Linux/Unix/MacOS
        os.system('clear')


class Chromedriver:

    def __init__(self):
        self.system = platform.uname().system
        self.chromedriver_path = {'Windows': '\\chromedriver.exe', 'Linux': '/chromedriver', 'Darwin': '/chromedriver'}
        self.chromedriver_zip = {'Windows': '\\chromedriver_win32.zip', 'Linux': '/chromedriver_linux64.zip',
                                 'Darwin': '/chromedriver_mac64.zip'}
        self.chromedriver_ver = {'Windows': '\\chromedriver.exe -v', 'Linux': '/chromedriver -v',
                                 'Darwin': '/chromedriver -v'}
        self.chromedriver_system_name = {'Windows': 'win32', 'Linux': 'linux64', 'Darwin': 'mac64'}

    def get_system(self):
        return self.system

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


chromedriver_checker()


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

# set date and time in dd/mm/YY H/M/S
now = dt.now()
date_cron = now.strftime("%d/%m/%Y %H:%M:%S")
#

# variables from config.ini
login = config['SETTINGS']['login']
password = config['SETTINGS']['password']
site_login = config['SETTINGS']['site_login_link']
site_resume = config['SETTINGS']['site_resume_link']
#


def executable_path():

    if os.uname().sysname == 'Windows':
        driver_path = directory_path + '\\chromedriver.exe'
        return driver_path
    else:
        driver_path = directory_path + '/chromedriver'
        return driver_path


# chrome options
driver_options = webdriver.ChromeOptions()
driver_options.add_argument("no-sandbox")
driver_options.add_argument("--headless")
driver_options.add_argument("--disable-gpu")
driver_options.add_argument("--window-size=1920,1080")
driver_options.add_argument("--disable-extensions")
driver_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                            "(KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36")
#

log_path = directory_path + '/log/hh.log'

# setting path for web driver path and log path
chrome_service = Service(executable_path=executable_path())
driver = webdriver.Chrome(service=chrome_service, service_log_path=log_path, options=driver_options)
#

# set web page
try:
    driver.get(site_login)
    driver.implicitly_wait(10)
    print(f'Going to site: {site_login}')
except TimeoutException:
    print(date_cron, "Can't go on", site_login)
    driver.close()
    driver.quit()
#

# define button "login with password" and click
try:
    button_login = driver.find_element(By.CSS_SELECTOR, "button.bloko-link_pseudo[data-qa='expand-login-by-password']")
    button_login.click()
    time.sleep(5)
    print('Finding expanded login')
except NoSuchElementException:
    print(date_cron, "Can't see button with expanded menu")
    driver.close()
    driver.quit()
#

# define input login and send keys
try:
    input_login = driver.find_element(By.CSS_SELECTOR, "input[data-qa='login-input-username']")
    input_login.send_keys(login)
    time.sleep(5)
    print('Finding login input')
except NoSuchElementException:
    print(date_cron, "Can't see input with username")
    driver.close()
    driver.quit()
#

# define input password and send keys
try:
    input_password = driver.find_element(By.CSS_SELECTOR, "input[data-qa='login-input-password']")
    input_password.send_keys(password)
    time.sleep(5)
    print('Finding password input')
except NoSuchElementException:
    print(date_cron, "Can't see input with password")
    driver.close()
    driver.quit()
#

# define button "join"
try:
    button_submit = driver.find_element(By.CSS_SELECTOR, "button[data-qa='account-login-submit']")
    button_submit.click()
    time.sleep(5)
    print('Finding login button')
except NoSuchElementException:
    print(date_cron, "Can't see button login button")
    driver.close()
    driver.quit()
#

# set web page
try:
    driver.get(site_resume)
    driver.implicitly_wait(10)
    print(f'Going to site {site_resume}')
except TimeoutException:
    print(date_cron, "Can't go on", site_resume)
    driver.close()
    driver.quit()
#

# define resume refresh button and execute
try:
    time.sleep(15)
    button_refresh = driver.find_element(By.XPATH, '//button[@data-qa="resume-update-button_actions"]')
    driver.execute_script("return arguments[0].scrollIntoView();", button_refresh)
except NoSuchElementException:
    print(date_cron, "Can't see refresh button")
    driver.close()
    driver.quit()
finally:
    button_refresh = driver.find_element(By.XPATH, '//button[@data-qa="resume-update-button_actions"]')
    driver.execute_script("return arguments[0].scrollIntoView();", button_refresh)
    if button_refresh.text == 'Поднимать автоматически' or button_refresh.text == 'Сделать видимым':
        print(date_cron, 'Time is not over!')
        driver.close()
        driver.quit()
    else:
        time.sleep(5)
        button_refresh.click()
        print('Clicking on button')
        clear_console()
        print(date_cron, 'All done!')
        driver.close()
        driver.quit()
#
