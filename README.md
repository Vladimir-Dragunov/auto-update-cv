# hhru-rby_refresh_resume
Скрипт для обновления резюме на сайтах hh.ru / rabota.by

Работает на Windows / Linux(Ubuntu) / Mac OS

Библиотеки необходимые для работы скрипта:
1. __Selenium__
2. __PyVirtualDisplay__
3. __Urllib3__

Необходимо внести данные в файле конфига config.py:
1. __input_login_hh__= 'you-login@email.com'
2. __input_password__= 'you-password'
3. __crontab_chromedriver_path__ = '/usr/bin/chromedriver' (для Windows 'X:\\you-folder\chromedriver.exe')
4. __crontab_chromedriver_log__ = '/home/username/chromedriver.log' (для Windows 'X:\\you-folder\chromedriver.log')

Для того чтобы работал на rabota.by, просто поменяйте строки:

>__driver.get("https://hh.ru/account/login")__ на __driver.get("https://rabota.by/account/login")__
>__driver.get("https://hh.ru/applicant/resumes")__ на __driver.get("https://rabota.by/applicant/resumes")__

Для того чтобы всё работало автоматически, создайте задачу в cron через команду crontab -e.

Задайте условие */30 * * * * /usr/bin/python3.8 -u /path/where/locate/script/hh.py >> /path/where/locate/log/crontab_chromedriver_error.log 2>&1 и сохраните.
