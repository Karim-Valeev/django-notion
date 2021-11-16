# Платформа педагогических исследований

Отправка кода в ветку develop запускает развертывание на staging, в ветку master - на production.

## Запуск

- `python3 -m venv venv` - создать виртуальное окружение
- `source venv/bin/activate` - войти в виртуальное окружение 
- `pip install -r requirements.txt` - установка зависимостей
- `docker-compose up` - запуск базы данных PostgreSQL (вместо выполнения этой команды можно поднять базу данных другим
способом)
- `python src/manage.py migrate` - применить миграции
- `python src/manage.py runserver` - запуск сервера для разработки
- `pip3 install pre-commit && pre-commit install` - включение pre-commit hook для автоматического запуска линтера
- `npm ci` - установка зависимостей для сборки фронтенда
- `npm run watch` - слежение за исходниками фронтенда и автоматическая пересборка их
- `npm run build` - сборка исходников фронтенда
- `npm run cypress` - запуск cypress gui
- `npm run cypress-run` - запуск автотестов cypress

## Загрузка данных

- `python src/manage.py loaddata src/main/fixtures/*.json` - загрузка начальных данных
- `python src/manage.py loaddata src/main/fixtures/test/*.json` - загрузка тестовых данных
    - тестовый пользователь: `test@test.ru qwe123`

*Другой вариант начальных данных есть в файле `console.sql`*

## Просмотр верстки

Верстка находится в папке `src/frontend`. Чтобы ее посмотреть, нужно выполнить следующее
- `cd src/frontend` - переход в папку
- `npm ci` - установка зависимостей
- `gulp` - запуск сервера для разработки с автоматической пересборкой файлов

Во время реализации функционала код должен переноситься в Django-проект: верстка - в шаблоны,
стили - в `src/main/static/assets/scss`, скрипты - в `src/main/static/assets/js`,
картинки - в `src/main/static/assets/images/`.

## Release notes generator

Запуск:

1. Добавить в файл `.env` переменную `TRELLO_TOKEN` с токеном, который можно взять в веб-инспекторе в куке `token` на 
https://trello.com.
2. `pip install -r requirements.txt` - поставить зависимости
3. `python3 deploy/release_notes_generator.py` - запустить
