''' run apscheduler '''
# pylint: disable = missing-function-docstring, eval-used, invalid-name, redefined-outer-name, unused-import, line-too-long
import logging
import time
#from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.schedulers.background import BackgroundScheduler
# from apscheduler.jobstores.redis import RedisJobStore
from apscheduler.triggers.cron import CronTrigger
import redlock
from . import APP, jobs


#jobstores = {'default': RedisJobStore(host=APP.config.get('REDIS_HOST'), db=0)}
#SCHED = BlockingScheduler(jobstores=jobstores)
SCHED = BackgroundScheduler(daemon=True)
logging.getLogger('apscheduler').setLevel(logging.WARNING)


DLM = redlock.Redlock(APP.config.get('REDLOCK_CONN'), retry_count=3, retry_delay=0.2)


def schedule_jobs(job_name):
    try:
        my_lock = DLM.lock(job_name, 10000)
        if my_lock:
            job_path = f'jobs.{job_name}.queue()'
            eval(job_path)
            time.sleep(1)
            DLM.unlock(my_lock)
    except redlock.MultipleRedlockException as exc:
        logging.error(exc)


for job_name, crontab_regex in APP.config.get('JOBS_SCHEDULE').items():
    trigger = CronTrigger.from_crontab(crontab_regex)
    SCHED.add_job(schedule_jobs, trigger, args=[job_name], id=job_name, replace_existing=True, max_instances=1)
