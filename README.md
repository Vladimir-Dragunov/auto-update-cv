# hhru-rby_refresh_resume
Скрипт для обновления резюме на сайтах hh.ru / rabota.by

Работает на [Windows(hh.py-win)](https://github.com/Vladimir-Dragunov/hhru-rby_refresh_resume/blob/main/hh-win.py) / Linux(Ubuntu) / Mac OS
> ###### *Для подержки на Windows требуется актуальная версия Google Chrome

Библиотеки необходимые для работы скрипта:
1. __Selenium__
2. __PyVirtualDisplay__
3. __Urllib3__

Необходимо внести данные в файле конфига config.py:
1. __input_login_hh__= 'you-login@email.com'
2. __input_password__= 'you-password'
3. __crontab_chromedriver_path__ = '/usr/bin/chromedriver' (для Windows 'X:/your-folder/chromedriver.exe')
4. __crontab_chromedriver_log__ = '/home/username/chromedriver.log' (для Windows 'X:/your-folder/chromedriver.log')

Для того чтобы всё работало автоматически, создайте задачу в cron через команду crontab -e.

Задайте условие */40 * * * * /usr/bin/python3 -u /path/where/locate/script/hh.py >> /path/where/locate/log/crontab_chromedriver_error.log 2>&1 и сохраните.

Если хотите запускать скрипт для сайта rabota.by, поменяйте строки:

>__driver.get("https://hh.ru/account/login")__ на __driver.get("https://rabota.by/account/login")__
>__driver.get("https://hh.ru/applicant/resumes")__ на __driver.get("https://rabota.by/applicant/resumes")__

__WARNING!__ : Не рекомендую убирать тайминги, т.к. вам подсунут captch-у или просто дропнут.
