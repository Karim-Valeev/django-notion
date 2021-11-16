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

