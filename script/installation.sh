#!/bin/bash

source venv/bin/activate

pip3 install flask

pip3 install flask_mysqldb

pip3 install pytest

pip3 install urllib3

pip3 install coverage

source ~/bashrc

python3 /var/lib/jenkins/workspace/"Pipeline 1"/app.py

