''' app initializer  '''
# pylint: disable=too-few-public-methods, wrong-import-position, cyclic-import, line-too-long
import os
import logging
from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate


APP = Flask(__name__)
APP.config.from_pyfile('config.py')
# SQA = SQLAlchemy(APP)
# MIGRATE = Migrate(APP, SQA)

from . import tasks, routes
