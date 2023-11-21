from python:3.10-alpine

RUN apk add --no-cache git postgresql-dev gcc libc-dev
RUN apk add --no-cache gcc g++ make libffi-dev python3-dev build-base

RUN pip install gunicorn
RUN pip install psycopg2
RUN pip install ipdb
RUN pip install ipython

COPY . /app/

WORKDIR /app/xtreme_biking

# Install Python dependencies
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# local settings.py
ADD ./docker/docker-settings.py /app/xtreme_biking/local_settings.py

RUN ./manage.py collectstatic
