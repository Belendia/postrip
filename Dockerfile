FROM python:3.9-alpine

LABEL maintainer="Belendia Serda belendia@gmail.com"

RUN apt-get -q update && apt-get -qy install netcat

ENV PYTHONUNBUFFERED 1
ENV DJANGO_ENV dev
ENV DOCKER_CONTAINER 1

COPY . /code
#ADD ./ussd_be/requirements.txt /code/requirements.txt
RUN pip install poetry
RUN poetry install --no-dev

# RUN pip install -r /code/requirements.txt

WORKDIR /code/
RUN mv wait-for /bin/wait-for

EXPOSE 8880

RUN adduser --disabled-password --gecos '' webuser

CMD ["gunicorn", "config.wsgi", "0:8880"]