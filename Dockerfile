FROM python:3.8

LABEL maintainer="Buhari Abubakar"
LABEL description="This docker will install python and the required libraries"

ENV PYTHONDONTWRITEBYTECODE=1

ENV PYTHONUNBUFFERED=1

WORKDIR /code/

RUN apt-get update
RUN apt-get install default-jdk -y


COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt --no-cache-dir

COPY ./code ./code

COPY ./data/file ./data/file


CMD [ "python",  "./code/spark_read_csvd.py"]

# "./code/read_db_data.py", 