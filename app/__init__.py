''' app initializer  '''
# pylint: disable=too-few-public-methods, wrong-import-position, cyclic-import, line-too-long
import os
from flask import Flask
from flask_rq2 import RQ


APP = Flask(__name__)
APP.config.from_pyfile('config.py')
RQ_CLIENT = RQ(APP)

from . import jobs, tasks, scheduler
scheduler.SCHED.start()
