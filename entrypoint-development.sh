./../wait_for_it.sh ${POSTGRES_HOST}:${POSTGRES_PORT} --timeout=30
python manage.py migrate
python manage.py runserver 0.0.0.0:8000