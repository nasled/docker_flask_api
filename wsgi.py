#!/usr/bin/python3

# uwsgi --socket 0.0.0.0:8000 --protocol=http -w wsgi

from api import app as application

if __name__ == "__main__":
    application.run()