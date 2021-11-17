# REST API backend for react-notion project

## Запуск

- `python3 -m venv venv` - создать виртуальное окружение
- `source venv/bin/activate` - войти в виртуальное окружение 
- `pip install -r requirements.txt` - установка зависимостей
- `docker-compose up` - запуск базы данных PostgreSQL (вместо выполнения этой команды можно поднять базу данных другим
способом)
- `python src/manage.py migrate` - применить миграции
- `python src/manage.py runserver` - запуск сервера для разработки
- `pip3 install pre-commit && pre-commit install` - включение pre-commit hook для автоматического запуска линтера

## TokenAuthentication

- 'DEFAULT_AUTHENTICATION_CLASSES': ['rest_framework.authentication.TokenAuthentication'], in REST_FRAMEWORK in settings
- отправив в POST параметрах валидные email и password по урлу get_api_token_auth/ можно получить токен юзера
- вставляя токен в заголовки можно получить доступ к своим заметкам, например: curl -X GET http://127.0.0.1:8000/api/example/ -H 'Authorization: Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b'

## JWTAuthentication

- 'DEFAULT_AUTHENTICATION_CLASSES': ['rest_framework.authentication.JWTAuthentication'], in REST_FRAMEWORK in settings
- Каждые 10 минут для любой операции с API надо либо с помощью refresh_token либо с помощью email и password запрашивать access_token
