release: python3 src/manage.py migrate
web: cd src && gunicorn django_notion.wsgi --log-file -
