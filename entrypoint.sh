#!/bin/sh
cd xtreme_biking/
cp local_settings.deploy.py xtreme_biking/settings.py
gunicorn xtreme_biking.wsgi