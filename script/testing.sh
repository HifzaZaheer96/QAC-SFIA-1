#!/bin/bash
source  ~/bashrc
source /var/lib/jenkins/workspace/"Pipeline 1"/venv/bin/activate
coverage run -m pytest ./test/testing.py
coverage report

# source  ~/bashrc
# /var/lib/jenkins/workspace/"Pipeline 1"/venv/bin/coverage run -m pytest /var/lib/jenkins/workspace/"Pipeline 1"/test/testing.py
# /var/lib/jenkins/workspace/"Pipeline 1"/venv/bin/coverage report 