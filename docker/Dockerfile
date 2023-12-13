from python:3.9-alpine

RUN apk add --no-cache git postgresql-dev gcc libc-dev
RUN apk add --no-cache gcc g++ make libffi-dev python3-dev build-base

WORKDIR /app

RUN git clone https://github.com/goncammej/Xtreme-biking.git .

WORKDIR /app/xtreme_biking

RUN pip install -r requirements.txt

# local settings.py
ADD docker-settings.py /app/xtreme_biking/local_settings.py



RUN ./manage.py collectstatic
