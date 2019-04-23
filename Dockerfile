# Dockerfile for Flask API

# use python base
FROM python:3

# leave the tag
MAINTAINER Art Naslednikau

# update and install distribution software
RUN apt-get update -y
RUN apt-get install -y curl nano

# add sources to and set the working directory
ADD . /app
WORKDIR /app

# install dependencies
RUN pip install pipenv
RUN pipenv install --system --deploy

# make port available from host
EXPOSE 5000
