#!/bin/sh

gunicorn --chdir ./server --bind localhost:5000 "app:create_app()" --reload
