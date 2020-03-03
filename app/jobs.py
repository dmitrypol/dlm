''' jobs '''
# pylint: disable = missing-function-docstring
import logging
import time
from . import RQ_CLIENT


@RQ_CLIENT.job()
def gen_report():
    time.sleep(1)
    logging.info('gen_report')


@RQ_CLIENT.job()
def import_data():
    time.sleep(1)
    logging.info('import_data')


@RQ_CLIENT.job()
def send_emails():
    time.sleep(1)
    logging.info('send_emails')


@RQ_CLIENT.job()
def update_cache():
    time.sleep(1)
    logging.info('update_cache')


@RQ_CLIENT.job()
def recur_payment():
    time.sleep(1)
    logging.info('recur_payment')
