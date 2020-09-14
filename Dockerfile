FROM python:3.7-alpine

ENV PYTHONUNBUFFERED 1

# Install dependencies
COPY ./requirements.txt /requirements.txt
RUN apk add --update --no-cache postgresql-client
RUN apk add --update --no-cache --virtual .tmp-build-deps \
    gcc libc-dev linux-headers postgresql-dev
RUN pip install -r /requirements.txt
RUN apk del .tmp-build-deps

# Setup directory structure
RUN mkdir /cuenca_challenge
WORKDIR /cuenca_challege
COPY ./nqueen.py /cuenca_challege/
COPY ./tests.py /cuenca_challege/