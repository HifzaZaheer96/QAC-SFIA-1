#!/bin/bash

sudo cp /var/lib/jenkins/workspace/"Pipeline 1"/script/flask.service /etc/systemd/system
sudo systemctl daemon-reload
sudo systemctl enable flask.service
sudo systemctl start flask.service


sleep 10

source  ~/.bashrc
/var/lib/jenkins/workspace/"Pipeline 1"/venv/bin/coverage run -m pytest /var/lib/jenkins/workspace/"Pipeline 1"/testing.py
/var/lib/jenkins/workspace/"Pipeline 1"/venv/bin/coverage report 