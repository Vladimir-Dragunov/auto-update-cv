# Auto-update CV
Скрипт для автоматического обновления резюме на сайтах hh.ru / rabota.by

Работает на Windows / Linux / Mac OS

Зависимости:
1. __Selenium__
3. __Urllib3__

Необходимо внести данные в файле конфига config.py:
1. __input_login_hh__= 'you-login@email.com'
2. __input_password__= 'you-password'
3. __crontab_chromedriver_path__ = '/usr/bin/chromedriver' (для Windows 'X:/your-folder/chromedriver.exe')
4. __crontab_chromedriver_log__ = '/home/username/chromedriver.log' (для Windows 'X:/your-folder/chromedriver.log')

# Планировщики задач

**LINUX или MAC OS**

Вызовите cron через команду 
```
crontab -e
```

Задайте внизу условие и сохраните
```
*/40 * * * * /usr/bin/python3 -u /path/where/locate/script/hh.py >> /path/where/locate/log/crontab_chromedriver_error.log 2>&1
```

**WINDOWS**

Для Windows вам понадобится создать bat-файл.

В нём укажите директорию к бинарному файлу python и директорию куда загружен скрипт

```
C:\you-folder\python.exe C:\you-folder\hh-win.py
pause
```

![1](https://i.imgur.com/O5NF5Fa.png)
![2](https://i.imgur.com/jxcvidK.png)
![3](https://i.imgur.com/NnLALQV.png)
![4](https://i.imgur.com/lkPsGKs.png)
![5](https://i.imgur.com/04ewFOQ.png)
![6](https://i.imgur.com/6DIiBqd.png)
![7](https://i.imgur.com/WGE3UrE.png)

# hh.ru или rabota.by

Если хотите запускать скрипт для сайта rabota.by, замените строки адресов на:
```
driver.get("https://rabota.by/account/login")
```
```
driver.get("https://rabota.by/applicant/resumes")
```

__WARNING!__ : Не рекомендую убирать тайминги, т.к. вам подсунут captch-у или просто дропнут.
