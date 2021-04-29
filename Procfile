release: python manage.py migrate --noinput
release: python manage.py collectstatic --noinput
web: gunicorn api.wsgi --log-file -