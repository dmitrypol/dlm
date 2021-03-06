''' config settings '''
# pylint: disable = line-too-long
import os
from logging.config import dictConfig

APP_NAME = os.environ.get('app_name')
HOME_DIR = os.environ.get('home_dir')
LOGS_DIR = f'{HOME_DIR}logs/'
TMP_DIR = f'{HOME_DIR}tmp/'
APP_ENV = os.environ.get('APP_ENV', 'dev')
SECRET_KEY = 'foobar'

REDIS_HOST = os.environ.get('REDIS_HOST')
REDLOCK_CONN = [
    {'host': REDIS_HOST, 'port': 6379, 'db': 2},
    {'host': REDIS_HOST, 'port': 6379, 'db': 3},
    {'host': REDIS_HOST, 'port': 6379, 'db': 4},
    ]
RQ_REDIS_URL = f'redis://{REDIS_HOST}:6379/1'

JOBS_SCHEDULE = {
    'gen_report':   '* * * * *',
    'send_emails':  '* * * * *',
    'recur_payment':'* * * * *',
    'import_data':  '* * * * *',
    'update_cache': '*/5 * * * *',
}

dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '{timestamp:%(asctime)s, level:%(levelname)s, module:%(module)s, lineno:%(lineno)d, %(message)s}',
    }},
    'handlers': {
        'file': {
            'level': 'INFO',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'formatter': 'default',
            'filename': f'{LOGS_DIR}{APP_NAME}-{APP_ENV}.log',
            'when': 'D',
            'interval': 1,
            'backupCount': 7
            }
        },
    'root': {
        'level': 'INFO',
        'handlers': ['file']
    }
})

if APP_ENV == 'test':
    pass
