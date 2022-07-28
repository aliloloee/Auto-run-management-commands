FROM python:3.9-slim-buster 
LABEL MAINTAINER="Ali Loloee Jahromi"

ENV PYTHONUNBUFFERED 1

RUN mkdir /Nightmare
WORKDIR /Nightmare
COPY . /Nightmare

ADD requirements.txt /Nightmare
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

RUN python manage.py collectstatic --noinput
