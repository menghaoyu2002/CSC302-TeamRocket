#!/bin/sh

python -m gunicorn --chdir ./server --log-level=debug --bind localhost:5000 "app:create_app()" --reload
