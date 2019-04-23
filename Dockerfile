# Dockerfile for Flask API

# use python base
FROM python:3

# leave the tag
MAINTAINER Art Naslednikau

# update and install distribution software
RUN apt-get update -y
RUN apt-get install -y curl

# store project path in environmental variable
ENV APP /app

# create and set the working directory
RUN mkdir $APP
WORKDIR $APP

# copy the project to the working dir
COPY . .

# install dependencies
#RUN pip install Pipfile
# Error response from daemon: OCI runtime create failed: container_linux.go:345: starting container process caused "exec: \"uwsgi\": executable file not found in $PATH": unknown.
RUN pip install -r requirements.txt

# make port available from host
EXPOSE 5000

# start the server
CMD [ "uwsgi", "--socket", "0.0.0.0:5000", "--processes", "1", "--threads", "8", "--protocol", "http", "-w", "wsgi"]