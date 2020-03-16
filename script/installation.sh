#!/bin/bash

source venv/bin/activate

pip3 install flask

pip3 install flask_mysqldb

source ~/.bashrc

python3 app.py

gunicorn --workers=4 --bind=0.0.0.0:5000 app:app