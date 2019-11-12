python manage.py migrate
python manage.py collectstatic --noinput
gunicorn --workers=5 --bind 0.0.0.0:8000 vicmun.wsgi
