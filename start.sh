#!/bin/bash
python manage.py collectstatic --noinput
python manage.py migrate --noinput
python fix_admin.py
gunicorn core.wsgi:application