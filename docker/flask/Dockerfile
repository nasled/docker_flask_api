# Dockerfile for Flask API

# use python base
FROM python:3

# leave the tag
MAINTAINER Art Naslednikau

# update and install distribution software
RUN apt-get update -y
RUN apt-get install -y curl nano

# install dependencies
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# make port available from host
EXPOSE 5000

# set working dir
WORKDIR /app

# https://github.com/ufoscout/docker-compose-wait/
ADD wait /wait
RUN chmod +x /wait
