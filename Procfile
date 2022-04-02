release: python manage.py makemigrations
release: python manage.py migrate --run-syncdb
release: python manage.py runscript load_noun
web: python manage.py runserver 0.0.0.0:$PORT
