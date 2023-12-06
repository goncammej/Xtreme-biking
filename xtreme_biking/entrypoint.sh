#!/bin/sh
cd xtreme_biking/
cp local_settings.deploy.py local_settings.py
./manage.py collectstatic --noinput
gunicorn xtreme_biking.wsgi