#!/bin/bash

source venv/bin/activate

pip3 install flask

pip3 install flask_mysqldb

source ~/bashrc

python3 /var/lib/jenkins/workspace/"Pipeline 1"/app.py

