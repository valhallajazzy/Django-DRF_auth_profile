# Реферальная система с возможностью авторизации по номеру телефона

В данном проекте реализованы: 

* Cистема регистрации/авторизации пользовтателей по номеру телефона.
![Screenshot](https://github.com/valhallajazzy/Django-DRF_referal_app/blob/main/pic/auth.png)

* Aутентификация по полученному 4х-значному коду в SMS.
![Screenshot](https://github.com/valhallajazzy/Django-DRF_referal_app/blob/main/pic/auth1.png)

* После аутентификации пользователя, ему предоставляется доступ к личному кабинету, в котором реализована  
реферальная система. Так же отображаются рефералы, которые воспользовались invite-кодом, данного аккаунта.
![Screenshot](https://github.com/valhallajazzy/Django-DRF_referal_app/blob/main/pic/referal_profile.png)

### Фронтенд общается по API с базой данных по адресам:

`api/sign_in/` - POST-запрос. Авторизация/регистрация пользовталей. {"phohe_number": "+7XXXXXXXXXX"}  
`api/sign_up/` - POST-запрос. Аутентификация пользователей. {"phohe_number": "+7XXXXXXXXXX", "code": <4x-значный int>}  
`api/invite_code/` - POST-запрос. Активация invite-кода. {"phohe_number": "+7XXXXXXXXXX", "friend_invite_code": "<6ти-значная строка>""}  
`api/get_profile/` - POST-запрос. Получение информации активного профия. {"phohe_number": "+7XXXXXXXXXX"}  
`api/logout/` - POST-запрос. Выход из системы. {"phohe_number": "+7XXXXXXXXXX"}  
`api/get_users/` - GET-запрос. Получение информации о всех пользователях.  

## Подготовка и запуск проекта
* Создаем файл `.env` в корневой директории проекта и указываем переменные:  
`DATABASE_NAME` - имя базы данных  
`DATABASE_USER` - пользователь базы данных  
`DATABASE_PASSWORD` - пароль базы данных  
`DATABASE_HOST` - хост базы данных  
`API_URL_DOMAIN` - домен для API без http:// или https:// (Например: `127.0.0.1:8001` или `google.com`)  
`ALLOWED_HOSTS` - домен для Django  

![Screenshot](https://github.com/valhallajazzy/Django-DRF_referal_app/blob/main/pic/avenv.png)

* Запускаем приложение и БД командой в docker-compose:
```console
$ docker-compose up -d
```
