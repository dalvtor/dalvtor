bash ./wait-for-it.sh --timeout=30 ${POSTGRES_HOST}:${POSTGRES_PORT}
python manage.py migrate
python manage.py runserver 0.0.0.0:8000