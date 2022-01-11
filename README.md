# hhru-rby_refresh_resume
Just refresher for hh.ru/rabota.by

Скрипт для обновления резюме на сайтах hh.ru/rabota.by

Для того чтобы работал на rabota.by, просто поменяйте строки:

>__driver.get("https://hh.ru/account/login")__ на __driver.get("https://rabota.by/account/login")__
>__driver.get("https://hh.ru/applicant/resumes")__ на __driver.get("https://rabota.by/applicant/resumes")__

Для того чтобы всё работало автоматически, создайте задачу в cron через команду crontab -e.

Задайте правило 0 */4 * * * DISPLAY=0: python path/where/locate/script/hh.py и сохраните.
