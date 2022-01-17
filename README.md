# hhru-rby_refresh_resume
Скрипт для обновления резюме на сайтах hh.ru / rabota.by

Работает на Windows / Linux(Ubuntu) / Mac OS

Для Windows, просто измените путь в переменной:
>__service = Service('/usr/bin/geckodriver')__ на __service = Service('C:\\Files\\geckodriver.exe')__

Библиотеки необходимые для работы скрипта:
1. __Selenium__
2. __PyVirtualDisplay__
3. __Urllib3__

Необходимо указать логин в переменную __Login = 'example@mail.com'__ и пароль __Password = 'qwerty123'__

Для того чтобы работал на rabota.by, просто поменяйте строки:

>__driver.get("https://hh.ru/account/login")__ на __driver.get("https://rabota.by/account/login")__
>__driver.get("https://hh.ru/applicant/resumes")__ на __driver.get("https://rabota.by/applicant/resumes")__

Для того чтобы всё работало автоматически, создайте задачу в cron через команду crontab -e.

Задайте условие */30 * * * * /usr/bin/python3.8 -u /path/where/locate/script/hh.py >> /path/where/locate/log/crontab_geckodriver_error.log 2>&1 и сохраните.
