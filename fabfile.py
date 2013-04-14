# -*- coding: utf-8 -*-
#
import os

from fabric import api


PROJECT_DIR = os.path.join(os.path.dirname(__file__), 'src/eukalypse_now')


def translations():
    """make and compile translations"""
    with api.lcd(PROJECT_DIR):
        api.local('python manage.py makemessages --all --no-wrap --no-location')
        api.local('python manage.py compilemessages')


def docs():
    """compile the documentation"""
    with api.lcd('docs'):
        api.local('make clean')
        api.local('make html')
