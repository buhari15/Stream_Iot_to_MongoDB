FROM python:3.8-slim

LABEL maintainer="Buhari Abubakar"
LABEL description="This docker will install python and the required libraries"

ENV PYTHONDONTWRITEBYTECODE=1

ENV PYTHONUNBUFFERED=1

WORKDIR /code/

RUN apt-get update && apt-get install -y default-jdk

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt --no-cache-dir


COPY --chown=1000:1000 ./code ./code
COPY --chown=1000:1000 ./data/file ./data/file

