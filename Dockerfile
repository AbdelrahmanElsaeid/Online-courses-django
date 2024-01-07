# start docker with pthon 
FROM python:3.11.6-slim-bullseye
 

# setup linux python

ENV PYTHONUNBUFFERED = 1

# update linux kernal  & setup tools

RUN apt-get update && apt-get -y install gcc libpq-dev 

#folder project

WORKDIR /app

# copy 

COPY requirements.txt /app/requirements.txt

# install requirements

RUN pip install -r /app/requirements.txt

#copy project folder

COPY . /app/