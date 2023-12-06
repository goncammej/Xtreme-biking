#!/bin/sh
cd xtreme_biking/
cp local_settings.deploy.py local_settings.py
gunicorn xtreme_biking.wsgi